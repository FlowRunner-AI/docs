# FlowRunner Documentation Rewrite — Design

**Date:** 2026-06-16
**Status:** Approved (design); implementation pending
**Authors:** Mark Piller + Claude (paired)

## Purpose

Rewrite the FlowRunner™ documentation to be accurate, complete, and approachable.
The current MkDocs site (~101 pages) is stale and incomplete relative to the product:
the *Custom Actions* extensibility tree is obsolete, the AI reference lists blocks that
are moving to a third-party extension, the Block Reference is partial, and entire platform
surfaces (Forms, MCP Servers, Knowledge Bases, Connections, Compliance & Security) are
missing or thin.

This is a **complete rewrite**, grounded in a product-verified recon already completed:
- `automations/block-knowledge/*.yaml` — 31 structured, product-verified records (every
  native block + concept records), the triple-purpose source (docs · tests · training).
- `automations/.cache/orientation/notes.md` — full recon of blocks and platform surfaces.
- The product is the **single source of truth**; existing docs prose is not trusted.

## Constraints (non-negotiable)

- **Design system is fixed.** Follow `automations/MKDOCS_GUIDE.md` and the locked
  `content/css/flowrunner-mkdocs.css` (do not modify). Light theme default; family
  resemblance with the product UI; no new colors/fonts; no inline `<style>`.
- **Writing style** follows `automations/CLAUDE.md` (terminology, formatting, tone) plus a
  new voice spec (below).
- **Do not name SurveyJS** in the docs (Forms is built on it, but licensing does not require
  attribution; the Survey Creator is white-labeled). See memory `forms-surveyjs-no-mention`.
- **Audience:** beginner-first with layered depth (progressive disclosure). A non-technical or
  new user can orient and build a first flow; technical depth is layered underneath for builders.

## Information Architecture (Approach C — Hybrid)

A layered IA along the Diátaxis spirit (learn → build → look up → understand): a beginner-first
learning/building journey, feature-area guides for the platform surfaces that are distinct
"places" in the app, and a generated Block Reference as the lookup layer.

```
1. LEARN  (orient → first success → concepts)
   - Overview — what FlowRunner is; flows & instances
   - Terminology (glossary)
   - Quick Start — build & run your first flow
   - Core Concepts — Flows & Instances · Triggers · Blocks ·
     Variables & Data Buckets · Expressions · Subflows ·
     Shared Memory (cross-instance state)
   - Tutorials — curated, modernized demo flows

2. BUILD  (how to build flows — the core craft)
   - The Flow Editor — canvas, palette, block config, naming
   - Data & Variables — data movement, variables/data buckets,
     Expression Editor, Transform Data
   - Flow Control — conditions, value router, loops, wait,
     synchronize, return result, error handling, grouping
   - AI in Flows — AI Agent, AI Router, attaching capabilities
     (extensions · flows · MCP · knowledge bases)
   - Integrations & I/O — HTTP, Call Flow, External Callback,
     communicating with Forms, Custom Cloud Code
   - Managing Flows — versions, permissions, import/export, rename/delete

3. RUN & MONITOR
   - Testing — test panel, skip/simulated result, debugging
   - Running flows — manual, API, triggers
   - Scheduling — flow schedule + start/stop scheduled runs
   - Monitoring & Analytics — Dashboard, Performance, Instances, Logs, Versions

4. PLATFORM  (the app's feature areas / "places")
   - Forms · Knowledge Bases · MCP Servers ·
     Connections (OAuth + API Keys) ·
     Compliance & Security (Audit Log, HIPAA, Panic Mode) ·
     Workspace (credentials/transfer, Team, Billing)

5. BLOCK REFERENCE  (generated from block-knowledge YAML — lookup layer)
   - AI · Triggers · Actions · Control Flow · Data · Reusability ·
     Groups · Knowledge Base · Shared Memory · Scheduled Runs

6. EXTEND  (PARKED — reserved home; design on product update)
   - Custom Actions (redone feature, not yet shipped)
```

### Cut from the existing docs
- The entire **Custom Actions / No-Code Action Dev / JS Action Dev** tree under *Extend* —
  obsolete. (Custom Actions itself is **parked**, not gone — see below.)
- **Moderate Content / Speech-to-Text / Text-to-Speech** as native AI blocks — moving to a
  third-party OpenAI extension; not documented as native.

### Parked (resume on product update)
- **SLA** — only available on the Business plan; the full mechanism (SLA Calendars ↔ per-flow
  SLA Goals ↔ per-block Compliance Condition) is reviewed after the app is upgraded.
  SLA Calendars structure is captured; the end-to-end linkage is still inferred.
- **Extend / Custom Actions** — the redone feature isn't in prod yet; reserve the home, design
  the section during the product-update review.

### Placement decisions
- **Scheduling** lives under *Run & Monitor* (it governs *when* flows run).
- **Managing Flows** (versions/permissions/import-export) folds into *Build*, not a separate
  top-level "Manage" as in today's nav.
- **Custom Cloud Code** lives under *Build › Integrations & I/O* (revisit prominence later — it
  is a differentiator).

## Block Reference Generation System

The Block Reference is generated deterministically from the YAML records — "fully generated"
mechanically (single source, consistent, no drift), reading conversational because the prose is
genuinely authored *into the records*, not conjured by the template.

### Source → page
- **Source of truth:** `block-knowledge/*.yaml` (31 records), enriched with authored prose
  fields (`intro`, `mental_model`, `when_to_use`) written in the FlowRunner voice.
- **Doc-facing fields** (appear on the page): name → h1, `intro` lede, `mental_model`,
  `when_to_use`, a generated **Configuration** table (field · type · required · description ·
  verbatim help tooltip), **Behavior**, **Gotchas**, **Cross-references** (as links),
  terminology links.
- **Internal-only fields** (never rendered to public docs): `testability`, `assertions`,
  `known_bugs`, `provenance` — these serve the tests/training purposes.

### Pipeline
```
block-knowledge/<id>.yaml  ──►  validate  ──►  template  ──►  content/reference/<id>.md  ──►  MkDocs build
   (data + authored prose)     (schema)      (Jinja/py)       (committed artifact)
   └─ same source also feeds tests + training (separate consumers, out of scope here)
```
- **Generator:** a small Python script (MkDocs is Python). Validates each record against the
  schema (`block-knowledge/README.md` defines it), renders the page template, writes to
  `content/reference/<id>.md`, and generates the Reference nav section. Adding a block = adding
  a YAML file.
- **Committed output with guardrails:** generated pages **are committed** (so diffs are
  reviewable in PRs and rendered docs live in git). Each carries a
  `<!-- generated from block-knowledge/<id>.yaml — do not edit -->` header, and a regen-diff
  check catches hand-edits to artifacts. The YAML is the only thing edited.

## Voice & Style Spec + Calibration Loop

### The spec
A living document, `block-knowledge/VOICE.md`, co-located with the source it governs. It owns
the **prose voice** and per-block-page conventions: tone, opening conventions, how a
`mental_model` should read (concrete analogy, not a restatement), banned phrasings ("simply",
"just", "powerful"), sentence rhythm, good/bad examples. It **extends** CLAUDE.md and
MKDOCS_GUIDE.md (which already own terminology, formatting, and the design system) — no
duplication.

### Calibration loop
1. Pick **1–2 representative blocks** that exercise the full page anatomy (proposed: a
   rich-config action like **Custom Cloud Code** + a control-flow block like **List Iterator**).
2. Claude drafts the authored prose (`intro` / `mental_model` / `when_to_use`).
3. Mark reviews and gives feedback.
4. Claude revises **and** extracts every generalizable note into `VOICE.md`.
5. Validate on the second block — drafts should already be closer.
6. Batch-draft the remaining blocks, with `VOICE.md` driving first-pass quality; reviews get
   lighter and shift from tone to block-specific facts.

**Convergence:** voice rules stabilize in the first blocks and stop recurring. Block-specific
facts are corrected case-by-case (they don't generalize). First drafts trend toward right.

The arrangement: **Claude writes, Mark reviews and gives feedback, Claude revises** — and the
generalizable feedback trains `VOICE.md`, so the investment compounds.

## Phased Sequencing

Ordered by dependency and leverage.

- **Phase 0 — Foundations** *(no prose)*: restructure `mkdocs.yml` to the new IA (stub pages so
  nav stands up); build the Reference generator (schema validation → template → script →
  committed output + do-not-edit headers + regen-diff check, wired into the build); seed an empty
  `block-knowledge/VOICE.md`; add park-markers for SLA + Extend/Custom Actions.
- **Phase 1 — Block Reference** *(highest leverage; source is ready; seeds the voice)*: calibrate
  `VOICE.md` on the 1–2 blocks; author prose for all 31 records (batch + review loop); generate +
  commit all reference pages.
- **Phase 2 — Learn**: Overview, Terminology, Quick Start, Core Concepts, curated Tutorials.
- **Phase 3 — Build**: Flow Editor, Data & Variables, Flow Control, AI in Flows, Integrations & I/O,
  Managing Flows.
- **Phase 4 — Run & Monitor**: Testing, Running, Scheduling, Monitoring & Analytics.
- **Phase 5 — Platform**: Forms, Knowledge Bases, MCP Servers, Connections, Compliance & Security,
  Workspace.
- **Parked**: SLA, Extend / Custom Actions (resume on product update).

**Rationale:** Reference precedes the Learn/Build prose deliberately — calibrating voice on the
ready-made reference source means every later page inherits a mature `VOICE.md`. Cross-references
from reference pages to not-yet-written concept pages will dangle briefly until targets land;
acceptable.

**Execution granularity:** the rewrite is too large for one implementation plan. The first plan
covers **Phase 0 + Phase 1** (scaffolding → generator → calibration → reference). Each later phase
gets its own plan when reached.

## Success criteria
- New IA stands up in `mkdocs.yml`; site builds clean on the existing design system.
- Reference generator produces all 31 block pages from YAML, committed, with anti-drift guardrails.
- `VOICE.md` exists and is converging; reference prose reads in the FlowRunner voice and is
  product-accurate.
- No SurveyJS mention; obsolete Custom Actions tree removed; SLA + Extend reserved as parked.
