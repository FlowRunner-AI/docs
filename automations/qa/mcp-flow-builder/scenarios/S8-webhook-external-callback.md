# S8 — Webhook (External Callback trigger → Return Result)

Driven 2026-09-02 02:58–03:00 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Wait for an external system to POST a payload to a webhook, then return the payload's id."

## Build (7 calls)
add_block external-callback "Webhook" (alias Webhook Payload) → add_block return-result → get_node_details(trigger) → wire_edge →
configure_block return {id `{{Webhook Payload->id}}`, receivedAt `{{Current Time}}`} → save_flow READY → start_flow.
Flow C35E7324-E096-4B10-B0CA-D1D20E8F2CD3, version 297D4A5C-82E3-49F9-8E9E-6053DE3340DE, trigger flowElementId 7A725CBD-71E6-46CB-AC48-E7C4EC4731D6.

## Oracles
- **O1:** TRIGGER first, `TRIGGER_DATA` token {label "Webhook Payload", subPath id} in the Return Result; LIVE. PASS.
- **O2:** S8-o2-canvas.png.
- **O3:** get_node_details returned `callbackUrl` BEFORE save (flowElementId exists at add_block time — the source-analysis prediction
  "only after save" was wrong; the tool description is right). POST `{"id":"evt-42"}` to the URL → `{"executionId":…}` 200;
  GET /execution/{id} → status COMPLETED, completion NORMAL, hasErrors false, 271 ms. `?execution=any` → 200 with a new executionId. PASS.
- test_run_block on the trigger → `pending: true`, `completed: false`, plus a clear `note` that the trigger is armed. Matches description.

## Findings
- callbackUrl embeds the workspace REST API key (same as the Console's trigger URL) — expected, but the MCP response now carries a secret
  into the agent's context. Worth a note in the readme ("treat as a password") — the Console page says so, the tool does not.
- Return Result output is not observable through the trigger activation API (by design); verified completion via the execution endpoint.

## Teardown
stop_flow(297D4A5C…). Flow kept for end-of-phase deletion.
