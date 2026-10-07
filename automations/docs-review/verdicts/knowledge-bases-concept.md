# Gate verdict — reference/knowledge-bases-concept.md

## 2026-10-06 - release sweep "Without version/devtasks2" + "without3"

- Verdict: **major-rework** (concept-page-review wf_a2ba6161-f45, one run; not re-run). Mark decides ship.
- Scope: FR-3662 -> FR-3666 (fixVersion **v.1.1.3, unreleased**): OpenSearch store, reworked PostgreSQL form, store choice
  permanent, test-failure messages. Weaviate (FR-3691) is in the dev bundle only - not documented.
- Mark's 2026-08-15 ruling still stands for the rest of the page: "KBs are verified by our QA" - the older-debt items below are
  listed for the record, not queued.

### Release delta - resolved after the gate
- Item 1 (blocker): the gate caught that refgen had overwritten the hand edit. Edits moved into
  block-knowledge/knowledge-bases-concept.yaml and regenerated: OpenSearch in the store list and its own bullet (Node URL with
  protocol and port, Username, Password, Verify SSL certificate on by default, Test, Index, 2.4+ with k-NN); "The choice is
  permanent"; the shared "picker stays locked until a test succeeds" paragraph with both failure messages verbatim.
  Generated page now has 10 "OpenSearch" hits.
- Item 2 (partial): PostgreSQL bullet rewritten to the driven form - host only, Port 5432, SSL mode Disable / Require /
  Verify full (default Require), Test, ((Table)) picker (was "Table Name"), `knowledge_base_vectors`, pgvector or a user
  allowed to install it. Column pickers for an existing table with data NOT documented (need a real database).
- Item 3 (partial): OpenSearch's ((Search entire index)) added; the unproven "embeddings produced outside FlowRunner" clause cut.
- Item 6: the banned "A flow that runs when..." sentence rewritten as a trigger block that waits for new content.
- Item 17: Add Document / List Documents pilled.
- Evidence: forms and both failure paths DRIVEN on dev 2026-10-06; the rest SOURCE (Sergey Androsov's FR-3666 answers),
  recorded in the YAML's RELEASE comment. PROD DRIVE OWED (same batched session as compliance).

### Older debt carried (covered by Mark's 08-15 QA ruling)
- Items 3-5, 7-16, 18-34: Search entire collection states per store, Data-tab upload path, section order, agent-managed
  documents section, attach-shot alt vs pixels, ledger contradictions, permanence/rotation wording, Failed/Stale statuses,
  embedding providers, MongoDB Index Name, headings, glossary tooltip, scope, detach state, example question, lede, formatting,
  Setup-tab typos (item 34: bundle only - not filed; needs a fresh look first).

---

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
