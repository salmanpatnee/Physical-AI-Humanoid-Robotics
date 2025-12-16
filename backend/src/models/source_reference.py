from pydantic import BaseModel, Field
from typing import Optional


class SourceReference(BaseModel):
    """
    A reference to the source material used in the chat response
    """
    id: Optional[str] = Field(None, description="Unique identifier for the source")
    title: str = Field(..., min_length=1, description="Title or description of the source")
    url: Optional[str] = Field(None, description="URL to the source material (if applicable)")
    contentPreview: Optional[str] = Field(None, description="Brief preview of the relevant content from the source")
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0, description="Confidence level in the relevance of this source (0-1)")