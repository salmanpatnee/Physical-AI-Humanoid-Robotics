from fastapi import FastAPI
from src.api.routes import router
import uvicorn
import os
from src.config import validate_environment, setup_logging
from src.middleware.error_handler import ErrorHandlingMiddleware
from src.middleware.security_headers import SecurityHeadersMiddleware

# Set up logging first
setup_logging()

# Validate environment variables on startup
validate_environment()

app = FastAPI(
    title="Book Agent API",
    description="An API for asking questions about book content and receiving grounded answers with source references",
    version="1.0.0"
)

# Add middleware (order matters)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(ErrorHandlingMiddleware)

# Include API routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Agent API"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)