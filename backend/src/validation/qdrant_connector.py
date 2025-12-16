from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Optional, Dict, Any
from .models import ContentChunk, SourceReference, Module
from .config import Config
import logging
import time
from functools import wraps
import cohere
import os

logger = logging.getLogger(__name__)


def retry_on_failure(max_retries=3, delay=1, backoff=2):
    """
    Decorator to retry a function on failure.

    Args:
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):  # +1 to include the initial attempt
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt == max_retries:  # Last attempt
                        logger.error(f"Function {func.__name__} failed after {max_retries} retries: {str(e)}")
                        raise e
                    else:
                        logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}. Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff  # Exponential backoff

            return None
        return wrapper
    return decorator


class QdrantConnector:
    """Connector class to interface with the Qdrant vector database."""

    def __init__(self):
        self.config = Config()
        client_params = self.config.get_qdrant_client_params()

        if not self.config.validate_config():
            raise ValueError("Qdrant configuration is incomplete. Please check your .env file.")

        self.client = QdrantClient(**client_params)

        # Initialize Cohere client for embeddings
        cohere_api_key = os.getenv("COHERE_API_KEY")
        if not cohere_api_key:
            raise ValueError("COHERE_API_KEY is not set in environment variables")
        self.cohere_client = cohere.Client(cohere_api_key)
        
    @retry_on_failure(max_retries=3, delay=1, backoff=2)
    def search(
        self,
        query_text: str,
        collection_name: str,
        limit: int = 5,
        threshold: float = 0.5
    ) -> List[ContentChunk]:
        """
        Perform a vector search in the specified collection.

        Args:
            query_text: The text to search for
            collection_name: Name of the Qdrant collection to search in
            limit: Maximum number of results to return
            threshold: Minimum similarity score threshold

        Returns:
            List of ContentChunk objects representing the search results
        """
        try:
            # Generate embeddings using Cohere
            embed_response = self.cohere_client.embed(
                texts=[query_text],
                model='embed-english-v3.0',
                input_type='search_query'
            )
            query_vector = embed_response.embeddings[0]

            # Perform the search using query_points with the embedding
            search_results = self.client.query_points(
                collection_name=collection_name,
                query=query_vector,
                limit=limit,
                score_threshold=threshold
            )

            # Convert search results to ContentChunk objects
            content_chunks = []
            for idx, result in enumerate(search_results.points):
                # Extract payload information
                payload = result.payload

                # Create SourceReference from payload
                source_ref = SourceReference(
                    book_title=payload.get('book_title', 'Unknown'),
                    chapter=payload.get('chapter', 'Unknown'),
                    page_number=payload.get('page_number', 0),
                    section=payload.get('section', 'Unknown'),
                    url=payload.get('url', None)
                )

                # Create and append ContentChunk
                chunk = ContentChunk(
                    id=str(result.id),
                    content=payload.get('content', ''),
                    source_reference=source_ref,
                    similarity_score=result.score,
                    position_in_result=idx + 1
                )
                content_chunks.append(chunk)

            logger.info(f"Search completed: {len(content_chunks)} results found for query: '{query_text[:50]}...'")
            return content_chunks

        except Exception as e:
            logger.error(f"Error during Qdrant search: {str(e)}")
            raise
    
    @retry_on_failure(max_retries=3, delay=1, backoff=2)
    def get_available_collections(self) -> List[Module]:
        """
        Get a list of available collections in the Qdrant database.

        Returns:
            List of Module objects representing the available collections
        """
        try:
            collections = self.client.get_collections()
            modules = []
            
            for collection in collections.collections:
                # Get the count of points in the collection
                count_result = self.client.count(
                    collection_name=collection.name,
                    exact=True
                )
                
                # Create a module representation
                module = Module(
                    id=collection.name,  # Using collection name as the module ID
                    title=collection.name,  # Using collection name as title for now
                    description=f"Collection {collection.name} in Qdrant",
                    total_chunks=count_result.count,
                    qdrant_collection_name=collection.name
                )
                modules.append(module)
                
            logger.info(f"Retrieved {len(modules)} collections from Qdrant")
            return modules
            
        except Exception as e:
            logger.error(f"Error retrieving collections from Qdrant: {str(e)}")
            raise
    
    def verify_connection(self) -> bool:
        """
        Verify that the connection to Qdrant is working.

        Returns:
            True if the connection is successful, False otherwise
        """
        try:
            # Try to get the list of collections to verify the connection
            _ = self.client.get_collections()
            return True
        except Exception as e:
            logger.error(f"Qdrant connection verification failed: {str(e)}")
            return False

    def safe_search(self, query_text: str, collection_name: str, limit: int = 5, threshold: float = 0.5):
        """
        Safely perform a vector search with comprehensive error handling.

        Args:
            query_text: The text to search for
            collection_name: Name of the Qdrant collection to search in
            limit: Maximum number of results to return
            threshold: Minimum similarity score threshold

        Returns:
            List of ContentChunk objects or None if error occurs
        """
        try:
            return self.search(query_text, collection_name, limit, threshold)
        except Exception as e:
            logger.error(f"Error during Qdrant search in collection '{collection_name}': {str(e)}")
            # Return empty list instead of failing completely
            return []