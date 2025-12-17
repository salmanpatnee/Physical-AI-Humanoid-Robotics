"""
Vercel Serverless Function for chatbot question answering.
Endpoint: /api/ask
"""
from http.server import BaseHTTPRequestHandler
import json
import sys
import os
from datetime import datetime
import time
import html
import re
import uuid

# Add backend source to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend', 'src'))

from services.retrieval_service import RetrievalService
from agents.book_agent import BookAgent
from models.question_answer import Question, Answer
from config import validate_environment

# Initialize services globally (reused across warm invocations)
retrieval_service = None
book_agent = None

def init_services():
    """Initialize services once for the serverless function"""
    global retrieval_service, book_agent
    if retrieval_service is None:
        retrieval_service = RetrievalService()
    if book_agent is None:
        book_agent = BookAgent()

def sanitize_input(input_text: str) -> str:
    """
    Sanitize user input to prevent injection attacks.

    Args:
        input_text: The input text to sanitize

    Returns:
        Sanitized version of the input text
    """
    if not input_text:
        return input_text

    # HTML escape
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

    return sanitized.strip()

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            start_time = time.time()

            # Validate environment on first request
            validate_environment()

            # Initialize services
            init_services()

            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))

            # Extract and sanitize request
            question = request_data.get('question', '').strip()
            book_id = request_data.get('book_id', '').strip() if request_data.get('book_id') else None
            selected_text = request_data.get('selected_text', '').strip() if request_data.get('selected_text') else None

            # Sanitize inputs
            question = sanitize_input(question)
            book_id = sanitize_input(book_id) if book_id else None
            selected_text = sanitize_input(selected_text) if selected_text else None

            # Validate question
            if not question or len(question.strip()) == 0:
                self.send_error(400, "Question cannot be empty")
                return

            if len(question) > 1000:
                self.send_error(400, "Question is too long (max 1000 characters)")
                return

            # Generate unique ID
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
            print(f"Processing question {question_id}: {question[:100]}")

            # Expand vague queries
            expanded_question = retrieval_service.expand_vague_query(question)

            # Retrieve relevant chunks (reduced from 5 to 3 for faster response)
            relevant_chunks = retrieval_service.retrieve_relevant_chunks(
                query_text=expanded_question,
                book_id=book_id,
                top_k=3
            )

            if relevant_chunks:
                print(f"Retrieved {len(relevant_chunks)} relevant chunks for question {question_id}")
            else:
                print(f"No relevant content found. Agent will use general knowledge.")

            # Extract content from chunks
            context_chunks = [chunk.content for chunk in relevant_chunks]

            # Generate answer
            answer = book_agent.generate_answer(
                question=user_question,
                context_chunks=context_chunks,
                source_references=[]
            )

            # Check if answer was generated
            if answer is None:
                print(f"Agent could not generate answer for question {question_id}")
                answer = Answer(
                    id=f"ans_{question_id}",
                    question_id=question_id,
                    content="I apologize, but I was unable to generate a response to your question. Please try rephrasing your question.",
                    confidence_score=0.0
                )

            # Create source references
            source_references = []
            if relevant_chunks:
                for chunk in relevant_chunks:
                    relevance_score = chunk.similarity_score if chunk.similarity_score is not None else 0.8
                    query_terms = question.split()
                    confidence_score = retrieval_service.calculate_source_reference_confidence(
                        chunk=chunk,
                        relevance_score=relevance_score,
                        query_terms=query_terms
                    )

                    source_ref = retrieval_service.create_source_reference(
                        answer_id=answer.id,
                        chunk=chunk,
                        relevance_score=confidence_score
                    )

                    if retrieval_service.validate_source_reference_content(source_ref, chunk):
                        source_references.append(source_ref)
                    else:
                        print(f"Source reference validation failed for chunk {chunk.id}")
            else:
                print(f"No sources available for question {question_id}")

            # Prepare response
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

            response_time = time.time() - start_time
            print(f"Successfully answered question {question_id} in {response_time:.2f} seconds")

            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', os.getenv('ALLOWED_ORIGIN', '*'))
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON in request body")
        except Exception as e:
            print(f"Error processing request: {str(e)}")
            import traceback
            traceback.print_exc()
            self.send_error(500, f"Internal server error: {str(e)}")

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', os.getenv('ALLOWED_ORIGIN', '*'))
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
