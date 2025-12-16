from abc import ABC, abstractmethod
from typing import Protocol
from ..models.user_query import UserQuery
from ..models.chat_response import ChatResponse


class ChatService(Protocol):
    """
    Protocol defining the interface for chat services
    """
    
    async def process_query(self, user_query: UserQuery) -> ChatResponse:
        """
        Process a user query and return a chat response with sources
        """
        ...