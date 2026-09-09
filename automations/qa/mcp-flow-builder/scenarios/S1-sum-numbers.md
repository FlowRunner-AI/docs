# S1 — Sum Numbers (the ticket's own test case)

Driven 2026-09-02 02:36–02:40 UTC · dev.flowrunner.ai · Documentation Flows · Claude Code as MCP client.
Prompt: "Sum Numbers: receives comma-separated integers via the Call Flow API (GET) and returns their sum."

## Tool sequence (agent-chosen, 12 calls)
create_flow → get_block_schema(data-transformer, textBinary.parseJsonToList) → get_block_schema(data-transformer, math.sum)
→ get_block_schema(return-result) → add_block ×3 → wire_edge ×2 → configure_block ×3 (aliases + `{{Parsed Numbers->}}`,
`{{Sum Result->}}` references) → get_flow_summary → save_flow (status READY) → test_run_block(Parse Numbers) → start_flow.
Flow: A87FD230-8189-4E42-BDCF-DF7217A1C1C6, version A289CA70-889F-4B32-AAAE-6AF7F97FD06D.

## Oracles
- **O1 definition (GET /api/app/…/flow/version/…):** 3 elements, DATA_TRANSFORMER→DATA_TRANSFORMER→COMPOSE_RESULT wired in order,
  ELEMENT_LINK tokens carry the right element ids, clientValidationState.valid=true, status LIVE after start. PASS.
- **O2 Console render (S1-o2-canvas.png, 1700×1050):** three connected blocks, Live badge, no red badges. PASS.
- **O3 Call Flow API (dev-api):** GET `?numbers=10,20,30,40` → `{"sum":100.0}`; POST `{"numbers":"1,2,3.5"}` → `{"sum":6.5}`;
  GET by NAME `?numbers=5,5` → `{"sum":10.0}`. All HTTP 200. PASS. (Sum is a DOUBLE, hence `100.0`.)
- test_run_block(Parse Numbers) with no initial data: completed=true, failed=false, params `["[null]"]`, result `[null]`. Not an error — but a
  debug run of an Initial-Data-dependent block cannot be meaningful; nothing in the tool warns about that.

## Findings (leads, all driven in this run)
1. **Duplicate default resultAlias.** Both data-transformer blocks came back with `resultAlias: "Transform Data Result"` even though each
   had a distinct `name` in add_block config. No issue reported by either block. The Console derives the alias from the block name
   ("Item Quantities Result" in TD Sandbox). Two identical aliases make `{{Transform Data Result->}}` ambiguous. → Phase 1 negative test:
   reference the duplicate alias and see which block resolves. Candidate subtask.
2. Top-level `firstElementId` IS set (52DC2B39…) — same as a Console-built flow. (An earlier read of `metaInfo.firstElementId` was the wrong key; no finding.)
3. `description` saved as "" and clientMetadata carries no viewport/descriptions (Console flows carry autoSave/descriptions/viewport) —
   consistent with the serializeDraft hazard flagged for E1.
4. get_block_schema(data-transformer, operationId) returns `operations: null` although the tool text says operations is "always present".
   Doc/behavior drift, minor.
5. Return Result single-value field is `singleData` — settles the ticket's open question Q5 (spec was right, dev doc was wrong).

## Teardown
stop_flow(versionId A289CA70…) after O3. Flow KEPT (not deleted) for S16 (call-flow target) and the replay test; delete at end of Phase 2.
