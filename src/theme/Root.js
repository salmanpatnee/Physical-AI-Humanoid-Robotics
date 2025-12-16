// src/theme/Root.js
import React, { useState, useEffect } from 'react';
import ChatWidget from '../components/ChatWidget/ChatWidget';

// Default theme
export default function Root({children}) {
  const [isWidgetOpen, setIsWidgetOpen] = useState(false);

  const toggleWidget = () => {
    setIsWidgetOpen(!isWidgetOpen);
  };

  const closeWidget = () => {
    setIsWidgetOpen(false);
  };

  return (
    <>
      {children}
      <ChatWidget 
        isOpen={isWidgetOpen} 
        onClose={closeWidget} 
        onToggle={toggleWidget} 
      />
    </>
  );
}