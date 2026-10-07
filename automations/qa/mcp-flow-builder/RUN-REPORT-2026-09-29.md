# FR-3247 MCP Flow Builder: re-test, 2026-09-29

Environment: dev.flowrunner.ai, workspace Documentation Flows (DE8F1ED3-0193-404C-BF6A-EAC9D52D5838). The server is the
29-tool, request-scoped redesign (console PR #632). Claude Code's own connection dropped with `404 Session not found`
(FR-3687), so the run used `tools/mcpc.mjs`: the MCP SDK 1.30 with the replay OAuth client. It reconnects and resends
on that 404, which is safe because the 404 comes back before the tool runs. Every call is logged to
`.cache/mcp-qa/sdk-run-2026-09-29.jsonl`. Real runs used the dev Call Flow API (`scratchpad p2f/callflow.py`, which
never prints the key).

## Flows built and run (all "MCP Probe - *", left on dev)

| Flow | What it covers | Real-run result |
|---|---|---|
| Sum Numbers | one 7-op batch, localAlias, Initial Data | GET `numbers=10,20,30,40` -> `{"sum":100.0}`; POST by name -> `{"sum":6.5}` |
| Ticket Router | router, add_router_case (single + any-of), default | billing/outage/bug/refund -> Finance/Engineering/Engineering/Support |
| Order Size | condition, set_condition_parts, then/else | POST 250 -> big, 42.5 -> small; GET `total=250` -> small (GET values are text; documented) |
| Cart Total | data-bucket, list-iterator, groupId, saveToVariable | ints -> `{"total":22}`; any decimal -> EL1031E (FR-3690); first save INVALID (FR-3688) |
| Status Check | http-request + error-handler | success ok; 404/500 -> handler with code null, message "" (FR-3494) |
| Visit Counter | shared-memory, `{{Shared Memory->key}}` | 1, 2, 3 across runs (key `mcpProbeVisits` = 3 left in the workspace) |
| Sum Caller | call-flow into Sum Numbers | `{"fromSubflow":6.0}` |
| Custom Ping | APP custom extension action | saves INVALID "'Model name for Api Service action' is required" (FR-3310; canvas-built "Params Probe" too) |
| Edge Cases, Sum Types, Loop First Save | ticket verifications | see below |

## Ticket verification (comment posted on each)

- Fixed: FR-3365 (batching), FR-3481 (description / notes / placeholder data / schedule / flow memory survive a save),
  FR-3483 and FR-3484 (obsolete by design; two concurrent clients showed no cross-talk), FR-3485 (LIVE and PAUSED edits
  rejected, nothing applied), FR-3486 (start refuses INVALID), FR-3487 (self-loop / duplicate / cycle / second handler /
  wiring after Return Result all rejected), FR-3488 (clear "no entry block" issue; isFirstElement rules), FR-3489,
  FR-3491 (a newly deployed extension was visible within about 1 s), FR-3492 (item 2 detected, not rejected).
- Partly fixed: FR-3490. The readme still has two dangling "known gap, see below" references. New stale text:
  `list_connections({})`, `get_flow_schedule({})`, "this session", `load_flow` in the `list_workspaces` description.

## New defects filed

- FR-3687 (Highest): `404 Session not found` on about half of requests (33/60 in the raw probe). Claude Code drops the server.
- FR-3688 (High): the first save of a List Iterator is INVALID with zero issues; a second save makes it READY.
- FR-3689 (High): FLOW-scoped calls take 14-27 s (a raw single request takes 14.3 s for a 3-block flow).
- FR-3690 (Medium, platform bug): Transform Data Sum with separate arguments 0 and 7.5 fails with EL1031E.
- Comments: FR-3663 (the Telegram ranking example), FR-3310 (still on dev, canvas too), FR-3494 (still, 404 too).
  FR-3247 has a summary plus 4 questions for the docs and the website brief.

## Not tested

Production (app.flowrunner.ai/mcp answers 401, so it is deployed; which design it runs is unknown); AI Agent, AI Router
and Knowledge Base runs (no AI key setup or KB in the dev workspace); the external-callback trigger; schedules firing;
parallel + Synchronize; Claude Desktop / claude.ai connectors; a non-default viewport under FR-3481.

## Left on dev

- LIVE probe flows: Sum Numbers, Ticket Router, Order Size, Cart Total, Status Check, Visit Counter, Sum Caller.
- Not live: Edge Cases, Sum Types, Loop First Save, Custom Ping.
- Custom extension `mcpcatalogprobe` (deployed from ~/dev/fr-cli-docs-project).
- Shared memory key `mcpProbeVisits`.
- Sum Numbers carries a disabled daily schedule, a description, placeholder data `taxRate` and a block note
  (the FR-3481 fixture).
