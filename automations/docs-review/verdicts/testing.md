# Verdict: content/run/testing.md (Testing a Flow)

- Date: 2026-09-25 (release v.1.1.2 sweep)
- Verdict: **major-rework** (concept-page-review wf_8ae98858, 7 lenses, one run; not re-run per the one-net rule)
- Scope reviewed: the v.1.1.2 changes (new "Set a block's result without running it" section, Launch dialog typed
  values), with the rest of the page read for context
- doclint: 0 errors, 0 warnings; mkdocs build --strict: clean; anchor #set-a-blocks-result-without-running-it
  resolves

## Gate summary

38 items (9 blocker, 16 major, 11 minor, 2 nit). The release delta held up on facts but had three real errors:
- the example proved nothing: the hand-set 1500 took the same Yes branch as the real run
- "Block Results shows an empty Input" was wrong
- the new control had no shot and two names

The rest was older debt in sections this release did not touch. Red-team candidates:
- a chip whose label ends in ")" breaks controlify
- a feature that changes what a block yields must be answered for every run kind the page defines

## Resolution (same day, one consolidated pass)

| # | Sev | Item | Resolution |
|---|---|---|---|
| 1 | blocker | Initial Data framed as trigger-supplied | FIXED: rewritten as "an API call sends the id"; no trigger framing |
| 2 | blocker | flow vs instance ("triggers the flow") | FIXED: "start an instance", "a version was LIVE", "run straight through" |
| 3 | blocker | expression token inside backticks | FIXED: literal URL + {{Initial Data->cartId}} pill |
| 4 | blocker | Test Panel unnamed, no shot | FIXED: named once at first mention; new testing-test-panel.png (read back) |
| 5 | blocker | overview shot hid the No branch | FIXED: testing-flow-overview.png recaptured, both branches in frame, minimap hidden |
| 6 | blocker | example proved nothing | FIXED: re-driven with Desk Lamp 450 -> Condition false (No branch); new testing-manage-condition-result.png |
| 7 | blocker | Edit an Output has no shot, drops the example | OPEN (older section) |
| 8 | blocker | errors only a bullet; Logging tab never shown | PARTIAL: timeline bullet deleted; Error Output shot and Logging tab OPEN |
| 9 | blocker | ledger | FIXED: ledger block + this file |
| 10 | major | chip ")" collision | FIXED: "The ((Populate from Instance)) selector (optional)"; **Previous Instance** bold |
| 11 | major | chip case | FIXED: ((run block)), ((manage block result)), **Test Panel** |
| 12 | major | A-icon types contradict | FIXED: A explained once at Flow Data; Launch sentence scoped to that dialog |
| 13 | major | A click needed for the example | FIXED: "Type 450, then click the A so it turns dark" |
| 14 | major | "a run is real" came too late | FIXED: line added where Run Block is taught; side-effect bullet links the new section |
| 15 | major | Flow Context contradiction | FIXED: "the run's ids" |
| 16 | major | picker reason omitted | FIXED: driven (Expression Editor Block Data lists currency/topItem/topItemTotal); testing-manage-picker.png; http-request.yaml gotcha updated + refgen |
| 17 | major | how a hand-set result goes away | FIXED: "replaced when you save a new one, or when the block runs again" (a full launch replaced it, driven) |
| 18 | major | run kinds beyond run block | OPEN (launch-from-a-later-block not driven) |
| 19 | major | Populate from Instance empty on drafts | FIXED: boundary stated (runs from LIVE versions only) |
| 20 | major | list / single-value shapes | PARTIAL: JSON Editor paste driven; list and single-value shapes OPEN |
| 21 | major | linear framing | FIXED: lede "wired together"; "after the blocks that feed it"; timeline bullet gone |
| 22 | major | block names as chips | OPEN (older walkthrough; style call) |
| 23 | major | LIVE read-only, no way out | OPEN |
| 24 | major | "execution" for a draft launch | FIXED: "an uninterrupted run" |
| 25 | major | toolbar Run Instance missing | OPEN |
| 26 | minor | play-icon alt | FIXED: tooltip "Run in test mode" named in prose and alt (read back) |
| 27 | minor | Initial Data / control styling | PARTIAL |
| 28 | minor | Launch A default vs call-flow-blocking.md | FIXED: re-driven on LIVE Order Lookup - typed 1042 / true / {"a":1} default dark and go out typed; click -> green -> "1042"; call-flow-blocking.md rewritten to match |
| 29 | minor | dialog reopens empty | FIXED: "Block Results always shows it as the block's Output" (FR-3392 comment 79279) |
| 30 | minor | where Launch rows come from | OPEN (the Flow Settings Initial Data Description lists the same keys, seen on Order Lookup; not stated) |
| 31 | minor | billing clause repeated | FIXED |
| 32 | minor | transform Input described wrongly | FIXED: "the order's product list and the four property names" (from the pixels); alt rewritten |
| 33 | minor | "smaller cart" undriven | FIXED: clause dropped (the Manage section shows the No branch) |
| 34 | minor | connection-not-set reason undriven | OPEN |
| 35 | minor | Slack / Send Email sends for real | OPEN |
| 36 | minor | Test Monitor tab order, docked shot | OPEN |
| 37 | nit | metaphor, filler transition | FIXED |
| 38 | nit | "grey" vs dark | FIXED |

Mark decides ship.

## Second pass (same day, Mark: "apply fixes")

Tested on prod in Testing Demo. The gate was not re-run.

| # | Was | Now |
|---|---|---|
| 7 | OPEN | FIXED: Edit an Output re-grounded in the example. topItemTotal edited to 1000 -> the Condition returns false (boundary case, No branch). Two new shots; the edit persists across a reload. Scope stated: it reaches only blocks that read this block's result (Get Top Item Total reads the `Cart` variable - tested) |
| 8 | PARTIAL | FIXED: new "## Find the block that failed" section. cartId 99999 -> Get Order Error "Cart with id '99999' not found"; Logging tab shown and its controls tested. Filed FR-3660 (Low): the Logging timestamps are not zero-padded, and this is visible in the shot |
| 18 | OPEN | FIXED: a launch from the Condition runs only from that block on; the dialog pre-fills the upstream result the block reads (new shot, which replaces testing-launch-instance.png) |
| 20 | PARTIAL | FIXED for lists (Form View "Item" rows, new shot) and invalid JSON (SAVE disabled, "Enter valid JSON to save."). Single value: no such block in the example |
| 22 | OPEN | FIXED: custom block names un-chipped; "Get Top Item Total, a Custom Cloud Code block"; the Condition named once as its tab reads |
| 23 / 25 | OPEN | FIXED: LIVE version tested (View tab, no run icons, no Test Monitor, toolbar Run Instance = a real instance) plus the way out (clone). New shot testing-live-toolbar.png |
| 34 | OPEN | FIXED: with no connection, run block is disabled on the Slack block (tested) |
| 35 | OPEN | CUT: the Slack/Send Email "really sends" bullet was removed; "the run is real" stays where Run Block is taught |
| 36 | OPEN | FIXED: the Test Monitor has THREE tabs. Flow Context is gone (FR-3180, v1.0.11), so the page was wrong. testing-flow-context.png retired; new whole-editor shot testing-editor.png |
| lede | - | the lede's "rather than" was fixed |

Still OPEN: single-value result shape; the pop-out log icon was not clicked. Fixture: Get Top Item Total's Output holds the edited value (2000); Flow Data cartId 123.
