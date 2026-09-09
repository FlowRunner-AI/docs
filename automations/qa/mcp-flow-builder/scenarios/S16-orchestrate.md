# S16 — Orchestrate (Assign Instance Name, Call Flow → S1, Stop/Start Scheduled Runs → S9)

Driven 2026-09-02 03:16–03:19 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Name the instance after the caller's orderId, sum the caller's numbers by calling the Sum Numbers flow, pause and resume the Daily Ping
schedule, return orderId and sum."

## Build (14 calls)
execution-name "Name Instance" (`order-{{Initial Data->orderId}}`) → call-flow "Sum via S1" (flowId of S1, initialData numbers, syncCall) →
stop-scheduled-runs (flowId S9) → start-scheduled-runs (flowId S9) → return-result {orderId, sum `{{Sum Flow Result->sum}}`}.
Flow 5488401A-E62C-460B-AB71-682417B14ABB, version 1217759C-DC56-48A9-BD07-D8470569A8F7.
Negative probe: configure_block(call-flow, {flowId, flowName}) → BAD_REQUEST with a precise remedy; node unchanged. PASS.

## Oracles
- **O1:** executionName is a 2-token expression (TEXT + INITIAL_DATA); call-flow initialData serialized as `{numbers: Expression}`; both
  scheduled-runs blocks carry flowId S9; LIVE. PASS.
- **O2:** S16-o2-canvas.png; Instances tab lists two instances named `order-A-7` (TERMINATED, then COMPLETED 720 ms). PASS.
- **O3 run 1:** TERMINATED 28105 at "Pause S9 Schedule": "There is no flow with the 'Live' status for ID '5A0025CD…'" (S9 was READY).
  After start_flow(S9): `{"orderId":"A-7","sum":6.0}` HTTP 200. PASS (call-flow into a LIVE S1 works, result referenced as `->sum`).
- get_flow_schedule(S9) after the run: `enabled: false`. Whether start-scheduled-runs re-enabled the schedule is UNVERIFIED (the flag may not be
  what the block toggles; startDate was in the past). Not claimed as a defect.

## Findings
1. F-S16-1 Neither scheduled-runs block description (nor our reference pages) says the target flow must be LIVE; the engine fails the run with
   28105 otherwise. Tool-doc gap + docs follow-up.
2. F-S16-3 start_flow on a PAUSED version resumes it (S1, S9). The only missing lifecycle tool is "deactivate to READY" (F-S4-5).

## Teardown
stop_flow on S16, S1, S9 (all PAUSED). Flows kept for end-of-phase deletion.
