# Gate verdict — run/monitoring.md

> **RESOLVED by Mark, 2026-08-15** — his three calls landed and were executed the same day:
> **(1) Page split** — the single-run drill-down (Opening a run / loop stepping / Retry attempts /
> Finding the step that failed) moved to the new `run/inspecting-a-run.md` ("Inspecting a Single
> Run", its own nav entry); this page keeps the health views and routes the fourth question.
> **(2) Shorten IDs is a BUG** — Mark files it in Jira himself; the docs stay silent on the
> control until the fix lands. **(3) Demo-data fix approved and executed** — Order Poller now
> fetches a real order-shaped stub and Update Order Status reads `Re-fetch Order Result->status`;
> relaunched with an Initial Data payload (`?orderId=1042`, run 41D56D7B) and both affected shots
> recaptured. Post-split both pages lint 0/0 (an intro tab-row shot was added to satisfy the
> chips-without-shot hard gate). The `revise` below stands as the record of what was Mark-gated.

- **Date:** 2026-08-14
- **Gate verdict:** `revise` (concept-page-review, final run wf_85d4ff7f — fourth gate round
  this session; every item not requiring Mark's input was cleared, see below)
- **doclint:** 0 errors / 0 warnings (page-level)
- **Trigger:** release 1.0.13 (FR-2958) added per-attempt retry detail to the run-history view;
  documenting it pulled the whole page through the gate, which then audited the July content.

## What was added and verified this session (all in-product, Documentation Flows)

- **NEW "Checking a block's retry attempts" section** — the ((Retry attempts)) tab in Element
  Execution Details, verified on a real LIVE errored run ("Retry Demo" E6775B29: 503 endpoint,
  5XX policy, max 3, fixed 2s): one card per failed attempt that triggered a retry (3 attempts →
  2 cards; final outcome stays on ((Data))), each card carrying attempt #, status badge,
  timestamp, response body, and the wait before the next try. Scoped to HTTP Request (FR-2958 v1).
- **"Finding the step that failed"** — finally verified live (the July page described errors
  without ever seeing one): TERMINATED row + filled Has Error column + Only With Errors filter
  (new shot), populated Problematic Instances with click-to-open verified (new shot), and the
  failing block's warning-triangle canvas marker vs the ticks (reframed shot).
- **All ten July-era claims re-driven** after Order Poller's runs aged out of retention
  (5 fresh LIVE activations launched): Dashboard recaptured with the tab row + shared date
  window + populated cards/heatmap/day-list/source chart; lower panels (Block Transitions %,
  Problematic Instances empty state) captured; Performance recaptured sorted descending with
  the loop-container nesting taught; Logs re-driven control by control (Filter matches the
  message segment and highlights; Log Source scopes to one run and reveals Show logging for;
  CLEAR LOG AREA verified; Basic timestamps verified; the false "filter to a single run or to
  errors" and "drop the ids" claims removed); loop drill-down re-driven (hover-revealed expand
  icon captured in-shot, RETURN verified, not-executed marker on the untaken branch taught).
- Structure: lede scoped to "four of the tabs" with the other three routed; three h3
  subsections; plan caveats footnoted; 11 shots, all read back.

## Remaining items — Mark's decisions (the gate cannot pass without them)

1. **Page split** — the page runs ~110 lines / 11 shots vs the 50-75 / 3-6 exemplar. Split
   "Reading a single run" (+ loop/retry/error subsections) into its own page, or record the
   one-surface framing as a deliberate exception?
2. **Shorten IDs** — the toggle is visible in the Logs shots but toggling produced no visible
   change (full UUIDs both ways). Expected behavior to document, or a bug to file in Jira?
   (Prose currently names only the verified controls.)
3. **Demo data fidelity** — Order Poller's Re-fetch Order hits jsonplaceholder, so the loop
   shot's Input/Output show a demo TODO, not order data; and the instance-detail shot's Initial
   Data is Empty Object. Fixing both means changing the flow Mark built (an order-shaped stub
   endpoint) and relaunching with a payload — his call.
4. **Retry-then-success rendering** — only the all-attempts-fail case was driven; a 503-then-200
   run needs a stateful endpoint. Drive later or accept the scoping.
5. Micro-drives left open: Active Instances above 0, Now tailing, Wrap messages, Iteration #
   stepping beyond pass 1, handled-error row presentation, Logs-tab retention horizon
   (footnote now scoped to the three verified views).

## Gate history this session

major-rework (wf_8e6f8d63) → revise (wf_97f116e3) → revise (wf_e3ecbfe9) → **revise
(wf_85d4ff7f, remaining items Mark-gated)**. Item-by-item dispositions are in
PLATFORM-REVIEW-LEDGER.md (Run & Monitor → Monitoring & Analytics, entries dated 2026-08-14).
