# Gate verdict — api/block-results.md

- **Date:** 2026-08-25
- **Gate verdict:** `major-rework` (concept-page-review, run wf_73ba7b68-2ec — 6 lenses + synthesis)
- **doclint:** 0 errors / 0 warnings (with `--warnings`)
- **Status:** REWRITE of a page that said the feature was unreleased. Blockers partially cleared
  (below); **not yet re-gated, so not ship.**

## Why the page was rewritten

The previous version read "It has no endpoint to call yet" and "Not released." FR-3243 shipped the
endpoint in **1.0.13** (2026-08-10); FR-3342 moved it under `flow/{flowId}` in **v1.0.14**. Driven end
to end 2026-08-25 — log in `.cache/api-spec/verification-2026-08-25-execution-api.md`.

**The spec in FR-3238 does not match the product:** `result` is the stored block-result envelope
(`data` / `errorCode` / `httpCode` / `success`), not the bare value the spec's sample implied. The
block's own output is under `result.data`.

## Gate summary (verbatim)

Not ready. The wire contract is genuinely well evidenced (dated verification comment plus a full driven
log), but the page carries seven blockers concentrated in two places: the worked examples do not hold up
(the `28162` demo sends an in-range `occurrence=2` against a block the page just showed ran six times,
and never shows the refusal body it promises), and every claim about the *product* rather than the wire
is unverified or contradicted by this repo's own dated in-product records — "renaming a block does not
rename its alias" is backwards for the auto-derived alias the section teaches (flow-editor.md, VERIFIED
2026-07-27, Mark's own correction), and "the same value a block placed after the loop would read" is
false per passing-data.md's verified loop-scoping rule.

## Blockers — resolutions

| # | Blocker | State |
| --- | --- | --- |
| 1 | "Renaming a block does not rename its alias" — **backwards** for the default alias | **FIXED.** Split into the two real cases: a default alias follows the block's name (so renaming breaks a client on the old one), a ticked-and-typed alias survives renames. Matches `flow-editor.md` (verified 2026-07-27, Mark's correction) |
| 2 | "the same value a block placed after the loop would read" — **false**; loop results are pass-scoped and unreadable after the loop (`passing-data.md`) | **FIXED.** Reworded to the true and stronger claim: this endpoint reaches per-pass values the flow itself cannot, because it reads the stored run |
| 3 | The `28162` example sent an **in-range** `occurrence=2` against a 6-pass block and showed no refusal body | **FIXED.** Re-driven with `occurrence=7` (28162, `details.occurrenceCount` 6) and the real refusal body is now printed |
| 4 | Reference Result Data As documented only in the ON state; it is a checkbox, off by default | **FIXED.** Both states stated, with the off-state consequence (not addressable here) and the route to `passing-data.md` |
| 5 | Skipped-branch behavior asserted, never driven | **PARTIAL.** The extrapolated sentence still stands — see below |
| 6 | No ledger section, no verdict file | **PARTIAL.** This file exists; ledger section still owed |
| 7 | Lede opened on storage mechanics rather than the reader's artifact | **FIXED.** Now opens on holding an `executionId`, and names the loop capability |

Also fixed: 28159-on-TERMINATED is now driven (was extrapolated); the adaptation instruction names all
four example-specific segments, not just the credentials; the banned not-X-but-Y flourish on the
Condition envelope is gone; the counted lead-in above the alias list is gone; ™ added.

## Still owed before a re-gate can return ship

**Drives:** the skipped-branch case (does an aliased block on an untaken branch answer 28161 while open
and what once terminal?); a hand-typed custom alias round-trip; alias uniqueness / `ambiguousBlock`;
blocks inside a SubFlow and inside a Call Flow'd child; a `success: false` envelope with populated
`errorCode`/`httpCode` (a failed block's result IS stored and readable — driven — but the codes were
`null`).

**Shots:** the Cart Summary canvas showing `Priciest so far?` inside the `Scan Products` List Iterator,
so the alias in the JSON maps to a block the reader can see; a mid-flight Instances frame for the
progress section; recapture the alias shot with the panel header included.

**Structure:** beautify both JSON samples one property per line; carry the full four-field envelope in
the occurrence sample; add HTTP status column to the Errors table (execution-status.md now has one — the
two must match); demonstrate `occurrence` on an alias that produces a real per-pass value rather than a
Condition whose `data` is `null` on all six passes; add a short poll snippet for the progress recipe.

## MARK — decision owed

- [ ] Same unenforced-API-key finding as `execution-status.md`: a garbage key returns stored block
      results. See that verdict file.
