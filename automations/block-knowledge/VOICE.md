# Block Reference - Voice & Style

This spec governs the **authored prose fields** in the block-knowledge records
(`docs.purpose`, `docs.mental_model`, `docs.when_to_use`, `docs.example`) that the reference
generator renders. It **extends** `automations/CLAUDE.md` (terminology, formatting, tone) and
`automations/MKDOCS_GUIDE.md` (design system); it does not duplicate them.

The markdown in `content/reference/` is generated. Never hand-edit those files. Edit the YAML
records and regenerate (`make refgen`).

## Content standard (the bar)

These pages exist to **teach the substance**, not to look tidy. A page is not done until a
newcomer could read it and genuinely understand the block. That means:

- **Complete, not gestural.** Do not leave the main idea to the reader's imagination. If a
  block works on data, *show the data*. If it runs a condition, *show the actual condition*, not
  "a condition checks each item".
- **Concrete and worked.** Examples are real scenarios with real sample data (a JSON array, an
  actual expression, an actual value), carried all the way through. Use realistic field names
  and values, and reuse them across the page so they tell one coherent story.
- **Walked through, step by step.** For anything with moving parts, trace what happens against
  the sample data - pass 1 does X, pass 2 hits the condition and does Y - so there is nothing
  left to guess.
- **Illustrated - every block page is shown, not just told.** When we document a block, a
  screenshot is always helpful. **Every block page carries at least one screenshot that captures
  the block itself and its config panel in the same image** - the reader sees the block on the
  canvas and the fields they will fill in, together, in one shot. (Mark) **Complex / control-flow
  blocks** (loops, conditions, error handling, the Expression Editor, anything with moving parts to
  trace) get that base screenshot *plus* additional ones - the actual data, the Expression Editor,
  the traced passes - and one vague screenshot is not enough; show each part that matters. The base
  block+config image is the floor for every page; add more wherever a part genuinely needs showing.
- **Thoroughness beats brevity.** Never trade away the substance to keep a page short. A short
  page that does not educate is a failed page.
- **Lead with value, not mechanics - the stage you set.** The lede and How-it-works must make the
  reader *want* the block: open with what it lets them do that is worth doing, not a dry restatement
  of the request it sends. For a feature-rich block, name its standout capabilities up front - an AI
  Agent uses tools, searches Knowledge Bases, and remembers across runs, so the *intro* says that,
  not page two. Excitement comes from *concrete capability*, not adjectives: the banned-words rule
  (no "powerful/robust/seamless") still holds; you earn the energy by showing what it does. A weak,
  incomplete stage is a failed page even if every fact is present. (AI Agent review, Mark)
- **How it works explains, it does not catalogue.** Convey the model or the loop plainly and
  vividly. Do not drop to an implementation detail the user would never bring (e.g. how many requests
  a call makes under the hood), and do not open on a confusing framing. Each sentence should build
  understanding, not list a mechanic.
- **Flagship features get their own section.** A block's standout capability does not belong buried
  in a config-table cell. Give it a `docs.sections` entry (`{title, body, image?, alt?}`, rendered as
  its own `##` heading between When-to-use and the Example) and write it like the reason the block
  exists - because it is. (e.g. AI Agent's *Manage Capabilities*.) When a feature is too deep for one
  page, give it a whole **concept record** (`category: Concepts`, `concept: true`); the generator navs
  these into their own top-level **Concept Guides** section, *not* a Block Reference category - a concept
  guide is a different beast from a block. (Mark)
- **Never assume FlowRunner fluency mid-sentence.** A term a newcomer may not know (expression, Data
  Bucket, Instance) is a glossary term - write it in plain prose so its tooltip applies; do not use
  it cold or redefine it inline.
- **Screenshots must show a VALID, working config - never an error state.** Fill required fields so
  no red error badge shows; a placeholder value is fine (type "Demo API Key" into a key field). Build
  **every expression value in the Expression Editor** so it binds (a reference renders as a coloured
  pill); never paste an expression like `{{Initial Data->x}}` straight into the field - it does not
  bind, and the screenshot would show a config the reader literally cannot reproduce. If you cannot
  produce a clean config, do not ship the shot. (AI Agent review, Mark)

The `docs.example` field is a **sequence of steps** (each may carry `text`, `code`+`lang`,
and/or `image`+`alt`) precisely so a worked example can interleave narration, data, and visuals.
Beyond the example, a record may add **`docs.sections`** - a list of `{title, body, image?, alt?}`
custom sections rendered between *When to use it* and *Example* - to give a flagship feature its own
heading.

## Voice

- Beginner-first, conversational, precise. Address the reader as "you".
- The **lede** (`docs.purpose`) says what the block does in one or two plain sentences. No
  marketing, no restating the block name back at the reader.
- **How it works** (`docs.mental_model`) leads with what the block *is* and *how it works* - a
  concrete model, not a restatement of the lede. Do not open with limitations or what it cannot
  do; constraints belong in their own section. **Protect the core message.** This section teaches
  how *this* block works and nothing else. General, cross-cutting FlowRunner facts (property-access
  syntax like `->`, expression rules, common settings) are true but misplaced here - they dilute
  the one idea the section exists to land. Send them to their real home (the Expression Editor
  reference, the glossary) and link if needed. Each section has a single job; a true detail in the
  wrong section is a defect.
- **When to use it** (`docs.when_to_use`) frames the real decision, including trade-offs - often
  a block is the right choice because it is quicker or cleaner than wiring up several others, not
  only because nothing else can do the job.
- **Examples are instrumental** for code and complex blocks. Provide a worked `docs.example`
  (intro + code + outro) with realistic inputs and the returned result. Where a screenshot adds
  perspective (e.g. arguments bound to a prior block's result, then used in code), use a real
  product screenshot.
- Banned words/phrases: "simply", "just", "powerful", "robust", "seamless", "easy".

## Formatting rules

- **No em-dashes (—).** Use a regular hyphen, a spaced hyphen " - ", or restructure the sentence.
- **Reference hierarchy - apply consistently:**
  - **Block names** (HTTP Request, Transform Data, Break, ...) render as styled tokens: the
    generator wraps every mention in `.fr-block` (a subtle green pill) so block references stand
    out from copy, and links the first mention of each *other* block to its reference page. Do not
    hand-format block names - write them in plain prose and let the generator style and link them.
  - **Concept terms** a newcomer may not know (Shared Memory, Data Bucket, Instance, Initial Data,
    Expression Editor, ...) are grounded by glossary tooltips: define them once in
    `snippets/includes/abbreviations.md` and every page shows a hover definition automatically. Add
    a definition the first time the batch introduces a new term; do not redefine inline.
  - **Named system values / Expression Editor pills** (`Current Iteration Item`, `Simulated
    Result`, ...) take `code` backticks - they are concrete named values the user sees in the UI.
  - **UI labels, buttons, sections** take **bold** (per CLAUDE.md).
  - **Ordinary keywords** in prose (return, async, await) get **no** formatting. Reserve code
    backticks otherwise for code shown in code blocks. Never format one code token while leaving
    a sibling plain.
- **Do not imply linear execution.** FlowRunner flows can branch and run steps in parallel, so
  avoid "in order", "one at a time", "then ... then" framing that paints a flow as a straight line.
- No `->` arrows as **prose shorthand** for flow or navigation ("Start leads to a Condition", not
  "Start -> Condition"); write it out. This is separate from the literal `->` **property-access
  operator** in expressions, which is real product syntax and stays in `code` (e.g.
  `Current Iteration Item->status`). Keep `->` out of image `alt` text, where it reads as "arrow".

## Defined terms (link to the glossary, do not redefine inline)

- **block container** - a block that holds other blocks inside it and runs them (List Iterator,
  Repeat, the Trigger/Action groups). The glossary defines the shared UX (step in to edit, etc.).
- `Current Iteration Item`, **Break**, and other product terms are defined once in the glossary.

## Page anatomy (rendered by the generator)

Section order, each separated by a blank line:
`lede → How it works → When to use it → Example → Configuration → Behavior → Limitations (or
Things to watch for) → Related`.

- **Configuration** table is `Field | Type | Description` - no Required column. A required field
  gets a leading "Required." in its Description; the field's help tooltip is folded into the
  Description.
- **Limitations** (`docs.limitations`) is the home for hard constraints. If a record has no
  `limitations`, the softer `docs.gotchas` render under "Things to watch for" instead.

## Calibration log

Generalizable rules extracted from review feedback, newest first.

### 2026-06-18 - AI Agent (cluster + flagship depth)
- **A flagship block can spawn a cluster of concept sub-articles.** When a feature is too deep for one
  page (AI Agent's flows-as-tools, Flow Memory), give it its own `*-concept.yaml` record
  (`category: Concepts`, `concept: true`) - it auto-loads and auto-navs through the same pipeline, the
  way Knowledge Bases and Flow Scheduling already do. The block page keeps the short version + an inline
  link; the sub-article details and shows it. (Mark)
- **Get the result shape exactly right.** An AI Agent's reply always arrives under an `output` property
  on the result (`output`, or `output->field` with Force Parsed Output); reading the result directly
  gets nothing. A wrong reference path on an example is a content defect - confirm the result shape, do
  not infer it. (Mark)
- **Trace where state physically lives.** Flow Memory (the agent's Messages History) is persisted in
  Shared Memory, so a Shared Memory: Delete with All on wipes it. When one feature is backed by another,
  document the link on BOTH pages (the warning belongs on Shared Memory: Delete too). (Mark)
- **Do not invent UI mechanics to fill a sub-article.** Where the exact UI (e.g. where flow/argument
  descriptions are entered) is not yet verified in-product, write the confirmed concept and park the
  screen specifics + screenshots for a capture pass - never fabricate a menu path. (carries the List
  Iterator "verify in-app" rule into concept pages.)
- **Multi-paragraph prose fields MUST use a literal block scalar (`|`), not folded (`>`).** YAML's
  folded `>` collapses the blank line between paragraphs to a single newline, so the whole field renders
  as one wall of text and a footnote definition loses its required blank line and breaks. Use `|` (with
  real blank lines between paragraphs) for any `mental_model`/section body that has more than one
  paragraph or a footnote; `>` is fine only for a single-paragraph field. (Pre-existing multi-paragraph
  `>` fields, e.g. flow-scheduling-concept, want the same fix in the Phase B sweep.)
- **Footnotes are available** (the `footnotes` extension is enabled): use `text[^id]` + a `[^id]:`
  definition line for caveats that would clutter the sentence (e.g. "waits for days[^plan]" → a note
  that prolonged waits depend on the pricing plan).

### 2026-06-16 - List Iterator (accumulation idiom + connectivity)
- **Blocks cannot hang disconnected.** Every block must sit on the connected path from Start; a
  dropped-but-unwired block is invalid, not just untidy. Only Action and Trigger *group members*
  may stand alone. When scripting the product, a node that does not wire in is an error to fix. (Mark)
- **Accumulating into a list is not "Set Variables append".** The idiom: declare a list variable
  *outside* the loop and seed it with the **Empty List** value, then *inside* use a **Transform
  Data** block with the **Add To List** operation, writing the result back to the same variable.
  Document this precisely - guessing a mechanism (e.g. Set Variables concatenation) is a content
  defect. (Mark) Verify product mechanics in-app before writing them.

### 2026-06-16 - List Iterator (property-access syntax)
- FlowRunner expressions read a **top-level** property with `->` and a **nested** property below
  that with a dot: `Current Iteration Item->status`, and `Current Iteration Item->customer.region`
  if `customer` is itself an object. The dot-only form (`Current Iteration Item.status`) is wrong.
  Document this; it is confusing but real. (Mark) Belongs in the Expression Editor reference too.
- A literal array typed into a field is treated as a **string** until the Expression Editor's
  **As JSON** toggle is on; only then is it structured data the loop can iterate and index. (Mark)
- `->` renders as a distinct structured pill (arrow icon) in field and Live Preview; `.status`
  stays unresolved raw text. Screenshots of references must use the `->` form. (Mark)

### 2026-06-16 - List Iterator (second calibration block)
- Use the term "block container", not just "container", for blocks that hold inner blocks; it is
  a glossary term. (Mark)
- Dropped "in order": flows are not linear (branches can run in parallel). (Mark)
- `Current Iteration Item` is a named system value (a pill in the Expression Editor) - backtick
  it. Refines the "no backticking keywords" rule: keywords plain, named system values backticked. (Mark)
- Concepts a reader may not know (e.g. `Current Iteration Item`) want a screenshot to ground them. (Mark)
- The Break block was missing - loops can be exited early with Break; document it and cross-link. (Mark)
- "shape it with Transform Data" did not explain how a value leaves a loop; results leave by being
  accumulated into a Data Bucket / Shared Memory, then read after the loop. (Mark)

### 2026-06-16 - Custom Cloud Code (first calibration block)
- No em-dashes anywhere; regular dashes only. (Mark)
- Stop backticking lone keywords like return when sibling code tokens are left plain; be
  consistent. (Mark)
- "How it works" was leading with limitations ("can't reach the outside world, not Node"). Lead
  with what it is and how it runs; move constraints to a Limitations section. (Mark)
- "When to use it" framed only as "when no block covers it". Add the real trade-off: code is
  often quicker/cleaner than a chain of Transform Data blocks. (Mark)
- Add worked Examples for code/complex blocks (code now; real screenshots where they help). (Mark)
- Generator fixes from this round: blank-line separation between all sections (a table was
  swallowing the next heading); dropped the empty/irrelevant Required column.
