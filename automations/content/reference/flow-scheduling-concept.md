<!-- GENERATED FILE - do not edit. Source: block-knowledge/flow-scheduling-concept.yaml. Regenerate: make refgen -->
# Flow Scheduling (Configure Flow Schedule)

Run a flow automatically on a calendar/interval/cron schedule. Scheduling is configured PER FLOW VERSION via the "Configure Flow Schedule" popup.

## How it works

A schedule attached to a flow version. The platform creates a new flow instance each time the schedule fires. The schedule DEFINITION (frequency/dates/policies) is separate from whether it is currently RUNNING (schedule.enabled) — the Start/[Stop Scheduled Runs](stop-scheduled-runs.md){.fr-block} blocks only toggle that enabled flag.

## When to use it

Any time a flow should start itself on a timetable (polling, periodic jobs, recurring sends) rather than only via triggers or manual/API invocation.

## Behavior

- When enabled and within Start..Expire, the platform creates a flow instance each time the schedule fires.
- Start/<span class="fr-block">Stop Scheduled Runs</span> blocks toggle schedule.enabled without altering the definition.

## Things to watch for

- Scheduling is per FLOW VERSION (not per flow).
- DEFINE/REMOVE a schedule here; START/STOP whether it creates instances via the Start/<span class="fr-block">Stop Scheduled Runs</span> blocks (they flip schedule.enabled; the definition is preserved).
- REMOVE SCHEDULING deletes the schedule definition; <span class="fr-block">Stop Scheduled Runs</span> only pauses it.

## Related

- [Start Scheduled Runs](start-scheduled-runs.md)
- [Stop Scheduled Runs](stop-scheduled-runs.md)
- [Call Flow](call-flow.md)
- [Triggers Group](triggers-group.md)
