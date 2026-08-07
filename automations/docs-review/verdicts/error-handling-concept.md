# Verdict — error-handling-concept (content/reference/error-handling-concept.md)

Gate: concept-page-review. Latest run 2026-07-09 → **major-rework**.

Screenshots live-captured/pixel-accurate (handle-error-read.png recaptured to the real 28063/AI Agent error).
OPEN:
- BLOCKER: Retry section frames Repeat as an attempt counter; FlowRunner Repeat is condition/iteration-driven. Name the Maximum Iteration Count field (=5), state how the loop terminates (Break on success; failsafe caps retries), reconcile with repeat.md. VERIFY the Retry Logic flow's Repeat config (condition vs maxIterations).
- MAJOR: How-it-works continuity — handle-error-read.png reads an AI Agent/28063 error but the section's running example is Fetch Orders. Either recapture to a Fetch Orders failure for How-it-works, or move the read shot to the Example (which uses AI Agent 28063).
- MAJOR: Example's "runs the AI Agent again" contradicts the retry lesson (a bare recovery path can't re-run) — reconcile.
- MAJOR: "Reacting to different errors" no-shot note claims handle-error-read.png as coverage but that shot isn't a Condition-branching-on-code scenario.
- [MARK-OVERRIDE] trwo-exits image kept per Mark.
doclint: 0 errors / 0 warnings.

---
Round (post-fix consolidated pass, 2026-07-09) — one-time-net gate run wf_b4337062-d41 → **major-rework**; findings triaged, fixes applied, NOT re-run per STANDING-RULES:
- BLOCKER (trwo-exits-with-errorhandler.png shows TWO blocks guarded): CONFIRMED in the pixels — Process Orders ALSO has a red error connector into Handle Error, so the shot shows a multi-guard shape, contradicting the "one block at a time" prose + its own alt text (which names only Fetch Orders). This is MARK'S image (he provided + placed it), so NOT replaced unilaterally. FLAGGED TO MARK with the pixel evidence: either recapture as a true single-block shot, or move the illustration to the multi-guard framing.
- MAJOR ("Maximum Iteration Count" label prose-only): RESOLVED — verification note added; the label is documented with its verbatim product tooltip on the Repeat block reference (repeat.yaml/repeat.md), schema key maxIterations, set to 5 in the Retry Logic flow. (Live re-confirm on the Repeat config panel not captured this pass; cited the block's own reference page instead.)
- MINOR (retry enabling rule implicit, red-team): RESOLVED — added the explicit rule: inside a Repeat, a HANDLED failure ends only the current pass, not the whole run; an unhandled one would stop the loop and all — the Handle Error is what lets Repeat come around.
- MINOR (raw-message vs "lean on message", NEW red-team class): RESOLVED — added a caveat that **message** is the raw failure text (sometimes an internal string like the example's JS error), so pair it with **source** rather than trusting it to read cleanly to an end user.
- MINOR (Condition-branches-on-code prose-only): reasoned from the mechanism (a Condition consumes any expression, incl. {{Handle Error Result->code}}); not wired live this pass. FLAGGED as reasoned-not-tested.
- MINOR (message+source "always" for a Custom Cloud Code throw): the 2026-06-23 product-owner note covers code-is-conditional + source-names-block; the narrow CCC-throw-populates-source edge is not separately pinned. FLAGGED.
- MINOR (How-it-works title/lump): JUDGMENT CALL — kept; the AI-Agent/28063 running example is carried cleanly through read-shot → Example → retry, and the two other diagrams are focused one-off illustrations. Flagged to Mark.
CANDIDATE NEW GUIDELINE RULE: when a page tells the reader to surface a caught-error field to end users, the sample value shown must itself read as an actionable human-facing reason, or the prose must flag it may be raw/internal.
doclint: 0 errors / 0 warnings.
