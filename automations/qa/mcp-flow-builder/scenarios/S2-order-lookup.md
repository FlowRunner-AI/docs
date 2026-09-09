# S2 — Order Lookup (Condition, two Return Results)

Driven 2026-09-02 02:39–02:41 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "If an orderId is provided return {orderId, status:'shipped'}, otherwise return {error:'Missing order ID'}."

## Tool sequence (9 calls)
create_flow → list_condition_operators(STRING) → get_block_schema(condition) → add_block condition + 2× return-result (data set in
add_block config using `{{Initial Data->orderId}}` — accepted, Initial Data is not an upstream block) → set_condition_parts
(isNotNull, property `{{Initial Data->orderId}}`) → wire_edge thenComponent / elseComponent → get_flow_summary → save_flow READY → start_flow.
Flow 6FE3C654-B7D3-4173-A05B-45B5CD136D8E, version 006E68F1-92F6-4931-B625-E0E325E5C27D.

## Oracles
- **O1:** CONDITION first, thenComponent/elseComponent point at the right elements, INITIAL_DATA token with subPathSegments orderId,
  valid=true, LIVE after start. PASS.
- **O2:** S2-o2-canvas.png. See file.
- **O3:** GET `?orderId=A-1001` → `{"orderId":"A-1001","status":"shipped"}`; GET without → `{"error":"Missing order ID"}`;
  POST `{"orderId":""}` → `{"orderId":"","status":"shipped"}` (isNotNull is true for ""; correct per operator semantics — an agent
  wanting "missing or blank" must pick isNotEmpty). All 200. PASS.

## Findings
- add_block issues for a fresh Condition read: `Condition setting is required`, `One of the "Yes" or "No" connection must be connected` —
  clear and actionable; set_condition_parts cleared the first, first wire_edge cleared the second.
- Condition default resultAlias "Condition Result" with storeResult=false (fine).

## Teardown
stop_flow(006E68F1…) after O3. Flow kept for end-of-phase deletion.
