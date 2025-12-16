from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserQuery(BaseModel):
    """
    Represents a question submitted by the user, optionally with selected text context
    """
    id: Optional[str] = Field(None, description="Unique identifier for the query")
    question: str = Field(..., min_length=1, description="The main question text entered by the user")
    selectedText: Optional[str] = Field(None, description="Optional text that the user has selected on the page")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now, description="When the query was submitted")
    userId: Optional[str] = Field(None, description="Identifier for the user making the request (for analytics)")
    
    class Config:
        # Allow extra fields for flexibility
        extra = "allow"