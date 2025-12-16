# Data Model: Validate Retrieval Pipeline

## Entities

### Query Request
- **Description**: Represents a question or search request submitted by the developer for validation purposes
- **Fields**:
  - `id` (string): Unique identifier for the query request
  - `question` (string): The text of the user question being tested
  - `expected_sources` (list): Optional list of source materials expected in response
  - `timestamp` (datetime): When the query was submitted
  - `module_context` (string): Optional context about which module this query relates to

### Content Chunk
- **Description**: A segment of text from a book that has been indexed in the vector database
- **Fields**:
  - `id` (string): Unique identifier for the content chunk
  - `content` (string): The actual text content of the chunk
  - `vector_embedding` (list[float]): Vector representation for semantic search
  - `source_reference` (SourceReference): Link to the original location
  - `similarity_score` (float): Score indicating relevance to the query
  - `position_in_result` (int): Order in which this chunk was returned

### Source Reference
- **Description**: Information that links a content chunk back to its original location
- **Fields**:
  - `book_title` (string): Title of the source book
  - `chapter` (string): Chapter number/name where the content appears
  - `page_number` (int): Page number in the source book
  - `section` (string): Section or subsection in the book
  - `url` (string): URL to the source content if available

### Validation Result
- **Description**: Captures the results of running a validation query
- **Fields**:
  - `id` (string): Unique identifier for the validation result
  - `query_request_id` (string): Reference to the original query request
  - `retrieved_chunks` (list[ContentChunk]): Retrieved content chunks
  - `relevance_score` (float): Overall relevance score (0-1)
  - `source_mapping_accuracy` (float): Accuracy of source reference mapping (0-1)
  - `latency_ms` (float): Time taken to retrieve results in milliseconds
  - `is_valid` (boolean): Whether the result meets validation criteria
  - `feedback` (string): Human-readable feedback about the result quality

### Module
- **Description**: A discrete collection of educational content in the vector database
- **Fields**:
  - `id` (string): Unique identifier for the module
  - `title` (string): Title of the module
  - `description` (string): Brief description of the module
  - `total_chunks` (int): Number of content chunks in the module
  - `qdrant_collection_name` (string): Name of the Qdrant collection containing this module

## Validation Rules

### Query Request Validation
- Question must not be empty
- Question must be a string between 10 and 500 characters
- Module context must be valid if provided

### Content Chunk Validation
- Content must not be empty
- Vector embedding must have the correct dimensions for the model used
- Source reference must be valid and not null
- Similarity score must be between 0 and 1

### Source Reference Validation
- Book title must not be empty
- Page number must be a positive integer
- URL must be a valid URL if provided

### Validation Result Validation
- Relevance score must be between 0 and 1
- Source mapping accuracy must be between 0 and 1
- Latency must be a positive number
- Retrieved chunks must not be empty