# Quickstart: Validate Retrieval Pipeline

## Prerequisites

- Python 3.11 or higher
- Access to the Qdrant vector database instance
- Python virtual environment (recommended)

## Setup

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install qdrant-client python-dotenv pandas requests
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with the following content:
   ```env
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_api_key  # if authentication is required
   QDRANT_PORT=6333  # default port, change if needed
   ```

## Running Validation

1. **Execute the validation script**:
   ```bash
   python src/scripts/run_validation.py
   ```

2. **Customize validation parameters** (optional):
   You can specify validation parameters via command line arguments:
   ```bash
   python src/scripts/run_validation.py --module-name "module1" --max-queries 50 --output-file "validation_results.csv"
   ```

## Understanding Results

After validation completes, you'll find:

- `validation_results.csv` - Detailed results of each query and its validation
- Console output summarizing validation metrics
- Performance statistics including average latency and accuracy measurements

## Key Metrics

- **Retrieval Accuracy**: Percentage of queries that returned topically correct chunks
- **Source Mapping Accuracy**: Percentage of chunks that map to correct book pages
- **Latency**: Response time for each query
- **Cross-Module Consistency**: Accuracy variance across different modules

## Next Steps

Once validation is complete and pipeline quality is confirmed:
1. Review the validation results
2. Address any identified issues
3. Prepare for agent integration