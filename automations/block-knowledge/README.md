# FlowRunner Block Knowledge Base — TRIPLE PURPOSE (docs · tests · training)

One YAML file per block: `block-knowledge/<block-id>.yaml`. Each file is the single
source for that block's **documentation**, **regression tests**, and **training material**.
Source of truth is the **product**, never the old docs.

## Record schema (keys)

```
id:        kebab block id (matches palette elementId where possible)
name:      display name
category:  palette category (AI | Actions | Utils | Groups | Triggers | …)
kind:      native | extension | mcp
concept:   true   # OPTIONAL — set for "+"-add concepts (AI Assistants, SubFlows)

api:               # identifiers so tooling can LOCATE/BUILD this block in a flow def
  element_type:    # elements[].type for leaf blocks (e.g. CONDITION, ACTION, WAIT)
  group_type:      # groups[].type for containers (LOOP | ACTIONS | TRIGGERS)
  loop_type:       # LIST_ITERATOR | REPEAT (when group_type: LOOP)
  meta_type:       # metaInfo.type (AI_AGENT | CALL_FLOW | CUSTOM_CLOUD_CODE | …)
  operation:       # metaInfo.operation (CALL_FLOW | …)
  subtype:         # metaInfo.subtype (MODERATION | TRANSCRIPTION | *_DOCUMENT | …)
  config_keys: []  # metaInfo keys observed (the config schema, for drift snapshots)

testability:       # so the suite knows what can run deterministically
  class:           # deterministic | external | partial
  hermetic:        # true if it can run with no 3rd-party side effects
  mock_strategy:   # for external/partial: how to stub (usually Skip Block + Simulated Result)

docs:              # DOCUMENTATION
  purpose:         # 1–2 sentences
  when_to_use:
  mental_model:    # analogy/concept (shared with training)
  config:          # list of {field, type, required, default, description, options}
  produces_result: # bool (Reference Result Data As present?)
  data_in:
  data_out:
  gotchas: []
  cross_refs: []   # other block ids / concepts
  terminology: []  # terms this block introduces

behavior: []       # TEST: verified runtime semantics (prose, each one assertion-able)
assertions: []     # TEST: machine-checkable {id, code|given, when, expect, note}
                   #   when: run-block (debug/run/element) | run-instance
known_bugs: []     # TEST: {id, repro, observed, expected, severity, workaround/note}
                   #   double as regression cases (fail until fixed, then guard)

training:          # TRAINING MATERIAL
  learning_objectives: []
  prerequisites: []          # block ids/concepts to teach first (build-on-prior)
  common_mistakes: []
  exercise:                  # a hands-on task

provenance:
  confidence:      # V-run | V-real | V-config | INFER  (see legend)
  evidence:        # flow/instance/screenshot refs
  verified_on:     # YYYY-MM-DD
```

## Universal help tooltips (apply to nearly every block)

The product renders per-field help as `?` icons (`i.fa-circle-question`); two appear on
almost every block (when their accordion is expanded). Verbatim, so individual records
don't repeat them:

- **Skip Block:** "When enabled, this block will be skipped during execution. The value
  entered in the 'Simulated Result' field will be treated as the block's output."
- **Logging:** "Log messages appear in the Logging panel while the flow is running (i.e.,
  in the \"LIVE\" state). The \"On Start\" configuration below applies just before the block
  begins execution. The \"On Completion\" configuration applies immediately after the block
  finishes execution, but before it moves on to its successor(s)."
  - *Trigger variant* (e.g. External Callback): "Log messages appear in the Logging panel
    while the flow is running (i.e., in the \"LIVE\" state). If the trigger condition rules
    out the trigger event, there will be no logging messages for the block."

Block-SPECIFIC help tooltips are captured per record under `docs.config[].help_tooltip`
or a `help_tooltips:` map.

### Universal input-mode toggle (Property/Value fields)

Any structured **Property/Value** field (Metadata, Filter, Call Flow input params, Return
Result properties — anywhere with key/value rows) carries a 2-icon mode toggle (`i.action-icon`,
just left of the field's `?`). It is **dual-mode**:

- **`fa-list`** (default/active) — tooltip *"Use Key/Value Pairs"*: enter discrete
  Property + Value rows.
- **`fa-minus`** — tooltip *"Use single input"*: switch the whole field to ONE expression
  value instead of rows (e.g. pass an existing object/map directly).

When documenting any such field, note both modes. (Records may set
`docs.config[].input_modes: [key_value, single]`.)

> ⚠ **Product gap to flag:** some help tooltips are unwritten placeholders showing the
> literal string **"TODO: Create a help text here"** (e.g. Repeat → *Current Iteration*).
> Where a record records that string, it means the product has no help text for that field
> yet — a doc/product-team action item, not our omission.

## Block config panel chrome (applies to every block)

The right-hand config panel has a fixed structure around each block's fields:

- **Header tabs:** *Blocks List* · *Block Configuration* (active) · *Flow Settings*.
- **Per-block actions:** *Run Block* (+ *Show Invocation History*), *Delete*.
- **Per-input expression wand** (lucide wand-sparkles, right edge of every input): opens the
  Expression Editor / switches the field to a dynamic expression.
- **Refresh** next to dropdown selectors (e.g. Flow on Call Flow / Scheduled Runs): reloads
  the list.
- **Input-mode toggle** (see above) on structured Property/Value fields — two visual forms:
  the `fa-list`/`fa-minus` pair ("Use Key/Value Pairs" / "Use single input") and a single
  `fa-toggle-on` ("Toggle single expression input").

Controls expose their tooltips two ways: native `title`/`aria-label` (tabs, actions) and
Radix hover tooltips (help `?`, refresh, input-mode toggles). The active tab/toggle suppresses
its own tooltip.

## Legends

**confidence** — V-run: from a real instance's runtime I/O · V-real: from a real flow's
definition/config · V-config: from the block's config panel / definition schema (not a
real run) · INFER: inferred only (must be upgraded before publishing).

**testability.class** — `deterministic`: engine/data/control-flow/Cloud Code; safe to
assert automatically · `external`: hits 3rd-party (OAuth/API) — only test via stubs ·
`partial`: deterministic core + external edges.

## Tooling primitives (for the eventual test runner / doc+training generators)
- Flow definition: `GET /api/app/<appId>/automation/flow/version/<versionId>`
  → `elements[]` (leaf) + `groups[]` (containers); wiring via `nextElementIds`,
  failure handler via `metaInfo.onFailElemId`, nesting via `element.groupId`.
- Run one block (unit test): `POST /api/app/<appId>/automation/flow/<flowId>/version/<vId>/debug/run/element/<elementId>`.
- Run a whole flow (E2E): instance run; inspect per-block Input/Output + execution
  counts in the instance analytics (see notes.md "Instance Analytics").
- Hermetic E2E: stub external blocks with **Skip Block → Simulated Result**.

## Required environment for the test suite (NOT the human's session)
A dedicated **test workspace** + a **non-interactive credential** (CallFlow API key /
service token). NEVER run the suite against LIVE production flows.

## Status
Exemplars done: custom-cloud-code, list-iterator. Remaining: convert the rest of the
verified blocks (see notes.md ledger) + capture the AI/integration family from Mark's
narration directly into this format.
