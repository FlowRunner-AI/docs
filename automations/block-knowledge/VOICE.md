# Block Reference - Voice & Style

This spec governs the **authored prose fields** in the block-knowledge records
(`docs.purpose`, `docs.mental_model`, `docs.when_to_use`, `docs.example`) that the reference
generator renders. It **extends** `automations/CLAUDE.md` (terminology, formatting, tone) and
`automations/MKDOCS_GUIDE.md` (design system); it does not duplicate them.

The markdown in `content/reference/` is generated. Never hand-edit those files. Edit the YAML
records and regenerate (`make refgen`).

## Voice

- Beginner-first, conversational, precise. Address the reader as "you".
- The **lede** (`docs.purpose`) says what the block does in one or two plain sentences. No
  marketing, no restating the block name back at the reader.
- **How it works** (`docs.mental_model`) leads with what the block *is* and *how it works* - a
  concrete model, not a restatement of the lede. Do not open with limitations or what it cannot
  do; constraints belong in their own section.
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
- **Inline code is for code, used consistently.** Do not wrap ordinary English keywords (return,
  async, await) in backticks inside narrative prose. Reserve `code` formatting for code shown in
  code blocks and for literal identifiers/values when genuinely needed - and never format one
  code token while leaving a sibling token plain. Use **bold** for UI labels and field names
  (per CLAUDE.md).
- No `->` arrows or terse note shorthand in rendered prose or bullets; write it out.

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
