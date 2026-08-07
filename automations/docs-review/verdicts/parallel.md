# Gate verdict — build/flow-control/parallel.md ("Running Steps in Parallel")

**Date:** 2026-07-14
**doclint:** 0 errors, 0 warnings
**concept-page-review verdict:** `major-rework` (run wf_616a3752-713, on the correct page — the
`args.page` default bug fired on the first run wf_5cb0d24f-bfd, which reviewed shared-memory; the
script default was hardcoded to this page and re-run per the documented workaround)

## Summary (gate)
"Strong, well-verified page: one continuous signup-enrichment example, all six screenshots pixel-match
their prose (including the non-default On Completion state and the green-pill/red-error A/B), every
high-risk runtime claim substantiated by the live-driven exploration log or a dated V-real note. Did
not ship as-is: one blocker (no ledger section) and two majors (the fan-out gesture was never taught;
the On Start pitfall overstated the product)."

## Work list — every item CLEARED in one consolidated pass (2026-07-14)

- **[BLOCKER] no PLATFORM-REVIEW-LEDGER section.** Added "## Running Steps in Parallel" mirroring the
  collections/repeating entries — SHOW-it (6 pixel-checked shots), VERIFIED/RUN-PROVEN (instances
  5FD4EC77, D8C21967; On Start red-pill; Race Test), doclint, and the timeout V-real flag. ✔
- **[MAJOR] fan-out gesture not taught.** Verified in-product (connections originate from a block's
  right-edge output handle; one block fans to many, visible zoomed). Added a plain sentence in §1:
  "You fan out by drawing more than one connection from a block's output - the dot on its right edge -
  one to each branch." Candidate NEW guideline (first page relying on an untaught canvas gesture must
  teach it) — parked for /docs-feedback, to raise with Mark. ✔
- **[MAJOR] On Start pitfall overstated/self-contradictory.** "will not even let you reference it"
  contradicted the observed behavior (the editor authors the reference, then flags it red). Reworded:
  "The editor flags a reference to it as invalid - it shows 'Referenced block is not accessible from
  this block' - and the flow will not run until you remove it." ✔
- **[MINOR] §2 title carried two takeaways.** Retitled "Bundle parallel actions in an Actions Group,
  and set when the flow continues" → "Bundle parallel actions in an Actions Group"; the transition
  mode lives under it as the when-does-the-flow-move-on consequence. ✔
- **[MINOR] §4 named the Expression Editor; shot shows the field's bound pill.** Reworded to match the
  pixels: "Each reference is built in the Expression Editor and sits in the field as a bound pill." ✔
- **[MINOR] lede closed on a meta/syllabus clause.** Dropped "and this page shows how to set that up…";
  ends on value ("holds the flow for that work when a later step needs it done"). ✔
- **[MINOR] §1 opener led with wiring.** Now leads with purpose ("Independent steps do not have to take
  turns."), mechanism after. ✔
- **[MINOR] block "New Signup" (a Set Variables) read as a trigger/event.** Renamed to "Set User Id" in
  both flows; recaptured parallel-fanout + parallel-actionsgroup-mode. ✔
- **[MINOR/verify] Synchronize "releases a single path" over-claimed a one-exit limit.** Reworded to the
  proven fact (releases ONCE after all branches arrive; downstream runs a single time). ✔
- **[MINOR] Expression Mode toggle visible in the Synchronize shot, unmentioned.** Added: Max Waiting
  Time is set in days/hours/minutes/seconds, or as seconds via ((Expression Mode)). ✔
- **[MINOR] closing paragraph restated the decision with a symmetric contrast.** Trimmed to the routing
  value + the two reference links. ✔
- **[MINOR/verify] timeout-drop is the one claim not reproduced this session.** Carried into the ledger
  as a flagged verify-for-Mark item; page documents it from synchronize.yaml V-real (2026-06-14). ✔
- **[NIT] "roughly 1, 2, and 4 seconds"** — delays are exact by construction; tightened to "the three
  calls take 1, 2, and 4 seconds" (kept "about" only on the observed total). ✔
- **[NIT] §4 redundant closing sentence.** Merged the two "no combined result" sentences into one. ✔

## Post-fix state
doclint 0/0; plain-style clean; 6 shots present and pixel-checked; ledger section added; two run-proven
flows in the workspace (Parallel Enrichment 280C5482, Enrichment Group 1B52CCED).

Per the standing "gate is a one-time net, not a loop" rule, the gate was NOT re-run to chase a `ship`
verdict. Handed to Mark with fixes documented; Mark decides ship. (A regression re-run is available on
request.)

## Mark review round (2026-07-14) — 7 corrections, all applied + re-verified in-product
- **"waits" misleading for parallel branches** (lede): branches don't wait, they run. Reworded to elapsed
  time - "Run one after another, the three calls take as long as all three combined. Run at the same
  time, they take only as long as the slowest."
- **connection gesture wrong** ("the dot on its right edge"): connections are made with a LINK ICON on
  each block, not a dot. VERIFIED in-product (the purple chain-link icon at a block's corner on hover).
  Reworded: "every block has a link icon you drag to the next step."
- **"takes as long as the slowest" only holds because of Synchronize**: §1 now attributes the
  flow-carries-on-after-the-slowest to the Synchronize block (shown in the shot), covered below.
- **§2 rushed to the mode**: now takes the reader to the group's settings panel first ("Select the group
  ... to open its settings"), then Outgoing Transition Mode.
- **mode icon on the outgoing line**: VERIFIED - the group's outgoing connection carries an HOURGLASS
  icon whose fill reflects the mode (On Completion bottom-filled, On Start top-filled). Now called out
  in prose + the mode shot recaptured to show it clearly.
- **without Synchronize, Build Summary runs 3×**: VERIFIED with a clean test ("Join Test" - a static
  downstream step ran 3× / execution-count badge = 3). Added as an admonition. (In the enrichment flow
  where the downstream reads results, the early runs fire before the other branches finish and the run
  TERMINATES with an error - "No Sync Test" instance; the clean 3× shows with a non-reading step.)
- **Expression Mode is about a DYNAMIC wait** (from flow data), not merely "seconds": reworded to
  "compute the cap from flow data at run time (as a number of seconds), so a flow can wait longer or
  shorter depending on what it is handling."
doclint 0/0; plain-style clean. Two more throwaway flows created for these verifications (No Sync Test,
Join Test) - added to the cleanup list.

## Parked follow-ups
- Reference: actions-group.yaml should document that under On Start the group's inner results are NOT
  accessible downstream; synchronize.yaml Expression Mode note if missing.
- Candidate guideline: teach any canvas gesture the first page to rely on it (fan-out).
- Cleanup: throwaway verification flows (AG Probe, Race Test, Timeout Test) to delete after Mark's review.
