# S13 — Shared Memory (remember the last caller across runs)

Driven 2026-09-02 03:14–03:16 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Remember the last caller's name across runs and return the previous one."

## Build (8 calls)
shared-memory-read "Read Previous" (key lastCaller, defaultValue "nobody", alias Previous Caller) → shared-memory-put "Remember Caller"
(data [{lastCaller: `{{Initial Data->name}}`}], override true) → return-result {previous `{{Previous Caller->}}`, current}.
Flow 0A03B693-BB7C-4639-97A3-248B66E63D2F, version 6F74399D-0952-4BDC-88D5-BA5523F197B0. All config passed in add_block; only the return
data waited for wiring.

## Oracles
- **O1:** shared-memory-put `data[].name` is a plain string and `value` an Expression, exactly as get_block_schema's `items` said (the readme
  calls this out as non-guessable — confirmed the schema tells the truth). Flow-level `metaInfo.sharedMemory` = FLOW_MEMORY anchor, no
  expiration (defaults; the MCP exposes no tool for Flow Memory settings). LIVE. PASS.
- **O2:** S13-o2-canvas.png.
- **O3:** Alice → `{"current":"Alice","previous":"nobody"}`; Bob → previous Alice; Carol → previous Bob. PASS.

## Findings
- Gap: no MCP tool sets the flow's Shared Memory settings (anchor type, missing-anchor policy, expiration) — the Console's Settings tab has
  them. Defaults were fine here; an agent asked for "per-customer memory" (INITIAL_DATA anchor) has no path.

## Teardown
stop_flow(6F74399D…). Flow kept for end-of-phase deletion. Shared-memory key `lastCaller` = "Carol" remains in the workspace's flow memory.
