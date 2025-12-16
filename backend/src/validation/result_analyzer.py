from typing import List, Dict, Any
import pandas as pd
import json
from datetime import datetime
from .models import ValidationResult


class ResultAnalyzer:
    """Process and summarize validation results."""
    
    def __init__(self, results_file_path: str = "validation_results.csv"):
        self.results_file_path = results_file_path
    
    def load_results_from_csv(self) -> pd.DataFrame:
        """Load validation results from CSV file."""
        try:
            df = pd.read_csv(self.results_file_path)
            return df
        except FileNotFoundError:
            print(f"Warning: Results file {self.results_file_path} not found.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error loading results from CSV: {str(e)}")
            return pd.DataFrame()
    
    def analyze_validation_results(self, results: List[ValidationResult]) -> Dict[str, Any]:
        """Analyze a list of validation results and return summary statistics."""
        if not results:
            return {
                "total_results": 0,
                "avg_relevance_score": 0.0,
                "avg_source_mapping_accuracy": 0.0,
                "avg_latency_ms": 0.0,
                "validation_success_rate": 0.0,
                "timestamp": datetime.now().isoformat()
            }
        
        relevance_scores = [r.relevance_score for r in results]
        source_accuracies = [r.source_mapping_accuracy for r in results]
        latencies = [r.latency_ms for r in results]
        successful_validations = [r for r in results if r.is_valid]
        
        # Calculate percentiles for a more comprehensive analysis
        import statistics
        try:
            relevance_p95 = self._calculate_percentile(relevance_scores, 95)
            latency_p95 = self._calculate_percentile(latencies, 95)
        except:
            relevance_p95 = 0.0
            latency_p95 = 0.0
        
        analysis = {
            "total_results": len(results),
            "successful_validations": len(successful_validations),
            "validation_success_rate": len(successful_validations) / len(results),
            "avg_relevance_score": sum(relevance_scores) / len(relevance_scores),
            "std_relevance_score": statistics.stdev(relevance_scores) if len(relevance_scores) > 1 else 0.0,
            "min_relevance_score": min(relevance_scores),
            "max_relevance_score": max(relevance_scores),
            "relevance_p95": relevance_p95,
            "avg_source_mapping_accuracy": sum(source_accuracies) / len(source_accuracies),
            "std_source_mapping_accuracy": statistics.stdev(source_accuracies) if len(source_accuracies) > 1 else 0.0,
            "avg_latency_ms": sum(latencies) / len(latencies),
            "std_latency": statistics.stdev(latencies) if len(latencies) > 1 else 0.0,
            "min_latency_ms": min(latencies),
            "max_latency_ms": max(latencies),
            "latency_p95": latency_p95,
            "timestamp": datetime.now().isoformat()
        }
        
        return analysis
    
    def analyze_csv_results(self) -> Dict[str, Any]:
        """Analyze validation results from CSV file."""
        df = self.load_results_from_csv()
        
        if df.empty:
            return {"error": "No data to analyze"}
        
        # Basic statistics
        analysis = {
            "total_records": len(df),
            "timestamp": datetime.now().isoformat(),
            "field_analysis": {}
        }
        
        # Analyze each important field
        for field in ['relevance_score', 'source_mapping_accuracy', 'latency_ms', 'is_valid']:
            if field in df.columns:
                if field == 'is_valid':
                    # Special handling for boolean field
                    valid_count = df[field].sum() if df[field].dtype in ['bool', 'int64'] else df[field].astype(str).str.lower().str.contains('true').sum()
                    analysis['field_analysis'][field] = {
                        "valid_count": int(valid_count),
                        "invalid_count": int(len(df) - valid_count),
                        "success_rate": float(valid_count / len(df))
                    }
                else:
                    # Numerical field analysis
                    analysis['field_analysis'][field] = {
                        "mean": float(df[field].mean()),
                        "std": float(df[field].std()),
                        "min": float(df[field].min()),
                        "max": float(df[field].max()),
                        "q25": float(df[field].quantile(0.25)),
                        "q50": float(df[field].median()),
                        "q75": float(df[field].quantile(0.75)),
                        "count": int(df[field].count())
                    }
        
        return analysis
    
    def generate_validation_report(self, results: List[ValidationResult] = None) -> Dict[str, Any]:
        """Generate a comprehensive validation report."""
        # If results are provided, analyze them directly
        if results:
            results_analysis = self.analyze_validation_results(results)
        else:
            # Otherwise, load from CSV
            results_analysis = self.analyze_csv_results()

        report = {
            "report_type": "Validation Report",
            "generated_at": datetime.now().isoformat(),
            "analysis": results_analysis
        }

        return report

    def generate_comprehensive_report(self, results: List[ValidationResult] = None) -> Dict[str, Any]:
        """Generate a comprehensive report with validation summary, insights, and recommendations."""
        # If results are provided, analyze them directly
        if results:
            results_analysis = self.analyze_validation_results(results)
        else:
            # Otherwise, load from CSV
            results_analysis = self.analyze_csv_results()

        # Generate insights and recommendations based on the analysis
        insights = self._generate_insights(results_analysis)
        recommendations = self._generate_recommendations(results_analysis)

        comprehensive_report = {
            "report_type": "Comprehensive Validation Report",
            "generated_at": datetime.now().isoformat(),
            "executive_summary": self._generate_executive_summary(results_analysis),
            "detailed_analysis": results_analysis,
            "key_insights": insights,
            "recommendations": recommendations,
            "validation_status": self._determine_validation_status(results_analysis)
        }

        return comprehensive_report

    def _generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate an executive summary of the validation results."""
        if "error" in analysis:
            return f"ERROR: {analysis['error']}"

        if "avg_relevance_score" in analysis:
            # Analysis from direct results
            avg_relevance = analysis["avg_relevance_score"]
            avg_source_acc = analysis["avg_source_mapping_accuracy"]
            avg_latency = analysis["avg_latency_ms"]
            success_rate = analysis["validation_success_rate"]

            summary = (
                f"Validation completed with {analysis['total_results']} test cases. "
                f"Average relevance score: {avg_relevance:.3f}, "
                f"Source mapping accuracy: {avg_source_acc:.3f}, "
                f"Average latency: {avg_latency:.2f}ms. "
                f"Success rate: {success_rate:.1%}."
            )
        else:
            # Analysis from CSV
            field_analysis = analysis.get("field_analysis", {})
            rel_analysis = field_analysis.get("relevance_score", {})
            success_analysis = field_analysis.get("is_valid", {})

            if rel_analysis:
                avg_relevance = rel_analysis.get("mean", 0)
                summary = (
                    f"Analyzed {analysis['total_records']} validation records. "
                    f"Average relevance score: {avg_relevance:.3f}. "
                )

                if "success_rate" in success_analysis:
                    summary += f"Success rate: {success_analysis['success_rate']:.1%}. "
            else:
                summary = f"Analyzed {analysis['total_records']} validation records."

        return summary

    def _generate_insights(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate insights based on validation results."""
        insights = []

        if "error" in analysis:
            return [f"Error in analysis: {analysis['error']}"]

        if "avg_relevance_score" in analysis:
            # Direct results analysis
            avg_relevance = analysis["avg_relevance_score"]
            avg_source_acc = analysis["avg_source_mapping_accuracy"]
            avg_latency = analysis["avg_latency_ms"]
            std_relevance = analysis["std_relevance_score"]

            # Relevance insights
            if avg_relevance >= 0.9:
                insights.append("Relevance scores are excellent with an average of {:.3f}".format(avg_relevance))
            elif avg_relevance >= 0.7:
                insights.append("Relevance scores are good but could be improved (average: {:.3f})".format(avg_relevance))
            else:
                insights.append("Relevance scores need significant improvement (average: {:.3f})".format(avg_relevance))

            # Consistency insights
            if std_relevance < 0.1:
                insights.append("Relevance scores show high consistency across tests")
            elif std_relevance < 0.2:
                insights.append("Relevance scores show moderate consistency")
            else:
                insights.append("Relevance scores show low consistency - investigate causes")

            # Source mapping insights
            if avg_source_acc >= 0.95:
                insights.append("Source mapping accuracy is excellent at {:.3f}".format(avg_source_acc))
            elif avg_source_acc >= 0.85:
                insights.append("Source mapping accuracy is good (accuracy: {:.3f})".format(avg_source_acc))
            else:
                insights.append("Source mapping accuracy needs improvement (accuracy: {:.3f})".format(avg_source_acc))

            # Performance insights
            if avg_latency < 500:
                insights.append("Performance is excellent with fast response times (avg: {:.2f}ms)".format(avg_latency))
            elif avg_latency < 1000:
                insights.append("Performance is acceptable (avg: {:.2f}ms)".format(avg_latency))
            else:
                insights.append("Performance needs optimization (avg: {:.2f}ms)".format(avg_latency))
        else:
            # CSV-based analysis
            field_analysis = analysis.get("field_analysis", {})
            rel_analysis = field_analysis.get("relevance_score", {})
            latency_analysis = field_analysis.get("latency_ms", {})

            if rel_analysis:
                avg_relevance = rel_analysis.get("mean", 0)
                if avg_relevance >= 0.9:
                    insights.append("Relevance scores are excellent with an average of {:.3f}".format(avg_relevance))
                elif avg_relevance >= 0.7:
                    insights.append("Relevance scores are good (average: {:.3f})".format(avg_relevance))
                else:
                    insights.append("Relevance scores need improvement (average: {:.3f})".format(avg_relevance))

            if latency_analysis:
                avg_latency = latency_analysis.get("mean", 0)
                if avg_latency < 500:
                    insights.append("Response times are excellent (avg: {:.2f}ms)".format(avg_latency))
                elif avg_latency < 1000:
                    insights.append("Response times are acceptable (avg: {:.2f}ms)".format(avg_latency))
                else:
                    insights.append("Response times need optimization (avg: {:.2f}ms)".format(avg_latency))

        return insights

    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on validation results."""
        recommendations = []

        if "error" in analysis:
            return ["Resolve the reported error before proceeding with validation"]

        if "avg_relevance_score" in analysis:
            # Direct results analysis
            avg_relevance = analysis["avg_relevance_score"]
            avg_source_acc = analysis["avg_source_mapping_accuracy"]
            avg_latency = analysis["avg_latency_ms"]

            # Recommendations based on relevance
            if avg_relevance < 0.8:
                recommendations.append("Improve relevance by reviewing and refining the vector embedding process")
                recommendations.append("Consider adjusting the similarity threshold or search parameters")

            # Recommendations based on source mapping
            if avg_source_acc < 0.9:
                recommendations.append("Enhance source reference data quality and completeness")
                recommendations.append("Implement additional validation checks for source mapping")

            # Recommendations based on performance
            if avg_latency > 1000:
                recommendations.append("Optimize Qdrant performance by reviewing collection settings")
                recommendations.append("Consider adding caching for frequent queries")

        return recommendations

    def _determine_validation_status(self, analysis: Dict[str, Any]) -> str:
        """Determine overall validation status based on results."""
        if "error" in analysis:
            return "ERROR"

        if "avg_relevance_score" in analysis:
            avg_relevance = analysis["avg_relevance_score"]
            avg_source_acc = analysis["avg_source_mapping_accuracy"]
            avg_latency = analysis["avg_latency_ms"]

            if avg_relevance >= 0.9 and avg_source_acc >= 0.95 and avg_latency < 1000:
                return "VALIDATED"
            elif avg_relevance >= 0.8 and avg_source_acc >= 0.9 and avg_latency < 1500:
                return "CONDITIONAL"
            else:
                return "NEEDS IMPROVEMENT"
        else:
            # For CSV analysis, use field analysis
            field_analysis = analysis.get("field_analysis", {})
            rel_analysis = field_analysis.get("relevance_score", {})
            success_analysis = field_analysis.get("is_valid", {})

            if rel_analysis:
                avg_relevance = rel_analysis.get("mean", 0)

                success_rate = success_analysis.get("success_rate", 0) if success_analysis else 0

                if avg_relevance >= 0.9 and success_rate >= 0.9:
                    return "VALIDATED"
                elif avg_relevance >= 0.75 and success_rate >= 0.75:
                    return "CONDITIONAL"
                else:
                    return "NEEDS IMPROVEMENT"

        return "UNKNOWN"
    
    def export_report_to_json(self, report: Dict[str, Any], output_path: str = "validation_report.json"):
        """Export the validation report to a JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"Report exported to {output_path}")
    
    def _calculate_percentile(self, data: List[float], percentile: float) -> float:
        """Calculate percentile of a list of values."""
        if not data:
            return 0.0
        
        sorted_data = sorted(data)
        index = (percentile / 100) * (len(sorted_data) - 1)
        
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower_index = int(index // 1)
            upper_index = min(lower_index + 1, len(sorted_data) - 1)
            weight = index % 1
            return sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight
    
    def compare_results(self, results1: List[ValidationResult], results2: List[ValidationResult], 
                       labels: tuple = ("Results Set 1", "Results Set 2")) -> Dict[str, Any]:
        """Compare two sets of validation results."""
        analysis1 = self.analyze_validation_results(results1)
        analysis2 = self.analyze_validation_results(results2)
        
        comparison = {
            "comparison_date": datetime.now().isoformat(),
            f"{labels[0]}_analysis": analysis1,
            f"{labels[1]}_analysis": analysis2,
            "differences": {
                "relevance_score_difference": analysis2.get("avg_relevance_score", 0) - analysis1.get("avg_relevance_score", 0),
                "source_accuracy_difference": analysis2.get("avg_source_mapping_accuracy", 0) - analysis1.get("avg_source_mapping_accuracy", 0),
                "latency_difference_ms": analysis2.get("avg_latency_ms", 0) - analysis1.get("avg_latency_ms", 0),
                "success_rate_difference": analysis2.get("validation_success_rate", 0) - analysis1.get("validation_success_rate", 0)
            }
        }
        
        return comparison