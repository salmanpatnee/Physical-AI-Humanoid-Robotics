# Data Model: Chatbot-Docusaurus Integration

## Entities

### User Query
- **Description**: Represents a question submitted by the user, optionally with selected text context
- **Fields**:
  - `id`: Unique identifier for the query
  - `question`: The main question text entered by the user
  - `selectedText`: Optional text that the user has selected on the page (nullable)
  - `timestamp`: When the query was submitted
  - `userId`: Identifier for the user making the request (for analytics, optional)

### Chat Response
- **Description**: The response from the chatbot to a user query
- **Fields**:
  - `id`: Unique identifier for the response
  - `answer`: The main answer text from the chatbot
  - `sources`: Array of source references that support the answer
  - `timestamp`: When the response was generated
  - `queryId`: Reference to the original query that generated this response

### Source Reference
- **Description**: A reference to the source material used in the chat response
- **Fields**:
  - `id`: Unique identifier for the source
  - `title`: Title or description of the source
  - `url`: URL to the source material (if applicable)
  - `contentPreview`: Brief preview of the relevant content from the source
  - `confidence`: Confidence level in the relevance of this source (0-1)

## Relationships
- A `User Query` generates one `Chat Response`
- A `Chat Response` contains many `Source Reference` objects

## Validation Rules
Based on functional requirements:
- `User Query.question` must not be empty or only whitespace
- `User Query.selectedText` is optional and can be null or empty
- `Chat Response.answer` must not be empty
- `Chat Response.sources` must contain at least one source reference
- Each `Source Reference` must have either a `url` or `contentPreview` (or both)

## State Transitions
- `User Query` starts in "pending" state and transitions to "processed" when the backend responds
- `Chat Response` starts in "processing" state and transitions to "complete" when the response is ready