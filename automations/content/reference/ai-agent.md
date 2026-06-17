<!-- GENERATED FILE - do not edit. Source: block-knowledge/ai-agent.yaml. Regenerate: make refgen -->
# AI Agent

Invoke an LLM with system/user prompts and (optionally) tools, returning its response.

## How it works

A configurable LLM call. Give it a model, prompts, optional tools (extensions / flows / MCP / knowledge bases), and it returns a response (optionally JSON).

## When to use it

Generate/summarize/classify/extract content, or run an agent that calls tools.

## Configuration

| Field | Description |
| --- | --- |
| AI Model / AI API Key / AI Provider | Required. Model + key (API Keys registry). Provider e.g. ANTHROPIC. |
| System Prompt / User Prompt | Instruction + input (User Prompt often a prior block result). |
| Tools | Attach tools the agent can call. The "Manage <span class="fr-block">AI Agent</span> Capabilities" modal has 4 categories: Extensions (built-in integration actions), MCP Extensions (tools from registered MCP servers, grouped by server — checkbox = all, or expand to pick), Flows (other flows as tools), Knowledge (knowledge bases). Has a search + a "Register new MCP Server" link. |
| Messages History (+ limit) | Feed prior instances' messages as context. |
| Force Parsed Output | Appends instruction to return JSON. |
| LangSmith Settings | Observability integration. |

## Behavior

- Calls the configured model with the prompts (+ tools/history); returns the response.
- With tools attached, it may call them to fulfill the task.

## Things to watch for

- Non-deterministic output.
- Tool params left blank are filled by the AI at runtime; pre-set to pin them.
- Needs a provider/model/key.

## Related

- [AI Router](ai-router.md)
- api-keys-registry
- knowledge-bases
- mcp-servers
- manage-capabilities
