# Implementation Plan: Vector DB Ingestion for Book Content

**Branch**: `016-vector-db-ingestion` | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/016-vector-db-ingestion/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a vector database ingestion system that crawls the Docusaurus book URLs (using sitemap at https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/sitemap.xml), extracts clean readable text, chunks the content, generates embeddings using Cohere, and stores the embeddings with metadata in Qdrant Cloud. The system will be implemented in a single Python file (main.py) with UV for dependency management. API keys for Cohere and Qdrant should be configured in the .env file located in the root directory.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**:
- beautifulsoup4 (for HTML parsing)
- requests (for URL crawling)
- cohere (for embeddings)
- qdrant-client (for Qdrant database interaction)
- python-dotenv (for environment variable management)
- uv for dependency and environment management
**Storage**: Qdrant Cloud vector database
**Testing**: pytest (if tests are requested later)
**Target Platform**: Linux server environment
**Project Type**: Single backend service project
**Performance Goals**: Process the entire book within 1 hour, handle 100+ pages efficiently
**Constraints**: Must fit in Qdrant Cloud Free Tier limits, process pages in reasonable time frames
**Scale/Scope**: Single book ingestion (~100 pages, ~1M+ tokens)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

All requirements checked against the constitution. No violations detected.
- The implementation follows the specification without adding unauthorized features
- The code will be deterministic and reproducible
- All content comes from the source Docusaurus book (no hallucination)
- The implementation will not generate tests unless explicitly requested

## Project Structure

### Documentation (this feature)

```text
specs/016-vector-db-ingestion/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py                     # Single file implementation of the ingestion system
├── pyproject.toml             # UV project configuration
├── uv.lock                    # UV lock file
├── .env.example               # Example environment variables
└── README.md                  # Project documentation
```

**Structure Decision**: Backend service structure chosen since this is a server-side ingestion system that fetches content from URLs, processes it, and stores it in a vector database. The single-file approach (main.py) makes sense for this specific task which follows a linear pipeline: fetch URLs → extract content → chunk → embed → store.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
