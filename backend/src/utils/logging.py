import logging
import sys
from datetime import datetime
from typing import Any, Dict


class MonitoringLogger:
    """
    A comprehensive logging utility for monitoring and debugging the Book Agent API
    """
    
    def __init__(self, name: str = __name__):
        self.logger = logging.getLogger(name)
    
    def log_api_request(self, 
                       endpoint: str, 
                       method: str, 
                       user_id: str = "anonymous", 
                       params: Dict[str, Any] = None) -> None:
        """
        Log API request details for monitoring
        """
        self.logger.info(
            f"API Request: {method} {endpoint} | User: {user_id} | Params: {params or 'None'}"
        )
    
    def log_api_response(self, 
                        endpoint: str, 
                        response_time: float, 
                        status_code: int, 
                        response_size: int = 0) -> None:
        """
        Log API response details for monitoring
        """
        self.logger.info(
            f"API Response: {endpoint} | Status: {status_code} | "
            f"Time: {response_time:.3f}s | Size: {response_size} bytes"
        )
    
    def log_performance_metric(self, 
                              metric_name: str, 
                              value: float, 
                              unit: str = "", 
                              tags: Dict[str, str] = None) -> None:
        """
        Log performance metrics for monitoring
        """
        tags_str = f" | Tags: {tags}" if tags else ""
        self.logger.info(
            f"Performance Metric: {metric_name} = {value}{unit}{tags_str}"
        )
    
    def log_error(self, 
                  error_type: str, 
                  error_message: str, 
                  context: Dict[str, Any] = None) -> None:
        """
        Log error details with context for debugging
        """
        context_str = f" | Context: {context}" if context else ""
        self.logger.error(
            f"Error: {error_type} | Message: {error_message}{context_str}"
        )
    
    def log_cache_hit(self, cache_key: str, hit: bool) -> None:
        """
        Log cache hit/miss for monitoring
        """
        hit_status = "HIT" if hit else "MISS"
        self.logger.info(f"Cache {hit_status}: {cache_key}")
    
    def log_external_call(self, 
                         service: str, 
                         endpoint: str, 
                         duration: float, 
                         success: bool) -> None:
        """
        Log external service calls for monitoring
        """
        status = "SUCCESS" if success else "FAILED"
        self.logger.info(
            f"External Call: {service}.{endpoint} | Status: {status} | Duration: {duration:.3f}s"
        )


# Create a global instance for easy use throughout the application
monitoring_logger = MonitoringLogger()