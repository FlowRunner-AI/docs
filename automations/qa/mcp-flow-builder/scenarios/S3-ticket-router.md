# S3 — Ticket Router (Value Router: SIMPLE case, ENUM_LIST case, default)

Driven 2026-09-02 02:41–02:43 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Route a support ticket by category: billing → Finance, bug or crash → Engineering, anything else → General; return the team name."

## Tool sequence (12 calls)
create_flow → get_block_schema(router) → add_block router (switchExpression `{{Initial Data->category}}` in config) + 3× return-result
→ add_router_case(billing) → add_router_case([bug, crash]) → wire_edge default (branch omitted) → wire_edge ×2 with caseIds
→ get_node_details(router) → save_flow READY → start_flow.
Flow D8BB527E-4CD5-47DF-8BFC-2F689198A49D, version D59BAC51-07BF-419C-B556-687ADF838374.

## Oracles
- **O1:** switchCases = [SIMPLE "billing", ENUM `values.type:"LIST"` [bug, crash], default "Everything Else"], each with the right
  nextComponents; valid=true; LIVE. PASS. **Settles ticket Q6: the server writes and accepts `LIST`, not `SIMPLE_LIST`.**
- **O2:** S3-o2-canvas.png.
- **O3:** billing→Finance, bug→Engineering, crash→Engineering, refund→General, missing category→General. All 200. PASS.

## Findings
- Fresh router issue text `At least one successor block must be assigned.` cleared by the first wire_edge (default branch) — good.
- add_router_case default label when omitted was not exercised (labels passed). ENUM_LIST viewMode chosen automatically for 2 values.
- get_node_details shows `value` for the SIMPLE case and `value: [..]` for ENUM — while the server JSON uses `values.value[]` for ENUM;
  the tool's presentation is a simplification, acceptable.

## Teardown
stop_flow(D59BAC51…) after O3. Flow kept for end-of-phase deletion.
