import os
import logging
from typing import Optional


class Config:
    """
    Configuration class to handle environment variables and application settings
    """
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    QDRANT_URL: Optional[str] = os.getenv("QDRANT_URL")
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")

    # Optional configuration with defaults
    DEFAULT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME", "book_content")
    DEFAULT_RELEVANCE_THRESHOLD: float = float(os.getenv("DEFAULT_RELEVANCE_THRESHOLD", "0.7"))
    DEFAULT_MAX_CONTENT_LENGTH: int = int(os.getenv("DEFAULT_MAX_CONTENT_LENGTH", "2000"))

    # Timeout settings
    OPENAI_REQUEST_TIMEOUT: int = int(os.getenv("OPENAI_REQUEST_TIMEOUT", "30"))  # 30 seconds default
    QDRANT_REQUEST_TIMEOUT: int = int(os.getenv("QDRANT_REQUEST_TIMEOUT", "10"))  # 10 seconds default


def setup_logging():
    """
    Set up logging configuration for the application
    """
    # Create a custom format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Configure the root logger
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(),  # Log to console
            # In production, you might also want to log to a file
        ]
    )

    # Set specific loggers to appropriate levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("qdrant_client").setLevel(logging.WARNING)  # Reduce Qdrant client logs
    logging.getLogger("openai").setLevel(logging.WARNING)       # Reduce OpenAI logs


def validate_environment() -> bool:
    """
    Validate that all required environment variables are set.
    Raises an exception if any required variable is missing.
    """
    missing_vars = []
    
    if not Config.OPENAI_API_KEY:
        missing_vars.append("OPENAI_API_KEY")
    
    if not Config.QDRANT_URL:
        missing_vars.append("QDRANT_URL")
    
    if not Config.QDRANT_API_KEY:
        missing_vars.append("QDRANT_API_KEY")
    
    if missing_vars:
        missing_str = ", ".join(missing_vars)
        raise EnvironmentError(
            f"Missing required environment variables: {missing_str}\n"
            f"Please set them in your environment or .env file.\n"
            f"Refer to .env.example for the required variables."
        )
    
    return True