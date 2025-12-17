"""
Vercel Serverless Function for health check.
Endpoint: /api/health
"""
from http.server import BaseHTTPRequestHandler
import json
import sys
import os
from datetime import datetime

# Add backend source to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend', 'src'))

from config import validate_environment, Config

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Validate environment
            validate_environment()

            # Check OpenAI connection
            try:
                import openai
                client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
                client.models.list()
                openai_status = "connected"
            except Exception as e:
                print(f"OpenAI connection error: {e}")
                openai_status = "error"

            # Check Qdrant connection
            try:
                from services.retrieval_service import RetrievalService
                retrieval_service = RetrievalService()
                collections = retrieval_service.client.get_collections()
                qdrant_status = "connected"
            except Exception as e:
                print(f"Qdrant connection error: {e}")
                qdrant_status = "error"

            overall_status = "healthy" if (qdrant_status == "connected" and openai_status == "connected") else "unhealthy"

            response = {
                "status": overall_status,
                "timestamp": datetime.now().isoformat(),
                "dependencies": {
                    "openai_api": openai_status,
                    "vector_database": qdrant_status
                }
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except Exception as e:
            error_response = {
                "status": "unhealthy",
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
