<!-- GENERATED FILE - do not edit. Source: block-knowledge/external-callback.yaml. Regenerate: make refgen -->
# External Callback

This trigger gives the flow its own web address, the Callback URL, and starts the flow when an outside system makes a request to that address. Whatever the caller sends becomes data your flow can read.

## How it works

The trigger hands you one unique Callback URL that points at this flow. When an outside system makes an HTTP request to that URL - a GET with query parameters, or a POST with a body - the trigger picks up the request, makes its contents available to the rest of the flow under the alias you choose (<span class="fr-block">External Callback</span> Data by default), and starts a run. It listens only while the flow is in the LIVE state; a request that arrives at any other time is not handled.
A trigger has no result of its own to compute - the data it exposes is the request that came in. Because it cannot run on demand the way an action block can, you teach it the shape of that data with Learning Mode: turn it on, send one real sample request to the Callback URL, and the trigger records the structure so you can point later steps at individual fields. Learning Mode works while you are still building, before the flow is LIVE.

## When to use it

Reach for it when something outside FlowRunner needs to kick off your flow - a payment provider announcing a charge, a form submission, another service posting an event. You give that system the Callback URL and it calls you, rather than you polling it. An Add a [Condition](condition.md){.fr-block} entry lets you gate the trigger so it fires only for the requests you care about, which keeps unrelated calls from starting runs. The same trigger can also resume a run that paused earlier and is waiting on a callback, so you can model a hand-off where your flow asks an outside system for something and continues once that system calls back.

## Example

Suppose a payment provider should kick off your flow every time a customer pays. In the provider's dashboard you paste this trigger's Callback URL as the webhook target. When a payment clears, the provider sends a POST to that URL with a JSON body like this:

```json
{
  "event": "payment.succeeded",
  "orderId": "ORD-4417",
  "amount": 4999,
  "currency": "USD",
  "customer": { "email": "dana@example.com" }
}
```

Before wiring anything up, you turn on Learning Mode and have the provider send one test payment to the Callback URL. The trigger records the structure above, so later steps can reference fields by name instead of guessing. The whole body is now available as <span class="fr-block">External Callback</span> Data, and a step reads the order number from `External Callback Data->orderId`.

The provider also sends other events to the same URL - refunds, disputes - that you do not want to act on here. Add a <span class="fr-block">Condition</span> that checks `External Callback Data->event` equals `"payment.succeeded"`, so a refund or dispute notification arrives but does not start a run.

Set the flow LIVE. Now each successful payment posts to the Callback URL, the condition passes, a new run begins with that payment as <span class="fr-block">External Callback</span> Data, and the steps after the trigger can read `External Callback Data->orderId` and `External Callback Data->amount` to record the sale.

## Configuration

| Field | Description |
| --- | --- |
| Callback URL | The flow's unique web address, generated for you with a copy button. Give this to the outside system so it can call your flow; the URL identifies the workspace and flow it belongs to. |
| Add a <span class="fr-block">Condition</span> | An optional gate on whether the trigger fires for a given request. If the condition is false for an incoming call, the trigger does not start a run for it. |
| Reference Trigger Data As | The name you use to read the incoming request elsewhere in the flow. A trigger has no computed result, so this alias points at the request that came in. |
| Execution parameter | Which waiting run to resume when this trigger is used to continue a paused run - a specific run by id, any one waiting run, or all of them. |

## Things to watch for

- The trigger listens only while the flow is in the LIVE state. A request that arrives when the flow is not LIVE is not handled and starts no run.
- Used at the start of a flow, the trigger begins a new run for each call. Used to continue a run that paused waiting on a callback, it resumes that existing run instead of starting a new one.
- Reference fields in the incoming request only after you have captured its shape with Learning Mode - otherwise there is nothing to point your expressions at. Learning Mode does not need the flow to be LIVE; it listens for one sample request while you build.
- When you turn Learning Mode on, the trigger waits for a real request to the Callback URL. Send that sample yourself with a test tool such as Postman, or have the integrating system send one; FlowRunner does not generate it for you.

## Related

- [Triggers Group](triggers-group.md)
- conditions-concept
- learning-mode
- instances-concept
