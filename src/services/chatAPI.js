// src/services/chatAPI.js

// Get API configuration from environment variables or use defaults
// For Vercel deployment, use same origin (empty string) to call serverless functions
// For local development, allow override via window.CHATBOT_API_URL
const API_BASE_URL = typeof window !== 'undefined'
  ? (window.CHATBOT_API_URL || '')
  : '';
const API_KEY = typeof window !== 'undefined'
  ? (window.CHATBOT_API_KEY || '')
  : '';

/**
 * Service for communicating with the chatbot backend API
 */
class ChatAPIService {
  /**
   * Submit a query to the chatbot API
   * @param {string} question - The question to ask
   * @param {string} [selectedText] - Optional selected text for context
   * @returns {Promise<Object>} The response from the chatbot
   */
  static async submitQuery(question, selectedText = null) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question,
          selected_text: selectedText || null
        })
      });

      if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error submitting query:', error);
      throw error;
    }
  }
}

export default ChatAPIService;