<!-- GENERATED FILE - do not edit. Source: block-knowledge/external-callback.yaml. Regenerate: make refgen -->
# External Callback

Start or resume a flow when an external system calls the trigger's unique Callback URL.

## How it works

An inbound webhook. The caller's payload becomes the trigger data; fires only when the flow is LIVE.

## When to use it

Webhook-style entry: let an external system invoke the flow (flow-start) or resume a waiting instance (mid-flow).

## Configuration

| Field | Description |
| --- | --- |
| Callback URL | Unique URL embedding workspace/api-key/flow/trigger ids; external systems POST/GET to it. |
| Add a [Condition](condition.md) | Govern WHEN the trigger should fire (false condition -> trigger doesn't fire). |
| Reference Trigger Data As | Alias for the inbound payload (the trigger has no "result"). |
| Execution parameter | specific ID \| any \| all (which waiting instance(s) to target for mid-flow resume). |

## Behavior

- On an inbound call (flow LIVE), creates/resumes an instance with the payload as External Callback Data.
- A false trigger condition prevents firing.

## Things to watch for

- Fires only when the flow is LIVE.
- Flow-start trigger creates a new instance; mid-flow trigger resumes a paused instance.
- Learning Mode (phone icon) captures the event shape at design time (no LIVE needed).
- Open: whether an instance is created when a condition evaluates false (TODO confirm).

## Related

- [Triggers Group](triggers-group.md)
- conditions-concept
- learning-mode
- instances-concept
