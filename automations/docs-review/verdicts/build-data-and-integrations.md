# Verdict — Build ▸ Data & Variables + Integrations & I/O (10 pages)

- **Date:** 2026-07-30
- **Status:** CLOSED 2026-08-06 — Mark reviewed all 10 pages line by line and every correction was applied in-session. See AWAITING-REVIEW.md for what he caught.
- **Gate blind spots this review exposed (worth carrying into future gates):** the gate passed `returning-a-result.md` while it contradicted `api/call-flow.md` on whether a REST caller can read the composed result; it passed a warning about blocks wired after a terminal block, a state the editor makes unreachable; and it passed `api/index.md` asserting a flow has no address until LIVE, contradicting `activating-a-trigger.md`. All three are CROSS-PAGE contradictions — no lens compares a claim against the page that owns the topic.
- **doclint:** 0 errors, 0 warnings across all 10. Full site build: no broken links.

## Pages
`build/data-and-variables/` index, passing-data, holding-values, reshaping-data, across-runs
`build/integrations/` index, calling-a-service, returning-a-result, running-another-flow, custom-actions

Written to Mark's IA rule (2026-07-29): **Platform introduces what things are; Build teaches how to use them.**

## The gate's verdict: revise (2 blockers, 19 majors). What was wrong and what changed.

### Blockers (both were my factual errors)
1. **`returning-a-result.md` claimed a REST API caller reads the composed result.** False: `flow-execution/overview.md:86-95` shows `POST /api/automation/flow/activate-by-name` returns `{"executionId": "String"}`. FIXED — the page now names Call Flow, SubFlow, and agent-as-tool as the readers, and states explicitly that an API start returns an executionId, not the result.
2. **`holding-values.md` taught list accumulation as a Set Variables step.** This violates a standing rule Mark set (VOICE.md:496-500): "Accumulating into a list is not 'Set Variables append'… seed with **Empty List**, then use **Transform Data / Add To List**… guessing a mechanism is a content defect." FIXED — the two idioms are now separated: running total via Set Variables (with the typed-`+`-concatenates trap), growing list via Empty List + Add To List, both with real shots, routed to `collections.md`.

### Systemic major 1 — my "doclint 0/0" was hollow
I **bolded** UI controls instead of chipping them `((…))`. doclint only demands a screenshot when a section carries a chip or an `.fr-block` pill, so bolding routed the core sections around the screenshot gate: green lint, unshown controls. FIXED — every named control is now chipped (16 chips across the batch), which surfaced the real gaps, and each was answered with a **real screenshot** rather than re-hidden:
- `return-result-config.png` (Content Type, Compose Result, Property/Value rows)
- `transform-data-operations.png` (the Operation picker, open)
- `http-request-config.png` (URL, Method, Header Name/Value)
- `list-iterator-seed.png` + `list-iterator-transform.png` (Empty List; Add To List writing back)
- `blocks-config-panel.png` (Reference Result Data As, Assign to a Variable)
- `call-flow-config.png` (Flow, Version, Initial Params) + `subflow-new-dialog.png` (Input Parameter Names)
- **`callflow-wait-for-completion.png` — captured fresh** (Documentation Flows, 2026-07-30). No existing image showed this toggle. A temporary Call Flow block was added to the `Route Requests` flow, the panel captured, and **the block deleted afterwards** — Mark's flow is back to its five blocks.

### Systemic major 2 — duplication of the concept/reference pages
The gate found `passing-data`, `holding-values`, `across-runs` were largely restatements of `expressions.md` / `blocks.md` / `variables.md` / `shared-memory.md`, and `reshaping-data`'s worked example copied the Transform Data reference verbatim, image included. FIXED by cutting, not padding:
- `passing-data` — dropped three restated sections; now leads with a one-line route to the Expression Editor and owns the scoping rules (loop-pass scope, untaken branches, results not yet learned).
- `holding-values` — dropped the naming/bucket and lifetime retellings; keeps the "when you need a variable" decision list and the accumulation idioms.
- `across-runs` — dropped the counter/anchor/expiration retellings; keeps the where-should-this-value-live ladder and says which two settings to get right, and where they live.
- `reshaping-data` — dropped the copied example and its image; now decision-first (do you even need one; one block one operation; which operation for which job) and routes to the reference for the walkthrough.

### Other majors fixed
- **`running-another-flow`** — added the missing third route (**Flows as Actions**, per `subflows.md:12`), the **LIVE requirement** for a called flow (`call-flow.md:39,56`) as a warning admonition, the **Version** selector, and where SubFlow input names are declared.
- **`calling-a-service`** — the credentials advice was unactionable for the very block the page teaches. Corrected to the verified mechanism: an HTTP Request has no credentials field, auth rides in a ((Header)) Name/Value pair (`http-request.md:94`). Added the response-body gotcha (no status/headers wrapper, so test a value in the body). "connectors" → **Extensions** (product term). "has a Retry Policy" → "turn on".
- **Marketplace contradiction** — `integrations/index.md` said "install from the marketplace" while `custom-actions.md` said there is nothing to install. Reconciled: Extensions ship built-in; a Marketplace offers pre-built actions to install.
- **Style** — removed the `not just a…` contrast construction and all four "just" fillers.

## Deliberately not done (flagged, not hidden)
- **Marketplace and Custom Actions specifics are undocumented.** The custom-action authoring experience was rebuilt (`extend/custom-actions.md` is a "Coming soon" stub) and the only Marketplace material in the repo is legacy and stale-branded ("Backendless Marketplace"). The page names both as routes and does not invent detail. **Needs in-product verification before it can be written properly.**
- **`across-runs.md`, `custom-actions.md`, and both index pages carry no screenshots**, each with a recorded reason: they are decision ladders and section maps that operate no controls, and every screen they mention is pictured on the page they route to.
- Minor items left by choice: the Core Concepts link landing on Flows & Instances (no concepts index exists); alias-suffix wording on the Transform Data reference itself (that page is generated from YAML and out of this batch's scope).
