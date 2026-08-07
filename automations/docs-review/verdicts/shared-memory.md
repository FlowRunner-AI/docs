# Verdict — Shared Memory (content/learn/concepts/shared-memory.md)

- **Date:** 2026-07-05
- **Status:** rebuilt after Mark caught two defects the old (alt-text-trusting, structure-only) gate missed. Ready for Mark's review — Mark is final quality authority.
- **doclint:** 0 errors, 0 warnings.

## The two misses (both now fixed, both now catchable by the upgraded gate)
1. **Anchoring screenshot showed the DEFAULT anchor** ("Flow Memory") under a section teaching per-caller anchoring — a picture of the opposite of the lesson. FIXED: captured `sm-anchor-inuse.png` (Memory Anchor Selection dialog, Anchor Source = Initial Data, Anchor Property = `data.customerId`) and swapped it in. A pixel-reading reviewer confirmed it now DEMONSTRATES the concept.
2. **Prose read as indifferent / proud-less.** FIXED: full craft rewrite. A per-paragraph reviewer now reads it as "someone who cares — warm, concrete, why-first, progressive; the opposite of flat."

## The system fix (so this class can't slip again)
- **The reviewer now READS the pixels** (DoD lens opens each PNG) instead of trusting author-written alt text — the root cause of miss #1. PROVEN: run on the OLD page, the upgraded reviewer flagged the default-anchor shot as a BLOCKER by looking at it.
- **A per-paragraph quality lens** interrogates every paragraph against explicit bars: Useful? Structured? Teaches? Builds on prior knowledge? Engaging (not boring)? — miss #2's fix. (Mark's correction: quality IS checkable, per paragraph.)
- Codified in `block-knowledge/VOICE.md`, `docs-review/CONCEPT-PAGE-PATTERN.md` (§0e, §0f), `tools/doclint/DEFINITION_OF_DONE.md`.

## Confirmation (upgraded reviewer, on the rewritten page)
- Screenshot: PASS (pixels show the configured caller anchor; alt faithful).
- Voice: strong; every paragraph alive. One defect found ("two-block" vs the counter's three blocks) — now fixed.

Note: the lens rated the OLD prose "23/24 alive" while Mark found it indifferent — the automated quality bar is not yet as demanding as Mark's ear. Mark remains the final authority; the lens is a strong net, not a replacement.
