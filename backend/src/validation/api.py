from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
import time

from .models import QueryRequest, ValidationResult, ContentChunk
from .qdrant_connector import QdrantConnector
from .retrieval_validator import RetrievalValidator
from .logger import ValidationLogger
from .config import Config
from .query_generator import QueryGenerator
from .utils import generate_validation_id


# Initialize FastAPI application
app = FastAPI(title="Validation API", description="API for validating retrieval pipeline")


# Request/Response Models for API
class ValidateQueryRequest(BaseModel):
    question: str
    expected_sources: Optional[List[str]] = None
    module_context: Optional[str] = None


class ValidateBatchRequest(BaseModel):
    queries: List[ValidateQueryRequest]
    output_file: Optional[str] = "batch_results.csv"


class ValidateQueryResponse(BaseModel):
    validation_id: str
    question: str
    retrieved_chunks: List[ContentChunk]
    relevance_score: float
    source_mapping_accuracy: float
    latency_ms: float
    is_valid: bool
    feedback: str


class ValidationSummaryResponse(BaseModel):
    summary: dict
    recent_validations: List[str]


# Initialize components
config = Config()
if not config.validate_config():
    raise ValueError("Configuration is not valid. Please check your .env file.")

qdrant_connector = QdrantConnector()
logger = ValidationLogger(config.RESULTS_FILE_PATH)
validator = RetrievalValidator(qdrant_connector, logger)
query_generator = QueryGenerator()


@app.post("/validate/query", response_model=ValidateQueryResponse)
async def validate_query(request: ValidateQueryRequest):
    """Submit a query to validate the retrieval pipeline."""
    try:
        # Create a query request object
        query_req = QueryRequest(
            id=generate_validation_id(),
            question=request.question,
            expected_sources=request.expected_sources,
            module_context=request.module_context
        )
        
        # Validate the query
        start_time = time.time()
        result = validator.validate_single_query(query_req)
        latency_ms = (time.time() - start_time) * 1000
        
        # Create and return response
        response = ValidateQueryResponse(
            validation_id=result.id,
            question=request.question,
            retrieved_chunks=result.retrieved_chunks,
            relevance_score=result.relevance_score,
            source_mapping_accuracy=result.source_mapping_accuracy,
            latency_ms=result.latency_ms,
            is_valid=result.is_valid,
            feedback=result.feedback
        )
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during validation: {str(e)}")


@app.get("/validate/results/{validation_id}", response_model=ValidateQueryResponse)
async def get_validation_result(validation_id: str):
    """Retrieve detailed results for a specific validation request."""
    # In a full implementation, we'd retrieve the result from storage
    # For now, we'll return a placeholder error
    raise HTTPException(
        status_code=404, 
        detail="Detailed result retrieval by ID is not implemented in this version. "
               "Results are logged to CSV files as specified in the configuration."
    )


@app.get("/validate/summary", response_model=ValidationSummaryResponse)
async def get_validation_summary():
    """Get a summary of recent validation results."""
    # In a production implementation, this would aggregate data from CSV logs
    # For now, we'll provide a basic implementation that can access in-memory data
    # and read from the CSV files if needed

    # This is a simplified implementation - in a real system, we would:
    # 1. Read recent data from the CSV log files
    # 2. Aggregate the information
    # 3. Calculate the summary metrics

    import os
    import pandas as pd  # Using pandas to process the CSV logs

    csv_path = config.RESULTS_FILE_PATH

    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)

            # Calculate summary metrics from the CSV data
            total_validations = len(df)
            avg_relevance_score = df['relevance_score'].mean() if 'relevance_score' in df.columns else 0.0
            avg_source_mapping_accuracy = df['source_mapping_accuracy'].mean() if 'source_mapping_accuracy' in df.columns else 0.0
            avg_latency_ms = df['latency_ms'].mean() if 'latency_ms' in df.columns else 0.0

            # Group by module if available
            accuracy_by_module = {}
            if 'module_name' in df.columns:
                module_group = df.groupby('module_name').agg({
                    'relevance_score': 'mean',
                    'source_mapping_accuracy': 'mean',
                    'latency_ms': 'mean'
                }).to_dict('index')

                for module, metrics in module_group.items():
                    accuracy_by_module[module] = {
                        "avg_relevance": metrics['relevance_score'],
                        "avg_source_accuracy": metrics['source_mapping_accuracy'],
                        "avg_latency": metrics['latency_ms']
                    }
            else:
                accuracy_by_module = {
                    "overall": {
                        "avg_relevance": avg_relevance_score,
                        "avg_source_accuracy": avg_source_mapping_accuracy,
                        "avg_latency": avg_latency_ms
                    }
                }

            # Get recent validation IDs
            recent_validations = df['validation_id'].tail(10).tolist() if 'validation_id' in df.columns else []

            summary = {
                "total_validations": int(total_validations),
                "avg_relevance_score": float(avg_relevance_score),
                "avg_source_mapping_accuracy": float(avg_source_mapping_accuracy),
                "avg_latency_ms": float(avg_latency_ms),
                "accuracy_by_module": accuracy_by_module,
                "last_updated": df['timestamp'].max() if 'timestamp' in df.columns else "N/A"
            }

        except Exception as e:
            # If there's an error reading the CSV, return basic metrics
            summary = {
                "total_validations": 0,
                "avg_relevance_score": 0.0,
                "avg_source_mapping_accuracy": 0.0,
                "avg_latency_ms": 0.0,
                "accuracy_by_module": {},
                "error_reading_logs": str(e)
            }
            recent_validations = []
    else:
        # CSV file doesn't exist yet
        summary = {
            "total_validations": 0,
            "avg_relevance_score": 0.0,
            "avg_source_mapping_accuracy": 0.0,
            "avg_latency_ms": 0.0,
            "accuracy_by_module": {}
        }
        recent_validations = []

    return ValidationSummaryResponse(
        summary=summary,
        recent_validations=recent_validations
    )


@app.post("/validate/batch")
async def validate_batch(request: ValidateBatchRequest):
    """Submit multiple queries for validation in a batch operation."""
    try:
        # Convert API requests to internal QueryRequest objects
        query_requests = []
        for api_req in request.queries:
            query_req = QueryRequest(
                id=generate_validation_id(),
                question=api_req.question,
                expected_sources=api_req.expected_sources,
                module_context=api_req.module_context
            )
            query_requests.append(query_req)

        # Update logger to use the specified output file
        batch_logger = ValidationLogger(request.output_file)

        # Validate all queries in the batch
        results = []
        failed_queries = 0

        for query_req in query_requests:
            try:
                result = validator.validate_single_query(query_req)
                results.append(result)

                # Log the result with the batch logger
                batch_logger.log_validation_result(result)
            except Exception as e:
                failed_queries += 1
                print(f"Failed to validate query '{query_req.question[:50]}...': {str(e)}")
                continue  # Continue with the next query

        # Calculate batch statistics
        if results:
            total_relevance = sum(r.relevance_score for r in results)
            avg_relevance = total_relevance / len(results)

            total_source_acc = sum(r.source_mapping_accuracy for r in results)
            avg_source_mapping_accuracy = total_source_acc / len(results)

            total_latency = sum(r.latency_ms for r in results)
            avg_latency = total_latency / len(results)
        else:
            avg_relevance = 0.0
            avg_source_mapping_accuracy = 0.0
            avg_latency = 0.0

        return {
            "batch_id": generate_validation_id(),
            "total_queries": len(request.queries),
            "successful_validations": len(results),
            "failed_validations": failed_queries,
            "status": "completed" if not failed_queries else "completed_with_errors",
            "results_file": request.output_file,
            "processed_count": len(results),
            "statistics": {
                "avg_relevance_score": avg_relevance,
                "avg_source_mapping_accuracy": avg_source_mapping_accuracy,
                "avg_latency_ms": avg_latency
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during batch validation: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint to verify the service is running."""
    try:
        is_connected = qdrant_connector.verify_connection()
        if not is_connected:
            raise HTTPException(status_code=503, detail="Cannot connect to Qdrant")
        
        return {"status": "healthy", "qdrant_connection": "ok"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")