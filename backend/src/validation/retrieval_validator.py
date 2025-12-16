import time
from datetime import datetime
from typing import List, Optional
from .models import QueryRequest, ValidationResult, ContentChunk, Module
from .qdrant_connector import QdrantConnector
from .metrics import ValidationMetricsCalculator
from .logger import ValidationLogger
from .utils import generate_validation_id
import logging


class RetrievalValidator:
    """Main validation logic for validating retrieval pipeline."""
    
    def __init__(self, qdrant_connector: QdrantConnector, logger: ValidationLogger = None):
        self.qdrant_connector = qdrant_connector
        self.metrics_calculator = ValidationMetricsCalculator()
        self.logger = logger or ValidationLogger()
        self.logger.logger = logging.getLogger(__name__)

    def _calculate_similarity_score(self, query_text: str, retrieved_chunks: List[ContentChunk]) -> float:
        """
        Calculate topical relevance of returned chunks to the query.

        Args:
            query_text: The original query text
            retrieved_chunks: List of chunks retrieved from the database

        Returns:
            Similarity score between 0 and 1
        """
        if not query_text or not retrieved_chunks:
            return 0.0

        # Extract keywords from the query
        from .utils import extract_keywords
        query_keywords = extract_keywords(query_text, num_keywords=20)
        if not query_keywords:
            return 0.0

        # Calculate how many keywords appear in the retrieved content
        total_content = " ".join([chunk.content for chunk in retrieved_chunks]).lower()

        # Count keyword matches
        matched_keywords = 0
        for keyword in query_keywords:
            if keyword.lower() in total_content:
                matched_keywords += 1

        # Calculate relevance score based on keyword matching
        relevance_score = matched_keywords / len(query_keywords)

        # Also factor in the similarity scores from the Qdrant search
        if retrieved_chunks:
            avg_qdrant_score = sum(chunk.similarity_score for chunk in retrieved_chunks) / len(retrieved_chunks)
            # Combine our keyword-based score with Qdrant's similarity score
            # Weight slightly more toward Qdrant's score as it's more sophisticated
            relevance_score = 0.3 * relevance_score + 0.7 * avg_qdrant_score

        return min(relevance_score, 1.0)  # Ensure score doesn't exceed 1.0

    def _aggregate_and_rank_chunks(self, chunks: List[ContentChunk]) -> List[ContentChunk]:
        """
        Aggregate and rank retrieved chunks based on relevance and other factors.

        Args:
            chunks: List of content chunks retrieved from the database

        Returns:
            List of aggregated and ranked chunks
        """
        if not chunks:
            return chunks

        # Sort by similarity score (descending) to maintain ranking from Qdrant
        sorted_chunks = sorted(chunks, key=lambda chunk: chunk.similarity_score, reverse=True)

        # Add position_in_result based on the sorted order
        for i, chunk in enumerate(sorted_chunks):
            chunk.position_in_result = i + 1

        # Additional ranking logic could be implemented here
        # For example, we might want to boost chunks based on:
        # - Source reference quality (if certain modules are more relevant)
        # - Content length (to avoid very short chunks)
        # - Recency of the source material (if applicable)

        return sorted_chunks

    def validate_single_query(
        self, 
        query_request: QueryRequest, 
        collection_name: str = None,
        limit: int = 5,
        threshold: float = 0.5
    ) -> ValidationResult:
        """
        Validate a single query against the retrieval pipeline.
        
        Args:
            query_request: The query request to validate
            collection_name: Name of the collection to search in (if None, will try to determine from context)
            limit: Maximum number of results to retrieve
            threshold: Minimum similarity score threshold
            
        Returns:
            ValidationResult containing the validation results
        """
        start_time = time.time()

        # Track sub-components of latency
        search_start_time = time.time()

        try:
            # Determine collection name based on module context if not provided
            if not collection_name:
                if query_request.module_context:
                    collection_name = query_request.module_context
                else:
                    # Use the first available collection if no context provided
                    available_modules = self.qdrant_connector.get_available_collections()
                    if available_modules:
                        collection_name = available_modules[0].qdrant_collection_name
                    else:
                        raise ValueError("No collections found in Qdrant")

            # Perform the search
            retrieved_chunks = self.qdrant_connector.search(
                query_text=query_request.question,
                collection_name=collection_name,
                limit=limit,
                threshold=threshold
            )

            search_latency = (time.time() - search_start_time) * 1000

            # Calculate metrics
            relevance_score = self._calculate_similarity_score(query_request.question, retrieved_chunks)

            # Verify source mapping using the new SourceValidator
            from .source_validator import SourceValidator
            source_validation_results = SourceValidator.validate_multiple_chunks_source_mapping(retrieved_chunks)
            source_mapping_accuracy = source_validation_results['overall_accuracy_rate']

            # Calculate total latency
            latency_ms = (time.time() - start_time) * 1000

            # Log detailed timing information if needed (for debugging/performance analysis)
            if latency_ms > 1000:  # If taking more than 1 second
                self.logger.logger.info(
                    f"Slow validation detected: {latency_ms:.2f}ms for query '{query_request.question[:50]}...'. "
                    f"Search component: {search_latency:.2f}ms"
                )
            
            # Determine if validation is successful based on thresholds
            is_valid = relevance_score >= 0.7 and source_mapping_accuracy >= 0.9 and latency_ms <= 2000  # 2 seconds
            
            # Generate feedback
            feedback_parts = []
            if relevance_score < 0.7:
                feedback_parts.append(f"Relevance score {relevance_score:.2f} below threshold")
            if source_mapping_accuracy < 0.9:
                feedback_parts.append(f"Source mapping accuracy {source_mapping_accuracy:.2f} below threshold")
            if latency_ms > 2000:
                feedback_parts.append(f"Latency {latency_ms:.2f}ms above threshold")
                
            if not feedback_parts:
                feedback_parts.append("Query successfully validated")
            
            feedback = "; ".join(feedback_parts)
            
            # Create validation result
            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=retrieved_chunks,
                relevance_score=relevance_score,
                source_mapping_accuracy=source_mapping_accuracy,
                latency_ms=latency_ms,
                is_valid=is_valid,
                feedback=feedback
            )
            
            # Log the result
            self.logger.log_validation_result(result)
            
            return result
            
        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000
            
            # Create a validation result indicating failure
            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=[],
                relevance_score=0.0,
                source_mapping_accuracy=0.0,
                latency_ms=latency_ms,
                is_valid=False,
                feedback=f"Error during validation: {str(e)}"
            )
            
            # Log the result
            self.logger.log_validation_result(result)
            
            # Re-raise the exception to indicate failure
            raise
    
    def validate_query_batch(
        self, 
        query_requests: List[QueryRequest], 
        collection_name: str = None,
        limit: int = 5,
        threshold: float = 0.5
    ) -> List[ValidationResult]:
        """
        Validate multiple queries in a batch.
        
        Args:
            query_requests: List of query requests to validate
            collection_name: Name of the collection to search in
            limit: Maximum number of results to retrieve
            threshold: Minimum similarity score threshold
            
        Returns:
            List of ValidationResult objects
        """
        results = []
        for query_request in query_requests:
            result = self.validate_single_query(query_request, collection_name, limit, threshold)
            results.append(result)
        return results
    
    def validate_modules(self, module_names: List[str], queries_per_module: int = 3) -> List[ValidationResult]:
        """
        Validate retrieval across multiple modules.
        
        Args:
            module_names: List of module names to validate
            queries_per_module: Number of queries to run per module
            
        Returns:
            List of ValidationResult objects for all queries across all modules
        """
        results = []
        
        for module_name in module_names:
            # Generate queries specific to this module
            # For simplicity, using general queries - in a real implementation, 
            # we might want more targeted queries for each module
            for _ in range(queries_per_module):
                # Create a sample query request for this module
                query_request = QueryRequest(
                    id=generate_validation_id(),
                    question=f"What are the key concepts in {module_name}?",
                    module_context=module_name
                )
                
                result = self.validate_single_query(query_request, collection_name=module_name)
                results.append(result)
        
        return results
    
    def validate_source_mapping(self, query_request: QueryRequest, collection_name: str = None) -> ValidationResult:
        """
        Specifically validate the source mapping accuracy.
        
        Args:
            query_request: The query request to validate for source mapping
            collection_name: Name of the collection to search in
            
        Returns:
            ValidationResult containing the source mapping validation results
        """
        start_time = time.time()
        
        try:
            # Perform the search
            if not collection_name and query_request.module_context:
                collection_name = query_request.module_context

            if not collection_name:
                available_modules = self.qdrant_connector.get_available_collections()
                if available_modules:
                    collection_name = available_modules[0].qdrant_collection_name
                else:
                    raise ValueError("No collections found in Qdrant")

            retrieved_chunks = self.qdrant_connector.search(
                query_text=query_request.question,
                collection_name=collection_name
            )

            # Apply response aggregation to ensure chunks are properly ranked
            retrieved_chunks = self._aggregate_and_rank_chunks(retrieved_chunks)
            
            # Calculate source mapping accuracy specifically
            source_mapping_accuracy = self.metrics_calculator.calculate_source_mapping_accuracy(
                retrieved_chunks, query_request.expected_sources
            )
            
            # For source mapping validation, relevance is less important
            # We're primarily focused on whether sources are correctly mapped
            relevance_score = 1.0  # We'll consider this perfect for source mapping validation
            
            # Calculate latency
            latency_ms = (time.time() - start_time) * 1000
            
            # Determine if source mapping is valid
            is_valid = source_mapping_accuracy >= 0.9
            
            feedback = f"Source mapping accuracy: {source_mapping_accuracy:.2f}"
            if not is_valid:
                feedback += f" (below threshold of 0.9)"
            
            # Create validation result
            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=retrieved_chunks,
                relevance_score=relevance_score,
                source_mapping_accuracy=source_mapping_accuracy,
                latency_ms=latency_ms,
                is_valid=is_valid,
                feedback=feedback
            )
            
            # Log the source mapping verification
            verification_details = {chunk.id: True for chunk in retrieved_chunks}  # Simplified
            self.logger.log_source_mapping_verification(result, verification_details)
            
            return result
            
        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000
            
            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=[],
                relevance_score=0.0,
                source_mapping_accuracy=0.0,
                latency_ms=latency_ms,
                is_valid=False,
                feedback=f"Error during source mapping validation: {str(e)}"
            )
            
            self.logger.log_validation_result(result)
            raise
    
    def update_cross_module_validation(
        self,
        query_request: QueryRequest,
        modules_to_check: List[Module]
    ) -> ValidationResult:
        """
        Update validation to include cross-module consistency tracking.

        Args:
            query_request: The query request to validate
            modules_to_check: List of modules to validate against

        Returns:
            ValidationResult with information about cross-module consistency
        """
        start_time = time.time()

        try:
            all_chunks = []
            module_results = {}

            # Query each module and collect results
            for module in modules_to_check:
                try:
                    chunks = self.qdrant_connector.search(
                        query_text=query_request.question,
                        collection_name=module.qdrant_collection_name
                    )
                    module_results[module.id] = {
                        'chunks': chunks,
                        'relevance': self._calculate_similarity_score(query_request.question, chunks),
                        'source_accuracy': self.metrics_calculator.calculate_source_mapping_accuracy(chunks),
                        'latency': 0.0  # Will be updated later
                    }
                    all_chunks.extend(chunks)
                except Exception as e:
                    module_results[module.id] = {
                        'chunks': [],
                        'relevance': 0.0,
                        'source_accuracy': 0.0,
                        'error': str(e)
                    }

            # Calculate overall relevance score across all modules
            relevance_scores = [result['relevance'] for result in module_results.values() if 'error' not in result]
            avg_relevance = sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0.0

            # Calculate cross-module consistency
            consistency = self.metrics_calculator.calculate_cross_module_consistency([
                ValidationResult(
                    id=generate_validation_id(),
                    query_request_id=query_request.id,
                    retrieved_chunks=result['chunks'],
                    relevance_score=result['relevance'],
                    source_mapping_accuracy=result['source_accuracy'],
                    latency_ms=100.0,  # Placeholder
                    is_valid=True,  # Placeholder
                    feedback=""  # Placeholder
                )
                for result in module_results.values() if 'error' not in result and result['chunks']
            ])

            # Calculate latency
            latency_ms = (time.time() - start_time) * 1000

            # Overall validation result
            is_valid = avg_relevance >= 0.5 and consistency >= 0.7  # Adjust thresholds as needed

            feedback = f"Avg relevance: {avg_relevance:.2f}, Consistency: {consistency:.2f}"

            # Create validation result
            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=all_chunks[:5],  # Limit for the main result
                relevance_score=avg_relevance,
                source_mapping_accuracy=1.0,  # Placeholder for this validation
                latency_ms=latency_ms,
                is_valid=is_valid,
                feedback=feedback
            )

            # Log module-specific results and update module tracking
            for module_id, module_result in module_results.items():
                module_validation_result = ValidationResult(
                    id=generate_validation_id(),
                    query_request_id=query_request.id,
                    retrieved_chunks=module_result['chunks'],
                    relevance_score=module_result.get('relevance', 0.0),
                    source_mapping_accuracy=module_result.get('source_accuracy', 0.0),
                    latency_ms=module_result.get('latency', latency_ms / len(modules_to_check)),  # Approximate
                    is_valid=module_result.get('relevance', 0.0) >= 0.3,
                    feedback=f"Module {module_id} result"
                )

                # Update the module with validation metrics
                for module in modules_to_check:
                    if module.id == module_id:
                        module.validation_accuracy = module_result.get('relevance', 0.0)
                        module.avg_latency = module_result.latency_ms
                        module.last_validated = datetime.now()
                        break

                self.logger.log_module_specific_metrics(module_validation_result, module_id)

            return result

        except Exception as e:
            latency_ms = (time.time() - start_time) * 1000

            result = ValidationResult(
                id=generate_validation_id(),
                query_request_id=query_request.id,
                retrieved_chunks=[],
                relevance_score=0.0,
                source_mapping_accuracy=0.0,
                latency_ms=latency_ms,
                is_valid=False,
                feedback=f"Error during cross-module validation: {str(e)}"
            )

            self.logger.log_validation_result(result)
            raise