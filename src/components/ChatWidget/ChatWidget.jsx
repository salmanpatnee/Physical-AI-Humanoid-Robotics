// src/components/ChatWidget/ChatWidget.jsx
import React, { useState, useEffect } from 'react';
import './ChatWidget.css';
import ChatAPIService from '../../services/chatAPI'; // Updated to use the chat API service

const ChatWidget = ({ isOpen, onClose, onToggle }) => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');

  // Function to capture selected text
  const captureSelectedText = () => {
    const selectedText = window.getSelection ? window.getSelection().toString().trim() : '';
    if (selectedText) {
      setSelectedText(selectedText);
    }
  };

  // Add event listener to capture text selection
  useEffect(() => {
    const handleSelection = () => {
      captureSelectedText();
    };

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('keyup', handleSelection);

    return () => {
      document.removeEventListener('mouseup', handleSelection);
      document.removeEventListener('keyup', handleSelection);
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    // Add user message to chat
    const userMessage = {
      id: Date.now(),
      text: message,
      sender: 'user',
      selectedText: selectedText || null
    };
    setMessages(prev => [...prev, userMessage]);

    setIsLoading(true);
    setMessage('');

    try {
      // Use the actual API service to send the query
      const response = await ChatAPIService.submitQuery(message, selectedText);

      const botMessage = {
        id: Date.now() + 1,
        text: response.answer,
        sender: 'bot',
        sources: response.sources || []
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error getting response:', error);
      const errorMessage = {
        id: Date.now() + 1,
        text: 'Sorry, there was an error processing your request.',
        sender: 'bot',
        sources: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      // Clear selected text after submission
      setSelectedText('');
    }
  };

  if (!isOpen) {
    // Show floating button when widget is closed
    return (
      <button className="chat-widget-float-button" onClick={onToggle}>
        <span>🤖 Chat</span>
      </button>
    );
  }

  return (
    <div className="chat-widget-container">
      <div className="chat-widget-header">
        <h3>Book Assistant</h3>
        <button className="chat-widget-close" onClick={onClose}>×</button>
      </div>
      <div className="chat-widget-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message ${msg.sender}`}>
            <div className="message-text">{msg.text}</div>
            {msg.sources && msg.sources.length > 0 && (
              <div className="message-sources">
                <h5>Sources:</h5>
                <ul>
                  {msg.sources.map((source, idx) => (
                    <li key={idx}>{source.title}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
        {isLoading && (
          <div className="message bot">
            <div className="message-text">Thinking...</div>
          </div>
        )}
      </div>
      <form onSubmit={handleSubmit} className="chat-widget-input-form">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder={`Ask a question${selectedText ? ' (selected text will be included)' : ''}...`}
          className="chat-widget-input"
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading} className="chat-widget-send-button">
          Send
        </button>
      </form>
      {selectedText && (
        <div className="selected-text-preview">
          Selected: "{selectedText.substring(0, 60)}{selectedText.length > 60 ? '...' : ''}"
        </div>
      )}
    </div>
  );
};

export default ChatWidget;