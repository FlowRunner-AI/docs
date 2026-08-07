# Gate verdict — build/flow-control/repeating.md ("Repeating Steps")

**Date:** 2026-07-11
**doclint:** 0 errors, 0 warnings
**concept-page-review verdict:** `revise` (run wf_8088cd7d-91c, on the CORRECT page)

> NOTE: the FIRST gate run (wf_c53e678d-62e) misfired to the *shared-memory* concept page
> (the `args.page` default bug — args did not reach the script, so it fell back to
> `'shared-memory'`). That verdict was about a different page and was DISCARDED, not recorded.
> The script default was hardcoded to this page and the gate re-run; the verdict below is the
> real one for repeating.md.

## Summary (gate)
"Well-taught, one coherent running example (Poll Until Shipped), screenshots match the pixels —
but does not ship as-is: (1) a §0g breach (one section mixed a feature's INPUT and OUTPUT under
a two-idea heading); (2) two red-team coherence defects (Wait-first vs 'between checks'; 'three
steps' vs a five-block body shot with an unexplained Cancelled?/Break); (3) DoD gaps (a floating
failsafe crop; missing ledger section). One high-risk claim (inner Break leaves the outer loop
running) was author inference with no driven run."

## Work list — every item CLEARED in one consolidated pass (2026-07-11)

- **[BLOCKER] guideline — mixed INPUT/OUTPUT section.** Split "What the steps inside can reach,
  and how to pass a value out" into two single-takeaway sections: **What a step inside the loop
  can read** (scope-in) and **Pass a result out with a top-level variable** (scope-out + the
  escape hatch, named explicitly). ✔
- **[MAJOR] educator — Wait-first vs "between checks".** Reworded §2: dropped "pauses between
  checks"; now "a Wait pauses so the service has time to make progress" + "runs three steps each
  pass", matching the shot's Wait -> Re-fetch -> Update order. ✔
- **[MAJOR] educator — "three steps" vs five-block shot.** Added a signpost clause: "The
  `Cancelled?` check and `Break` further down the shot are an early exit, built in the next
  section." ✔
- **[MAJOR] verify-in-product — inner Break leaves the outer loop running (unbacked).** Softened
  to the verified facts only (a Break ends the loop it sits in; FlowRunner allows nesting a Repeat
  in a Repeat) and deferred the nested-Break specifics to the [Break] reference (V-real in
  break.yaml). Exploration log records that the nested-Break run was NOT driven and why. ✔
- **[MAJOR] definition-of-done — missing ledger section.** Added a "## Repeating Steps" section to
  PLATFORM-REVIEW-LEDGER.md mirroring the routing/branching format. ✔
- **[MAJOR] definition-of-done — floating failsafe crop.** Replaced the bare sub-crop with a shot
  that earns its place and shows block identity: the Maximum Iteration Count field on the Repeat
  block with its help tooltip open ("interrupt the Repeat While loop... preventing endless loops").
  Recorded in the exploration log. ✔
- **[MINOR] educator — §5 read-claim / output spine.** Tightened on split: read section states
  only the verified read (top-level variable + a prior block's result); output section leads with
  the non-obvious survival rule. ✔
- **[MINOR] educator — Break "divide the work" + No-path gap.** Dropped the summary clause; added
  the No-path half-sentence (pass ends, loop re-checks at the top, a not-cancelled order keeps
  polling). ✔
- **[MINOR] educator — closing restates the lede's route.** Routed to Working Through a List once
  (in the lede); trimmed the close to end on Repeat's unique quality ("a 'keep going until'"). ✔
- **[MINOR] educator — §5 run-on / restated rule.** Ended the output section on the concrete
  result ("now holding shipped"); cut the restated-rule sentence. ✔
- **[MINOR] guideline — bold the group label.** "under **Flow Context**" now bolded. ✔
- **[MINOR] verify-in-product — List Iterator also exposes Current Iteration Number.** Not driven;
  removed the "(and inside a List Iterator)" parenthetical rather than assert an unverified claim
  (List Iterator may expose a Current Iteration Item, not the same pill). §6 is now Repeat-only. ✔
- **[MINOR] verify-in-product — "Current Iteration" field vs the pill.** Deliberate omission
  recorded in the exploration log; both shots put the field on screen. Accepted. ✔

## Post-fix state
doclint 0/0; plain-style greps clean; 91 lines; 5 shots present and pixel-checked; all links/images
resolve; ledger section added.

Per the standing "gate is a one-time net, not a loop" rule, the gate was NOT re-run to chase a
`ship` verdict. Handed to Mark with the fixes documented; Mark decides ship. (A single regression
re-run is available on request.)

## Mark review round — 2026-07-13 (7 corrections, all applied)
1. Loop-exit precision: condition evaluated BEFORE each iteration; false → that pass never runs, Repeat is done. Reworded §1.
2. "the status" → **Order Status**; ADDED an admonition that the checked value can change from anywhere in the instance (e.g. a parallel branch), not only inside Repeat.
3. Made explicit that the Cancelled? Condition's No path is unconnected, and an unconnected branch ends the pass there (then the loop re-checks).
4. §5 title → "Accessing flow data inside the loop".
5. "set outside the loop" → "declared outside the loop".
6. §6 title → "Returning data from the loop".
7. Corrected an inaccuracy: block results are ITERATION-scoped (a later pass can't see an earlier pass's result); only variables carry pass-to-pass and out. Reworded §6. → parked reference follow-up for repeat.yaml / list-iterator.yaml; distilled into the variable-scope-elevation memory.

doclint 0/0 after all corrections; plain-style clean; 97 lines. Re-handed to Mark.
