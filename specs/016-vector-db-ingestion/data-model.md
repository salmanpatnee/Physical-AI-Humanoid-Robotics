# Data Model: Vector DB Ingestion for Book Content

## Overview
Data models for the vector database ingestion system. This document defines the structure of content chunks, embeddings, and metadata that will be stored in Qdrant.

## Core Entities

### ContentChunk
**Definition**: A segment of extracted readable text from a Docusaurus page, with associated metadata

**Fields**:
- `id` (string): Unique identifier for the chunk (UUID format)
- `content` (string): The actual extracted text content
- `url` (string): Source URL of the original document
- `section_title` (string): Title of the section from which this chunk was extracted
- `created_at` (datetime): Timestamp when the chunk was created
- `token_count` (integer): Number of tokens in the content
- `source_page_title` (string): Title of the source document/page

**Validation Rules**:
- Content must not be empty
- URL must be a valid URL format
- Token count must be positive
- ID must be unique across all chunks

### EmbeddingVector
**Definition**: Numerical representation of the semantic meaning of a content chunk

**Fields**:
- `chunk_id` (string): Reference to the ContentChunk.id
- `vector` (array[float32]): The embedding vector (dimensions depend on Cohere model)
- `model_version` (string): Version of the embedding model used
- `embedding_created_at` (datetime): Timestamp when the embedding was generated

**Validation Rules**:
- Vector must have consistent dimensions
- Model version must be a valid Cohere model identifier
- Chunk ID must reference an existing ContentChunk

### QdrantRecord
**Definition**: Complete record stored in Qdrant database containing both content and embedding

**Fields**:
- `id` (string): Same as ContentChunk.id
- `vector` (array[float32]): Embedding vector data
- `payload` (object): Metadata object containing:
  - `content`: Original content string
  - `url`: Source URL
  - `section_title`: Section title
  - `source_page_title`: Page title
  - `token_count`: Number of tokens
  - `created_at`: Creation timestamp

**Validation Rules**:
- ID must match ContentChunk.id
- Vector dimensions must match Cohere model output
- Payload fields must validate against ContentChunk properties

### CrawlResult
**Definition**: Result of crawling a single URL

**Fields**:
- `url` (string): The crawled URL
- `status` (enum): Status of the crawl (success, failed, rate_limited)
- `content` (string): Raw HTML content retrieved
- `title` (string): Page title from HTML
- `crawled_at` (datetime): When the page was crawled
- `error_message` (string, optional): Error details if crawl failed

**Validation Rules**:
- URL must be valid
- Status must be one of the defined enum values
- Content must be present if status is success

## Relationships

1. **ContentChunk → EmbeddingVector**: One-to-one relationship
   - One ContentChunk has exactly one EmbeddingVector
   - Referenced by chunk_id field

2. **ContentChunk + EmbeddingVector → QdrantRecord**: Composition
   - QdrantRecord combines ContentChunk and EmbeddingVector data for storage
   - No direct reference, data is embedded in the record

3. **CrawlResult → ContentChunk**: One-to-many relationship
   - One crawled page can generate multiple content chunks
   - Inferred by URL matching

## State Transitions (if applicable)

### ContentChunk States
- `pending_extraction`: Content has been crawled but not yet processed
- `extracted`: Content has been cleaned and prepared
- `chunked`: Content has been split into appropriate chunks
- `embedded`: Embedding has been generated for the chunk
- `stored`: Chunk and embedding have been saved to Qdrant

### Transition Rules
- `pending_extraction` → `extracted`: After successful content extraction from HTML
- `extracted` → `chunked`: After content is split into appropriate chunks
- `chunked` → `embedded`: After Cohere API returns embedding
- `embedded` → `stored`: After successful storage in Qdrant