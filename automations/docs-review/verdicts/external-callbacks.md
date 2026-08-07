# Verdict — build/flow-control/external-callbacks.md ("Waiting on an External System")

## Mark review round 2 — 2026-07-16
- Rewrote the head-breaking sentence in "Getting the execution id" into clear steps (open Expression
  Editor, pick two references, join with `?execution=`), and added a **MermaidJS sequence diagram** of
  the user/flow/external-system exchange.
- Learning Mode: added that the callback icon turns **purple -> green** after learning and that clicking
  the green icon opens the **Result Structure** popup; replaced the learned shot with that popup (fields +
  types), captured in-product.
- **Referencing method (the big one):** rewrote "Reading the callback data" to teach the ONLY correct way
  — open the Expression Editor, find the data, double-click or drag the field in; the `->` text is the
  inserted result, never typed. (I had been teaching the wrong, typed way — same root as the executionId
  "pill" error. Saved to memory.)
- Condition example generalized: gate on whatever field of the reader's OWN payload distinguishes the
  calls; `event EQUALS payment.succeeded` is one illustration, not universal.

## Mark punch-list round — 2026-07-16 (16 points, all applied)
- Callback URL: cut the "workspace host" tangent; say how to get it (open block, copy the complete value,
  no id assembly); moved the config image to right after that text.
- Corrected the wait: not "no end time" — a run waits up to the plan max (30 days Growth / 1 year others);
  repositioned so it follows the mid-flow bullet. Paused image moved with it.
- GET/POST: rewrote as prose-then-code (was code-with-comments); added real cURL for POST and GET.
- execution section: added the URL-structure code block; defined `any` ("FlowRunner picks which"); added a
  cURL resume example.
- Getting the id to the caller: fixed the core error — the Execution ID is a RUNTIME value (assigned per
  run, absent at build time), so "pill vs typed text" was nonsense and is removed; moved the
  "id in Flow Context" detail into the dynamic-URL case; reframed the two cases on the real axis
  (system accepts a per-request URL vs posts to one fixed webhook); removed the redundant trailing `any`.
- Learning Mode: added a cURL that sends the sample; corrected the overstatement — it makes fields
  referenceable by name (convenience), not a gate (you can reference a known field name without it).
- Conditions: added the ADD A CONDITION button shot after the intro; cut the operations list (screen-narration).
- Watch-fors: "the flow must be LIVE" is general (start or resume), not mid-flow-only; dropped the pill note.
- Newly verified/confirmed 2026-07-16: GET-resume + query-params-as-data (C97487D6); `executionId` alias;
  any/all + 28056/28010/28059/28060; condition gating (refund->null stays paused / payment.succeeded->resume).
  LIVE-for-start and reference-without-learning rest on the reference doc (authoritative), noted honestly.

## FULL REWRITE to engineering depth — 2026-07-16 (supersedes the rounds below)
Mark: the page read like a children's book and starved the substance (the `execution` targeting got two
lines; vague "pearls"; not mirroring the product). Root cause: I rewrote from the product + reasoning
WITHOUT reading the authoritative original. Fixed the process AND the page.

- **Read the authoritative original first** — there are TWO reference files; I had only read
  `external-callback.md`. The detailed one is `external-callback-trigger.md`
  (`git show HEAD:docs/reference/external-callback-trigger.html`). Read both in full.
- **Rewrote every section to reference-grade depth** (not one showcase section): the activation endpoint
  format; GET vs POST (query params vs JSON body as trigger data); the `execution` parameter as a table
  (`{id}` / `any` = next available / `all` = broadcast, comma-separated response), `execution|executionId`
  alias; an error-code table (`28056` no-execution / `28010` not-LIVE / `28059` bad id / `28060` any-empty);
  three concrete ways to get the execution id to the caller; Learning Mode; reading data with `->`;
  conditions (Value to Check / Data Type / Operation / Value, the operation set); watch-fors. Cut all
  vague narrative; concrete values throughout (aligned example payloads to the ORD-9001 learned shot).
- **Verified the whole API surface in-product (2026-07-16)** — not guessed: GET-resume + query-params
  becoming trigger data (C97487D6); `?executionId=` alias (4FA4690A); `any` wakes one, `all` returns the
  comma-separated id list (904EFDDC + 6BEDE8DE); errors 28056/28010/28059/28060; `all`-empty → `null`;
  condition gating (`event EQUALS payment.succeeded`: a `refund` call returned `null` and left the run
  paused, `payment.succeeded` resumed it). New shot: externalcallback-condition. doclint 0/0; plain clean.
- **Scope (Mark):** omit Execution Permissions/security and the `user-token` header.
- **Gate:** NOT re-run — Mark directed the exact content of this rewrite; his review is the authority
  (re-running the stochastic gate after his explicit direction is the loop he flagged). Handing to Mark.

---


**Date:** 2026-07-15
**Latest gate verdict:** `revise` (run 2). Run 1 was `major-rework`.
**doclint:** 0 errors / 0 warnings.
**Handling:** all findings from both runs resolved in one consolidated pass. Per the standing
anti-loop rule ("never re-run the gate to chase a clean verdict; a single regression re-run only if
Mark asks"), the gate was NOT run a third time. Presenting to Mark with findings + resolutions;
Mark decides ship (or asks for a regression run).

## Run 1 — `major-rework` (all cleared)
- **BLOCKER (educator/red-team) — self-defeating example.** §4 read `External Callback Data->orderId`
  = ORD-9001, but the flow *sent* orderId — reading back its own value, never motivating why you read
  callback data. **RESOLVED:** re-ran the flow (instance 838ECE57) so the read-back step now reads
  `External Callback Data->event` = `payment.succeeded` — the payment OUTCOME the provider supplies,
  which the flow cannot know until the callback arrives. Block renamed to **Store Payment Result**,
  variable **Payment Result**. Grounded in §3's learned-structure shot (which shows `event`).
- **BLOCKER (definition-of-done) — config shot continuity.** Config shot's third block still read
  "Record Sale". **RESOLVED:** recaptured; third block now reads "Store Payment Result".
- **MAJOR (educator/red-team) — config minimap + §1 opener.** **RESOLVED:** recropped the config shot
  above the minimap; §1 now opens purpose-first ("Place an External Callback where the run should
  stop and wait…") before the palette-drag mechanic.

## Run 2 — `revise`
Gate summary: strong, well-backed page with a continuous RUN-PROVEN walkthrough; does not ship only
because of two real majors (term-colliding "without consuming a step"; stale ledger) plus a red-team
gap (where a real provider gets the Callback URL). Everything else minor polish.

### Majors — all resolved
- **guideline — "without consuming a step".** Term collision (docs use "step" = a block) + an
  unverified billing/metering claim with no note or pixel behind it. **RESOLVED:** dropped the clause;
  restated plainly — "The run holds at the callback for as long as the outside work takes — seconds or
  days — and then wakes on the same instance when the call arrives." No cost claim asserted.
- **definition-of-done — stale ledger (PLATFORM-REVIEW-LEDGER lines 419/421).** Still described the
  superseded Record Sale / ORD-9001 recapture. **RESOLVED:** updated the SHOW-it and PAUSE+RESUME
  lines to Store Payment Result reading `External Callback Data->event = payment.succeeded` (instance
  838ECE57); noted the earlier orderId proof is superseded; kept the provider-only-value rationale.
- **educator/red-team — where does the provider GET the Callback URL? (candidate new rule).**
  Page taught the internal reference mechanism but not how the outside system obtains the address.
  **RESOLVED:** added — "The Callback URL is shown, read-only with a copy button, on the External
  Callback's panel. It is the address you hand the outside system — many providers take it as a
  webhook target you paste into their dashboard; others receive it in a request the flow sends them
  first, as in this example." (Candidate guideline for Mark: a hand-off/integration feature must state
  WHERE the outside system obtains the address, not just the internal reference.)

### Minors — resolved
- **Resume section opened on machine-state + restated the resume mechanic.** RESOLVED: value-first
  opener (holds seconds-or-days, wakes same instance); status follows as confirming; dropped the
  retelling.
- **Hand-off opener re-listed the lede's examples.** RESOLVED: opens directly on the new fact (where
  you place the callback is where the run stops).
- **Learning Mode opener asserted trigger-theory.** RESOLVED: plain version — the trigger can't know
  the field names until it has seen one; Learning Mode captures the shape from a sample.
- **Execution ID styled three ways.** RESOLVED: `Execution ID` in code at every prose mention.
- **Callback URL chip/name.** RESOLVED: reconciled the picker pill name ("External Callback URL",
  under "External Callback URLs") with the panel's Callback URL in prose.
- **§4 never named the "Payment Result" variable; alt conflated read vs. save.** RESOLVED: prose names
  the variable and the value (`payment.succeeded`); alt describes the callback field flowing INTO
  Payment Result.
- **Screenshot hygiene (minimap / React Flow watermark / clipped control on paused & resumed).**
  RESOLVED: recropped both from the full run screenshots — paused is a clean flow crop (EC waiting
  indicator + pending step); resumed is a clean Set Variables panel (Value = External Callback
  Data->event). No minimap, watermark, or clipped controls.
- **Ledger open cleanup box (line 425).** RESOLVED: flow now STOPPED (Ready); cleanup consciously
  deferred to section end with the other throwaways (noted in the ledger).
- **verify-in-product — top-of-flow "new run per call".** RESOLVED (softened): "starts a new run when
  it is called," full behavior routed to the External Callback reference; parked a follow-up to drive
  or confirm it.
- **verify-in-product — Callback URL form equivalence.** RESOLVED: run-proven that the panel Callback
  URL string is the trigger activate URL that the resume POST targets with `?execution=` (recorded in
  the exploration log).

## Mark review — round 1 (2026-07-15), all applied
- **Screen-narration ("Callback URL is shown, read-only with a copy button, on the panel").** REMOVED.
  Prose now says what the address is FOR (the one thing you give the outside system), not what the
  widget looks like.
- **Under-explained "which run to wake."** REWROTE with the real WHY: a Callback URL points at the
  flow, not a run; multiple runs can wait at the same callback at once (verified: 2-3 paused
  simultaneously), so the caller must name the run.
- **Missing real integration paths.** ADDED all three, thoroughly: (a) the flow composes and sends the
  full address (only when the system accepts a per-request callback URL); (b) a fixed/pasted webhook
  URL that cannot take a per-request address — the Execution ID reaches the system another way and it
  appends `?execution=<id>`; (c) a caller that started the run via the Call Flow API already got the
  executionId in the response (grounded in reference/call-flow.md).
- **Missing `?execution=any` / `?execution=all`.** ADDED, and VERIFIED in-product today: `any` woke one
  waiting run (36B09CF9; others stayed), `all` woke every waiting run (068C5A05 + CFEE8562 both).
- **"wakes on the same instance" over-claim.** FIXED — true only for a specific id; `any`/`all` select
  differently. Prose no longer claims "same instance."
- **`payment.succeeded` stated but not shown in any screenshot.** FIXED — the §4 shot is now a clean
  2-panel image from the completed run: the Set Variables Value (`External Callback Data->event`) above
  the block's Output (`Payment Result: payment.succeeded`). The value now appears in the shot.

Generalizable principles from this round (to confirm with Mark before encoding): (1) never state a
concrete value/output in prose unless a screenshot on the page shows it; (2) for a hand-off/integration
feature, document the full range of how an outside system obtains and uses the mechanism (dynamic vs.
static webhook vs. API-response), not just the happy path.

## Evidence
- Run-proven end to end today: instance 838ECE57 paused at the callback (Status RUNNING / End N/A),
  resumed via `<CallbackURL>?execution=838ECE57…` with `{"event":"payment.succeeded",…}`, COMPLETED
  (1m 20s); Store Payment Result read `External Callback Data->event` = `payment.succeeded`.
- LIVE-only negative verified: POST while stopped → code 28010 (rejected).
- 6 shots recaptured/recropped 2026-07-15. doclint 0/0; plain-style clean.
