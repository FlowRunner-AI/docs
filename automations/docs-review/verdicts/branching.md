# Verdict — build/flow-control/branching.md

- **Date:** 2026-07-10
- **Verdict:** `major-rework` — SUPERSEDED 2026-08-06. Re-checked against the current page: all three blockers are resolved. 'No on the left' no longer appears; the bracket shot's alt matches its pixels; STRING/CONTAINS is verified at line 69; the default grouping is recorded. The OR-reset blocker was superseded by Mark's ruling (it is a product bug he is fixing, so the claim was pulled from the page and the log). The DoD finding that 'docs-review/verdicts/ has no branching verdict file' is self-refuting — this file is it.
- **doclint:** 0 errors, 0 warnings (`python3 -m tools.doclint content/build/flow-control/branching.md --warnings`)
- **Note:** first gate run (wf_14a407d6) misfired on the script default and reviewed `shared-memory`; discarded. This verdict (wf_a02fe174) is the real branching.md review.

## Summary

Not ready. The spine is excellent — one continuous order-approval example, strong titles, six of seven screenshots match their prose, and the trigger's-own-data distinction is handled correctly — but three gating defects block ship. TWO are outright false-to-product claims a builder will trip on within a minute (the parentheses section shows the OR surviving when the author's own log twice-verified that adding a part RESETS every connector to AND; and the prose says "No on the left" while both canvas shots show No exiting the bottom), plus a decontextualized bracket screenshot whose alt over-claims an editor not in frame. The theme of what remains: reconcile prose to the author's own verified log/pixels, recapture the bracket shot, state the default ungrouped grouping, verify the STRING/CONTAINS label, and open a ledger section + write a fresh ship verdict (none exists on disk). NEW-RULE CANDIDATE for the guidelines: "prose must not contradict the page's own exploration log" — a recurring red-team catch that no standing rubric line covers.

## Work list (13 items)

### [BLOCKER] guideline — Set evaluation order with parentheses

**Issue:** The prose says a new part 'joins with AND' and presents the strip as reading `Part A OR Part B AND Part C` — i.e. the OR set in the previous section survives. But the page's OWN exploration log (line 16) states, re-verified twice, that a fresh part RESETS every connector on the strip to AND. So after adding Part C the strip actually reads `Part A AND Part B AND Part C` and the builder's earlier A-B OR silently vanishes. A reader following along in-product will watch their OR disappear and mistrust the page — a direct contradiction between prose and the author's own verified log.

**Fix:** State the real behavior the log verified: adding a part resets EVERY connector on the strip to AND, so after adding Part C the strip reads `Part A AND Part B AND Part C`; the reader must re-set the A-B connector back to OR to get `Part A OR Part B AND Part C`. Make the prose (and the shot, if it shows a persisted OR) reflect that reset explicitly.

*Raised by: Red team, Product-fidelity checklist*

### [BLOCKER] definition-of-done — Set evaluation order with parentheses (branching-brackets.png)

**Issue:** branching-brackets.png is a 436x74 bare crop of only the connector chips 'Part A OR ( Part B AND Part C )' floating on a plain background. Its alt text claims it is 'The expanded expression editor showing...', but the pixels show NO editor — no modal chrome, no magnifier, and none of the clickable parenthesis affordances the prose teaches ('click the magnifier... then click the parenthesis marks before and after a part'). The shot neither demonstrates the section's actual lesson (HOW to place brackets) nor matches its alt text.

**Fix:** Recapture the expanded/magnified arrangement editor with enough modal surround that it reads AS a distinct larger editor, showing the clickable '(' ')' targets placed around the (Part B AND Part C) group. Then correct the alt to describe what is actually in frame (the expanded editor with brackets placed around Part B AND Part C).

*Raised by: Definition of Done, Guideline compliance*

### [BLOCKER] verify-in-product — Place the Condition block

**Issue:** The prose asserts 'two exits - Yes on the right, No on the left.' I read both canvas screenshots: in branching-block.png the Yes edge leaves the top-right and the No edge leaves the BOTTOM of the block routing downward; no edge emerges from the left except the incoming Start connection. The pixels contradict the 'No on the left' spatial claim. (The exploration log line 10 says 'Yes right, No left' as source handles, so the on-screen render and the handle description disagree — needs adjudication in-product.)

**Fix:** Verify the actual handle/edge positions in-product. Reconcile the prose to what renders: describe the exits as they appear (e.g. 'Yes leaves the top-right and No the bottom'), or if source handles genuinely differ from routed edges, drop the left/right claim and describe the labeled Yes/No exits without asserting a side the screenshot contradicts.

*Raised by: Red team, Product-fidelity checklist*

### [MAJOR] definition-of-done — Whole page (ledger / verdict)

**Issue:** Confirmed on disk: PLATFORM-REVIEW-LEDGER.md has NO section for content/build/flow-control/branching.md, and docs-review/verdicts/ has no branching verdict file. On the DoD lens the ledger IS the binding definition of done, and the 'run the gate before handoff' standard requires a fresh ship verdict on disk as the last step. Without it there is no recorded, evidence-backed clearance — doclint-green is never the bar.

**Fix:** Add a ledger section for the page recording the in-product verification evidence already captured in the exploration log (the seven fresh shots, the LIVE run outcomes proving each path, the type/operation enumerations, the trigger-filter executionId=null vs real-id proof), and run the concept-page-review gate to write a fresh ship verdict to disk before handoff.

*Raised by: Definition of Done*

### [MAJOR] verify-in-product — Set the data type and operation

**Issue:** The prose states '`STRING` offers `CONTAINS`' as a concrete operation-label example, but the exploration log (lines 6-7) enumerates only INT and BOOLEAN operation lists — STRING's operations are never enumerated. This is a prose-only, high-risk falsifiable claim (an exact dropdown label) with no screenshot and no note backing it.

**Fix:** Open the Operation dropdown with Value Data Type = STRING and confirm an operation literally labelled CONTAINS exists; record it in the exploration log. If the exact label differs, correct the example.

*Raised by: Product-fidelity checklist, Red team*

### [MAJOR] educator — Set evaluation order with parentheses

**Issue:** The section tells the reader the ungrouped `Part A OR Part B AND Part C` 'has two readings' and shows how to add brackets, but never states which reading FlowRunner evaluates when the reader does NOTHING. The Condition reference confirms a deterministic default exists. A builder who leaves the strip ungrouped gets a result the page never discloses, so they cannot predict their flow's behavior, and 'two readings' reads as unresolved ambiguity when the engine must resolve it.

**Fix:** Verify the default grouping FlowRunner applies to an ungrouped mixed AND/OR strip (e.g. left-to-right, or AND binds tighter) and state it, framing brackets as OVERRIDING that default rather than resolving a true ambiguity.

*Raised by: Red team*

### [MINOR] educator — Set the data type and operation

**Issue:** The section is teaching the INT / GREATER THAN check for the worked example, then breaks off into a reference-level aside about how the AI QUESTION operation works (its fields and behavior) — an operation the example never uses. This drags block-reference mechanism onto a concept page, dilutes the one idea, and the page already routes to the Condition reference for 'every type's operations' in the same breath.

**Fix:** Cut the AI QUESTION mechanism explanation from this section. If AI-driven branching is worth surfacing on the concept page, give it a one-line value mention where it earns its place, not a mechanism aside inside the number-comparison walkthrough.

*Raised by: Educator quality*

### [MINOR] guideline — Pick the value to check / Make a trigger fire only when a check passes

**Issue:** Two trailing sentences deflect to prior Learn-nav pages the reader has already been taught ('The Expression Editor page covers the editor itself.' / 'The Triggers page covers what triggers can start.'). Each reads as a reflex cross-link that adds no answer the section needed — contrast the legitimate forward route to the sibling Routing page whose question differs.

**Fix:** Drop both reflex sentences (or fold the Expression Editor reference into the glossary tooltip the term already carries). Keep only the forward route to the sibling page whose question differs (Routing on a Value).

*Raised by: Educator quality*

### [MINOR] guideline — Set the data type and operation (line 60)

**Issue:** The only trademark on the page appears mid-page on line 60 inside a body sentence about type detection — not near the top and not on a headline mention; the lede never names the product. Sibling flow-control pages carry no FlowRunner mention at all, so this lone mid-page trademark is also inconsistent with the section's established convention.

**Fix:** Either drop the trademark and use the bare name here (matching the sibling pages), or move the first/prominent FlowRunner mention to the lede if a product mention belongs there.

*Raised by: Guideline compliance*

### [MINOR] definition-of-done — Combine checks into one question (branching-parts-or.png)

**Issue:** branching-parts-or.png shows a type-detection warning triangle on Part B's Value Data Type (BOOLEAN / CHECKBOX, IS TRUE), but the section prose never addresses it. The type-mismatch warning is explained one section earlier, but here it sits on the 'correctly built' two-part OR the reader is following, so a reader reproducing this config will see the same warning on their own correct check and wonder what they did wrong. The log confirms this warning is transient and clears in the settled state.

**Fix:** Recapture parts-or.png in the settled state where the transient warning has cleared (or with a firstOrder BOOLEAN value present so the detected type matches), so the shot shows no unexplained warning. If recapture is impractical, add a half-line noting it is the same type-detection hint from the prior section.

*Raised by: Definition of Done, Educator quality, Red team*

### [MINOR] verify-in-product — Combine checks into one question

**Issue:** The prose routes a question with more than two answers to the Value Router block ('route on a value with Value Router... covered in Routing on a Value'). routing.md exists (confirmed), but the exact block name/label 'Value Router' as the multi-way branching block is a prose-only, medium-risk label claim not shown in any screenshot on this page.

**Fix:** Confirm in-product that 'Value Router' is the exact block name for multi-way branching (already routed correctly to the existing routing.md target).

*Raised by: Product-fidelity checklist*

### [NIT] definition-of-done — Place the Condition block / Wire the Yes and No paths (alt text)

**Issue:** The block's on-canvas label in the pixels is 'Needs Manager Approval?' (with a question mark, confirmed by reading branching-block.png); both alt texts render it without the '?'.

**Fix:** Match the alt text to the canvas label ('Needs Manager Approval?') in both image alts.

*Raised by: Educator quality*

### [NIT] educator — Set evaluation order with parentheses

**Issue:** This is the densest passage on the page — it packs both parenthesization readings, the concrete false-on-shipping consequence, and the bracket-placement UI mechanics into one paragraph, hitting the reader with a wall of clauses versus the crisp cadence above. It teaches well and earns its place; this is optional polish, not a failing passage.

**Fix:** Optional: break the two-readings explanation from the how-to-place-brackets mechanics into two short paragraphs so the concept lands before the UI steps.

*Raised by: Whole-page craft*

---

## Re-drive #2 — 2026-07-10 (gate run wf_50db37c4, verdict major-rework)

Gate re-run after the first fix pass returned `major-rework` again — with narrower, real findings (the fidelity lens crashed on a socket error, so its checklist was partial). All 11 items resolved below. **I did NOT re-run the gate a fourth time** — per the standing "gate is a one-time net, not a loop; hand to Mark, who decides ship" rule, the two remaining items are Mark's judgment calls, not fixable defects. Handing over as a status update, not a "done" claim.

**Concrete findings cleared:**
- [x] BLOCKER (ship verdict on disk) — resolves once Mark rules on the two judgment items below; not re-looping the gate to manufacture a green verdict.
- [x] MAJOR branching-brackets.png over-claim — recaptured as the arrangement strip with brackets around Part B AND Part C; crop cleaned to the card interior (no dark/red bleed); alt rewritten to describe exactly what is in frame (no "larger editor" over-claim).
- [x] MAJOR navigation wall — prose now names the palette tab for each reference: Initial Data lives on the ((Variables)) tab; the trigger's External Callback Data lives on the ((Block Data)) tab.
- [x] MINOR arithmetic metaphor — replaced with plain "FlowRunner evaluates every AND before any OR" (default grouping still run-proven).
- [x] MINOR bold Initial Data — unbolded so the glossary tooltip applies.
- [x] MINOR **+** not chipped — now ((+)).
- [x] MINOR INT-for-currency — added "A total with cents would use DOUBLE."
- [x] MINOR AI QUESTION "every" unverified — softened to "Most data types" (verified on INT/BOOLEAN/STRING; not all seven driven).
- [x] NIT section title — "Place the Condition block" → "Add the flow's decision point" (takeaway-carrying).
- [x] NIT alt "?" — both alts already carry "Needs Manager Approval?".

**Two items left for Mark (judgment, not defects):**
1. **MAJOR / product bug — the boolean type-detection warning.** VERIFIED it is unavoidable and reproducible: on a FRESH flow (2F32B2E2) a `BOOLEAN / CHECKBOX` check on `{{Initial Data->firstOrder}}` shows "detected type: INT" BEFORE any run AND still after a LIVE run with a real JSON boolean `true`. The check evaluates correctly regardless (firstOrder true → Yes, run-proven). So FlowRunner mis-detects boolean Initial Data fields as INT — a probable **product bug**. The page currently KEEPS the boolean example and explains the warning honestly (per the gate's own sanctioned alternative). **Mark's call:** keep the boolean example (surfacing the quirk honestly) or switch the multi-part example to all-INT fields (itemCount / discountPercent) for a warning-free exemplar. The bug itself is filed for the product team.
2. **NIT — trademark on Build pages.** No page in build/ names the product; this page uses bare "FlowRunner" to match siblings. Whether deep Build narrative pages carry ™ on first mention is a convention call for Mark.

doclint 0/0; plain-style greps clean.

---

## Mark review round — 2026-07-10 (6 corrections, all applied)

1. **Newly-dropped block shows no branches** → prose now warns: a just-dropped Condition shows no exits until selected/connected. (Verified in-product: fresh drop = no exits; select reveals Yes/No.)
2. **Value to Check referenced but never shown** → added a config-panel shot (`branching-fields.png`) at first reference, before the Expression Editor shot.
3. **Set Variables can't "process an order"** → No-path block changed to an HTTP Request `Submit Order` (Yes = HTTP Request `Notify Manager`); `branching-paths.png` recaptured.
4. **"connector" collides with a glossary/snippet term** → reworded to "the AND/OR between the parts."
5. **Boolean type warning** → Mark's clean flow shows none; my earlier "product bug" was a CONTAMINATED-FLOW artifact — retracted (bug memory deleted). Multi-part example switched to all-INT fields (`itemCount`, `discountPercent`) so the shot is clean and warning-free; `branching-parts-or.png` recaptured, no warnings. The defensive parenthetical is gone.
6. **"Adding a part resets connectors to AND" is a bug being fixed** → removed from the page and the exploration log.

Rebuilt on a fresh flow ("Order Approval Clean", ADDC6191). Principles distilled into CONCEPT-PAGE-PATTERN §0j (example fidelity; warn on state-dependent shots; show a control at first reference; rule out self-contamination before calling a bug; don't teach a bug-being-fixed; check common words for glossary collisions). doclint 0/0; plain-style greps clean. Gate not re-looped (Mark is reviewing directly).
