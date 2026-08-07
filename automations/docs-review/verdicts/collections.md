# Gate verdict — build/flow-control/collections.md ("Working Through a List")

**Date:** 2026-07-13
**doclint:** 0 errors, 0 warnings
**concept-page-review verdict:** `major-rework` (run wf_585380d2-506, on the correct page — script default hardcoded to this page to dodge the `args.page` default bug)

## Summary (gate)
"Strong spine — one continuous cart-scanning example, purpose-first sections, all five shots
confirmed against pixels — but one red-team BLOCKER (the page printed `5944.77` as the literal
stored value of Cart Total when the product stores the float `5944.7699999999995`), plus majors
(the loop-scope 'why' was prose-only/undriven; no PLATFORM-REVIEW-LEDGER section; a lone
`((Current Iteration Item))` chip inconsistent with five backticked mentions) and craft minors."

## Work list — every item CLEARED in one consolidated pass (2026-07-13)

- **[BLOCKER] float value.** The page printed `5944.77` twice as Cart Total's stored contents; the
  product stores `5944.7699999999995`. Fixed (option a): §3 now shows the true stored value and
  adds one plain sentence that summing decimals leaves a floating-point tail (round to `5944.77`
  for a customer-facing figure); the payoff prose no longer restates a rounded number as the
  contents. NEW-RULE candidate noted for the guidelines. ✔
- **[MAJOR] undriven loop-scope 'why'.** Drove it in-product on this flow: a post-loop block could
  NOT see the inner Condition's "Priciest so far? Result" while it COULD see all three Data Bucket
  variables (and no Current Iteration Item/Number outside the loop). Recorded as a dated note in
  the page's exploration log; scratch block deleted so the saved flow matches the run-proof. ✔
- **[MAJOR] missing ledger section.** Added "## Working Through a List" to PLATFORM-REVIEW-LEDGER.md
  mirroring the routing/repeating entries, each item evidenced. ✔
- **[MAJOR] chip/backtick inconsistency.** Changed `((Current Iteration Item))` → `Current Iteration
  Item` (backtick) to match the five other mentions and VOICE.md's named-system-value rule. Raised
  the house convention (chip vs backtick for Flow-Context pick values; repeating.md chips
  ((Current Iteration Number))) to Mark for a ruling. ✔
- **[MINOR] payoff shot alt (Input==Output).** Reworded the alt to frame it as Update Top setting
  the priciest product on the final pass, not a no-change frame. ✔
- **[MINOR] Break "sits behind a Condition" reads as required.** Softened to "You usually put a
  Break on a Condition's exit path...". ✔
- **[MINOR] three Break reasons in one sentence.** Broken into a bulleted list. ✔
- **[MINOR] two Repeat pointers.** Folded to one — the close carries the single which-tool route;
  dropped the "Repeating Steps shows one in action" link from the Break paragraph. ✔
- **[MINOR/NIT] §3 verbosity + one-term.** Compressed; use "Data Bucket variable" throughout
  (dropped "top-level variable"). ✔
- **[NIT] lede antecedent.** "handing each item to those steps in turn." ✔

## Post-fix state
doclint 0/0; plain-style clean; 5 shots present and pixel-checked; iteration-scoping driven on the
Cart Summary flow; ledger section added.

Per the standing "gate is a one-time net, not a loop" rule, the gate was NOT re-run to chase a
`ship` verdict. Handed to Mark with fixes documented; Mark decides ship. (A regression re-run is
available on request.)

## REWRITE 2 (Mark's 2nd review, 2026-07-13 — he stopped again)
Fixed each point: "Step into the loop" -> "Step into the List Iterator block"; the step-in no longer
chains Expand+Return into a round-trip that lands you where you started (Expand to enter; Return
separately, when done); **Current Iteration Item is now SHOWN** — a re-captured shot of it under
Flow Context in the Expression Editor, reaching a product's price (his "where is that magical thing?");
the accumulate shot re-captured as the Add To Total **config panel** with full context (the
over-cropped Live-Preview fragment dropped); informative titles ("Keep the best one so far" ->
"Find one item in the list"; "Build up a result as you go" -> "Total the items in a variable";
"Reach into the current item" -> "Read the current item"). doclint 0/0.

## CONCEPT-FIRST REWRITE (Mark review, 2026-07-13)
Mark stopped his review — the first draft was a quality step-back: it dove into the cart example
too soon, over-anchored to "product," used mechanical titles ("Read each item with Current
Iteration Item"), and kept impractical detail (the As JSON toggle). Redone concept-first (text
only — flow, shots, and run-proof unchanged and still valid):
- Lede opens on the general reality: collections come from anywhere - a database query, an uploaded
  file, an AI step, an HTTP Request, or built internally - and a List Iterator does the same work
  for every entry.
- §1 teaches the ((List)) as any array from any source, THEN establishes the running example
  clearly ("one flow runs alongside it" - a flow that fetched a cart). As JSON cut.
- Concept stated in general terms (entry / element / item); the cart's "product" appears only as
  the example's instance, not as the concept's vocabulary.
- Teaching-oriented titles: Point the loop at an array / Reach into the current item / Build up a
  result as you go / Keep the best one so far / Stop before you reach the end.
doclint 0/0; plain-style clean; 89 lines. Handed back to Mark for re-review.

## REWRITE 4 (Mark's 5-point round, 2026-07-14)
Applied each point on top of Mark's own in-file edits (he had inserted a `listiterator-expand.png`
reference at §2 and condensed a sentence): (1) added the raw cart JSON block before the §1 image
(re-fetched from the live API to author it); (2) cut the "most walks handle each element on its own
and are finished there" filler; (3) fixed the §2 Current Iteration Item sentence — "To work on an
element... handed to them fresh" -> "To access the current element... you pick it" (de-folksy);
(4) rewrote the §3 opener to teach iteration-reset scoping accurately (each pass = clean slate; a
step's value does not survive to the next pass; only a Data Bucket variable carries across passes and
out) — replacing the confusing "a loop cannot hand a value back... gone the moment the loop moves on";
(5) generalized "A running total is the plainest version" to the seed->update->read pattern, with
total/list/count/find named as instances so a reader who needs none of them still gets the shape.
Also captured `listiterator-expand.png` (Scan Products hovered, Expand tooltip+icon) to resolve Mark's
new image reference; fixed the §1 JSON to show the API's exact Slipper total `99.94999999999999` (not a
rounded `99.95`), consistent with the no-false-stored-value rule. doclint 0/0. Open Q raised to Mark:
is calling a List Iterator a "loop" acceptable (the page uses it throughout, as did Mark's edits)?

## Convention — SETTLED (Mark, 2026-07-13)
Mark ruled: **chip the "pills" that come from the Expression Editor.** So Current Iteration Item /
Current Iteration Number are chipped (`((Current Iteration Item))`), not backticked — this page was
updated to chips (overriding the gate's backtick finding), and it now matches repeating.md's
`((Current Iteration Number))`. Open follow-ups: whether Data Bucket variables (currently bold) are
also chipped, and updating VOICE.md's named-system-value line so the gate stops flagging chips.
