from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Optional, Tuple
from src.models.question_answer import BookContentChunk, SourceReference
from src.config import Config
import logging


class RetrievalService:
    """
    Service to retrieve book content from Qdrant for each user query
    """

    def __init__(self):
        # Initialize Qdrant client with timeout
        self.client = QdrantClient(
            url=Config.QDRANT_URL,
            api_key=Config.QDRANT_API_KEY,
            timeout=Config.QDRANT_REQUEST_TIMEOUT,  # Use timeout from config
        )
        self.collection_name = Config.DEFAULT_COLLECTION_NAME
        self.relevance_threshold = Config.DEFAULT_RELEVANCE_THRESHOLD
        self.logger = logging.getLogger(__name__)

    def retrieve_relevant_chunks(
        self,
        query_text: str,
        book_id: Optional[str] = None,
        top_k: int = 5
    ) -> List[BookContentChunk]:
        """
        Retrieve relevant book content chunks based on the query text.

        Args:
            query_text: The text to search for in the vector database
            book_id: Optional filter to search only within a specific book
            top_k: Number of top results to return

        Returns:
            List of BookContentChunk objects that are relevant to the query
        """
        try:
            # Create a filter if book_id is specified
            filters = None
            if book_id:
                filters = models.Filter(
                    must=[
                        models.FieldCondition(
                            key="book_id",
                            match=models.MatchValue(value=book_id)
                        )
                    ]
                )

            # Perform vector search
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_text=query_text,
                limit=top_k,
                query_filter=filters,
                with_payload=True,
                with_vectors=False
            )

            # Convert search results to BookContentChunk objects
            # Only include chunks that meet the relevance threshold
            chunks = []
            for result in search_results:
                # Check if the score meets our relevance threshold
                score = result.score  # This is the similarity score from Qdrant
                if score < self.relevance_threshold:
                    self.logger.info(f"Skipping chunk with score {score} below threshold {self.relevance_threshold}")
                    continue

                payload = result.payload

                # Create BookContentChunk from the payload
                chunk = BookContentChunk(
                    id=payload.get("id", ""),
                    content=payload.get("content", ""),
                    book_id=payload.get("book_id", ""),
                    chapter=payload.get("chapter"),
                    page_number=payload.get("page_number"),
                    document_position=payload.get("document_position", 0),
                    embedding=[],  # Embedding might not be needed after retrieval
                    metadata=payload.get("metadata")
                )

                chunks.append(chunk)

            return chunks

        except Exception as e:
            self.logger.error(f"Error retrieving relevant chunks: {e}")
            raise

    def check_relevance_threshold(
        self,
        query_text: str,
        book_id: Optional[str] = None,
        threshold: Optional[float] = None
    ) -> bool:
        """
        Check if there are any chunks above the relevance threshold for a given query.

        Args:
            query_text: The text to search for in the vector database
            book_id: Optional filter to search only within a specific book
            threshold: Optional threshold to override the default

        Returns:
            True if there are chunks above the threshold, False otherwise
        """
        if threshold is None:
            threshold = self.relevance_threshold

        try:
            # Create a filter if book_id is specified
            filters = None
            if book_id:
                filters = models.Filter(
                    must=[
                        models.FieldCondition(
                            key="book_id",
                            match=models.MatchValue(value=book_id)
                        )
                    ]
                )

            # Perform a single result search to check the highest score
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_text=query_text,
                limit=1,
                query_filter=filters,
                with_payload=False,
                with_vectors=False
            )

            if search_results:
                highest_score = search_results[0].score
                return highest_score >= threshold
            else:
                return False

        except Exception as e:
            self.logger.error(f"Error checking relevance threshold: {e}")
            return False
    
    def create_source_reference(
        self,
        answer_id: str,
        chunk: BookContentChunk,
        relevance_score: float
    ) -> SourceReference:
        """
        Create a SourceReference from a BookContentChunk.

        Args:
            answer_id: The ID of the answer this reference is for
            chunk: The BookContentChunk that was used
            relevance_score: How relevant the chunk was to the question

        Returns:
            SourceReference object
        """
        # Create source location string
        location_parts = []
        if chunk.book_id:
            location_parts.append(chunk.book_id)
        if chunk.chapter:
            location_parts.append(f"Chapter {chunk.chapter}")
        if chunk.page_number is not None:
            location_parts.append(f"Page {chunk.page_number}")

        source_location = ", ".join(location_parts) if location_parts else "Unknown location"

        # Create more detailed citation information
        citation_parts = []
        if chunk.book_id:
            citation_parts.append(f'"{chunk.book_id}"')
        if chunk.chapter:
            citation_parts.append(f"Chapter {chunk.chapter}")
        if chunk.page_number is not None:
            citation_parts.append(f"p. {chunk.page_number}")

        citation = ", ".join(citation_parts) if citation_parts else "Source"

        # Validate that content snippet is actually part of the chunk content
        content_snippet = chunk.content if len(chunk.content) <= 200 else chunk.content[:200] + "..."

        # Ensure the content snippet is actually from the chunk (validation)
        if content_snippet not in chunk.content and len(chunk.content) > 0:
            # If not found, take the first 200 chars anyway as a fallback
            content_snippet = chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content

        return SourceReference(
            id=f"ref_{answer_id}_{chunk.id}",
            answer_id=answer_id,
            chunk_id=chunk.id,
            relevance_score=relevance_score,
            content_snippet=content_snippet,
            source_location=source_location,
            confidence_score=relevance_score,  # Use relevance as confidence
            page_reference=f"p. {chunk.page_number}" if chunk.page_number is not None else None,
            section_title=chunk.chapter if chunk.chapter else None,
            metadata=chunk.metadata
        )

    def calculate_source_reference_confidence(self,
                                            chunk: BookContentChunk,
                                            relevance_score: float,
                                            query_terms: List[str] = None) -> float:
        """
        Calculate a confidence score for a source reference based on various factors.

        Args:
            chunk: The BookContentChunk being referenced
            relevance_score: The vector similarity score
            query_terms: Terms from the original query to check against the content

        Returns:
            A confidence score between 0.0 and 1.0
        """
        # Start with the relevance score
        base_confidence = relevance_score

        # Adjust based on content length (longer content may be more reliable)
        length_factor = min(len(chunk.content) / 1000, 1.0)  # Normalize to max 1.0
        length_adjustment = 0.1 * length_factor  # Max 0.1 adjustment

        # Adjust based on presence of query terms (if provided)
        term_match_factor = 0.0
        if query_terms:
            content_lower = chunk.content.lower()
            matched_terms = sum(1 for term in query_terms if term.lower() in content_lower)
            term_match_factor = min(matched_terms / len(query_terms), 1.0) * 0.2  # Max 0.2 adjustment for term matching

        # Combine adjustments
        confidence = base_confidence + length_adjustment + term_match_factor
        # Ensure confidence doesn't exceed 1.0
        confidence = min(confidence, 1.0)

        return confidence

    def validate_source_reference_content(self, source_ref: SourceReference, chunk: BookContentChunk) -> bool:
        """
        Validate that the source reference content accurately represents the original chunk.

        Args:
            source_ref: The source reference to validate
            chunk: The original book content chunk

        Returns:
            True if the content is valid and accurate, False otherwise
        """
        try:
            # Check if the content snippet is part of the original chunk
            if source_ref.content_snippet not in chunk.content:
                # For very short content snippets, we allow partial matches
                if len(source_ref.content_snippet) < 20:
                    return source_ref.content_snippet in chunk.content
                return False

            # Additional validation could be added here as needed
            # For example: checking if key terms from snippet exist in original

            return True
        except Exception:
            # If validation fails due to an exception, return False
            return False