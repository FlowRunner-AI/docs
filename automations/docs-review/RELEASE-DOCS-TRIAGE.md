# Release docs triage — 39 tickets (26 Waiting for Release + 13 Closed, all `fixVersion IS EMPTY`)

Pulled 2026-08-31 from Jira project FR. Board-matching JQL:

```
project = FR AND status IN ("Waiting for Release", "Closed") AND fixVersion IS EMPTY
```

Verification host: **dev.flowrunner.ai** (Mark, 2026-08-31 — everything in Jira is available there).

---

## A. Docs are now WRONG — a shipped page contradicts the release (12)

| Ticket | Page(s) | What breaks |
| --- | --- | --- |
| FR-3408 | `api/call-flow-blocking.md`, `api/call-flow-nonblocking.md` | Page states `activate-blocking` takes the flow **NAME only** (id → 28047) and `activate` takes the **id**. Ticket makes both endpoints share one URL form and accept **id or name**. Every URL, cURL block and the "why the two differ" prose is now wrong. Also invalidates memory `flowrunner-call-flow-api-facts`. |
| FR-3442 | `reference/flow-memory-concept.md` | Page routes the reader to the Flow Settings tab to set the Memory Anchor; on a LIVE flow that tab crashed the editor. Fix makes it viewable — re-drive and state the LIVE behavior (read-only, per FR-3346 precedent). |
| FR-3426 | `platform/api-keys.md`, `manage/workspace-settings.md` | Regenerate API key returned 404; confirmation dialog said "REST key" (Backendless leftover). Both the action and its dialog copy change. |
| FR-3386 | `manage/workspace-settings.md` | Page documents the ((RENAME)) button. Server rejected the update. Resolution went one way or the other — the page describes a route that did not work. |
| FR-3352 | `reference/condition.md` (+ `block-knowledge/condition.yaml`) | Condition failed the whole block on a null input for every check, not just Has Key. Now returns `false`. No null behavior is documented at all. |
| FR-3159 | `learn/concepts/expressions.md`, `learn/concepts/variables.md` | A dot in a Data Bucket/variable name (`n.n`) made the flow INVALID. Now resolves. Naming constraints need stating either way. |
| FR-3409 | `api/call-flow-blocking.md` (Launch Flow Instance dialog shot), `run/running-flows.md` | Initial Data **keys** are no longer editable in the Launch Instance popup. The existing screenshot depicts the old dialog. |
| FR-3301 | `reference/list-iterator.md`, `run/inspecting-a-run.md` | A nested List Iterator displayed as "not executed" in Block Results after a successful run. Fixed — any screenshot or claim showing the old state is wrong. |
| FR-3361 | `reference/external-callback.md`, `build/flow-control/external-callbacks.md` | Console-supplied Callback URL for a trigger **inside a SubFlow** did not resume the debug execution (28059). Fixed. Documented integration paths need re-checking against the memory rule "document ALL integration paths". |
| FR-3362 | same as above | Terminating one flow version destroyed pending callback triggers of **other** versions. Affects anything the docs say about versions being independent. |
| FR-3410 | `extend/triggers.md` | Trigger Callback URL now built from `hostType/packageId/serviceId`, not the legacy `hostType/serviceName/modelName/lang`. |
| FR-2612 | `extend/parameters-and-types.md` | `Array<Array<Complex>>` (a nested custom schema inside a custom schema) rendered as a plain field instead of a schema. Now supported — the types page should show the nested case. |

## B. New content — the feature is not in the docs at all (4)

| Ticket(s) | Where | Size |
| --- | --- | --- |
| FR-3321, FR-2236, FR-2084, FR-3444 | `manage/billing.md` (currently 47 lines, verified 2026-07-10) | **Major rewrite.** Nothing on: the 14-day Professional trial (one per account, no card), the 80/90/95/100% execution warnings and the hard stop, upgrade proration + counter reset, downgrade at cycle end, export/transfer blocked on trial/canceled/past-due (9124/9125/9127), the new `trialing` status, suspension after a failed first payment. |
| FR-2561 | new page | **New.** Notification Service + the console Notification Panel — severity, source tag, counter, Dismiss All, retention, email delivery. Nothing exists today. |
| FR-3394 | Instances screen — **placement open, see below** | Instances **Export** to CSV: filter-scoped, async, notification + emailed link, and a defined column set. |
| FR-3395 | same | Live per-state count circles above the Instances table: filter-scoped, self-updating, clickable as a filter. |

**Placement problem for FR-3394 / FR-3395.** No page currently owns the Instances *list* as a
reader destination. `run/monitoring.md` covers Dashboard / Performance / Logs and explicitly hands
the single-run drill-down to `run/inspecting-a-run.md`; that page is about one run and touches the
list only in its "Opening a run" lede; `run/running-flows.md` mentions the tab in passing (line 34).
Export and the live state counts both answer "what is happening across my runs right now, and how
do I get that out?" — a different reader question from either page's.
**Recommendation:** give the Instances list its own short page under Test & Run (finding a run,
filtering, the state counts, Export), and have all three existing pages route to it. Alternative:
graft both onto `inspecting-a-run.md`, which is cheaper but folds two reader questions into one
page — the split Mark already made in the other direction on 2026-08-15.

## C. No docs impact (16)

`FR-3072` `FR-3391` (both labelled DOCUPDATE-NO) · `FR-3210` (storage refactor, explicitly transparent) · `FR-3300` `FR-3432` (Duplicate) · `FR-3439` (flaky test) · `FR-3446` (SAML spike) · `FR-3400` (NPE) · `FR-3406` (import round-trip fidelity) · `FR-3366` (server-side scope validation) · `FR-3385` (custom-extension logo) · `FR-2255` (Won't Do) · `FR-3393` (console-internal endpoint) · `FR-3350` `FR-3379` `FR-3382` (Expression Editor bug fixes — no documented claim changes; check only whether any Expression Editor screenshot shows the broken state).

## D. Mark's decisions (answered 2026-08-31)

1. **FR-3247 "Prompt to Flow" — INTERNAL.** Not documented in this pass. Mark: "internal. It will be a next task for you by the way." Parked as the next task after this release pass.
2. **FR-3412 Extensions Runner — do NOT document the legacy format.** Mark: "we never documented legacy format for extensions. No one knows about them." Mentioning it now would teach a format nobody uses. **DO document the Files API for extensions** (`WORKSPACE` / `FLOW` / `EXECUTION` scopes, `usesFileStorage`, `createFiles`), including the FR-3420 gap for Custom Extensions.
3. **FR-3386 — renaming is ALLOWED.** `manage/workspace-settings.md` keeps its RENAME procedure; verify it now succeeds on dev.

## E. Verification environment (settled)

**"Documentation Flows" on dev.flowrunner.ai** — Mark, 2026-08-31: "it is entirely for you."
Same workspace name as on app.flowrunner.ai; the boundary is the workspace NAME, on both hosts.

---

## Execution order — FINAL STATUS (2026-08-31)

All 39 tickets are dispositioned. Nothing is left open.

### Docs changed (11 pages, 3 new screenshots, 1 new nav entry each for two new pages)

| Ticket(s) | Page | What changed | Basis |
| --- | --- | --- | --- |
| FR-3408 | `api/call-flow-blocking.md`, `api/call-flow-nonblocking.md` | Both endpoints take id **or** name over GET/POST; single not-found code `28053`; rename caveat became conditional; the two pages' asymmetry story removed | DRIVEN (8-way matrix, 3 error paths) |
| *(bonus)* | same two pages | New error row `2027` — **the API key is now enforced**, an old known defect now fixed | DRIVEN |
| FR-3386, FR-3426 | `manage/workspace-settings.md` | Rename works end to end (and changes the console URL); regenerate works and its dialog no longer says "REST key"; the "old URLs must be rebuilt" claim is now proven | DRIVEN (all three exercised) |
| FR-3442 | `reference/flow-memory-concept.md` | Flow Settings is unreachable on a LIVE version — `/edit` now redirects to `/view`; routes readers to stop or use a draft | DRIVEN (both states) |
| FR-3442 | `learn/concepts/placeholders.md` | Provenance updated: the `/edit` crash hole this page recorded is closed | DRIVEN |
| FR-3352 | `block-knowledge/condition.yaml` → `reference/condition.md` | Null input no longer fails the block — returns false; plus the Yes/No wiring validation rule | DRIVEN (2 operations, Run Block) |
| FR-3394, FR-3395 | `run/inspecting-a-run.md` | New sections: the four state circles (Running/Pending/Completed/Terminated) as filters, and filter-scoped CSV export. 2 new shots | DRIVEN (circles, toggle, ellipsis, export request) |
| FR-2561 | **NEW** `platform/notifications.md` | The notification panel: opening, what an entry carries, workspace grouping, the filter link, Mark read. 2 new shots | DRIVEN (every control exercised) |
| FR-3412 | **NEW** `extend/files.md` | The Files API: `usesFileStorage`, the three scopes, all five methods, every option and result field, the Custom Extensions gap | SOURCE-DERIVED from `flow-extension-runner` (not driven) |
| FR-2612 | `extend/parameters-and-types.md` | Added the `z.array(z.object({…}))` case — a list of structured entries | Composition of documented types (not driven) |
| FR-3321, FR-2236, FR-2084, FR-3444 | `manage/billing.md` (47 → 130 lines) | Corrected the plan ladder (Free and Starter were missing), the chip label and the shot; added the trial, the 80/90/95/100% warnings and hard stop, upgrade/downgrade timing, and the export/transfer restrictions | Ladder/chip/shot DRIVEN; trial, thresholds, restrictions SPEC-SOURCED |

### No doc change needed — determined by reading our own pages first

- **FR-3409** — no page claims Initial Data *keys* are editable; the prose only describes typing values.
- **FR-3301** — no page claims a nested iterator shows as "not executed".
- **FR-3159** — we document no variable-naming constraints, so nothing contradicts the fix.
- **FR-3361 / FR-3362** — neither callback page mentions SubFlows or cross-version triggers.
- **FR-3410** — `hostType`/`packageId`/`serviceId` are console-internal and appear nowhere in `extend/triggers.md`.
- Plus the 16 already in section C.

### Product findings reported to Mark

1. **The API key is now enforced** (`2027`) — a previously known, reported, undocumented defect is fixed.
2. **FR-3394's user-facing half is missing.** The export request fires and returns 200, but no confirmation
   message appeared and no notification-panel entries arrived, though the ticket specifies two.
3. **FR-2561 has no "Dismiss All"** — the ticket specifies one; the panel offers only per-workspace Mark read.
4. **`manage/billing.md` was missing two whole plans** (Free and Starter) before this pass.

### Residuals for Mark

- The Instances shot shows 0/0/0/11 (all TERMINATED) because TD Sandbox's Get Order block fails — a
  mixed-status shot needs a demo flow that completes.
- The notifications shot shows one repeated message for the same reason.
- `extend/files.md` is the one page here whose facts are read from source rather than driven.
- The trial/threshold/restriction half of `billing.md` is spec-sourced; it cannot be driven without a
  trial workspace and real charges.
- `block-knowledge/condition.yaml` still cites an FBB flow in `provenance.evidence`. I added my own
  evidence beside it and flagged it rather than rewriting it unprompted — that remediation is still pending
  your direction across ~25 reference pages.
- The `concept-page-review` gate has **not** been run on these pages for this revision.

## F. FR-2973 subtask sweep, 2026-09-09

| Ticket | Docs effect | Verified |
| --- | --- | --- |
| FR-3387 (0.0.7) | config coercion + validation, `.secret()`, `.labels()` replaces `.map()`, label/description defaults, `params` optional, `FR_EXT_INVALID_SCHEMA` / `FR_EXT_INVALID_CONFIG` | DRIVEN on dev (config tab, editor run) |
| FR-3425 | `.optional()` is correct again; `.default()` fires; `.nullish()` workaround reverted everywhere | DRIVEN (harness + editor) |
| FR-3475 | `.shared()` harmless in a custom extension | SOURCE (guide); oauth.md corrected |
| FR-3473 | `.secret()` masks a config field | DRIVEN |
| FR-3537 / FR-3538 / FR-3543 | dates section, unsupported-type degradation, `z.fileUrl()` never documented | SOURCE (param-schemes) |
| FR-3420 (0.0.8) | `filesScope`, scope-outside-a-run rule; **warning stays** - fails on dev with `ENOTFOUND fr-automation` | DRIVEN, defect commented |
| FR-3477 | OAuth page still held out of nav - blocked at GitHub sign-in | PARTIAL |
| FR-3384 / FR-3474 | not on dev; reload rule and "Local Extensions" stay | DRIVEN |
| FR-3553 | troubleshooting entry for a legacy-format service under the CLI | SOURCE (ticket) |
| harness | `runServiceMethod({ configs })`, `init` never refreshes `sandbox/` | DRIVEN (init re-run) |

## G. Release 1.1.1.0 sweep, 2026-09-17 (68 tickets; 34 not covered by A-F)

Verification host: dev.flowrunner.ai (app.flowrunner.ai needs a sign-in this browser does not have), Documentation Flows, throwaway flow "Release Probe 1.1.1" (`B7316DCB`, stopped, kept for FR-3596) and TD Sandbox (restored: 3 nodes / 2 edges, temporary placeholder removed).

| Ticket | Page | Change | Verified |
| --- | --- | --- | --- |
| FR-3441 | `api/block-results.md` | `result` is the block's value; `null` for a no-value block; failed block keeps the envelope; 28068 / 28159 unchanged | DRIVEN (dev-api, run C9CA47EA); failed-block envelope from the ticket's drive |
| FR-3431 | `run/running-flows.md`, `api/call-flow-blocking.md` | "On hold" -> **Paused**; non-LIVE dialog shows no URL ("start or resume this version to get it"); toolbar shot recaptured | DRIVEN |
| FR-3470 | `block-knowledge/condition.yaml` -> `reference/condition.md` | wrong-type value -> false + WARN in the flow log; No path must be safe | DRIVEN (customer=John -> No; WARN line read in Logs) |
| FR-3402 | `run/monitoring.md` | Shorten IDs + Wrap messages controls, new shot | DRIVEN (on/off/persisted) |
| FR-3381 / FR-3468 / FR-3380 | `learn/concepts/expressions.md` | new section: pencil opens the path row, type button Object/List, index dropdown First..Last + typed number, #Second pill, no edit-time validation; 3 shots | DRIVEN (no-sample path); with-sample tree and primitive types from the ticket recap |
| FR-3465 | `learn/concepts/placeholders.md` | rename now re-points every field; old warning + placeholders-renamed-break.png retired | DRIVEN (hail -> wave, field followed, Ready, survived reload) |
| FR-3460 | `learn/concepts/placeholders.md` | Placeholder Data section only on a draft's launch dialog; LIVE dialog has none | DRIVEN (both dialogs) |
| FR-3349 / FR-3437 / FR-3464 | `manage/billing.md`, `run/inspecting-a-run.md`, `run/monitoring.md` | visibility ladder (never "retention"), selector rungs, bulk export Growth+, one Free workspace, card rules, past-due label, in-flight re-stamp, hidden-instances notice, outside-history screen, "(Trial)" suffix, "Past 24 hours" preset | "Past 24 hours" DRIVEN; the rest SOURCE-DERIVED (no trial/Free/past-due/old-run state available) |
| FR-3389, FR-3505, FR-3536, FR-3569, FR-3317, FR-3390, FR-3343, FR-3296, FR-2113, FR-3357, FR-3495, FR-3496, FR-3535, FR-3566, FR-3276 | - | no documented claim touched | read |
| FR-3411 / 3417 / 3422 / 3423 / 3497 | - | **no Activity Log page exists** in the docs (workspace Activity Log, Flows Activity Log, the WS_* / ACC_* / SYS_* operation catalogue) - a whole screen undocumented; decision for Mark | - |

Product finding: **FR-3596** filed - the right panel (Settings tab, and the View page) crashes with `Cannot read properties of undefined (reading 'customer')` on a flow whose Condition references `{{Initial Data->customer}}`, built through the MCP flow builder; a console-built flow does not crash.

Open contradiction for Mark: FR-3349 says the Professional trial expires **down to Free**; FR-3321 (the billing page's source) says the charge is attempted and the subscription goes past due. The page keeps FR-3321's account.

**Prod pass, 2026-09-17 (Mark signed the browser in to app.flowrunner.ai):** selector rungs 300/3,000 and 12,000/30,000/60,000 DRIVEN; FR-3441 unwrapped result DRIVEN on api.flowrunner.ai (Cart Summary run FEAD9180); the "Instance not found" screen DRIVEN (the 2026-08-25 run is gone - 404/28068 over the API as well); `instances/find` answers `{ hiddenItemsCount, items }`. Still not seen anywhere: a workspace on trial, Free, or past due; a run inside storage but outside visibility (hidden count 0 on every flow tried).
