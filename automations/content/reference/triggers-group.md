<!-- GENERATED FILE - do not edit. Source: block-knowledge/triggers-group.yaml. Regenerate: make refgen -->
# Triggers Group

Pause the flow until trigger condition(s) are met across a group of triggers.

## How it works

A multi-trigger wait. Either "any one trigger fires" or "all triggers fire within a time window".

## When to use it

Coordinate multiple inbound events (wait for any one, or all within a timeframe).

## Configuration

| Field | Description |
| --- | --- |
| Outgoing Transition Mode | ONE_OCCUR (>=1 trigger fires) \| all triggers within a timeframe. |
| Occur Within / Time Unit | Timeframe for the "all triggers" mode. |

## Behavior

- Waits for triggers; proceeds when >=1 fires (ONE_OCCUR) or all fire within the window.

## Things to watch for

- All triggers in the group are equal/unordered.
- The 'all within timeframe' mode requires occurWithin + unit.
- No group-level return value; use individual trigger results.
- Stored as a groups[] entry (type TRIGGERS).

## Related

- [Actions Group](actions-group.md)
- [External Callback](external-callback.md)
