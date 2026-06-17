<!-- GENERATED FILE - do not edit. Source: block-knowledge/stop-scheduled-runs.yaml. Regenerate: make refgen -->
# Stop Scheduled Runs

Halt scheduled instance creation for a flow that has a schedule — so the platform stops creating instances on that flow's schedule.

## How it works

The counterpart to [Start Scheduled Runs](start-scheduled-runs.md){.fr-block} — halts a target flow's scheduled instance creation (Start resumes it).

## When to use it

Programmatically turn scheduled processing OFF for a flow from within another flow (e.g. pause scheduled runs during maintenance, or halt once a condition is met).

## Configuration

| Field | Description |
| --- | --- |
| Name | Block label on the canvas. |
| Flow | Required. The target flow whose scheduled runs to stop. (BUG: currently lists ALL flows, not only flows that have a schedule — see known_bugs.) |

## Behavior

- Halts scheduled instance creation for the selected flow by setting its schedule.enabled=false.
- The schedule definition (frequency/dates/policies) is preserved; only the enabled flag changes.

## Things to watch for

- Halts instance creation (Start resumes it); pairs with <span class="fr-block">Start Scheduled Runs</span>.
- Distinct from FLOW SCHEDULING (the clock-icon popup), which DEFINES the schedule. This block CONTROLS (halts) it.
- Stop does NOT delete the schedule — it only sets schedule.enabled=false; the schedule object (frequency, dates, policies) is preserved, so Start can re-enable it. Verified via API on the Email Sender demo.
- No Skip Block toggle is exposed on this block family in the config panel.

## Related

- [Start Scheduled Runs](start-scheduled-runs.md)
- [Flow Scheduling (Configure Flow Schedule)](flow-scheduling-concept.md)
- [Call Flow](call-flow.md)
