# S12 — Parallel fan-out, Synchronize, Wait

Driven 2026-09-02 03:11–03:14 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Run two HTTP GETs in parallel, wait for both, then wait 2 s and return 'done'."

## Build (16 calls)
data-transformer "Kick Off" (first block) → fan-out via two wire_edge calls to http-request "Fetch A"/"Fetch B" (httpbin /get?branch=a|b)
→ both → synchronize "Wait for Both" (maxWaitingTime 30) → wait "Pause 2s" (delay 2) → return-result {status, a `{{Response A->args.branch}}`,
b `{{Response B->args.branch}}`}. Flow 6F0D1003-AB97-4AA1-8A9F-726F04AA1761, version 3B910D76-9277-4EF6-99E6-6BD8D48BA1A6.
actions-group was not used (a plain fan-out is what an agent reaches for first); its schema was read (transitionMode ON_START/ON_COMPLETION).

## Oracles
- **save_flow #1 → INVALID:** `The value for maximum waiting time should be a number greater than 0…` — `{text:"30"}` became a String.
  Re-configured both timing fields with `type: "NUMBER"` → READY.
- **O1:** Kick Off.nextElementIds = [Fetch B, Fetch A]; both → Synchronize → Wait → Done; maxWaitingTime/delay tokens `{id:"NUMBER", value:30|2}`;
  LIVE. PASS.
- **O2:** S12-o2-canvas.png.
- **O3:** `{"a":"a","b":"b","status":"done"}` HTTP 200 in 3.85 s wall clock (≈ parallel fetch + 2 s wait). PASS.

## Findings
1. F-S12-1 numeric expression fields (synchronize.maxWaitingTime, wait.delay) accept a text literal silently; only the server rejects.
   The block descriptions say "in seconds" but not "must be a number"; inputSchema shows resultType null. Candidate improvement.

## Teardown
stop_flow(3B910D76…). Flow kept for end-of-phase deletion.
