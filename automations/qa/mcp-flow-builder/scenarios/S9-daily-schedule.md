# S9 — Daily Ping (flow schedule via set_flow_schedule)

Driven 2026-09-02 03:00–03:03 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Every day at 08:00 ping https://httpbin.org/get."

## Build
create_flow → add_block http-request "Ping" (GET) → save_flow READY → set_flow_schedule(daily, everyDays 1, startDate 2026-09-03T08:00:00Z,
enabled) → get_flow_schedule. Flow 5A0025CD-1825-4D4F-B076-8D0191243A82, version 07310859-7242-4CC7-8FD8-ECADA37D0021.

## Oracles
- **O1:** metaInfo.schedule = {enabled true, frequency {schedule daily, repeat.every 1}, startDate 1788422400000 (= 2026-09-03T08:00Z),
  endDate null, both policy flags false}. Identical to get_flow_schedule. PASS.
- **O2:** S9-o2-schedule-dialog.png — Console "Configure Flow Schedule" dialog shows Frequency Daily, Repeat every 1 days, Expire Never. PASS.
- **O3:** not waited for (fires 2026-09-03 08:00 UTC only if the flow is LIVE; left READY and schedule disabled at teardown).

## Findings
1. F-S9-1 weekDays [0,9] accepted and persisted (`repeat.on: [0,9]`) — no range validation client- or server-side. Candidate subtask.
2. F-S9-3 set_flow_schedule works before any save_flow (the description says save is required) — harmless, but the text is inaccurate.
3. Gap: Console offers Monthly and Cron frequencies; the MCP offers once/custom/daily/weekly only (monthly acknowledged in the readme, cron
   not mentioned). An agent asked for "first Monday of the month" or a cron expression has no path.
4. F-S9-2 required-field errors are clear and correct.

## Teardown
set_flow_schedule(enabled:false, versionId explicit). Flow kept for end-of-phase deletion.

## Addendum (03:19 UTC)
Teardown call `set_flow_schedule({schedule:"daily", enabled:false})` without startDate reset startDate to now+30 s (tool default) — an agent
that only wants to toggle `enabled` must resend startDate or it is silently replaced. Worth a note in the tool description.
