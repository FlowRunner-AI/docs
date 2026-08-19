# Doc-triage stage-2 prompt - eval results (2026-08-12)

30 real FR tickets (status Closed / Waiting for Release), one fresh Opus agent per
ticket running specs/doc-triage-stage2-code-review.md verbatim, ticket + full comment
thread + parent (for sub-tasks) as input. Raw outputs: session scratchpad eval/outputs/.

| Ticket | Type/Summary (short) | Verdict | Qs | Adjudication |
|---|---|---|---|---|
| FR-2500 | Blocking call to run a flow times out | needs_info | 5 | agree - Comment confirms new wait-time query param decided with Mark - real API change |
| FR-3364 | Block Data and Variables tabs are hidden | not_candidate | 0 | agree - Layout regression fix |
| FR-3217 | Emails from FlowRunner | needs_info | 5 | agree - New failure notification + email; questions include how to reproduce for screenshots |
| FR-3250 | Way for customers to manage their subscriptions  | ready | 0 | agree - Stripe portal button; READY brief includes tooltip text, config source, verification steps |
| FR-3241 | Block "Reference Result Data As" should be moved | not_candidate | 0 | agree - Internal clientMetadata->metaInfo refactor; NOT fooled by doc-relevant parent spec |
| FR-999 | "Send with Template" mess | needs_info | 6 | POLICY CALL - Marketplace method changes - docs currently have no per-integration reference; scope decision needed |
| FR-1155 | Dynamic options for Facebook Ads | needs_info | 5 | POLICY CALL - Empty ticket, marketplace integration; uncertainty rule fired as designed, same scope decision |
| FR-3336 | File Reader tool does not work properly | needs_info | 6 | agree - File Reader behavior + provider file-type support matrix |
| FR-3342 | "Get execution status" and "get block results" e | ready | 0 | agree - API path change; READY brief is spec-level (endpoints, error codes, breaking old path) |
| FR-3283 | [SERVER] Add support for API_KEY placeholder dat | needs_info | 5 | agree - API Key placeholder server side; correct via parent context |
| FR-3264 | Add the new "API Key" data type in the Flow Plac | needs_info | 5 | agree - API Key placeholder type - clear candidate |
| FR-3345 | Server does not validate HTTP Request in AI Agen | not_candidate | 0 | agree - resultType:null save-rejection fix, restores intended behavior |
| FR-3332 | Block is not resolved when using copy/paste from | needs_info | 4 | agree - New unresolved-references popup on cross-flow paste |
| FR-3333 | Failed to send workspace notification. Invalid o | not_candidate | 0 | agree - Transient deploy desync, no code change - read from comment |
| FR-3346 | Open Code Editor must be enabled when flow is LI | needs_info | 6 | agree - Code editor read-only when LIVE; screenshot-only description, questions target exactly the gap |
| FR-3311 | Add new NotificationType when a flow fails (stat | needs_info | 5 | agree - New FLOW_INSTANCE_TERMINATED notification + email |
| FR-3353 | AI Question in condition is broken | not_candidate | 0 | agree - aiQuestion operator restore |
| FR-3340 | Folders & Files tab displays incorrect folder na | not_candidate | 0 | agree - Closed without fix; feature deprecated - read from comments |
| FR-3339 | Ensure that AI Agent tool configs are properly v | needs_info | 5 | agree - AI Agent tool config validation relaxation - borderline but user-facing |
| FR-3338 | Failed to Load Knowledge Base List with In-Memor | not_candidate | 0 | agree - KB list load fix |
| FR-3337 | Most basic flow fails with 500 | needs_info | 3 | agree - Current-date-without-type now returns ISO instead of 500 + console default - documentable behavior |
| FR-3335 | Assign Instance Name added as an AI Agent tool i | needs_info | 4 | agree - Assign Instance Name as agent tool + error text rename - borderline but user-facing |
| FR-3331 | Left toolbar improvements | not_candidate | 0 | agree - Toolbar polish/chrome - matches teach-value-not-narrate philosophy |
| FR-3330 | Input field in Create Object operation is not us | not_candidate | 0 | agree - Cosmetic input-field layout fix |
| FR-3324 | Console blows up when selecting a value in new E | not_candidate | 0 | agree - Crash fix |
| FR-3323 | Dictionary fields stopped showing user-friendly  | not_candidate | 0 | agree - Regression restore (dictionary friendly names) |
| FR-3322 | Make the "shared services" github repo private | not_candidate | 0 | agree - Repo made private - internal |
| FR-3320 | The error message mentions the name “Backendless | not_candidate | 0 | agree - Error-message brand rename; not doc content (rebrand sweep is a separate effort) |
| FR-3316 | Remove "InMemory" KnowledgeBase adapter | needs_info | 6 | agree - Empty ticket, feature removal that may touch KB guide; escalation is the designed behavior |
| FR-3314 | Text size changes on the Instances tab | not_candidate | 0 | agree - Cosmetic text-size fix |

## Scorecard

- Output validity: 30/30 parse, carry all fields, and follow every consistency rule
  (not_candidate => no comment/label; needs_info => questions present; [doc-triage]
  prefix on every comment; ready => brief present).
- Candidate calls: 16 flagged. 14 clearly correct; 2 (FR-999, FR-1155) hinge on an
  undecided policy - whether marketplace integration method catalogs are doc scope.
  Zero clear false positives.
- Non-candidate calls: 14/14 correct, including the traps: a sub-task with a
  doc-relevant parent spec (FR-3241), a ticket closed without a fix (FR-3340), a
  transient incident with no code change (FR-3333), and pure-cosmetic fixes.
- ready/needs_info calibration: the only two 'ready' verdicts (FR-3250, FR-3342) are
  exactly the two tickets whose thread carries a full spec. Both briefs are
  verification-oriented (what to exercise and confirm), not assertion-oriented.
- Thread comprehension: caught FR-3217's half-answered question ('answered only with
  yes'), FR-999's stale rename report, FR-2500's decision buried in a one-line comment.

## Caveat

Run through Claude Code subagents pinned to Opus, not the production claude-opus-5 API
call path - transferable, but re-spot-check after the flow is wired.
