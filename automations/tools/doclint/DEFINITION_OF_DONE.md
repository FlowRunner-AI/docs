# Definition of Done — a page is not "done" (and is NOT reported done) until every box is checked

This exists because the failure was never a missing rule. It was that nothing between
"drafted" and "done" could fail. These boxes are that failing step. Half are checked by
the `doclint` gate (automated, build-breaking); half need a human/adversarial pass. A
page does not ship, and is not described to Mark as finished, until ALL are green and
Mark has verified at least the first proven page.

**Triage every rule.** If a rule can be checked mechanically, it becomes a `doclint`
gate (build-breaking) - NEVER a checklist item, because a checklist depends on memory,
which is the exact thing that fails. The human list below is only for genuine judgment
calls, and those are the weaker tier, backstopped by the adversarial review and by Mark.
(Mark, 2026-06-25, after I parked the automatable block-link rule here instead of in the
gate, then claimed it "belonged in the gate" - a contradiction he rightly caught.)

## Automated (the `doclint` gate must be green)

- [ ] **No uncovered on-screen reference.** Every section whose prose marks a control
      with `((Component))` carries a screenshot. (`screenshot-coverage`, ERROR)
- [ ] **No unmarked on-screen reference.** Prose that points at the screen ("the wand
      icon", "the Expression Editor", "click...") is either marked + shown, or is
      genuinely conceptual. (`screenshot-coverage-prose`, WARN — resolve each one.)
- [ ] **Structure:** exactly one H1, a plain-prose lede before the first `##`, no
      heading deeper than h3. (`structure`, `lede`, ERROR)
- [ ] **Style:** no em-dashes; zero banned filler/marketing words. (`em-dash` ERROR,
      `banned-word` WARN)
- [ ] **Block links.** The first body mention of a known block name links to its
      reference page. (`block-link`: ERROR for distinctive names, WARN for ambiguous
      common words like Wait/Condition; mentions inside code, HTML comments, headings, or
      image alt are ignored; `<!-- doclint: allow-unlinked: NAME -->` escapes a legitimate
      non-block use.)
- [ ] **A block-documenting section shows the block.** Every `##` section that names a
      block (a `.fr-block` pill) carries a screenshot, or a conscious opt-out. (`section-shot`,
      WARN — add a real shot of the scenario, or mark `<!-- doclint: no-shot: <reason> -->`.
      "Related" is exempt.) Catches the Writing/Counter miss: a documented action with no shot.
- [ ] **No trigger-as-start framing.** Prose never frames a flow's start as trigger-based
      (a flow can start with anything). (`trigger-start`, WARN — reword; Initial Data = data
      sent when a run starts, a trigger's data lives on the trigger block. Skipped on the
      Triggers page; `<!-- doclint: allow: trigger-start -->` escapes a genuine triggers topic.)

## Human / adversarial (doclint cannot check these — do not skip them)

- [ ] **Verify-then-write.** Every claim about how the product BEHAVES was confirmed
      in-product before being written — not inferred from a plausible model. Keep a
      short verification note per page (what was checked, what the screen showed, date).
      This is the gate that kills confident-but-wrong premises (e.g. the Triggers page).
- [ ] **Verify the WHOLE surface, not one panel.** A control's absence from the config
      panel is NOT its absence from the product. Check every place a control can live: the
      block's HOVER toolbar, right-click menus, modals, the canvas — and where a feature
      has an end-to-end flow, actually RUN it (activate it, send the request, view what it
      produced). (Mark, 2026-06-24: I checked only the panel, wrongly declared Learning
      Mode "removed"; it is a block hover icon, and a real POST proved it learns the
      payload structure.)
- [ ] **EXERCISE every control's states before writing — and log it.** For every toggle,
      dropdown, or mode the page names, DRIVE all of its states in the live product and
      document ALL of them, never just the one a static screenshot shows (Content Type =
      JSON *and* XML *and* Plain Text; Compose Result ON *and* OFF). Keep a per-page
      product-exploration HTML comment of what you clicked and saw. (Mark, 2026-07-06:
      Return Result documented only "Compose Result on / JSON key-value" because I read one
      shot instead of clicking the toggle — the exact failure this and the rule above forbid.)
- [ ] **Internal coherence + example continuity.** A section's example matches its own
      framing (no jump from an Initial-Data framing to a variable example unbridged), input
      and output are not mixed in one section, and a consecutive section BUILDS ON the
      preceding example rather than swapping in an unrelated one (not "one example per page").
- [ ] **Precise product terminology + stated scope.** The exact product word is used, never
      one that names a different feature (reuse ≠ repetition = Repeat/List Iterator); and the
      page states the feature's boundary + escape hatch (subflow = flow-scoped → Call Flow /
      Flows as Actions for cross-flow). (Mark, 2026-07-06, Subflows.)
- [ ] **Screenshot DEMONSTRATES its concept — judged by the PIXELS, not the alt text.**
      Open every image and look at it. The shot must SHOW the section's real scenario in
      action (an anchor actually set to a caller id; a value actually written) — never a
      default / empty / merely-related panel. A shot of a setting's DEFAULT under a section
      teaching the NON-default shows the OPPOSITE of the lesson: a blocker. Confirm the alt
      text matches the pixels (it was written by the same author and can carry the same blind
      spot). (Mark, 2026-07-04: a default-anchor shot slipped past five reviews because the
      reviewer trusted alt text.) The `concept-page-review` DoD lens now reads the PNGs.
- [ ] **Screenshot quality (VOICE.md).** Each shot depicts the REAL named scenario the
      prose describes (no generic placeholder); the subject sits beside its panel with a
      clean gap; nothing clipped at an edge; no dark backdrop bleed; eyeballed after
      cropping.
- [ ] **Every paragraph passes the quality bar (per-paragraph, not per-page).** Each
      paragraph, heading, list item, and admonition is Useful, Structured, Teaches, Builds on
      prior knowledge, and is Engaging (not boring). Flat, indifferent, box-ticking prose is a
      FAILURE even when structurally clean. (Mark, 2026-07-04: "written by someone indifferent
      to the product… no pride." Quality IS checkable — per paragraph.) Bar = the approved
      Variables / Expression Editor pages. The `concept-page-review` quality lens enforces this.
- [ ] **Screenshot-at-first-reference.** The shot sits where the prose FIRST points at
      the control, introduced by the sentence before it describing what it shows.
- [ ] **Every capability declares its value - even on how-to/Manage pages.** Each section
      says WHY or WHEN you would reach for the thing, not only what the UI shows or that you
      can do it. "You can rename a workspace" is mechanical; "rename it when its purpose has
      drifted from its name, so the label still says what is inside" carries value. (Mark,
      2026-06-25, Workspace Settings: "states what the user sees without declaring any value"
      - rename and transfer never said why or when.)
- [ ] **Concept page stays at concept altitude.** A concept page leads with value and
      bridges the reader's existing mental model; it does NOT carry reference-level
      mechanism (config fields, modes, exact syntax, step-by-step setup), and it never
      crowns one implementation as the centerpiece - each is just an example. (The linter
      cannot judge altitude; this is an adversarial-review call. Mark, 2026-06-25.)
- [ ] **Read in nav order, as the reader.** The page assumes only what earlier pages in
      the dependency sequence already taught; it introduces, then links, each new term.
- [ ] **Adversarial review pass.** A separate reviewer read the page against this list
      with the job of FINDING violations, and returned none open.
- [ ] **Every evidence pointer resolves, and every "fixed" claim is verifiable in the artifact.** Before
      handoff, grep each verdict/ledger pointer's target (a "Round N block" must exist in the file the
      pointer names) and re-grep the page for each edit the ledger claims (a silent no-op replace is how a
      "fixed" claim and the artifact diverge - it happened on Call Flow, five recurrences of dangling
      pointers before the rule was written, 2026-08-24). Assert on every programmatic text replacement.
- [ ] **Reported honestly.** "Done" is claimed only after all the above — Mark is not
      the one who finds the holes.
