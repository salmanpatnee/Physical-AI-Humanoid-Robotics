# Quickstart: Validate Retrieval Pipeline

## Prerequisites

- Python 3.11 or higher
- Access to the Qdrant vector database instance
- Python virtual environment (recommended)
- Backend directory with validation components installed

## Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Dependencies are already defined in pyproject.toml. If using uv:
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install qdrant-client python-dotenv pandas requests fastapi uvicorn
   ```

4. **Set up environment variables**:
   Ensure the `.env` file exists in the project root with the following content:
   ```env
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_api_key  # if authentication is required
   QDRANT_PORT=6333  # default port, change if needed
   ```

## Running Validation

1. **Execute the main validation script (User Story 1 - Retrieval Accuracy)**:
   ```bash
   python src/scripts/run_validation.py
   ```

2. **Execute source mapping validation (User Story 2)**:
   ```bash
   python src/scripts/run_us2_validation.py
   ```

3. **Execute cross-module validation (User Story 3)**:
   ```bash
   python src/scripts/run_us3_validation.py
   ```

4. **Customize validation parameters** (optional):
   You can specify validation parameters via command line arguments:
   ```bash
   python src/scripts/run_validation.py --max-queries 50 --output-file "validation_results.csv"
   python src/scripts/run_us2_validation.py --max-queries 30 --output-file "source_mapping_results.csv"
   python src/scripts/run_us3_validation.py --queries-per-module 5 --output-file "cross_module_results.csv"
   ```

## Running the Validation API

1. **Start the validation API server**:
   ```bash
   uvicorn src.validation.api:app --reload --port 8000
   ```

2. **Access the API documentation**:
   Open your browser to http://localhost:8000/docs to see the interactive API documentation

3. **Use the validation endpoints**:
   - POST /validate/query - Submit a single query for validation
   - POST /validate/batch - Submit multiple queries for batch validation
   - GET /validate/summary - Get summary of recent validation results
   - GET /validate/results/{validation_id} - Get detailed results for a specific validation (not implemented in this version)

## Understanding Results

After validation completes, you'll find:

- `validation_results.csv` - Detailed results of each query and its validation
- `source_mapping_validation_results.csv` - Results specific to source mapping validation
- `cross_module_validation_results.csv` - Results for cross-module consistency
- Console output summarizing validation metrics
- Performance statistics including average latency and accuracy measurements

## Key Metrics

- **Retrieval Accuracy**: Percentage of queries that returned topically correct chunks
- **Source Mapping Accuracy**: Percentage of chunks that map to correct book pages
- **Latency**: Response time for each query
- **Cross-Module Consistency**: Accuracy variance across different modules
- **Validation Success Rate**: Percentage of validations that meet all criteria

## Analyzing Results

1. **Generate detailed reports**:
   Use the ResultAnalyzer component to generate comprehensive reports:
   ```python
   from src.validation.result_analyzer import ResultAnalyzer

   analyzer = ResultAnalyzer("validation_results.csv")
   report = analyzer.generate_comprehensive_report()
   analyzer.export_report_to_json(report, "comprehensive_validation_report.json")
   ```

## Next Steps

Once validation is complete and pipeline quality is confirmed:
1. Review the validation results and reports
2. Address any identified issues
3. Run additional validation tests if needed
4. Prepare for agent integration