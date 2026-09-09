# Gate verdict — learn/concepts/placeholders.md

- **Date:** 2026-08-26
- **Latest gate run:** wf_664ee969-306 (round 30) → `major-rework`, four blockers. Cleared in round 31;
  re-gate pending. **NOT ship.**
- **Round 29 reached `revise` (no blockers)**; round 30 then found four, **two of them regressions I
  introduced in round 29**. See "The pattern" below — this is the third repair round to do that.
- **Current shape:** 8 h2 sections, 8 screenshots, ~175 body lines. Four screenshots retired across
  rounds 24-25.
- **Round 21** (wf_1a57df9d-69d) reached `revise` — no blockers — then round 22 found four more, three of
  them artifacts of my own round-21 edits. See "Where this stands" at the bottom.
- **Status:** **NOT ship. Do not present the page as done until this file says `ship`.**
- **doclint:** 0 errors / 0 warnings; site builds `--strict`.

## Rounds

| # | Run | Verdict | What it caught |
| --- | --- | --- | --- |
| 1 | wf_c81baa51-627 | major-rework | Lede opened on a definition; + dialog and type list unpictured; safety claim covered design-time only; install-time validation asserted from an unshipped ticket; no ledger |
| 2 | wf_5055ac03-f6b | major-rework | Probe artifacts as teaching material (`currencyKey` typed STRING under a weather-key description; a result reading `{"brand": 5}`); banned "published snapshot"; unverifiable cross-workspace claim |
| 3 | wf_811bb776-72d | major-rework | Example's API key was a borrowed OpenAI setup; worked example modelled the gesture the security warning forbade; block named only in alt text |
| — | **Mark, 2026-08-26** | — | (a) weather example wrong at the root — its placeholders varied per run; (b) I contradicted "API keys apply only to AI API keys"; (c) I asserted LIVE-version behaviour never observed |
| 4 | wf_72d755d7-247 | major-rework | Lede still leaned on the inert AI key; per-run line failed on trigger-started flows; `api-keys.md` carried a recipe FR-3443 makes impossible |
| 5 | wf_367c49ab-c49 | major-rework | Stale verdict file; evidence-free ledger clearance; silence about FR-3460; untested "every expression field"; `[object]` derivation disproved by the page's own pixels |
| 6 | wf_4f70b411-ce5 | major-rework | Enumeration mismatch (lede 3 / panel 4 / close 3); closing payoff promised a key nothing consumes; gear + trash described from icon shapes |
| — | **Mark, 2026-08-26** | — | "why invent a reason for Placeholder rather than describe the vision we came up with the concept?" — the page was reframed on the Catalog purpose |
| 7 | wf_c33c0aa0-abe | major-rework | Alt text not swept after the round-7 example change; "correct binding" shot carried the error badge the page teaches as the tell for a broken one |
| 8 | wf_059c1d93-090 | major-rework | Lede named the wrong actor ("whoever runs it"); Catalog stated in present tense with non-product verbs |
| 9 | wf_2a045deb-5c2 | major-rework | Lede absolute revoked by the AI-key paragraph; hand-off payoff contradicted by clone/export carrying the author's values |
| 10 | wf_25bdc1d3-f4b | major-rework | Expression references as `code` instead of the `.fr-expr` pill; import behaviour asserted from an export-only drive |
| 11 | — | — | (drives folded into 10/12) |
| 12 | wf_25bdc1d3-f4b | major-rework | Payoff section had no pixels; this verdict file contradicted the page |

## Round-12 blockers — cleared

| Blocker | Resolution |
| --- | --- |
| The payoff section — the one that reverses the safety net built above it — had no screenshot | **NOT cleared in round 13, and this row previously claimed it was.** The round-13 capture was a degenerate probe (empty canvas, "Not Ready" chip) and was deleted rather than shipped; the section then ran with no pixels at all until round 15. Corrected here because round 14's gate caught the file did not exist. |
| This file listed as "not driven" three things the page asserts | Rewritten. Rounds 6–12 added with drive ids; the not-driven list below is now accurate |

Also this round: the closing section's meta-commentary opener removed (same class cut in round 11,
recurring); the lede's duplicated hand-off claim collapsed to one sentence.

## Driven evidence

| Fact | Drive |
| --- | --- |
| Eight data types and their saved-row tags | B891988E |
| Type survives into the expression (`INT` → 8) | Ticket Triage probes |
| Loop scope: Placeholder Data group inside a List Iterator | B891988E |
| LIVE version opens in view mode with no tab strip | CD3F8A0B |
| Launch dialog's Placeholder Data section is inert (lands in Initial Data) | DE79A5E2, run 101CDF04 → FR-3460 |
| Gear reopens with name + type editable; trash confirms | A47E6D2B |
| Rename breaks bindings ("The placeholder data item is not available") | 9D713BEA |
| Empty value flags the reading field and disables Start | A47E6D2B |
| Export carries placeholder values; import restores them | 9F1B9B1F → D4AB6992; re-driven 4BF893CA → 8A6B1F32 |

All probe flows created for these drives were deleted; workspace back to 35 flows each time.

## Round-14 work (round 15 fixes)

| Blocker / major | How it was cleared |
| --- | --- |
| **Escape hatch pointed at Shared Memory as a workspace-wide store** — contradicted by the glossary, `shared-memory.md`, `variables.md`. My own error, introduced in round 13. | Rewritten: Shared Memory belongs to a single flow too, so it does not bridge flows; the hatch is now one flow owning the value and the others reaching it with Call Flow. |
| **Payoff section had no screenshot; the verdict file claimed a file that did not exist** | Root cause fixed rather than cropped around: the example flow was `Not Ready` because its Condition's branches were unwired. Wired THEN → "Escalate ticket" and ELSE → "Queue normally", so the flow is now **Ready** with no error badge anywhere. Re-exported, deleted the old probe, re-imported as "Triage (from Ops)", captured `placeholders-imported-prefilled.png`: breadcrumb naming a different flow, green Ready chip, complete canvas, all three values inherited. |
| **JSON fence was a hand-trimmed composite** | Replaced with the entry verbatim from a fresh export, `error: null` included, and the lead-in now names `flowVersion.metaInfo.executionStaticData`. |
| **Type-preservation claim driven on a different block; "needs no conversion" unfalsifiable** | Driven on the Condition itself and the claim was **partly wrong**. Launching with `urgency` from the launch form fails: *"'GREATER_THAN' operation requires all values be numbers. One of values is 'String'"*. The same comparison succeeds under ((Run Block)), so the placeholder is not the string — the placeholder does arrive as its declared type. Prose rewritten to say exactly that, and **Value Data Type** is now named: it picks the comparison, it does not convert either side. |
| **"Flow Settings" tab label asserted by no pixels** | Confirmed in-product: the three tab `title` attributes are exactly `Blocks List`, `Block Configuration`, `Flow Settings`. `build/data-and-variables/across-runs.md:46` is therefore correct too. |
| **Launch Flow Instance section contradicted `run/testing.md`** | Driven: the dialog's Placeholder Data section lists only the placeholders the flow actually reads (just `escalateAbove` on this flow), which is why `testing.md`'s screenshot of a flow without placeholders shows no such section. Page now states the condition; the exploitable "travels as Initial Data" semantic (FR-3460) was cut. |
| **LIVE claim had no pixels and was looser than what was driven** | Started the flow, captured `placeholders-live-view-mode.png` — a green **Live** chip, first tab reading **View**, and the entire right-hand side empty. Flow stopped afterwards; it is back to Ready. |
| **Empty-value Start gate stated unconditionally** | Scoped to what was actually observed: *while a block is reading an empty placeholder* the version cannot be started. |
| Section overload; lede shape; role named five ways; delete-dialog quoted without pixels; type-value formatting; Flow Catalog over-claim; API KEY told three times; crop hygiene | All applied. The LIVE/clone/launch material is now its own h2; the delete quote is gone; one role noun ("whoever sets the flow up"); Flow Catalog no longer claims type checking; the orphan ✕ is cropped out of two shots and framed as a real control in the third. |

## Round-15 work (round 16 fixes)

| Blocker / major | How it was cleared |
| --- | --- |
| **BLOCKER: the page documented its own worked example failing and offered no remedy** | Root cause found and it is a product defect, not a fact about placeholders. Driven four ways: launch-dialog form → FAILS (`'GREATER_THAN' operation requires all values be numbers. One of values is 'String'`, reproduced twice); the GET URL **the dialog itself generates from those same form values** → COMPLETED/NORMAL; POST with a JSON body → COMPLETED/NORMAL; ((run block)) → `{"conditionResult": true}`. So the placeholder is a number on every route and the form is the only producer of a string. Filed as **FR-3461**. The failure narrative is out of the page entirely — documenting a filed defect as behaviour is the FR-3460 mistake again — and the type section now carries `placeholders-condition-result.png` as its evidence. |
| **Two h2s carried four concepts each** | Split into nine h2s: the type rule, the version-scope boundary and the Flow Catalog payoff each got their own heading, so all three are reachable from the ToC. Still inside the ~dozen budget. |
| **Launch Flow Instance described, never pictured** | Captured `placeholders-launch-dialog.png`: the Initial Data table plus the Placeholder Data section holding `escalateAbove[int]` alone — the one placeholder this flow reads. |
| **LIVE teaching buried inside an admonition** | Lifted into prose; the admonition is gone and the section opens on the fact. |
| **flow / version / instance conflation in a heading** | Retitled to "Changing a value on a LIVE version"; "Launch this flow" removed. |
| **((Data Type)) options bolded instead of chipped** | All eight now chipped, plus the later mentions. **Value Data Type** stays bold — that one is a field label you read. |
| **Call Flow escape hatch did not solve the problem it was offered for** | Dropped. The boundary is now stated plainly: each flow declares its own, and Shared Memory does not bridge them either. |
| **Export safety advice collided with the page's own rule** | An empty placeholder a block reads makes the version unstartable, so "clear it before you export" hands over a broken flow. Now: replace it with a harmless stand-in. |
| Glossary scope; lede repetition; garden-path phrasing; plain-style flourishes; "whoever installs it" drift; ((run block)) case; crop hygiene on the dialog shot | All applied. `definitions.md:26` narrowed to "read through an expression by the fields that need it". |

## Round-16 work (round 17 fixes)

| Blocker / major | How it was cleared |
| --- | --- |
| **BLOCKER: the worked example declared three placeholders and the flow read only ONE.** `notifyChannel` and `notifyOnWeekends` were decoration; the page's own launch-dialog screenshot listed a single row, which is the evidence that exposed it. | Fixed in the product rather than the prose. Replaced the "Escalate ticket" Set Variables with an HTTP Request **Post summary to Slack** whose Body is `{"channel": {{notifyChannel}}, "text": "Escalated ticket"}`, and deleted `notifyOnWeekends`, which nothing read. The flow is Ready with two placeholders, both genuinely consumed: `escalateAbove` by the Condition, `notifyChannel` by the request body. Recaptured the panel, imported and launch-dialog shots — the launch dialog now lists **both**, which is the same test that caught the defect. |
| **BLOCKER: the launch-dialog shot pictured the exact configuration filed as failing (FR-3461)** | The `urgency` value box is cleared in the recapture, so the frame shows the dialog's structure without handing the reader a recipe that fails. |
| **Cloning taught as the only way to change a LIVE version's value** | Wrong, and contradicted `run/running-flows.md:46`. Stopping a LIVE version hands it back as an editable draft — driven twice this session. Both routes now stated with the trade-off (stopping is direct but the flow is down; cloning leaves LIVE running). |
| **Launch-dialog material filed under a LIVE heading** | It is not LIVE-specific. Promoted to its own h2, "Launching a run does not change the value". |
| **Read-only + version scope under one heading** | Split into "Nothing writes back to a placeholder" and "A placeholder belongs to one flow", and the scope section now answers the builder's real question (no workspace-level store; each flow declares its own). |
| **Query-string transport claim asserted with no mechanism** | Dropped. The page now states only the altitude that holds everywhere: whatever starts the run has to supply `urgency` as a number. |
| **Export remedy mutated the reader's working flow** | Re-pointed at a clone: clone, stand-ins on the clone, export the clone, delete it. |
| ((Value Data Type))/((Operation)) chips; plain-style flourishes; type-tag paragraph narrating the author's method; API KEY told twice; Catalog section title and bare "This"; Expression Editor link; **Flow Context** bold; trash narration | All applied. |

## Round-17 work (round 18 fixes)

| Blocker / major | How it was cleared |
| --- | --- |
| **BLOCKER: two screenshots were stale after the round-17 example change** — `placeholders-expression-editor.png` still listed the deleted `notifyOnWeekends`; `placeholders-live-view-mode.png` still showed the superseded "Escalate ticket" block. | Both recaptured. The Expression Editor now shows exactly two pills; the LIVE frame was re-taken with the flow re-started in its current shape ("Post summary to Slack" on the Yes branch) and the flow stopped afterwards. **My own fallout:** I changed the flow and swept the alt text instead of re-opening every image. |
| **`notifyChannel`'s consumption was asserted, never shown** | Captured `placeholders-in-request-body.png` — the HTTP Request panel with {{notifyChannel}} bound inside a JSON body, which is the harder and more interesting case than a reference alone in a field. The block is now named in prose with its `.fr-block` pill. |
| **The panel shot showed neither of the two controls its sentence names** | Recaptured wide enough to include the right panel's tab strip with the gear active. |
| **"Value Data Type beside Operation" contradicted by the page's own shot** | Read off the live DOM: Value to Check, Value Data Type, Operation, Value — top to bottom. Corrected to "above". |
| **"whatever starts the run has to supply urgency as a number" was broader than the drive supports** | The generated GET URL completed NORMAL with a query-string value. Restated to name the three routes actually driven. |
| **JSON fence flagged as never observed** | Not a defect. The gate cited the round-11 note (`description:""`); a fresh export today matches the fence byte-for-byte, key order included. Recorded so it is not re-raised. |
| Ledger screenshot box checked with descriptions the pixels disproved | Rewritten against the current pixels and **left unchecked** until a ship run. |
| Glossary collision on "Placeholder Data"; plain-style hits; type-tag mapping; scope-section title and workspace-store claim; description-is-optional guidance; restatements | All applied. |

## Round-18 work

| Blocker | Status |
| --- | --- |
| **Type-tag rule had regressed to a wrong derivation** — "the dropdown label in lower case" gives `[boolean / checkbox]` and `[json array]`; the driven tags are `[boolean]` and `[array]`. My own round-17 compression introduced it. | **Cleared.** All eight driven tags listed again, in dropdown order. |
| **"Setting a placeholder's value" never said where a value is typed** — the only control it named was the gear, which opens a dialog with no value field. | **Cleared.** The section now opens on the value control in each row, and says plainly that the gear's dialog is not where the value lives. |
| **The launch dialog was documented only in the negative** while the round-5 drive already owned the fact. | **Cleared.** The page now states that what you type there travels with the run as Initial Data under the placeholder's own name, and can land as a property the flow did not expect. FR-3460 is not narrated. |
| **The GET-route sentence contradicted `call-flow-nonblocking.md:68`** ("query values arrive as text"). | **Cleared, and the contradiction resolved by re-driving** — see below. Every route claim is out of the page; only the placeholder-side rule remains. |
| **The example hard-codes the Slack webhook URL** — the most secret, most per-deployment value in the scenario — directly under "neither value is typed into a block", while parameterising a channel name a Slack app webhook ignores. | **OPEN — needs Mark.** This is an example-design decision, not a wording fix. |

## What re-driving the type question actually showed (and a ticket I had to correct)

I had told FR-3461 that the launch dialog "sends every Initial Data value as a string". **That mechanism is
wrong** and I have corrected the ticket. Re-driven on the current flow, the Condition passed on *every*
API route, including a deliberate string:

| Route | `urgency` sent as | Condition |
| --- | --- | --- |
| POST | `{"urgency": 10}` | passed |
| POST | `{"urgency": "10"}` (string) | passed |
| GET | `?urgency=10` | passed |
| POST | both `urgency` and `escalateAbove` as strings | passed |
| GET | the dialog's generated URL verbatim | passed |

So `GREATER_THAN` tolerates a numeric string, and the page can claim nothing about what the *other* operand
has to be. Everything resting on that is gone. What survives is the part that is solid: a placeholder
arrives as the type it was declared with (the export writes `"value": 8` unquoted).

FR-3461's *observation* still stands — the dialog fails where all five API routes succeed — so the ticket
is still valid; only my explanation was wrong.

## Round-19 work (round 20 fixes) — Mark chose Option A

| Blocker | How it was cleared |
| --- | --- |
| **The example hard-coded the Slack webhook URL** (round-18 blocker, held for Mark) | Mark chose Option A. Rebuilt in-product: `notifyChannel` renamed to `notifyWebhook` (STRING, `https://hooks.example.com/triage/T29F4B1`) and bound into the HTTP Request's ((URL)) field; block renamed **Post escalation summary**; its Body now reads `Initial Data → urgency`. Two placeholders, both read, and the one that is secret is now the placeholder. The rename broke the old body binding and the flow went Not Ready until rebound — a live confirmation of the rename warning the page teaches. |
| **`placeholders-new-dialog.png` was stale** — its background panel still showed `notifyChannel` / `#support-triage`, hidden behind a generic alt. My own round-18 rule, broken in round 19. | Recaptured on the current version. The frame now shows a real new declaration with the full type list open and the current card behind it; the alt names what is behind the dialog so a future stale frame cannot hide. |
| **The LIVE clone route contradicted the one-LIVE-version invariant** taught by `flows-and-instances.md:23` and `running-flows.md:13`. | Rewritten to the canonical mechanic from `flow-editor.md:290`: only one version is LIVE, so starting the clone makes it LIVE and the original steps aside. The stop route is named with its control location. |
| **Ledger described an artifact that no longer exists** | Running-example paragraph and all twelve screenshot descriptions rewritten from the pixels, each PNG re-opened while writing its line. |
| **"a channel name two flows both post to"** — leftover from the retired example | Carries the running example now. |
| Type-section evidence rested on a fence that showed only the STRING row | The fence now carries both rows, so `"value": 8` appears unquoted beside the quoted string — evidence a reader can check. The unearned "guarantees" framing is gone. |

## Rounds 20-23

| Round | Gate | What it caught |
| --- | --- | --- |
| 20 | wf_3bf25eca-b2f → `major-rework` | Two shots stale after the round-19 rebuild; notifyChannel's consumption never shown; panel shot missing the controls its sentence named. |
| 21 | wf_1a57df9d-69d → **`revise`** (no blockers) | The secrecy justification was false (a placeholder gives no confidentiality); the ((Stop)) locator was wrong; the empty-value claim had no pixels; the dialog shot invented a third placeholder. |
| 22 | wf_057553ea-1b8 → `major-rework` | A lead-in describing the wrong image (my round-21 edit); ledger and verdict file stale; **deleting a placeholder is destructive and the page said nothing**; the clone locator wrong. |
| 23 | — | Cleared round 22's four blockers: lead-in/shot order, stale ledger + verdict, the unstated delete hazard, and a third wrong locator (Clone). |
| 24 | — | **Subtraction pass (Mark's Option A):** 224 → 160 lines, 12 → 7 shots, 11 → 7 sections. |
| 25 | wf_32e5c396-1ec → `major-rework` | **Cut residue:** the subtraction deleted screenshots while leaving the sentences that depended on them. Restored the LIVE view-mode and launch-dialog shots; retired renamed-break; restored "where the value is typed"; fixed the JSON-body sentence to match its pixels; promoted the cross-flow scope to its own h2. |
| 27 | — | Cleared round 26's blocker; drove the Run Instance tooltip. |
| 28 | wf_0933c636-b62 → `revise` | No blockers. 14 majors: repair residue, unclosed loops, prose-only claims. |
| 29 | — | Drove three claims on the copy flow. **Found I had the delete consequence backwards.** |
| 30 | wf_664ee969-306 → `major-rework` | Four blockers, two of them round-29 regressions: a secrecy remedy pointing at a store no HTTP Request can read, and a type claim crediting the placeholder for the ((Value Data Type)) dropdown's work. |
| 26 | wf_9c6d076e-edb → `major-rework` (1 blocker) | The LIVE section said Placeholder Data has "no route there" while the page's own shots show ((Run Instance)) opening an editable Placeholder Data section — the FR-3460 trap, one section from its own correction. |

**Round-27 fixes.** The LIVE section now says plainly that ((Run Instance)) is still in the toolbar and
its dialog still shows editable boxes, and that what you type there travels with the run rather than
changing the version. The lightning control was driven: its tooltip is **Run Instance** (the dialog it
opens is titled Launch Flow Instance), so the prose names both correctly. The "any field that offers the
Expression Editor" absolute was narrowed back to the driven scope (top level and inside a loop); SubFlow
scope remains NOT driven and is not claimed.

**Round-23 fixes.** Lead-ins re-matched to the shipped shot order. The delete hazard is now stated where
the trash is introduced: it flags every field that read the row, and unlike a rename it cannot be undone
by typing the name back. The clone route was re-driven — hovering the toolbar copy icon gives the tooltip
**Clone**, so "from the ((Version Admin)) tab" was wrong and the prose now names the toolbar control.

**Locators cost three rounds.** ((Stop)) was wrong twice (round 20 "beside the Live chip", round 21 "where
a Ready version shows play" — pause occupies that slot) and ((Clone)) once. Each was written from a note
or a DOM dump rather than read back against the screenshots this page itself ships. That is the standing
lesson from this page.

## Round 24 — the subtraction pass (Mark's Option A)

Mark chose subtraction over splitting or keeping the depth. **224 → 160 body lines, 12 → 7 screenshots,
11 → 7 sections.**

Folded away as one-sentence facts inside the sections that already earned a screenshot: the standalone
type, write-back and version-scope headings, and the Launch-dialog heading. Cut outright: the LIVE toolbar
geography — the two wrong ((Stop)) locators lived there, and `run/running-flows.md` owns those controls —
plus duplicated statements of the gear affordance, the type-to-control mapping and clone-carries-values.

Kept deliberately, because each was earned by a gate round: the eight literal type tags (wrong twice when
derived), the single frame carrying disabled Start + Not Ready + block badge + red field, the delete
hazard, the "held in the clear" boundary, and the export fence — the page's only artifact a reader can
check the type claim against.

Five screenshots were retired with their sections and deleted rather than left orphaned. All are
recapturable from flow `88C3EE86`, which is Ready and unchanged.

## Where this stood before the subtraction pass

The page is **not ready**, and the honest read after 22 gate rounds is that it is over-built rather than
under-finished: ~220 body lines and twelve screenshots against exemplars at 50-75 lines and 3-6 shots
(`variables.md` is 54 lines / 4 shots). Round 22's own summary names the cause — accretion, with four
facts each stated twice — and prescribes a subtraction pass rather than a split. Each patch round has been
clearing real defects while the page's size makes every edit ripple into the next round. **That trade-off
is Mark's call, not mine**, and it is the same class of decision as the Option A example choice.

## Round-31 fixes

| Blocker | How it was cleared |
| --- | --- |
| **The secrecy remedy was a dead end** — I sent readers to the workspace API key store for a webhook URL, but `api-keys.md:63` says the only flow-side consumer is the ((AI API Key)) field on AI blocks, and `http-request.md` has no credentials field. Identical defect to the Call Flow hatch I removed in round 16. | The page now states the boundary with no false remedy: there is no store a flow can read a secret back from at run time; the AI provider key is the one exception because it is picked on the block and never travels in the flow. |
| **The type claim credited the wrong control.** I wrote that the INT declaration is why the Condition compares numerically. `branching.md:67` and `condition.md` say ((Value Data Type)) governs the comparison, and my own round-19 drive showed GREATER_THAN accepts a numeric string. | Cut to what the export proves — `escalateAbove` is written `8`, not `"8"` — with comparison semantics pointed at Branching, which owns that control. |
| **The delete hazard was fused into Declaring and explained by forward reference** to a rename taught two sections later. | Merged into one h2, "Renaming or removing a placeholder breaks the fields that read it", teaching the shared error string once and both consequences — including the round-29 finding that re-declaring the name re-binds. |
| **Ledger and verdict file stale again** | Rounds 25-30 added here; counts reconciled; the ledger's gate box renamed to this run. |

Also: the value-setting opener now survives all eight types ("in whatever control its type gives it"),
((Run Instance)) is located as the lightning icon, and `placeholders-renamed-break.png` was recaptured at
the full framing the gate asked for — Not Ready chip, error badge, red field and message in one frame.

## The pattern

Round 28 reached `revise` with no blockers. Round 29's repairs introduced two new blockers. That is the
third time a repair round has added substantive errors, and the cause is consistent: when I fix a finding
I tend to write an *explanation* that goes past what I drove — a mechanism, a remedy, a reason. The
driven facts on this page have held up; the connective tissue I write around them is what keeps failing.

## Product observation, not filed

The product's status chip reads **Live**; the docs write **LIVE** in 161 places against 18 for "Live".
Not changed unilaterally — flagged for Mark as a docs-wide convention call.

## Not claimed, because not driven

SubFlow scope (the two-item hedge that invited the question was removed rather than answered — the claim
now sits at the version altitude that *was* driven); type validation on save; whether an `api_key` row
exports its chosen setup id; whether a non-AI key can ever appear in the `api_key` picker.

## Tickets this page produced

| Ticket | What |
| --- | --- |
| [FR-3443](https://backendless.atlassian.net/browse/FR-3443) | AI API Key fields should accept an API KEY placeholder |
| [FR-3442](https://backendless.atlassian.net/browse/FR-3442) | Flow Settings crashes the editor on a LIVE flow via `/edit` |
| [FR-3460](https://backendless.atlassian.net/browse/FR-3460) | Launch Flow Instance's Placeholder Data section is inert |
| [FR-3461](https://backendless.atlassian.net/browse/FR-3461) | The launch dialog fails a comparison that every API route passes. **My original description blamed string typing; corrected in a comment after re-driving — `GREATER_THAN` accepts a numeric string on all five API routes.** |

None gates the page.

## MARK — one open question

Export carries placeholder **values**, so a shared flow arrives pointed at the author's channel — and a
secret typed into a `STRING` placeholder would travel in the file too. Raised in conversation, no ticket
filed pending your call.
