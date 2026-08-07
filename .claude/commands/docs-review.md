---
description: Pre-handoff gate for a concept page — doclint + adversarial multi-lens review; writes a verdict and only lets you hand off on `ship`.
argument-hint: <page> (bare name like "shared-memory", or a path)
---

You are running the **pre-handoff gate** for the concept page: `$ARGUMENTS`

This gate — not your own judgment — decides whether the page is done. Do exactly this:

1. **Resolve the page.** A bare name like `shared-memory` → `automations/content/learn/concepts/shared-memory.md`; otherwise treat `$ARGUMENTS` as the path.

2. **Mechanical floor.** Run `python3 -m tools.doclint <page> --warnings` from `automations/`. Note every error and warning.

3. **Adversarial review.** Invoke the `concept-page-review` workflow (the Workflow tool) with `args: { page: "$ARGUMENTS" }`. This runs four lenses (educator, guideline-compliance, definition-of-done, product-fidelity) against the live rubric and returns a JSON report: `verdict` (`ship` | `revise` | `major-rework`), `summary`, and `workList`.

4. **Record the verdict.** Write/overwrite `automations/docs-review/verdicts/<page-name>.md` with: the date (from context, not `date`), the verdict, the doclint result, the `summary`, and the full `workList` (each item's severity, kind, section, issue, fix). This file is the git-tracked evidence of done-ness.

5. **Act on the verdict:**
   - **Not `ship`** → present the work list. **You** clear every item yourself — including doclint issues and every `verify-in-product` item, which means driving the live product with Playwright to confirm the claim (capturing fresh screenshots where a claim needs one). Never hand a `verify-in-product` item to Mark. When the list is clear, **re-run `/docs-review` on the same page** and loop until `ship`.
   - **`ship`** → add or update the page's row in `automations/docs-review/AWAITING-REVIEW.md` (what changed + today's date), confirm the ledger section is cleared, then tell Mark the page is ready for review. Reference the verdict file.

**Hard rule:** you may only describe a page to Mark as done/ready when its verdict file says `ship`. "doclint is clean" is not `ship`.
