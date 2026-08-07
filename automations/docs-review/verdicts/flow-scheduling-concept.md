# Verdict — flow-scheduling-concept (content/reference/flow-scheduling-concept.md)

Gate: concept-page-review. Latest run 2026-07-09 → **major-rework**.

History: 2026-07-08 handed to Mark WITHOUT a gate run (process failure). First real gate runs 2026-07-09.
Round 1 (major-rework): "Play"→START FLOW, Pause/Stop-vs-block scope, Frequency 1-of-6, tautology, no ledger, doclint warns. FIXED.
Round 2 (major-rework): greyed 2nd-checkbox enablement, lede "runs" verb, "few minutes"↔30s framing, "toggles"→checkboxes, non-default policy shot, Weekly/Monthly verified. FIXED.
Round 3 (major-rework) — OPEN:
- BLOCKER: "Every X seconds"=30 may violate the 60s floor (scheduledflows.md L45). 30 was read off a stored flow, not confirmed accepted as fresh input. → verify in popup; if rejected, move example to a valid interval + recapture.
- MAJOR: 2nd policy checkbox ON state shown in no pixel (flow-scheduling-policy.png cropped it away). → recapture with Expire set + 2nd checkbox ticked, crop wider.
- MAJOR: post-expiry Call Flow API behavior (2nd option) prose-only → live test.
- MAJOR: split How-it-works (3 ideas) into takeaway-titled sections.
- MINOR: run-overlap behavior; trigger fate after expiry.
doclint: 0 errors / 0 warnings.

---
Round 4 — post-fix consolidated pass (2026-07-09, one-time-net gate run wf_36fd8ca0-041 → **major-rework**; findings triaged, fixes applied, NOT re-run per STANDING-RULES "gate is a one-time net"):
- BLOCKER (30s floor): RESOLVED earlier — verified live the "Every X seconds"=30 is accepted (SAVE stayed enabled; legacy 60s floor is stale). Note on page.
- MAJOR (2nd-checkbox pixel): RESOLVED — flow-scheduling-policy.png RECAPTURED with Expire set to a date and BOTH Flow Execution Policy checkboxes ticked + enabled (live dialog, taller viewport, PIL crop). Alt updated.
- MAJOR (post-expiry API): RESOLVED — verification note quotes the 2nd option's own product help tooltip verbatim ("When this option is enabled and the flow's schedule has expired, a new flow instance can be created by using the 'Call Flow' API.").
- MAJOR (both-on contradiction, NEW red-team class): RESOLVED — because the recaptured shot now shows BOTH checkboxes ticked, added a timeline paragraph reconciling them (checkbox 1 gates the API while the schedule is live; checkbox 2 re-opens it only after Expire; both-on = refused during life, accepted after expiry). Candidate new guideline rule captured below.
- MAJOR (clone inherits schedule): RESOLVED — dated verification note added citing the product-owner 2026-07-08 correction (clone DOES inherit; opens with same Frequency/Start/Expire). This corrects a previously-wrong claim.
- MAJOR (new-version takeover): RESOLVED by rewording — the takeover is now DERIVED from the already-verified LIVE-gating rule (a schedule produces runs only while its version is LIVE) + one-LIVE-version-at-a-time, not asserted as a separate untested behavior.
- MAJOR (split How-it-works): JUDGMENT CALL — kept the 3-paragraph How-it-works as one continuous mental model (what a schedule is → when it produces runs → how it travels with versions). The generator renders custom sections only AFTER "When to use it," so splitting would scatter the mental model. Flagged to Mark for his call.
- MINOR (tautology openers): trimmed in the version-travel paragraph.
FLAGGED TO MARK (genuinely open, not silently closed):
- Start/Stop Scheduled Runs keeping the version LIVE while triggers/Call Flow API still fire is schema- + demo-verified (metaInfo.schedule.enabled independent of LIVE state) but NOT driven end-to-end by a live A/B (schedule-off + trigger-still-fires). Honestly labelled as such.
CANDIDATE NEW GUIDELINE RULE: when two controls in the same panel can be enabled together AND a screenshot shows them both on, the prose must state what the COMBINATION does, not just each in isolation.
doclint: 0 errors / 0 warnings.
