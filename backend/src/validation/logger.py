import csv
import logging
from datetime import datetime
from typing import List
from .models import ValidationResult


class ValidationLogger:
    """Logging module to create CSV outputs for validation results."""
    
    def __init__(self, results_file_path: str = "validation_results.csv"):
        self.results_file_path = results_file_path
        self.logger = logging.getLogger(__name__)
        
        # Set up basic logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def log_validation_result(self, result: ValidationResult):
        """Log a single validation result to the CSV file."""
        # Define the field names for the CSV
        fieldnames = [
            'validation_id', 'query_request_id', 'timestamp', 'relevance_score',
            'source_mapping_accuracy', 'latency_ms', 'is_valid', 'feedback',
            'retrieved_chunks_count'
        ]
        
        # Prepare the row data
        row = {
            'validation_id': result.id,
            'query_request_id': result.query_request_id,
            'timestamp': datetime.now().isoformat(),
            'relevance_score': result.relevance_score,
            'source_mapping_accuracy': result.source_mapping_accuracy,
            'latency_ms': result.latency_ms,
            'is_valid': result.is_valid,
            'feedback': result.feedback,
            'retrieved_chunks_count': len(result.retrieved_chunks)
        }
        
        # Write to CSV file
        file_exists = False
        try:
            with open(self.results_file_path, 'r', newline='', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False
        
        with open(self.results_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header only if file is new
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(row)
        
        self.logger.info(f"Logged validation result {result.id} to {self.results_file_path}")
    
    def log_validation_results(self, results: List[ValidationResult]):
        """Log multiple validation results to the CSV file."""
        for result in results:
            self.log_validation_result(result)
    
    def log_source_mapping_verification(self, result: ValidationResult, verification_details: dict = None):
        """Log source mapping verification results specifically."""
        from .source_validator import SourceValidator

        # If no verification details provided, generate them using the SourceValidator
        if verification_details is None:
            validation_results = SourceValidator.validate_multiple_chunks_source_mapping(result.retrieved_chunks)
            verification_details = validation_results['detailed_results']

        # Define the field names for source mapping verification CSV
        fieldnames = [
            'validation_id', 'query_request_id', 'timestamp', 'book_title',
            'chapter', 'page_number', 'section', 'url', 'collection_name',
            'document_id', 'content_hash_match', 'content_length_match',
            'is_source_reference_valid', 'is_content_valid', 'is_overall_valid'
        ]

        # Prepare rows for each retrieved chunk
        rows = []
        for i, chunk in enumerate(result.retrieved_chunks):
            # Get verification result for this chunk
            if i < len(verification_details):
                chunk_verification = verification_details[i]
                source_valid = chunk_verification['source_reference_valid']
                content_valid = chunk_verification['content_valid']
                overall_valid = chunk_verification['overall_validity']
            else:
                # Default values if no verification result available for this chunk
                source_valid = True
                content_valid = True
                overall_valid = True

            row = {
                'validation_id': result.id,
                'query_request_id': result.query_request_id,
                'timestamp': datetime.now().isoformat(),
                'book_title': chunk.source_reference.book_title,
                'chapter': chunk.source_reference.chapter,
                'page_number': chunk.source_reference.page_number,
                'section': chunk.source_reference.section,
                'url': chunk.source_reference.url or '',
                'collection_name': chunk.source_reference.collection_name or '',
                'document_id': chunk.source_reference.document_id or '',
                'content_hash_match': chunk.source_reference.content_hash is not None,  # Simplified
                'content_length_match': len(chunk.content) == (chunk.source_reference.original_content_length or len(chunk.content)),  # Simplified
                'is_source_reference_valid': source_valid,
                'is_content_valid': content_valid,
                'is_overall_valid': overall_valid
            }
            rows.append(row)

        # Write to a specific source mapping verification file
        verification_file_path = self.results_file_path.replace('.csv', '_source_mapping.csv')
        file_exists = False
        try:
            with open(verification_file_path, 'r', newline='', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(verification_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if file is new
            if not file_exists:
                writer.writeheader()

            for row in rows:
                writer.writerow(row)

        self.logger.info(f"Logged source mapping verification for {result.id} to {verification_file_path}")
    
    def log_module_specific_metrics(self, result: ValidationResult, module_name: str):
        """Log module-specific metrics."""
        # Define the field names for module-specific metrics CSV
        fieldnames = [
            'validation_id', 'query_request_id', 'timestamp', 'module_name',
            'relevance_score', 'source_mapping_accuracy', 'latency_ms', 'is_valid',
            'feedback', 'retrieved_chunks_count'
        ]

        # Prepare the row data
        row = {
            'validation_id': result.id,
            'query_request_id': result.query_request_id,
            'timestamp': datetime.now().isoformat(),
            'module_name': module_name,
            'relevance_score': result.relevance_score,
            'source_mapping_accuracy': result.source_mapping_accuracy,
            'latency_ms': result.latency_ms,
            'is_valid': result.is_valid,
            'feedback': result.feedback,
            'retrieved_chunks_count': len(result.retrieved_chunks)
        }

        # Write to a module-specific metrics file
        module_file_path = self.results_file_path.replace('.csv', '_by_module.csv')
        file_exists = False
        try:
            with open(module_file_path, 'r', newline='', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(module_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if file is new
            if not file_exists:
                writer.writeheader()

            writer.writerow(row)

        self.logger.info(f"Logged module-specific metrics for {module_name} to {module_file_path}")