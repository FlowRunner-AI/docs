# Gate verdict — api/execution-status.md

- **Date:** 2026-08-25
- **Gate verdict:** `major-rework` (concept-page-review, run wf_74029faf-83f — 6 lenses + synthesis)
- **doclint:** 0 errors / 0 warnings (with `--warnings`)
- **Status:** NEW page. Blockers partially cleared in one pass (below); **not yet re-gated, so not
  ship.** Do not present to Mark as ready until a re-run returns `ship`.

## Why the page exists

`content/api/block-results.md` and `call-flow-nonblocking.md` both told readers that no call returns a
run's outcome by id. That stopped being true on 2026-07-28. The Execution Status & Results API (Jira
FR-3238) shipped across three releases — FR-3242 status in **v1.0.12**, FR-3243 block result in
**1.0.13**, FR-3342 finalising both paths under `flow/{flowId}` in **v1.0.14**. Both endpoints were
driven end to end on 2026-08-25; log in `.cache/api-spec/verification-2026-08-25-execution-api.md`.

**The written spec in FR-3238 does not match the shipped product.** Statuses are uppercase and the
vocabulary differs: `RUNNING` / `PENDING` / `COMPLETED` / `TERMINATED`, not the spec's
`running` / `suspended` / `completed` / `failed`. The page follows the product.

## Gate summary (verbatim)

Not ready. The spine is genuinely good — artifact-first lede, correct teaching order, the right central
lesson (COMPLETED + hasErrors), a runnable poll recipe, seven ToC entries, and a real dated drive log —
but six blockers stand: the lede says the API "started a flow" (Mark's flow-vs-instance correction), the
page ships zero screenshots while its two central sections teach fields that are literally on screen in
the Instances tab, three paragraphs assert behavior the page's OWN header records as NOT DRIVEN
(truncation semantics, handled-error ordering, caught-plus-fatal coexistence), the page never tells the
reader this endpoint cannot return the flow's answer, the "three outcomes" table omits the hand-stopped
TERMINATED case the page itself introduces, and there is no ledger section or verdict file, so nothing is
cleared with evidence.

## Blockers — resolutions

| # | Blocker | State |
| --- | --- | --- |
| 1 | Lede said the API "started a flow" — violates the flow-vs-instance rule | **FIXED.** Now "started a run of a FlowRunner™ flow"; lede widened to any run whose id you hold |
| 2 | Truncation paragraph asserted cap behavior the page's own header records as NOT DRIVEN | **FIXED.** Scoped to the observed value (`false` on every run behind the page) and what `true` signals; the cap number is not claimed |
| 3 | Central lesson (COMPLETED + hasErrors) pictured nowhere | **FIXED.** Captured `execstatus-completed-haserrors.png` — the Instances row for run 5932DC8F, the same run whose JSON the page prints, HAS ERROR ticked + STATUS COMPLETED. Also closes an open item recorded on `inspecting-a-run.md` |
| 4 | The four statuses no-shot rationale claimed coverage on Inspecting a Run that does not exist | **FIXED.** Rationale removed, real shot added |
| 5 | Page never says this endpoint cannot return the flow's own answer | **FIXED.** Stated where the COMPLETED payload lands, routing to Call Flow (Blocking) |
| 6 | No ledger section, no verdict file | **PARTIAL.** This verdict file exists; the PLATFORM-REVIEW-LEDGER section is still owed |

Also fixed from the majors/minors: handled-error ordering claim ("newest last") dropped — it rested on
a sample of one; "the same shape" corrected to "the same three fields" (the samples disagreed); the
28068 error sample no longer uses an id the page shows as a live run; hand-stop located on the Instances
tab; HTTP status added to every error row; the garden-path polling sentence rewritten.

## Still owed before a re-gate can return ship

**Drives:** 21+ handled errors in one run (truncation + which end is dropped); two ordered handled errors
(ordering); one run with a caught failure AND a fatal one (the combination is asserted, never produced);
a run sitting in a Wait and one at a Synchronize (does either report PENDING? external-callbacks.md says
a run held at a mid-flow trigger is RUNNING — the two pages currently disagree); the callback hold limit
and what a run reports after it expires; retention horizon; whether reads consume the execution
allowance and what the poll rate limit is; lower-cased flow id on this endpoint; `flowVersion` on a run
whose flow has since had a new version made LIVE.

**Shots:** an Instances frame carrying RUNNING/PENDING (the Payment Hand-off Test run at its callback is
the highest-value frame).

**Structure:** split "Making the call" into request and "What comes back" so the response object has its
own anchor; add a RUNNING body under the poll loop; bound the poll example in the script itself and guard
it against a body with no `status` key; add the Instances tab as a source for the execution id.

## MARK — decision owed

- [ ] **The API key segment is not enforced on these read endpoints.** A garbage key returns the full
      status payload and block results (driven 2026-08-25). On `activate` this defect spends executions;
      here it **discloses run data and stored block results** to anyone holding the URL shape. Same
      defect class already on record for Call Flow, higher consequence. Not documented on the page.
