# BUILD Section Plan

Plan for authoring the **Build** nav section, grounded in a review of the 20 legacy
`content/flow-editing/` files and a 27-block sweep of the Block Reference. Developed 2026-07-07;
restructured 2026-07-09 after Mark's three corrections (reader's worldview first; section/page
split; questions, never comparisons). The BUILD content is **empty stubs** — greenfield authoring;
nothing to preserve.

**Structure: 22 files — 3 single pages, 3 sections (index + children).**

## Organizing axis (reader's worldview first)

**Two levels, both reader-side (CONCEPT-PAGE-PATTERN §0i; memory `docs-reader-worldview-first`):**

1. **A nav SECTION mirrors one coherent region of the reader's worldview.** The reader arrives to
   fix a specific problem and to map the model already in their head — how decisions get made, how
   information flows, repetition, waiting, failure — onto how FlowRunner runs. "Flow Control" is a
   section because real-world decision-making + information flow is one chunk of that model.
2. **A PAGE answers ONE reader question** ("How do I loop?") at the scale of the approved
   exemplars (~50–75 lines / 3–6 shots — Variables, Expressions, Subflows). A page that needs h4s
   or folds several questions splits. The section's short index page carries the map: which page
   answers which question, plus routes for questions whose answer lives elsewhere. Coherence comes
   from adjacency + the map, never concatenation.

**Framing rule:** maps, page names, and prose are the reader's QUESTIONS routed to the right tool —
never "X vs Y" block comparisons. The reader doesn't know two blocks exist; the question framing
itself does the routing. Overlapping blocks answer different questions and compose, not compete.

The three-layer altitude table below is **machinery** that keeps BUILD task-thin (link out; don't
re-teach a concept or catalogue a block) — it is NOT why pages are carved as they are.

| Layer | Question it answers | Unit |
| --- | ----- | ----- |
| **Core Concepts** (Platform) | "What *is* this and how does it behave?" | one concept |
| **Block Reference** | "What are *this block's* fields, options, envelope, gotchas?" | one block |
| **BUILD** (this section) | **"How do I actually do X?"** | ONE reader question per page |

BUILD is task-oriented, verb-first — the cookbook layer. It links out (green `.fr-block` pills /
glossary terms) and shows the reader *doing the job*. Every BUILD page: opens on the builder's
outcome (pattern §0/§3), carries one running worked example with real names, SHOWS each named
surface with a real screenshot, and re-verifies every product specific in-product. **Legacy is the
SUBSTANCE base for BUILD** (Mark, 2026-07-09: "most of the content for BUILD was previously
written; some of it may be outdated") — reuse the legacy content, verify what's outdated against
the current product, and match the plain house delivery style (`dataflow.md`,
`snippets/errorhandling.md`; the plain-style pre-handoff check in STANDING-RULES.md). BUILD pages
are narrative, so the `concept-page-review` gate + per-paragraph quality bar apply.

**Legacy terminology drift to purge:** "Backendless" → FlowRunner/Midnight Coders; "sub-flow" (the
Repeat container) collides with the Subflows feature — say "the blocks inside the Repeat"; "CallFlow
API" → Call Flow; "AI Assistants" → AI Agent; "Transformer" → Transform Data; and legacy frames
flows as starting with a trigger (a prime-directive violation — a flow starts with anything).

## Table of contents (what the left nav will show)

Section labels are clickable — they ARE the index pages (`navigation.indexes`, already enabled).
Each entry annotated with the reader question it answers.

```
Build
│
├─ The Flow Editor                        build/flow-editor.md
│     "I'm on the canvas — how do I place, connect, configure, arrange blocks?"
│
├─ Data & Variables                       build/data-and-variables/index.md
│  │   (index = the map: how information moves through a flow; routes per-user memory,
│  │    Expression Editor concept, loop-scope questions → the loop pages)
│  ├─ Passing Data Between Blocks         passing-data.md
│  │     "How do I use one block's output in another block?"
│  ├─ Holding Values in Variables         holding-values.md
│  │     "How do I keep a value to use later in the run?"
│  ├─ Reshaping Data                      reshaping-data.md
│  │     "The data isn't the shape I need — how do I change it?" (Transform Data;
│  │      when it outgrows the ops → Custom Cloud Code)
│  └─ Sharing Data Across Runs & Flows    across-runs.md
│        "How do I keep data between runs / share it between flows?" (Shared Memory)
│
├─ Flow Control                           build/flow-control/index.md
│  │   (index = the map: real-world decision-making & information flow onto FlowRunner;
│  │    routes meaning→AI Router, scheduled time→Scheduling)
│  ├─ Yes/No Branching                           branching.md
│  │     "How do I make the flow act differently based on a check?" (Condition)
│  ├─ Routing on a Value                  routing.md
│  │     "How do I send the flow down one of several paths based on a value?" (Value Router)
│  ├─ Repeating Steps                     repeating.md
│  │     "How do I do something N times / until a condition? How do I poll?" (Repeat)
│  ├─ Working Through a List              collections.md
│  │     "How do I process each item in a list? Collect the results?" (List Iterator)
│  ├─ Running Steps in Parallel           parallel.md
│  │     "How do I run steps at the same time — and continue when all are done?"
│  │      (Actions Group, Synchronize)
│  ├─ Waiting                             waiting.md
│  │     "How do I pause for time, wait for an event, or wait for an outside
│  │      system/approval?" (Wait, Triggers Group, External Callback — split-check)
│  └─ Handling Errors                     error-handling.md
│        "How do I recover when a step fails? Retry? Know what went wrong?" (Handle Error)
│
├─ AI in Flows                            build/ai-in-flows.md
│     "How do I put AI to work — run an agent, route by meaning, judge an image,
│      maintain a knowledge base?" (single page; split-check at planning time)
│
├─ Integrations & I/O                     build/integrations/index.md
│  │   (index = the map: getting data in and out; routes forms→Forms,
│  │    inbound starts→Running Flows/Triggers, secrets→OAuth/AI Keys)
│  ├─ Calling an External Service         calling-a-service.md
│  │     "How do I call an API — and authenticate the call?" (HTTP Request + OAuth)
│  ├─ Returning a Result                  returning-a-result.md
│  │     "How do I send an answer back to whoever started the flow?" (Return Result)
│  ├─ Running Another Flow                running-another-flow.md
│  │     "How do I start another flow from this one?" (Call Flow)
│  ├─ Generating Documents                generating-documents.md   [pending PDF verify]
│  │     "How do I produce a PDF/document from flow data?"
│  └─ Custom & Marketplace Actions        custom-actions.md
│        "The block I need doesn't exist — now what?" (pointer to Extend + Marketplace)
│
└─ Managing Flows                         build/managing-flows.md
      "How do I keep a growing flow organized — reuse steps, group, name, version?"
```

Findability check: a reader scanning the nav for "wait", "list", "variables", "errors",
"parallel", or "service" finds their own word.

## Per-unit plan

### 1. `build/flow-editor.md` — "The Flow Editor" (single page)
**SCOPE RULING (Mark, 2026-07-24): the guided first-flow build belongs to QUICK START, not here.**
`content/learn/quickstart.md` is a stub and is queued for later; when written it is the step-by-step
"build your first flow" walkthrough and can reuse the verified `Order Check` example and its screenshots.
This page stays the editor's **mechanics reference** - organisation as-is - and must not be turned into a
tutorial. Do not re-litigate this.

Reader's question: "I'm in the canvas — how do I place, connect, name, configure, arrange blocks?"
Outline: lede (assembling real logic on the canvas) → canvas & palette (Triggers/Actions/Groups/Utils, search, Marketplace) → placing a block (Start; a flow can start with anything) → connecting (transitions, parallel successors, convergence) → configuring (settings panel; static vs Expression Editor) → naming for clarity → arranging/readability → editor controls (Auto Save, Test Mode).
Source: `floweditor.md`, `workingwithblocks.md`, `blocknaming.md`. KEEP connect/successor mechanics + naming guidance. REWRITE Backendless→FlowRunner; re-verify control bar; replace Arcade demos with fresh shots. DROP marketing throat-clearing. Link (don't duplicate): Blocks concept, Expression Editor concept, Testing.
Length-forecast check at planning time — it's an orientation read (one working surface), so a
single page is expected to hold; split if it exceeds exemplar scale.

### 2. `build/data-and-variables/` — "Data & Variables" (section: index + 4)
Worldview chunk: how information moves through a flow.
- **index.md** — the map, question-framed: use one block's output → Passing Data Between Blocks;
  keep a value for later in the run → Holding Values in Variables; wrong shape → Reshaping Data;
  keep it between runs / share between flows → Sharing Data Across Runs & Flows. Cross-routes:
  building values/expressions → Expression Editor concept; remember PER USER → Per-User Memory
  concept; "my value disappears outside the loop" → Repeating Steps / Working Through a List.
- **passing-data.md** — the result→input thread: the alias, picking a result in the Expression
  Editor, walking into fields. Source: `dataflow.md` (KEEP its threading narrative + plain style).
- **holding-values.md** — Set Variables; when a variable earns its place. Thin; links Variables &
  Data Buckets concept + Set Variables reference. Source: lightly `variables.md`.
- **reshaping-data.md** — Transform Data worked example (link reference for the op catalogue);
  when the reshaping outgrows the ops → Custom Cloud Code (arguments in, returned value out —
  scale-check whether CCC needs its own child page). Source: `transformer.md` + CCC from
  in-product/YAML. DROP the operators/Common-Values/Flow-Context catalogues (Expression Editor
  concept owns those).
- **across-runs.md** — Shared Memory Put/Read/Delete for cross-run and cross-flow data; links the
  Shared Memory concept. Routes Per-User Memory.

### 3. `build/flow-control/` — "Flow Control" (section: index + 7; highest value, heaviest verification)
Worldview chunk: how decisions get made and how information flows — mapped onto FlowRunner.
- **index.md** — the map, question-framed (see ToC). Cross-routes: route on MEANING/free text →
  AI Router (AI in Flows); run at a scheduled TIME → Scheduling (Run & Monitor).
- **branching.md** — Condition: single check (value/type/operation), multi-part AND/OR,
  parentheses/evaluation priority (Mark 2026-07-09: complex conditions are IN scope here), Yes/No
  paths, trigger filter conditions (settled: short section on this page). Routes: AI yes/no about
  an image → the IMAGE operation (with AI in Flows); more than two outcomes → Routing on a Value.
  Source: `conditions.md` (KEEP the task slice; the datatype-operation tables belong to the
  Condition **reference**). Lesson plan approved path: ~/.claude/plans/docs-lesson-flow-control-branching.md.
- **routing.md** — Value Router: Single/Collection/Range + Everything Else. Routes meaning-based
  routing → AI Router. Source: `valuerouter.md`.
- **repeating.md** — Repeat: N times / until; the polling pattern (Repeat + Wait + Condition);
  Break ("stop early") in context; getting a value out of the loop (variable elevation). Source:
  `loops.md` + in-product.
- **collections.md** — List Iterator: per-item work, the accumulation idiom ("collect results"),
  Break in context, value elevation out of the loop. NO legacy source — author from in-product.
- **parallel.md** — Actions Group (On Start/On Completion), Synchronize ("continue when all
  branches are done" — NO legacy source for Synchronize). Source: `grouping-actions.md`.
- **waiting.md** — pause for a duration/until a time (Wait); wait for whichever of several events
  (Triggers Group); wait for an outside system / human approval — resume via External Callback's
  Callback URL. Routes "run the whole flow on a timetable" → Scheduling. Source: `waitblock.md`,
  `grouping-triggers.md`, External Callback YAML/in-product. **Split-check at page-plan time**:
  time-based vs outside-system may be two questions → two pages.
- **error-handling.md** — Handle Error: wiring it, reading code/message/source, fallback paths,
  the retry pattern (verify in-product what retry actually looks like). Links the Error Handling
  concept guide (philosophy) and Handle Error reference (fields). Source: `error-handling.md`
  (snippet shell → `snippets/errorhandling.md`).
Exercise every mode/toggle (pattern §0g). Each child gets its own running example.

### 4. `build/ai-in-flows.md` — "AI in Flows" — ✅ SHIPPED 2026-08-06 (this outline was STALE; superseded by the approved lesson plan + Mark's interview)
Reader's question: "How do I put AI to work in a flow?" — answered as a single teaching page + map
(Mark's role call). Actual shape: lede (axis: how much of the job the model gets) → model + key
prerequisite → AI Transform (Transform Data operation) → ready-made extension AI actions →
AI QUESTION (Condition operation, every data type; Condition reference got a companion section) →
AI Router → AI Agent → page-level Related. Corrections to this outline, verified in-product:
the Condition "IMAGE operation" is legacy-gone (the modern surface is per-type AI QUESTION);
Moderate Content / Speech to Text / Text to Speech are OpenAI/ElevenLabs EXTENSION actions, not
native blocks (covered by the ready-made-actions section); KB maintenance stays with the KB
concept guide + the four block references. Evidence: PLATFORM-REVIEW-LEDGER "AI in Flows" +
docs-review/verdicts/ai-in-flows.md.

### 5. `build/integrations/` — "Integrations & I/O" (section: index + 5)
Worldview chunk: getting data in and out of a flow.
- **index.md** — the map, question-framed (see ToC). Cross-routes: collect user input → Forms
  (Platform); start my flow from my app / receive a webhook → Running Flows + Triggers concept;
  secrets/auth → OAuth Connections, AI API Keys.
- **calling-a-service.md** — HTTP Request + authenticating via OAuth Connections. NO dedicated
  legacy file — author from in-product + reference.
- **returning-a-result.md** — Return Result; single result and multiple Return Results. Source:
  `return-result.md`. Envelope detail stays in the reference.
- **running-another-flow.md** — Call Flow; question-framed (reuse *within* one flow routes to
  Subflows via the map, not a comparison). NO dedicated legacy file.
- **generating-documents.md** — PDF Generator (**verify it still exists first**). Source:
  `pdf-generator.md`; relocate the deep PDF Template Editor walkthrough (may be its own how-to).
- **custom-actions.md** — pointer page to Extend + Marketplace. Source: `custom-actions.md`.
Real-time UI (`communicate-with-ui.md` is Backendless-UI-specific) — product-owner decision
pending; add a child only if it survives.

### 6. `build/managing-flows.md` — "Managing Flows" (single page; settle the Manage/Run boundary first)
Reader's question: "How do I keep a growing flow organized?"
Outline: lede → reusing a sequence with a Subflow (link Subflows concept + SubFlow reference) →
grouping for readability (Actions Group's organizational face) → documenting (Notes) →
versioning & lifecycle (verify; may overlap Run & Monitor).
Source: `subflows.md` (strongest legacy file), LIVE/analytics caveat from `floweditor.md`.
Trim the result-envelope section to a pointer (Return Result reference owns it).
**BOUNDARY (Mark, 2026-07-24): naming AND arranging blocks belong to `flow-editor.md`, not here** — so
`blocknaming.md` maps to the editor page only, and this page must not re-teach renaming or canvas layout.
What stays here is organizing a *grown* flow: extracting a Subflow, grouping, Notes, versioning.
Keep strictly to build-time organization of one flow; runtime → Run & Monitor.

## Block coverage (27-block sweep, 2026-07-09 — every block has a home or an explicit route)
- AI Agent, AI Router, Moderate Content, Speech to Text, Text To Speech → ai-in-flows
- KB Add/Delete/Delete-by-Filter/List → ai-in-flows (maintaining a knowledge base)
- HTTP Request → calling-a-service; Return Result → returning-a-result; Call Flow → running-another-flow
- Custom Cloud Code → reshaping-data (YAML-verified as data work; no network access)
- Set Variables → holding-values; Transform Data → reshaping-data; Shared Memory ×3 → across-runs
- Condition → branching; Value Router → routing; Repeat → repeating; List Iterator → collections;
  Break → repeating + collections (in context); Actions Group → parallel (+ its organizational
  face in managing-flows); Synchronize → parallel; Wait + Triggers Group + External Callback → waiting
- Handle Error → error-handling; SubFlow → managing-flows
- Assign Instance Name → Run & Monitor → Monitoring (route note — not BUILD; don't orphan it)
- Start/Stop Scheduled Runs → Run & Monitor → Scheduling + Flow Scheduling concept (not BUILD)

## Legacy → destination mapping (summary)
- flow-editor ← `floweditor.md`, `workingwithblocks.md`, `blocknaming.md`
- data-and-variables/* ← `dataflow.md`, `transformer.md`, (thin) `variables.md`, `expressioneditor.md`
- flow-control/* ← `conditions.md`, `valuerouter.md`, `loops.md`, `grouping-actions.md`, `grouping-triggers.md`, `waitblock.md`, `error-handling.md`
- ai-in-flows ← `using-ai.md` (skeleton only; re-author)
- integrations/* ← `pdf-generator.md`, `custom-actions.md`, `communicate-with-ui.md`, `return-result.md`
- managing-flows ← `subflows.md`, `blocknaming.md`

## Gaps (need fresh in-product authoring — no legacy narrative)
- `List Iterator`, `Synchronize`, `Break` — collections.md / parallel.md / loop pages.
- `HTTP Request`, `Call Flow` — calling-a-service.md / running-another-flow.md.
- `External Callback` as mid-flow wait/resume — waiting.md.
- `Custom Cloud Code` in the reshaping story — reshaping-data.md.
- The modern AI surface (AI Agent, Moderate Content, Speech-to-Text/Text-to-Speech, Knowledge
  Bases, MCP Servers, Per-User Memory) — all post-date `using-ai.md`.

## Open verifications & placement decisions (settle before/at page-plan time)
1. managing-flows vs the top-level **Manage** section vs **Run & Monitor** (versioning/lifecycle placement).
2. Whether the PDF Template Editor deep-dive and the real-time UI recipe still ship / belong in BUILD.
3. How much AI belongs in BUILD vs AI reference vs AI concept guides.
4. waiting.md split-check: time-based vs outside-system (two questions → two pages?).
5. reshaping-data.md split-check: does Custom Cloud Code need its own child?
6. The retry-after-failure pattern — verify in-product what it actually looks like.
7. "How do I end a run early?" — open in-product question (what IS the answer?).
8. Trigger filter conditions — branching.md vs Triggers concept.
9. Assign Instance Name lands in Run & Monitor → Monitoring (record there so it isn't dropped).

## Recommended sequencing
1. **flow-control/** (highest value + richest source; heaviest verification — budget for it) →
2. **flow-editor** (foundational orientation) →
3. **data-and-variables/** (write after flow-editor) →
4. **managing-flows** (settle Manage/Run boundary first) →
5. **integrations/** (needs a scoping pass) →
6. **ai-in-flows** (thinnest source; write last, after AI reference/concept pages stabilize).

Within a section: index LAST (the map is written after the pages it maps exist).

Verification-heaviest: flow-control/*, data-and-variables/*, ai-in-flows — biggest
product-exploration logs + product-owner checkpoints.
