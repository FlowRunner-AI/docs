<!-- GENERATED FILE - do not edit. Source: block-knowledge/actions-group.yaml. Regenerate: make refgen -->
# Actions Group

Group multiple actions to run in PARALLEL, then continue based on a transition mode.

## How it works

A parallel block. Inner actions start together; the group transitions when they start (ON_START) or when they all complete (ON_COMPLETION).

## When to use it

Launch independent actions concurrently instead of sequentially (fan-out).

## Configuration

| Field | Description |
| --- | --- |
| Outgoing Transition Mode | ON_START (proceed when all started) \| ON_COMPLETION (proceed when all finished). |

## Behavior

- Contained actions execute concurrently.
- ON_COMPLETION: downstream proceeds only after all inner actions finish.
- ON_START: downstream proceeds once all inner actions have started.

## Things to watch for

- Inner actions run in parallel, not sequenced.
- ON_START may proceed before inner results are available.
- No group-level return value; use individual action results.
- Stored as a groups[] entry (type ACTIONS).

## Related

- [Triggers Group](triggers-group.md)
- [Synchronize](synchronize.md)
