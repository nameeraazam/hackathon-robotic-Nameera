import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { text: "Hi! I'm the Humanoid Robotics Assistant. Ask me anything about the book!", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = input;
    setMessages(prev => [...prev, { text: userMsg, sender: 'user' }]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userMsg }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setMessages(prev => [...prev, { text: data.answer, sender: 'bot' }]);
    } catch (error) {
      console.error("Error:", error);
      setMessages(prev => [...prev, { text: "Sorry, I'm having trouble connecting to the brain. Make sure the Python backend is running!", sender: 'bot' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.chatContainer}>
      {!isOpen && (
        <button className={styles.chatButton} onClick={() => setIsOpen(true)}>
          🤖
        </button>
      )}
      
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.header}>
            <span>Robotics Assistant</span>
            <button className={styles.closeButton} onClick={() => setIsOpen(false)}>×</button>
          </div>
          
          <div className={styles.messages}>
            {messages.map((msg, idx) => (
              <div key={idx} className={`${styles.message} ${msg.sender === 'user' ? styles.userMessage : styles.botMessage}`}>
                {msg.text}
              </div>
            ))}
            {isLoading && <div className={styles.message + ' ' + styles.botMessage}>Thinking...</div>}
            <div ref={messagesEndRef} />
          </div>
          
          <form className={styles.inputArea} onSubmit={handleSubmit}>
            <input
              type="text"
              className={styles.input}
              placeholder="Ask a question..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
            <button type="submit" className={styles.sendButton} disabled={isLoading}>
              ➤
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;
