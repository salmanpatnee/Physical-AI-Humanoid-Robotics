// src/services/chatAPI.js

const API_BASE_URL = process.env.REACT_APP_CHATBOT_API_URL || process.env.BACKEND_API_URL || 'http://localhost:8000';
const API_KEY = process.env.REACT_APP_API_KEY || '';

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
      const response = await fetch(`${API_BASE_URL}/api/chat/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': API_KEY,
        },
        body: JSON.stringify({
          question,
          selectedText: selectedText || null
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