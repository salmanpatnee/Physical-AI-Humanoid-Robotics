# Feature Specification: Integrated RAG Chatbot Development

**Feature Branch**: `016-rag-chatbot-integration`  
**Created**: 2025-12-06
**Status**: Draft  
**Input**: User description: "The system should read the book (PDF or docs/) and produce searchable text chunks with identifiers and basic metadata (document, page, chunk_id), then generate vector embeddings for each chunk and store them in a hosted vector database. Acceptance: chunks + embeddings exist for the whole book and a sample similarity query returns relevant chunk IDs. Context: Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book. This chatbot, utilizing the OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier, must be able to answer user questions about the book's content, including answering questions based only on text selected by the user."

## User Scenarios & Testing

### User Story 1 - Book Content Ingestion for RAG (Priority: P1)

As a system administrator, I want to process the book's content (PDF or docs/) into searchable text chunks with metadata and generate vector embeddings, so that the content is indexed and ready for the RAG chatbot to utilize.

**Why this priority**: This is the foundational backend process required for the RAG chatbot to function.

**Independent Test**: A script can be run to ingest a sample book section, and the vector database can be queried to confirm that chunks, metadata, and embeddings for that section are correctly stored and retrievable.

**Acceptance Scenarios**:

1. **Given** book content in PDF or `docs/` format, **When** the ingestion process is executed, **Then** the content is chunked, embedded, and stored in the vector database.
2. **Given** a specific `chunk_id`, **When** queried from the vector database, **Then** its associated text content, document name, and page number are returned.
3. **Given** a sample query vector, **When** a similarity search is performed, **Then** relevant chunk IDs are returned.

### User Story 2 - Embedded RAG Chatbot Interaction (Priority: P1)

As a book reader, I want to interact with an embedded RAG chatbot within the published book, so that I can ask questions about the book's content and receive accurate, contextually relevant answers.

**Why this priority**: This is the primary user-facing feature that delivers the core value of the RAG chatbot.

**Independent Test**: The embedded chatbot UI can be opened, a question about the book content can be posed, and a relevant answer should be returned.

**Acceptance Scenarios**:

1. **Given** I am reading a section of the book, **When** I open the embedded RAG chatbot, **Then** I can input a question related to the book's content.
2. **Given** I have asked a question, **When** the chatbot processes my question, **Then** it retrieves relevant information from the vector database and provides an answer based on the book's content.

### User Story 3 - Context-Aware Question Answering (Priority: P2)

As a book reader, I want to select a specific passage of text within the book and ask the RAG chatbot questions constrained to that selected context, so that I can get highly focused answers without irrelevant information.

**Why this priority**: Enhances the chatbot's utility by allowing more precise, context-specific interactions.

**Independent Test**: A user can select a text passage, pose a question specifically about that passage, and verify that the chatbot's answer is limited to the selected context.

**Acceptance Scenarios**:

1. **Given** I have selected a passage of text in the book, **When** I activate the chatbot's context-aware mode and ask a question, **Then** the chatbot's answer uses only information from the selected text.
2. **Given** the chatbot answers based on selected text, **When** the answer is reviewed, **Then** it does not contain information outside the selected passage.

## Requirements

### Functional Requirements

- **FR-001**: The system MUST read and extract text from PDF documents (`Hackathon I.pdf`) and markdown files (`docs/`).
- **FR-002**: The system MUST segment extracted text into searchable chunks with `chunk_id`, `document`, and `page` metadata.
- **FR-003**: The system MUST generate vector embeddings for each chunk using an appropriate embedding model.
- **FR-004**: The system MUST store chunks, metadata, and embeddings in the Qdrant Cloud Free Tier vector database.
- **FR-005**: The system MUST provide a FastAPI backend for processing chatbot queries.
- **FR-006**: The chatbot MUST be embedded within the published book (Docusaurus frontend).
- **FR-007**: The chatbot MUST utilize OpenAI Agents/ChatKit SDKs for conversational logic and response generation.
- **FR-008**: The chatbot MUST use Neon Serverless Postgres for persistent storage (e.g., chat history, user preferences).
- **FR-009**: The chatbot MUST be able to answer questions based *only* on text selected by the user within the book.

### Key Entities

-   **Text Chunk**: Segment of book content with `chunk_id`, `document`, `page`, `text`.
-   **Vector Embedding**: Numerical representation of a text chunk.
-   **Vector Database**: Qdrant Cloud Free Tier, storing embeddings and metadata.
-   **Chatbot UI**: Frontend component embedded in Docusaurus.
-   **Chatbot Backend**: FastAPI application.
-   **Conversational Logic**: Powered by OpenAI Agents/ChatKit SDKs.
-   **Persistent Storage**: Neon Serverless Postgres.

## Success Criteria

### Measurable Outcomes

-   **SC-001**: 100% of book content is successfully chunked, embedded, and stored in Qdrant.
-   **SC-002**: The embedded chatbot is visible and interactive on all book pages.
-   **SC-003**: For general questions, the chatbot provides relevant answers from the book content with a relevance score of at least 80% (using the internal vector similarity score from the database).
-   **SC-004**: For questions based on selected text, the chatbot's answers are strictly confined to the selected context in 95% of test cases.
-   **SC-005**: The chatbot's response time for a typical query is under 5 seconds.