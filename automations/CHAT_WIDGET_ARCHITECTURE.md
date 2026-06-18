# Chat Widget Architecture

## Component Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Documentation Site                       │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                                                         │ │
│  │  Your Documentation Content                            │ │
│  │  (MkDocs Material Theme)                               │ │
│  │                                                         │ │
│  │                                  ┌──────────────────┐  │ │
│  │                                  │  Chat Widget     │  │ │
│  │                                  │  Button (Float)  │  │ │
│  │                                  └────────┬─────────┘  │ │
│  │                                           │            │ │
│  │  When clicked ─────────────────────────> │            │ │
│  │                                           ▼            │ │
│  │                              ┌────────────────────┐   │ │
│  │                              │  Chat Widget       │   │ │
│  │                              │  Panel (Expanded)  │   │ │
│  │                              │                    │   │ │
│  │                              │  [Messages Area]   │   │ │
│  │                              │  [Input Field]     │   │ │
│  │                              │  [Send Button]     │   │ │
│  │                              └────────┬───────────┘   │ │
│  │                                       │               │ │
│  └───────────────────────────────────────┼───────────────┘ │
│                                          │                 │
└──────────────────────────────────────────┼─────────────────┘
                                           │
                                           │ HTTP POST
                                           │ (User Question +
                                           │  Conversation History +
                                           │  Page Context)
                                           │
                                           ▼
              ┌────────────────────────────────────────────┐
              │         FlowRunner™ Backend                │
              │  ┌──────────────────────────────────────┐  │
              │  │  1. App Logic Trigger                │  │
              │  │     (Receives HTTP request)          │  │
              │  └─────────────┬────────────────────────┘  │
              │                │                           │
              │                ▼                           │
              │  ┌──────────────────────────────────────┐  │
              │  │  2. Set Variables Block              │  │
              │  │     - Extract question               │  │
              │  │     - Extract conversation history   │  │
              │  │     - Extract page context           │  │
              │  └─────────────┬────────────────────────┘  │
              │                │                           │
              │                ▼                           │
              │  ┌──────────────────────────────────────┐  │
              │  │  3. AI Agent Block                   │  │
              │  │     ┌──────────────────────────────┐ │  │
              │  │     │ System Prompt:               │ │  │
              │  │     │ "You are FlowRunner™         │ │  │
              │  │     │  docs assistant..."          │ │  │
              │  │     └──────────────────────────────┘ │  │
              │  │     ┌──────────────────────────────┐ │  │
              │  │     │ Tools:                       │ │  │
              │  │     │ - searchDocumentation()      │ │  │
              │  │     │ - getBlockReference()        │ │  │
              │  │     └──────────────────────────────┘ │  │
              │  │     ┌──────────────────────────────┐ │  │
              │  │     │ Memory:                      │ │  │
              │  │     │ - Conversation history       │ │  │
              │  │     │ - Context awareness          │ │  │
              │  │     └──────────────────────────────┘ │  │
              │  └─────────────┬────────────────────────┘  │
              │                │                           │
              │                ▼                           │
              │  ┌──────────────────────────────────────┐  │
              │  │  4. Return Result Block              │  │
              │  │     Returns:                         │  │
              │  │     { answer: "AI response..." }     │  │
              │  └─────────────┬────────────────────────┘  │
              │                │                           │
              └────────────────┼───────────────────────────┘
                               │
                               │ HTTP Response
                               │ (AI Answer)
                               │
                               ▼
              ┌────────────────────────────────────────────┐
              │         Chat Widget (Frontend)             │
              │  ┌──────────────────────────────────────┐  │
              │  │  Displays AI response in chat        │  │
              │  │  Adds to conversation history        │  │
              │  │  Saves to localStorage               │  │
              │  └──────────────────────────────────────┘  │
              └────────────────────────────────────────────┘
```

## Data Flow

### 1. User Input Flow

```
User Types Question
        ↓
Click Send / Press Enter
        ↓
chat-widget.js: sendMessage()
        ↓
Show typing indicator
        ↓
callFlowRunnerFlow(message)
        ↓
POST to FlowRunner™ endpoint
```

### 2. Request Payload

```json
{
  "question": "How do I create a condition?",
  "sessionId": "session_1734533245678_abc123xyz",
  "context": {
    "currentPage": "/flow-editing/conditions.html",
    "pageTitle": "Conditional Logic - FlowRunner™ User Guide"
  }
}
```

**Session ID Details:**
- Unique per user session
- Format: `session_[timestamp]_[random]`
- Persists in localStorage across page refreshes
- Server uses this to maintain conversation context

### 3. FlowRunner™ Processing

```
Trigger receives request
        ↓
Extract sessionId and question (Set Variables)
        ↓
Retrieve conversation history from database (using sessionId)
        ↓
AI Agent processes:
  - Analyzes question
  - Reviews conversation history from server
  - Uses page context for relevance
  - Searches documentation (via tools)
  - Generates response
        ↓
Save question + response to database (with sessionId)
        ↓
Return result to frontend
```

**Server-Side Session Management:**
- Store conversation history in a database table
- Table schema: `{ sessionId, role, content, timestamp }`
- Retrieve history before AI Agent call
- Save both user question and AI response after generation
- Limit history to last N messages for token efficiency

### 4. Response Payload

```json
{
  "answer": "To create a condition in FlowRunner™, follow these steps:\n\n1. Drag a **Condition** block from the toolbox\n2. Connect it to your flow\n3. Configure the condition logic...",
  "timestamp": "2025-12-18T12:00:00Z",
  "model": "gpt-4-turbo-preview"
}
```

### 5. UI Update Flow

```
Receive response
        ↓
Remove typing indicator
        ↓
Format message (markdown → HTML)
        ↓
Add to messages UI
        ↓
Save to conversation history
        ↓
Scroll to bottom
        ↓
Ready for next question
```

## File Structure

```
automations/
├── content/
│   ├── css/
│   │   ├── style.css                 # Existing styles
│   │   └── chat-widget.css          # Chat widget styles ✨ NEW
│   ├── js/
│   │   └── chat-widget.js           # Chat widget logic ✨ NEW
│   └── [your markdown files]
├── mkdocs.yml                        # Updated config ✨ MODIFIED
├── CHAT_WIDGET_SETUP.md             # Setup guide ✨ NEW
├── CHAT_WIDGET_ARCHITECTURE.md      # This file ✨ NEW
└── EXAMPLE_FLOW_CONFIG.json         # Flow example ✨ NEW
```

## Key Components

### Frontend (chat-widget.js)

**Responsibilities:**
- Render chat UI
- Handle user interactions
- Manage conversation state
- Call FlowRunner™ API
- Display responses
- Persist conversation history

**Key Functions:**
- `initChatWidget()` - Initialize on page load
- `toggleChat()` - Open/close widget
- `sendMessage()` - Send user message
- `callFlowRunnerFlow()` - API call to FlowRunner™
- `addMessageToUI()` - Display messages
- `formatMessage()` - Convert markdown to HTML

### Styling (chat-widget.css)

**Features:**
- Dark/Light mode support
- Responsive design (mobile-friendly)
- Smooth animations
- Material Design principles
- Matches MkDocs Material theme

### Backend (FlowRunner™ Flow)

**Blocks:**
1. **App Logic Trigger** - Entry point
2. **Set Variables** - Data extraction
3. **AI Agent** - Core intelligence
4. **Return Result** - Response formatting

**AI Agent Tools:**
- `searchDocumentation()` - Find relevant docs
- `getBlockReference()` - Get block details

## Configuration Points

### 1. Widget Appearance

**File:** `content/js/chat-widget.js`

```javascript
const CONFIG = {
  theme: {
    primaryColor: '#4F46E5',    // Main accent color
    headerBg: '#1e1e1e',        // Header background
    userMsgBg: '#4F46E5',       // User message bubble
    botMsgBg: '#2a2a2a',        // Bot message bubble
    inputBg: '#1e1e1e'          // Input field background
  }
};
```

### 2. API Endpoint

**File:** `content/js/chat-widget.js`

```javascript
const CONFIG = {
  flowEndpoint: 'https://YOUR_APP.backendless.app/api/services/...',
  apiKey: null  // Optional authentication
};
```

### 3. AI Agent Behavior

**In FlowRunner™ Flow:**
- System prompt (defines assistant personality)
- Temperature (creativity level)
- Max tokens (response length)
- Tools configuration (search capabilities)

## Security Considerations

```
┌─────────────────────────────────────────────┐
│  Security Layers                            │
├─────────────────────────────────────────────┤
│  1. CORS - Restrict allowed origins         │
│  2. Rate Limiting - Prevent abuse           │
│  3. Input Validation - Sanitize user input  │
│  4. API Key - Optional authentication       │
│  5. Content Filtering - AI guardrails       │
└─────────────────────────────────────────────┘
```

## Performance Optimization

```
┌─────────────────────────────────────────────┐
│  Optimization Strategies                    │
├─────────────────────────────────────────────┤
│  1. Response Caching - Cache common Q&A     │
│  2. Debouncing - Prevent rapid requests     │
│  3. Lazy Loading - Load widget on demand    │
│  4. Local Storage - Persist conversations   │
│  5. Compression - Minimize payload size     │
└─────────────────────────────────────────────┘
```

## Testing Checklist

- [ ] Widget appears on all pages
- [ ] Dark/Light mode works correctly
- [ ] Mobile responsive design functions
- [ ] Messages send successfully
- [ ] AI responses display properly
- [ ] Conversation history persists
- [ ] Error handling works
- [ ] Typing indicator shows/hides
- [ ] Scroll behavior is smooth
- [ ] Links in responses work
- [ ] Code formatting displays correctly

## Monitoring & Analytics

### Recommended Metrics to Track:

1. **Usage Metrics**
   - Number of conversations
   - Messages per conversation
   - Active users

2. **Performance Metrics**
   - Response time
   - Error rate
   - API call duration

3. **Content Metrics**
   - Most asked questions
   - Popular topics
   - Unanswered questions

4. **Quality Metrics**
   - User satisfaction
   - Follow-up questions
   - Conversation completion rate

## Future Enhancements

### Potential Features:

1. **Suggested Questions**
   - Show common questions as buttons
   - Context-aware suggestions

2. **Voice Input**
   - Speech-to-text integration
   - Hands-free interaction

3. **File Upload**
   - Upload images for analysis
   - Share code snippets

4. **Feedback System**
   - Thumbs up/down on responses
   - Report incorrect information

5. **Multi-language Support**
   - Detect user language
   - Translate responses

6. **Export Conversations**
   - Download chat history
   - Share helpful conversations

---

**Ready to implement?** Follow the [CHAT_WIDGET_SETUP.md](./CHAT_WIDGET_SETUP.md) guide!
