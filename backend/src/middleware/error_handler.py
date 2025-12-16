from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging
import traceback
from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as http_ex:
            # Log the HTTP exception
            logger.error(f"HTTP {http_ex.status_code} error for {request.url.path}: {http_ex.detail}")
            return JSONResponse(
                status_code=http_ex.status_code,
                content={"detail": http_ex.detail}
            )
        except Exception as ex:
            # Log the full exception with traceback
            logger.error(f"Unexpected error for {request.url.path}: {str(ex)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            
            # Return a generic error response
            return JSONResponse(
                status_code=500,
                content={"detail": "An unexpected error occurred. Please try again later."}
            )