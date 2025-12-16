from fastapi import APIRouter, HTTPException
import logging

from ..models.user_query import UserQuery
from ..models.chat_response import ChatResponse

# Import the service for dependency injection
from ..services.query_service import MockQueryProcessingService

router = APIRouter()
logger = logging.getLogger(__name__)

# Initialize the query service
query_service = MockQueryProcessingService()

@router.post("/api/chat/query", response_model=ChatResponse)
async def chat_query_endpoint(
    user_query: UserQuery,
):
    """
    Endpoint to submit a query to the chatbot

    Args:
        user_query (UserQuery): The query from the user with optional selected text

    Returns:
        ChatResponse: The response from the chatbot with sources
    """
    try:
        logger.info(f"Received query: {user_query.question[:50]}...")

        # Basic validation
        if not user_query.question or not user_query.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        # Process the query using the service
        response = await query_service.process_query(user_query)

        logger.info("Successfully processed query")
        return response

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")