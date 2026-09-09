# S4 — Price Tax (List Iterator, nested Transform Data ×2, Data Bucket accumulator)

Driven 2026-09-02 02:43–02:49 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Given a list of prices, return each price with 20% tax added."

## Build (agent-chosen)
data-bucket "Init Results" (bucket Results, field results = `{{Empty List}}`) → list-iterator "For Each Price" (list `{{Initial Data->prices}}`)
→ nested: data-transformer "Add Tax" (math.multiply `{{Current Iteration Item->}}` × 1.2 NUMBER) → data-transformer "Append Taxed Price"
(arrays.add `{{Data Buckets:Results - results->}}`, `{{Taxed Price->}}`, saveToVariable Results/results) → return-result "Return Prices"
(prices = `{{Data Buckets:Results - results->}}`).
Flow E2D6B704-45B7-4D4D-8670-9F902BA9E906, version A15618BA-D89E-47FB-A2A3-5CB8A41375D9. Loop pills in add_block config were accepted for a nested block.

## Oracles
- **O1:** group LOOP with firstElementId = Add Tax, elementIds nested, bucket → nextGroupIds [loop], loop → Return Prices; valid=true. PASS.
- **O2:** S4-o2-canvas.png — three top-level blocks (bucket, loop, return) connected, Live badge. PASS.
- **O3 first run:** POST `{"prices":[10,20]}` → `{"prices":[]}` **FAIL** (see F-S4-1). After fix: `[12.0,24.0]`; `[5,7.5,100]` → `[6.0,9.0,120.0]`. PASS.
  GET `?prices=10,20` → TERMINATED 28063 "'List Iterator' block expected to receive a list … but 'String' was given" — correct engine behavior.

## Findings (driven; details in .cache/mcp-qa/findings-log.md)
1. **F-S4-1 saveToVariable silently inert without setResultToVariable=true.** configure_block accepted the bucket target with issues [];
   server received `saveToVariable: null`; run produced an empty list. No issue/warning links the two fields. Candidate subtask.
2. **F-S4-5 stop_flow pauses; PAUSED cannot be edited.** save_flow after stop_flow → `ERROR: Paused version of the flow cannot be edited`.
   The readme/list_flows/start_flow text prescribes exactly that sequence. No MCP tool returns a version to READY; the Console's Stop
   button (square icon) was needed. Candidate subtask (High).
3. **F-S4-6 list_flows wiped the session pointer** (E7): save_flow → "no flow yet — call create_flow or load_flow first" and the unsaved
   edit was orphaned. Recovered with load_flow + reapply. Candidate subtask (High).
4. F-S4-2 (E3) save over LIVE → clear server rejection `Live version of the flow cannot be edited`. Acceptable.
5. F-S4-4 get_block_schema(data-transformer, operationId) repeats the full schema + 100-entry enum per operation lookup (token cost).

## Teardown
stop_flow(A15618BA…) after O3. Flow kept for end-of-phase deletion. Note: all four probes now sit in PAUSED, not READY.
