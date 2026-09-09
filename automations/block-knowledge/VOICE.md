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
- **A screenshot goes WHEREVER the prose points the reader at something on screen - one per such
  place, applied per section, NEVER capped at one per page.** This is the decision rule for ANY page
  (reference, concept, or narrative). If a sentence sends the reader to a specific location, control,
  panel, dialog, tab, or configured state - "where MCP Servers lives", the Register MCP Server form,
  the block list's MCP Extensions group, the Manage Capabilities window - that place gets its own
  screenshot. A page that points the reader at four distinct places carries four screenshots. The
  ONLY thing that gets no screenshot is purely conceptual prose with no on-screen referent. Shipping
  one screenshot and describing the rest in words is the exact "just to get a checkmark" failure the
  standard of care forbids - do the full job. (Mark, 2026-06-22, after the MCP page shipped one shot
  where it needed about four. See the standard-of-care memory.)
- **Illustrate the control AT its first reference, and the picture must match the prose.** Two
  failures that kept recurring - codified here so they stop. **(1) Put the shot where the prose first
  introduces the control, not in a later section.** If *How it works* names ((Outgoing Transition
  Mode)) or *When to use* names ((On Completion)), the screenshot of that control goes THERE - the
  reader sees it the moment they read about it, and never meets a named control with nothing to look
  at. (The generator now lets *How it works* / *When to use* carry a screenshot via
  `mental_model_image`/`mental_model_alt` and `when_to_use_image`/`when_to_use_alt`, so there is no
  structural excuse to bury it in the Example.) **(2) Every screenshot depicts the actual worked
  scenario the prose describes - real named blocks, real config - never a generic placeholder.** If
  the example says a flow created a customer record and three enrichment actions run inside the group,
  the shot shows exactly that (`Create Customer Record`, `Company Lookup`, `Credit Score`, `Support
  Tickets`), not a bare `Start -> Actions Group`. A picture that contradicts its own prose reads as
  "made in a hurry" and fails the bar. (Mark, 2026-06-23 - Actions Group AND Triggers Group both
  shipped exactly this defect.)
- **Carry every claim through: HOW, WHY, WHERE - and verify "always".** Stating a fact is half a
  job; the reader must be able to act on it. (Mark, 2026-06-23, Handle Error.) **(a) Show the HOW.**
  When a block *produces / exposes / hands you / returns* a value, show the concrete way to GET and
  USE it - the result alias, the Expression Editor path (Block Data -> the alias), the real reference
  syntax (e.g. `` `{{Handle Error Result->message}}` ``), illustrated where introduced. "It hands you
  the error" without showing how to read it is incomplete. **(b) Give the WHY.** If a detail has a
  non-obvious reason, state it inline - do not make the reader connect the dots. (Why does the error
  carry a `source`? Because one Handle Error can guard several blocks, so source says which one
  failed.) **(c) Say WHERE.** When you tell the reader to reach for a block/control, name where it
  lives - the palette category (e.g. **Utils**), the nav path, the tab. **(d) Examples consume the
  output.** A worked example must show the result actually read and used (the recovery step reading
  the error and building the notification), not just the setup. **(e) Illustrate connected, never
  dead-ended.** A block defined by what feeds it and what consumes it must be shown wired on BOTH
  sides. **(f) Verify "always" in-product.** Never claim a field is always present without checking -
  a Custom Cloud Code throw yields NO `code`, though an HTTP failure does; state what is reliable
  (message, source) vs. conditional (code), and build guidance on the reliable parts.
- **Illustrated - every block page is shown, not just told.** When we document a block, a
  screenshot is always helpful. **Every block page carries at least one screenshot that captures
  the block itself and its config panel in the same image** - the reader sees the block on the
  canvas and the fields they will fill in, together, in one shot. (Mark) **Complex / control-flow
  blocks** (loops, conditions, error handling, the Expression Editor, anything with moving parts to
  trace) get that base screenshot *plus* additional ones - the actual data, the Expression Editor,
  the traced passes - and one vague screenshot is not enough; show each part that matters. The base
  block+config image is the floor for every page; add more wherever a part genuinely needs showing.
- **Screenshots show the thing in context, and the prose sets them up.** Capture a feature with its
  block selected on the canvas and its config panel together, with enough surround to place it (e.g.
  the subflow's RETURN / "SubFlow <name>" bar) - never a cropped fragment of one panel section floating
  on its own; the reader must be able to tell what they are looking at and where it lives. And always
  introduce a screenshot in the sentence before it by DESCRIBING what it shows ("the screenshot below
  shows the HTTP Request inside the subflow, its header bound to the input"), not by dropping it in cold.
  In a worked **example** the intro describes what the shot depicts - it must NOT tell the reader to
  "step into" or "select" anything, because the example flow is ours and the reader cannot navigate it;
  reserve imperative "do X" navigation for how-to / section instructions. **Compose tight:** before
  capturing, pan the canvas so the subject block sits beside the config panel with a small clean gap -
  never left-aligned with a dead gap of empty canvas, and never tucked under/behind the panel (the block
  and all its controls must be fully visible) - and keep unrelated chrome (the minimap, neighbouring
  panels) out of frame. Crop cleanly: trim editor chrome, and for a dialog floating
  over the dark canvas, cut to the last fully-clean row so no dark backdrop or rounded-corner bleed
  shows at the edges. Never clip a button or control mid-element at the frame edge (a half-cut DELETE
  button reads as unfinished) - include it whole, or frame it out. **Verify before presenting:** read
  the cropped image back every single time and confirm the subject and all its controls are fully
  visible, the panel header/buttons are whole, nothing is clipped at any edge, and there is no dead
  canvas or stray chrome - a screenshot you have not eyeballed is not finished. (Mark)
- **Thoroughness beats brevity.** Never trade away the substance to keep a page short. A short
  page that does not educate is a failed page.
- **Lead with value, not mechanics - the stage you set.** The lede and How-it-works must make the
  reader *want* the block: open with what it lets them do that is worth doing, not a dry restatement
  of the request it sends. For a feature-rich block, name its standout capabilities up front - an AI
  Agent uses tools, searches Knowledge Bases, and remembers across runs, so the *intro* says that,
  not page two. Excitement comes from *concrete capability*, not adjectives: the banned-words rule
  (no "powerful/robust/seamless") still holds; you earn the energy by showing what it does. A weak,
  incomplete stage is a failed page even if every fact is present. (AI Agent review, Mark)
- **Concept pages teach the model and lead with value; mechanism lives on the reference pages.** A
  concept page (Triggers, Blocks, Variables...) exists to mold the reader's existing mental model of
  automation onto FlowRunner's - not to operate a control. Lead with what the feature lets them do and
  the *breadth* of it, and bridge from what they already know ("when X happens, do Y") to how
  FlowRunner names it. Use concrete, relatable examples. Do NOT drag in reference-level mechanism on a
  concept page - config fields, modes, exact syntax, step-by-step setup belong on the Block Reference
  page, and dropping them into a concept intro is too soon and buries the idea. And NEVER crown one
  implementation as the centerpiece: External Callback is *one* trigger example, peer to Gmail's
  "On New Message", not "the" trigger. Screenshots on a concept page illustrate the value (the breadth
  of triggers, a recognizable trigger as a flow's entry), not a config panel. (Mark, 2026-06-25, after
  I built a Triggers page that centered External Callback and deep-dived Learning Mode - reference-level
  mechanics that drowned the concept and led with plumbing instead of value.)
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

- **The ™ goes on the first or most prominent mention only**, then the bare name in body prose.
  Write `FlowRunner™` once near the top of a page (or on the page's headline mention), and plain
  `FlowRunner` everywhere after. Repeating ™ on every occurrence reads as noise; one prominent mark
  is the convention. (Decided 2026-06-20; supersedes CLAUDE.md's "always include ™".)
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
  - **Expression-Editor references - any value that goes into a field through the Expression Editor**
    (a block's result alias, an alias with a property path such as `Sum Operation Result` or
    `HTTP Request Result->items`, a Data Bucket reference, a named system value like
    `Current Iteration Item`) take the `.fr-expr` wand-pill token, NOT `code` backticks. These are
    tokens you INSERT in the editor, never text you type or paste; dressing them as monospace `code`
    (which reads as copy/paste) actively teaches the trap. Mechanism: author the reference as
    `{{...}}` in the prose; the generator's `exprify` pass (after `controlify`, before `linkify`)
    renders it as the pill and turns `->` into a `→` arrow. Reserve the token for "the value a
    field reads"; write "point this field at X" as prose, not as a typed literal. The pill wears the
    product's real Lucide `wand-sparkles` icon (the wand on expression-enabled inputs); markers
    inside code fences are left literal. (Supersedes the earlier "pills take `code` backticks" rule.)
  - **UI components - any literal element of the product interface** (a field, toggle, button,
    dropdown, or dialog: System Prompt, User Prompt, AI Model, Manage Capabilities, Force Parsed
    Output, Skip Block, Expand, APPLY, ...) take the `.fr-control` chip: a neutral OUTLINED chip
    (border + faint surface fill, no new palette color) in regular weight. **Case matches the UI
    exactly** - the chip renders verbatim (no CSS case transform), so write the component in the case
    the product shows it (`Force Parsed Output` title case; an `APPLY`/`DELETE` button uppercase). The
    cue is deliberately distinct from the green block pill (a thing you *place* on the canvas) and the
    dotted concept tooltip (a thing you *learn*) - the chip means "a literal thing you'll find in the
    product UI". Rule, decided 2026-06-19: **when the prose names a UI component, chip it.** Mechanism:
    - **Placement is by intent, marked in the source - never string-matched.** Write the component as
      `((Component Name))` at each spot where the prose genuinely refers to the UI element; the
      generator's `controlify` pass renders it as the chip. This is why there are no false positives:
      "((Expand))" chips, but the ordinary verb "expand" (left unmarked) does not - the author, who
      knows the product, decides, not a matcher. No per-word stoplists, no config-type inference.
    - `controlify` runs BEFORE `linkify` (and linkify protects the finished chips), so a component
      whose name contains a block name (`((Wait for completion))` contains Wait) stays whole.
    - Mark **every genuine mention** in flowing prose (lede, How it works, sections, Example,
      Behavior, gotchas). Do NOT mark inside **headings**, **image `alt`** text, the **Configuration /
      Common-settings tables** (the row-name column already lists them), or **code** (a literal
      `((...))` in a snippet is left alone by the generator).
    - A **concept** (Initial Data, Data Bucket, Knowledge Base, Expression Editor) keeps its glossary
      tooltip and is NOT marked - it is a thing you learn, not an on-screen control. When a term is
      both, prefer the glossary tooltip it already has.
    - Styling lives in `content/css/site-overrides.css` (`.fr-control`), never the locked
      design-system CSS; dark-scheme contrast is tuned there too.
    - **Narrative pages get the same chips.** Reference pages convert `((...))` in the refgen
      generator; hand-authored narrative pages (First Steps / Platform / Build / Run & Monitor) get
      the identical conversion at build time via the MkDocs hook `hooks/control_chips.py` (which
      reuses refgen's `controlify`). So `((Label))` is the one chip syntax everywhere - never bold a
      UI component, and never hand-write a `<span>`. Block names on narrative pages get the green
      pill too: write them as a markdown link to the reference page with the class -
      `[Set Variables](../../reference/set-variables.md){.fr-block}` - so a block reference renders as
      the same clickable green pill everywhere it appears. (Mark, 2026-06-25: block references carry
      the green-pill styling on every page, not links-only - supersedes the earlier "generator-only"
      rule.) Concepts keep their dotted tooltips.
  - **Field labels and section names** take **bold** (per CLAUDE.md) - they are things you *read*,
    not press.
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

Generalizable rules extracted from review feedback, newest first. STANDING PROCESS: every specific
correction Mark gives is extrapolated into a general rule here (or into the Content standard above) in
the same turn - a one-off fix without a written rule is treated as an incomplete response.

### 2026-08-24 - Call Flow gate red-team - four new rules (pending Mark's confirmation)
- **An error table's "What to do" is applied verbatim in the failure moment - it must be safe standalone.**
  Advice that only fits the NEXT call ("raise the timeout") reads as "re-send now" and can cause the very
  hazard the page warns about (a duplicate run). Lead the remedy with the standing fact, then mark
  next-call advice as such.
- **When a GET has side effects, name the side effect where the URL is handed out.** "Keep it private"
  does not cover accidental fetches - link unfurlers, browser prefetch, uptime monitors all start real
  runs. Say so at the point the copyable URL appears; every number in a worked example must likewise be
  derivable from what the page shows or states.
- **A maxim distilled from one worked scenario must hold on every path of the example flow, or be
  scoped.** "On means the caller gets only that block's value" is false for a run that never reaches the
  block - scope it ("a run that reaches the block ...").
- **When a page warns of a failure state, hand the reader the manual recovery its own facts imply.**
  "You hold no id for it" reads as unrescuable when the Instances tab shows the id two sections later -
  close the loop in the same sentence.

### 2026-08-24 - blocking Call Flow lede, Mark 3/10 - two rules
- **A lede names the transport and the ordinary contract; edge cases never surface there.** "One GET or
  POST request starts the flow, waits, and returns the flow's answer" - the reader must know what they
  will SEND from sentence one. Release Caller (or any toggle/mode) belongs only in its own section.
- **Precision repairs apply at the lowest possible altitude.** When a reviewer flags a plain lede claim
  as technically contradicted by an edge case, reword the claim so it stays true - do NOT promote the
  edge case upward. (The 3/10 lede was reviewer-induced: a gate round's "scope the maxim" fix pushed
  Release Caller into the lede. Same failure family as the 30-entry ToC.)

### 2026-08-24 - Call Flow round-11 red-team - two rules (pending Mark's confirmation)
- **Two outcome rules whose intersection is reachable must have that case answered.** "One Return Result
  reached -> its value" and "a failed run -> the TERMINATED envelope" collide on a run that reaches one and
  then fails - drive the intersection and state the precedence (driven: the reached Return Result wins).
- **A page that sets its own evidentiary retention bar applies it uniformly.** If undriven rows are dropped
  "until driven", no undriven row survives a content fold; anything kept on catalog lineage carries a
  provenance line in the page comment. Alt text may only use framings the visible prose establishes.

### 2026-08-24 - api/index.md removed - no routing hubs
- **A section index whose content is routing + shared fragments is excessive** (Mark: "it may cause
  confusion"). Nav labels and page ledes route; shared error codes were folded into each endpoint page's
  own Errors table; the credentials section moved to its canonical page (Workspace Settings). Pages stay
  self-contained; a reader never detours through a hub.

### 2026-08-24 - Call Flow split gates - four rules (pending Mark's confirmation)
- **A screenshot's redaction must never falsify prose built on that image.** If a shot blanks a live
  value (credentials -> YOUR_WORKSPACE_ID), the prose at the shot declares it ("blanked in these
  screenshots") so claims like "the URL is live as written" stay true.
- **Sibling endpoint pages cover crossover mistakes and shared contracts symmetrically.** If page A says
  "the name does not work here", page B says the mirror; a safety warning (accidental GET starts a run)
  lives on BOTH pages that hand out the URL; shared facts ({} body valid) match verbatim or are cut from
  both.
- **'(((': never let a parenthesis touch a ((chip)) marker** - the paren is swallowed into the rendered
  chip label. Now a doclint ERROR (chip-paren-collision).
- **INTERIM, for Mark to confirm: in a shot-less reference table (an Errors table's "What to do" cell), a
  control the reader acts on stays BOLD, not chipped.** VOICE says chip every control you act on; doclint
  hard-gates any chip in a section without a screenshot - the deadlock made reviewers flag the same rows
  in four consecutive gate rounds. Options for Mark: (a) bless this interim rule; (b) relax doclint to
  accept an explicit per-section opt-out so the chips can land. Until he rules, bold + this note is the
  convention.

### 2026-08-24 - Call Flow endpoints - copy-ready, one call shape per section, no swiss-army pages
- **"Forcing someone to think brings useability down"** (Mark, verbatim). On API pages: show every
  endpoint as one FULL URL (never base + relative path the reader concatenates); give GET and POST each
  a self-contained section with a complete pasteable example (never interleaved "on a GET / on a POST"
  rules); and document one call per page - Mark: "If needed create blocking page and non-blocking page.
  If needed, create section for GET and one for POST." Applied: call-flow.md split into
  call-flow-blocking.md + call-flow-nonblocking.md.

### 2026-08-24 - Call Flow ToC - heading budget
- **A page's ToC stays scannable: ~a dozen entries, h3 only for a real reader destination.** The
  spec-first Call Flow rewrite ended up with 29 ToC entries after successive review rounds each
  promoted run-ins to h3 "for anchors"; Mark: "impossible to navigate ... the TOC has 30 entries."
  Sub-parts of a section (Headers/Body, an error group, a dialog tab) are bold run-ins, not
  headings. More destinations than the budget = split the page, never inflate the ToC.

### 2026-08-24 - Call Flow gate round 24 red-team - four rules (pending Mark's confirmation)
- **An API page states which version of the versioned artifact its address binds to, and what moves that
  binding.** The blocking URL carries no version segment: it runs whichever version is LIVE, so a colleague
  starting a clone silently changes what a shipped integration executes, with no URL change and no error.
- **A page may withhold a known bug's cosmetics, but the reader's most likely error must still appear in
  the failure map.** Malformed JSON returns HTTP 500; the Errors intro asserted 415/405 were the only
  non-400s. The condition is now documented without documenting the stack trace.
- **A row a client handles programmatically states its detection signal, not only its remedy.**
- **When two controls on one row compose, the bullet recommending the second says what the first does to
  its output.** The dialog's per-value JSON editor is recommended for objects while the green A icon, on by
  default, escapes exactly those objects.

### 2026-08-24 - Call Flow gate rounds 22-23 red-team - four rules (pending Mark's confirmation)
- **A remedy removed for safety must be swept out of every pointer that carries it.** Round 21 deleted the
  regenerate-the-key advice from the security paragraph; it still shipped in the Related bullet on both API
  pages and in the linked page's own prose. A link's description is a recommendation.
- **A security note names the endpoint's OWN distinguishing capability as part of the exposure.** A leaked
  blocking URL does not merely spend executions - it returns the flow's composed answer. Generic sibling
  wording understated it.
- **A bullet glued to an image or a ":" lead-in is not a list item.** It ships as a literal "- " inside that
  block. This shipped twice with doclint green; now a `split-list` ERROR.
- **Never hedge about our own product's enum.** "Handle an unrecognised value rather than assuming these are
  the only two" reads as the documentation guessing about the product; scope the fact instead ("this call
  answers only after the run has finished, so these are the two states it reports").

### 2026-08-24 - Call Flow gate round 21 red-team - four rules (pending Mark's confirmation)
- **A page may omit a known enforcement gap, but it may NEVER ship a remedy that gap makes ineffective.**
  The page told readers to regenerate the API key after a leak while our own log records that the key
  segment is not checked - the remedy would have left them believing a leaked URL was dead. Removed.
- **Deleting an unproven guarantee is not a fix when the reader still has to act - give the defensive
  practice instead.** Dropping the `blockName` uniqueness claim left the client with no way to key on it;
  the page now says to name every Return Result before building on it.
- **A "costs nothing" claim must survive the page's own limit table.** "A larger timeout costs nothing"
  sat above a table charging for in-flight calls (`998`).
- **A hazard attached to the URL rather than the method repeats in every self-contained method section.**
  The accidental-fetch warning lived only under GET, though POST hands out the same live URL.

### 2026-08-24 - Call Flow gate round 20 red-team - four rules (pending Mark's confirmation)
- **Never write a counted lead-in above a list ("Three things follow from that:").** Later rounds add
  bullets and the count silently goes false. Use a countless lead-in.
- **A field prescribed as a client's lookup key needs its STABILITY stated, not just its uniqueness.**
  `blockName` is the block's editable Name field: renaming a Return Result breaks every client keyed on it,
  the same hazard the page already warns about for the flow name in the URL.
- **A remediation the page tells a reader to perform must state what else it breaks.** "Regenerate the API
  key" is workspace-wide: it invalidates the call URL of every flow in the workspace.
- **Where the product generates the same call the page hand-writes, say where the generated form differs
  in OUTCOME.** The dialog's cURL sends `"1042"` as a string, so it returns the GET-shaped answer the POST
  section teaches readers to avoid - a difference in bytes that is a difference in results.
- **A "not driven" note is a claim too - check it before repeating it.** "Fan-out unwireable via
  automation" was carried for two rounds while the page's own screenshots showed a wired fan-out; the
  gesture just needed a different angle. Retest the obstacle before letting it excuse an undriven claim.

### 2026-08-24 - Call Flow gate round 19 red-team - three rules (pending Mark's confirmation)
- **A sweeping simplifier on an API page must survive every other section of the same page.** "Everything
  else you send becomes Initial Data", "whatever the timeout", "cannot fetch it afterwards", "always
  application/json" - each was contradicted by the page's own later text or by a drive. Before shipping a
  word like everything / whatever / cannot / always, read the rest of the page against it.
- **When a page tells a client to key off a field, state that field's uniqueness guarantee.** `blockName`
  was prescribed as the lookup key with nothing said about how many entries can carry it.
- **When a per-block toggle can be set on several blocks and the example has several, answer the
  multi-toggle case.** Release Caller's three consequence bullets covered every direction except the one a
  builder creates by accident (the toggle on two Return Results).

### 2026-08-24 - Call Flow gate round 18 red-team - three rules (pending Mark's confirmation)
- **A remedy attaches to the general condition it fixes, not only to the extreme case that motivated
  it - and when a failure destroys a value the product already produced, say so.** The Release Caller
  remedy sat under "Runs longer than the maximum wait", so it read as >300s-only; and the timeout bullets
  never said the composed answer is discarded and unfetchable, which is the consequence a builder cares
  about.
- **A scoping repair must not contradict the mechanism it scopes.** Round 17's "in its original shape,
  before the Audit Copy branch" named the one topology that CANNOT host the observation, because the page
  itself teaches that a Return Result ends its path. Name a shape that could actually produce the result.
- **A non-deterministic response field carries the warning on its OWN row.** Documenting the
  non-determinism on a neighbouring field does not inoculate the convenient singular field a client will
  actually reach for (`result` vs `results`).

### 2026-08-24 - Call Flow gate round 17 red-team - three rules (pending Mark's confirmation)
- **A blocking-API page states the response's TIMING contract, not only its body.** The page said what
  comes back and when it times out, but never when the response is sent relative to the run - the very
  thing that makes the default timeout expire. Say it plainly ("sent when the run finishes; Release
  Caller answers earlier"), and derive the timeout advice from it.
- **When a running example's topology mutates across sections, every anecdote says which shape it ran
  on.** The failed-run story was driven on the branchless Order Lookup but read against the Audit Copy
  branch introduced two sections earlier, where it appears to contradict the page's own two-results rule.
- **Adaptation instructions carry the CONSTRAINTS of the swapped part, not just its location.** "Put your
  values in place of orderId=1042" without "query values are URL-encoded" breaks on the first value with
  a space or `&`.

### 2026-08-24 - Call Flow gate round 16 red-team - four rules (pending Mark's confirmation)
- **Sweep every above/below/described-earlier pointer after a page split or section move.** A pointer that
  was true on the old layout can survive as a self-link (the dialog section's "described above" anchored
  to its own containing section). doclint's dead-anchor check cannot catch it - the anchor exists.
- **A driven page-level claim must not absorb undriven carried rows by framing.** "Most errors come back
  as HTTP 400..." silently extended a driven claim over the carried rate-limit rows (limiters commonly
  answer 429). Scope the claim to the rows it was driven on; let carried rows stand on codes alone.
- **A client-side recipe must work for every response shape the page itself teaches.** The
  test-for-executionId discriminator assumed JSON while the page teaches XML/Plain-Text composed values;
  the always-valid discriminator (the Content-Type header) went unstated.
- **Adaptation instructions name every example-specific part to swap.** "Put your flow's name in place of
  Order%20Lookup" left `orderId=1042` to land as a stray property in the reader's flow.

### 2026-08-24 - Call Flow gate round 15 red-team - two rules (pending Mark's confirmation)
- **A toggle that overrides a page's organizing rule is stated in BOTH reachable directions.** The
  Response section's counting frame (how many Return Results the run reached) is overridden by Release
  Caller; the page only closed the direction the worked example shows (toggle on the FIRST block). The
  driven other direction (toggle on the LATER block -> that block's value alone, not the envelope) left a
  careful reader applying the frame wrong. State the override for every direction the reader can reach.
- **When a surface displays data in a shape different from the wire format, say so.** The dialog's JSON
  Editor shows values under an `initialData` wrapper that the endpoint does NOT unwrap (driven: it lands
  as a literal property). Readers copy what they see - name the displayed shape as display-only and show
  what to send.

### 2026-08-24 - Call Flow gate round 14 red-team - four rules (pending Mark's confirmation)
- **Copy-readiness must survive a literal paste.** A code fence is a paste promise: a URL wrapped across
  indented lines inside a ```text block fails the one reader sent to build from it. Route such readers
  through a complete runnable example instead, or keep the block single-line and let it scroll.
- **A page's evidence log must be reconciled with the contract the prose ships.** Two of the author's own
  driven observations contradicting each other (XML body "= the Result value" vs "arrives JSON-quoted")
  is shipped doubt whichever side the prose picks - reconcile the log, and point at the recorded decision.
- **An error table's framing noun must be true of every row it covers.** "Refusals" over a table holding
  28118 (an accepted request whose run is executing) primes exactly the duplicate-run mistake the page
  warns against. "Errors" is the honest noun.
- **Every "must" on an API page is a claim about a refusal - drive the refusal or don't promise it.**
  "The body must be a JSON object" was false as a refusal: [1,2,3] and "x" are accepted (200, run starts,
  nothing lands in Initial Data by name). State what happens, not an unenforced rule.

### 2026-08-24 - Flow vs instance: what the API starts (Mark)
- **The API starts an INSTANCE; the flow must already be started (LIVE).** Mark, on "one GET or POST
  request starts the flow": "a reader who pays attention, will be confused. A flow MUST BE started in
  order for Call Flow to work. The API starts an instance. It is an importan[t] distinction which you
  messed up here." "Start the flow" is only ever the ((Start flow))/LIVE action; a request, trigger,
  event, or schedule starts an instance (a run). Swept docs-wide (both API ledes, workspace-settings,
  flow-control index, branching, triggers page + heading, triggers-group.yaml + regen); now a doclint
  warn (`flow-vs-instance`, actor-keyed so legitimate Start-flow uses never flag).

### 2026-08-24 - Blocking lede, second round (Mark) - lede links the reader's artifact to the feature
- **"If a flow has X, this is how you get Y."** Mark, on the rewritten lede ("turns a flow into a plain
  HTTP API ..."): "That's no educational enough. An educational approach would say this: 'if a flow has
  Return Result, to get it, use the blocking call - the result returned by Return Result is what's
  delivered by this API'. Is it really that hard????" Sentence one names the artifact the reader built
  (the Return Result block) as its SUBJECT and presents the feature as the way to get its value; the
  product abstraction follows as a consequence, never leads. Same family as the mechanics-first lede
  corrections on Expression Editor (2026-06-29 / 07-01): frame from the reader's side, not the product's.

### 2026-08-24 - Call Flow gate round 12 - three rules (pending Mark's confirmation)
- **Author notes never reach readers.** HTML comments (verification logs, security notes,
  doclint markers) shipped verbatim into the built pages' view-source - including a finding
  deliberately kept out of the docs. Now stripped at build (`hooks/strip_html_comments.py`,
  fence-aware, before the chip hook); any new build path must keep that guarantee.
- **A URL that embeds credentials is taught as a credential.** Every endpoint whose address
  carries the workspace id/key states so where the URL is handed out, with handling guidance
  (server-side only, regenerate on exposure) - without documenting any enforcement gap.
- **A retitled heading invalidates its authored anchors.** Mark's Endpoint retitle silently
  killed every `#endpoint` link; doclint now recomputes heading slugs the way the site does and
  ERRORs on dead fragments, same-page and cross-page (`dead-anchor`; first sweep caught a live
  one on inspecting-a-run.md, confirmed against the built HTML).

### 2026-08-06 - ai-in-flows gate red-team - two new rules (pending Mark's confirmation)
- **A proven-failing feature never ships as a silent worked example.** If the author's own
  verification shows a feature hard-fails, the page may only teach it as designed after the
  product owner's explicit ship-pending-fix decision, recorded in the ledger AND the handoff -
  and a screenshot's tab/state must never be composed to hide a failure the log records
  (evidence-shaping). (AI QUESTION runtime bug; Mark chose ship-pending-fix.)
- **"Every X on this page" is a claim about every X on the page.** A page-wide generalization
  must be verified on each surface the page's own roadmap enumerates, or scoped to the surfaces
  actually verified (extension actions turned out to use their own Configure connection, not the
  model/key pattern). Likewise the lede's organizing frame must cover every section it promises.

### 2026-08-06 - ai-in-flows review round (Mark) - four rules + one recurrence
(General principles restated for Mark's confirmation.)
- **Show-the-HOW cannot be delegated to the reference.** When a page verified a result's shape, it
  states the read syntax inline ({{Alias->property}} as the wand-pill) - "downstream blocks read it
  like any other; see the reference" does NOT satisfy the HOW rule. Doubly binding when the
  reference's own example is wrong: the guide is then the only correct source.
- **Every Build page ends with a page-level `## Related`.** A route cluster parked inside a section
  reads as the page's closing block; never let more sections follow it.
- **Section order follows the page's own declared axis.** If the page is built on an escalation
  (effort/scale of the judgment), the least-effort option cannot come last - placement is part of
  the teaching, not layout convenience.
- **The lede's roadmap enumerates exactly what the page delivers.** N sections promised = N
  delivered, in page order; adding a section means updating the roadmap.
- RECURRENCE: "exactly as you learned in <page>" scaffolding slipped through (§0b ban). Add
  "as you learned" to the plain-style pre-handoff greps.

### 2026-08-06 - State the intrinsic fact; let the reader draw the consequence (ai-in-flows, Mark)
"Every AI step runs on a model account you control - your provider, your bill" → drop "your
provider, your bill". General principle (restated for Mark's confirmation): **state the fact that
carries the value ("runs on a model you choose, through your own provider account") and let the
reader draw the consequences (billing) themselves** - spelling out an implication the reader
reaches in the same breath is noise, kin to the no-tautology and don't-answer-unasked-questions
rules. Focus prose on the intrinsic value of the fact, not its downstream arithmetic.

### 2026-07-27 - Block vs operation; beautified JSON; the expression-reference token (Transform Data review)
Four corrections, all generalizable beyond Transform Data:
- **Never call an operation "a [Operation] block."** The block is the block TYPE (e.g. Transform Data); the
  things you select inside it are OPERATIONS. Write "an Item Quantities block (Transform Data) runs the Map
  List operation," not "a Map List block." In worked examples, give each block a CUSTOM name and put the
  real block type in parentheses - "a Get Order block (HTTP Request)" - so the reader can map prose to the
  canvas. This generalizes to any block with modes/operations/sub-types.
- **Beautify JSON: property per line.** Do not flatten multi-property objects onto one line in examples. Use
  the traditional multi-line layout (each property on its own line, nested objects indented, array elements
  each on their own line). Scalars, short scalar arrays, and JSON-STRING literals (the input to Parse JSON)
  stay inline.
- **Expression references get their own token, never `code`.** A value that goes into a field through the
  Expression Editor is a token you INSERT (a pill), never text you type or paste - so it must NOT be dressed
  as monospace `code` (which reads as copy/paste). Author it as `{{...}}` in prose; refgen renders it as the
  `.fr-expr` wand-pill (see Formatting rules). Reserve the token for "the value a field reads," and describe
  "point this field at X" in prose rather than showing a typed literal.
- **Doc cues that echo a product affordance use the REAL product icon.** The `.fr-expr` token wears the exact
  Lucide `wand-sparkles` icon from the product's expression-enabled inputs (extracted from the live DOM),
  not a look-alike glyph. When a cue references something the reader sees in the UI, match the UI.

### 2026-07-09 - Write PLAIN; mimic the house style already in the repo (Agent Memory / Error Handling / Flow Scheduling, ~20 rounds)
The beat-down: I kept drafting in a flourishy, "sophisticated" register and left Mark to catch it, round
after round. What finally passed: match the plain delivery style ALREADY in the repo - the legacy docs
(`content/flow-editing/dataflow.md`, `snippets/errorhandling.md`: plain declaratives, a bulleted list for
any set of fields/options, one screenshot per point) and the approved exemplars (Variables, Expression
Editor). The rule already existed (Content standard / §0b "say it plainly"); the failure was not ENFORCING
it at draft time. Do not out-write the house style - match it. Mark: "I do not need a Leo Tolstoy writing
FlowRunner docs. The task is much simpler than you make it out to be."

**Plain-style pre-handoff check** - run before ANY page goes to Mark; fix every hit. Most of it is greppable,
so it does not rely on taste:
- No contrast / "clever" constructions: `not X but Y`, `rather than a`, `the difference between X and Y`,
  `worth dwelling on`, `one voice ... rather than a one-shot worker`, cute closes ("...when the task deserves a flow").
- No metaphors; no unresolved back-references (`the same way you saw above` - the reader scrolled and can't
  tell what you mean; name it or drop it).
- Any enumeration of 3+ items (error fields, frequency options, policy choices) is a BULLETED LIST, not buried
  in a sentence.
- Every named control/location gets a screenshot at first mention OR a stated location (Mark: "not a single
  clue where Start Flow / Pause / Stop are").
- Short declarative sentences; plain concrete words. No incidental over-naming - do not hammer a variable name
  (`AI Response`) that isn't in the screenshot and isn't the point.
- Don't imply a specific block is required for a generic action (`which the Custom Cloud Code can check` - any
  block can check a value). Concrete beats vague ("malformed or invalid input - fails the same way every time",
  not "input the step will reject").

### 2026-07-08 - Educational quality over word count; verify behavior; credit the platform (Agent Memory / Error Handling / Flow Scheduling review)
- **Word count is never the goal; a reader's understanding is.** Do not lump distinct mechanisms into one
  paragraph to bulk it up (Flow Scheduling folded the Start/Stop Scheduled Runs blocks into the core "what a
  schedule is" intro). One mechanism per paragraph/section, introduced where it is relevant.
- **Lead with the primary/manual control; a convenience is not THE mechanism.** Never present a programmatic
  convenience as the way to do something a simpler manual control already does (scheduled runs pause/stop from
  the LIVE version's Pause/Stop controls; the Start/Stop Scheduled Runs blocks are just the programmatic
  equivalent). Manual/primary first; and never imply the user must build a second flow to do a UI action.
- **Do not assert reader difficulty you can't substantiate** ("the piece that trips people up", "the part
  everyone gets wrong") - state the fact plainly. And no **tautologies** whose conclusion restates the premise
  ("because the schedule rides on one version, that version runs on it" = "sugar in water tastes sweet").
- **Verify behavior - propagation, inheritance, gating - before asserting; test it when you can.** "A cloned
  version does not inherit the schedule" was wrong. The product's own legacy docs (`flow-management/`,
  `flow-execution/`) are a valid cross-check for *behavior* (not style/terms); and testable behavior gets a real
  test (a throwaway scheduled flow + a Call Flow REST call proved "Allow only scheduled flow instances" rejects
  an API launch with "Flow can be called only by scheduler.", and off it returns an executionId).
- **Use the product's exact term** - "START a version -> LIVE", never "Publish".
- **Credit FlowRunner, not "the agent"/"it", for platform-managed work** (loading/saving an agent's Messages
  History) so readers don't think they must touch the agent's prompts or the store.
- **A screenshot points out WHERE (its panel/tab in context), not just the cropped control, and sits at the
  first mention.** **Precision over hedging** - no "roughly every 30 seconds" when the cadence is exact.

### 2026-07-06 - The reviewer must not assert a defect it cannot verify (gate calibration, Mark-confirmed)
- **Uncertain screenshot concern -> "verify", never "blocker".** On the Expression Editor re-run the reviewer
  asserted a correct **As JSON** shot was "possibly JSON Editor mode" and called the prose "Data Bucket variables"
  a label mismatch against the UI's **VARIABLES / LOCAL VARIABLES** groups. Both were wrong - Mark confirmed the
  shots are correct. Rule: when the reviewer cannot confirm from the pixels that a screenshot is wrong, it flags the
  item as **verify (low confidence), addressed to Mark** - it does NOT assert a defect or block on it.
- **A fair prose summary of a UI group is not a label mismatch.** Prose may describe a group of controls in plain
  words ("your Data Bucket variables"); that is only a mismatch if the prose QUOTES a literal UI label the screen
  contradicts. Do not flag a reasonable description as a label error.
- Net: the gate stays adversarial on what it can prove from the pixels, and downgrades what it merely suspects to a
  flagged-for-Mark verify item. (Guards against over-flagging correct work, the mirror of the miss-real-defects failure.)

### 2026-07-06 - Exercise the surface, keep examples continuous, use the exact term (Subflows review)
- **Exercise every control's states before writing.** Documenting a control (a toggle, a dropdown) from ONE
  static screenshot is a defect - drive all its states (Compose Result on AND off; Content Type JSON/XML/Plain
  Text) and document every one, with a per-page product-exploration log. (The Return Result failure.)
- **Example continuity.** A running walkthrough must not switch to an unrelated example between consecutive
  sections (Get New Token -> status/amount -> token). Build the next section on the prior one's basis. This is
  NOT "one example per page" - unrelated sections may differ.
- **Precise product terminology.** Never borrow a word that names a different product feature: "reuse" (subflows)
  is not "repetition" (Repeat / List Iterator). **State scope + escape hatch:** a subflow is flow-scoped; cross-flow
  reuse is Call Flow / Flows as Actions.
- **No mixing a feature's input and output in one section**, and no defensive/obvious clarifications.

### 2026-07-04 - Quality IS checkable, per paragraph; and read the pixels
- **Every paragraph must pass a quality bar; flat competence is a failure.** Mark: a page can be
  structurally clean and still read as "someone indifferent to the product, just doing their job - no pride."
  The fix is not "accept the gate can't judge quality" (wrong - I said that and was corrected); it is to
  interrogate EVERY paragraph against explicit questions: **Useful? Structured? Teaches? Builds on prior
  knowledge? Engaging (not boring)?** Any failure is rewritten, not shipped. The `concept-page-review` gate
  runs a per-paragraph quality lens. Bar = the Variables / Expression Editor exemplars.
- **A screenshot must DEMONSTRATE its concept, judged by the PIXELS.** A shot of a setting's DEFAULT slipped
  past five reviews under a section teaching the NON-default, because the reviewer trusted the author-written
  alt text instead of looking. The image must show the real scenario IN ACTION (an anchor set to a caller id,
  not the "Flow Memory" default). Reviewers now open and SEE the PNGs; alt text is never taken on trust.

### 2026-06-22 - Standard of care + the screenshot decision rule
- **Standard of care (governs everything).** FlowRunner is Mark's life's work; the docs ARE the
  product, not a description of it, so a doc imperfection is a product imperfection. Nothing ships
  "to get a checkmark"; never make Mark the QA; do the harder/more complete thing; own and fix any
  shortfall without being pushed. Recorded as the `flowrunner-standard-of-care` memory and pinned at
  the top of the memory index - read it first, honor it above any task.
- **Screenshot decision rule (codified in the Content standard above).** A screenshot goes wherever
  the prose points the reader at something on screen - one per such place, per section, NEVER capped
  at one per page. Surfaced when the MCP Servers page shipped ONE screenshot (the nav) but needed
  about four (nav/register entry, the Register form, the block-list MCP Extensions location, the
  Manage Capabilities window). The "one per page" cap was the wrong rule, and it then read as
  laziness. The page is owed its missing screenshots.

### 2026-06-20 - MCP Servers (first Platform feature page) + decisions
Decisions: **(1)** narrative pages now use the `.fr-control` chip (via the `hooks/control_chips.py`
MkDocs hook), same `((...))` syntax as the reference - codified in the Reference-hierarchy bullet.
**(2)** ™ on the first/prominent mention only, then bare name - codified in Formatting rules.
Writing rules generalized from Mark's review:
- **Be specific, not vague.** "its tools become something you can use" is empty - name the concrete
  options ("usable two ways: as a standalone action in a flow, or as a tool an AI Agent calls"). If a
  later sentence already says it, fold it up; do not foreshadow vaguely then explain.
- **Use the full term on load-bearing mentions.** "When you register a server" -> "an MCP server".
- **Scope a claim to where it is true; never over-generalize with "either way".** The "inputs use the
  Expression Editor, result reads downstream" claim holds for a tool used as a flow action, NOT for a
  tool an agent calls (the agent fills inputs and reads results itself). Splitting into two sections -
  "as a flow action" vs "with an AI Agent" - made the boundary honest. Watch for any "either way /
  in both cases" that quietly papers over a real difference.
- **Plan-, performance-, or cost-dependent caveats go in a footnote, with the WHY.** Agent capacity:
  attach only needed tools, because every capability is described to the model on every run (bigger
  prompt, more options to weigh -> slower, costlier, likelier to mis-pick). State the mechanism, not
  just the warning.
- **Say the plain thing; drop cute indirection.** "A registered server is not frozen" -> just "Open a
  server to manage it... change the URL, name...". Name the action.
- **Headings must name the real thing.** "Where the tools show up" hid that it only covered the agent
  case; the standalone-action surface (the block list) was missing. A heading promises coverage - keep
  it.
- **Screenshot the thing the prose points at.** "You manage servers under Agent tools & Knowledge ▸
  MCP Servers" wants a shot of exactly that nav section + screen, not just told.

### 2026-06-19 - Narrative pages (Learn/Build/Run/Platform): first exemplar (Flows and Instances)
These generalize from Mark's review of the first teaching page. They apply to the hand-authored
narrative sections (not the generated reference), but most are good prose rules everywhere.
- **Break dense sentences.** A sentence carrying three or more clauses ("you build it in the editor -
  the steps, the logic, the order - and from then on it runs over and over, a fresh instance...")
  reads as a wall. Split into short declaratives. Readability beats packing.
- **Set up a loaded term before you use it.** Do not hit the reader with `LIVE` cold; first establish
  that "a flow has a state", then name LIVE as that state. Introduce the concept, then the label.
- **State the escape hatch with the limitation.** When you say something is constrained or off by
  default ("instances do not share state"), in the same breath point to the feature that lifts it
  ("...that is what Shared Memory is for"). Never leave a reader stuck on the limitation.
- **Plan/billing-dependent numbers go in a footnote, not the prose.** "Fifty instances run in
  parallel[^parallel]" with the footnote noting the cap depends on the billing plan - never state a
  plan-bound quantity as an absolute.
- **Plant product breadth where it fits naturally.** Listing what sets a flow off, include "an outside
  system calls it over the API" - seeds the integration story without a detour. Look for these no-cost
  openings.
- **Do not frame around one assumed mental model.** "You do not loop over the orders yourself" trips a
  reader who is holding a single payload of many orders. Avoid framings that only make sense for one
  reading of the scenario.
- **Headings carry the takeaway, not filler.** "In practice" / "Where you see each one" are weak;
  prefer headings that state the point ("A flow has a state", "The editor and the Instances tab").
- **Do not restate a point already made.** "You build it once" landing a third time is noise - cut it.
- **Keep verbs consistent with the mental model you set up.** Once the page establishes that a flow is
  the design and an instance is the run, never say the flow itself "runs" or "does not run" - that
  contradicts what the reader just learned. FlowRunner *creates instances of* the flow. Name the right
  actor (FlowRunner makes the run) and the right object (the instance is the run).

### 2026-06-19 - Control cue (the `.fr-control` chip) - final shape after two pivots
- Added a fourth reference cue, the `.fr-control` chip, codified in the Reference-hierarchy bullet
  above. It landed in three steps, each a correction worth keeping:
  - **Styling:** neutral OUTLINED chip, **regular weight** (bold too heavy), and case matching the UI
    EXACTLY - no blanket uppercase. (I forced global uppercase first; Mark: uppercase only where the
    UI itself is uppercase, e.g. `APPLY`/`DELETE`. `Force Parsed Output` stays title case.) Dark-theme
    contrast needed an explicit lift (the neutral chip has no accent color to lean on).
  - **Scope:** widened from "buttons + toggles only" to **any UI component** - field, toggle, button,
    dropdown, dialog. Mark's simpler rule: *when the prose names a UI component, chip it.* So System
    Prompt / User Prompt / AI Model (fields) chip too, not just the controls. Concepts (Initial Data,
    Knowledge Base, Expression Editor) keep their glossary tooltip and are NOT chipped.
  - **Mechanism:** abandoned string-matching entirely. Auto-matching a label like "Expand" or "All"
    wrongly hits the ordinary words. The fix is **author-marked placement**: write `((Component))` in
    the source where it genuinely means the UI element; the generator renders the chip. Placement is
    intent, not a match, so there are zero false positives and no per-word rules. ((Expand)) chips;
    the verb "expand" left unmarked does not.
- Process note: each pivot came from a pointed Mark question ("would you chip 'Expand' uncondition-
  ally?" exposed that string-matching is the wrong tool). Lesson: a cue applied by *matching* a label
  fails for any label that is also an ordinary word; cues that need judgment must be author-placed.

### 2026-06-19 - SubFlow (screenshots in context; verify labels in-product)
- **Screenshots in context, introduced in prose** - captured in the "Screenshots show the thing in
  context" bullet of the Content standard. A decontextualized panel-fragment crop (e.g. a lone Headers
  section floating on its own) confuses readers: show the selected block on its canvas with the
  surrounding context (the subflow RETURN bar, etc.), and tell the reader what they are about to look at
  in the sentence before the image. Crop hygiene: a dialog over the dark canvas bleeds its rounded
  corners / backdrop at the edges, so trim to the last fully-clean row. (Mark)
- **No overlay tint in a shot (2026-09-09, Billing)** - a capture taken while the notifications drawer
  (or any dialog backdrop) is open comes out uniformly grey; Mark: "a screenshot on the /manage/billing
  page is too dark". Before capturing, confirm no drawer or backdrop is open (the notifications drawer
  puts "Unread only" in the page text); when reading a shot back, a uniformly dim frame means an overlay,
  so close it and recapture rather than ship it. (Mark)
- **SubFlow argument model (verified live, label was wrong in the record)** - a SubFlow block passes
  inputs via its **Initial Params** list (the record had said "Input parameters"); each Initial Params
  name becomes a field in the subflow's **Initial Data**, read inside as `{{Initial Data->name}}` - the
  same model as a triggered flow or Call Flow. Subflows are created in the New SubFlow dialog (Name +
  Input Parameter Names = the declared args); logic is built by dragging the subflow in and stepping in
  (Expand); the arg list is edited via the edit icon on the subflow in the Subflows palette. Generalizes:
  never trust a record's field LABELS or mechanics without confirming them in the live product. (Mark)

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
