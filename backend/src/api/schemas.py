from pydantic import BaseModel
from typing import List, Optional
from ..models.user_query import UserQuery
from ..models.chat_response import ChatResponse
from ..models.source_reference import SourceReference


class QueryRequest(BaseModel):
    """
    Request schema for the chat query endpoint
    """
    question: str
    selectedText: Optional[str] = None


class QueryResponse(BaseModel):
    """
    Response schema for the chat query endpoint
    """
    answer: str
    sources: List[SourceReference]