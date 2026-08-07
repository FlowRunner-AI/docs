# Screenshot recapture punch-list

## VALIDATED CAPTURE METHOD (2026-06-24) — the procedure for every clean shot

The blocker on clean shots was the `automation-expression-input` fields + the error badge. Resolved and proven on Moderate Content:
1. Drop the block; type values into its fields — **typed values DO register** (the value shows in the field). For an *expression/reference* value, use the field's wand icon → Expression Editor → Block Data → double-click the field (inserts `{{Alias->field}}`); for a *literal*, type it.
2. The block's red "N" badge on a standalone block is **a connectivity error (no predecessor), not a field error.** **Wire the block to a predecessor** (force handles visible via CSS `opacity/visibility/display !important`, then Playwright `dragTo` from a source handle to the target handle) → the badge clears to `none`.
3. Declutter the canvas (delete unrelated test blocks via the panel DELETE button + confirm dialog), compose (pan the viewport so the block sits beside the config panel), move the real mouse off-canvas (hover a sidebar item) to clear hover artifacts, remove forced-handle CSS, hide scrollbars.
4. Screenshot the viewport → crop with PIL to block+config (no error badges, no clipped controls) → READ the crop back to verify → save to `content/images/reference/`.



Systemic finding (goal push, 2026-06-23): across the existing block reference pages, **prose is largely sound but many screenshots show placeholder / default / empty / error-state configs that don't match the worked example** — the exact match-scenario defect Mark flagged on Actions Group / Triggers Group. Prose fixes are applied per-page (HOW-to-read, WHERE/palette, chips, dead cross_refs, imperative-voice, name consistency). The screenshots below need in-product rebuild + recapture to match each page's worked scenario.

Status legend: ☐ to do · ☑ recaptured

## Wave 1 (prose fixed)

- ☑ **condition** `condition-config.png` — RECAPTURED 2026-06-24: Value to Check = `{{Initial Data->amount}}` (bound pill via Expression Editor → Variables → Initial Data), Value Data Type INT, Operation GREATER THAN, Value 1000; Yes→Set Variables / No→Set Variables fork shown, no badges. Image MOVED from end-of-example to right after the config-setup paragraph (screenshot-at-reference rule); alt rewritten (old alt wrongly said status/STRING/EQUALS/cancelled). 2nd multi-part shot (OR expedited IS TRUE) still optional/deferred.
- ☐ **list-iterator** (5) `list-iterator-{expression,seed,condition,transform,loop}.png` — Condition named **"Order cancelled?"**, Transform Data named **"Add To List Operation"**; show List Iterator block+config (List bound to orders result), the loop body, and the Expression Editor building `{{Current Iteration Item->...}}`. Replace floating panel-fragments with block+config shots.
- ☑ **repeat** `repeat-config.png` — RECAPTURED 2026-06-24: stepped-into the Repeat (loop body), built Start → Wait → HTTP Request → Set Variables (all badge-free, HTTP given a URL), captured the "Block Repeat" body view. Image repositioned after the loop-body paragraph; alt rewritten to describe the body (Condition/Max-Iter are in the example prose, not in the body image — and Max Iteration is a READONLY stepper field, can't be typed; condition needs a real bucket var). **LOOP-BODY MECHANIC LEARNED: hover the loop block → click the fa-expand icon → step into a sub-canvas (header "Block \<name\>" + RETURN), Start node + "drop a block here"; drop blocks + wire Start→…; RETURN to exit. Applies to list-iterator + break.**
- ☑ **set-variables** `set-variables-config.png` — RECAPTURED 2026-06-24: Data Bucket = Ticket (created via type-to-create), greeting = `"Hi " + {{Initial Data->requester}} + ", we are on it."` (compound expr — Initial Data renders as a clean pill, confirmed in Live Preview), processedCount = `{{Ticket - processedCount}} + 1` (bucket-var pill), badge clear. Image repositioned after config code block; alt rewritten. **NEW: compound expressions in the Expression Editor tokenize correctly when typed naturally** (literals + `+` + `{{ref}}`). Also: hid React-Flow zoom controls via CSS to stop them intruding on crops (persistent).
- ◑ **transform-data** `transform-data-config.png` — RECAPTURED 2026-06-24 (primary shot): Operation Get Property Value, Object = `{{HTTP Request Result}}` (HTTP Request wired upstream), Property Name = primaryProductName, alias auto = Get Property Value Operation Result, no error badge. Image repositioned after the Get-Property-Value paragraph; alt rewritten. NOTE: Object pill shows `{{HTTP Request Result}}` (braces) rather than a clean block-result pill — raw-typed block-result refs don't tokenize like `Initial Data` does; acceptable/valid, polish via Block-Data insertion if Mark flags. 2nd Sort List shot ☑ DONE 2026-06-24: `transform-data-sort-config.png` — Operation Sort List, List = `["new", "clearance", "featured"]` (literal array via Expression Editor), Order Ascending, no badge; image inserted after the Sort-List result JSON.
- ☑ **value-router** `value-router-config.png` — RECAPTURED 2026-06-24: Value to Evaluate = `{{Initial Data->ira_product_type}}` (bound pill); 3 Single-Value branches (Performance MMA/performance_mma, Plus MMA/plus_mma, IRA CD/ira_cd) + Everything Else; all four connectors wired to Set Variables handling steps (badge clear, no "successor" error). Canvas fan-out shot; image repositioned after the "four output connectors" paragraph; alt rewritten (old said plan/premium). Minor: faint AI-Agent sliver at far-left edge — acceptable, polish later if Mark flags.
- ☑ **wait** `wait-config.png` — RECAPTURED 2026-06-24: Handle Error → Wait wired (badge clear), config panel Expression Mode off, Minutes 1 / rest 0, no error badge, DELETE header cropped out. Alt updated to note the Handle Error branch.
- ☐ **synchronize** `synchronize-config.png` — three Call Flow branches (Create Funding Method / Create Ancillary Products / Create Entity Involvement) converging into Synchronize, Max Waiting Time 0d0h1m0s (60s). Source: LIVE "Create IRA" flow.

## Wave 2 (prose fixed)

- ☑ **ai-router** `ai-router-config.png` — RECAPTURED 2026-06-24: AI Model = Gemini 3.5 Flash, AI API Key = placeholder (clears the old "AI Model/API Key required" error), AI Decision Request = "Determine the sentiment of the message", Decision Data message = `{{Initial Data->message}}` (bound pill), Expected Decisions positive/negative/neutral + Everything Else, badge clear; positive connector wired to a Set Variables. (Note: per the record, named connectors only show on hover — the wired positive one is visible; the Expected-Decisions list in the panel enumerates all four.) Image repositioned after the config paragraph; alt rewritten.
- ☑ **break** `break-config.png` — RECAPTURED 2026-06-24: built inside the Repeat loop body — Set Variables → Condition (`{{Current Iteration}}` INT GREATER THAN 5) → Yes → Break, Break selected showing its panel (Name + Notes only, confirming Break has no real config), no badges. Alt rewritten with the in-loop context.
- ☐ **call-flow** `call-flow-config.png` — wrong flow (Email Sender, Wait off). Recapture: Flow = Create Beneficiary, 3 named Initial Params rows bound, Wait for completion ON. (Follow-up: a Version/Select Version field is undocumented — verify in-product.)
- ☑ **http-request** `http-request-config.png` — RECAPTURED 2026-06-24: GET https://api.github.com/users/octocat/orgs, Body/Query empty, Header Accept=application/vnd.github+json, wired off Handle Error (badge clear), DELETE header + zoom controls cropped out. Alt rewritten with exact values.
- ☐ **return-result** `return-result-config.png` — empty config. Recapture: Issue Token subflow, two rows (token, expiresAt) filled, inside the subflow RETURN/SubFlow bar.
- ☑ **assign-instance-name**, **custom-cloud-code**, **subflow** — screenshots CLEAN, no recapture needed.

## Wave 3 (prose fixed)

- ☑ **knowledge-base-add-document** `...-config.png` — RECAPTURED 2026-06-24: KB ID = Support Articles, Content = `{{HTTP Request Result->body}}`, File Name = Resetting your password, Metadata source=support-site/category=account, badge clear (old red "value cannot be empty" gone). Image repositioned after the Metadata paragraph; alt rewritten. **RECORD FIX:** KB ID field is a TEXT/EXPRESSION field (wand), NOT a "dropdown" — corrected prose + config type + removed "the dropdown lists your KBs" claim. ⚠️ Other 3 KB records likely also say "dropdown" — fix when capturing each.
- ☑ **knowledge-base-list-documents** `...-config.png` — RECAPTURED 2026-06-24: KB ID = Support Articles, Filter area=billing & status=retired, Limit/Offset empty, badge clear. Image repositioned after the filter-config paragraph; alt rewritten; KB ID "dropdown" → expression-field corrected.
- ☑ **knowledge-base-delete-document** `...-config.png` — RECAPTURED 2026-06-24: KB ID = Product Manuals, File ID = `{{Knowledge Base: List Documents Result->files[0].fileId}}`, badge clear (old red "2" gone). Image repositioned after config paragraph; alt rewritten; KB ID "dropdown" → expression-field corrected.
- ☑ **knowledge-base-delete-by-filter** `...-config.png` — RECAPTURED 2026-06-24: KB ID = Product Catalog, Filter source=nightly-import & importDate=2026-06-14, badge clear. Image repositioned after config code block; alt rewritten with specifics; KB ID "dropdown" → expression-field corrected. **All 4 KB shots DONE.**
- ☑ **shared-memory-put** `...-config.png` — RECAPTURED 2026-06-24: Override on, Perform Changes runCount = `{{Read Count}} + 1`, badge clear (old "(no value)" gone). Image already well-placed; alt rewritten with specifics.
- ☑ **shared-memory-delete** `...-config.png` — RECAPTURED 2026-06-24: Mode=Keys, Key=cursor, badge clear (old empty-Key error gone). Image repositioned after the config code block; alt rewritten with specifics.
- ☑ **external-callback, shared-memory-read, start-scheduled-runs, stop-scheduled-runs** — screenshots CLEAN.

Note: shared-memory-delete prose had a UI-model error (framed as an All toggle; the real control is a **Mode** radio with All/Keys + a Key list) — fixed in prose.

## Final review batch (prose fixed)

- ☐ **ai-agent** `ai-agent-config.png` (minor) — System Prompt shown is abbreviated; recapture with the example's full System Prompt. Config is otherwise clean (Demo API Key filled, User Prompt a bound Expression-Editor pill). Optional: a `ai-agent-capabilities` shot with a group expanded + the two example tools attached.
- ☐ **flow-memory-concept** `flow-memory-messages-history.png` — toggle shown OFF on a page about turning memory ON; recapture with Messages History ON, Limit 15.
- ☑ **flows-as-agent-tools-concept** — screenshots CLEAN.

## NEW block records — IN-PRODUCT VERIFICATION DONE (2026-06-24)

Verified each against the live palette. Result:
- **KEPT (native AI blocks) — CONFIG NOW VERIFIED IN-PRODUCT (V-config), records corrected:**
  - `ai-content-moderation` (**Moderate Content**, id matches): fields Text Content + Images ✓; alias corrected `ModerationResult`→**Moderate Content Result**.
  - `ai-speech-to-text` (**Speech to Text**; real element id `ai-create-transcription`): fields Model/File URL/Language/Prompt/Temperature ✓; no per-block API key; alias **Speech to Text Result** ✓.
  - `ai-text-to-speech` (**Text To Speech**, id matches): fields Input/Model(tts-1)/Voice(alloy)/Response Format(mp3)/Speed ✓; **removed an invented "AI API Key" field**; alias casing fixed to **Text To Speech Result**; removed a broken image ref.
  - ☑ **Moderate Content — FULLY DONE**: result shape RUNTIME-VERIFIED by running it live (V-real — confirmed categories[13]/category_applied_input_types/category_scores/flagged/flaggedCategories, matching the record exactly); screenshot `ai-content-moderation-config.png` captured + inserted (block+config, Text Content = the comment, alias, no error badges). Record corrected (alias, config_keys=moderationContent).
  - ⏸ **Speech to Text, Text To Speech** — config verified (V-config). **DEFERRED per Mark (2026-06-24): "safely skip Text to Speech and Speech to Text for now."** Records stay at V-config (fields/aliases corrected in-product); runtime-shape verify + screenshot are parked, not abandoned. (STT also needs a public audio File URL to run, which we don't have on hand.)
- **PULLED — ghosts (do not exist in product):** `ai-assistant` (superseded by AI Agent), `applogic-trigger` (no "app logic"/"applogic"/"codeless" match). Records + pages deleted.
- **PULLED — Backendless *extension* blocks, not native core (Mark's call: keep Block Reference native-only):** `save-record`/`find-records`/`delete-record` (real names "Save Record In Database", "Find Record(s) in Database", "Delete Record In Database"), `send-email`, `record-saved`/`record-updated`/`user-registered` (real names "On Record Created/Updated", "On New User Registered"). All live in the palette beside Airtable/Salesforce/SMTP equivalents. Records + pages deleted; `triggers.md` and `blocks.md` revised to native-only (Data category removed; integration triggers/actions framed as extension-provided). Block Reference now 38 native records.

## PLATFORM-PAGE VERIFY markers — IN-PRODUCT VERIFICATION (2026-06-24)

Navigated the live workspace nav + each screen. **10 of 14 VERIFY markers resolved with confirmed facts; 6 remain.**
- ☑ **workspace.md** — flow tabs (Edit/Dashboard/Performance/Instances/SLA Goals/Logs/Version Admin) confirmed; Compliance & security nav-group items confirmed; **CORRECTED a real error: the top switcher is a WORKSPACE switcher (lists Calibrate/Demo/MyProjects/… + "New Workspace"), NOT a "project switcher" — "MyProjects" is a workspace name, there is no project sub-level.** Remaining: ☐ execution definition (line 15 — needs billing confirmation).
- ☑ **compliance-and-security.md** — Audit Log (records developer/access actions; columns Date/Developer/Event/IP/Device; filter/search/date-range/download/delete); Compliance = **HIPAA**: accept an electronic BAA → Activate HIPAA Compliance (for PHI); Panic Mode = compromised-credentials lockdown (kills Console sessions, blocks Console, logs out app users, rejects API, stops Cloud Code timers; Activate/Deactivate); SLA Calendars = Time Zone + Work Week (per-day toggles + time spans, split spans via +) + Excluded Dates (holidays), Create a New Calendar. Remaining: ☐ SLA Goals tab composition (line 20 — needs a flow with a configured goal).
- ◑ **forms.md** — builder location + surface confirmed (Forms nav → open a form → Designer/Preview/Themes/Logic/JSON Editor, left toolbox, center canvas, right props); **question types confirmed** (Single-Line/Long Text/Multiple Textboxes; Radio/Checkbox/Dropdown/Multi-Select/Boolean/Image Picker/Ranking; Rating Scale/Slider; File Upload; Matrix ×3; Panel/Dynamic Panel) — builder IS Survey Creator/SurveyJS per the in-app banner, **never named in docs per the rule**; publish = public form URL via VIEW (`/api/public/app/{id}/form/{id}`). Remaining: ☐ form→flow connection mechanism (19, 23), ☐ where responses are listed (38), ☐ cross-links (43).

SCREENSHOT-NEEDED markers across these pages are a separate batch (the live Audit Log shows real emails/IPs → needs privacy-safe capture; Compliance/Panic/SLA/Forms screens are PII-safe and ready to capture).

## NEW concept-page SCREENSHOT-NEEDED markers (Phase 3) — still pending

- `learn/concepts/blocks` — palette+canvas; a block's config panel (common settings); Expression Editor reading a result
- `learn/concepts/variables` — Set Variables config (Ticket bucket)
- `learn/concepts/expressions` — Expression Editor: Block Data → result → `{{...}}` built (reuse/adapt `handle-error-read.png`)
- `learn/concepts/subflows` — SubFlow config (Initial Params)
- `learn/concepts/shared-memory` — Put / Read / Delete config panels (3)

---
**Phase 1 status: all 30 block pages + 5 concept guides reviewed & prose-fixed.** Recapture debt above (~22 shots) is the remaining in-product workstream for these pages. Already-clean (no recapture): assign-instance-name, custom-cloud-code, subflow, external-callback, shared-memory-read, start-scheduled-runs, stop-scheduled-runs, flows-as-agent-tools-concept (+ the recently-reworked actions-group, triggers-group, handle-error, error-handling-concept, flow-scheduling-concept, knowledge-bases-concept).
