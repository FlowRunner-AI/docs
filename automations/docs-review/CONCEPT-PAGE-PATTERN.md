# Locked concept-page pattern (from the Mark-approved Variables exemplar, 2026-06-25)

This is what cleared Mark's bar on Variables. Apply it to every concept page. The binding
definition of done is still the page's section in PLATFORM-REVIEW-LEDGER.md (every item cleared
with evidence) — this pattern is HOW.

## 0. Wear the educator's hat FIRST (Mark, 2026-06-29 — the thing I kept missing)

The repeated failure: I "shoot it straight" — write **mechanics-first** and don't build on what the
reader already knows. That produces mediocre, below-bar pages.

**What "mechanics" means (Mark, 2026-07-01 — sharpened after I missed twice):** it is ANY description
of how the machine works — the UI ("where you give a field a value") AND the flow's data-plumbing
("blocks pass what they produce; a block's settings are input fields; the values come from earlier
results"). Both are the machine. Even "the interface that enables information flow between blocks" is
mechanics — it would fit an architecture spec. **The lede opens on VALUE/OUTCOME from the builder's
seat: what their automation gets to DO.** The model is the approved Variables lede ("its logic needs to
hold values … stitch a name into an email greeting, add one to a running count"), NOT "a variable is a
container." (Expression Editor exemplar, Mark's pick: open on "a flow handles each case on its own
terms — greeting this customer, charging this order …"; the data-flow *how* comes AFTER, never first.)

Fix, every concept page, before drafting:

0. **THE PRODUCT IS THE ONLY SOURCE OF TRUTH** (Mark, 2026-07-02). Verify every claim by driving the
   CURRENT product; capture every screenshot FRESH from it (no dead blocks, no redesigned-away UI).
   Legacy pages (`content/flow-editing/`, …) are useful ONLY for the *delivery style* to emulate (e.g.
   `dataflow.md`: plain, grounded, concrete) — NOT for content, terms, or screenshots (the product has
   changed since; legacy content is unreliable). When unsure how something works, open it and look.
0b. **SAY IT PLAINLY; the idea is usually elementary.** No poetic scene-setting ("specifics of the
   moment", "just wrote in"). No lecturing readers on things they already grasp (e.g. dynamic vs. typed
   data). No "you already met / back in <page>" scaffolding and no reflex cross-links. Trust the reader.
   **MATCH the plain house style already in the repo — do not out-write it:** the legacy delivery style
   (`content/flow-editing/dataflow.md`, `snippets/errorhandling.md`: plain declaratives, a bulleted list for
   any set of fields/options, one screenshot per point) and the approved exemplars (Variables, Expression
   Editor). Run the **plain-style pre-handoff check** (STANDING-RULES Hard rules; VOICE.md Calibration Log
   2026-07-09) before every handoff: it is mostly greppable (no "not X but Y" / "the difference between" /
   "worth dwelling on" / cute closes / "as you saw above"; 3+ items → a list; every named control shown or
   located). The ~20-round beat-down of 2026-07-09 was one failure — drafting flourishy and leaving Mark to catch it.
0c. **Every section TITLE is a meaningful anchor** — a reader must be able to say what the section
   taught from its title alone. "The data a step can reach" fails; "Using another block's result" works.
0d. **Recurring corrections (distilled from Mark's reviews — check every page against these):**
   - **A FlowRunner flow can start with ANYTHING**, not just a trigger — this is a product differentiator.
     NEVER frame the start as "a trigger", and never imply a flow begins with one (checked the shared
     `Initial Data` glossary snippet too). **Initial Data** = the data sent when a run is started, e.g. an
     API call's payload; when a *trigger* starts the flow, the trigger's data lives on the trigger block,
     NOT in Initial Data. (Mark, repeatedly.)
   - **SHOW every main documented concept with a screenshot** — "the image files exist / it lints" is NOT
     the bar. Each main concept/action on the page gets a real shot of its real scenario.
   - **One concept per section.** Never combine two distinct concepts under one heading (e.g. don't merge
     "missing anchor" with "how long memory lasts"). Split them; title each for its own takeaway.
   - **The lede states the ordinary contract and the transport, never an edge case (Mark, 2026-08-24,
     3/10: "Not a word about GET or POST ... you go into the weeds ... of Release Caller (WHO CARES AT THIS
     POINT????)").** An API lede names the method(s) the reader will send (one GET or POST request) and
     gives the mental model in one breath ("turns a flow into a plain HTTP API ... same round trip").
     Toggles, exceptions, and special modes NEVER appear in the lede - they live in their own sections.
     When a review finds the lede's plain claim technically contradicted by an edge case, fix it by
     wording the claim so it stays true ("returns the flow's answer as the response body"), never by
     naming the edge case up top - precision repairs apply at the LOWEST possible altitude.
   - **A call, trigger, event, or schedule starts an INSTANCE, never "the flow" (Mark, 2026-08-24:
     "A flow MUST BE started in order for Call Flow to work. The API starts an instance. It is an
     importan[t] distinction").** "Start the flow" is reserved for the ((Start flow)) action that makes a
     version LIVE - the precondition. What an API request, trigger firing, or schedule tick starts is an
     instance (a run) of the flow: write "starts an instance of the flow" / "starts a run". doclint warns
     on actor + "starts the/a flow" (`flow-vs-instance`).
   - **The lede TEACHES by linking the reader's artifact to the feature (Mark, 2026-08-24, second lede
     round: "An educational approach would say this: 'if a flow has Return Result, to get it, use the
     blocking call - the result returned by Return Result is what's delivered by this API'. Is it really
     that hard????").** Open on the thing the reader BUILT and state the feature as the way to get/do
     what they want with it: "If a flow has a Return Result block, the blocking Call Flow endpoint is how
     your code gets that result." The product-level abstraction ("turns a flow into a plain HTTP API")
     never leads - it follows as a consequence, or is dropped. Test: does sentence one name the reader's
     artifact as its subject and answer their question about it?
   - **An API page never makes the reader think about mechanics (Mark, 2026-08-24, Call Flow: "The
     format makes reader think - this is a huge problem. Forcing someone to think brings useability
     down.")** Three concrete bans that follow: (1) **never base-URL + relative-path** - every endpoint is
     shown as ONE full copy-ready URL, and every example is complete and runnable as pasted; (2) **one
     call shape per section** - GET and POST each get their own section with their own complete example
     and their own data rules; never interleave "on a GET ... / on a POST ..." conditionals in shared
     prose or an "applies to" column; (3) **no swiss-army pages** - one page per call/use case (blocking
     and non-blocking are separate pages); a page that forces a mid-read choice between calls gets split.
   - **A section index that only routes is a hop, not a page (Mark, 2026-08-24: api/index.md "is
     excessive and may cause confusion").** The nav labels and each page's lede already do the routing; a
     "which page do I need" hub duplicates them and adds a click. Kill the hub and make every page in the
     section fully self-contained - shared fragments (an error-code table, a credentials pointer) are
     duplicated into each page or moved to their one canonical home, never parked on an index the reader
     must detour through.
   - **The ToC is a navigation surface with a BUDGET (Mark, 2026-08-24, Call Flow: "the TOC has 30
     entries ... impossible to navigate").** Headings exist for the reader scanning the ToC, so a page
     carries roughly a dozen ToC entries (h2 + h3), never dozens. Reserve h3 for a genuine reader
     destination ("what happens on timeout?"); a mechanism, a parameter group, an example, or an error
     group inside a section is a **bold run-in** (`**Headers.** ...`), not a heading. When a reviewer
     asks for "an anchor per idea" and the ToC would exceed the budget, the budget wins — and if the
     content genuinely needs more destinations than the budget allows, that is the page-split signal
     (§0i), not a license for a 30-entry ToC. One-concept-per-section (above) is about not MERGING two
     concepts under one title; it is not a mandate to promote every paragraph to a heading.
   - **Verify every UI location IN-PRODUCT; never guess where a control lives.** ("gear in the editor
     toolbar" was wrong twice — the Flow Memory settings are the right-hand panel's ⚙ Settings tab.)
     Drive the product and look; the product owner's word also counts. See [[flowrunner-flow-memory-settings]].
   - **Expression syntax is not copy-pasteable.** `{{...}}` references and `{{+}}` operators are tokens you
     build in the Expression Editor by picking them; do not present the rendered string as text to type/paste.
   - **Don't answer questions no one asked** (defensive lines like "a Read does not change the store").
   - **"Lints clean / files exist" ≠ done.** Judge against the STANDARD OF CARE and this checklist, never a
     checkbox. Report status honestly; surface what is unverified rather than self-certifying.
0e. **EVERY PARAGRAPH passes the quality bar** (Mark, 2026-07-04 — the deepest correction; a page can be
   structurally clean and still read as "someone indifferent to the product, doing their job, no pride").
   Quality is not un-checkable — it is checkable *per paragraph*. Interrogate every paragraph, heading, list
   item, and admonition against five questions; any failure is a defect to rewrite, not ship:
   - **Useful** — earns its place; not filler or restatement a reader could skip with no loss.
   - **Structured** — one clear point, well-formed, in the right place.
   - **Teaches** — advances understanding (a model, a how/why/where), not a flat statement of fact.
   - **Builds on prior knowledge** — uses what earlier Learn-nav pages taught; no re-explaining, contradicting,
     or forward-referencing machinery not yet introduced.
   - **Engaging, not boring** — reads as someone who knows and LIKES the product; concrete and alive, not
     indifferent box-ticking a reader's eyes slide off. Flat competence is a FAILURE, not a pass.
   The bar is the approved exemplars (Variables, Expression Editor). The `concept-page-review` gate now runs a
   per-paragraph quality lens for exactly this.
0f. **A screenshot must DEMONSTRATE its section's concept — and the reviewer READS the pixels** (Mark,
   2026-07-04 — a shot of a setting's DEFAULT slipped past FIVE reviews under a section teaching the NON-default,
   because the reviewer trusted the author's alt text instead of looking). The image must SHOW the real scenario
   in action (an anchor actually set to a caller id; a value actually written), never a default/empty/related
   panel. Judge the picture by opening it, not by its alt text; confirm the alt text matches the pixels.
0g. **Recurring corrections, round 2 (Mark, 2026-07-06 — Subflows review; the gate missed all of these):**
   - **EXERCISE the whole surface before you write — click every toggle, open every dropdown, read every mode.**
     Never document a control from one static screenshot. If a page names a toggle (Compose Result) or a
     dropdown (Content Type), it must document ALL of its states/options (JSON *and* XML *and* Plain Text; the
     toggle ON *and* OFF), because you actually drove them. Keep a per-page product-exploration LOG (an HTML
     comment) of what you clicked and saw. This is the rule the Return Result failure broke — an EXISTING rule.
   - **Internal coherence + example CONTINUITY.** A section's example must match its own framing (no jump from
     an "Initial Data" framing to a "variable" example without connecting them), and do not mix a feature's
     INPUT and OUTPUT in one section. **Continuity:** when the PRECEDING section (or its screenshot) sets up an
     example that gives a good basis, a consecutive section must BUILD ON that same example, not introduce a
     fresh unrelated one. This is NOT "one example per page" — unrelated/non-consecutive sections may differ;
     the defect is breaking a running walkthrough (Get New Token → suddenly status/amount → back to token).
   - **Precise product terminology.** Use the product's exact word; never borrow one that names a DIFFERENT
     product feature. "Reuse" (why you make a subflow) is not "repetition" (which is the Repeat / List Iterator
     blocks). A term collision is a defect.
   - **State the SCOPE and its escape hatch.** A feature page names the boundary of the feature and what to use
     beyond it (a subflow is flow-scoped, not shared across flows → Call Flow / Flows as Actions for cross-flow).
0h. **Recurring corrections, round 3 (Mark, 2026-07-08 — Agent Memory / Error Handling / Flow Scheduling review):**
   - **Educational quality over word count — never lump distinct mechanisms into one "how it works" intro.**
     Flow Scheduling's intro folded the Start/Stop Scheduled Runs blocks into the core "what a schedule is"
     explanation "for word count". Each distinct mechanism gets its own paragraph/section, introduced where it
     is relevant. If you catch yourself padding an intro, split it. (Sharpens 0d "one concept per section".)
   - **Lead with the PRIMARY / manual control; a convenience is not THE mechanism.** Don't position a
     programmatic convenience as the way to do a thing when a simpler manual control exists. Scheduled runs are
     paused/stopped with the LIVE version's own Pause/Stop controls (the manual, primary way); the Start/Stop
     Scheduled Runs blocks are only the programmatic equivalent for doing it from inside a flow. Manual/primary
     first, convenience second — and never imply the user must build a second flow to do something the UI does.
   - **Never assert reader difficulty you can't substantiate.** No "the piece that trips people up", "people
     find this confusing", "the part everyone gets wrong". You have no evidence, and (Mark) a printed timetable
     being a different thing from a plane actually flying does not "trip people up". State the fact plainly; drop
     the invented struggle.
   - **No tautologies / useless cause-effect.** A sentence whose conclusion merely restates its premise teaches
     nothing — "because the schedule rides on one version, that version is the one that runs on it" is "because
     you put sugar in the water it tastes sweet". Cut it, or replace it with the real, non-obvious fact.
   - **Verify PROPAGATION / INHERITANCE / GATING behavior — don't guess it, and test it when you can.** "A
     cloned version does not inherit the schedule" was WRONG (a clone copies the schedule). Any claim about what
     carries over, what gates what, or what a policy affects is verified against the CURRENT product; the
     product's OWN legacy docs (`flow-management/`, `flow-execution/`) are a valid cross-check for *behavior*
     (they settled clone-inheritance, the Pause/Stop controls, and schedule activation). When behavior is
     testable, TEST IT: a throwaway flow + a real Call Flow REST call proved "Allow only scheduled flow
     instances" rejects an API launch ("Flow can be called only by scheduler."), and flipping it off accepted it.
   - **When a feature changes how runs are created, answer it for EVERY start path (trigger / Call Flow API /
     schedule).** Extends 0d: not only "never frame the start as a trigger" — whenever a policy/feature alters
     instance creation, spell out its effect on all start paths. "What about launches via API?" must already be
     answered on the page.
   - **Use the product's EXACT term.** "START a version → it becomes LIVE", never "Publish" (there is no
     publish). Extends 0g's terminology rule with this specific collision.
   - **Attribute platform-managed work to FlowRunner, not "the agent" / "it".** When the system does something
     automatically (loads and saves an agent's Messages History in Shared Memory), say **FlowRunner** does it —
     so the reader never thinks they must manipulate the agent's prompts or the store themselves.
   - **A screenshot must point out WHERE, not just crop the control**, and sit at the FIRST mention. Show the
     control in its panel/tab context so a reader can find it (the Flow Memory shot shows the right-hand
     panel's ⚙ Settings tab, not just the three fields). AND the specific control your prose NAMES must be
     visibly IN the frame, not just its neighbors — the first recapture cut off the very gear tab it named and
     I certified it anyway. Read the pixels against your own words before you accept a shot you made. See
     [[docs-screenshot-at-reference]]. (Note: at DPR≠1, Playwright clip/element screenshots drift horizontally
     and silently crop the right edge — capture full-viewport and crop the PNG in device px instead.)
   - **Precision over hedging.** Don't write "roughly every 30 seconds" when the cadence is exactly what you
     set. Drop unearned "roughly / about / around".
   - **"Things to watch for" is for gotchas and pitfalls ONLY — core concepts go in the main body** (Mark,
     2026-07-09). The Flow Execution Policy options (how a schedule gates triggers and the Call Flow API) were
     core concepts wrongly parked in the gotchas list; they belong in their own titled section. If a "watch
     for" item is actually teaching a concept rather than warning about a trap, promote it to a main-text section.
   - **Each distinct mechanism gets its own section AND an example that fits it** (Mark, 2026-07-09; extends 0h's
     "don't lump distinct mechanisms"). Don't tuck a second mechanism into an unrelated example as an aside — the
     programmatic Start/Stop Scheduled Runs story did not belong in the polling Example. And don't force an
     ill-fitting framing onto it (a "maintenance window"); write the example that actually motivates the
     mechanism — a self-terminating poller the clock cannot schedule shows *why* you'd start/stop runs from a flow.
0i. **Recurring corrections, round 4 (Mark, 2026-07-09 — BUILD-section reasoning review):** extends §0's
   lede-level "open on value/outcome from the builder's seat" up to the **page-boundary / information-architecture** level.
   - **Organize by the READER'S worldview, never by the product's structure.** The reader does not care
     what we have (the block inventory) or, mostly, how it works — they arrive to FIX A SPECIFIC PROBLEM and
     to MAP the model already in their head (how decisions get made, how information flows, repetition,
     waiting, failure) onto how FlowRunner runs. Producer-side facts — what blocks exist, how they work,
     avoiding doc duplication, altitude layering — are the MACHINERY that serves that mapping, NEVER the
     organizing axis. (I built a whole fold-rationale on those and missed the reader entirely; Mark corrected it.)
   - **A SECTION mirrors one coherent region of the reader's worldview; a PAGE answers ONE reader
     question** (Mark, 2026-07-09, round 2 — the first encoding of this rule said "test a page boundary …
     NOT by page length", which was itself an over-rotation Mark caught with a usability forecast). "Flow
     Control" is a nav *section* because "how decisions get made and how information flows in the real
     world" is one chunk of the model the reader already carries; its short index page carries the map
     (which page answers which question, plus routes for questions whose answer lives elsewhere), and each
     child page answers ONE question ("How do I loop?") at the scale of the approved exemplars (~50–75
     lines / 3–6 shots — Variables, Expressions, Subflows are the calibration). A page that needs h4s or
     folds several reader questions SPLITS. Page length and findability ARE boundary tests at the page
     level; the worldview test applies at the section level. Coherence comes from adjacency + the index
     map, never concatenation. See [[docs-reader-worldview-first]].
   - **Maps, page names, and framing are reader QUESTIONS, never block-vs-block comparisons** (Mark,
     2026-07-09). The reader asks "How do I loop?" / "How do I handle a collection?" — never "Repeat vs
     List Iterator" (they don't know two blocks exist). Where blocks overlap, the question framing itself
     routes to the right tool; don't manufacture rivalry between blocks that answer different questions
     (Condition and Value Router are rarely either-or in a real flow — they compose).
0j. **Recurring corrections, round 5 (Mark, 2026-07-10 — first BUILD page, branching.md):**
   - **Example blocks must plausibly DO the job the example claims.** Never wire a block to a task it cannot
     perform to fill a slot (a Set Variables named "Process Order" — a reader wonders how setting a variable
     processes an order). Pick the block a real builder would use (an HTTP Request that submits the order, a
     Call Flow to the fulfillment flow). Example FIDELITY, not just structural correctness.
   - **Warn when a screenshot shows a state that only appears AFTER an action.** A freshly dropped Condition
     shows no Yes/No exits until it is selected/connected; a shot of the wired block, with no note, makes a
     reader who just dropped one think it is broken. Show the useful state, but tell the reader the initial
     state differs and what reveals it.
   - **Show a control the FIRST time the prose sends the reader to it** (reinforces §0d / [[docs-screenshot-at-reference]]).
     Naming a field ("open Value to Check … with the icon at its right edge") with no shot of that panel yet
     reads as disconnected. Put the panel/field shot at first reference, before drilling into a sub-editor.
   - **Rule out contamination from your OWN test history before calling an anomaly a product bug.** A boolean
     type-mismatch warning I "verified as a bug" was an artifact of flows I had poisoned with earlier
     mistyped debug runs; Mark's clean flow showed none. Reproduce on a genuinely fresh slate (a new flow,
     no prior runs) before concluding — and never over-claim a bug. Extends [[docs-verify-behavior-empirically]].
   - **Don't teach a known bug as intended behavior.** When a surprising behavior might be a bug, confirm with
     the product owner before documenting it (the "adding a part resets connectors to AND" reset was a bug
     being fixed — documenting it would have taught readers a soon-dead quirk). Ask; don't enshrine.
   - **Before using a common word in prose, check it is not a glossary/snippet term that renders a DIFFERENT
     meaning** (e.g. "connector" has a snippet that reads unlike the AND/OR chip meant here). Extends §0g's
     term-collision rule to ordinary words, not just block-name clashes.
1. **Quick interview with Mark first** (his chosen cadence). 2–4 questions: the concept's ROLE in the
   system in one line; what the reader must already know and from which prior page; the ONE idea they
   must leave with; anything commonly misunderstood. Don't draft the frame cold.
2. **Map the reader's prior knowledge** from the pages that come BEFORE this one in the LEARN nav
   (Workspace → Flows & Instances → Triggers → Blocks → Variables → Expression Editor → Subflows →
   Shared Memory). Build on those terms; never re-explain, contradict, or forward-reference. Record the
   map in the page's ledger. (E.g. by Expression Editor the reader already knows from Blocks: results,
   the **alias** / Reference Result Data As, **Flow Context**, "wired for order, not for data.")
3. **Lede opens on VALUE/OUTCOME, bridging from that prior knowledge** — what the builder's automation
   gets to DO, in concrete real-world terms — not a definition, not the UI, not the flow's data-plumbing.
   Then the mechanism (the how) follows, and the operations/SHOW after that.
4. **Re-scan EVERY section opener the same way** — no section may open on the machine either; the
   value/purpose leads, mechanics follow.

Mechanics are never the opener. If a lede could open an architecture spec, or a manual for someone who
can't see the screen, it's wrong.

0j. **New failure classes (2026-07-09 concept-page-review red-team lens, Agent Memory / Error Handling / Flow Scheduling):**
   - **Combination-state coherence.** When two controls in the same panel can be enabled together AND a
     screenshot shows them both on, the prose must state what the COMBINATION does — not just each control in
     isolation. (Flow Scheduling: the shot showed both Flow Execution Policy checkboxes ticked; one says "the API
     is refused," the other "the API can still start a run" — a flat contradiction until the page reconciles them
     as a timeline. If two options read as opposites, the reader needs the window each one governs.)
   - **Cross-page control consistency.** Sibling concept pages that link to each other must show the IDENTICAL
     value-form and control label for the same control. (Agent Memory showed the Memory Anchor as bare
     `customerId` while its linked Per-User Memory taught `data.customerId`; and one page's "Flow Settings" tab
     was the other's "Settings" tab. A reader who follows the cross-link can't tell which is right. Reconcile to
     the live product truth on BOTH pages.)
   - **Sample data must match the guidance built on it.** When a page tells the reader to surface a caught-error
     (or any) field to end users, the SAMPLE value shown for that field must itself read as an actionable,
     human-facing reason — or the prose must flag that it may be raw/internal. (Error Handling said "lean on
     message" while the only sample message was a raw JS TypeError; a builder wiring a notification straight from
     it would surface a stack-trace fragment to a person.)

## Structure
1. **Lede leads with what the user's LOGIC does with the thing** — the operations/capabilities,
   tied to real automation needs, NOT "here's what it is." (Variables: "set a value aside, build on
   one - stitch a name into an email greeting, add one to a count - read it, clear it.") Write for a
   reader who is NOT assumed to be a developer.
2. Then **what it is** (one tight definition), then the operations **each in its own section**
   (write / read / change / …), then **lifetime / limits**, then the **escape hatch + Related**.
3. The page is built from the USER's questions ("how do I save a value? read it? update it?"), made
   scannable — not a feature inventory.

## SHOW it (the #1 repeated demand)
- Every section that names a UI surface gets a **real screenshot of the REAL named scenario** (the
  actual block/value the prose describes — not a placeholder). Variables: writing panel, the
  read-back pill in the editor, the increment block+panel.
- HYBRID capture: I capture repeatable in-product shots via `tools/shots/` (crop + PII-redact +
  recipe); Mark captures fiddly/branded ones from numbered `SHOT-FOR-MARK` shot-lists embedded in
  the page source. A screenshot-coverage WARN on a section is the honest "shot still pending" signal.

## Styling (VOICE.md — never bold a UI component or a block)
- **Block references → green pill**: `[Set Variables](../../reference/set-variables.md){.fr-block}`
  — on EVERY page (Mark 2026-06-25, supersedes the old links-only rule).
- **UI controls you press** (buttons/toggles/fields/dropdowns/dialogs) → `((Label))` chip (`.fr-control`).
- **Field labels you read / section names** → **bold**. **Concepts** → dotted glossary tooltip.

## Substance
- Examples human-readable (names with spaces, real scenarios: `Reply Greeting`, `Items Checked`).
- **One worked example**; push reference mechanism (config catalogues, exact syntax, modes,
  envelope shapes) to the block reference pages.
- **Verify-then-write**: confirm every behavioral claim in-product before writing. The product
  owner's word counts as verification (e.g. "remove = set empty"). Don't assert a mechanism you
  haven't seen.
- One term per idea (no "named container" twice); break dense sentences; ™ once near the top;
  spaced hyphens, never em-dashes.

## Done
- Page is "done" only when its ledger section is fully checked with evidence, gate is 0 errors,
  shots are in (or precisely listed for Mark), and Mark signs off. I never declare "done" against
  doclint or a generic reviewer.
