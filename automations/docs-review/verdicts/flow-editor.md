# Verdict: content/build/flow-editor.md (Flow Editor)

## 2026-10-06 - release sweep "Without version/devtasks2" + "without3"

- Verdict: **major-rework** (concept-page-review wf_9be5a87f-593, one run; not re-run). Mark decides ship.
- Scope: FR-914 (one editing session; Session dialog with START EDIT / STAY IN VIEW MODE). Driven on dev 2026-10-06 with two
  tabs of the same staff account; prod re-drive owed.

### Release delta - resolved after the gate (all driven on dev 2026-10-06)
- Item 4: "That is the single most common thing to get stuck on." deleted.
- Item 5: the bullet promoted to its own h2, "When the version is open for editing somewhere else", after "Change a flow
  that is already live"; lead-in before the shot; the shot is named as the own-tab variant; teammate variant in its own sentence.
- Item 6: chips in on-screen caps, ((START EDIT)) / ((STAY IN VIEW MODE)).
- Item 7 (partial): floweditor-session.png recaptured as a clean element shot (no focus ring, no backdrop). Teammate variant
  is still SOURCE (FR-914 engineer comment + bundle string) - the page says only that it names the teammate and email.
- Item 8: displaced side driven - red "Error" toast "It looks like you have started a new flow editing session. You are in
  view mode now." Way back driven - clicking ((Edit)) in the tab row brings the dialog back. Both on the page.
- Item 9: lock scope driven - it is PER VERSION (a clone, Version 2, was editable while Version 1 was held). Page now says
  "Each version has its own session, so a clone and its original can be edited at the same time."
- Item 10: "nothing lost" scoped to "every change is kept the moment it is made"; unapplied Expression Editor work NOT driven.

### Owed on prod (batched session)
- Re-drive the two-tab case and recapture floweditor-session.png from prod (item 7).
- Items 2 + 13: palette and areas shots still show the AI ASSISTANTS group (gone on prod; confirmed absent on dev today as a
  customer) and Mark's email; LIVE shot predates FR-3467.

### Older debt carried
- Alias shot shows the default alias (1); ledger stale (3); block container round trip (11) and its two absolute claims (12);
  zero-downtime claim (14); first-block heading (15); unwired-block gotcha vs red badge (16); cross-link repetition (17);
  lightning icon behaviour vs testing.md (18); notready shot (19); icon row / SLA icon / Start flow (20, 21); pick-before-run (22);
  panel-top order (23); delete vs references (24); removeconnection shot (25); Ready order (26); running example set-up (27);
  alias token / layout line (28); ™ + Related (29); router exits / fan-out / INT decimals / action-first starts (30-32); nit (33).

---

# Verdict — build/flow-editor.md ("The Flow Editor")

**Date:** 2026-07-24
**Gate verdict (run 1):** `major-rework` — 32 findings, 9 blockers.
**doclint:** 0 errors / 0 warnings.
**Status:** blockers cleared; a short carried list remains (below). Not handed off as done.

## How the gate ran
`concept-page-review` on `build/flow-editor.md`, 7 agents, four lenses plus red-team. It independently
confirmed the screenshot defects Mark had already caught by asking "what QA did you do on that image?",
and found two content defects that mattered more than the images.

## Blockers — resolved
1. **Safety: the page said building was inert.** Lede claimed "Nothing is running while you do it" and the
   test section said run block runs "against test data" — but a test run performs the action for real
   (`testing.md`: "testing a Slack or Send Email block really sends the message"), and the page's own log
   recorded that run block issued the real HTTP call. **Fixed:** the consequence is now stated inline
   before the link to Testing, and the lede no longer claims inertness.
2. **Safety: taught the practice the sibling disrecommends.** Page said to stop a live flow and edit the
   draft; `running-flows.md:48` says "you do not edit the live version in place… Clone the live version,
   change and test the copy, then Start flow on it." **Fixed:** leads with clone-edit-start; stopping is
   the secondary route, with the downtime stated.
3. **`floweditor-place.png` showed nothing** — subject cropped out of frame, alt asserted three things not
   in the picture. **Replaced and verified.**
4. **`floweditor-test.png`** — tab clipped to "ults", no Input heading, 40% unrelated settings panel.
   **Replaced and verified.**
5. **`floweditor-areas.png`** — first block clipped at the frame edge, tabs cut mid-word, minimap in frame.
   **Re-staged (canvas panned + zoomed) and replaced.**
6. **`floweditor-palette.png` alt named four groups not in the picture.** **Palette driven end to end**
   (nine groups confirmed; no Marketplace affordance exists any more), recaptured with all groups visible,
   alt now names only what is in frame.
7. **Per-block error badge had no shot** though the page taught it. **Added**, on the example's own Get
   Order block, badge open reading "URL is required".
8. **LIVE read-only asserted twice, shown nowhere.** **Added**: View tab, Live badge, palette absent.
9. **No ledger section and no verdict on disk.** **Both added** (this file; ledger entry before the
   Run & Monitor section).

## Majors — resolved
- Lede opened on the machine → now opens on the outcome the example delivers.
- "Working areas" narrated geography → reframed by the job each area does, and the panel's three tabs are
  named (fixing the "how do I get back to the palette?" dead end).
- "Things to watch for" was three restatements → replaced with real traps (an unwired block silently
  holds the version at Not Ready; a Condition forks, it does not fan out).
- Section order taught renaming *after* a shot that already showed renamed blocks and a renamed alias →
  **Name and arrange** now precedes **Type a value**.
- Expression mechanics re-taught what `expressions.md` owns → trimmed to the editor-specific fact.
- The link-icon shot showed four affordances without saying which → prose and alt now name the green
  chain icon.
- A result alias was dressed as monospace `code` → now the expression token.
- Dropped an example I could no longer reproduce (a Condition with no exit wired did not re-trigger the
  validation error once the block was parented).

## Decisions recorded
- **Page scale (Mark, 2026-07-24): keep ONE page.** It is a single orientation read of one working
  surface; tighten by cutting what siblings own rather than splitting. This satisfies the split check
  pre-registered in BUILD-SECTION-PLAN unit 1.
- **Value Data Type INT (Mark, 2026-07-24):** correct as configured for the worked comparison; example
  unchanged.
- **The tour stays (Mark, 2026-07-24):** its job is to introduce the areas' names, which the rest of the
  documentation uses. The guard against narration is "name → what you do there → shot", never an
  inventory.

## Verify-in-product gaps — CLOSED (2026-07-24, round 2)
- **Renaming is safe, and my page said the opposite.** Renamed Get Order to Fetch Order: its alias became
  `Fetch Order Result` **and the downstream reference in Check Total re-pointed itself**. Version stayed
  Ready. The page's "rename early, before anything points at it" caution was wrong and now states that
  references follow the rename.
- **Edits autosave.** Renamed a block, navigated away to another flow and back with no save action - the
  change persisted. There is no save control in the editor. Now stated on the page.
- **Ready gates going live.** With a required field cleared, ((Start flow)) is *disabled*
  (`disabled=true`, `cursor-not-allowed`) and clicking does nothing. The page now says so.
- **Deletion** now has its own section and the real "Delete block confirmation" dialog shot, captured on
  the example's own Check Total block (then cancelled).

## Scope ruling + late verifications (2026-07-24)
- **Guided first-flow build → Quick Start** (Mark). This page stays a mechanics reference, organisation
  as-is. Recorded in BUILD-SECTION-PLAN unit 1 so it is not re-litigated.
- **Duplication cut** against the pages that own the material: the side-effect warning (was near-verbatim
  `testing.md`) compressed to one clause + link; the palette category enumeration dropped (`blocks.md`
  owns it); the rename rationale dropped (`blocks.md` owns it), keeping only the editor consequence.
- **No undo - PARTLY verified here, over-claimed on the page.** Only a *move* was driven (Cmd+Z did not
  revert it), but the page went on to assert that a rename and a deletion are equally irreversible.
  Closed properly in round 3 below.
- **Container section deepened** and routed to Repeating Steps / Working Through a List, which own loops.
- **Changing which block runs first - NOT VERIFIED, deliberately off the page.** The Start marker's
  connection is not a `react-flow__edge` in the DOM, so it offers none of the normal connection controls,
  and the mechanism is not discoverable by inspection. With no undo available, probing it destructively on
  the example flow was not worth the risk. The legacy original documents it only via an Arcade embed.
  Carried.

## Round 3 (2026-07-27) — three claims I wrote without observing

Mark asked why I was raising "the green chain icon" and "undo" at all. Fair: all three were sentences
**I had put on this page**, each stating a consequence I had never watched happen. Same root cause as the
image failure — writing the consequence instead of driving it.

1. **"the green chain icon"** — the chain takes the *block's* colour. This page's own two shots prove it
   (green on the HTTP Request, gold on the List Iterator), and the example's Condition is pink, so a
   reader wiring it would hunt for a colour that is not there — on the page's core gesture. Rewritten to
   shape + corner, with the invariant stated. No recapture needed.
2. **"Nothing reverses a move, a rename, or a deletion"** — generalised from one test (Cmd+Z after a
   move). Now driven properly: Cmd+Z and Ctrl+Z after a real block deletion restored nothing (nodes 2,
   edges 0, Not Ready); Cmd+Z in a focused name field does character-level text undo *in that field only*;
   and no undo affordance exists — the toolbar's five controls are Start flow / Schedule / Clone / Export
   / Run Instance, block and canvas have no context menu, and nothing in the DOM carries undo or redo in
   its title, aria-label or class. Bullet rewritten to exactly that.
3. **Delete consequences** — I had opened the confirmation dialog for the screenshot and *cancelled*, then
   written the consequences. Now observed on a clone: before 3 nodes / 2 edges / Ready → after 2 nodes /
   **0 edges** / Not Ready. Both edges go, and only the **downstream** block is left parentless ("Block
   should be connected with it's parent"); the upstream block is fine, still held by Start. My prose said
   "the blocks it sat between", plural — corrected. The dialog shot also moved up to sit where the prose
   first names it.

**Test hygiene:** both probes ran on throwaway clones (Version 2, then Version 3), never on the shipped
example. Both were deleted afterwards; Order Check is back to a single Version 1 / Ready matching every
screenshot on the page. Verified in the header and on the canvas after each cleanup.

## Round 4 (2026-07-27) — Mark's review: the page yanked the reader around

Mark's central finding was structural, not line-level: *"You are all over the place, there is no common
thread, I do not feel like you're walking me through, I feel like you're yanking me from one spot to
another."* The tour front-loaded the toolbar, the Test Monitor, the LIVE read-only state and the
clone-edit-start rollout **before the reader had placed a single block**, and taught what happens when you
select a block before anything had been added to select.

**Fix: every area is now introduced where the reader uses it.** The tour names the four areas and stops.

| Was | Now lives in |
| --- | --- |
| panel switches to settings on select (in the tour) | Place a block — after you place and select one |
| toolbar + version status (in the tour) | Get the version to Ready, with the toolbar shot |
| Test Monitor detail + forward link (in the tour) | Test a block without going live |
| LIVE read-only + clone-edit-start (in the tour) | Change a flow that is already live (new closing section) |

Line-level corrections from the same review:

- **Colour removed entirely.** Mark: *"Does it really matter to the user what color it is drawn in?"* — no.
  Round 3 corrected green→"green or gold"; the right answer was to drop colour and name the control by its
  own tooltip, **Drag to connect with another block**. Verified by hovering it.
- **The flow model was missing at the one point it was needed.** "Connections decide what runs next" now
  opens with what actually happens — a block does its work, hands its result on, and the connection decides
  who receives it — instead of arriving later in the paragraph.
- **"Blocks that split the path label their exits"** was replaced with the real list: a Condition has Yes
  and No; a Value Router and an AI Router have one connection per branch you name; the canvas labels each.
- **Alias claim was unqualified and wrong.** The page said renaming a block renames the result alias, full
  stop. Mark: *"not unless user assigned a custom alias - we do not overwrite it."* Verified: **Reference
  Result Data As** is a checkbox, off by default, with a greyed auto-derived `<Name> Result` beneath. Ticked
  it, typed `Big Order Check`, renamed the block `Check Total`→`Total Gate`: the alias did not move. Page now
  states both halves. New screenshot.
- **Multi-select was undocumented.** Shift+drag selects a rectangle; dragging one selected block moved both
  by an identical delta while the unselected one stayed put; Delete/Backspace raises a plural "Delete blocks
  confirmation" naming all of them. Delete and Backspace also work for a single block, which the page only
  taught via the panel button. New screenshot.
- **The block's own run icon was missing.** Mark asked for it: the play icon in the block's icon row reads
  **Run in test mode** and does the same thing as ((run block)). All four icons in the row were hovered and
  named; the lightning (**Run instance from this element**) is named and routed onward rather than
  described, since its run behaviour was not driven here.
- **"Some blocks cannot offer their fields until they have actually run"** read as if the *block* had the
  fields. Rewritten around the block's **result**.
- **Section title fixed twice:** "Try it before anything is live" was a poor link target for a testing
  section → "Test a block without going live"; "Name and arrange the flow so it reads" sounded incomplete →
  "Name your blocks and lay out the flow". No inbound links pointed at either old anchor.
- **The expression pill was not broken.** Mark quoted the raw `{{Get Order Result->total}}` from the
  markdown source; the build hook converts it, and the built page contains three real `fr-expr` pills with
  no leftover braces. Confirmed by building the site. His request for an admonition showing readers what the
  decoration means is now on the page, with a live pill inside it — verified in the rendered HTML.

## Carried, not dropped
- The container section's shot is from the Cart Summary flow rather than Order Check. The palette drag
  became unreliable mid-session, so a container could not be added to the worked example. The image is an
  accurate picture of the ((Expand)) control and its alt claims nothing more; the continuity gap is real
  and logged.
- Changing which block runs first is documented in the legacy original but still unverified.
- No Marketplace affordance exists beside the palette Search (legacy claim stale).
- ~~Example-flow state: "Flag Large Order" was deleted~~ **RETRACTED 2026-07-24.** It was never deleted.
  I inferred deletion from a DOM query of `.react-flow__node`, which only returns nodes React Flow has
  RENDERED - off-screen nodes are virtualised away. The minimap and a zoom-out both show all three blocks,
  the Yes edge intact, and the version Ready. The flow matches the shipped screenshots. Lesson: never
  assert product state from a node query alone; confirm with the minimap or a fitted view.

## The process failure worth keeping
I copied three cropped images into `content/images/` **without opening any of them**, on the strength of
their pixel dimensions, then wrote alt text asserting content I had never seen. Recorded as memory
`docs-read-every-image-back`. The check is claim-by-claim against the pixels, not a general impression —
I had *looked* at the palette shot and still shipped an alt naming groups outside the frame.
