# Awaiting Mark's review — rolling list

The pages handed over and waiting for Mark. Kept current: add a row when something is handed over,
move it to **Signed off** when Mark clears it, and note any change he asks for. Mark is the final
authority — a `ship` verdict in `verdicts/` is the gate's opinion, never the sign-off.

## Pages waiting for review

| # | Page | State | Since |
|---|------|-------|-------|
| 5 | [Custom Cloud Code](../content/reference/custom-cloud-code.md) | **Release 1.0.13 (FR-3102/FR-3227) rewrite, gate `ship`** ([verdict](verdicts/custom-cloud-code.md)). The runtime changed wholesale and was fully re-probed in-product: fetch/Buffer/crypto/timers now available (new "What the code can use" section), 10s cap gone (65s verified; memory is the ceiling - 100MB ok, 200MB crashes the pod), both known bugs fixed and removed, the un-awaited-rejection behavior REVERSED (now crashes the environment - documented), agent-tool attach corrected to the verified Manage Capabilities ▸ Utils flow, and a NEW canvas screenshot of the worked chain (Fetch Orders → Count Open Orders → Any Open? → Save Open Order Ids, built Ready in Runtime Probe). quickstart-code.md's "no network access" claim also removed. doclint 0/0. | 2026-08-14 |
| 6 | [Knowledge Bases](../content/reference/knowledge-bases-concept.md) | **Release 1.0.13 (FR-3316) rewrite — CLOSED per Mark 2026-08-15** ([verdict](verdicts/knowledge-bases-concept.md)). In-Memory store removed; the create dialog is now a two-step wizard (all three stores driven, tooltips captured, two fresh shots: setup + storage). The two remaining screenshot recaptures are deliberately not being done — Mark: "KBs are verified by our QA, no need to redo the work." Nothing outstanding. | 2026-08-14 |
| 7 | [Monitoring & Analytics](../content/run/monitoring.md) + [Inspecting a Single Run](../content/run/inspecting-a-run.md) | **Release 1.0.13 (FR-2958) addition + full re-drive; Mark's three calls applied 2026-08-15** ([verdict](verdicts/monitoring.md)). NEW Retry attempts section verified on a real errored run; the Errors payoff shot live; all July claims re-driven and every shot recaptured. Per Mark: page SPLIT into health views (Monitoring & Analytics) + single-run drill-down (Inspecting a Single Run, new nav entry); Shorten IDs confirmed a BUG (Mark files in Jira; docs stay silent on the control); demo-data fix approved and applied (Order Poller order-shaped data + payload relaunch, two shots recaptured). | 2026-08-14 |
| 1 | [Retrieving Block Results](../content/api/block-results.md) | Never reviewed. 21-line placeholder for the unreleased block-results API; routes to the Test Monitor and run history in the meantime. **No gate verdict on disk.** | 2026-08-05 |
| 2 | [API (section index)](../content/api/index.md) | Revised 2026-08-06 at Mark's request against this session's corrections: LIVE claim corrected (it contradicted `activating-a-trigger.md`), "Everything a flow does…" overclaim cut, endpoint choice stated, "rarely" quantifier and "section above" deixis removed, unverified key-revocation timing dropped. **No gate verdict on disk.** | 2026-08-06 |
| 3 | [AI in Flows](../content/build/ai-in-flows.md) | Ready for Mark. NEW 8th Build unit (single teaching page + map): five manifestations on one support-desk story, each shot from a kept scenario flow (Order Intake / Refund Check / Ticket Router / Draft Reply). Run-proven: AI Transform (10473), AI Router ({"decision":"Billing"}; Everything Else proven non-removable), AI Agent (reply under `output`, consumed by Send Reply). AI QUESTION verified on all 7 data types; **the aiQuestion 6-arguments runtime bug is FIXED and verified live 2026-08-07** (both exits driven; shot recaptured with the real Success result). Mark's review round (read-syntax pills, page-level Related, section order, roadmap, scaffold, model-first shot) applied 2026-08-06. Companion: condition.yaml AI QUESTION section + refgen. Gate `major-rework` cleared in one pass — verdict + 19-item resolution table in [verdicts/ai-in-flows.md](verdicts/ai-in-flows.md); ledger section added with 8 filed follow-ups (api-keys.md staleness, ai-router result shape, ai-agent Files field, ...). doclint 0/0. **Follow-up batch resolved (Mark's ask)** — all 8 closed, item-by-item in the ledger (the last, the aiQuestion runtime bug, closed 2026-08-07 after the fix landed). | 2026-08-06 |
| 4 | [API Keys](../content/platform/api-keys.md) | REWRITTEN to the current product (was "AI API Keys", stale): retitled + nav label updated; location stated (Connections ▸ API Keys); three tabs documented (My Keys / AI Providers / Custom); provider catalog updated (+DeepSeek, Kimi, Voyage AI); NEW custom-keys section (Add Custom API Key dialog, driven); Save-as-Setup re-driven live. Six fresh shots, all read back, incl. a NEW sidebar-location shot and the in-block Saved API Key Setups popover. Inbound link texts updated on 4 pages (workspace, oauth-connections, quickstart-agent, ai-in-flows). doclint 0/0. Part of the ai-in-flows follow-up batch. | 2026-08-06 |

## Signed off

### 2026-08-06 — Mark's page-by-page review
Reviewed live in session; every correction applied and verified in the same turn.

- ✅ [Data & Variables](../content/build/data-and-variables/index.md) — intro reframed after "moving data is not what building a flow is about".
- ✅ [Passing Data Between Blocks](../content/build/data-and-variables/passing-data.md) — alias and Assign to a Variable corrected to optional switches; "most of which" quantifier cut.
- ✅ [Reshaping Data](../content/build/data-and-variables/reshaping-data.md) — "the value does not exist yet" reworked; "choosing the operation is the whole job" corrected (assembling the inputs can be the larger job); "almost never" cut.
- ✅ [Holding Values in Variables](../content/build/data-and-variables/holding-values.md)
- ✅ [Sharing Data Across Runs & Flows](../content/build/data-and-variables/across-runs.md) — counter lead-in scoped to "across runs" per Mark.
- ✅ [Integrations & I/O](../content/build/integrations/index.md)
- ✅ [Calling an External Service](../content/build/integrations/calling-a-service.md) — 6 Mark points: dedicated-block section retitled and given the how (palette Search box); "headers identify you" corrected; the credentials-only header section folded back into the block's four fields; config shot moved to where it belongs; "Make the call survive a bad day" → "When a call fails"; Retry Policy deep-linked.
- ✅ [Returning a Result](../content/build/integrations/returning-a-result.md) — circular lede replaced (subject is now the flow producing a result, not the caller waiting); **REST caller corrected from an exclusion to a reader** (`activate-blocking` returns the composed result — the page had contradicted `api/call-flow.md`); impossible "blocks wired after it never run" removed at the YAML source.
- ✅ [Running Another Flow](../content/build/integrations/running-another-flow.md) — Initial Params taught with the real column names (Property/Value) and the example matched to the screenshot; "the Property here" clunker cut; ambiguous "that block's alias" resolved.
- ✅ [Custom & Marketplace Actions](../content/build/integrations/custom-actions.md) — rebuild admonition removed per Mark.
- ✅ [Call Flow](../content/api/call-flow.md) — 5 Mark points earlier; 2026-08-06 added the Launch Flow Instance dialog's blocking-URL behaviour (a flow containing Return Result gets the blocking URL — the dialog states it verbatim and the shipped screenshot showed it while the prose did not).
- ✅ [Activating an External Callback](../content/api/activating-a-trigger.md) — 14 Mark points, full rewrite; LIVE claim corrected (Learning Mode / Run Block answer without a LIVE version).
- ✅ [Welcome](../content/index.md) — vision-led opening per Mark's brief; hero screenshot; diagrams removed.
- ✅ [Quick Start: A Contact Us Form](../content/learn/quickstart.md) and [with code](../content/learn/quickstart-code.md)
- ✅ [Quick Start: An AI Agent](../content/learn/quickstart-agent.md) — Mark confirmed finished 2026-08-06.

### Closed earlier (rows carried from the previous list)
All handed over June–July 2026 with their gate findings cleared; struck 2026-08-06 after confirming
the recorded issues are fixed in the current content.

- ✅ [Expression Editor](../content/learn/concepts/expressions.md) — approved exemplar.
- ✅ [Variables & Data Buckets](../content/learn/concepts/variables.md) — approved exemplar.
- ✅ [Shared Memory](../content/learn/concepts/shared-memory.md)
- ✅ [Per-User Memory](../content/reference/per-user-memory-concept.md) — 2026-08-06: tab name reconciled to **Flow Settings** (it said "Settings" while its sibling said "Flow Settings"; the live tooltip is "Flow Settings"). Same fix applied to `across-runs.md`.
- ✅ [Agent Memory](../content/reference/flow-memory-concept.md)
- ✅ [Subflows](../content/learn/concepts/subflows.md)
- ✅ [Terminology](../content/definitions.md)
- ✅ [Running Steps in Parallel](../content/build/flow-control/parallel.md) — work list cleared in one pass 2026-07-14.
- ✅ [Adding a Delay](../content/build/flow-control/waiting.md) — work list cleared in one pass 2026-07-15.

## Open follow-ups (not review items)

- **`docs-review/` is untracked in git** — no history exists for any verdict or ledger.
- **The API section has never been gated.** `call-flow.md` and `activating-a-trigger.md` went to Mark
  without a verdict; the 14-point review that followed is what the gate exists to prevent.
- **[flow-execution/overview.md](../content/flow-execution/overview.md)** still documents the
  pre-rebrand `backendless.app/api/automation/flow/activate-by-name` endpoint, contradicting the API section.
- **[reference/ai-agent.md](../content/reference/ai-agent.md)** documents Force Parsed Output and
  Messages History, neither present in the block's panel; the panel's Files section is undocumented;
  capability counts are stale.
- **Anchor links are not validated by the build** — no `validation:` block in `mkdocs.yml`, so a deep
  link that rots when a section is retitled fails silently.
- **39-file refgen diff** (+1761/-1034) sitting uncommitted, flushed through from Mark's earlier
  `block-knowledge/*.yaml` edits.
- **Rules applied this session but not yet written into VOICE.md**: don't present one part of a
  multi-part task as the task; link the section, not the page; floating deixis ("here", bare "above",
  "that block's" with a competing antecedent) is a defect.
