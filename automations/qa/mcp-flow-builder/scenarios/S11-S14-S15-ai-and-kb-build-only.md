# S11 / S14 / S15 — AI Agent, AI Router, Knowledge Base (build-only: no AI key setup, no KB in the workspace)

Driven 2026-09-02 03:20–03:26 UTC · dev.flowrunner.ai · Documentation Flows · flow "MCP Probe – S11 Agent"
(EB016C23-40AC-49BB-B7F5-7D0A29E577A3, version 5E2DB9F6-FEC8-4658-840D-1224D8E53DA8).

## What was built
- ai-agent "Answer Math" (ANTHROPIC / claude-sonnet-4-6 from list_ai_providers, systemPrompt+userPrompt) + agent tools HTTP_REQUEST (built-in)
  and github mergePullRequest (extension-backed) via add_agent_tool; return-result reading `{{Agent Answer->output}}` (sampleResult exposed).
- ai-router "Classify Feedback" with three decisions (complaint / praise / question) + default "Everything Else"; decisionRequest set.
- knowledge-base-list-documents with a placeholder id (knowledgeBaseId is an Expression `{text}`; no client-side existence check).

## Results
- Issues are precise: `AI Api Key is required` (agent), `AI API Key is required` / `AI Decision Request is required` / successor required (router),
  `[Merge Pull Request] connectionId: OAuth Connection is required` (tool). save_flow → INVALID with the server's generic "fix problems" message.
- **E4:** start_flow on the INVALID version → ok; server status LIVE with valid=false. Paused afterwards.
- **E15:** junk top-level patch on the extension-backed tool accepted silently; the built-in HTTP_REQUEST tool rejected the same with a field list.
- **E16:** add_block(ai-text-to-speech) rejected as deprecated while the readme recommends it.
- **E2/E3:** auto-checkpoint on the 5th mutation hit the PAUSED version and surfaced as the mutation's error while the mutation had applied.
- configure_block(ai-agent, {tools}) and add_ai_router_decision("") rejected with clear messages. list_ai_providers(ANTHROPIC, excludeDeprecated)
  returned 10 models incl. claude-opus-4-8.
- Not run (no key): agent answer, router classification, KB listing.

## Teardown
Flow PAUSED (was made LIVE by the E4 probe). Delete at end of phase.
