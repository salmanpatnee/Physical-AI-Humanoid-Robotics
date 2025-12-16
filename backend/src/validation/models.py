from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class SourceReference:
    """Information that links a content chunk back to its original location."""
    book_title: str
    chapter: str
    page_number: int
    section: str
    url: Optional[str] = None
    collection_name: Optional[str] = None  # Added for comprehensive source mapping
    document_id: Optional[str] = None  # Added to uniquely identify the source document
    content_hash: Optional[str] = None  # Added to verify content integrity
    vector_id: Optional[str] = None  # Added to track the specific vector in Qdrant
    original_content_length: Optional[int] = None  # Added for content validation


@dataclass
class ContentChunk:
    """A segment of text from a book that has been indexed in the vector database."""
    id: str
    content: str
    # vector_embedding: List[float]  # Omitting for now as we don't need to manipulate embeddings directly
    source_reference: SourceReference
    similarity_score: float
    position_in_result: int


@dataclass
class QueryRequest:
    """Represents a question or search request submitted by the developer for validation purposes."""
    id: str
    question: str
    expected_sources: Optional[List[str]] = None
    timestamp: datetime = datetime.now()
    module_context: Optional[str] = None


@dataclass
class Module:
    """A discrete collection of educational content in the vector database."""
    id: str
    title: str
    description: str
    total_chunks: int
    qdrant_collection_name: str
    validation_accuracy: float = 0.0  # Added to track module-specific validation accuracy
    last_validated: Optional[datetime] = None  # Added to track when module was last validated
    avg_latency: float = 0.0  # Added to track average response latency for this module
    tags: Optional[List[str]] = None  # Added for categorization and filtering
    vector_size: Optional[int] = None  # Added to store the size of vectors in this module
    metadata: Optional[Dict[str, Any]] = None  # Added for additional arbitrary metadata


@dataclass
class ValidationResult:
    """Captures the results of running a validation query."""
    id: str
    query_request_id: str
    retrieved_chunks: List[ContentChunk]
    relevance_score: float  # Overall relevance score (0-1)
    source_mapping_accuracy: float  # Accuracy of source reference mapping (0-1)
    latency_ms: float  # Time taken to retrieve results in milliseconds
    is_valid: bool  # Whether the result meets validation criteria
    feedback: str  # Human-readable feedback about the result quality