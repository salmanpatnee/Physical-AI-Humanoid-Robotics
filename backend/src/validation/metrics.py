from typing import List
from .models import ContentChunk, ValidationResult
import statistics


class ValidationMetricsCalculator:
    """Calculator for relevance scoring and accuracy measurements."""
    
    @staticmethod
    def calculate_relevance_score(expected_content_keywords: List[str], retrieved_chunks: List[ContentChunk]) -> float:
        """
        Calculate relevance score based on keyword matching between expected content and retrieved chunks.
        
        Args:
            expected_content_keywords: List of keywords that should be present in relevant chunks
            retrieved_chunks: List of content chunks retrieved from the database
            
        Returns:
            Relevance score between 0 and 1
        """
        if not expected_content_keywords or not retrieved_chunks:
            return 0.0
        
        # Count how many expected keywords appear in the retrieved content
        found_keywords = set()
        all_retrieved_text = " ".join([chunk.content.lower() for chunk in retrieved_chunks])
        
        for keyword in expected_content_keywords:
            if keyword.lower() in all_retrieved_text:
                found_keywords.add(keyword.lower())
        
        # Calculate score as the ratio of found keywords to expected keywords
        relevance_score = len(found_keywords) / len(expected_content_keywords)
        return min(relevance_score, 1.0)  # Ensure score doesn't exceed 1.0
    
    @staticmethod
    def calculate_source_mapping_accuracy(retrieved_chunks: List[ContentChunk], expected_sources: List[str] = None) -> float:
        """
        Calculate accuracy of source reference mapping.

        Args:
            retrieved_chunks: List of content chunks with source references
            expected_sources: Optional list of expected source identifiers to compare against

        Returns:
            Source mapping accuracy between 0 and 1
        """
        if not retrieved_chunks:
            return 0.0

        # Use the enhanced SourceValidator for comprehensive source mapping validation
        from .source_validator import SourceValidator
        validation_results = SourceValidator.validate_multiple_chunks_source_mapping(retrieved_chunks)
        return validation_results['overall_accuracy_rate']

    @staticmethod
    def calculate_enhanced_source_mapping_accuracy(retrieved_chunks: List[ContentChunk], expected_sources: List[str] = None) -> dict:
        """
        Calculate detailed source mapping accuracy with breakdown by component.

        Args:
            retrieved_chunks: List of content chunks with source references
            expected_sources: Optional list of expected source identifiers to compare against

        Returns:
            Dictionary with detailed accuracy metrics
        """
        if not retrieved_chunks:
            return {
                'overall_accuracy': 0.0,
                'source_reference_accuracy': 0.0,
                'content_accuracy': 0.0,
                'expected_source_match_rate': 0.0
            }

        # Use the enhanced SourceValidator for comprehensive source mapping validation
        from .source_validator import SourceValidator
        validation_results = SourceValidator.validate_multiple_chunks_source_mapping(retrieved_chunks)

        # Calculate expected source match rate if expected sources provided
        expected_match_rate = 0.0
        if expected_sources and retrieved_chunks:
            matching_sources = 0
            for chunk in retrieved_chunks:
                if any(expected_source.lower() in chunk.source_reference.book_title.lower()
                      for expected_source in expected_sources):
                    matching_sources += 1
            expected_match_rate = matching_sources / len(retrieved_chunks)

        return {
            'overall_accuracy': validation_results['overall_accuracy_rate'],
            'source_reference_accuracy': validation_results['source_accuracy_rate'],
            'content_accuracy': validation_results['content_accuracy_rate'],
            'expected_source_match_rate': expected_match_rate
        }
    
    @staticmethod
    def calculate_cross_module_consistency(results: List[ValidationResult]) -> float:
        """
        Calculate consistency of validation results across different modules.

        Args:
            results: List of validation results from different modules

        Returns:
            Consistency score between 0 and 1 (higher variance = lower consistency)
        """
        if not results:
            return 0.0

        if len(results) < 2:
            # With only one result, consistency is not measurable
            return 1.0

        # Extract relevance scores from all results
        relevance_scores = [result.relevance_score for result in results]

        # Calculate standard deviation as a measure of variance
        if len(relevance_scores) > 1:
            std_dev = statistics.stdev(relevance_scores)
            mean_score = statistics.mean(relevance_scores)

            # Normalize the standard deviation to get a consistency measure
            # Lower std_dev means higher consistency
            if mean_score > 0:
                # Using a simple inverse relationship, capped at 1.0
                consistency = max(0.0, 1.0 - (std_dev / mean_score))
            else:
                consistency = 0.0
        else:
            consistency = 1.0

        return consistency

    @staticmethod
    def calculate_enhanced_cross_module_consistency(results: List[ValidationResult]) -> dict:
        """
        Calculate enhanced consistency metrics across modules with breakdown by metric type.

        Args:
            results: List of validation results from different modules

        Returns:
            Dictionary with detailed consistency metrics
        """
        if not results:
            return {
                'relevance_consistency': 0.0,
                'source_mapping_consistency': 0.0,
                'latency_consistency': 0.0,
                'overall_consistency': 0.0,
                'variance_by_metric': {}
            }

        if len(results) < 2:
            # With only one result, consistency is perfect
            return {
                'relevance_consistency': 1.0,
                'source_mapping_consistency': 1.0,
                'latency_consistency': 1.0,
                'overall_consistency': 1.0,
                'variance_by_metric': {
                    'relevance': 0.0,
                    'source_mapping': 0.0,
                    'latency': 0.0
                }
            }

        # Extract scores for different metrics
        relevance_scores = [result.relevance_score for result in results]
        source_mapping_scores = [result.source_mapping_accuracy for result in results]
        latency_scores = [result.latency_ms for result in results]

        # Calculate consistency for each metric
        def calculate_consistency_metric(scores):
            if len(scores) < 2:
                return 1.0

            std_dev = statistics.stdev(scores)
            mean_score = statistics.mean(scores)

            if mean_score != 0:
                return max(0.0, 1.0 - (std_dev / abs(mean_score)))
            else:
                # If mean is 0, consistency depends only on whether all values are 0
                return 1.0 if all(s == 0 for s in scores) else 0.0

        relevance_consistency = calculate_consistency_metric(relevance_scores)
        source_mapping_consistency = calculate_consistency_metric(source_mapping_scores)
        latency_consistency = calculate_consistency_metric(latency_scores)

        # Overall consistency as average of individual consistencies
        overall_consistency = (relevance_consistency + source_mapping_consistency + latency_consistency) / 3

        return {
            'relevance_consistency': relevance_consistency,
            'source_mapping_consistency': source_mapping_consistency,
            'latency_consistency': latency_consistency,
            'overall_consistency': overall_consistency,
            'variance_by_metric': {
                'relevance': statistics.variance(relevance_scores) if len(relevance_scores) > 1 else 0,
                'source_mapping': statistics.variance(source_mapping_scores) if len(source_mapping_scores) > 1 else 0,
                'latency': statistics.variance(latency_scores) if len(latency_scores) > 1 else 0
            }
        }
    
    @staticmethod
    def calculate_overall_accuracy(results: List[ValidationResult]) -> dict:
        """
        Calculate overall accuracy metrics across multiple validation results.
        
        Args:
            results: List of validation results
            
        Returns:
            Dictionary with overall accuracy metrics
        """
        if not results:
            return {
                "avg_relevance_score": 0.0,
                "avg_source_mapping_accuracy": 0.0,
                "avg_latency_ms": 0.0,
                "validation_success_rate": 0.0,
                "total_validations": 0
            }
        
        relevance_scores = [r.relevance_score for r in results]
        source_mapping_accuracies = [r.source_mapping_accuracy for r in results]
        latencies = [r.latency_ms for r in results]
        successful_validations = sum(1 for r in results if r.is_valid)
        
        return {
            "avg_relevance_score": sum(relevance_scores) / len(relevance_scores),
            "avg_source_mapping_accuracy": sum(source_mapping_accuracies) / len(source_mapping_accuracies),
            "avg_latency_ms": sum(latencies) / len(latencies),
            "validation_success_rate": successful_validations / len(results),
            "total_validations": len(results)
        }