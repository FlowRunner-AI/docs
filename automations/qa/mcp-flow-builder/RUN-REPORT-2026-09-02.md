# FR-3247 MCP Flow Builder — QA run report, 2026-09-02

Environment: dev.flowrunner.ai, workspace Documentation Flows (DE8F1ED3-0193-404C-BF6A-EAC9D52D5838), server "FlowRunner MCP Flow Builder"
0.1.0 at https://dev.flowrunner.ai/mcp, client = Claude Code (OAuth 2.1/PKCE/DCR, consent by Mark 02:32 UTC). 300+ tool calls recorded
(automations/.cache/mcp-qa/run-2026-09-01.jsonl). Every flow built was a throwaway "MCP Probe – *" and was deleted at the end (14 flows).
Oracles per scenario: O1 server definition via the Console API, O2 Console canvas screenshot, O3 real run via dev-api Call Flow API.

## Scenarios (Phase 2)
| # | Scenario | Result |
|---|---|---|
| S1 | Sum Numbers (Transform ×2, Return) | PASS all oracles; `{"sum":100.0}`; replayed 18/18 by replay.mjs |
| S2 | Order Lookup (Condition) | PASS both branches |
| S3 | Ticket Router (Value Router SIMPLE + ENUM + default) | PASS 5 inputs; settles Q6 (`values.type: "LIST"`) |
| S4 | Price Tax (List Iterator + bucket accumulator) | PASS after fix — first run returned `[]` (saveToVariable inert without setResultToVariable) |
| S5 | Countdown (Repeat, Condition, Break) | PASS with `<=`; `equal` on a Double value never matched (engine) |
| S6 | HTTP + error handler | PASS routing; 5xx reaches handler with code null / message "" |
| S7 | Data Bucket references | covered by S4/S5 |
| S8 | Webhook (External Callback) | PASS; callbackUrl available pre-save; execution COMPLETED |
| S9 | Daily schedule | PASS (set/get/Console dialog); weekDays [0,9] accepted |
| S10 | Open-Meteo extension (no account) | BLOCKED: server rejects APP-hosted extension actions ("Model name … is required") — Console too → platform (FR-3310) |
| S11/S14/S15 | AI Agent, AI Router, Knowledge Base | build-only (no AI key / KB in workspace); validation messages correct |
| S12 | Parallel fan-out + Synchronize + Wait | PASS after typing fix (text literal in numeric field rejected by server only) |
| S13 | Shared Memory across runs | PASS (nobody → Alice → Bob) |
| S16 | Instance name + Call Flow → S1 + Stop/Start Scheduled Runs | PASS after starting S9 (target must be LIVE) |

Q5 (`singleData`) and Q6 (`LIST`) from the ticket's open-questions ledger are settled by the saved JSON; Q8: keyword pills are saved WITH parentheses.

## Phase 1 — tool surface
42/42 tools present; 41 exercised (remove_agent_tool not). Coverage table: tool-surface.md. All documented-shape mismatches in
docs/features/mcp-flow-builder/api-reference.md confirmed (appId vs workspaceId; plain strings vs {text} for set_condition_parts /
add_router_case / set_data_bucket_fields; list_block_types params).

## Phase 3/4 — edge cases (all driven)
E1 data loss on load→save (CONFIRMED, Highest) · E2/E3 auto-checkpoint on paused/live version surfaces as tool error (CONFIRMED) ·
E4 start_flow on INVALID → LIVE (CONFIRMED) · E5 self-loop/duplicates accepted; self-loop breaks reference resolution (CONFIRMED) ·
E6 first-block removal → firstElementId null, server "no blocks" (CONFIRMED) · E7 list_flows wipes pointer (CONFIRMED) · E8 set_context
same-ws no-op, echoes flowId null · E9 second client hijacks session (CONFIRMED via replay.mjs) · E10 bucket fields replace · E11 stale alias
label · E15 extension-backed agent tool patch unvalidated (CONFIRMED) · E16 readme recommends deprecated blocks (CONFIRMED) · E17 doc shapes
rejected by input validation (CONFIRMED). Not run: E12 (test_run twice), E13 (empty-workspace tools), E14 (deprecated block round-trip),
token expiry/refresh after 1 h, Claude Code restart, multi-pod affinity.

## Phase 5 — FlowRunner registering its own /mcp
Registration SUCCEEDS on dev (consent popup, callback, 42 tools listed) — Mark's 2026-08-06 failure no longer reproduces. FR-3373: an email
as Custom Header Name is stored unvalidated (`{"mark@backendless.com": "…"}`); fix branch not on dev. Server deleted after the test.

## Platform findings (not MCP)
APP-hosted custom extension actions rejected on save (modelName null; Console too) → FR-3310 comment. Condition EQUALS vs Double → new bug.
Handle Error on HTTP 5xx: code null, message "" (docs promise a code) → new bug. start/stop-scheduled-runs require LIVE target (docs gap).

## Artifacts
scenarios/*.md · tool-surface.md · tools/record-hook.sh · tools/replay.mjs (+package.json) · .cache/mcp-qa/{findings-log.md, run-*.jsonl,
S*-o1-definition.json, S*-o2-canvas.png, P5-*.png, replay-S1-result.md, readme-tool-output.md, inventory-2026-09-02.md, env.json}.

## Left on dev for Mark to decide
Two OAuth client registrations (Claude Code; "FlowRunner MCP QA replay"). Shared-memory key `lastCaller` = "Carol" in Documentation Flows.
Telegram service config has a `notARealField: null` entry from the validation probe.

## Jira (posted 2026-09-02 03:43–03:45 UTC)
Run report comment on FR-3247. Subtasks under FR-3247: FR-3481 (Highest, E1 data loss), FR-3482 (High, stop_flow pauses), FR-3483 (High,
list_flows wipes pointer), FR-3484 (High, second client hijack), FR-3485 (checkpoint masquerade), FR-3486 (start INVALID), FR-3487 (self-loop /
duplicate edges), FR-3488 (entry block removal), FR-3489 (saveToVariable inert), FR-3490 (agent-facing text defects), FR-3491 (stale catalog),
FR-3492 (validation gaps). Bugs: FR-3493 (Condition EQUALS vs Double), FR-3494 (Handle Error 5xx empty). Comments: FR-3373 (header repro),
FR-3310 (modelName rejection for APP extensions).
