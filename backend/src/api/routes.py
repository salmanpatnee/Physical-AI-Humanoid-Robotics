from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
import uuid
from datetime import datetime
import logging
import time
from collections import defaultdict
from typing import Dict

# Import models, services and agents
from ..models.question_answer import Question, Answer, SourceReference
from ..services.retrieval_service import RetrievalService
from ..services.caching_service import CachingService
from ..agents.book_agent import BookAgent
from ..config import Config, validate_environment

# Rate limiting storage
request_counts: Dict[str, List[float]] = defaultdict(list)
RATE_LIMIT_WINDOW = 60  # 60 seconds
MAX_REQUESTS_PER_WINDOW = 10  # 10 requests per minute per IP

# Create router
router = APIRouter()

# Initialize services
retrieval_service = RetrievalService()
book_agent = BookAgent()
caching_service = CachingService()

# Set up logger
logger = logging.getLogger(__name__)


def check_rate_limit(client_ip: str) -> bool:
    """
    Check if the client has exceeded the rate limit.

    Args:
        client_ip: IP address of the client

    Returns:
        True if within rate limit, False if exceeded
    """
    current_time = time.time()

    # Clean old requests outside the window
    request_counts[client_ip] = [
        req_time for req_time in request_counts[client_ip]
        if current_time - req_time < RATE_LIMIT_WINDOW
    ]

    # Check if the client is within the rate limit
    if len(request_counts[client_ip]) >= MAX_REQUESTS_PER_WINDOW:
        return False  # Rate limit exceeded

    # Add current request to the count
    request_counts[client_ip].append(current_time)
    return True


from pydantic import BaseModel
import html
import re


def sanitize_input(input_text: str) -> str:
    """
    Sanitize user input to prevent injection attacks and remove potentially harmful content.

    Args:
        input_text: The input text to sanitize

    Returns:
        Sanitized version of the input text
    """
    if not input_text:
        return input_text

    # Remove potentially dangerous scripts (basic check)
    # This is a simple sanitization - in production, consider using a dedicated library
    sanitized = html.escape(input_text)

    # Remove potential SQL injection patterns
    sql_patterns = [
        r"(?i)(union\s+select)",
        r"(?i)(drop\s+\w+)",
        r"(?i)(delete\s+from)",
        r"(?i)(insert\s+into)",
        r"(?i)(update\s+\w+\s+set)",
        r"(?i)(exec\s*\()",
        r"(?i)(execute\s*\()",
        r"(?i)(sp_)",
        r"(?i)('--)",
        r"(?i)(';)",
        r"(?i)(;--)",
        r"(?i)(;\s*exec)",
    ]

    for pattern in sql_patterns:
        sanitized = re.sub(pattern, "", sanitized)

    # Remove potential command injection characters
    sanitized = re.sub(r'[;&|$`]', ' ', sanitized)

    # Additional sanitization could be added based on specific requirements

    return sanitized.strip()


class QuestionRequest(BaseModel):
    question: str
    book_id: Optional[str] = None
    selected_text: Optional[str] = None

    class Config:
        # Allow extra fields for flexibility
        extra = "forbid"

@router.post("/ask",
             summary="Ask a question about book content",
             description="Submit a question about book content and receive a grounded answer based on retrieved information with source references.")
async def ask_question(request: QuestionRequest, request_obj: Request = None):
    """
    API endpoint to ask a question about book content and receive a grounded answer with source references.

    Args:
        request: QuestionRequest model containing the question and optional parameters
        request_obj: FastAPI Request object to access client information for rate limiting

    Returns:
        A JSON response containing:
        - answer: The generated answer to the question
        - sources: List of source references used to generate the answer
        - confidence_score: Overall confidence in the answer
        - timestamp: When the response was generated

    Raises:
        HTTPException: If the question is invalid, rate limit is exceeded, or no relevant content is found
    """
    start_time = time.time()

    # Get client IP for rate limiting
    client_ip = "127.0.0.1"  # Default value, will use actual IP if request_obj is provided
    if request_obj:
        client_ip = request_obj.client.host if request_obj.client else "127.0.0.1"

    # Check rate limit
    if not check_rate_limit(client_ip):
        logger.warning(f"Rate limit exceeded for IP: {client_ip}")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please try again later."
        )

    # Check cache first
    cached_response = caching_service.get(request.question, request.book_id)
    if cached_response:
        logger.info(f"Cache hit for question: {request.question[:50]}...")
        response_time = time.time() - start_time
        logger.info(f"Returned cached response in {response_time:.2f} seconds")
        return cached_response

    try:
        # Sanitize user inputs
        question = request.question.strip()
        book_id = request.book_id.strip() if request.book_id else None
        selected_text = request.selected_text.strip() if request.selected_text else None

        # Additional sanitization - remove potentially harmful characters/sequences
        question = sanitize_input(question)
        book_id = sanitize_input(book_id) if book_id else None
        selected_text = sanitize_input(selected_text) if selected_text else None

        # Pydantic already validates the question via the QuestionRequest model
        # but we can add additional custom validation here if needed
        if not question or len(question.strip()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Question cannot be empty"
            )

        if len(question) > 1000:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Question is too long (max 1000 characters)"
            )

        # Generate a unique ID for this question
        question_id = str(uuid.uuid4())

        # Create Question object
        user_question = Question(
            id=question_id,
            content=question,
            book_id=book_id,
            timestamp=datetime.now(),
            selected_text=selected_text
        )
        
        # Log the incoming question
        logger.info(f"Processing question {question_id}: {question}")
        
        # Retrieve relevant book content chunks
        relevant_chunks = retrieval_service.retrieve_relevant_chunks(
            query_text=question,
            book_id=book_id,
            top_k=5  # Retrieve top 5 relevant chunks
        )
        
        # Check if we have enough content to answer the question
        if not relevant_chunks:
            logger.warning(f"No relevant content found for question {question_id}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Cannot answer the question with available book content. No relevant content found."
            )
        
        logger.info(f"Retrieved {len(relevant_chunks)} relevant chunks for question {question_id}")
        
        # Extract content from chunks for the agent
        context_chunks = [chunk.content for chunk in relevant_chunks]
        
        # Generate the answer using the book agent
        answer = book_agent.generate_answer(
            question=user_question,
            context_chunks=context_chunks,
            source_references=[]  # We'll create these after getting the answer
        )
        
        # Check if the agent was able to generate an answer
        if answer is None:
            logger.warning(f"Agent could not generate answer for question {question_id} due to insufficient information")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Cannot answer the question with available book content. Insufficient information."
            )
        
        # Create source references for the answer using the actual similarity scores
        # For this, we need to perform the search again to get the similarity scores
        # since the retrieval_service.retrieve_relevant_chunks method filters results

        # Perform a new search to get the similarity scores for the response
        all_search_results = retrieval_service.client.search(
            collection_name=retrieval_service.collection_name,
            query_text=question,
            limit=5,  # Same as top_k in retrieve_relevant_chunks
            with_payload=True
        )

        source_references: List[SourceReference] = []
        for result in all_search_results:
            # Only create source reference if the chunk was in our filtered relevant chunks
            for chunk in relevant_chunks:
                if chunk.id == result.id:
                    # Calculate a proper confidence score for the source reference
                    query_terms = question.split()  # Simple approach to get query terms
                    confidence_score = retrieval_service.calculate_source_reference_confidence(
                        chunk=chunk,
                        relevance_score=result.score,
                        query_terms=query_terms
                    )

                    source_ref = retrieval_service.create_source_reference(
                        answer_id=answer.id,
                        chunk=chunk,
                        relevance_score=confidence_score  # Use calculated confidence as relevance
                    )

                    # Validate the source reference content accuracy
                    if retrieval_service.validate_source_reference_content(source_ref, chunk):
                        source_references.append(source_ref)
                    else:
                        logger.warning(f"Source reference validation failed for chunk {chunk.id}")

                    break  # Found the corresponding chunk, move to the next result

        # Prepare the response with proper formatting
        response = {
            "answer": answer.content,
            "sources": [
                {
                    "content_snippet": ref.content_snippet,
                    "source_location": ref.source_location,
                    "relevance_score": ref.relevance_score
                }
                for ref in source_references
            ],
            "confidence_score": answer.confidence_score or 0.8,
            "timestamp": datetime.now().isoformat()
        }
        
        # Cache the response for future requests
        caching_service.set(question, response, book_id=book_id)
        logger.info(f"Cached response for question: {question[:50]}...")

        # Calculate response time
        response_time = time.time() - start_time
        logger.info(f"Successfully answered question {question_id} in {response_time:.2f} seconds")
        return response

    except HTTPException as http_ex:
        # Calculate response time even for errors
        response_time = time.time() - start_time
        logger.warning(f"HTTP error {http_ex.status_code} for question in {response_time:.2f} seconds")
        # Re-raise HTTP exceptions as they are
        raise
    except Exception as e:
        # Calculate response time for unexpected errors
        response_time = time.time() - start_time
        logger.error(f"Error processing question in {response_time:.2f} seconds: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your question"
        )


@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify the service is running and dependencies are accessible.
    """
    # Check if environment variables are valid
    try:
        Config.validate_environment()
    except Exception as e:
        return {
            "status": "unhealthy",
            "timestamp": datetime.now().isoformat(),
            "error": str(e),
            "dependencies": {
                "openai_api": "error",
                "vector_database": "error"
            }
        }
    
    # Check if we can connect to Qdrant
    try:
        # Perform a simple operation to test Qdrant connection
        # We'll just list the collections to verify connectivity
        collections = retrieval_service.client.get_collections()
        qdrant_status = "connected"
    except Exception as e:
        logger.error(f"Qdrant connection error: {e}")
        qdrant_status = "error"
    
    # Check if we can connect to OpenAI
    try:
        # Perform a simple operation to test OpenAI connection
        # We'll just validate the key works by making a simple call
        import openai
        client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        client.models.list()
        openai_status = "connected"
    except Exception as e:
        logger.error(f"OpenAI connection error: {e}")
        openai_status = "error"
    
    # Determine overall status
    overall_status = "healthy" if (qdrant_status == "connected" and openai_status == "connected") else "unhealthy"
    
    return {
        "status": overall_status,
        "timestamp": datetime.now().isoformat(),
        "dependencies": {
            "openai_api": openai_status,
            "vector_database": qdrant_status
        }
    }