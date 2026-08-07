# Gate verdict — build/flow-control/waiting.md ("Adding a Delay")

**Date:** 2026-07-15
**doclint:** 0 errors, 0 warnings
**concept-page-review verdict:** `major-rework` (run wf_63c33030-228; page hardcoded into the gate
script per the documented `args.page` workaround)

## Summary (gate)
"Strong spine - plain house style, value-first lede, meaningful anchors, two of three shots verified
clean, every runtime behavior backed by a dated in-product note. Not ready: (1) the Expression-Mode
shot showed a bare literal `3`, the opposite of the section's data-driven lesson; (2) its alt
overclaimed 'holding an expression'; (3) no ledger section / verdict on disk; plus a major - the
'covered in Handling Errors' cross-reference pointed to a page with no backoff coverage."

## Work list — cleared in one consolidated pass (2026-07-15)
- **[BLOCKER] Expression-Mode shot = literal `3`.** Built "Dynamic Wait Demo": Set Config sets a
  `Wait Seconds` variable (300), and the Wait's ((Seconds)) reads it. Bound the reference live in the
  Expression Editor (typed the Data Bucket token - click-insert of a pill does not register in
  automation; the Live Preview rendered the resolved pill). Recaptured wait-expression-mode.png so the
  Seconds field now shows the bound reference pill "Default - Wait Seconds", not a constant. ✔
- **[BLOCKER] alt overclaimed "holding an expression".** Rewritten to match the pixels: "its Seconds
  field holds a reference pill, Default - Wait Seconds, that reads the wait length from the flow's own
  variable." §3 prose reworked to the real scenario (an earlier step sets Wait Seconds; the Wait reads it). ✔
- **[BLOCKER] no ledger section / verdict.** Added the "Adding a Delay" ledger section (SHOW-it,
  run-proofs, fixes) and this verdict file. ✔
- **[MAJOR] "covered in Handling Errors" points to absent content.** error-handling.md is currently a
  stub (no wait/backoff/retry). Softened to a topical pointer: "Retrying a failed step is part of
  [Handling Errors]." Fully resolves when error-handling.md is written with the backoff-retry pattern
  (Mark's call: it lives fully there). Tracked in the ledger. ✔ (soften) / pending target coverage.
- **[MINOR] long-wait instance cost.** Added: "A waiting run is still an active instance ... a long
  wait keeps that run open for the whole time." (Verified: the instance did not COMPLETE until the
  Wait ended.) The exact slot/plan-cap accounting is not driven (wait.yaml has no cap fact) - parked
  as a candidate guideline. ✔ (note added)
- **[MINOR] wait-branch.png doesn't show the 5s duration.** Author's-call, low stakes - left as is:
  the shot's job is the branch-scoping topology (Wait on one branch), and the 5s is prose + log-backed. ✔ (declined, justified)
- **[MINOR] Utils palette location** - confirmed in-product (Wait is under the Utils palette group). ✔
- **[NIT] §1 opener led with the mechanic.** Now leads with purpose: "To hold a step for a set
  stretch, reach for a Wait ...". ✔

## Post-fix state
doclint 0/0; plain-style clean; 3 shots present and pixel-checked (Expression-Mode shot now shows a
real bound reference); two run-proven flows in the workspace (Paced Calls 4077259E, Delay One Path
3FECA0F9). Per the "gate is a one-time net, not a loop" rule, the gate was NOT re-run to chase a
`ship` verdict. Handed to Mark with fixes documented; Mark decides ship.

## Parked follow-ups
- error-handling.md must cover the Wait-on-retry backoff so the Page-A pointer resolves fully.
- Candidate guideline (red-team): a page inviting long waits must state parked-instance slot/cap.
- Cleanup: throwaway flows (incl. Dynamic Wait Demo, Paced Calls, Delay One Path once shots are final).
