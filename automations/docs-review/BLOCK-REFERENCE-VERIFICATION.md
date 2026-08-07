# Block Reference — Verification Punch-List

Full audit of all 33 Block Reference pages (4 parallel adversarial passes, 2026-07-07) against the
YAML sources, provenance, VOICE.md, and DEFINITION_OF_DONE.md. This tracks (a) fixes already made
and (b) the remaining **needs-verify-in-product** items. Product-truth claims that read *inferred*
(V-config provenance, single-observation inferences, schema-derived enums) are listed for a live
in-product confirmation pass. Status: [x] fixed · [ ] open (needs product verification).

## Already fixed (2026-07-07)
- [x] **Generator: `.fr-block` spans leaking into inline code + image alt** — `render.py` `_PROTECT` now
  handles double-backtick spans and tolerates `]` inside alt/link text. 0 leaks across all 39 pages.
- [x] **doclint: `_CODE`/`_IMAGE`/`_LINK_TEXT`** mirrored the same fix (double-backtick stripping, `]`-in-alt).
- [x] **Moderate Content example branch logic** — flagged (`== true`) now takes the **Yes** path (was "No").
- [x] **Trigger-as-start** — `set-variables` and `value-router` examples reworded ("When a run starts…" /
  "each run starts with…") to stop conflating trigger data with Initial Data.
- [x] **flows-as-agent-tools** — External Callback first mention now linked.

## Verified in-product 2026-07-08 (config panels + captured results)
- [x] **Error Handling / Handle Error error shape** — a real captured AI Agent failure returned
  `{ code: 28063, source: "AI Agent", message: "Cannot read properties of null…" }`. Confirms `{message, source, code}`,
  the 28063 code's realism, and that `code` is FlowRunner's own numeric code (NOT an HTTP status). Page is correct.
- [x] **Return Result — Compose Result toggle + Content Type** — driven in-product: toggle ON = Property/Value rows,
  OFF = single Result expression; Content Type = JSON/XML/Plain Text. YAML now documents the toggle + both states + enum.
- [x] **Call Flow** — `Wait for completion` toggle, `Assign to a Variable`, and a **Version** selector (appears once a
  Flow is chosen) all confirmed. Fixed the anomalous `{{Call Flow Result:id->}}` colon syntax to the verified arrow
  form `{{Call Flow Result->id}}`, and added the Version field to config.
- [x] **Synchronize** — Max Waiting Time offers **Expression Mode** (Days/Hours/Minutes/Seconds + expression). Page correct.
- [x] **Condition** — fields Value to Check / Value Data Type (dropdown) / Operation / Reference Result Data As, with
  **bracket grouping `( )`** present. (Full Value-Data-Type enum + per-type operations still to enumerate via the dropdown.)
- [x] **External Callback — Learning Mode location** — NOT in the settings panel (panel = Callback URL / Reference Trigger
  Data As / Logging); it is a **block hover-toolbar** control. `executionParam`/`userToken` are internal, not surfaced fields.
  YAML now states where Learning Mode lives.
- [x] **Custom Cloud Code known-bugs** — surfaced (bare-scalar return failure; BigInt/circular false-success; BigInt added to serialization limits).
- [x] **Knowledge Bases In Memory** — the create dialog flags In Memory non-persistent (⚠) but shows no explicit "6-hour"
  TTL / lock / status text, so the unverifiable specifics were softened.

## STILL OPEN — need enum-dropdown inspection or a live run

### Config enums (open the block's dropdown)
- [ ] **Condition** — Value-Data-Type enum + the per-type operation lists
- [ ] **Value Router** — Collection and Range modes + Everything Else
- [ ] **Wait** — the "Wait for" field label + confirm expression resolves to seconds
- [ ] **Transform Data** — the full operation list
- [ ] **Shared Memory: Put** — Override default + the OFF-state behavior
- [ ] **Set Variables** — Skip Block presence in common settings
- [ ] **KB Add / Delete-by-Filter** — the Metadata "single object" alternative mode

### Result shapes / behaviors (need a live run with keys/services — best captured by running representative flows)
- [ ] **HTTP Request** — status/headers exclusion + `HTTP Method` default
- [ ] **Repeat** — pre-check-then-run + 0-based `Current Iteration`
- [ ] **KB Add Document** — `status` field + exact `Processing`/`Completed` casing
- [ ] **KB Delete-by-Filter** — the `count` result key
- [ ] **Speech to Text / Text to Speech** — result shapes + enum members
- [ ] **Shared Memory: Delete** — Mode=All wipes an AI Agent's Messages History
- [ ] **Break** — ends only the nearest enclosing loop (outer continues)
- [ ] **Wait** — only its branch pauses; parallel branches keep moving
- [ ] **Synchronize** — a dropped branch's result on timeout
- [ ] **Value Router** — top-to-bottom first-match ordering
- [ ] **Triggers Group** — window/race modes (at-least-one vs all-within-window)

### Screenshot recaptures
- [ ] **Call Flow** — shot should show the worked scenario (Create Beneficiary, not Email Sender)
- [ ] **Return Result** — token/expiresAt scenario + a Compose-OFF shot
- [ ] **External Callback** — a shot of Learning Mode (on the hover toolbar)
- [ ] **Speech to Text / Text to Speech** — no screenshot at all (below the block+config floor)

## HIGHEST-PRIORITY in-product verifications
1. **HTTP Request** — does the result truly exclude the **status code and response headers**? The page asserts
   "you cannot test the numeric status to tell success from failure," built on one happy-path GET. If wrong,
   it misdirects error-handling design across the docs. (blocker-class claim.) Also confirm `HTTP Method` default.
2. **Custom Cloud Code** — surface the two documented `known_bugs`: `return 42` fails ("Invalid status code: 42",
   wrap scalars); returning a BigInt/circular ref reports **Success** but silently swaps the result for a
   serialization error object (high-severity false-success). Add BigInt to the serialization-limits list.
3. **Return Result** — Compose Result **toggle ON *and* OFF** + **Content Type** enum (JSON/XML/Plain Text).
   Page documents only the ON/JSON state (the exact 2026-07-06 failure). *(Already verified in-product this cycle:
   ON = Property/Value rows, OFF = single "Result" expression, Content Type = JSON/XML/Plain Text — apply to YAML.)*
   Also the **multi-Return-Result envelope** shape (first result / list tagged by block name / overall status).
4. **Repeat** — whole-block live run (only V-config page): pre-check-then-run order, `Current Iteration` 0-based,
   `{{Current Iteration}}` readable in the condition/body, 10000 default. (Also reconcile stale `data_out`.)
5. **Value Router** — **Collection** and **Range** modes (Range inclusive on both bounds?) + top-to-bottom
   first-match ordering + the `Value Router Result` alias. Only Single Value is evidenced.
6. **External Callback** — where **Learning Mode** lives (likely a block hover icon, not the panel; add a shot at
   first reference) and what `executionParam` / `userToken` config keys surface as; mid-flow resume semantics.
7. **Call Flow** — the undocumented **Version** field + the toggle beside `Flow` in the config panel; confirm the
   `Wait for completion` label and capture both states. Reconcile result-alias syntax `{{Call Flow Result:id->}}`
   (colon) vs the `->`-drill form on subflow/return-result — one is likely wrong; unify.
8. **Triggers Group** — run **both** modes (at-least-one / all-within-window) to lift the schema-inferred window/race
   behavior to verified (V-config).
9. **Shared Memory: Delete** — confirm Mode=All actually wipes an AI Agent's **Messages History** (V-config claim).
10. **KB result envelopes** — Add Document `status` enum casing (`Processing`/`Completed`); Delete-by-Filter `count`
    key name; List Documents wrapper keys beyond `files`.

## Per-page needs-verify (grouped)
**AI / integration:** ai-agent (screenshot model label only — otherwise solid) · ai-router (panel label
"AI Decision Request (prompt)") · ai-content-moderation (abbreviated 13-category enum still faithful?; nested
`category_scores.violence` read form) · **ai-speech-to-text** (result `text` shape unverified V-config; MP3…/25MB
enums are OpenAI-derived; **no screenshot**) · **ai-text-to-speech** (result `fileURL` unverified; voice/model/format
enums + 4096-char limit OpenAI-derived; **no screenshot**; "leave on tts-1-hd" vs default tts-1) · http-request (see #1) ·
custom-cloud-code (see #2) · transform-data (operation-name-derived aliases e.g. `Sort List Operation Result`).

**Memory / knowledge:** shared-memory-put (Override default + OFF-state behavior; palette wording) · shared-memory-read
(default alias `Shared Memory: Read Result` verbatim; doubled Default-Value tooltip sentence — editorial) · shared-memory-delete
(see #9; `Keys`/`All` radio labels) · knowledge-base-add-document (status enum #10; Metadata single-object mode) ·
knowledge-base-list-documents (Limit/Offset default paging) · knowledge-base-delete-document (block-name casing "Delete
**by** Filter" not "By"; result contents) · knowledge-base-delete-by-filter (`count` key #10) · set-variables (unset-var→0
arithmetic coercion the counter depends on; Skip Block presence in common settings; expression pseudo-syntax vs real pills).

**Control flow:** condition (Value Data Type enum + per-type operations + `Condition Result` alias + brackets/precedence UI) ·
break (nested-loop = inner-only; "no result" vs `storeResult` key) · repeat (see #4) · list-iterator (`Data Buckets:…->` read
token; pixel-check 5 shots — strongest evidence otherwise) · wait ("Wait for" vs Days/Hours/Minutes/Seconds label; expression
resolves to **seconds**) · synchronize (Expression Mode support on Max Waiting Time; timeout-drops-branch-result; topology shot) ·
value-router (see #5; Everything Else non-removable) · handle-error (strongest page; drop duplicated `Reference Result Data As`
config row — editorial).

**Structure / flow control:** call-flow (see #7) · subflow (`Assign to a Variable` shown but absent from common settings;
SubFlow-nesting truly blocked?) · return-result (see #3) · external-callback (see #6) · assign-instance-name ("GUID"→"Instance
ID" term; trigger-payload-vs-Initial-Data phrasing) · actions-group (exemplary; reconcile `produces_result: true` vs "no combined
result") · triggers-group (see #8) · start/stop-scheduled-runs (accurate incl. known dropdown-lists-all-flows bug; generic-scenario
screenshots — soft).

## Screenshot gaps / scenario mismatches (recapture)
- **No screenshot at all:** ai-speech-to-text, ai-text-to-speech (below the block+config floor).
- **Shot shows the wrong scenario** (pixels contradict the worked example): call-flow (Email Sender vs Create Beneficiary),
  return-result (status/amount vs token/expiresAt); soft: start/stop-scheduled-runs (Scheduled Runs vs Email Sender/Nightly Report).
- **Missing a control's shot:** external-callback Learning Mode; return-result Compose OFF; call-flow Wait-for-completion.
- Pixel-eyeball (per DoD "judged by the pixels") the multi-shot pages (list-iterator ×5, condition, value-router, wait, synchronize).
