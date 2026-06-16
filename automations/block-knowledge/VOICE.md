# Block Reference — Voice & Style

This spec governs the **authored prose fields** in the block-knowledge records
(`docs.purpose`, `docs.mental_model`, `docs.when_to_use`) that the reference
generator renders. It **extends** `automations/CLAUDE.md` (terminology, formatting,
tone) and `automations/MKDOCS_GUIDE.md` (design system) — it does not duplicate them.

The markdown in `content/reference/` is generated. Never hand-edit those files.
Edit the YAML records and regenerate (`make refgen`).

## Voice (seed — refined during calibration)

- Beginner-first, conversational, precise. Address the reader as "you".
- The **lede** (`docs.purpose`) says what the block does in one or two plain sentences.
  No marketing ("powerful", "seamless"), no restating the block name back at the reader.
- The **mental model** gives a concrete analogy or framing — not a restatement of the lede.
- **When to use it** is about the decision: when to reach for this block vs. a neighbour.
- Banned words/phrases: "simply", "just", "powerful", "robust", "seamless", "easy".

## Calibration log

(Generalizable rules extracted from review feedback land here, newest first.)
