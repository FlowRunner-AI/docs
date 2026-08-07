/**
 * FlowRunner™ Documentation Chat Widget
 * Connects to FlowRunner AI Agent for documentation assistance
 */

(function() {
  'use strict';

  // Configuration - UPDATE THESE VALUES
  const CONFIG = {
    // Your FlowRunner flow URL endpoint
    flowEndpoint: 'https://api.flowrunner.ai/B40B97DB-A31E-4A78-A98B-A0D714BA2553/226A0113-9F16-455B-B1C3-18D321336231/automation/flow/ChatWithDocs/activate-blocking?waitResponseTimeoutSeconds=300',

    // Optional: API key or authentication if required
    apiKey: null,

    // Widget appearance
    theme: {
      primaryColor: '#4F46E5', // Indigo to match your theme
      headerBg: '#1e1e1e',
      userMsgBg: '#4F46E5',
      botMsgBg: '#2a2a2a',
      inputBg: '#1e1e1e'
    }
  };

  // Widget state
  let isOpen = false;
  let sessionId = null;
  let textSizeLevel = 0; // -2 to +2 range for text size adjustments

  /**
   * Initialize the chat widget
   */
  function initChatWidget() {
    sessionId = getOrCreateSessionId();
    createChatWidgetHTML();
    attachEventListeners();
    loadChatHistory();
    loadTextSizePreference();
  }

  /**
   * Get existing session ID or create a new one
   */
  function getOrCreateSessionId() {
    const STORAGE_KEY = 'flowrunner_chat_session_id';
    let storedSessionId = null;

    try {
      storedSessionId = localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      console.warn('Could not access localStorage:', e);
    }

    if (!storedSessionId) {
      // Generate a unique session ID
      storedSessionId = generateSessionId();

      try {
        localStorage.setItem(STORAGE_KEY, storedSessionId);
      } catch (e) {
        console.warn('Could not save session ID:', e);
      }
    }

    return storedSessionId;
  }

  /**
   * Generate a unique session ID
   */
  function generateSessionId() {
    // Format: timestamp-random
    const timestamp = Date.now();
    const random = Math.random().toString(36).substring(2, 15);
    return `session_${timestamp}_${random}`;
  }

  /**
   * Create the chat widget HTML structure
   */
  function createChatWidgetHTML() {
    const widgetHTML = `
      <!-- Chat Widget Button -->
      <div id="chat-widget-button" class="chat-widget-button" aria-label="Open chat" role="button" tabindex="0">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
      </div>

      <!-- Chat Widget Container -->
      <div id="chat-widget-container" class="chat-widget-container" style="display: none;">
        <!-- Header -->
        <div class="chat-widget-header">
          <div class="chat-widget-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
              <path d="M2 17l10 5 10-5M2 12l10 5 10-5"></path>
            </svg>
            <span>FlowRunner™ Assistant</span>
          </div>
          <button id="chat-widget-close" class="chat-widget-close" aria-label="Close chat">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>

        <!-- Toolbar -->
        <div class="chat-widget-toolbar">
          <button id="chat-clear-btn" class="chat-toolbar-btn" aria-label="Clear chat history" title="Clear chat history">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
          </button>
          <button id="chat-text-smaller-btn" class="chat-toolbar-btn" aria-label="Decrease text size" title="Decrease text size">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
          <button id="chat-text-larger-btn" class="chat-toolbar-btn" aria-label="Increase text size" title="Increase text size">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>

        <!-- Messages Area -->
        <div class="chat-widget-messages" id="chat-widget-messages">
          <div class="chat-welcome-message">
            <p>👋 Hi! I'm the FlowRunner™ documentation assistant.</p>
            <p>Ask me anything about FlowRunner™ features, blocks, or how to build automations!</p>
          </div>
        </div>

        <!-- Input Area -->
        <div class="chat-widget-input-container">
          <textarea
            id="chat-widget-input"
            class="chat-widget-input"
            placeholder="Ask about FlowRunner™..."
            rows="1"
            aria-label="Chat message input"
          ></textarea>
          <button id="chat-widget-send" class="chat-widget-send" aria-label="Send message">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
        </div>

        <!-- Powered by -->
        <div class="chat-widget-footer">
          <span>Powered by <strong>FlowRunner™</strong></span>
        </div>
      </div>
    `;

    // Insert widget into the page
    const container = document.createElement('div');
    container.id = 'chat-widget-root';
    container.innerHTML = widgetHTML;
    document.body.appendChild(container);
  }

  /**
   * Attach event listeners to widget elements
   */
  function attachEventListeners() {
    const button = document.getElementById('chat-widget-button');
    const closeBtn = document.getElementById('chat-widget-close');
    const sendBtn = document.getElementById('chat-widget-send');
    const input = document.getElementById('chat-widget-input');

    // Toolbar buttons
    const clearBtn = document.getElementById('chat-clear-btn');
    const textSmallerBtn = document.getElementById('chat-text-smaller-btn');
    const textLargerBtn = document.getElementById('chat-text-larger-btn');

    button.addEventListener('click', toggleChat);
    button.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleChat();
      }
    });

    closeBtn.addEventListener('click', toggleChat);
    sendBtn.addEventListener('click', sendMessage);

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    });

    // Auto-resize textarea
    input.addEventListener('input', function() {
      this.style.height = 'auto';
      this.style.height = Math.min(this.scrollHeight, 120) + 'px';
    });

    // Toolbar button handlers
    clearBtn.addEventListener('click', clearChatHistory);
    textSmallerBtn.addEventListener('click', decreaseTextSize);
    textLargerBtn.addEventListener('click', increaseTextSize);
  }

  /**
   * Toggle chat widget visibility
   */
  function toggleChat() {
    const container = document.getElementById('chat-widget-container');
    const button = document.getElementById('chat-widget-button');

    isOpen = !isOpen;

    if (isOpen) {
      container.style.display = 'flex';
      button.style.transform = 'scale(0)';
      setTimeout(() => {
        // Scroll to bottom
        const messagesContainer = document.getElementById('chat-widget-messages');
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        // Focus input
        document.getElementById('chat-widget-input').focus();
      }, 300);
    } else {
      container.style.display = 'none';
      button.style.transform = 'scale(1)';
    }
  }

  /**
   * Send a message to the FlowRunner AI agent
   */
  async function sendMessage() {
    const input = document.getElementById('chat-widget-input');
    const message = input.value.trim();

    if (!message) return;

    // Add user message to UI
    addMessageToUI(message, 'user');

    // Clear input
    input.value = '';
    input.style.height = 'auto';

    // Save message to history
    saveChatMessage('user', message);

    // Show typing indicator
    showTypingIndicator();

    try {
      // Call FlowRunner flow
      const response = await callFlowRunnerFlow(message);

      // Remove typing indicator
      removeTypingIndicator();

      // Add bot response to UI
      addMessageToUI(response, 'bot');

      // Save response to history
      saveChatMessage('assistant', response);

    } catch (error) {
      removeTypingIndicator();
      addMessageToUI('Sorry, I encountered an error. Please try again.', 'bot', true);
      console.error('Chat widget error:', error);
    }
  }

  /**
   * Call the FlowRunner flow endpoint
   */
  async function callFlowRunnerFlow(userMessage) {
    const headers = {
      'Content-Type': 'application/json'
    };

    // Add API key if configured
    if (CONFIG.apiKey) {
      headers['Authorization'] = `Bearer ${CONFIG.apiKey}`;
    }

    const requestBody = {
      question: userMessage,
      sessionId: sessionId,
      context: {
        currentPage: window.location.pathname,
        pageTitle: document.title
      }
    };

    const response = await fetch(CONFIG.flowEndpoint, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Adjust this based on your FlowRunner flow's response structure
    return data.answer || data.response || data.result || 'No response from the assistant.';
  }

  /**
   * Add a message to the chat UI
   */
  function addMessageToUI(message, type, isError = false) {
    const messagesContainer = document.getElementById('chat-widget-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message chat-message-${type}`;

    if (isError) {
      messageDiv.classList.add('chat-message-error');
    }

    // Convert markdown-style formatting to HTML
    const formattedMessage = formatMessage(message);

    messageDiv.innerHTML = `
      <div class="chat-message-content">
        ${formattedMessage}
      </div>
      <div class="chat-message-time">${getCurrentTime()}</div>
    `;

    messagesContainer.appendChild(messageDiv);

    // Scroll to bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  /**
   * Format message with full markdown support
   */
  function formatMessage(message) {
    // Escape HTML first
    let formatted = message
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // Split into lines for block-level processing
    let lines = formatted.split('\n');
    let html = [];
    let inList = false;
    let inOrderedList = false;
    let inCodeBlock = false;
    let codeBlockContent = [];

    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];

      // Code blocks (```)
      if (line.trim().startsWith('```')) {
        if (inCodeBlock) {
          // End code block
          html.push('<pre><code>' + codeBlockContent.join('\n') + '</code></pre>');
          codeBlockContent = [];
          inCodeBlock = false;
        } else {
          // Start code block
          inCodeBlock = true;
        }
        continue;
      }

      if (inCodeBlock) {
        codeBlockContent.push(line);
        continue;
      }

      // Headings (## text)
      if (line.match(/^#{1,6}\s/)) {
        if (inList) {
          html.push('</ul>');
          inList = false;
        }
        if (inOrderedList) {
          html.push('</ol>');
          inOrderedList = false;
        }

        const level = line.match(/^(#{1,6})/)[1].length;
        const text = line.replace(/^#{1,6}\s+/, '').trim();
        html.push(`<h${level}>${processInlineFormatting(text)}</h${level}>`);
        continue;
      }

      // Unordered lists (- item or * item)
      if (line.match(/^\s*[-*]\s/)) {
        if (inOrderedList) {
          html.push('</ol>');
          inOrderedList = false;
        }
        if (!inList) {
          html.push('<ul>');
          inList = true;
        }
        const text = line.replace(/^\s*[-*]\s+/, '').trim();
        html.push(`<li>${processInlineFormatting(text)}</li>`);
        continue;
      }

      // Ordered lists (1. item)
      if (line.match(/^\s*\d+\.\s/)) {
        if (inList) {
          html.push('</ul>');
          inList = false;
        }
        if (!inOrderedList) {
          html.push('<ol>');
          inOrderedList = true;
        }
        const text = line.replace(/^\s*\d+\.\s+/, '').trim();
        html.push(`<li>${processInlineFormatting(text)}</li>`);
        continue;
      }

      // Close lists if we hit a non-list line
      if (inList) {
        html.push('</ul>');
        inList = false;
      }
      if (inOrderedList) {
        html.push('</ol>');
        inOrderedList = false;
      }

      // Empty lines become breaks
      if (line.trim() === '') {
        html.push('<br>');
        continue;
      }

      // Regular paragraphs
      html.push(`<p>${processInlineFormatting(line)}</p>`);
    }

    // Close any open lists
    if (inList) {
      html.push('</ul>');
    }
    if (inOrderedList) {
      html.push('</ol>');
    }

    return html.join('');
  }

  /**
   * Process inline markdown formatting (bold, italic, code, links)
   */
  function processInlineFormatting(text) {
    // Bold: **text** or __text__ (do bold first, before italic)
    text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/__(.+?)__/g, '<strong>$1</strong>');

    // Italic: *text* or _text_
    text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
    text = text.replace(/_(.+?)_/g, '<em>$1</em>');

    // Inline code: `code`
    text = text.replace(/`(.+?)`/g, '<code>$1</code>');

    // Links: [text](url)
    text = text.replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    return text;
  }

  /**
   * Show typing indicator
   */
  function showTypingIndicator() {
    const messagesContainer = document.getElementById('chat-widget-messages');
    const typingDiv = document.createElement('div');
    typingDiv.id = 'chat-typing-indicator';
    typingDiv.className = 'chat-message chat-message-bot';
    typingDiv.innerHTML = `
      <div class="chat-message-content">
        <div class="chat-typing-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    `;
    messagesContainer.appendChild(typingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  /**
   * Remove typing indicator
   */
  function removeTypingIndicator() {
    const indicator = document.getElementById('chat-typing-indicator');
    if (indicator) {
      indicator.remove();
    }
  }

  /**
   * Get current time formatted
   */
  function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  }

  /**
   * Save a chat message to localStorage
   */
  function saveChatMessage(role, content) {
    const STORAGE_KEY = `flowrunner_chat_history_${sessionId}`;

    try {
      let history = [];
      const stored = localStorage.getItem(STORAGE_KEY);

      if (stored) {
        history = JSON.parse(stored);
      }

      history.push({
        role: role,
        content: content,
        timestamp: new Date().toISOString()
      });

      // Keep only last 50 messages to prevent storage overflow
      if (history.length > 50) {
        history = history.slice(-50);
      }

      localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
    } catch (e) {
      console.warn('Could not save chat message:', e);
    }
  }

  /**
   * Load chat history from localStorage and display it
   */
  function loadChatHistory() {
    const STORAGE_KEY = `flowrunner_chat_history_${sessionId}`;

    try {
      const stored = localStorage.getItem(STORAGE_KEY);

      if (stored) {
        const history = JSON.parse(stored);

        // Display messages in UI
        history.forEach(msg => {
          if (msg.role === 'user') {
            addMessageToUI(msg.content, 'user');
          } else if (msg.role === 'assistant') {
            addMessageToUI(msg.content, 'bot');
          }
        });
      }
    } catch (e) {
      console.warn('Could not load chat history:', e);
    }
  }

  /**
   * Clear chat history
   */
  function clearChatHistory() {
    showConfirmDialog(
      'Clear Chat History?',
      'Are you sure you want to clear all messages? This cannot be undone.',
      () => {
        // User confirmed - clear history
        const STORAGE_KEY = `flowrunner_chat_history_${sessionId}`;

        try {
          // Clear from localStorage
          localStorage.removeItem(STORAGE_KEY);

          // Clear UI - remove all messages except welcome message
          const messagesContainer = document.getElementById('chat-widget-messages');
          messagesContainer.innerHTML = `
            <div class="chat-welcome-message">
              <p>👋 Hi! I'm the FlowRunner™ documentation assistant.</p>
              <p>Ask me anything about FlowRunner™ features, blocks, or how to build automations!</p>
            </div>
          `;
        } catch (e) {
          console.warn('Could not clear chat history:', e);
        }
      }
    );
  }

  /**
   * Show custom confirmation dialog
   */
  function showConfirmDialog(title, message, onConfirm) {
    // Create modal overlay
    const overlay = document.createElement('div');
    overlay.className = 'chat-confirm-overlay';
    overlay.innerHTML = `
      <div class="chat-confirm-dialog">
        <div class="chat-confirm-header">
          <h3>${title}</h3>
        </div>
        <div class="chat-confirm-body">
          <p>${message}</p>
        </div>
        <div class="chat-confirm-footer">
          <button class="chat-confirm-btn chat-confirm-cancel">Cancel</button>
          <button class="chat-confirm-btn chat-confirm-ok">Clear</button>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Add event listeners
    const cancelBtn = overlay.querySelector('.chat-confirm-cancel');
    const okBtn = overlay.querySelector('.chat-confirm-ok');

    const closeDialog = () => {
      overlay.remove();
    };

    cancelBtn.addEventListener('click', closeDialog);
    okBtn.addEventListener('click', () => {
      onConfirm();
      closeDialog();
    });

    // Close on overlay click
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeDialog();
      }
    });

    // Close on Escape key
    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        closeDialog();
        document.removeEventListener('keydown', handleEscape);
      }
    };
    document.addEventListener('keydown', handleEscape);

    // Focus the OK button
    setTimeout(() => okBtn.focus(), 100);
  }

  /**
   * Increase text size
   */
  function increaseTextSize() {
    if (textSizeLevel >= 2) return; // Max size limit

    textSizeLevel++;
    applyTextSize();
  }

  /**
   * Decrease text size
   */
  function decreaseTextSize() {
    if (textSizeLevel <= -2) return; // Min size limit

    textSizeLevel--;
    applyTextSize();
  }

  /**
   * Apply text size to messages container
   */
  function applyTextSize() {
    const messagesContainer = document.getElementById('chat-widget-messages');

    // Base font size is 14px, each level adds/subtracts 2px
    const baseFontSize = 14;
    const newFontSize = baseFontSize + (textSizeLevel * 2);

    messagesContainer.style.fontSize = `${newFontSize}px`;

    // Save preference to localStorage
    try {
      localStorage.setItem('flowrunner_chat_text_size', textSizeLevel.toString());
    } catch (e) {
      console.warn('Could not save text size preference:', e);
    }
  }

  /**
   * Load text size preference from localStorage
   */
  function loadTextSizePreference() {
    try {
      const saved = localStorage.getItem('flowrunner_chat_text_size');
      if (saved !== null) {
        textSizeLevel = parseInt(saved, 10);
        if (isNaN(textSizeLevel)) {
          textSizeLevel = 0;
        }
        // Clamp to valid range
        textSizeLevel = Math.max(-2, Math.min(2, textSizeLevel));
        applyTextSize();
      }
    } catch (e) {
      console.warn('Could not load text size preference:', e);
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatWidget);
  } else {
    initChatWidget();
  }

})();
