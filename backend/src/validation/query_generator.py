import random
from typing import List
from .models import QueryRequest
from .utils import generate_query_request_id


class QueryGenerator:
    """Generate representative user questions for validation."""
    
    def __init__(self):
        # Sample questions organized by topic areas that might be in the educational content
        self.sample_questions = {
            "robotics": [
                "What are the core principles of humanoid robotics?",
                "Explain the difference between forward and inverse kinematics.",
                "What are the main challenges in humanoid robot locomotion?",
                "How does sensor fusion work in robotics?",
                "What are the safety considerations for humanoid robots?"
            ],
            "ai": [
                "What is the difference between supervised and unsupervised learning?",
                "Explain how neural networks learn.",
                "What are the ethical considerations in AI development?",
                "How does reinforcement learning work?",
                "What are the limitations of current AI systems?"
            ],
            "qdrant": [
                "How does vector search work in Qdrant?",
                "What are the best practices for designing vector embeddings?",
                "How do you optimize Qdrant for semantic search?",
                "What is the impact of vector dimensionality on search performance?",
                "How do you handle schema changes in Qdrant collections?"
            ],
            "general": [
                "Can you explain the basic concepts of this topic?",
                "What are the key takeaways from this chapter?",
                "How does this concept relate to real-world applications?",
                "What are the prerequisites for understanding this material?",
                "Can you summarize the main points of this section?"
            ]
        }
    
    def generate_single_query(self, topic: str = None, module_context: str = None) -> QueryRequest:
        """Generate a single representative user question."""
        if topic and topic in self.sample_questions:
            question_pool = self.sample_questions[topic]
        else:
            # If no specific topic, pick from all available questions
            all_questions = []
            for questions in self.sample_questions.values():
                all_questions.extend(questions)
            question_pool = all_questions
        
        # Randomly select a question
        question = random.choice(question_pool)
        
        # Create and return the query request
        query_request = QueryRequest(
            id=generate_query_request_id(),
            question=question,
            module_context=module_context
        )
        
        return query_request
    
    def generate_multiple_queries(self, count: int, topic: str = None, module_context: str = None) -> List[QueryRequest]:
        """Generate multiple representative user questions."""
        queries = []
        for _ in range(count):
            query = self.generate_single_query(topic, module_context)
            queries.append(query)
        return queries
    
    def generate_queries_for_modules(self, module_names: List[str], queries_per_module: int = 3) -> List[QueryRequest]:
        """Generate queries specifically targeted for each module."""
        all_queries = []
        for module_name in module_names:
            # Determine topic based on module name
            topic = self._determine_topic_for_module(module_name)
            queries = self.generate_multiple_queries(queries_per_module, topic, module_name)
            all_queries.extend(queries)
        return all_queries
    
    def _determine_topic_for_module(self, module_name: str) -> str:
        """Determine the most relevant topic for a given module."""
        module_lower = module_name.lower()
        
        # Check if module name contains keywords that match our topic areas
        if any(keyword in module_lower for keyword in ["robot", "kinematics", "locomotion", "actuator"]):
            return "robotics"
        elif any(keyword in module_lower for keyword in ["ai", "learning", "neural", "ml", "intelligen"]):
            return "ai"
        elif any(keyword in module_lower for keyword in ["qdrant", "vector", "search", "embedding", "similarity"]):
            return "qdrant"
        else:
            return "general"
    
    def generate_validation_queries(self) -> List[QueryRequest]:
        """Generate a standard set of validation queries for comprehensive testing."""
        validation_queries = []
        
        # Add queries from each category
        for topic in self.sample_questions.keys():
            queries = self.generate_multiple_queries(2, topic=topic)
            validation_queries.extend(queries)
        
        return validation_queries