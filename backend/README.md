# Vector DB Ingestion System

This system ingests content from Docusaurus book URLs, extracts readable text, chunks it, generates embeddings using Cohere, and stores the embeddings with metadata in Qdrant Cloud for semantic retrieval.

## Setup

1. Clone the repository
2. Navigate to the backend directory: `cd backend`
3. Install dependencies using UV: `uv sync --dev`
4. Copy the example environment file: `cp .env.example .env`
5. Update the `.env` file with your API keys:
   - `COHERE_API_KEY`: Your Cohere API key
   - `QDRANT_API_KEY`: Your Qdrant API key
   - `QDRANT_URL`: Your Qdrant cluster URL

## Usage

### Basic Ingestion
Run the ingestion system with default settings:
```
python main.py
```

### Custom Ingestion
Run the ingestion system with custom parameters:
```
python main.py --book-url "https://example.com/book" --collection-name "my-collection" --chunk-size 512 --overlap 50
```

### Semantic Search
Perform a semantic search on the ingested content:
```
python main.py --search "What is ROS 2?"
```

### Run API Server
Start the FastAPI server to expose endpoints:
```
python main.py --api --host 127.0.0.1 --port 8000
```

After starting the API server, you can use the following endpoints:
- `POST /search` - Perform semantic search
- `POST /ingest-book` - Ingest a book
- `GET /ingestion-status/{job_id}` - Check ingestion job status

## Configuration Options
- `--book-url`: URL of the Docusaurus book to ingest (default from .env)
- `--collection-name`: Name of the Qdrant collection to use (default: "book-content")
- `--chunk-size`: Size of text chunks in tokens (default: 512)
- `--overlap`: Overlap between chunks in tokens (default: 50)
- `--search`: Perform a semantic search with the given query
- `--api`: Run the API server instead of command-line operations
- `--host`: Host for the API server (default: 127.0.0.1)
- `--port`: Port for the API server (default: 8000)

## Architecture

The system follows a linear pipeline:
1. Crawl all pages from the specified book URL using the sitemap
2. Extract readable content from each page
3. Chunk the content into 512-token segments
4. Generate embeddings using Cohere
5. Store the content and embeddings in Qdrant Cloud
6. Report progress and final statistics

## Example Scripts

See `examples.py` for common use cases and implementation examples.

## Troubleshooting

Refer to `TROUBLESHOOTING.md` for solutions to common issues.