import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to manage environment variables for the validation pipeline."""
    
    # Qdrant Configuration
    QDRANT_URL: str = os.getenv("QDRANT_URL", "")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    
    # Validation Configuration
    DEFAULT_LIMIT: int = int(os.getenv("DEFAULT_LIMIT", 5))
    DEFAULT_THRESHOLD: float = float(os.getenv("DEFAULT_THRESHOLD", 0.5))
    
    # File paths
    RESULTS_FILE_PATH: str = os.getenv("RESULTS_FILE_PATH", "validation_results.csv")
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that required configuration values are present."""
        return bool(cls.QDRANT_URL and cls.QDRANT_API_KEY)

    @classmethod
    def validate_complete_config(cls) -> tuple[bool, list[str]]:
        """Validate all configuration values and return detailed results."""
        errors = []

        if not cls.QDRANT_URL:
            errors.append("QDRANT_URL is required but not set")
        if not cls.QDRANT_API_KEY:
            errors.append("QDRANT_API_KEY is required but not set")
        if cls.QDRANT_PORT <= 0:
            errors.append("QDRANT_PORT must be a positive integer")
        if cls.DEFAULT_LIMIT <= 0:
            errors.append("DEFAULT_LIMIT must be a positive integer")
        if cls.DEFAULT_THRESHOLD <= 0 or cls.DEFAULT_THRESHOLD > 1:
            errors.append("DEFAULT_THRESHOLD must be between 0 and 1")

        return len(errors) == 0, errors
    
    @classmethod
    def get_qdrant_client_params(cls) -> dict:
        """Get parameters for initializing Qdrant client."""
        params = {
            "url": cls.QDRANT_URL,
            "port": cls.QDRANT_PORT,
        }
        
        if cls.QDRANT_API_KEY:
            params["api_key"] = cls.QDRANT_API_KEY
            
        return params