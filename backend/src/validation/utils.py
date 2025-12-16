import re
from typing import List, Dict, Any
from .models import QueryRequest


def generate_validation_id() -> str:
    """Generate a unique validation ID."""
    import uuid
    return f"val_{str(uuid.uuid4())[:8]}"


def generate_query_request_id() -> str:
    """Generate a unique query request ID."""
    import uuid
    return f"qry_{str(uuid.uuid4())[:8]}"


def clean_text(text: str) -> str:
    """Clean and normalize text for processing."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', ' ', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text


def extract_keywords(text: str, num_keywords: int = 10) -> List[str]:
    """Extract keywords from text using simple frequency analysis."""
    # Clean the text
    cleaned_text = clean_text(text.lower())
    
    # Split into words and remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 
        'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 
        'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 
        'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 
        'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their'
    }
    
    words = cleaned_text.split()
    word_freq = {}
    
    for word in words:
        if word not in stop_words and len(word) > 2:  # Only consider words longer than 2 chars
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:num_keywords]]


def validate_query_request(query_request: QueryRequest) -> List[str]:
    """Validate a query request and return a list of validation errors."""
    errors = []
    
    # Validate question
    if not query_request.question or len(query_request.question.strip()) == 0:
        errors.append("Question cannot be empty")
    elif len(query_request.question) < 10:
        errors.append("Question must be at least 10 characters long")
    elif len(query_request.question) > 500:
        errors.append("Question must be no more than 500 characters long")
    
    # Validate expected sources if provided
    if query_request.expected_sources is not None:
        if not isinstance(query_request.expected_sources, list):
            errors.append("Expected sources must be a list")
        else:
            for source in query_request.expected_sources:
                if not isinstance(source, str) or len(source.strip()) == 0:
                    errors.append(f"Expected source '{source}' is not a valid string")
    
    # Validate module context if provided
    if query_request.module_context is not None:
        if not isinstance(query_request.module_context, str) or len(query_request.module_context.strip()) == 0:
            errors.append("Module context must be a non-empty string if provided")
    
    return errors


def normalize_text_for_comparison(text: str) -> str:
    """Normalize text for comparison purposes."""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and extra whitespace
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing whitespace
    return text.strip()


def calculate_text_similarity(text1: str, text2: str) -> float:
    """Calculate text similarity using a simple overlap method."""
    if not text1 or not text2:
        return 0.0
    
    # Normalize both texts
    norm_text1 = set(normalize_text_for_comparison(text1).split())
    norm_text2 = set(normalize_text_for_comparison(text2).split())
    
    if not norm_text1 and not norm_text2:
        return 1.0
    if not norm_text1 or not norm_text2:
        return 0.0
    
    # Calculate Jaccard similarity
    intersection = norm_text1.intersection(norm_text2)
    union = norm_text1.union(norm_text2)
    
    return len(intersection) / len(union)


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks."""
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Move start forward by chunk_size minus overlap
        start = end - overlap
        
        # If the remaining text is less than chunk_size, include it as the last chunk
        if len(text) - end < chunk_size:
            if end < len(text):
                chunks.append(text[end:])
            break
    
    return chunks


def find_closest_match(query: str, candidates: List[str], threshold: float = 0.5) -> str:
    """Find the closest matching string from a list of candidates."""
    best_match = None
    best_similarity = 0.0
    
    for candidate in candidates:
        similarity = calculate_text_similarity(query, candidate)
        if similarity > best_similarity and similarity >= threshold:
            best_similarity = similarity
            best_match = candidate
    
    return best_match