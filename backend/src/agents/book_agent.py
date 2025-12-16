import openai
from typing import List, Optional
import logging
from src.models.question_answer import Question, Answer, SourceReference
from src.config import Config

# Set up logging
logger = logging.getLogger(__name__)


class BookAgent:
    """
    An AI agent using the OpenAI Agents SDK with rules to answer only from retrieved book content
    """
    
    def __init__(self):
        # Set the OpenAI API key from config
        openai.api_key = Config.OPENAI_API_KEY

        # Use OpenAI client with timeout
        self.client = openai.OpenAI(
            api_key=Config.OPENAI_API_KEY,
            timeout=Config.OPENAI_REQUEST_TIMEOUT  # Use timeout from config
        )

        # Define the model to use
        self.model = "gpt-3.5-turbo"  # This can be configured based on requirements

    def generate_answer(
        self,
        question: Question,
        context_chunks: List[str],
        source_references: List[SourceReference]
    ) -> Optional[Answer]:
        """
        Generate an answer based only on the provided context chunks.
        
        Args:
            question: The question to answer
            context_chunks: List of relevant book content chunks
            source_references: List of source references for the chunks
        
        Returns:
            Answer object with content and source references, or None if insufficient data
        """
        if not context_chunks:
            return None  # Not enough information to answer
        
        # Create context from the retrieved chunks
        context = "\n\n".join([f"Source {i+1}: {chunk}" for i, chunk in enumerate(context_chunks)])
        
        # Construct the prompt to ensure the agent only uses provided context
        system_message = (
            "You are a helpful assistant that answers questions based only on the provided context. "
            "Do not use any prior knowledge or information outside of the provided context. "
            "If the answer cannot be determined from the provided context, state that explicitly."
        )
        
        user_message = (
            f"Based on the following context, answer the question: '{question.content}'\n\n"
            f"Context:\n{context}"
        )
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,  # Lower temperature for more consistent answers
                max_tokens=500
            )

            # Extract the answer text
            answer_text = response.choices[0].message.content

            # Track token usage
            prompt_tokens = response.usage.prompt_tokens if response.usage else 0
            completion_tokens = response.usage.completion_tokens if response.usage else 0
            total_tokens = response.usage.total_tokens if response.usage else 0

            logger.info(f"Token usage for question {question.id}: "
                       f"Prompt={prompt_tokens}, Completion={completion_tokens}, Total={total_tokens}")

            # Check if the response indicates insufficient information
            if self._indicates_insufficient_info(answer_text):
                return None

            # Create and return the answer
            answer = Answer(
                id=f"ans_{question.id}",
                question_id=question.id,
                content=answer_text,
                confidence_score=self._calculate_confidence(response)
            )

            return answer

        except Exception as e:
            logger.error(f"Error generating answer with OpenAI: {e}")
            return None

    def _indicates_insufficient_info(self, answer_text: str) -> bool:
        """
        Check if the answer indicates insufficient information to answer the question.
        """
        insufficient_indicators = [
            "cannot determine",
            "not provided",
            "not mentioned",
            "no information",
            "insufficient information",
            "not enough information",
            "not specified",
            "not stated",
            "not available",
            "unable to determine",
            "unknown",
            "not found in the context",
            "context does not mention",
            "not discuss"
        ]

        text_lower = answer_text.lower()
        return any(indicator in text_lower for indicator in insufficient_indicators)

    def _calculate_confidence(self, response) -> float:
        """
        Calculate a confidence score based on the response.
        This is a simplified implementation - a real system would have more sophisticated logic.
        """
        # For now, return a fixed confidence score based on response length and other factors
        # This would be enhanced in a production system
        message_content = response.choices[0].message.content
        return 0.8 if len(message_content) > 50 else 0.6