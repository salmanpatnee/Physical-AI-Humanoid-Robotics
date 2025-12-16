# Quickstart Guide: Book Agent SDK

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Access to Qdrant vector database with book content
- UV package manager (or pip as alternative)

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set up Environment
```bash
# Create virtual environment
uv venv  # or python -m venv venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
uv pip install fastapi openai python-dotenv qdrant-client pydantic
# or using requirements.txt:
# pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=your_qdrant_instance_url
QDRANT_API_KEY=your_qdrant_api_key
```

## Running the Service

### 1. Start the FastAPI Application
```bash
# Using uvicorn
uvicorn backend.src.main:app --reload --port 8000

# Or if using a different structure
python -m backend.src.main
```

### 2. Verify the Service is Running
Visit `http://localhost:8000/health` to check the service status.
Visit `http://localhost:8000/api-docs` to access the API documentation.

## Using the API

### Ask a Question
```bash
curl -X POST http://localhost:8000/api/v1/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the three laws of robotics?",
    "book_id": "robotics-principles"
  }'
```

### Example Response
```json
{
  "answer": "The three laws of robotics, as defined by Isaac Asimov, are: 1) A robot may not injure a human being or, through inaction, allow a human being to come to harm...",
  "sources": [
    {
      "content_snippet": "The first law states that a robot may not injure a human being...",
      "source_location": "Chapter 1, Page 15, Robotics Ethics",
      "relevance_score": 0.92
    }
  ],
  "confidence_score": 0.89,
  "timestamp": "2025-12-16T10:30:00Z"
}
```

## Development

### Project Structure
```
backend/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── book_agent.py        # OpenAI agent implementation
│   ├── services/
│   │   ├── __init__.py
│   │   └── retrieval_service.py # Service to retrieve book content from Qdrant
│   ├── models/
│   │   ├── __init__.py
│   │   └── question_answer.py   # Pydantic models for API requests/responses
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py            # API endpoint definition
│   └── main.py                  # FastAPI application entry point
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
└── .env.example
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_retrieval_service.py
```

### Adding New Book Content
To add new book content to the system:
1. Process the book content into chunks
2. Generate embeddings for each chunk
3. Store the chunks in the Qdrant vector database with appropriate metadata

### Implementation Notes
- Answers are generated only from retrieved book content chunks
- Source references are provided with each answer
- The service will refuse to answer if insufficient relevant content is found
- API responses include confidence scores and source relevance metrics