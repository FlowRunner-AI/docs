---
description: Turn Mark's review of a page into applied fixes AND distilled guideline rules — the anti-"one-off fix" gate.
argument-hint: <page> (Mark's review text is in the conversation)
---

Mark has reviewed **$ARGUMENTS**. Process his feedback so that it improves both the page AND the guidelines. Work through every point he raised, in order. Do NOT skip step 3 for any point.

For the whole review:

1. **Log to the ledger.** In `automations/docs-review/PLATFORM-REVIEW-LEDGER.md`, under this page's section (create it if absent), add each of Mark's points as a checklist item.

2. **Apply the fix.** Make the change on the page. If a point is a product-fact question, verify it in the live product first (never guess). Check the item off with evidence (what changed / what you saw in-product / which shot).

3. **Distill the rule (REQUIRED — a fix without this is incomplete).** For EACH point decide: is this generalizable beyond this page?
   - **Yes** → write the rule into `automations/docs-review/CONCEPT-PAGE-PATTERN.md` §0d and/or the `automations/block-knowledge/VOICE.md` Calibration Log, and add a `memory/` entry if it is a recurring correction. (The reviewer reads these live, so this permanently raises the bar.)
   - **No** → note explicitly "one-off, no rule" for that point.
   Your final summary MUST list, per point, either the guideline diff you made or "one-off, no rule". Do not present the work as complete without this per-point accounting.

4. **Update the trackers.** Update the page's row in `automations/docs-review/AWAITING-REVIEW.md`.

5. **Re-gate.** Run `/docs-review $ARGUMENTS` to confirm the fixes clear the gate and re-record the verdict. Loop to `ship`.

Report back with: the per-point fix + rule-or-one-off table, and the new verdict.
