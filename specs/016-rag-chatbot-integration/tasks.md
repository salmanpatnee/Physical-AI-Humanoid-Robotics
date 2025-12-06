# Tasks: Integrated RAG Chatbot Development

**Input**: Design documents from `specs/016-rag-chatbot-integration/`

## Phase 1: Setup

**Purpose**: Initialize project structure and dependencies.

- [ ] T001 Create the base directory structure: `backend/src/`, `ingestion/scripts/`, `frontend/src/components/RAGChatbot/`.
- [ ] T002 Initialize a `requirements.txt` file in the `backend/` directory.
- [ ] T003 Add FastAPI, Uvicorn, OpenAI SDK, Qdrant client, pdfplumber, python-frontmatter, and Neon Postgres SDK to `backend/requirements.txt`.

---

## Phase 2: Foundational - Ingestion Pipeline (US1)

**Goal**: Process book content into searchable chunks and store embeddings.

**Independent Test**: A script is run against sample content, and the Qdrant DB is queried to verify correct storage of chunks, metadata, and embeddings.

### Implementation for User Story 1

- [ ] T004 [US1] Implement logic in `ingestion/scripts/process_book.py` to read and extract text from PDF files (e.g., `Hackathon I.pdf`).
- [ ] T005 [US1] Implement logic in `ingestion/scripts/process_book.py` to read and extract text from markdown files in the `docs/` directory.
- [ ] T006 [US1] Implement text chunking logic in `ingestion/scripts/process_book.py`, ensuring `chunk_id`, `document`, and `page` metadata are generated.
- [ ] T007 [US1] Implement embedding generation using a Sentence Transformer model (e.g., `all-MiniLM-L6-v2`) within `ingestion/scripts/process_book.py`.
- [ ] T008 [US1] Implement logic to connect to Qdrant Cloud and store chunks, metadata, and embeddings in `ingestion/scripts/process_book.py`.

**Checkpoint**: Ingestion pipeline is functional; book content is chunked, embedded, and stored in Qdrant.

---

## Phase 3: Foundational - Backend API (US2)

**Goal**: Establish a FastAPI backend to serve chatbot queries.

**Independent Test**: The FastAPI application can be started, and a test query to the `/chat` endpoint successfully returns a response (even if placeholder).

### Implementation for User Story 2 (Backend)

- [ ] T009 [US2] Set up the basic FastAPI application in `backend/src/main.py` based on `openapi.yaml`.
- [ ] T010 [US2] Implement Pydantic models for API requests and responses in `backend/src/models/`.
- [ ] T011 [US2] Implement the database connection and basic CRUD operations for chat history with Neon Serverless Postgres in `backend/src/db/`.
- [ ] T012 [US2] Implement the `/chat` API endpoint in `backend/src/api/chat.py` (or integrated into `main.py`).
- [ ] T013 [US2] In the `/chat` endpoint, implement logic to query Qdrant for relevant text chunks based on the user's message.
- [ ] T014 [US2] In the `/chat` endpoint, integrate the OpenAI Agents/ChatKit SDK to generate a conversational response based on retrieved chunks and chat history.
- [ ] T015 [US2] Implement logic to store chat messages (user and assistant) and session data in Neon Postgres.

**Checkpoint**: Backend API is functional, processing queries and generating responses.

---

## Phase 4: Frontend Chatbot Component (US2 & US3)

**Goal**: Embed an interactive chatbot UI within the Docusaurus book and enable context-aware questioning.

**Independent Test**: The embedded chatbot UI is visible and interactive. General questions are answered. Selected text context is correctly passed and used.

### Implementation for User Story 2 & 3 (Frontend)

- [ ] T016 [US2] Create the basic React UI component for the RAG chatbot in `frontend/src/components/RAGChatbot/`.
- [ ] T017 [US2] Implement a service (`frontend/src/services/chatbotApi.ts`) to handle communication with the FastAPI `/chat` endpoint.
- [ ] T018 [US2] Integrate the RAG chatbot component into the Docusaurus layout (e.g., `src/theme/Layout/`).
- [ ] T019 [US3] Implement frontend logic to detect user text selection and make it available to the chatbot component.
- [ ] T020 [US3] Modify the chatbot UI to allow asking questions specifically about the selected text, passing the selected text as `context` to the backend.

**Checkpoint**: Embedded chatbot is fully integrated and functional, supporting context-aware questions.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, testing, and deployment preparation.

- [ ] T021 Write unit tests for the backend API endpoints in `backend/tests/test_api.py`.
- [ ] T022 Write E2E tests using Playwright to validate the full chatbot interaction and response relevance.
- [ ] T023 Ensure all necessary environment variables (e.g., Qdrant API key, Neon DB connection string, OpenAI API key) are configured and secure.
- [ ] T024 Run `npx docusaurus build` and `python -m uvicorn backend.src.main:app --host 0.0.0.0 --port 8000` to ensure the entire system builds and runs without errors.
- [ ] T025 Document deployment steps for both the FastAPI backend and the Docusaurus frontend.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies.
-   **Ingestion Pipeline (Phase 2)**: Depends on Setup.
-   **Backend API (Phase 3)**: Depends on Setup. Can be developed in parallel with the Ingestion Pipeline to some extent, but integration requires a functional pipeline.
-   **Frontend Chatbot Component (Phase 4)**: Depends on Backend API (Phase 3).
-   **Polish & Cross-Cutting Concerns (Phase 5)**: Depends on all previous phases.

### User Story Dependencies

-   **User Story 1 (Ingestion)**: Must be completed first as it provides the data for the RAG system.
-   **User Story 2 (Embedded Chatbot)**: Depends on User Story 1 (data) and the core Backend API implementation.
-   **User Story 3 (Context-Aware Q&A)**: Depends on User Story 2 (basic chatbot functionality).

### Parallel Opportunities

-   Frontend component UI development can start in parallel with some backend API development, assuming API contracts are stable.
-   Individual tasks within the same phase marked `[P]` (none explicitly marked for this feature as most are sequential logic steps, but some file creations can be).

---

## Implementation Strategy

### MVP First

1.  Complete **Phase 1: Setup**.
2.  Complete **Phase 2: Foundational - Ingestion Pipeline (US1)**.
3.  Complete core parts of **Phase 3: Foundational - Backend API (US2)** for basic query processing.
4.  Complete core parts of **Phase 4: Frontend Chatbot Component (US2)** for basic embedding and UI.
5.  **STOP and VALIDATE**: Test basic chatbot interaction for general questions.

### Incremental Delivery

-   Deliver a functional ingestion pipeline.
-   Deliver a functional backend API for RAG queries.
-   Deliver a basic embedded chatbot UI.
-   Enhance chatbot with context-aware questioning.
-   Add comprehensive testing and deployment documentation.
