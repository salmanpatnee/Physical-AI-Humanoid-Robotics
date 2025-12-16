import time
import threading
from enum import Enum
from typing import Callable, Any, Optional


class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Trip to prevent calls
    HALF_OPEN = "half_open" # Test if we can close again


class CircuitBreaker:
    """
    A simple circuit breaker implementation for external API calls
    """
    
    def __init__(self, 
                 failure_threshold: int = 5, 
                 recovery_timeout: int = 60, 
                 expected_exception: type = Exception):
        self.failure_threshold = failure_threshold  # Number of failures to trip
        self.recovery_timeout = recovery_timeout    # Time in seconds to wait before half-open
        self.expected_exception = expected_exception
        
        # State variables
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time = None
        
        # For thread safety
        self._lock = threading.Lock()
    
    @property
    def state(self) -> CircuitState:
        return self._state
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Call the provided function with circuit breaker protection
        """
        with self._lock:
            # If open, fail fast
            if self._state == CircuitState.OPEN:
                if time.time() - self._last_failure_time >= self.recovery_timeout:
                    # Move to half-open after timeout
                    self._state = CircuitState.HALF_OPEN
                else:
                    raise Exception(f"Circuit breaker is OPEN. Last failure: {self._last_failure_time}")
        
        try:
            result = func(*args, **kwargs)
            
            # Success - reset failure count
            with self._lock:
                self._failure_count = 0
                self._state = CircuitState.CLOSED
            
            return result
            
        except self.expected_exception as e:
            # Failure - increment counter and possibly trip
            with self._lock:
                self._failure_count += 1
                self._last_failure_time = time.time()
                
                if self._failure_count >= self.failure_threshold:
                    self._state = CircuitState.OPEN
                    
            raise e


class ExternalService:
    """
    Wrapper for external service calls with circuit breaker protection
    """
    
    def __init__(self, name: str = "ExternalService"):
        self.name = name
        self.circuit_breaker = CircuitBreaker()
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Make a call to an external service with circuit breaker protection
        """
        return self.circuit_breaker.call(func, *args, **kwargs)


# Create circuit breakers for specific services
openai_circuit_breaker = ExternalService("OpenAI")
qdrant_circuit_breaker = ExternalService("Qdrant")