<!-- GENERATED FILE - do not edit. Source: block-knowledge/ai-agent.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: AI Agent -->
# AI Agent

This block puts an AI agent to work inside your flow. You hand it a goal in plain language and a set of tools - any of FlowRunner's built-in actions, your own flows, the tools on an MCP server, or a Knowledge Base to search - and the agent decides for itself which tools to use to reach the goal, then returns its answer. It can also carry memory across runs and hand back structured data the blocks after it can read.

## How it works

You give the agent three things: a <span class="fr-control">System Prompt</span> that sets its role and rules, a <span class="fr-control">User Prompt</span> that carries the request for this run, and - through <span class="fr-control">Manage Capabilities</span> - the tools it is allowed to use. From there it works toward the goal on its own. It reads the request, and whenever finishing the job needs a fact or an action it does not already have, it reaches for one of its tools: looking something up with a built-in action, running one of your flows, calling out to an MCP server, or searching a Knowledge Base. It folds whatever comes back into its work and keeps going until it can answer. You do not wire those steps up yourself - you supply the goal and the tools, and the agent chooses which to use and when. Its reply always comes back under an `output` property on the result - plain text there, or a structured object when you turn on <span class="fr-control">Force Parsed Output</span> - so a later block reads the answer from `output`, not from the result itself. The <span class="fr-control">User Prompt</span> is usually built in the Expression Editor from earlier blocks' results, so a fresh input flows in on every run.

## When to use it

Reach for it when a step calls for judgment or open-ended work rather than a fixed rule - reading messy input and deciding what it means, gathering the right facts from several places, drafting a reply, or handling a small task from start to finish. Attach tools and it stops being something that only answers and becomes one that can act: look a customer up, search your own documents, and kick off a follow-up flow, all in a single step. Its wording varies from run to run, so use it where that is welcome - and turn on <span class="fr-control">Force Parsed Output</span> when a later block needs the result in a fixed shape.

## What the agent can do (Manage Capabilities)

<span class="fr-control">Manage Capabilities</span> is where an answer-only model turns into an agent. Open it and you choose the tools this agent is allowed to reach for, drawn from six groups:

- **Extensions** - FlowRunner's built-in actions, well over a thousand of them, grouped by the extension they come from: send an email, create or find a record, call an HTTP endpoint, post a message, and far more. These are the same actions you would otherwise drop on the canvas as blocks; here the agent can run any you attach, on its own, whenever the task calls for it.
- **MCP Extensions** - tools published by the MCP servers you have registered, grouped by server. Attach a whole server, or expand it and pick individual tools.
- **Flows** - your own flows, handed to the agent as tools it can run. A flow you already built becomes a skill the agent can call mid-task; the flow's description and the description of each of its arguments are what tell the agent when to call it and what to pass. Because the agent runs the whole flow and waits for its result, a flow tool can even pause the agent until a person responds. See [Flows as agent tools](flows-as-agent-tools-concept.md).
- **Knowledge** - your [Knowledge Bases](knowledge-bases-concept.md), exposed as document tools (add, list, and delete documents), so the agent can search your own content and ground its answer in it instead of guessing.
- **Shared Memory** - the flow's own key/value store, so the agent can stash a value mid-task and read it back later, or share state with the rest of the flow. (This is the same store that backs the agent's [Messages History](flow-memory-concept.md).)
- **Utils** - a small set of utility tools: naming the current instance, making an HTTP request directly, reading a file from a URL, and running a [Custom Cloud Code](custom-cloud-code.md) snippet the agent can feed its own inputs to.

<!-- Utils re-verified in-product 2026-08-14 (Documentation Flows, Manage AI Agent Capabilities -> Utils), post release 1.0.13 / FR-3227: exactly four tools - Assign Instance Name ("Assign a custom name to the current flow instance for identification."), Custom Cloud Code ("Runs a JavaScript snippet with typed arguments. Anything left empty is filled in by the agent."), File Reader ("Read a file from a URL. Supported file types depend on the selected AI provider and model."), HTTP Request ("Send an HTTP request to any URL with configurable method, headers, body, and query parameters."). NOTE this workspace showed FIVE categories (Extensions 3195 / Flows 33 / Knowledge 4 / Shared Memory 3 / Utils 4) - MCP Extensions appears only when MCP servers are registered, and counts have drifted from the 2026-06-24 capture (see parked follow-up: recapture ai-agent-capabilities.png + reconcile counts/groups). -->


You decide what this particular agent gets; it then decides, run by run, which of those tools it actually needs. Leave a tool's input blank and the agent fills it in itself - handy, but the value is its own guess, so pin any input that has to be exact.

![The Manage AI Agent Capabilities window. Down the left, six tool groups with counts - Extensions (1449), MCP Extensions (50), Flows (18), Knowledge (4), Shared Memory (3), and Utils (2) - above a search box. The Knowledge group is selected, listing its document tools on the right: Add Document, Delete by Filter, Delete Document, and List Documents, each with a plus to attach it.](../images/reference/ai-agent-capabilities.png)

## Example

Say a support flow receives a customer's question and you want an agent to answer it. A good answer needs facts the model does not have on its own: the customer's recent orders, and what your help articles say. This is exactly where capabilities earn their keep.

Set the <span class="fr-control">System Prompt</span> to the job the agent should do on every question:

```text
You are a support assistant. Use your tools to look up the customer and their
recent orders, and to search the help articles, then answer the question in two
or three sentences. If you are not sure, say so rather than guess.
```

In the <span class="fr-control">User Prompt</span>, feed in the incoming question. Build it in the Expression Editor so the live question flows in on every run rather than being pasted in as fixed text:

```text
{{Initial Data->question}}
```

![The AI Agent block's configuration panel: AI Model set to Claude Sonnet 4.6, an API key filled in, a System Prompt telling the agent to use its tools to look up the customer and search the help articles, and the User Prompt shown as a bound reference pill reading "Initial Data question". The MANAGE CAPABILITIES button at the top of the panel is where its tools are attached next.](../images/reference/ai-agent-config.png)

Now open <span class="fr-control">Manage Capabilities</span> and attach two tools: a built-in action that fetches a customer's recent orders, and your Help Articles Knowledge Base. That is the whole of the wiring - you are handing the agent the tools, not scripting when to use them.

When the flow runs, the agent reads the question, decides on its own that it needs the order history and a help article, calls the lookup action and searches the Knowledge Base, and writes an answer grounded in both - none of which you wired step by step. Turn on <span class="fr-control">Force Parsed Output</span> and name the fields you want in the <span class="fr-control">System Prompt</span>, and the structured answer comes back inside the result's `output` property, ready for a later block to act on:

```json
{
  "output": {
    "answer": "Your most recent order, #10473, shipped Tuesday and is due to arrive Friday. If it has not arrived by then, reply here and we will open a trace.",
    "needsHuman": false
  }
}
```

Because the reply always arrives under `output`, a later block reads `output->needsHuman` to decide whether to send the answer straight to the customer or route the ticket to a person, and shows `output->answer` either way.

## Configuration

| Field | Description |
| --- | --- |
| AI Model | Required. The model to call, chosen from one list grouped by provider (Claude, GPT, Gemini, and others); the provider is implied by the model you pick. |
| AI API Key | Required. The key that authorizes the call. Pick a key you have already saved, or type a new one right here. Without a valid key the call cannot run. |
| System Prompt | The standing instruction that sets the agent's role, behavior, and rules, applied to every request this block makes. |
| User Prompt | The request for this run. Usually built in the Expression Editor from earlier blocks' results, so the input changes from run to run. |
| Manage Capabilities | Opens the window where you attach the agent's tools - built-in actions, MCP server tools, your own flows, and Knowledge Bases. See "What the agent can do" above. |
| Files | Files for the model to read alongside the prompts - each entry is a URL and a MIME Type, added with the <span class="fr-control">+</span> control. The files are attached to the first message of the conversation; with <span class="fr-control">Messages History</span> on they are sent only once, at the start of the dialogue. What the model can read depends on the provider: Anthropic takes images (JPEG, PNG, GIF, WebP) and PDF; Gemini takes images, PDF, audio, video, PPTX and more (not DOCX, DOC, or EPUB); OpenAI pro models take images and most document formats, OpenAI standard models images only; other providers do not support file reading. |
| Messages History | When on, the model is also fed the messages from recent prior runs of this block, up to the limit you set (maximum 20), so it can carry context across separate interactions. This is the agent's memory across runs (see [Agent Memory](flow-memory-concept.md)), and it is kept in Shared Memory. |
| Force Parsed Output | When on, the block asks the model to return structured JSON instead of plain text, by adding an instruction to your System Prompt. Use it when a later block needs to read specific fields from the result. |
| LangSmith Settings | Connects this block to LangSmith, an outside service for tracing and monitoring AI calls, so you can inspect what was sent and returned. |

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Reference Result Data As | The alias used to reference this block's result in later blocks. |
| Assign to a Variable | Optionally store the result in a Data Bucket variable too; you choose the bucket and the variable name. |
| Skip Block | When on, the block is skipped during execution and the value in Simulated Result is used as its output. |
| Logging | What to log to the Logging panel while the flow is LIVE, both on start and on completion. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Things to watch for

- The reply always arrives in the result's output property. Read it as `output` for the text, or `output->yourField` for a named field when <span class="fr-control">Force Parsed Output</span> is on. Reading the result directly, without going through `output`, gets you nothing.
- The output is not deterministic: the same prompts can come back worded differently from one run to the next, so this block suits work where the wording can vary, not a step that needs an identical value every time. Write downstream steps to tolerate that, and when a later block needs the result in a fixed shape, turn on <span class="fr-control">Force Parsed Output</span> so the model returns structured JSON instead of prose.
- When you attach a tool but leave one of its inputs blank, the agent fills that input in itself while it runs. That is convenient, but it means the value is the agent's guess. If an input has to be a specific value, set it explicitly so the agent cannot choose its own.
- The block cannot run without a model and a valid API Key. You can pick a saved key or type a new one in the <span class="fr-control">AI API Key</span> field.
- <span class="fr-control">Messages History</span> only carries context when it is turned on, and even then only up to the limit you set (maximum 20). With it off, each run starts with no memory of earlier runs.
- While testing, you can avoid a real model call - and its cost - by turning on <span class="fr-control">Skip Block</span> and putting a sample reply in <span class="fr-control">Simulated Result</span>, so the rest of the flow runs against that stand-in instead.

## Related

- [Flows as Agent Tools](flows-as-agent-tools-concept.md)
- [Agent Memory](flow-memory-concept.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
- [AI Router](ai-router.md)
