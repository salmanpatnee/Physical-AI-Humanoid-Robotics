# Quickstart: RAG Chatbot

This document provides a brief overview of the components of the RAG chatbot feature.

## Ingestion Pipeline

-   **Location**: `ingestion/scripts/process_book.py`
-   **Purpose**: To read content from `docs/` and PDF files, chunk it, generate embeddings, and store them in the Qdrant vector database.
-   **Usage**: `python ingestion/scripts/process_book.py`

## Backend API

-   **Location**: `backend/`
-   **Framework**: FastAPI
-   **Purpose**: To handle chat requests, retrieve relevant context from the vector database, and generate responses using the OpenAI Agents/ChatKit SDKs.
-   **Endpoint**: `POST /chat`

## Frontend Component

-   **Location**: `frontend/src/components/RAGChatbot/`
-   **Purpose**: To provide a user interface for the chatbot, embedded within the Docusaurus site.
-   **Usage**: The component will be added to the Docusaurus layout to be accessible on all pages.
