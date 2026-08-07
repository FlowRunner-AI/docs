# Quick Start: Chat Widget Integration

Get your FlowRunner™ documentation chat widget up and running in 5 steps!

## ✅ What's Already Done

- ✨ Chat widget UI components created
- ✨ Styling with dark/light mode support
- ✨ JavaScript functionality implemented
- ✨ MkDocs configuration updated
- ✨ Mobile-responsive design ready

## 🚀 5 Steps to Launch

### Step 1: Configure Your FlowRunner™ Endpoint (2 minutes)

1. Open `automations/content/js/chat-widget.js`
2. Find line ~15 with `const CONFIG`
3. Replace the placeholder with your actual endpoint:

```javascript
const CONFIG = {
  flowEndpoint: 'https://YOUR_APP_ID.backendless.app/api/services/YOUR_SERVICE/YOUR_OPERATION',
  apiKey: null, // Add if needed
};
```

### Step 2: Build Your Documentation (1 minute)

```bash
cd automations
mkdocs build
```

### Step 3: Test Locally (1 minute)

```bash
mkdocs serve
```

Open http://localhost:8000 and look for the chat button in the bottom-right corner!

### Step 4: Create Your AI Flow in FlowRunner™ (10 minutes)

**Quick Flow Setup:**

1. Create new flow: "Documentation Chat Assistant"
2. Add **App Logic Trigger** (set to Synchronous with Return Result)
3. Add **AI Agent** block:
   - Model: GPT-4 Turbo
   - System Prompt: "You are a FlowRunner™ documentation assistant..."
   - User Message: `${triggerData.question}`
4. Add **Return Result** block:
   - Result: `{ answer: ${aiAgentResponse} }`
5. Enable the flow (make it LIVE)
6. Copy the trigger URL to Step 1

### Step 5: Deploy (depends on your setup)

Build and deploy your docs:

```bash
mkdocs build
# Then deploy to your hosting (GitHub Pages, Netlify, etc.)
```

## 🎨 Customization

### Change Widget Colors

In `content/js/chat-widget.js`:

```javascript
theme: {
  primaryColor: '#YOUR_BRAND_COLOR'
}
```

### Change Widget Position

In `content/css/chat-widget.css`:

```css
.chat-widget-button {
  bottom: 24px;  /* Adjust distance from bottom */
  right: 24px;   /* Adjust distance from right */
}
```

### Change Welcome Message

In `content/js/chat-widget.js`, find the welcome message HTML (~line 87):

```html
<div class="chat-welcome-message">
  <p>👋 Hi! Your custom welcome message here!</p>
</div>
```

## 📊 Expected Flow Input/Output

### What the widget sends to your flow:

```json
{
  "question": "How do I create a condition?",
  "sessionId": "session_1734533245678_abc123xyz",
  "context": {
    "currentPage": "/flow-editing/conditions.html",
    "pageTitle": "Conditional Logic"
  }
}
```

### What your flow should return:

```json
{
  "answer": "Your AI-generated response here..."
}
```

## 🔧 Troubleshooting

### Widget not appearing?

```bash
# Check if files exist
ls automations/content/js/chat-widget.js
ls automations/content/css/chat-widget.css

# Rebuild
cd automations && mkdocs build
```

### No AI response?

1. Check browser console for errors (F12)
2. Verify FlowRunner™ flow is LIVE
3. Check flow execution logs in FlowRunner™
4. Verify the endpoint URL is correct

### CORS errors?

In Backendless Console:
- Go to Settings → API Settings
- Add your docs domain to allowed origins

## 📚 Documentation Files

- **[CHAT_WIDGET_SETUP.md](./CHAT_WIDGET_SETUP.md)** - Full setup guide
- **[CHAT_WIDGET_ARCHITECTURE.md](./CHAT_WIDGET_ARCHITECTURE.md)** - How it works
- **[EXAMPLE_FLOW_CONFIG.json](./EXAMPLE_FLOW_CONFIG.json)** - Flow structure example

## 💡 Pro Tips

### 1. Improve AI Responses

Add these tools to your AI Agent:

```javascript
{
  name: "searchDocs",
  description: "Search FlowRunner™ documentation",
  parameters: { query: "string" }
}
```

### 2. Add Context Awareness

Use the page context in your system prompt:

```
Current page: ${triggerData.context.currentPage}
Focus your answer on content related to this page.
```

### 3. Rate Limiting

Add a condition before AI Agent to limit requests:

```javascript
if (requestsThisHour > 100) {
  return { answer: "Too many requests, try again later" }
}
```

## 🎯 Next Steps

1. ✅ Get basic chat working
2. 📝 Refine AI prompts for better responses
3. 🔍 Add documentation search tools
4. 📊 Monitor usage and optimize
5. 🚀 Collect user feedback

## 🆘 Need Help?

1. Check FlowRunner™ docs: https://docs.flowrunner.ai
2. Review flow execution logs
3. Check browser console (F12 → Console)
4. Inspect network requests (F12 → Network)

---

**Ready to chat?** Let's make your documentation interactive! 🎉
