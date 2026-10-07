# Verdict: content/platform/compliance-and-security.md (Compliance & Security)

## 2026-10-06 - release sweep "Without version/devtasks2" + "without3"

- Verdict: **major-rework** (concept-page-review wf_6b183a54-177, one run; not re-run per the one-net rule). Mark decides ship.
- Scope: the release delta only - FR-3674 (Activity Log renamed Change Log; devtasks2) and its follow-on FR-3675
  (Flows Activity Log version picker + "Open flow instance" icon; Jira fixVersion **v.1.1.3, unreleased**).
- Evidence basis: driven on dev.flowrunner.ai 2026-10-06 from a staff account; on prod only the strings were found in the
  app.flowrunner.ai JS bundle. A bundle string is NOT a prod drive (gate item 1) - the prod session is signed out.

### Release delta - resolved after the gate
- Item 14: "It keeps the older name." deleted (the account-menu sentence keeps the ((Activity Log)) chip as the menu reads).
- Item 1 (partial): RELEASE comment rewritten to separate devtasks2 (FR-3674) from v.1.1.3 (FR-3675), mark everything
  DRIVEN-on-dev, and list the prod drives owed; it says to remove the icon paragraph if the icon is not on prod.

### Owed - one batched prod session (needs Mark to sign the browser in to app.flowrunner.ai)
- Item 1: nav + screen title read Change Log; account-menu label; notification button label; Flows Activity Log version picker
  greyed "All versions"; the icon, its tooltip and target. Recapture compliance-nav.png on prod.
- Item 2: recapture flows-activity-log.png with the icon (also used on notifications.md) - or drop the icon paragraph.
- Item 9: performer filter disabled for System as a NON-system user (mark@flowrunner.ai is a staff account).
- Items 18, 19: View in Activity Log filter window; Change Log shot layout after FR-3675.

### Older debt carried (not part of this release; open since 09-25 or earlier)
- Panic Mode (items 3, 7): undriven Backendless-era effects, no way back documented; FR-2682 still Open.
- SLA Calendars shot (item 4): removed per-day control + empty Excluded Dates.
- FR-3659 "Show event details" (item 5): fix now Implemented in v.1.1.3, not retroactive - decision for Mark (warning or not).
- Ledger section stale (item 6); Change Log coverage sentence (item 8, needs re-drive after FR-3421); lede (10); Flows Activity
  Log order (11) and what it records (12); entry/filter narration (13); Compliance box order (15); HIPAA states (16);
  headings (17); formatting (20); abbreviations (21); badge states (22); "FlowRunner team" changes (23); API key wording (24);
  half-hour zones (25); DST claim (26); SLA Goals tab position (27).

---

# Verdict: content/platform/compliance-and-security.md (Compliance & Security)

- Date: 2026-09-25 (release v.1.1.2 sweep)
- Verdict: **major-rework** (concept-page-review wf_4ad8e333, 7 lenses, one run; not re-run per the one-net rule)
- Scope reviewed: the v.1.1.2 change (Audit Log section replaced by Activity Log / Flows Activity Log), plus the
  rest of the page
- doclint: 0 errors, 0 warnings; mkdocs build --strict: clean; anchors #activity-log and #flows-activity-log resolve

## Gate summary

36 items (8 blocker, 16 major, 12 minor). The release delta needed:
- a split into two logs
- a driven coverage claim
- a safe entry-dialog shot (FR-3659: details print secrets)

Most of the rest sits in untouched sections:
- Panic Mode: never driven, Backendless-era text, and FR-2682 still open
- SLA Calendars: a default-state shot and structure
- HIPAA scope
- plan gating

## Resolution (same day, one consolidated pass)

| # | Sev | Item | Resolution |
|---|---|---|---|
| 1-2 | blocker | Panic Mode undriven, Backendless-era wording | OPEN - decision for Mark (older debt; activating it locks the workspace) |
| 3 | blocker | one section for two logs | FIXED: "## Activity Log" (reader-first opening) + "## Flows Activity Log" + account-log pointer |
| 4 | blocker | coverage claim | FIXED: driven - creating / starting / stopping / deleting flows leaves no entry; stated |
| 5 | blocker | account log | PARTIAL: location + filters only (its log was empty) |
| 6 | blocker | entry dialog | FIXED: activity-log-entry.png with Show event details collapsed; levels driven (Critical red / Warning orange / Info) |
| 7 | blocker | ledger / stale notes | FIXED: July Audit Log note marked SUPERSEDED; ledger block + this file |
| 8 | blocker | SLA plan admonition | FIXED: "SLA Goals, and the SLA tracking they drive, ..."; whether calendars are gated OPEN |
| 9 | major | FR-3659 warning | DECISION FOR MARK |
| 10 | major | intro enumeration | FIXED |
| 11 | major | lede ("a switch to stop everything") | OPEN, waits on Panic Mode |
| 12 | major | worked example | PARTIAL: real Open-Meteo deploy entry used; no purpose-built scenario |
| 13 | major | filter prose | FIXED |
| 14 | major | View in Activity Log | FIXED (driven via notifications) |
| 15 | major | Flows log entry types | PARTIAL: categories + SYSTEM performer driven; trigger failure / manual terminate not produced |
| 16 | major | "always" | FIXED: dropped |
| 17 | major | categories | FIXED: all eight listed |
| 18 | major | System initiator gloss | FIXED: platform actions (seen) + FlowRunner team actions (SOURCE, FR-3560) |
| 19-21 | major | SLA Calendars shot / structure / hierarchy | OPEN (older section) |
| 22 | major | flow vs instance | FIXED |
| 23 | major | Panic Mode prose | OPEN with 1-2 |
| 24 | major | HIPAA | OPEN (older section) |
| 25 | minor | shots from the Tests workspace | OPEN |
| 26 | minor | plan gating of the logs | OPEN |
| 27 | minor | admonition placement | OPEN |
| 28 | minor | inbound links | FIXED: workspace.md / oauth-connections.md say "the activity logs" |
| 29-32 | minor | SLA / abbreviations | OPEN |
| 33 | minor | nav shot alt | FIXED: compliance-nav.png recaptured, alt matches |
| 34 | minor | Related | FIXED: Flow Scheduling -> Notifications |
| 35 | minor | SLA Goals bridge | OPEN |
| 36 | minor | page structure | DECISION FOR MARK (move SLA Calendars onto the SLA Goals page) |

Mark decides ship.

## Second pass (same day, Mark: "apply fixes")

Tested on prod in Documentation Flows (Growth plan).

| # | Was | Now |
|---|---|---|
| 19-21 / 31 | OPEN | Section retitled "## SLA Calendars", with a "A calendar has:" bullet list. Time Zone = whole-hour offsets GMT-12..+12, no daylight saving (tested). The toolbar is named (Save / Clone / Rename / Delete). The second-span claim was removed (the control is gone). **Filed FR-3661 (High)**: Work Week hours display 12:00 AM whatever is stored, and editing one end resets the other on save (400 with no message, or silently saved wrong). The old sla-calendars.png is kept until the fix, because a fresh shot would show the bug |
| 29 / 35 | OPEN | PARTIAL: the SLA Goals tab's location is stated. On Growth it is greyed with the tooltip "Available on Business plan and higher", which backs the note. The calendar picker inside a goal can't be reached on this plan |
| 8 / 26 / 27 | OPEN | Plan notes reconciled: SLA Goals KEPT (tooltip); Panic Mode KEPT (FR-2682 states it) but the buttons are enabled on Growth, commented on FR-2682; HIPAA REMOVED (no source anywhere) |
| 23 / 11 | OPEN | Panic Mode rewritten plainly: the screen's own list, quoted as the screen's. The undriven gloss ("scheduled flows", "stop everything") was dropped from the section and the lede |
| 24 | OPEN | Compliance section opens on the outcome. The agreement link opens the BAA PDF (tested) |
| 25 | OPEN | FIXED: compliance-hipaa.png and panic-mode.png recaptured in Documentation Flows |
| 30 | OPEN | FIXED: text defects on both screens reported on FR-2682 (comment 79284) |
| 4 | FIXED | extended: creating or saving an SLA calendar leaves no Activity Log entry |

Still OPEN: Panic Mode activation (never tested, because it locks the workspace); SLA Goals calendar picker (needs Business); Activity Log retention per plan; SLA/PHI/BAA abbreviations; page-structure decision (#36).
