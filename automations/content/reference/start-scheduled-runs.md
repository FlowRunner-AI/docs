<!-- GENERATED FILE - do not edit. Source: block-knowledge/start-scheduled-runs.yaml. Regenerate: make refgen -->
# Start Scheduled Runs

Resume scheduled instance creation for a flow that has a schedule — so the platform (re)starts creating instances on that flow's schedule.

## How it works

A switch that resumes a target flow's schedule. The schedule itself is defined separately on the target flow (Configure Flow Schedule); this block only resumes instance creation.

## When to use it

Programmatically turn scheduled processing back ON for a flow from within another flow (e.g. an operator flow that resumes/halts scheduled runs).

## Configuration

| Field | Description |
| --- | --- |
| Name | Block label on the canvas. |
| Flow | Required. The target flow whose scheduled runs to start. (BUG: currently lists ALL flows, not only flows that have a schedule — see known_bugs.) |

## Behavior

- Resumes scheduled instance creation for the selected flow by setting its schedule.enabled=true.
- The schedule must already exist; this block only flips the enabled flag (it does not define the schedule).

## Things to watch for

- The flow must already HAVE a schedule (Configure Flow Schedule); this block only resumes instance creation.
- Distinct from FLOW SCHEDULING (the clock-icon popup), which DEFINES the schedule. This block CONTROLS (resumes) it.
- No Skip Block toggle is exposed on this block family in the config panel.

## Related

- [Stop Scheduled Runs](stop-scheduled-runs.md)
- [Flow Scheduling (Configure Flow Schedule)](flow-scheduling-concept.md)
- [Call Flow](call-flow.md)
