# FlowRunner™ Documentation Chat Widget Setup Guide

This guide will help you set up the AI-powered chat widget that connects to your FlowRunner™ flow.

## Overview

The chat widget provides:
- ✅ Floating chat button in the bottom-right corner
- ✅ Clean, modern UI that matches your documentation theme
- ✅ Dark/Light mode support
- ✅ Conversation history persistence
- ✅ Typing indicators
- ✅ Mobile responsive design
- ✅ Connection to FlowRunner™ AI Agent flow

## Files Created

1. **`content/js/chat-widget.js`** - JavaScript functionality
2. **`content/css/chat-widget.css`** - Styling
3. **`mkdocs.yml`** - Updated to include the widget files

## Setup Instructions

### Step 1: Create Your FlowRunner™ AI Agent Flow

1. **Go to FlowRunner™** and create a new flow
2. **Add an AI Agent block** with access to your documentation
3. **Configure the AI Agent**:
   - Set the system prompt to act as a FlowRunner™ documentation assistant
   - Give it access to documentation context (you can use RAG or vector database)
   - Configure it to answer questions based on the docs

#### Example Flow Structure:

```
[App Logic Trigger]
    ↓
[AI Agent Block]
    ↓
[Return Result Block]
```

#### Example AI Agent Configuration:

**System Prompt:**
```
You are a helpful FlowRunner™ documentation assistant. Your role is to help users
understand FlowRunner™ features, blocks, and how to build automations.

Use the provided documentation context to answer questions accurately. If you're
not sure about something, say so rather than making up information.

Be concise, friendly, and technical when needed. Provide code examples when appropriate.
```

**Tools/Functions:**
- Add a function to search documentation
- Add a function to retrieve specific block reference information

### Step 2: Get Your Flow Endpoint URL

1. In FlowRunner™, go to your flow
2. Note the **App Logic Trigger** URL or create an API endpoint
3. The URL will look something like:
   ```
   https://YOUR_APP_ID.backendless.app/api/services/YOUR_SERVICE/YOUR_OPERATION
   ```

### Step 3: Configure the Chat Widget

Open `content/js/chat-widget.js` and update the configuration:

```javascript
const CONFIG = {
  // Your FlowRunner flow URL endpoint
  flowEndpoint: 'https://YOUR_APP_ID.backendless.app/api/services/YOUR_SERVICE/YOUR_OPERATION',

  // Optional: API key if your flow requires authentication
  apiKey: null, // or 'your-api-key-here'

  // Customize appearance if needed
  theme: {
    primaryColor: '#4F46E5',
    // ... other theme options
  }
};
```

### Step 4: Configure Your FlowRunner™ Flow Input/Output

#### Expected Flow Input (from chat widget):

```json
{
  "question": "How do I create a condition in FlowRunner?",
  "sessionId": "session_1734533245678_abc123xyz",
  "context": {
    "currentPage": "/flow-editing/conditions.html",
    "pageTitle": "Conditional Logic - FlowRunner™ User Guide"
  }
}
```

**Session Management:**
- The `sessionId` is a unique identifier generated per user session
- Format: `session_[timestamp]_[random]` (e.g., `session_1734533245678_abc123xyz`)
- Stored in localStorage and persists across page refreshes
- Your FlowRunner™ flow should use this ID to maintain conversation history on the server side
- Example: Store conversation history in a database table with `sessionId` as the key

#### Expected Flow Output (to chat widget):

```json
{
  "answer": "To create a condition in FlowRunner™, you can..."
}
```

**Note:** The widget looks for the response in these fields (in order):
- `data.answer`
- `data.response`
- `data.result`

Adjust the `callFlowRunnerFlow` function if your flow uses a different response structure.

### Step 5: Build and Test

1. **Build your documentation:**
   ```bash
   cd automations
   mkdocs build
   ```

2. **Test locally:**
   ```bash
   mkdocs serve
   ```

3. **Open your browser** and navigate to `http://localhost:8000`

4. **Look for the chat button** in the bottom-right corner

5. **Click and test** by asking questions about FlowRunner™

## Customization Options

### Change Widget Position

In `content/css/chat-widget.css`, modify:

```css
.chat-widget-button {
  bottom: 24px;  /* Distance from bottom */
  right: 24px;   /* Distance from right */
}
```

### Change Widget Colors

In `content/js/chat-widget.js`, modify the `CONFIG.theme`:

```javascript
theme: {
  primaryColor: '#YOUR_COLOR',
  headerBg: '#YOUR_COLOR',
  userMsgBg: '#YOUR_COLOR',
  botMsgBg: '#YOUR_COLOR',
  inputBg: '#YOUR_COLOR'
}
```

### Change Widget Size

In `content/css/chat-widget.css`:

```css
.chat-widget-container {
  width: 400px;        /* Default width */
  height: 600px;       /* Default height */
}
```

### Disable Conversation History

In `content/js/chat-widget.js`, comment out these lines:

```javascript
// saveConversationHistory();
// loadConversationHistory();
```

## Advanced: AI Agent Setup Tips

### 1. Use RAG (Retrieval-Augmented Generation)

Connect your AI Agent to a vector database with your documentation:

1. Convert your markdown docs to embeddings
2. Store in a vector database (Pinecone, Weaviate, etc.)
3. Add a function to the AI Agent to retrieve relevant docs
4. Pass the retrieved context to the AI Agent

### 2. Provide Page Context

The widget already sends the current page URL and title. Use this in your flow:

```javascript
// In your FlowRunner flow logic
const currentPage = flowContext.question.context.currentPage;
const pageTitle = flowContext.question.context.pageTitle;

// Use this to provide more relevant context
// For example, if user is on /flow-editing/conditions.html,
// prioritize information about conditions
```

### 3. Add Suggested Questions

Modify the welcome message in `chat-widget.js`:

```javascript
<div class="chat-welcome-message">
  <p>👋 Hi! I'm the FlowRunner™ documentation assistant.</p>
  <p>Try asking:</p>
  <ul style="margin: 8px 0 0 0; padding-left: 20px;">
    <li>How do I create a condition?</li>
    <li>What is an AI Agent block?</li>
    <li>How do error handlers work?</li>
  </ul>
</div>
```

## Troubleshooting

### Widget Not Appearing

1. Check browser console for errors
2. Verify files are included in `mkdocs.yml`
3. Rebuild the docs: `mkdocs build`

### No Response from AI

1. Check the Network tab in browser dev tools
2. Verify the `flowEndpoint` URL is correct
3. Check if your FlowRunner™ flow is enabled (LIVE)
4. Check the flow's execution logs for errors

### CORS Errors

If you see CORS errors in the console:

1. In Backendless Console, go to **Settings** → **API Settings**
2. Add your documentation domain to allowed origins
3. Or use a proxy in your FlowRunner™ flow

### Styling Issues

1. Clear browser cache
2. Check if CSS file is loaded (Network tab)
3. Verify no CSS conflicts with Material theme

## Example FlowRunner™ Flow Configuration

### Flow Structure

```
1. [App Logic Trigger]
   ↓ Receives: { question, conversationHistory, context }

2. [Set Variables Block]
   ↓ Extract question, format context

3. [AI Agent Block]
   ↓ System: "You are a FlowRunner™ docs assistant..."
   ↓ User message: {question}
   ↓ Tools: [searchDocs, getBlockReference]

4. [Return Result Block]
   ↓ Returns: { answer: aiResponse }
```

### AI Agent System Prompt Example

```
You are an expert FlowRunner™ documentation assistant. Your goal is to help
users understand and use FlowRunner™ effectively.

Guidelines:
- Be concise but thorough
- Use examples when helpful
- Reference specific blocks and features by name
- If you don't know something, say so
- Use markdown formatting in responses (**, `, etc.)

Current page context: {context.currentPage}
Page title: {context.pageTitle}

Use this context to provide more relevant answers.
```

## Performance Optimization

### Caching Responses

Add caching to avoid redundant AI calls:

```javascript
// In chat-widget.js, add a simple cache
const responseCache = new Map();

async function callFlowRunnerFlow(userMessage) {
  const cacheKey = userMessage.toLowerCase().trim();

  if (responseCache.has(cacheKey)) {
    return responseCache.get(cacheKey);
  }

  const response = await fetch(/* ... */);
  const data = await response.json();
  const answer = data.answer || data.response || data.result;

  responseCache.set(cacheKey, answer);
  return answer;
}
```

### Debouncing

Prevent multiple rapid requests:

```javascript
let requestInProgress = false;

async function sendMessage() {
  if (requestInProgress) return;
  requestInProgress = true;

  try {
    // ... existing code
  } finally {
    requestInProgress = false;
  }
}
```

## Security Considerations

1. **API Key Protection**: If using an API key, consider backend proxy
2. **Rate Limiting**: Implement rate limiting in your FlowRunner™ flow
3. **Input Validation**: Validate and sanitize user input in the flow
4. **CORS**: Only allow your documentation domain

## Next Steps

1. **Test thoroughly** with various questions
2. **Monitor FlowRunner™ flow** execution logs
3. **Collect feedback** from users
4. **Iterate on AI prompts** for better responses
5. **Add analytics** to track usage

## Support

For issues or questions:
- Check FlowRunner™ documentation
- Review flow execution logs
- Inspect browser console for errors
- Check Network tab for API call details

---

**Built with FlowRunner™** 🚀
