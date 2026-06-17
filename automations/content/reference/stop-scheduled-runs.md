<!-- GENERATED FILE - do not edit. Source: block-knowledge/stop-scheduled-runs.yaml. Regenerate: make refgen -->
# Stop Scheduled Runs

This block turns off the schedule on another flow, so the platform stops launching that flow on its set times. The flow's schedule itself stays defined - it is paused, not deleted.

## How it works

When a flow has a schedule, the platform starts a new run of it on a set rhythm - every 30 minutes, every night at 2am, and so on. This block reaches over to one of those flows, named in its Flow field, and switches that rhythm off. The schedule definition stays in place untouched - its frequency, its start and end dates, its policies - so nothing is lost; only its on/off switch is flipped to off. No more runs of that flow are launched on the clock until something turns the schedule back on, which is what its counterpart [Start Scheduled Runs](start-scheduled-runs.md){.fr-block} does.

## When to use it

Reach for it when one flow needs to pause another flow's scheduled runs on its own, without a person opening that flow and toggling its schedule by hand. The common case is a quiet window: before a maintenance job runs, a flow stops the scheduled work that would collide with it, does the maintenance, then turns the schedule back on with <span class="fr-block">Start Scheduled Runs</span>. It also fits a condition-driven halt - stop a flow's scheduled runs the moment some limit is reached or an error rate climbs too high. Doing this from a flow is cleaner than relying on someone to remember to flip the switch at the right moment.

## Example

Suppose you have a flow called Email Sender that the platform runs on a schedule every 30 minutes to send a batch of queued emails. Tonight you need to migrate the email provider, and you do not want a scheduled batch firing in the middle of it. You build a short maintenance flow to handle the pause and resume around that work.

The maintenance flow opens with a <span class="fr-block">Stop Scheduled Runs</span> block. In its Flow field you pick Email Sender - the flow whose schedule you want to pause. When this flow runs, that one line is enough to switch Email Sender's schedule off, so no new batch is launched on the clock from this point on.

After it, a [Wait](wait.md){.fr-block} block holds for the length of the migration, and then a <span class="fr-block">Start Scheduled Runs</span> block - also pointed at Email Sender - turns the schedule back on. Laid out, the maintenance flow does three things in sequence:

```text
Stop Scheduled Runs   (Flow: Email Sender)   -> schedule paused
Wait                  (60 seconds)           -> migration window
Start Scheduled Runs  (Flow: Email Sender)   -> schedule resumed
```

The payoff: throughout the wait, Email Sender launches no scheduled batches, so the migration runs clean. Its schedule was never deleted - every detail of its every-30-minutes setup is still there - so the <span class="fr-block">Start Scheduled Runs</span> block at the end brings it straight back to life, and the next batch goes out on the regular rhythm.

## Configuration

| Field | Description |
| --- | --- |
| Flow | Required. The flow whose schedule you want to pause. Note - the dropdown currently lists every flow in the workspace, not only the ones that actually have a schedule, so pick the scheduled flow by name. |

## Things to watch for

- This block pauses a schedule; it does not delete one. The flow's schedule - its frequency, its dates, its policies - is left fully defined, just switched off. Its counterpart <span class="fr-block">Start Scheduled Runs</span> flips that same switch back on. To remove a schedule outright, you use the flow scheduling popup instead, not this block.
- Picking a flow that has no schedule has nothing to switch off. Make sure the flow you choose actually runs on a schedule, especially since the Flow dropdown currently lists unscheduled flows too.
- This block acts on the target flow's real schedule on the platform. When you are testing, point it at a throwaway flow rather than a production one, so you do not pause scheduled work that other people depend on.

## Related

- [Start Scheduled Runs](start-scheduled-runs.md)
- [Flow Scheduling (Configure Flow Schedule)](flow-scheduling-concept.md)
- [Call Flow](call-flow.md)
