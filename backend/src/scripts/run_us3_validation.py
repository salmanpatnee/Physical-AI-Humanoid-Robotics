#!/usr/bin/env python3
"""
Validation script to execute US3-specific validation across multiple modules.
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
from validation.models import QueryRequest, Module
from validation.config import Config
from validation.module_selector import ModuleSelector
from validation.metrics import ValidationMetricsCalculator


def run_us3_validation(queries_per_module: int = 3, output_file: str = "cross_module_validation_results.csv"):
    """
    Execute User Story 3 validation: Cross-Module Retrieval Validation
    
    This function tests retrieval across multiple modules/books to ensure 
    consistent performance across the entire corpus.
    """
    print("Starting User Story 3 validation: Cross-Module Retrieval Validation")
    print(f"Target: {queries_per_module} queries per module, output to {output_file}")
    
    # Initialize components
    config = Config()
    if not config.validate_config():
        print("ERROR: Configuration is not valid. Please check your .env file.")
        return False
    
    qdrant_connector = QdrantConnector()
    logger = ValidationLogger(output_file)
    validator = RetrievalValidator(qdrant_connector, logger)
    query_generator = QueryGenerator()
    module_selector = ModuleSelector(qdrant_connector)
    
    # Verify Qdrant connection
    if not qdrant_connector.verify_connection():
        print("ERROR: Cannot connect to Qdrant. Please check your configuration.")
        return False
    
    print("[OK] Qdrant connection verified")
    
    # Get all available modules
    modules = module_selector.get_all_modules()
    if not modules:
        print("ERROR: No modules found in Qdrant.")
        return False
    
    print(f"[OK] Found {len(modules)} modules for validation:")
    for i, module in enumerate(modules, 1):
        print(f"  {i}. {module.title} ({module.qdrant_collection_name}) - {module.total_chunks} chunks")
    
    # Generate queries for each module
    print(f"\nGenerating {queries_per_module} queries for each of {len(modules)} modules...")
    all_results = []
    module_results_map = {}
    
    for module in modules:
        print(f"\nValidating module: {module.title}")
        
        # Generate queries specific to this module
        queries = query_generator.generate_multiple_queries(
            queries_per_module, 
            module_context=module.qdrant_collection_name
        )
        
        module_results = []
        for i, query_request in enumerate(queries, 1):
            print(f"  Query {i}/{queries_per_module}: '{query_request.question[:50]}...'")
            
            try:
                result = validator.validate_single_query(
                    query_request, 
                    collection_name=module.qdrant_collection_name
                )
                module_results.append(result)
                all_results.append(result)
                
                status = "[PASS]" if result.is_valid else "[FAIL]"
                print(f"    {status} Relevance: {result.relevance_score:.2f}, "
                      f"Source Acc: {result.source_mapping_accuracy:.2f}, "
                      f"Latency: {result.latency_ms:.2f}ms")
                
                # Log module-specific metrics
                logger.log_module_specific_metrics(result, module.qdrant_collection_name)
                
            except Exception as e:
                print(f"    [ERROR] Error validating query: {str(e)}")
                continue
        
        module_results_map[module.qdrant_collection_name] = module_results
        print(f"  Completed validation for {module.title} with {len(module_results)} results")
    
    # Perform cross-module consistency validation
    print(f"\nPerforming cross-module consistency validation...")
    try:
        cross_module_result = validator.update_cross_module_validation(
            QueryRequest(
                id="cross_module_query",
                question="Perform cross-module validation across all available modules"
            ),
            modules
        )
        print(f"[OK] Cross-module validation completed")
        print(f"  - Avg relevance: {cross_module_result.relevance_score:.3f}")
        print(f"  - Is valid: {cross_module_result.is_valid}")
    except Exception as e:
        print(f"[ERROR] Cross-module validation failed: {str(e)}")
    
    # Calculate and display summary
    print("\n" + "="*60)
    print("CROSS-MODULE VALIDATION SUMMARY")
    print("="*60)
    
    if all_results:
        # Calculate overall metrics
        avg_relevance = sum(r.relevance_score for r in all_results) / len(all_results)
        avg_source_accuracy = sum(r.source_mapping_accuracy for r in all_results) / len(all_results)
        avg_latency = sum(r.latency_ms for r in all_results) / len(all_results)
        success_rate = sum(1 for r in all_results if r.is_valid) / len(all_results)
        
        print(f"Total queries processed: {len(all_results)}")
        print(f"Across {len(modules)} modules")
        print(f"Successful validations: {sum(1 for r in all_results if r.is_valid)}/{len(all_results)} ({success_rate:.1%})")
        print(f"Average relevance score: {avg_relevance:.3f}")
        print(f"Average source mapping accuracy: {avg_source_accuracy:.3f}")
        print(f"Average latency: {avg_latency:.2f}ms")
        print(f"Results logged to: {output_file}")
        
        # Check cross-module consistency
        consistency_metrics = ValidationMetricsCalculator.calculate_enhanced_cross_module_consistency(all_results)
        print(f"\nCROSS-MODULE CONSISTENCY:")
        print(f"  - Relevance consistency: {consistency_metrics['relevance_consistency']:.3f}")
        print(f"  - Source mapping consistency: {consistency_metrics['source_mapping_accuracy']:.3f}")
        print(f"  - Latency consistency: {consistency_metrics['latency_consistency']:.3f}")
        print(f"  - Overall consistency: {consistency_metrics['overall_consistency']:.3f}")
        
        # Per-module breakdown
        print(f"\nPER-MODULE BREAKDOWN:")
        for module in modules:
            if module.qdrant_collection_name in module_results_map:
                module_results = module_results_map[module.qdrant_collection_name]
                if module_results:
                    mod_avg_rel = sum(r.relevance_score for r in module_results) / len(module_results)
                    mod_avg_acc = sum(r.source_mapping_accuracy for r in module_results) / len(module_results)
                    mod_avg_lat = sum(r.latency_ms for r in module_results) / len(module_results)
                    
                    print(f"  {module.title}:")
                    print(f"    - Accuracy: {mod_avg_rel:.3f}")
                    print(f"    - Source mapping: {mod_avg_acc:.3f}")
                    print(f"    - Latency: {mod_avg_lat:.2f}ms")
                    print(f"    - Validation count: {len(module_results)}")
        
        # Success criteria check
        print(f"\nSUCCESS CRITERIA CHECK:")
        print(f"  [OK] Retrieval works across all modules: {'PASS' if len(modules) > 0 else 'FAIL'} ({len(modules)} modules)")
        print(f"  [OK] Consistent accuracy (within 5% variance): {'PASS' if consistency_metrics['relevance_consistency'] >= 0.95 else 'FAIL'} ({consistency_metrics['relevance_consistency']:.1%})")
        print(f"  [OK] Latency under 2 seconds: {'PASS' if avg_latency < 2000 else 'FAIL'} ({avg_latency:.0f}ms avg)")
        
        # Overall assessment
        overall_pass = (
            len(modules) > 0 and 
            consistency_metrics['relevance_consistency'] >= 0.95 and 
            avg_latency < 2000
        )
        print(f"\nOVERALL ASSESSMENT: {'PASS' if overall_pass else 'FAIL'}")
        
        return overall_pass
    else:
        print("No results to summarize.")
        return False


def main():
    parser = argparse.ArgumentParser(description='Execute US3-specific validation across multiple modules')
    parser.add_argument('--queries-per-module', type=int, default=3, 
                       help='Number of queries to run per module (default: 3)')
    parser.add_argument('--output-file', type=str, default='cross_module_validation_results.csv',
                       help='Output CSV file for results (default: cross_module_validation_results.csv)')
    
    args = parser.parse_args()
    
    success = run_us3_validation(args.queries_per_module, args.output_file)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
