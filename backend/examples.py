"""
Example scripts for common use cases of the Vector DB Ingestion System.

This file demonstrates various ways to use the system.
"""

# Example 1: Basic ingestion of the default book
def example_basic_ingestion():
    """
    Example: Perform basic ingestion of the default Physical AI & Humanoid Robotics book
    """
    print("Example 1: Basic ingestion")
    print("Command: python main.py")
    print("This will:")
    print("- Fetch the sitemap from the default book URL")
    print("- Process all pages")
    print("- Chunk content (512 tokens with 50-token overlap)")
    print("- Generate embeddings using Cohere")
    print("- Store in Qdrant collection 'book-content'")
    print()


# Example 2: Ingestion with custom parameters
def example_custom_ingestion():
    """
    Example: Perform ingestion with custom parameters
    """
    print("Example 2: Custom ingestion")
    print("Command: python main.py --book-url 'https://example.com/book' --collection-name 'my-collection' --chunk-size 1024 --overlap 100")
    print("This will:")
    print("- Use a custom book URL")
    print("- Store in a custom collection named 'my-collection'")
    print("- Use larger chunks of 1024 tokens")
    print("- Use 100-token overlap between chunks")
    print()


# Example 3: Semantic search
def example_semantic_search():
    """
    Example: Perform semantic search on the ingested content
    """
    print("Example 3: Semantic search")
    print("Command: python main.py --search 'What is ROS 2?' --collection-name 'book-content'")
    print("This will:")
    print("- Perform a semantic search for 'What is ROS 2?'")
    print("- Search in the 'book-content' collection")
    print("- Return the most relevant results with URLs and metadata")
    print()


# Example 4: Running the API server
def example_run_api():
    """
    Example: Run the API server
    """
    print("Example 4: Run API server")
    print("Command: python main.py --api --host 0.0.0.0 --port 8080")
    print("This will:")
    print("- Start the FastAPI server")
    print("- Listen on all interfaces (0.0.0.0) on port 8080")
    print("- Expose /search and /ingest-book endpoints")
    print()


# Example 5: Using the search API programmatically
def example_use_search_api():
    """
    Example: Use the search API programmatically
    """
    import json
    print("Example 5: Using the search API")
    print("POST request to http://localhost:8000/search with payload:")
    payload = {
        "query": "How do I implement a PID controller for robot movement?",
        "collection_name": "book-content",
        "limit": 5
    }
    print(json.dumps(payload, indent=2))
    print("Response will include relevant content chunks with metadata")
    print()


if __name__ == "__main__":
    print("Vector DB Ingestion System - Common Use Cases")
    print("=" * 50)
    example_basic_ingestion()
    example_custom_ingestion()
    example_semantic_search()
    example_run_api()
    example_use_search_api()
    
    print("For more information, run: python main.py --help")