# Research: Vector DB Ingestion for Book Content

## Overview
Research document for the vector database ingestion system to crawl Docusaurus book URLs, extract text, and store embeddings in Qdrant Cloud.

## Research Tasks Completed

### 1. Content Extraction from Docusaurus Sites
**Task**: Research best practices for extracting readable content from Docusaurus-generated sites

**Decision**: Use BeautifulSoup4 with specific selectors for Docusaurus content areas
**Rationale**: Docusaurus sites have consistent DOM structure with content in specific containers that can be targeted
**Alternatives considered**:
- Selenium (for JS-heavy sites) - rejected as overkill for static content
- Newspaper3k - rejected as it's designed for news articles, not documentation sites
- Readability (Mozilla's library) - considered but BS4 with custom selectors is more direct

### 2. Text Chunking Strategies
**Task**: Research optimal text chunking approaches for semantic search

**Decision**: Use 512-1024 token chunks with overlap
**Rationale**: Balances semantic coherence with retrieval precision; matches spec assumption
**Alternatives considered**:
- Fixed character lengths - less semantically meaningful
- Sentence-based chunks - may break up related concepts
- Entire sections - may exceed embedding model limits

### 3. Cohere Embedding Models
**Task**: Research which Cohere embedding model to use

**Decision**: Use Cohere's embed-multilingual-v3.0 model
**Rationale**: Latest model with good performance for English and non-English content; handles technical documentation well
**Alternatives considered**:
- embed-english-v3.0 - good for English-only content, but multilingual provides flexibility
- embed-english-light-v3.0 - faster/cheaper but potentially lower quality

### 4. Qdrant Cloud Integration
**Task**: Research Qdrant Cloud setup and Python client usage

**Decision**: Use qdrant-client Python library with API key authentication
**Rationale**: Official client library with good documentation and examples
**Alternatives considered**:
- Direct HTTP API calls - more complex, reinventing the wheel
- Other vector DBs (Pinecone, Weaviate) - already specified as Qdrant

### 5. URL Crawling Strategy
**Task**: Research best practices for crawling documentation sites

**Decision**: Use requests library with sitemap or manual URL list for Docusaurus sites
**Rationale**: Docusaurus sites often have sitemaps; if not, we can generate from sidebar structure
**Alternatives considered**:
- Web crawlers (like Scrapy) - overkill for structured documentation sites
- Link following algorithms - unnecessary for Docusaurus with known structure

### 6. UV Dependency Management
**Task**: Research UV as dependency manager vs pip/poetry

**Decision**: Use UV as requested in requirements
**Rationale**: New, fast Python package manager; good for projects that want to try modern tooling
**Alternatives considered**:
- Poetry - also good, but UV was specifically mentioned in requirements
- Standard pip + venv - more common but slower than modern alternatives

## Architecture Considerations

### Single File Design (main.py)
**Decision**: Consolidate entire system into single main.py file
**Rationale**: Simple linear pipeline (fetch → extract → chunk → embed → store) doesn't require complex architecture
**Trade-offs**:
- Pros: Easier to deploy, single file to manage, simpler for this specific use case
- Cons: Less modular, harder to test individual components, less reusable

### Error Handling and Resilience
**Decision**: Implement retry mechanisms and graceful degradation
**Rationale**: Network requests and API calls can fail; system should be resilient
**Approach**: Use tenacity library for retry logic with exponential backoff

### Metadata Preservation
**Decision**: Store source URL and section info with each chunk
**Rationale**: Essential for traceability and attribution when content is retrieved
**Format**: Include as payload in Qdrant records