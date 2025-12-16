from abc import ABC, abstractmethod
from typing import Protocol
import logging

from ..models.user_query import UserQuery
from ..models.chat_response import ChatResponse


logger = logging.getLogger(__name__)


class QueryProcessingService(Protocol):
    """
    Protocol defining the interface for query processing services
    """
    
    async def process_query(self, user_query: UserQuery) -> ChatResponse:
        """
        Process a user query and return a chat response with sources
        """
        ...


class MockQueryProcessingService:
    """
    Mock implementation of the QueryProcessingService for testing
    """
    
    async def process_query(self, user_query: UserQuery) -> ChatResponse:
        """
        Process a user query and return a mock chat response
        """
        logger.info(f"Processing query: {user_query.question}")
        
        # In a real implementation, this would:
        # 1. Send the query to the RAG system
        # 2. Include selected text context if provided
        # 3. Retrieve relevant sources from the book content
        # 4. Generate a response based on the content
        # 5. Return the response with proper sources
        
        # For now, return a mock response
        from ..models.chat_response import ChatResponse
        from ..models.source_reference import SourceReference
        
        mock_sources = [
            SourceReference(
                id="mock-source-1",
                title="Physical AI & Humanoid Robotics Book",
                url="https://example.com/book",
                contentPreview="This is a preview of the book content that was used to generate the answer...",
                confidence=0.92
            )
        ]
        
        response = ChatResponse(
            id=f"response-{user_query.id or 'temp'}",
            answer=f"This is a mock response for the question: '{user_query.question}'. " +
                   (f"The selected text was: '{user_query.selectedText}'." if user_query.selectedText else "") +
                   " In the actual implementation, this would be generated from the book content.",
            sources=mock_sources,
            queryId=user_query.id or "temp-query-id",
        )
        
        logger.info("Query processed successfully")
        return response