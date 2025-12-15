# Tasks: Vector DB Ingestion for Book Content

**Feature**: 016-vector-db-ingestion | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Design documents from `specs/016-vector-db-ingestion/`

## Implementation Strategy

**MVP**: Implement User Story 1 (content ingestion pipeline) with basic crawling, extraction, chunking, and storage to Qdrant.
**Delivery**: Incremental implementation by user story priority (P1, P2, P3).
**Testing**: Manual verification of each user story completion with independent test criteria.

## Dependencies

- User Story 2 (Semantic Search Querying) and User Story 3 (Content Chunk Management) depend on User Story 1 (Content Ingestion Pipeline) being completed first
- Foundational phase must be completed before any user story phases
- Setup phase must be completed first

## Parallel Execution Examples

- [US1] Crawl and extract content can run in parallel for different URLs
- [US1] Embedding generation can run in parallel for different content chunks
- [US2] Search functions can be developed in parallel with the ingestion pipeline

---

## Phase 1: Setup

**Goal**: Initialize the project structure, set up UV dependency management, and install required libraries.

### Independent Test: 
Project directory structure is created with all necessary files and dependencies installed.

- [ ] T001 Create backend directory structure
- [ ] T002 Initialize Python project with UV using `uv init`
- [ ] T003 Create pyproject.toml with project metadata and dependencies
- [ ] T004 Add dependencies to pyproject.toml: beautifulsoup4, requests, cohere, qdrant-client, python-dotenv, tenacity
- [ ] T005 Generate uv.lock file with `uv sync --dev`
- [ ] T006 Create .env.example file with environment variable placeholders
- [ ] T007 Create main.py with initial file structure and imports
- [ ] T008 Create README.md with project documentation

---

## Phase 2: Foundational

**Goal**: Implement core utilities and configuration loading that all user stories will depend on.

### Independent Test: 
Core utilities are implemented and can load configuration from environment variables.

- [ ] T010 Create configuration loading function to read from .env file
- [ ] T011 Implement utility functions for logging and progress tracking
- [ ] T012 Create helper functions for token counting and text processing
- [ ] T013 Set up Cohere client with API key from environment variables
- [ ] T014 Set up Qdrant client with URL and API key from environment variables
- [ ] T015 Implement retry mechanism with tenacity for API calls
- [ ] T016 Create constants file for configuration defaults (chunk size, overlap, etc.)

---

## Phase 3: User Story 1 - Content Ingestion Pipeline (Priority: P1)

**Goal**: Implement the core functionality to crawl Docusaurus book URLs, extract readable content, chunk it, generate embeddings, and store in Qdrant.

**User Story**: An internal system component needs to automatically fetch content from published Docusaurus book URLs, process it into readable format, and store it in a vector database for later retrieval.

**Independent Test**: The system can fetch content from a Docusaurus book URL, process it, generate embeddings using Cohere, and store them in Qdrant with proper metadata. The process can be verified by checking that content chunks exist in the database with associated embeddings.

**Acceptance Scenarios**:
1. Given a valid Docusaurus book URL, When the ingestion pipeline runs, Then all public pages are processed into readable content chunks with embeddings stored in Qdrant
2. Given a Docusaurus page with various content types (text, lists, code blocks), When the extraction process runs, Then readable content is extracted while preserving semantic meaning
3. Given content extraction has completed successfully, When embeddings are generated, Then each content chunk has a corresponding vector representation stored in Qdrant

- [ ] T020 [US1] Implement function to fetch sitemap.xml from https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/sitemap.xml
- [ ] T021 [US1] Parse sitemap to extract all book page URLs
- [ ] T022 [US1] Create function to fetch HTML content from a single URL using requests
- [ ] T023 [P] [US1] Create function to extract readable content from HTML using BeautifulSoup and Docusaurus-specific selectors
- [ ] T024 [P] [US1] Create function to chunk extracted content into 512-token segments with 50-token overlap
- [ ] T025 [P] [US1] Create function to generate embeddings using Cohere for content chunks
- [ ] T026 [US1] Create Qdrant collection for storing content chunks and embeddings
- [ ] T027 [US1] Store chunk content, embeddings, and metadata in Qdrant with proper payload structure
- [ ] T028 [US1] Implement progress tracking for ingestion process
- [ ] T029 [US1] Add error handling for failed URL fetches, extraction, or embedding generation
- [ ] T030 [US1] Implement graceful degradation for API limits and connection issues
- [ ] T031 [US1] Create main ingestion function that orchestrates the entire pipeline
- [ ] T032 [US1] Add command-line arguments for configuration (book URL, collection name, chunk size, overlap)
- [ ] T033 [US1] Implement ingestion statistics reporting

---

## Phase 4: User Story 2 - Semantic Search Querying (Priority: P2)

**Goal**: Implement semantic search capability to retrieve relevant content chunks based on text queries.

**User Story**: An internal system component needs to perform semantic search queries against the stored content embeddings to retrieve relevant chunks based on text queries.

**Independent Test**: The system can accept a text query and return relevant content chunks from the Qdrant vector database. Relevance can be verified by examining the returned content for semantic alignment with the query.

**Acceptance Scenarios**:
1. Given a semantic query text, When the search function is called, Then relevant content chunks are returned in ranked order by semantic similarity
2. Given search results from Qdrant, When they are processed, Then metadata including source URL and section reference is preserved

- [ ] T040 [US2] Implement semantic search function that takes query text and returns relevant chunks
- [ ] T041 [US2] Create function to generate embedding for query text using Cohere
- [ ] T042 [US2] Implement vector search in Qdrant using the query embedding
- [ ] T043 [US2] Format search results with preserved metadata (URL, section title, etc.)
- [ ] T044 [US2] Add search result ranking by similarity score
- [ ] T045 [US2] Implement search result limiting (top N results)
- [ ] T046 [US2] Add search API endpoint: POST /search

---

## Phase 5: User Story 3 - Content Chunk Management (Priority: P3)

**Goal**: Implement proper management of content chunks with metadata preservation and validation.

**User Story**: The system needs to manage content chunks with proper metadata, including the original URL, section reference, and other relevant information.

**Independent Test**: For each stored content chunk, the system maintains accurate metadata including source URL and section reference. This can be verified by examining stored records and validating their metadata.

**Acceptance Scenarios**:
1. Given content has been processed from a source URL, When it is stored in Qdrant, Then metadata includes the original URL and section reference
2. Given content chunks with metadata in the database, When they are retrieved, Then the metadata is intact and accurate

- [ ] T050 [US3] Create function to validate content chunk metadata before storage
- [ ] T051 [US3] Implement metadata extraction and validation from source pages
- [ ] T052 [US3] Add metadata validation when retrieving content from Qdrant
- [ ] T053 [US3] Create function to update/modify chunk metadata if needed
- [ ] T054 [US3] Implement function to retrieve content by metadata criteria (URL, section, etc.)
- [ ] T055 [US3] Add metadata consistency checks during ingestion
- [ ] T056 [US3] Add API endpoint for metadata management: GET /ingestion-status/{job_id}

---

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Complete the system with additional features, documentation, and error handling.

### Independent Test: 
System is fully documented, handles errors gracefully, and includes status tracking functionality.

- [ ] T060 Add comprehensive error logging and reporting
- [ ] T061 Implement ingestion job status tracking with unique job IDs
- [ ] T062 Add ingestion rate limiting to prevent overwhelming APIs
- [ ] T063 Create ingestion progress API endpoint: GET /ingestion-status/{job_id}
- [ ] T064 Add ingestion statistics and metrics
- [ ] T065 Update README.md with complete usage instructions
- [ ] T066 Add example scripts for common use cases
- [ ] T067 Implement comprehensive input validation
- [ ] T068 Add graceful handling for Qdrant Cloud Free Tier limits
- [ ] T069 Update .env.example with all required variables and explanations
- [ ] T070 Create documentation for troubleshooting common issues