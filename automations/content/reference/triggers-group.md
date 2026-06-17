<!-- GENERATED FILE - do not edit. Source: block-knowledge/triggers-group.yaml. Regenerate: make refgen -->
# Triggers Group

This block holds several triggers together and waits for inbound events to arrive at them. It lets the flow continue when any one of those triggers fires, or only once they have all fired within a time window you set.

## How it works

A <span class="fr-block">Triggers Group</span> is a block container for triggers. Instead of a single trigger starting the flow on its own, you place two or more triggers inside the group, and the group decides when the flow moves on based on which of them have fired. The triggers inside have no order and none is the "main" one - the group simply watches them all and waits.
How it waits is set by the **Outgoing Transition Mode**. In the "any one fires" mode the group lets the flow continue the moment the first of its triggers receives an event, and the rest are no longer waited on. In the "all fire within a window" mode the group continues only after every trigger inside it has fired, and only if they all do so inside the timeframe you set - you give that timeframe as a number plus a unit, such as 30 minutes. If the window passes before every trigger has fired, the all-fire condition is not met.

## When to use it

Reach for it when more than one inbound event could, or should, move your flow forward, and a single trigger cannot express that. The "any one fires" mode suits a race - you are waiting on whichever of several events shows up first, like an approval that might arrive by email or by a webhook, and you act on the first one. The "all fire within a window" mode suits a rendezvous - you need several events to have all happened close together before you proceed, like waiting for both a payment confirmation and a shipping confirmation within an hour. If only one event ever matters, a single trigger on its own is the simpler choice; the group earns its place once the decision spans several triggers at once.

## Example

Suppose a run pauses partway through and should resume as soon as approval comes in, but approval might arrive two different ways - a manager clicking a link in an email, or an upstream system posting to a webhook. Put two [External Callback](external-callback.md){.fr-block} triggers inside a <span class="fr-block">Triggers Group</span>: one whose Callback URL the email link points at, and one whose Callback URL the upstream system posts to.

Set the group's Outgoing Transition Mode to the "any one fires" mode. Now whichever event arrives first - the click or the post - releases the flow, and the second is no longer waited on. The flow continues without you having to wire up branching logic to watch both paths yourself, and without caring which channel the approval came through.

## Configuration

| Field | Description |
| --- | --- |
| Outgoing Transition Mode | Required. How the group decides to continue. One choice continues as soon as any single trigger inside it fires; the other continues only after every trigger has fired within the time window you set below. |
| Occur Within / Time Unit | The length of the time window for the "all fire" mode, given as a number and a unit (for example 30 and Minutes). Every trigger must fire inside this window for the group to continue. It does not apply to the "any one fires" mode. |

## Things to watch for

- The triggers in the group have no order and no priority - the group reacts to whichever of them fire, not to a particular one.
- If you choose the 'all fire within a window' mode, you have to set a time window. Without one there is no defined period for the triggers to all fire inside.
- The group itself does not produce a combined result for later steps to read. Each trigger inside it still exposes its own data under its own alias, so read those individually.

## Related

- [Actions Group](actions-group.md)
- [External Callback](external-callback.md)
