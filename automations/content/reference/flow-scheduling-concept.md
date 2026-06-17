<!-- GENERATED FILE - do not edit. Source: block-knowledge/flow-scheduling-concept.yaml. Regenerate: make refgen -->
# Flow Scheduling (Configure Flow Schedule)

Flow scheduling starts a flow on its own, on a timetable you set, so it runs without anyone or anything kicking it off. You set it up in the Configure Flow Schedule popup.

## How it works

A schedule is a timetable you attach to one version of a flow. You give it a start time, a frequency, and an end (or no end), and from then on FlowRunner starts a fresh run of that flow every time the timetable comes due - each run is a new Instance with its own data, exactly as if a trigger had fired it. You open the popup from the clock icon in the flow editor's top toolbar, or from the Flow Schedule card on the Version Admin tab. Frequency is where you pick the cadence: a single run at the start time, every few seconds, daily, weekly, monthly, or a Cron expression for a custom timetable. Expire sets when the timetable stops - leave it on Never for no end, or set an end date.
There are two separate ideas here, and keeping them apart saves a lot of confusion. One is the schedule's DEFINITION - the start, frequency, and end you typed into this popup. The other is whether that schedule is currently switched on and producing runs. This popup defines the schedule; the [Start Scheduled Runs](start-scheduled-runs.md){.fr-block} and [Stop Scheduled Runs](stop-scheduled-runs.md){.fr-block} blocks switch it on and off from inside a flow, without changing the definition you set here.

## When to use it

Reach for a schedule whenever a flow should start itself on a timetable rather than waiting for a trigger, an API call, or a manual launch - a nightly cleanup job, a poll that checks a source every few minutes, a weekly report, a recurring batch of emails. The trade-off to weigh is control: a schedule starts runs on the clock whether or not there is anything to do, so for work that should start in response to an event (a record changed, a request came in) a trigger fits better. Pick a schedule when the timing itself is the thing that should drive the flow.

## Behavior

- While the schedule is switched on and the current time falls between its start and its expiry, FlowRunner starts a new run of the flow each time the timetable comes due.
- The <span class="fr-block">Start Scheduled Runs</span> and <span class="fr-block">Stop Scheduled Runs</span> blocks turn the timetable on and off without changing the start, frequency, or expiry you set in the popup.

## Things to watch for

- A schedule belongs to one version of the flow, not to the flow as a whole. If you publish a new version, check that the version meant to run on the timetable is the one carrying the schedule.
- Defining a schedule here is not the same as switching it on. This popup sets the timetable; the <span class="fr-block">Start Scheduled Runs</span> and <span class="fr-block">Stop Scheduled Runs</span> blocks turn that timetable on and off from inside a flow. Stopping it pauses the runs but keeps the timetable you set.
- REMOVE SCHEDULING and <span class="fr-block">Stop Scheduled Runs</span> are not the same thing. REMOVE SCHEDULING deletes the timetable outright, so there is nothing left to restart - you would have to set it up again. <span class="fr-block">Stop Scheduled Runs</span> only pauses an existing timetable, and a later <span class="fr-block">Start Scheduled Runs</span> picks it back up unchanged.
- Allow only scheduled flow instances changes how triggers behave. With it on, only the schedule creates new runs - a trigger no longer starts a fresh run on its own. If the flow begins with a trigger, a scheduled run has to already be going for that trigger to be accepted, which is different from the usual behavior where the first trigger starts a new run.
- Allow flow instantiation via API when the schedule expires is what lets the [Call Flow](call-flow.md){.fr-block} API still start a run after the timetable's end date has passed. Without it, an expired schedule means no new runs from that path either.

## Related

- [Start Scheduled Runs](start-scheduled-runs.md)
- [Stop Scheduled Runs](stop-scheduled-runs.md)
- [Call Flow](call-flow.md)
- [Triggers Group](triggers-group.md)
