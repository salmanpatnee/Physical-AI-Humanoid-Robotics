import hashlib
import json
from typing import Any, Optional, Dict
from datetime import datetime, timedelta
import threading


class CachingService:
    """
    A simple in-memory cache service for storing and retrieving 
    answers to frequently asked questions.
    """
    
    def __init__(self, default_ttl: int = 3600):  # Default TTL: 1 hour
        self.cache: Dict[str, Any] = {}
        self.timestamps: Dict[str, datetime] = {}
        self.default_ttl = default_ttl  # Time to live in seconds
        self._lock = threading.Lock()  # For thread safety
    
    def _generate_key(self, question: str, book_id: Optional[str] = None) -> str:
        """
        Generate a unique cache key based on the question and optional book_id.
        
        Args:
            question: The question text
            book_id: Optional book identifier
            
        Returns:
            A unique cache key
        """
        key_data = {
            "question": question.lower().strip(),
            "book_id": book_id
        }
        key_json = json.dumps(key_data, sort_keys=True)
        return hashlib.md5(key_json.encode()).hexdigest()
    
    def get(self, question: str, book_id: Optional[str] = None) -> Optional[Any]:
        """
        Retrieve a cached response.
        
        Args:
            question: The question text
            book_id: Optional book identifier
            
        Returns:
            Cached response if found and not expired, None otherwise
        """
        key = self._generate_key(question, book_id)
        
        with self._lock:
            # Check if key exists
            if key not in self.cache:
                return None
            
            # Check if the entry has expired
            if datetime.now() > self.timestamps[key]:
                # Entry expired, remove it
                del self.cache[key]
                del self.timestamps[key]
                return None
            
            return self.cache[key]
    
    def set(self, question: str, response: Any, ttl: Optional[int] = None, book_id: Optional[str] = None):
        """
        Store a response in the cache.
        
        Args:
            question: The question text
            response: The response to cache
            ttl: Time to live in seconds (optional, uses default if not provided)
            book_id: Optional book identifier
        """
        if ttl is None:
            ttl = self.default_ttl
            
        key = self._generate_key(question, book_id)
        expiration_time = datetime.now() + timedelta(seconds=ttl)
        
        with self._lock:
            self.cache[key] = response
            self.timestamps[key] = expiration_time
    
    def invalidate(self, question: str, book_id: Optional[str] = None):
        """
        Remove a specific entry from the cache.
        
        Args:
            question: The question text
            book_id: Optional book identifier
        """
        key = self._generate_key(question, book_id)
        
        with self._lock:
            if key in self.cache:
                del self.cache[key]
                if key in self.timestamps:
                    del self.timestamps[key]
    
    def clear(self):
        """
        Clear all entries from the cache.
        """
        with self._lock:
            self.cache.clear()
            self.timestamps.clear()
    
    def size(self) -> int:
        """
        Get the number of entries in the cache.
        
        Returns:
            Number of cached entries
        """
        return len(self.cache)