# Gate verdict — reference/knowledge-bases-concept.md

> **RESOLVED by Mark, 2026-08-15:** "KBs are verified by our QA, no need to redo the work."
> The two remaining recapture items below (kb-attach-to-agent.png and the Setup/Data-tab shots)
> are deliberately NOT being produced — the QA team owns Knowledge Base verification. With that,
> nothing on this page is outstanding; the gate's `revise` stands as the record of what the
> screenshots would have added, and Mark's decision closes it.

- **Date:** 2026-08-14
- **Gate verdict:** `revise` (docs-content-review, final run wf_0b55d68e — third gate round this session)
- **doclint:** 0 errors / 0 warnings (page-level; repo-wide warnings belong to blocks.md)
- **Trigger:** release 1.0.13 (FR-3316 / FR-3338) removed the In-Memory vector store; the page's
  setup-screen section, default-store claims, screenshot, and training material were stale.

## What was rebuilt and verified this session (all in-product, Documentation Flows)

- Create dialog re-driven end to end: now a **two-step wizard** ("Create AI Agents Knowledge
  Base": General Settings → Storage Configuration). Vector Store options are exactly
  **MongoDB Atlas / Qdrant / PostgreSQL (pgvector)**, no default; In-Memory is gone.
  Description and AI API Key are required. Embedding Model list confirmed (grouped by
  Open AI / Google Gemini AI / Mistral AI / Cohere / Voyage AI; default Text Embedding 3 Small).
- All three Storage Configuration forms driven; every field tooltip captured verbatim into the
  yaml `ui` block (incl. MongoDB's Test-gated Database/Collection pickers, pgvector table
  auto-creation, and the Search entire collection semantics).
- Two fresh screenshots captured and read back: `knowledge-bases-setup.png` (step 1, Product
  Docs scenario) and `knowledge-bases-storage.png` (step 2, Qdrant).
- Three gate rounds cleared: chunk-size/overlap grounding, worked-scenario framing (Product
  Docs on Qdrant, carried through prose), attach-section payoff (warranty-period question,
  used consistently), KB-screen section added (Setup/Data tabs), Add-Document first-load beat
  ("Loading and maintaining documents"), file-id/metadata grounding, standing-resource dedup,
  bring-your-own store+key trade-off in When-to-use, terminology consistency, and all nits.

## Remaining items — ALL blocked on one thing

Creating a Knowledge Base in Documentation Flows needs an **embedding-capable API key**
(only an Anthropic key is saved; embeddings need OpenAI / Voyage / Gemini / Mistral / Cohere).
Until one exists, the following cannot be recaptured, and the gate correctly holds the page at
`revise`:

1. **kb-attach-to-agent.png** — still shows "Test KB" (2026-07-10 capture, different workspace)
   against the Product Docs walkthrough; Manage Capabilities Knowledge-group labels also
   drifted ("DOCUMENT MANAGEMENT ACTIONS"/"KNOWLEDGE BASES" empty-state vs the shot's
   "Document Management"/"Search"). Pre-existing parked item (2026-08-06).
2. **Setup/Data tab shots** of an opened Product Docs KB (new section currently no-shot with
   the blocker documented in-source).

Both recaptures are scheduled in the page's own RECAPTURE comments. Once a key is added, the
reshoot plus a gate re-run should take the page to `ship`.

## Fidelity checklist (non-gating)

The gate's 17-claim verify-in-product list is superseded for the claims driven this session
(dialog labels, store options, per-store fields, tooltips — all captured 2026-08-14 in the
yaml's verification comments). Genuinely outstanding: pgvector auto-creation observed only as
the product's own tooltip claim; Search-entire-collection scoping behavior (tooltip-sourced);
chunk-size units at runtime; the with-KB Manage Capabilities state (same key blocker).
