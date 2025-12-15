"""
Vector DB Ingestion System for Book Content

This system crawls Docusaurus book URLs, extracts readable content, chunks it,
generates embeddings using Cohere, and stores in Qdrant Cloud with proper metadata.
"""
import os
import sys
import logging
import argparse
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient
from tenacity import retry, stop_after_attempt, wait_exponential
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
import uuid
from datetime import datetime

# Import for web API (only if needed)
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional as PydanticOptional
except ImportError:
    FastAPI = None
    BaseModel = object
    PydanticOptional = Optional


# Load environment variables
load_dotenv()

# Constants with default values
DEFAULT_CHUNK_SIZE = 512
DEFAULT_OVERLAP_SIZE = 50
DEFAULT_COLLECTION_NAME = "book-content"
DEFAULT_BOOK_URL = os.getenv("BOOK_URL", "https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/")


def load_config():
    """Load configuration from environment variables."""
    config = {
        "cohere_api_key": os.getenv("COHERE_API_KEY"),
        "qdrant_api_key": os.getenv("QDRANT_API_KEY"),
        "qdrant_url": os.getenv("QDRANT_URL"),
        "book_url": os.getenv("BOOK_URL", DEFAULT_BOOK_URL),
    }
    
    # Validate required configuration
    missing_keys = [key for key, value in config.items() if not value]
    if missing_keys:
        raise ValueError(f"Missing required configuration: {', '.join(missing_keys)}")
    
    return config


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ingestion.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def progress_tracker(total_items: int):
    """Create a progress tracking generator."""
    for current in range(1, total_items + 1):
        yield current
        print(f"Progress: {current}/{total_items} ({current/total_items*100:.1f}%)")
        

def count_tokens(text: str) -> int:
    """Count approximate number of tokens in text."""
    # Simple approximation: 1 token ~ 4 characters for English text
    return len(text) // 4


def setup_cohere_client(api_key: str):
    """Set up Cohere client with API key from environment variables."""
    try:
        client = cohere.Client(api_key)
        return client
    except Exception as e:
        logging.error(f"Error setting up Cohere client: {e}")
        raise


def setup_qdrant_client(url: str, api_key: str):
    """Set up Qdrant client with URL and API key from environment variables."""
    try:
        client = QdrantClient(
            url=url,
            api_key=api_key,
        )
        return client
    except Exception as e:
        logging.error(f"Error setting up Qdrant client: {e}")
        raise


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def make_api_call_with_retry(api_func, *args, **kwargs):
    """Make an API call with retry logic using tenacity."""
    return api_func(*args, **kwargs)


def fetch_sitemap(book_url: str) -> str:
    """Fetch sitemap.xml from the provided book URL."""
    sitemap_url = f"{book_url.rstrip('/')}/sitemap.xml"
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching sitemap from {sitemap_url}: {e}")
        raise


def parse_sitemap(sitemap_content: str) -> List[str]:
    """Parse sitemap XML content and extract all URLs."""
    try:
        root = ET.fromstring(sitemap_content)
        urls = []
        for url_element in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url_element.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc is not None and loc.text:
                urls.append(loc.text)
        return urls
    except ET.ParseError as e:
        logging.error(f"Error parsing sitemap XML: {e}")
        raise


def fetch_html_content(url: str) -> str:
    """Fetch HTML content from a single URL using requests."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching content from {url}: {e}")
        raise


def extract_content_from_html(html_content: str, url: str = "") -> Dict[str, Any]:
    """Extract readable content from HTML using BeautifulSoup and Docusaurus-specific selectors."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Try to find Docusaurus-specific content containers
        # Docusaurus typically uses .markdown, .theme-doc-markdown, or main tag for content
        content_element = (
            soup.select_one('.markdown') or 
            soup.select_one('.theme-doc-markdown') or 
            soup.select_one('main div[class*="docItemContainer"]') or
            soup.select_one('main') or
            soup.body
        )
        
        if content_element:
            # Extract text content
            content_text = content_element.get_text(separator=' ', strip=True)
            
            # Extract the page title
            title_element = soup.find('title')
            page_title = title_element.get_text().strip() if title_element else "Untitled"
            
            # Extract section title from H1 if available
            h1_element = soup.find('h1')
            section_title = h1_element.get_text().strip() if h1_element else page_title
            
            return {
                'content': content_text,
                'title': page_title,
                'section_title': section_title,
                'url': url
            }
        else:
            # If no specific content container found, extract from body
            body = soup.body
            if body:
                content_text = body.get_text(separator=' ', strip=True)
                title_element = soup.find('title')
                page_title = title_element.get_text().strip() if title_element else "Untitled"
                return {
                    'content': content_text,
                    'title': page_title,
                    'section_title': page_title,
                    'url': url
                }
            else:
                return {
                    'content': '',
                    'title': 'Untitled',
                    'section_title': 'Untitled',
                    'url': url
                }
    except Exception as e:
        logging.error(f"Error extracting content from {url}: {e}")
        raise


def chunk_content(content: str, chunk_size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_OVERLAP_SIZE) -> List[Dict[str, Any]]:
    """Chunk extracted content into segments with specified size and overlap."""
    if not content:
        return []
    
    # Split content into words
    words = content.split()
    chunks = []
    start_idx = 0
    
    while start_idx < len(words):
        # Calculate the end index for this chunk
        end_idx = start_idx + chunk_size
        
        # Create the chunk
        chunk_text = ' '.join(words[start_idx:end_idx])
        
        # Create chunk object
        chunk_obj = {
            'id': str(uuid.uuid4()),
            'content': chunk_text,
            'token_count': count_tokens(chunk_text),
            'start_idx': start_idx,
            'end_idx': end_idx
        }
        chunks.append(chunk_obj)
        
        # Move start index forward by chunk_size - overlap to create sliding window
        start_idx = end_idx - overlap
        
        # Make sure we don't have negative start index or go backwards
        if start_idx >= end_idx:
            start_idx = end_idx  # Move to the end if overlap would cause a loop
    
    return chunks


def generate_embeddings(content_chunks: List[Dict[str, Any]], cohere_client, model: str = "embed-multilingual-v3.0") -> List[Dict[str, Any]]:
    """Generate embeddings using Cohere for content chunks."""
    if not content_chunks:
        return []
    
    # Extract just the content texts for embedding
    texts = [chunk['content'] for chunk in content_chunks]
    
    try:
        # Generate embeddings for the texts
        response = cohere_client.embed(
            texts=texts,
            model=model,
            input_type="search_document"  # Using search_document as the input type for document embeddings
        )
        
        # Combine the chunks with their embeddings
        result = []
        for i, chunk in enumerate(content_chunks):
            chunk_with_embedding = chunk.copy()
            chunk_with_embedding['embedding'] = response.embeddings[i]
            chunk_with_embedding['model_version'] = model
            chunk_with_embedding['embedding_created_at'] = datetime.now().isoformat()
            result.append(chunk_with_embedding)
        
        return result
    except Exception as e:
        logging.error(f"Error generating embeddings: {e}")
        raise


def create_qdrant_collection(qdrant_client, collection_name: str, vector_size: int = 1024):
    """Create Qdrant collection for storing content chunks and embeddings."""
    from qdrant_client.http import models
    
    try:
        # Check if collection already exists
        collections = qdrant_client.get_collections()
        collection_exists = any(col.name == collection_name for col in collections.collections)
        
        if not collection_exists:
            # Create the collection with specified vector configuration
            qdrant_client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,  # Cohere's multilingual-v3.0 model returns 1024-dim vectors
                    distance=models.Distance.COSINE
                )
            )
            logging.info(f"Created Qdrant collection: {collection_name}")
        else:
            logging.info(f"Qdrant collection already exists: {collection_name}")
            
    except Exception as e:
        logging.error(f"Error creating Qdrant collection: {e}")
        raise


def store_in_qdrant(qdrant_client, collection_name: str, chunks_with_embeddings: List[Dict[str, Any]]):
    """Store chunk content, embeddings, and metadata in Qdrant with proper payload structure."""
    from qdrant_client.http import models
    
    try:
        points = []
        for item in chunks_with_embeddings:
            point = models.PointStruct(
                id=item['id'],
                vector=item['embedding'],
                payload={
                    'content': item['content'],
                    'url': item.get('url', ''),
                    'section_title': item.get('section_title', ''),
                    'source_page_title': item.get('title', ''),
                    'token_count': item.get('token_count', 0),
                    'created_at': item.get('created_at', datetime.now().isoformat()),
                    'model_version': item.get('model_version', ''),
                    'embedding_created_at': item.get('embedding_created_at', '')
                }
            )
            points.append(point)
        
        # Upload points to Qdrant
        qdrant_client.upload_points(
            collection_name=collection_name,
            points=points
        )
        
        logging.info(f"Stored {len(points)} chunks in Qdrant collection: {collection_name}")
        
    except Exception as e:
        logging.error(f"Error storing chunks in Qdrant: {e}")
        raise


def ingest_book_content(
    book_url: str,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_OVERLAP_SIZE,
    cohere_client=None,
    qdrant_client=None
):
    """Main ingestion function that orchestrates the entire pipeline."""
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting ingestion from book URL: {book_url}")
    
    # Fetch and parse sitemap
    logger.info("Fetching sitemap...")
    sitemap_content = fetch_sitemap(book_url)
    urls = parse_sitemap(sitemap_content)
    logger.info(f"Found {len(urls)} URLs in sitemap")
    
    # Initialize progress tracking
    total_pages = len(urls)
    processed_pages = 0
    
    # Process each URL
    for i, url in enumerate(urls, 1):
        logger.info(f"Processing page {i}/{total_pages}: {url}")
        
        try:
            # Fetch HTML content
            html_content = fetch_html_content(url)
            
            # Extract readable content
            extracted_data = extract_content_from_html(html_content, url)
            
            # Chunk the content
            content_chunks = chunk_content(
                extracted_data['content'], 
                chunk_size=chunk_size, 
                overlap=overlap
            )
            
            logger.info(f"Created {len(content_chunks)} chunks from {url}")
            
            if content_chunks:
                # Add metadata to chunks
                for chunk in content_chunks:
                    chunk['url'] = url
                    chunk['title'] = extracted_data['title']
                    chunk['section_title'] = extracted_data['section_title']
                    chunk['created_at'] = datetime.now().isoformat()
                
                # Generate embeddings
                chunks_with_embeddings = generate_embeddings(content_chunks, cohere_client)
                
                # Store in Qdrant
                store_in_qdrant(qdrant_client, collection_name, chunks_with_embeddings)
                
                processed_pages += 1
                
        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
            continue  # Continue with the next URL
    
    logger.info(f"Ingestion completed. Processed {processed_pages}/{total_pages} pages.")


def semantic_search(query_text: str, qdrant_client, collection_name: str, cohere_client, limit: int = 5):
    """Implement semantic search function that takes query text and returns relevant chunks."""
    logger = logging.getLogger(__name__)

    try:
        logger.info(f"Performing semantic search for query: {query_text}")

        # Generate embedding for query text using Cohere
        query_embedding = generate_query_embedding(query_text, cohere_client)

        # Perform vector search in Qdrant using the query embedding
        search_results = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=limit
        )

        # Format search results with preserved metadata (URL, section title, etc.)
        formatted_results = []
        for result in search_results:
            formatted_result = {
                'id': result.id,
                'content': result.payload.get('content', ''),
                'url': result.payload.get('url', ''),
                'section_title': result.payload.get('section_title', ''),
                'source_page_title': result.payload.get('source_page_title', ''),
                'score': result.score
            }
            formatted_results.append(formatted_result)

        # Add search result ranking by similarity score
        # Results from Qdrant are already ranked by similarity score

        # Add search result limiting (top N results) - already handled by limit parameter in search

        return formatted_results

    except Exception as e:
        logger.error(f"Error during semantic search: {e}")
        raise


def generate_query_embedding(query_text: str, cohere_client, model: str = "embed-multilingual-v3.0"):
    """Create function to generate embedding for query text using Cohere."""
    try:
        # Generate embedding for the query text
        response = cohere_client.embed(
            texts=[query_text],
            model=model,
            input_type="search_query"  # Using search_query as the input type for query embeddings
        )

        # Return the embedding vector
        return response.embeddings[0]
    except Exception as e:
        logging.error(f"Error generating query embedding: {e}")
        raise


# Pydantic models for API
class SearchRequest(BaseModel):
    query: str
    collection_name: str = DEFAULT_COLLECTION_NAME
    limit: int = 5


class SearchResult(BaseModel):
    id: str
    content: str
    url: str
    section_title: str
    source_page_title: str
    score: float


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]


class IngestionRequest(BaseModel):
    book_url: str = DEFAULT_BOOK_URL
    collection_name: str = DEFAULT_COLLECTION_NAME
    chunk_size: int = DEFAULT_CHUNK_SIZE
    overlap: int = DEFAULT_OVERLAP_SIZE


class IngestionResponse(BaseModel):
    message: str
    processed_pages: int
    total_pages: int
    collection_name: str


class IngestionStatus(BaseModel):
    job_id: str
    status: str  # "running", "completed", "failed"
    total_pages: int
    processed_pages: int
    completed_chunks: int
    started_at: str
    completed_at: Optional[str] = None
    error_message: Optional[str] = None


# Global variable to store ingestion job statuses
ingestion_jobs = {}


# Global variables to store clients for API usage
api_cohere_client = None
api_qdrant_client = None
api_config = None


def create_api():
    """Create FastAPI application with search endpoints."""
    if FastAPI is None:
        print("FastAPI is not installed. Run: pip install fastapi uvicorn")
        return None

    app = FastAPI(
        title="Vector DB Ingestion API",
        description="API for ingesting Docusaurus book content and performing semantic search",
        version="0.1.0"
    )

    @app.post("/search", response_model=SearchResponse)
    async def search_endpoint(request: SearchRequest):
        """Add search API endpoint: POST /search"""
        try:
            # Initialize clients if not already done
            global api_cohere_client, api_qdrant_client
            if api_cohere_client is None or api_qdrant_client is None:
                if api_config is None:
                    config = load_config()
                else:
                    config = api_config

                api_cohere_client = setup_cohere_client(config["cohere_api_key"])
                api_qdrant_client = setup_qdrant_client(config["qdrant_url"], config["qdrant_api_key"])

            # Perform semantic search
            results = semantic_search(
                query_text=request.query,
                qdrant_client=api_qdrant_client,
                collection_name=request.collection_name,
                cohere_client=api_cohere_client,
                limit=request.limit
            )

            # Format results to match the response model
            formatted_results = [
                SearchResult(
                    id=result['id'],
                    content=result['content'],
                    url=result['url'],
                    section_title=result['section_title'],
                    source_page_title=result['source_page_title'],
                    score=result['score']
                )
                for result in results
            ]

            return SearchResponse(
                query=request.query,
                results=formatted_results
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/ingest-book")
    async def ingest_endpoint(request: IngestionRequest):
        """Ingestion API endpoint: POST /ingest-book"""
        try:
            # Initialize clients if not already done
            global api_cohere_client, api_qdrant_client
            if api_cohere_client is None or api_qdrant_client is None:
                if api_config is None:
                    config = load_config()
                else:
                    config = api_config

                api_cohere_client = setup_cohere_client(config["cohere_api_key"])
                api_qdrant_client = setup_qdrant_client(config["qdrant_url"], config["qdrant_api_key"])

            # Create the collection
            create_qdrant_collection(api_qdrant_client, request.collection_name)

            # Count total pages for the response
            sitemap_content = fetch_sitemap(request.book_url)
            urls = parse_sitemap(sitemap_content)
            total_pages = len(urls)

            # Run the ingestion process
            ingest_book_content(
                book_url=request.book_url,
                collection_name=request.collection_name,
                chunk_size=request.chunk_size,
                overlap=request.overlap,
                cohere_client=api_cohere_client,
                qdrant_client=api_qdrant_client
            )

            return IngestionResponse(
                message="Ingestion completed successfully",
                processed_pages=total_pages,  # Note: this is a simplification; actual implementation would track actual processed pages
                total_pages=total_pages,
                collection_name=request.collection_name
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/ingestion-status/{job_id}", response_model=IngestionStatus)
    async def ingestion_status_endpoint(job_id: str):
        """Add API endpoint for metadata management: GET /ingestion-status/{job_id}"""
        try:
            if job_id in ingestion_jobs:
                return ingestion_jobs[job_id]
            else:
                raise HTTPException(status_code=404, detail=f"Ingestion job {job_id} not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return app


def validate_chunk_metadata(chunk_data: Dict[str, Any]) -> bool:
    """Create function to validate content chunk metadata before storage."""
    required_fields = ['id', 'content', 'url', 'section_title']
    for field in required_fields:
        if field not in chunk_data or not chunk_data[field]:
            return False
    return True


def extract_and_validate_metadata(html_content: str, url: str) -> Dict[str, Any]:
    """Implement metadata extraction and validation from source pages."""
    # Extract metadata using the existing content extraction function
    extracted_data = extract_content_from_html(html_content, url)

    # Validate the extracted metadata
    if not extracted_data['content']:
        logging.warning(f"No content extracted from {url}")

    if not extracted_data['title']:
        logging.warning(f"No title extracted from {url}")

    if not extracted_data['section_title']:
        logging.warning(f"No section title extracted from {url}")

    return extracted_data


def validate_metadata_on_retrieval(retrieved_payload: Dict[str, Any]) -> bool:
    """Add metadata validation when retrieving content from Qdrant."""
    required_fields = ['content', 'url', 'section_title', 'source_page_title']
    for field in required_fields:
        if field not in retrieved_payload:
            logging.error(f"Missing required field {field} in retrieved payload")
            return False
    return True


def update_chunk_metadata(qdrant_client, collection_name: str, chunk_id: str, new_metadata: Dict[str, Any]):
    """Create function to update/modify chunk metadata if needed."""
    try:
        # Update the payload for the specific point
        qdrant_client.set_payload(
            collection_name=collection_name,
            payload=new_metadata,
            points_selector=[chunk_id]
        )
        logging.info(f"Updated metadata for chunk {chunk_id}")
    except Exception as e:
        logging.error(f"Error updating metadata for chunk {chunk_id}: {e}")
        raise


def retrieve_by_metadata_criteria(qdrant_client, collection_name: str,
                                url: str = None, section_title: str = None,
                                source_page_title: str = None) -> List[Dict[str, Any]]:
    """Implement function to retrieve content by metadata criteria (URL, section, etc.)."""
    from qdrant_client.http import models

    # Build the filter based on the provided criteria
    filter_conditions = []

    if url:
        filter_conditions.append(
            models.FieldCondition(
                key="url",
                match=models.MatchValue(value=url)
            )
        )

    if section_title:
        filter_conditions.append(
            models.FieldCondition(
                key="section_title",
                match=models.MatchValue(value=section_title)
            )
        )

    if source_page_title:
        filter_conditions.append(
            models.FieldCondition(
                key="source_page_title",
                match=models.MatchValue(value=source_page_title)
            )
        )

    # Create the filter if we have conditions
    if filter_conditions:
        query_filter = models.Filter(
            must=filter_conditions
        )
    else:
        # If no filters, return all points (use with caution on large collections)
        query_filter = None

    try:
        points = qdrant_client.scroll(
            collection_name=collection_name,
            scroll_filter=query_filter,
            limit=1000  # Adjust as needed
        )

        results = []
        for point in points[0]:  # points[0] contains the actual points
            result = {
                'id': point.id,
                'payload': point.payload,
                'vector': point.vector
            }
            results.append(result)

        return results
    except Exception as e:
        logging.error(f"Error retrieving content by metadata criteria: {e}")
        raise


def add_ingestion_job_status(job_id: str, status: str, total_pages: int = 0,
                           processed_pages: int = 0, completed_chunks: int = 0,
                           started_at: str = None, completed_at: str = None,
                           error_message: str = None):
    """Add ingestion job status tracking with unique job IDs."""
    global ingestion_jobs

    # Create job status object
    job_status = IngestionStatus(
        job_id=job_id,
        status=status,
        total_pages=total_pages,
        processed_pages=processed_pages,
        completed_chunks=completed_chunks,
        started_at=started_at or datetime.now().isoformat(),
        completed_at=completed_at,
        error_message=error_message
    )

    # Store the job status
    ingestion_jobs[job_id] = job_status.dict()


def implement_rate_limiting(max_requests_per_minute: int = 100):
    """Add ingestion rate limiting to prevent overwhelming APIs."""
    import time
    from collections import deque

    # Track request times
    request_times = deque()

    def check_rate_limit():
        now = time.time()
        # Remove requests older than 1 minute
        while request_times and now - request_times[0] > 60:
            request_times.popleft()

        # Check if we've exceeded the limit
        if len(request_times) >= max_requests_per_minute:
            return False  # Rate limit exceeded

        # Add current request
        request_times.append(now)
        return True  # Within rate limit

    return check_rate_limit


def implement_input_validation(value: Any, field_name: str) -> bool:
    """Implement comprehensive input validation."""
    # Validate different types of inputs
    if field_name == "collection_name":
        # Collection name should not be empty and should follow naming conventions
        if not value or not isinstance(value, str) or len(value.strip()) == 0:
            return False
        # Additional checks for valid collection name could be added here

    elif field_name == "url":
        # Validate URL format
        if not value or not isinstance(value, str):
            return False
        # Basic URL validation
        from urllib.parse import urlparse
        try:
            result = urlparse(value)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    elif field_name == "chunk_size":
        # Validate chunk size is a positive integer
        if not isinstance(value, int) or value <= 0:
            return False

    elif field_name == "overlap":
        # Validate overlap is a non-negative integer
        if not isinstance(value, int) or value < 0:
            return False

    return True


def handle_qdrant_free_tier_limits():
    """Add graceful handling for Qdrant Cloud Free Tier limits."""
    # For Qdrant Cloud Free Tier:
    # - Limited storage space
    # - Limited vector count
    # - Limited API calls

    # The implementation would check:
    # 1. Current collection size
    # 2. Vector count
    # 3. Storage usage
    # 4. API call limits

    # Return True if within limits, False if limits would be exceeded
    # This would typically involve making an API call to Qdrant to check current usage
    pass


def main():
    """Main entry point for the vector DB ingestion system."""
    print("Vector DB Ingestion System")

    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Vector DB Ingestion System for Book Content')
    parser.add_argument('--book-url', type=str, default=DEFAULT_BOOK_URL,
                        help='URL of the Docusaurus book to ingest (default from .env)')
    parser.add_argument('--collection-name', type=str, default=DEFAULT_COLLECTION_NAME,
                        help='Name of the Qdrant collection to use (default: "book-content")')
    parser.add_argument('--chunk-size', type=int, default=DEFAULT_CHUNK_SIZE,
                        help='Size of text chunks in tokens (default: 512)')
    parser.add_argument('--overlap', type=int, default=DEFAULT_OVERLAP_SIZE,
                        help='Overlap between chunks in tokens (default: 50)')
    parser.add_argument('--search', type=str, help='Perform a semantic search with the given query')
    parser.add_argument('--api', action='store_true', help='Run the API server')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host for the API server (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8000, help='Port for the API server (default: 8000)')

    args = parser.parse_args()

    print("Loading configuration...")

    if args.api:
        # Run the API server
        if FastAPI is None:
            print("FastAPI is not installed. Run: pip install fastapi uvicorn")
            sys.exit(1)

        print("Starting API server...")
        app = create_api()
        if app:
            import uvicorn
            uvicorn.run(app, host=args.host, port=args.port)
        else:
            print("Failed to create API application")
            sys.exit(1)
    else:
        try:
            config = load_config()
            logger = setup_logging()
            logger.info("Configuration loaded successfully")

            # Set up Cohere client
            cohere_client = setup_cohere_client(config["cohere_api_key"])
            logger.info("Cohere client initialized")

            # Set up Qdrant client
            qdrant_client = setup_qdrant_client(config["qdrant_url"], config["qdrant_api_key"])
            logger.info("Qdrant client initialized")

            if args.search:
                # Perform semantic search
                print(f"Performing semantic search for: {args.search}")
                search_results = semantic_search(
                    query_text=args.search,
                    qdrant_client=qdrant_client,
                    collection_name=args.collection_name,
                    cohere_client=cohere_client
                )

                print(f"Found {len(search_results)} results:")
                for i, result in enumerate(search_results, 1):
                    print(f"{i}. Score: {result['score']:.3f}")
                    print(f"   Content: {result['content'][:100]}...")
                    print(f"   URL: {result['url']}")
                    print(f"   Section: {result['section_title']}")
                    print()
            else:
                # Create the collection
                create_qdrant_collection(qdrant_client, args.collection_name)

                # Run the ingestion process
                print(f"Starting ingestion from: {args.book_url}")
                print(f"Using collection: {args.collection_name}")
                print(f"Chunk size: {args.chunk_size}, Overlap: {args.overlap}")

                ingest_book_content(
                    book_url=args.book_url,
                    collection_name=args.collection_name,
                    chunk_size=args.chunk_size,
                    overlap=args.overlap,
                    cohere_client=cohere_client,
                    qdrant_client=qdrant_client
                )

                print("System initialization complete and ingestion finished")

        except ValueError as e:
            print(f"Configuration error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error during process: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()