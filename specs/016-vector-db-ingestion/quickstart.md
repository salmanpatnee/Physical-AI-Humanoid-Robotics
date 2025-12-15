# Quickstart: Vector DB Ingestion for Book Content

## Overview
Quickstart guide to set up and run the vector database ingestion system for the Physical AI & Humanoid Robotics book.

## Prerequisites
- Python 3.11 or higher
- UV package manager
- Access to Cohere API
- Qdrant Cloud account and API key

## Setup

### 1. Clone and Navigate to Backend Directory
```bash
# Create backend directory if it doesn't exist
mkdir backend && cd backend
```

### 2. Initialize Project with UV
```bash
# Initialize new Python project with UV
uv init
```

### 3. Install Dependencies
```bash
# Add required dependencies
uv add beautifulsoup4 requests cohere qdrant-client python-dotenv

# Install in development mode
uv sync --dev
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with your API keys:
```bash
# .env (in root directory)
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=your_qdrant_cluster_url_here
BOOK_URL=https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/
```

## Usage

### Run the Ingestion
```bash
# Run the main ingestion script
python main.py
```

### Expected Output
The system will:
1. Crawl all pages from the specified book URL
2. Extract readable content from each page
3. Chunk the content into 512-token segments
4. Generate embeddings using Cohere
5. Store the content and embeddings in Qdrant Cloud
6. Report progress and final statistics

## Configuration Options
The main.py script can be configured with command-line arguments:
- `--book-url`: URL of the Docusaurus book to ingest (default from .env)
- `--collection-name`: Name of the Qdrant collection to use (default: "book-content")
- `--chunk-size`: Size of text chunks in tokens (default: 512)
- `--overlap`: Overlap between chunks in tokens (default: 50)

## Verification
After ingestion, you can verify the data was stored correctly by:
1. Checking your Qdrant Cloud dashboard for the collection
2. Using the search functionality to retrieve known content
3. Confirming the expected number of chunks were created

## Troubleshooting
- **Rate Limiting**: If you encounter rate limits, consider adding delays between API calls
- **Memory Issues**: For large books, process in batches to prevent memory overflow
- **Cohere API Issues**: Ensure your API key is valid and you have sufficient credits
- **Qdrant Connection**: Verify your Qdrant URL and API key are correct