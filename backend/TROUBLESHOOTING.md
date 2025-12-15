# Troubleshooting Guide for Vector DB Ingestion System

This guide covers common issues and their solutions when using the vector database ingestion system.

## Common Issues and Solutions

### 1. API Connection Issues

**Problem**: Connection errors when connecting to Cohere or Qdrant APIs.

**Symptoms**: 
- "ConnectionError" or "TimeoutError" exceptions
- HTTP 401 (Unauthorized) responses
- SSL/TLS certificate errors

**Solutions**:
- Verify your API keys in the .env file are correct and haven't expired
- Check that your internet connection is working
- Confirm the API endpoints are reachable from your location
- If using a corporate firewall, ensure API endpoints are not blocked
- For SSL errors, try updating your certificates or use a different network

### 2. Rate Limiting Issues

**Problem**: Receiving rate limit errors from APIs.

**Symptoms**:
- HTTP 429 (Too Many Requests) responses
- Intermittent failures during ingestion
- Slower than expected processing times

**Solutions**:
- Implement rate limiting in your code using exponential backoff
- Add delays between API calls if processing many documents
- Consider upgrading your API plan if you consistently hit rate limits
- Use the rate limiting function implemented in the code

### 3. Memory Issues

**Problem**: Running out of memory during large ingestion jobs.

**Symptoms**:
- "MemoryError" exceptions
- System becoming unresponsive
- Process being killed by the OS

**Solutions**:
- Process documents in smaller batches
- Increase system memory if possible
- Clear unused variables and use generators instead of lists where possible
- For large books, process in batches to prevent memory overflow

### 4. Cohere API Issues

**Problem**: Issues with embedding generation.

**Symptoms**:
- Embedding generation failing
- Inconsistent embedding quality
- API responses taking too long

**Solutions**:
- Ensure your API key is valid and you have sufficient credits
- Check that the input text doesn't exceed model limits
- Verify the correct model name is being used
- Monitor your API usage to avoid rate limits

### 5. Qdrant Connection Issues

**Problem**: Connecting to Qdrant Cloud fails.

**Symptoms**:
- Cannot establish connection to Qdrant cluster
- Authentication failures
- Collection creation failures

**Solutions**:
- Verify your Qdrant URL and API key are correct
- Check that the Qdrant cluster is running and accessible
- Confirm your Qdrant Cloud plan supports the operations you're trying to perform
- Ensure the cluster URL is properly formatted

### 6. Content Extraction Problems

**Problem**: Content not being extracted properly from web pages.

**Symptoms**:
- Empty content chunks
- Mixed content from different sections
- Missing important information

**Solutions**:
- Verify the Docusaurus site structure hasn't changed
- Update CSS selectors if the site layout has been modified
- Check for JavaScript-rendered content that requires special handling
- Ensure the sitemap correctly lists all book pages

### 7. Chunking Issues

**Problem**: Text not being chunked appropriately.

**Symptoms**:
- Chunks too large or too small
- Sentences being broken mid-paragraph
- Important context being lost

**Solutions**:
- Adjust chunk_size and overlap parameters based on your content
- Consider content type when setting chunking parameters
- Validate that chunks maintain semantic meaning
- Review the chunking algorithm for edge cases

### 8. Search Quality Issues

**Problem**: Search results not being relevant to queries.

**Symptoms**:
- Irrelevant results being returned
- Poor semantic matching
- Unexpected ranking of results

**Solutions**:
- Verify embeddings were generated correctly during ingestion
- Check that query embeddings use the same model as document embeddings
- Consider fine-tuning your search approach based on content type
- Review the similarity threshold used for matching

## Performance Optimization

### Improving Ingestion Speed
- Use parallel processing for independent operations
- Optimize API calls with appropriate batching
- Ensure fast internet connection for web crawling
- Consider processing less critical metadata in background

### Reducing API Costs
- Implement caching for frequently accessed embeddings
- Use appropriate embedding models based on your needs
- Monitor API usage to stay within budget
- Consider batch processing to reduce per-operation overhead

## Environment Configuration

### Required Environment Variables
Make sure your .env file contains all required variables:
```
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_URL=your_qdrant_cluster_url_here
BOOK_URL=https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/
```

### Dependency Issues
If you encounter dependency conflicts:
1. Create a new virtual environment
2. Install dependencies using the provided pyproject.toml
3. Run `uv sync` to resolve dependencies