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
- **Illustrated.** Use screenshots of the real product (the actual config, the actual data, the
  Expression Editor) to show *where things are, what they look like, and how they work*. One
  vague screenshot is not enough; show each part that matters.
- **Thoroughness beats brevity.** Never trade away the substance to keep a page short. A short
  page that does not educate is a failed page.

The `docs.example` field is a **sequence of steps** (each may carry `text`, `code`+`lang`,
and/or `image`+`alt`) precisely so a worked example can interleave narration, data, and visuals.

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
  - **Block names** (HTTP Request, Transform Data, Break, ...) are **links** to their reference
    pages. The generator links the first prose mention automatically; do not hand-format them.
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
