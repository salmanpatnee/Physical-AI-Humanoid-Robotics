#!/usr/bin/env python3
"""
Validation script to execute US1-specific validation and output CSV results
for retrieval accuracy testing.
"""

import argparse
import sys
import os
from typing import List

# Add the backend/src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from validation.qdrant_connector import QdrantConnector
from validation.retrieval_validator import RetrievalValidator
from validation.logger import ValidationLogger
from validation.query_generator import QueryGenerator
from validation.models import QueryRequest
from validation.config import Config


def run_us1_validation(max_queries: int = 10, output_file: str = "validation_results.csv"):
    """
    Execute User Story 1 validation: Validate Retrieval Accuracy
    
    This function queries the vector database with sample questions to ensure
    the system returns topically correct content chunks that match the question intent.
    """
    print("Starting User Story 1 validation: Validate Retrieval Accuracy")
    print(f"Target: {max_queries} queries, output to {output_file}")
    
    # Initialize components
    config = Config()
    if not config.validate_config():
        print("ERROR: Configuration is not valid. Please check your .env file.")
        return False
    
    qdrant_connector = QdrantConnector()
    logger = ValidationLogger(output_file)
    validator = RetrievalValidator(qdrant_connector, logger)
    query_generator = QueryGenerator()
    
    # Verify Qdrant connection
    if not qdrant_connector.verify_connection():
        print("ERROR: Cannot connect to Qdrant. Please check your configuration.")
        return False
    
    print("[OK] Qdrant connection verified")
    
    # Generate validation queries
    print(f"Generating {max_queries} validation queries...")
    validation_queries = query_generator.generate_validation_queries()
    
    # If we need more queries, repeat the validation queries
    while len(validation_queries) < max_queries:
        validation_queries.extend(query_generator.generate_validation_queries())
    
    # Trim to the exact number requested
    validation_queries = validation_queries[:max_queries]
    
    print(f"[OK] Generated {len(validation_queries)} queries for validation")
    
    # Validate each query
    results = []
    successful_validations = 0
    total_relevance_score = 0
    total_source_accuracy = 0
    total_latency = 0
    
    print("Starting validation process...")
    for i, query_request in enumerate(validation_queries, 1):
        print(f"Validating query {i}/{len(validation_queries)}: '{query_request.question[:50]}...'")
        
        try:
            result = validator.validate_single_query(query_request)
            results.append(result)
            
            if result.is_valid:
                successful_validations += 1
            
            total_relevance_score += result.relevance_score
            total_source_accuracy += result.source_mapping_accuracy
            total_latency += result.latency_ms
            
            status = "[PASS]" if result.is_valid else "[FAIL]"
            print(f"  {status} Relevance: {result.relevance_score:.2f}, "
                  f"Source Acc: {result.source_mapping_accuracy:.2f}, "
                  f"Latency: {result.latency_ms:.2f}ms")
            
        except Exception as e:
            print(f"  [ERROR] Error validating query: {str(e)}")
            continue
    
    # Calculate and display summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    if results:
        avg_relevance = total_relevance_score / len(results)
        avg_source_accuracy = total_source_accuracy / len(results)
        avg_latency = total_latency / len(results)
        success_rate = successful_validations / len(results)
        
        print(f"Total queries processed: {len(results)}")
        print(f"Successful validations: {successful_validations}/{len(results)} ({success_rate:.1%})")
        print(f"Average relevance score: {avg_relevance:.3f}")
        print(f"Average source mapping accuracy: {avg_source_accuracy:.3f}")
        print(f"Average latency: {avg_latency:.2f}ms")
        print(f"Results logged to: {output_file}")
        
        # Check if we met the success criteria
        print("\nSUCCESS CRITERIA CHECK:")
        print(f"  [OK] 90% of sample queries return topically correct chunks: "
              f"{'PASS' if avg_relevance >= 0.9 else 'FAIL'} ({avg_relevance:.1%})")
        print(f"  [OK] 100% of retrieved chunks map to correct book pages: "
              f"{'PASS' if avg_source_accuracy >= 1.0 else 'FAIL'} ({avg_source_accuracy:.1%})")
        print(f"  [OK] Query response time under 2 seconds: "
              f"{'PASS' if avg_latency < 2000 else 'FAIL'} ({avg_latency:.0f}ms avg)")
        
        # Overall assessment
        overall_pass = avg_relevance >= 0.9 and avg_source_accuracy >= 1.0 and avg_latency < 2000
        print(f"\nOVERALL ASSESSMENT: {'PASS' if overall_pass else 'FAIL'}")
        
        return overall_pass
    else:
        print("No results to summarize.")
        return False


def main():
    parser = argparse.ArgumentParser(description='Execute US1-specific validation for retrieval accuracy')
    parser.add_argument('--max-queries', type=int, default=10, 
                       help='Maximum number of queries to validate (default: 10)')
    parser.add_argument('--output-file', type=str, default='validation_results.csv',
                       help='Output CSV file for results (default: validation_results.csv)')
    
    args = parser.parse_args()
    
    success = run_us1_validation(args.max_queries, args.output_file)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()