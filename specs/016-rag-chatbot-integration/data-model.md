# Data Model for RAG Chatbot

This document outlines the data models for the entities used in the RAG chatbot feature.

## Text Chunk

Represents a segment of text extracted from a source document, stored in the Qdrant vector database.

-   **chunk_id**: `string` (UUID) - Unique identifier for the text chunk.
-   **document**: `string` - The name of the source document (e.g., "module1-intro.md").
-   **page**: `integer` (optional) - The page number from the source PDF.
-   **text**: `string` - The text content of the chunk.
-   **embedding**: `vector` - The vector embedding of the text.

## Chat Message

Represents a single message in a chat session, stored in the Neon Serverless Postgres database.

-   **message_id**: `string` (UUID) - Unique identifier for the message.
-   **session_id**: `string` - Identifier for the chat session.
-   **role**: `string` - The role of the message sender (e.g., "user", "assistant").
-   **content**: `string` - The text content of the message.
-   **timestamp**: `datetime` - The time the message was created.
-   **metadata**: `json` (optional) - Additional metadata, such as retrieved context from the vector database.
