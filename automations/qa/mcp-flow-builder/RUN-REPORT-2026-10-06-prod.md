# FR-3247 MCP Flow Builder: retest on PROD, 2026-10-06

Server: app.flowrunner.ai/mcp, "FlowRunner MCP Flow Builder" 0.2.0, 29 tools (the same redesign tested on dev 09-29).
Client: `tools/mcpc.mjs`, run with `MCP_QA_CACHE=.cache/mcp-qa-prod MCP_URL=https://app.flowrunner.ai/mcp`. A new
OAuth client was registered and approved on the prod consent page; the page does not ask for a workspace, so the
token can reach every workspace on the account, and the harness guard pins it to Documentation Flows
(86989ED5-…). Log: `.cache/mcp-qa-prod/sdk-run-2026-10-06.jsonl`. Real runs went through the blocking Call Flow API,
called from inside the signed-in Settings > General page (the key never leaves the browser).

## Results
- Stability: 0 session-lost retries; probe 30/30 ok; build calls 0.15-1.3 s. FR-3687 and FR-3689 fixed on prod.
- FR-3688 fixed: Cart Total (List Iterator) READY on the first save, started.
- FR-3490 fixed: the readme has no stale text ("known gap", load_flow, list_connections({}) are all gone).
- Custom extension action (TMDB getMovieDetails) via MCP: READY, started, ran -> {"title":"Dune: Part Two"}.
- Real runs: Sum Numbers GET 100.0 / POST 6.5; Ticket Router 4/4; Order Size big/small; Cart Total ints 22;
  Visit Counter 1,2,3; Sum Caller 6.0; Status Check 200 ok.
- Guards: self-loop and cycle rejected; start INVALID rejected; edit LIVE rejected; stop -> edit ok;
  test_run_block ok; disabled daily schedule set and read back.
- The editor opens an MCP-built flow (Cart Total) and its Settings panel loads (no FR-3596-style crash).

## Still failing
- FR-3690: Cart Total with decimal prices -> TERMINATED, 28077, "EL1031E: Problem locating method sum(Integer,Double)".
- FR-3494: Status Check 404/500 -> the handler result has code null and message "".

## Left on prod (Documentation Flows)
LIVE: MCP Prod - Sum Numbers, Ticket Router, Cart Total, Status Check, Order Size, Visit Counter, Sum Caller,
Movie Lookup. Stopped: MCP Prod - Edge Cases (with a disabled daily schedule). Shared memory key from Visit Counter.

## Not tested
The Claude Code / Claude Desktop connector path (needs a new session with the prod server registered), AI Agent /
AI Router / Knowledge Base runs, realtime triggers, and other workspaces.
