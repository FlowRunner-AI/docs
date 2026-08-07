# Verdict — flow-memory-concept / Agent Memory (content/reference/flow-memory-concept.md)

Gate: concept-page-review. Latest run 2026-07-09 → **revise** (up from major-rework/revise).

Screenshots VERIFIED live-accurate: flow-memory-settings.png (anchor=customerId, gear tab) + flow-memory-messages-history.png (AI Agent header, toggle ON, limit 15).
OPEN:
- MAJOR: messages-limit UNIT — hold "messages" everywhere (not "turns"); reconcile the "15 messages" example vs two-messages-per-run; add exchange math. (partly fixed)
- MAJOR: state the DEFAULT limit value (verify in-product on a fresh AI Agent).
- MAJOR: "Giving each caller their own memory" carries 3 settings — split or trim the two policies to a pointer (Per-User Memory owns them).
- MAJOR: retitle generic sections is a gate ask BUT "How it works"/"When to use it" are generator-standard titles used by the approved exemplars — treat as pattern-convention, confirm with Mark.
- MINOR: How-it-works + caller-section openers lead on the machine; banned word "just".
doclint: 0 errors / 0 warnings.

---
Round (post-fix consolidated pass, 2026-07-09) — one-time-net gate run wf_c07c671c-e23 → **revise**; findings triaged, fixes applied, NOT re-run per STANDING-RULES:
- MAJOR (cross-page anchor value-form mismatch with Per-User Memory, NEW red-team class): RESOLVED — verified the Memory Anchor in-product; recaptured flow-memory-settings.png with the anchor set to the path `data.customerId` (via the real Memory Anchor Selection dialog: Anchor Source=Initial Data, Anchor Property=data.customerId), matching the sibling Per-User Memory example exactly. Alt updated.
- MAJOR (anchor presented as free-text typed, not the dialog): RESOLVED — prose now names the ((Memory Anchor Selection)) dialog with ((Anchor Source)) + ((Anchor Property)), and includes the default source Flow Memory (= no split), grounding "left at its default, every run shares one memory." (Anchor Source options verified live: Initial Data / Initial Trigger / Flow Memory.)
- MAJOR (two policy dropdowns shown in one silent state): RESOLVED — deferral made explicit: prose names each policy's shown default (Terminate on Memory Access; Never), says each opens into a set of options, and points to Per-User Memory for the full enumeration.
- MINOR (tab name "Flow Settings" vs sibling "Settings"): RESOLVED in this page's favor — the gear tab's live product tooltip is literally "Flow Settings" (verified). NB: the sibling Per-User Memory page calls it the "Settings" tab; that page (not this one) should be reconciled to "Flow Settings". FLAGGED.
- MINOR (messages-vs-turns unit): default 15 / max 20 and 2-messages-per-run are noted; whether the Limit field COUNTS individual messages vs exchanges is not pixel-confirmed. Prose holds one unit (messages) consistently; the "≈7-8 back-and-forths" is derived. FLAGGED as not-pixel-confirmed.
- MINOR (load-at-start/append-at-end sequencing; isolation "same value share / different never cross"): prose-only runtime behavior, grounded in the mechanism + legacy behavior docs; not driven by a two-run live A/B. FLAGGED.
CANDIDATE NEW GUIDELINE RULE: sibling concept pages that cross-link must show the identical value-form and control label for the same control (anchor form, tab name).
doclint: 0 errors / 0 warnings.
