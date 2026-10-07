# Docs standing rules — read at the start of every docs session

Printed by the SessionStart hook so the process is always in context. **Done is not your
judgment and it is not the gate's `ship` verdict either — it is MARK'S sign-off.** The gate
mirrors your blind spots; treat it as a net, never the bar.

## Part 0 — the durable fix (how you work; read this first)
1. **You are NOT the quality authority — Mark is. Stop asserting quality.** Never say "done / ready /
   good / so good now." Every handoff is exactly three things: (a) what you changed, (b) what you
   EXERCISED in-product with evidence, (c) each gate finding and how you resolved it. Then let Mark judge.
2. **Exercise before you write, and LOG it.** No sentence about any control (toggle, dropdown, mode) until
   you have driven EVERY one of its states in the live product and recorded what each does, in a per-page
   product-exploration HTML comment. "I saw one screenshot" is not "I understand the feature" (Return Result).
3. **Run a red-team lens every review** — one whose only job is to find a failure class NOT on the checklist
   ("assume this list is incomplete; what would Mark catch that no lens here covers?"). New classes become rules.
4. **Principle-first correction capture.** When Mark corrects you, restate the GENERAL principle in one line
   and let him confirm it before you encode anything — so you stop shipping rules shaped like the one instance.

## The four failures this system exists to stop
1. **Not thinking like an educator** — mechanics-first, burying the idea. → `/docs-plan`.
2. **Not following the guidelines** — the rules exist; you skip them. → the reviewer's guideline lens.
3. **Thinking you are done when you are not** — self-certifying on "doclint 0/0 / files exist". → `/docs-review` verdict.
4. **Not updating the guidelines from Mark's feedback** — a fix without a distilled rule. → `/docs-feedback`.

## The loop (never shortcut it)
`/docs-plan <page>` → write, **verifying every product claim in-product** as you go →
`/docs-review <page>` until the verdict is `ship` (you clear every work-list item yourself
— including driving the product to confirm claims; you do the work, not Mark) → hand to
Mark (a row appears in AWAITING-REVIEW only with a recorded `ship` verdict) → Mark reviews →
`/docs-feedback <page>` (apply fixes + **distill generalizable rules into the guidelines** +
update the ledger) → `/docs-review` re-confirms.

## Hard rules
- **Mark reads ONE file: `docs-review/FOR-MARK.md`.** (Mark, 2026-10-06: verdicts/ is "unworkable".) Verdicts,
  ledgers and triage tables are my working notes; never send him to them, never show him gate labels. FOR-MARK.md
  holds numbered self-contained decisions, what is waiting on him, what I'll do by default, and one plain line per
  page that misleads readers today. Keep it current; delete answered items.
- **Verify in the environment Mark names.** (Mark, 2026-10-06: "I told you everything is available in prod".) If
  that environment is signed out, ask for the sign-in FIRST, in one line - never quietly drive another
  environment and hand back a list of "owed" checks.
- **Teach VALUE; never narrate the screen.** (Mark's 2/10 Monitoring review, 2026-07-14.) A reader can see the
  UI already - documentation earns its place only by teaching what a thing is FOR: the question it answers, when
  you'd reach for it, what you learn from it, what action it drives. Before a sentence ships, ask "what does the
  reader DO with this?" - if it only restates what's on screen ("this is an apple, it is a fruit"), cut or rewrite
  it. EXERCISE every interactive control (checkboxes, clicking a chart element, filters, selectors) and document
  what it DOES - never skip one and describe only the static view. Don't name the demo flow unless it matters to
  the reader. Say "workspace billing plan", not vague "your plan". Cut filler cross-refs ("covered under X") and
  empty phrases that carry no information. See memory docs-teach-value-not-narrate.
- **Write PLAIN; run the plain-style pre-handoff check before EVERY handoff.** The ~20-round beat-down of
  2026-07-09 (Agent Memory / Error Handling / Flow Scheduling) was one failure: I drafted in a flourishy,
  "sophisticated" register and left Mark to catch it. Match the plain house style already in the repo — the
  legacy `content/flow-editing/dataflow.md` and `snippets/errorhandling.md` (plain declaratives; a bulleted
  list for any set of fields/options; one screenshot per point) and the approved exemplars (Variables,
  Expression Editor). Do NOT out-write it. Before handing over, fix every hit of the **plain-style check**
  (mostly greppable — see VOICE.md Calibration Log 2026-07-09): no contrast/"clever" constructions
  (`not X but Y`, `rather than a`, `the difference between X and Y`, `worth dwelling on`, cute closes); no
  metaphors; no unresolved back-references (`the same way you saw above`); 3+ items → a bulleted list; every
  named control/location gets a screenshot or a stated location; short declaratives; no incidental over-naming;
  don't imply a specific block is required for a generic action. Mark: "I do not need a Leo Tolstoy writing
  FlowRunner docs."
- **NEVER tell Mark a page is "done"/"ready" without a `ship` verdict in `docs-review/verdicts/<page>.md`.**
  "doclint is clean" and "the files exist" are NOT done. **FORCING CHECK — before you type "take a look" /
  "ready" / "have a look" / any handoff phrasing, open `docs-review/verdicts/` and confirm a FRESH verdict for
  THIS page exists. If it does not, the `concept-page-review` gate has not run — STOP and run it, clear every
  blocker/major yourself, then hand over.** (2026-07-09: handed Mark all three concept guides — Flow Scheduling,
  Agent Memory, Error Handling — with ZERO verdicts on disk. The rule was already written, right here. I skipped
  it and made Mark the reviewer of last resort. Do not do this again.)
- **The gate is a ONE-TIME net per revision, NOT a loop.** Run `concept-page-review` ONCE to surface blind
  spots; fix the substantive findings (blockers + real majors + verify-in-product) in ONE consolidated
  root-cause pass — lock the page's single running example FIRST, verify open facts up front, fix whole
  classes not line-items — then hand to Mark, who decides ship. **Never re-run the gate to chase a clean
  verdict.** An adversarial exemplar reviewer is stochastic and never returns zero findings; re-running it
  is the token-burning loop Mark called out (2026-07-09). Subjective prose-craft is Mark's call, not a
  ship-blocking gate lens — the craft lens flags only genuinely weak passages, and a clear, competent page
  passes it. (A single optional re-run as a REGRESSION net is fine only if Mark asks.)
- **Every UI/behavior/location claim is verified in the live product before you write it.** Never guess
  where a control lives. Capture screenshots FRESH. The product is the only source of truth.
- **Show every main documented concept** with a real shot of its real scenario.
- **A flow can start with anything, not just a trigger.** Never frame the start as trigger-based.
- **Every correction Mark gives becomes a written rule in the same turn** (CONCEPT-PAGE-PATTERN §0d and/or
  VOICE.md, plus a memory if recurring) — a one-off fix without a distilled rule is an incomplete response.
- **Update `AWAITING-REVIEW.md` and `PLATFORM-REVIEW-LEDGER.md` as you go**, not as an afterthought.

## The rubric (what the reviewer and you are held to)
- `docs-review/CONCEPT-PAGE-PATTERN.md` — the educator method + §0d recurring corrections.
- `block-knowledge/VOICE.md` — voice, screenshots, formatting, the Calibration Log.
- `tools/doclint/DEFINITION_OF_DONE.md` — the automated vs. adversarial gate list.
- `docs-review/PLATFORM-REVIEW-LEDGER.md` — the binding, evidenced definition of done, per page.

The reviewer reads these live, so distilling a correction into them immediately raises the bar.
