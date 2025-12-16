from typing import List, Dict, Any
from .models import ContentChunk, SourceReference
import hashlib


class SourceValidator:
    """Validate source mapping accuracy and completeness."""
    
    @staticmethod
    def validate_source_reference(source_ref: SourceReference) -> Dict[str, Any]:
        """
        Validate a single source reference for completeness and accuracy.
        
        Args:
            source_ref: The SourceReference to validate
            
        Returns:
            Dictionary with validation results
        """
        validation_results = {
            'is_valid': True,
            'missing_fields': [],
            'issues': [],
            'confidence_score': 1.0
        }
        
        # Check required fields
        if not source_ref.book_title or source_ref.book_title == 'Unknown':
            validation_results['missing_fields'].append('book_title')
            validation_results['is_valid'] = False
        
        if not source_ref.chapter or source_ref.chapter == 'Unknown':
            validation_results['missing_fields'].append('chapter')
            validation_results['is_valid'] = False
        
        if source_ref.page_number <= 0:
            validation_results['missing_fields'].append('page_number')
            validation_results['is_valid'] = False
        
        if not source_ref.section or source_ref.section == 'Unknown':
            validation_results['missing_fields'].append('section')
            validation_results['is_valid'] = False
        
        # Check optional but important fields
        if not source_ref.collection_name:
            validation_results['issues'].append('collection_name is missing')
        
        if not source_ref.document_id:
            validation_results['issues'].append('document_id is missing')
        
        # Calculate confidence score based on completeness
        total_fields = 9  # Total number of fields in SourceReference
        present_fields = total_fields - len(validation_results['missing_fields'])
        validation_results['confidence_score'] = present_fields / total_fields
        
        return validation_results
    
    @staticmethod
    def validate_content_integrity(chunk: ContentChunk) -> Dict[str, Any]:
        """
        Validate that the content chunk matches its source reference.
        
        Args:
            chunk: The ContentChunk to validate
            
        Returns:
            Dictionary with validation results
        """
        validation_results = {
            'is_content_valid': True,
            'content_matches_hash': True,
            'content_length_matches': True,
            'issues': []
        }
        
        # Check if content length matches the stored length
        if chunk.source_reference.original_content_length is not None:
            if len(chunk.content) != chunk.source_reference.original_content_length:
                validation_results['content_length_matches'] = False
                validation_results['issues'].append(
                    f"Content length mismatch: expected {chunk.source_reference.original_content_length}, "
                    f"got {len(chunk.content)}"
                )
        
        # Check if content hash matches (if available)
        if chunk.source_reference.content_hash:
            current_hash = hashlib.sha256(chunk.content.encode()).hexdigest()
            if current_hash != chunk.source_reference.content_hash:
                validation_results['content_matches_hash'] = False
                validation_results['issues'].append(
                    "Content hash mismatch - content may have been modified"
                )
        
        # Overall validation
        validation_results['is_content_valid'] = (
            validation_results['content_length_matches'] and 
            validation_results['content_matches_hash']
        )
        
        return validation_results
    
    @staticmethod
    def validate_chunk_source_mapping(chunk: ContentChunk) -> Dict[str, Any]:
        """
        Validate the complete source mapping for a content chunk.
        
        Args:
            chunk: The ContentChunk to validate
            
        Returns:
            Dictionary with comprehensive validation results
        """
        # Validate the source reference
        source_validation = SourceValidator.validate_source_reference(chunk.source_reference)
        
        # Validate content integrity
        content_validation = SourceValidator.validate_content_integrity(chunk)
        
        # Combine results
        validation_results = {
            'chunk_id': chunk.id,
            'source_reference_valid': source_validation['is_valid'],
            'content_valid': content_validation['is_content_valid'],
            'overall_validity': source_validation['is_valid'] and content_validation['is_content_valid'],
            'source_validation': source_validation,
            'content_validation': content_validation
        }
        
        return validation_results
    
    @staticmethod
    def validate_multiple_chunks_source_mapping(chunks: List[ContentChunk]) -> Dict[str, Any]:
        """
        Validate source mapping for multiple content chunks.
        
        Args:
            chunks: List of ContentChunk objects to validate
            
        Returns:
            Dictionary with aggregated validation results
        """
        results = []
        total_chunks = len(chunks)
        valid_source_refs = 0
        valid_content = 0
        valid_overall = 0
        
        for chunk in chunks:
            chunk_result = SourceValidator.validate_chunk_source_mapping(chunk)
            results.append(chunk_result)
            
            if chunk_result['source_reference_valid']:
                valid_source_refs += 1
            if chunk_result['content_valid']:
                valid_content += 1
            if chunk_result['overall_validity']:
                valid_overall += 1
        
        # Calculate accuracy rates
        source_accuracy = valid_source_refs / total_chunks if total_chunks > 0 else 0
        content_accuracy = valid_content / total_chunks if total_chunks > 0 else 0
        overall_accuracy = valid_overall / total_chunks if total_chunks > 0 else 0
        
        aggregated_results = {
            'total_chunks': total_chunks,
            'valid_source_references': valid_source_refs,
            'valid_content': valid_content,
            'valid_overall': valid_overall,
            'source_accuracy_rate': source_accuracy,
            'content_accuracy_rate': content_accuracy,
            'overall_accuracy_rate': overall_accuracy,
            'detailed_results': results
        }
        
        return aggregated_results