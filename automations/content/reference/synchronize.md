<!-- GENERATED FILE — do not edit. Source: block-knowledge/synchronize.yaml. Regenerate: make refgen -->
# Synchronize

Merge multiple parallel execution branches back into one path; wait for all to arrive.
## How it works

A barrier / join. All incoming branches must reach it (or the timeout fires) before the single downstream path proceeds.
## When to use it

After fanning out into concurrent branches (e.g. several Call Flows / Actions Group), converge before continuing.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Max Waiting Time | simple (D/H/M/S) or expression (seconds) |  | How long to wait for all branches before proceeding anyway. |
## Behavior

- Waits for ALL incoming parallel branches, then continues down its single successor.
- If Max Waiting Time elapses first, continues anyway; late-arriving branches dropped.
## Things to watch for

- On timeout, execution continues even if not all branches arrived; late branches are dropped.
- Pair with parallel fan-out (multiple predecessors).
## Related

- [Actions Group](actions-group.md)
- [Call Flow](call-flow.md)
