# FR-3247 "Prompt to Flow" — automated QA plan for the MCP Flow Builder

## Context

FR-3247 (New Feature, Highest, Waiting for Release, assignee Inna) delivers the MCP Flow Builder: an MCP server at
`https://dev.flowrunner.ai/mcp` ("FlowRunner MCP Flow Builder (Beta)", server version 0.1.0) that lets an AI client
build, save, schedule, start and test-run FlowRunner flows from natural language. It shipped to dev in console PR #498
(2026-08-06) plus #513 (build fix) and #515 (FR-3329, `appId`→`workspaceId` rename). The ticket description is the
knowledge-capture handoff (protocol spec, generation guide, generator system prompt, requirements schema, extension
catalog — all six docs are on disk at `/Users/mark/Documents/FlowRunner/Development/Prompt to Flow/`). Its own §5
names the biggest gap: **"there is no end-to-end validation harness … generate → import → confirm it runs."** This plan
is that harness, with Claude Code as the MCP client.

Related tickets: FR-3365 (sub-task, Open — `apply_operations` batching; **not in the current dev build**, so the plan is
written against the live `tools/list`, not a fixed tool list), FR-3373 (Reopened — auth-header autofill in the MCP
Servers registration form; fix exists only on a feature branch, not merged to dev), FR-3225 (the broader
"FlowRunner MCP" atomic-actions design — a different product surface, out of scope here), FR-3275 (Closed).

Source of truth used for this plan: local checkout `/Users/mark/Documents/FlowRunner/Development/console` at
`c8c208833b` (dev, 2026-08-28) — `server/src/mcp-flow-builder/**`, `docs/features/mcp-flow-builder/**`,
`server/src/router/public/mcp-oauth/`, `client/src/screens/mcp-servers/**`, `server/__tests__/mcp-flow-builder/**`.

## Decisions taken (Mark, 2026-09-01)

| Decision | Choice |
|---|---|
| Client paths | (1) Claude Code as the MCP client — primary. (2) FlowRunner registering its own `/mcp` (the 2026-08-06 attempt) incl. the FR-3373 regression. Raw curl/SDK protocol probes are **out of scope** (not selected). |
| External accounts | Use whatever is already connected in Documentation Flows on dev. Inventory first; run end-to-end only where a connection / AI key exists; everything else is "built, not run". No new OAuth by Mark. |
| Reporting | Run report as a comment on FR-3247 + **one subtask per confirmed defect** (Vladimir's 08-06 request; standing rule "Jira is the channel"). Doc-vs-code drift goes in the report, not subtasks. |
| Harness | Claude-driven live run, with every MCP call recorded to JSONL by a hook, plus a Node replay script (`@modelcontextprotocol/sdk`) for deterministic re-runs after FR-3365 lands. |

Standing constraints that bind every step: workspace boundary = **Documentation Flows only** (`list_workspaces`
returns every app the account can see — the plan uses exactly one id and never touches another); browser viewport
≥1600×1000 before any canvas judgment; no Jira ticket without a repro driven immediately before filing; every probe
flow is named `MCP Probe – <scenario>` and deleted at the end of its scenario, with the deletion logged.

## What the system under test actually is (from source)

- **42 tools, no resources, no prompts.** Registered in a loop from `tools/index.ts:46-99`; `readme` is a *tool*
  (must be called first), not an MCP prompt/resource. Results are `JSON.stringify` in one text block; errors come back
  as `isError: true` with text `<BAD_REQUEST|NOT_FOUND|VALIDATION_ERROR|INVALID_OPERATION|ERROR>: <msg>` (500-char cap).
- **Auth:** OAuth 2.1 + PKCE with dynamic client registration; the issued bearer **is the developer auth key**
  (account-wide, `scopes_supported: []`, **no workspace picker on consent**). `requireAuth` checks presence only; an
  invalid token fails *inside* the tool call as `isError`, never as 401. Identity cached 60 s per token.
- **Workspace = a tool parameter** (`set_context`, `create_flow`, `load_flow`, `list_flows` …). The console does no
  authorization check on `workspaceId`; only the Java backend rejects. `list_flows` / `list_connections` **mutate the
  session pointer as a side effect.**
- **State:** one active `(workspace, flow)` per **account** in Redis (sliding 1 h TTL) — all clients on the same token
  share and can clobber one draft. MCP transport sessions are process-local (a second pod → `400 No valid session ID`).
  **Auto-checkpoint PUTs the real flow every 5 mutations**, so partial/invalid flows reach the server without
  `save_flow`. `save_flow` and `start_flow` are **not gated on issues**; saving over a LIVE version is only warned in prose.
- **29 addable built-in types** (`block-schemas.ts:36-66`); `ai-content-moderation` / `ai-create-transcription` /
  `ai-text-to-speech` are hard-rejected as deprecated **although the `readme` tool still tells the agent to use them**;
  `sub-flow` and `ai-assistant` are not addable at all.
- **Known drift:** `docs/features/mcp-flow-builder/api-reference.md` says `appId` (code: `workspaceId`), says
  `set_condition_parts.property` / `add_router_case.values` / `set_data_bucket_fields.value` are plain strings (code:
  `{ text, type? }`), documents params `list_block_types` no longer takes, and omits 7 tools.
- **Probable data-loss hazard:** `serializeDraft` (`draft/lifecycle.ts:105-115`) rebuilds the envelope from a
  `flowMeta` that carries only `{id,name,flowGroupId,version,clientTimeZone}` → `description`, `placeholderData`,
  `viewport`, per-block descriptions and `metaInfo` (possibly the schedule) look like they are **dropped on
  `load_flow` → `save_flow`** of a Console-built flow. Must be confirmed empirically (scenario E1).

## Phase 0 — Setup (one session, ~1 h, one manual click from Mark)

1. **Register the server in Claude Code** (local scope, untracked):
   ```
   claude mcp add --transport http flowrunner-dev https://dev.flowrunner.ai/mcp -s local
   ```
   then `/mcp` → authenticate. Claude Code performs discovery → DCR at `/developer/oauth2/client/mcp-register` →
   opens `https://dev.flowrunner.ai/oauth2/consent?...` in the system browser. **Mark's only manual step:** be logged
   in on dev.flowrunner.ai in that browser, tick "I recognize and trust this URL", click Authorize. Record: client name
   shown, redirect URI shown, whether the token later refreshes (check after >1 h idle in Phase 5).
2. **Recorder hook.** Add a `PostToolUse` hook (matcher `mcp__flowrunner-dev__.*`) in
   `.claude/settings.local.json` running `automations/qa/mcp-flow-builder/tools/record-hook.sh`, which appends
   `{ts, tool_name, tool_input, tool_response}` from stdin to `automations/.cache/mcp-qa/run-<date>.jsonl`.
   This makes the replay log automatic rather than hand-copied.
3. **Boundary lock.** First calls: `readme` → `list_workspaces` → pick the entry named exactly `Documentation Flows`
   → `set_context({workspaceId})`. Write that id to `automations/.cache/mcp-qa/env.json`. Every later call that takes
   `workspaceId` uses that value and nothing else. Also read the workspace **REST API key** from Workspace Settings on
   dev (Playwright, Documentation Flows) into `env.json` — needed for the Call Flow API oracle.
4. **Inventory (decides scenario coverage):** `list_connections`, `list_ai_api_key_setups`, `list_knowledge_bases`,
   `list_extension_services`, `list_block_types`. Save raw outputs. Mark scenarios S9/S10/S11/S13 as runnable or
   build-only based on what exists.
5. **Playwright profile check** (existing `.mcp.json` server): viewport resize to ≥1600×1000; confirm URL path is
   `/app/Documentation%20Flows/` before any product action; kill a stale profile lock if present (procedure in
   `automations/.cache/orientation/notes.md:51-56`).

Files created: `automations/qa/mcp-flow-builder/{TEST-PLAN.md, tools/record-hook.sh, tools/replay.mjs,
scenarios/*.md}` (tracked); `automations/.cache/mcp-qa/**` (gitignored raw logs, screenshots, exported JSON).

## Phase 1 — Tool-surface conformance (every one of the 42 tools touched)

Goal: each tool called at least once with a valid input **and** once with a representative invalid input; the actual
`tools/list` schema and result shapes recorded and diffed against `api-reference.md` and the `readme` text.

| Group | Tools | Valid probe | Invalid probe (expected error text, from source) |
|---|---|---|---|
| Session | `readme`, `set_context` | as in Phase 0 | `set_context` with an unknown workspace id → observe: console does not pre-validate; what does the backend say? |
| Lifecycle | `list_workspaces`, `list_flows`, `create_flow`, `load_flow`, `save_flow`, `start_flow`, `stop_flow`, `set_flow_schedule`, `get_flow_schedule` | build "MCP Probe – Surface" | `save_flow` before `create_flow` → `INVALID_OPERATION: No real flow to save to…`; `set_flow_schedule({schedule:'custom'})` w/o `everySeconds`; `weekly` w/o `weekDays`; `weekDays:[0,9]` (no range validation in code — record what the backend does) |
| Catalog | `list_block_types`, `list_extension_services`, `list_extension_methods`, `search_extensions`, `get_block_schema`, `get_service_config`, `set_service_config`, `list_knowledge_bases` | `get_block_schema` for all 29 types + `data-transformer` with an `operationId` | `get_block_schema({type:'ai-text-to-speech'})` → deprecated rejection **while `readme` recommends it** (defect candidate); `type:'sub-flow'` → NOT_FOUND; `search_extensions({query:''})` → silent `[]`; `search_extensions({service:'Nope'})` → throws; `set_service_config` on a `shared:true` field |
| Graph | `add_block`, `configure_block`, `wire_edge`, `remove_edge`, `remove_block` | per scenarios | `add_block('break-repeat')` outside a loop; `configure_block` with `conditionParts` (reserved) / `type` (structural) / unknown key; `wire_edge` twice same pair (no duplicate guard); self-loop; `remove_edge` then check phantom edge |
| Complex fields | `list_condition_operators`, `set_condition_parts`, `add_router_case`, `add_ai_router_decision`, `set_data_bucket_fields` | per scenarios | plain-string `property` (as the doc says) vs `{text}` (as code wants) — record which the server accepts; `add_router_case` duplicate values |
| Extension params | `resolve_dictionary` | only if a connected service with a dictionary param exists | param without dictionary; missing `connectionId`; unmet `dependsOn` |
| Connections | `list_connections`, `set_connections`, `get_connection_url` | inventory; `get_connection_url` for a connected service's block type | `get_connection_url({type:'condition'})` → "doesn't need a connection"; a string that is both a serviceId and a block type |
| AI | `list_ai_providers`, `list_ai_api_key_setups`, `add_agent_tool`, `remove_agent_tool`, `configure_agent_tool` | S11 | `add_agent_tool` on a non-agent node; unknown toolId; top-level patch with junk key on a schema-less tool (code applies it unvalidated — defect candidate) |
| Inspection | `get_flow_summary`, `get_node_details`, `get_flow_json` | every scenario | `get_node_details` unknown id; `get_flow_json({name})` rename side effect |
| Test run | `test_run_block` | S1, S2 | on unsaved draft → hash rejection; on a group; on a node with issues; note it re-executes (not polls) when called twice |

Oracle: recorded JSONL + a generated `tool-surface.md` table (tool, valid result shape, invalid result text, matches
doc Y/N). Secrets check: assert `list_ai_api_key_setups` output has no `keys`.

## Phase 2 — Prompt-to-Flow scenarios (the core value test)

Each scenario = a **natural-language prompt** (I act as the agent that turns it into tool calls, no scripted
sequence), then three independent oracles:

- **O1 Definition:** authenticated `GET /api/app/<workspaceId>/automation/flow/version/<versionId>` via the Playwright
  session (independent of the MCP server's own `get_flow_json`) — assert element types, `nextElementIds`,
  `firstElementId`, `clientValidationState.valid`, `status: READY`.
- **O2 Console render:** open the flow in the editor at ≥1600×1000, screenshot; no red badges, graph shape matches.
- **O3 Run:** `start_flow`, then invoke via the Call Flow API on dev
  (`https://dev-api.flowrunner.ai/{workspaceId}/{apiKey}/automation/flow/{flowId}/activate-blocking`) or the trigger
  URL / schedule, and assert the returned body; then `stop_flow`, delete the flow via the Console, log the deletion.

| # | Prompt (synthetic, newcomer-clear) | Blocks exercised | Runnable? | Pass criteria |
|---|---|---|---|---|
| S1 | "Sum Numbers: receives comma-separated integers via the Call Flow API (GET) and returns their sum." (the ticket's own test case) | data-transformer ×2 (`textBinary.parseJsonToList`, `math.sum`), return-result | yes | GET `?numbers=10,20,30,40` → `{"sum":100}`; `test_run_block` on each transformer returns the intermediate value |
| S2 | "Order Lookup: if an orderId is provided return {orderId, status:'shipped'}, otherwise return {error:'Missing order ID'}." | condition + set_condition_parts (isNotNull), return-result ×2 | yes | both branches via API; mirrors the documented Order Lookup example |
| S3 | "Route a support ticket by category: billing → 'Finance', bug or crash → 'Engineering', anything else → 'General'; return the team name." | router + add_router_case (SIMPLE and ENUM_LIST), default branch, return-result ×3 | yes | 4 inputs → 3 teams; default wiring correct (`branch` default = defaultCase) |
| S4 | "Given a list of prices, return each price with 20% tax added." | list-iterator group, data-transformer inside (`{{...}}` loop pill), data-bucket to lift results, return-result | yes | POST `[10,20]` → `[12,24]`; `isFirstElement` inside group; `break-repeat` misuse rejected |
| S5 | "Count down from 5 to 0 with a Repeat loop and stop early when the counter hits 2." | repeat + set_condition_parts on repeat, data-bucket, break-repeat inside | yes | run completes; result shows break honored |
| S6 | "Call https://httpbin.org/status/500 and, if it fails, return {error:true, message}." | http-request, error-handler, data-transformer (`general.createObject`), return-result | yes | error branch returns message; happy path with `/status/200` |
| S7 | "Store a greeting prefix in a variable and return prefix + the caller's name." | data-bucket + set_data_bucket_fields, `{{Data Buckets:…}}` reference in return-result | yes | reference string from the tool response resolves at run time |
| S8 | "Wait for an external system to POST a payload to a webhook, then return the payload's `id`." | external-callback, return-result | yes | `get_node_details` returns `callbackUrl` **only after save** and only if a default API key exists (record both states); POST to the URL → run |
| S9 | "Every day at 08:00 ping https://httpbin.org/get." | http-request + `set_flow_schedule({schedule:'daily'})` | yes (then disable) | `get_flow_schedule` echoes; Console Schedule dialog shows it; disable + delete after |
| S10 | "When <connected service> …, send …" using whatever `list_connections` returned (e.g. Telegram sendMessage) | extension action via `search_extensions`, `configure_block({params, connectionId})`, `resolve_dictionary` if a dictionary param exists | only if connected | message actually arrives, else "built, status READY" |
| S11 | "An AI agent that answers 'what is 2+2' using provider X" (+ one agent tool if a service is connected) | ai-agent, add_agent_tool, configure_agent_tool | only if an AI key setup exists | `test_run_block` returns an answer; tools listed in `get_node_details.tools` |
| S12 | "Run two HTTP GETs in parallel, wait for both, then wait 2 s and return 'done'." | fan-out wiring, synchronize, wait, actions-group, return-result | yes | both branches complete; synchronize `maxWaitingTime` set |
| S13 | "Remember the last caller's name across runs and return the previous one." | shared-memory-put / shared-memory-read (+ Flow Memory settings if the tool exposes them) | yes | second run returns first run's value |
| S14 | "Classify free text as complaint / praise / question with an AI Router." | ai-router + add_ai_router_decision ×3 | only if AI key exists | decisions wired; run classifies |
| S15 | "List the documents in knowledge base X." | knowledge-base-list-documents | only if a KB exists | result lists documents |
| S16 | "Name the running instance after the caller's orderId." + "Start the scheduled runs of flow 'MCP Probe – S9'." | execution-name, start-scheduled-runs / stop-scheduled-runs, call-flow (sync) into S1 | yes | instance name visible in Instances screen; call-flow returns S1's sum |

Generation checklist applied to every scenario (from the ticket's Generation Guide §6): invocation pattern correct,
GET strings vs POST typed values handled, `firstElementId` set, all `{{…}}` references resolve, notes on blocks.
Any scenario where the **agent** (me) needed information the `readme`/schemas did not provide is itself a finding
("capabilities are knowledge, not questions" — Generation Guide §0).

## Phase 3 — Edge and negative cases derived from the source (bug candidates)

Ordered by likely severity; each is a fresh repro with exact call + response saved.

| # | Case | Expected per code | Why it matters |
|---|---|---|---|
| E1 | Console-built flow with description, placeholder data, viewport, schedule, per-block descriptions → `load_flow` → `save_flow` → diff O1 before/after | fields dropped (`serializeDraft` hard-codes empties) | **data loss on any AI edit of an existing flow** |
| E2 | Build 5 mutations without `save_flow` → check server (O1) | auto-checkpoint pushed a partial/invalid flow | invisible server writes |
| E3 | `start_flow` a LIVE version, then `configure_block` ×5 (auto-checkpoint) and `save_flow` | prose warns only; nothing enforces | saving over LIVE |
| E4 | `save_flow` / `start_flow` with red issues | not gated | agent can go broken draft → LIVE |
| E5 | `wire_edge` twice; self-loop A→A; cycle A→B→A; then `remove_edge` once | duplicate edges, phantom remains | graph corruption |
| E6 | add A, add B, `remove_block(A)`, `save_flow` | `firstElementId: null` | unrunnable flow saved |
| E7 | `list_flows({workspaceId: same})` mid-draft; observe pointer + `get_flow_summary` after | pointer rewritten, `flowId` from `flowMeta` | read-only tool mutates state |
| E8 | `set_context({workspaceId: same})` with a different flow loaded | no-op (guarded by `flowId !== undefined`) | surprising semantics |
| E9 | Two clients, same token (Claude Code + replay script): B calls `set_context` while A is mid-draft | A's draft wiped / pointer switched | one-draft-per-account |
| E10 | `set_data_bucket_fields` / `set_condition_parts` second call with one item | replaces whole array | no additive path |
| E11 | Rename `resultAlias` after a `{{ref}}` exists | reference breaks silently | documented, unenforced |
| E12 | `test_run_block` twice on an HTTP POST block; and a >24 s block | re-executes; returns `completed:false` not error | side effects |
| E13 | Tools that never check for an empty workspace (`list_knowledge_bases`, `get_service_config`, …) called with a fresh pointer | request to `/api/manage/app//…` | malformed URL |
| E14 | Deprecated / `sub-flow` block inside a Console-built flow → `load_flow` → `configure_block` → `save_flow` | patchable but never re-addable | round-trip asymmetry |
| E15 | Extension-backed agent tool, `configure_agent_tool` top-level patch with junk keys | applied unvalidated | silent config garbage |
| E16 | `readme` recommends `ai-text-to-speech` etc.; `add_block` rejects | contradiction in the agent-facing guide | agent dead-end |
| E17 | Doc-shape inputs (plain strings for `property`/`values`/`value`) | rejected or mis-parsed | doc drift → agent failures |

## Phase 4 — Session, auth and lifecycle through the Claude Code client

- Reconnect after Claude Code restart: is the transport session re-initialized cleanly and is the **draft** intact
  (Redis) — expect yes/yes.
- Leave the session idle >1 h: token refresh (advertised `refresh_token`) and Redis pointer expiry (sliding 1 h TTL) —
  record which breaks first and how the failure surfaces to the agent.
- Revoke the OAuth client on dev mid-session (if a UI exists) → next call: `isError` text vs 401; 60 s identity cache.
- Two Claude Code sessions with the same token, same flow → concurrent `configure_block`: lock serializes (30 s TTL);
  observe ordering and whether either call is lost.
- Load-balancer affinity: repeat the same session over several minutes; any `400 No valid session ID` indicates a
  second pod without sticky sessions (record, do not assume).

## Phase 5 — FlowRunner registering its own `/mcp` (Mark's 08-06 attempt) + FR-3373

Playwright on dev, Documentation Flows, MCP Servers screen (prose recipe: `automations/content/platform/mcp-servers.md`):

1. Register `https://dev.flowrunner.ai/mcp`, name `MCP Probe – Self`, no auth fields. Expected from source: OAuth
   discovery succeeds → popup consent → DCR with `Config.integration.mcpClient.oauth.redirectURI` (defaults to `""`)
   → likely `redirect_uri does not match any URI registered for this client`, **or** the silent fallback in
   `create-mcp-modal/index.tsx:93-95` to plain registration → `401 Authentication required`. Record the exact
   user-visible message (Mark's 08-06 screenshot showed a failure; confirm current state).
2. If registration succeeds: Tools tab lists the 42 tools with the unique-hostname rule respected; attach one tool to
   an AI Agent; run — note the recursion hazard (the agent mutating the same account's Redis pointer).
3. **FR-3373 regression:** open Authentication Settings; check whether the browser autofills Custom Header Name /
   API key (fresh Chromium profile with a saved credential to provoke it); enter `mark@backendless.com` deliberately as
   the header name → save → connect. Expected on current dev: stored without validation, fails at connect with
   `Headers.append … invalid header name`. Post the result as a comment on FR-3373 (fix `ffbe190a16` is not on dev
   and only hardens `MaskedInput`; header-name validation is still absent client- and server-side).
4. Delete `MCP Probe – Self`.

## Phase 6 — Reporting and the replay harness

- **Run report** → comment on FR-3247: environment + drive date, workspace, tool-surface table summary, scenario
  results (S1–S16 with runnable/built-only), defects filed (keys), doc-drift list (`api-reference.md`, `readme`
  tool), explicit **NOT TESTED** list (raw protocol probes, prod, services without connections).
- **One subtask per confirmed defect** under FR-3247 (search Jira first; FR-3373 gets a comment, not a new ticket).
  Body: exact tool call JSON, exact response, expected vs actual, drive date, `dev.flowrunner.ai` / Documentation
  Flows, what was NOT tested. Only findings I drove myself go in; source-analysis-only claims are labeled as such.
- **Replay script** `automations/qa/mcp-flow-builder/tools/replay.mjs`: reads a run JSONL, connects with
  `Client` + `StreamableHTTPClientTransport` and a minimal `OAuthClientProvider` (localhost callback, token cached in
  `.cache/mcp-qa/token.json`), replays calls in order, **remaps ids** (`nodeId`, `versionId`, `flowId`, `caseId`,
  `toolId`, `decisionId`) from recorded → live by response position, and asserts normalized result shape +
  `issues` + `status` against the recording. Substitutes the Documentation Flows id from `env.json` and refuses to
  run if `list_workspaces` does not contain it. Reports a diff table. Used for the E9 second-client test and for
  re-running after FR-3365.
- Tracked copy of this plan + per-scenario result files in `automations/qa/mcp-flow-builder/`; raw logs,
  screenshots and exported JSON in `automations/.cache/mcp-qa/`.

## Safety rails

- Never call any tool with a `workspaceId` other than the Documentation Flows id; never `load_flow` a version whose
  `list_flows` entry is not an `MCP Probe – *` flow or TD Sandbox (`C24408A2-1FA3-43DF-BB94-D4DE39D3DE29`), except
  the deliberately Console-built E1/E14 fixture flows I create myself.
- `start_flow` only on probe flows; `stop_flow` + delete at scenario end; schedules disabled before delete; no probe
  left LIVE overnight.
- Real side effects (S10 message send, S11 AI spend) only on connections/keys that already exist, once each.
- Jira writes: fresh repro immediately before each; report what was not tested; FR-3373 comment not duplicate ticket.

## Verification of the plan itself

Phase 0 ends when: `flowrunner-dev` shows `✔ Connected` in `claude mcp list`, the hook has written at least one
JSONL line, `env.json` holds the Documentation Flows id + API key, and S1 passes all three oracles. If S1 cannot pass
(OAuth or backend blocker), stop and report that single blocker rather than continuing.

Full run is done when: all 42 tools appear in `tool-surface.md`, every S# has a result file with O1/O2/O3 evidence or
an explicit build-only reason, every E# has a verdict, the report comment is on FR-3247, subtasks exist for confirmed
defects, `replay.mjs` reproduces S1 from its recording, and `list_flows` shows no remaining `MCP Probe – *` flow.

## Estimated effort

Phase 0 + Phase 1: one session. Phase 2: two sessions (S1–S8 then S9–S16). Phases 3–4: one session. Phase 5: half a
session. Phase 6: half a session, interleaved (subtasks filed as defects are confirmed). Roughly five sessions.

## Open items only Mark can settle (not blocking Phase 0)

- Whether the OAuth **client registration** created by Claude Code on dev should be revoked after the run.
- Whether E1 (data loss on load→save), if confirmed, is Highest priority — it blocks "AI edits an existing flow".
- After release: repeat Phase 0 + S1/S2 against `https://app.flowrunner.ai/mcp` (prod consent routes were missing on
  2026-08-10 per Inna's comment).
