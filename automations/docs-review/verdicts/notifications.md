# Verdict: content/platform/notifications.md (Notifications)

- Date: 2026-09-25 (release v.1.1.2 sweep)
- Verdict: **major-rework** (concept-page-review wf_6a87808a, 7 lenses, one run; not re-run per the one-net rule)
- Scope reviewed: the v.1.1.2 changes (grouped terminations, pop-up, View in Activity Log), plus the rest of the page
- doclint: 0 errors, 0 warnings; mkdocs build --strict: clean; anchor #terminated-runs-of-one-flow-share-an-entry
  resolves (the inbound link from compliance-and-security.md was updated)

## Gate summary

28 items (4 blocker, 17 major, 5 minor, 2 nit). The main problems:
- the grouping section's heading and lede framed flows as the thing that runs
- "group" meant two different things
- the pop-up's Show details was never driven
- several anatomy claims were undriven (time format, read state, badge)

## Resolution (same day, one consolidated pass)

| # | Sev | Item | Resolution |
|---|---|---|---|
| 1 | blocker | ledger / verdict | FIXED: ledger block + this file |
| 2 | blocker | Show details undriven | FIXED: driven on Order Sync - flowId, flowName, version, executionId, reason, workspaceId, workspaceName; nothing secret for this event |
| 3 | blocker | lede / flow framing | FIXED: "Once a flow is LIVE, its runs happen..." |
| 4 | blocker | heading | FIXED: "## Terminated runs of one flow share an entry"; inbound anchor updated |
| 5 | major | anatomy mixes single and grouped | PARTIAL: bullets kept generic; a single ungrouped capture not taken |
| 6 | major | "group" has two meanings | FIXED: workspace "heading"; "entry" for merged terminations |
| 7 | major | counted lead-in; title scope | FIXED: "Each entry shows:"; title bullet scoped |
| 8 | major | counted lead-in | FIXED: "Use these to keep the list short:" |
| 9 | major | time format | FIXED: "a time, or how long ago" (both forms seen) |
| 10 | major | chip case | FIXED: ((mark read)) |
| 11 | major | View in Activity Log scope | FIXED: URL read - top of the hour (UTC) to the latest run, flow + version |
| 12 | major | N+ case | OPEN (not driven; the "N+" form was seen only in other workspaces' entries) |
| 13 | major | grouping boundaries | SOURCE (FR-3568 developer note): different flow or next hour -> new entry; not driven |
| 14 | major | the stop case | SOURCE (FR-3568): stated; not driven |
| 15 | major | badge / count | FIXED: badge on the bell ("99+"), panel title carries the count |
| 16 | major | header icons | Backed by the 2026-08-31 dev drive (pin survives reload); not re-driven |
| 17 | major | read state | FIXED: opening an entry does not clear the dot (driven) |
| 18 | major | mark read shot | FIXED: notifications-unread-only.png; mark read behaviour from the 08-31 drive |
| 19 | major | Your Account heading | OPEN (needs an account event; not produced) |
| 20 | major | toasts and email | PARTIAL: "no pop-up for your own action" stated (SOURCE + three silent launches); email rule left off the page |
| 21 | major | lede examples | OPEN: "a payment that failed" (billing.md) and "a limit you are close to" kept from the earlier page |
| 22 | minor | severity | FIXED: "Warning for a terminated run" |
| 23 | minor | evidence logs | FIXED: superseded notes marked; SOURCE lines added |
| 24 | minor | workspaces paragraph | FIXED |
| 25 | minor | plain style | FIXED |
| 26 | minor | Related | FIXED: Compliance & Security link added |
| 27 | minor | plan gating of the link | OPEN |
| 28 | nit | screen treatment | FIXED |

Mark decides ship.

## Second pass (same day, Mark: "apply fixes")

Tested on prod: Export instances to CSV on Order Sync.

| # | Was | Now |
|---|---|---|
| 19 | OPEN | FIXED: the export-ready message sits under a **YOUR ACCOUNT** heading at the top of the panel (new shot, cropped above the next workspace) |
| 20 | PARTIAL | FIXED/CORRECTED: the export pop-up DID appear for my own action, so "a message you caused yourself does not pop up" was too broad. It is now scoped to terminated runs you launched. The pop-up stays until closed; view details opens the detail pop-up (Info, no download link). New shot notifications-popup.png |
| 21 | OPEN | CUT: the export also carries `flow-execution`, so the source-chip "run vs account" contrast was removed |
| 22 | FIXED | extended: Info level for an export |

Also: inspecting-a-run.md's CSV section now says a notification announces the file (its 08-31 "not observed" note is superseded).
Still OPEN / SOURCE only: the stop case, the hour boundary, a second flow in the same hour, N+ paging, plan gating of the link.
