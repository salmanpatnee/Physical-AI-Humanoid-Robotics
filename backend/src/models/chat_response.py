from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .source_reference import SourceReference


class ChatResponse(BaseModel):
    """
    The response from the chatbot to a user query
    """
    id: str = Field(..., description="Unique identifier for the response")
    answer: str = Field(..., min_length=1, description="The main answer text from the chatbot")
    sources: List[SourceReference] = Field(..., min_length=1, description="Array of source references that support the answer")
    timestamp: datetime = Field(default_factory=datetime.now, description="When the response was generated")
    queryId: str = Field(..., description="Reference to the original query that generated this response")