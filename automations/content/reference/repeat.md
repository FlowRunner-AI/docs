<!-- GENERATED FILE - do not edit. Source: block-knowledge/repeat.yaml. Regenerate: make refgen -->
# Repeat

Repeat an inner sub-flow while a condition holds (with a failsafe iteration cap).

## How it works

A while-loop container. Runs the body, re-checks the condition; stops when false or when maxIterations (failsafe) is hit.

## When to use it

Loop an unknown number of times until a condition becomes false (polling, retries, accumulation) — when you don't have a fixed list (use [List Iterator](list-iterator.md) for lists).

## Configuration

| Field | Description |
| --- | --- |
| [Condition](condition.md) | Required. Loop continues while true (re-evaluated each iteration). |
| Max Iterations (failsafe) | Hard cap to prevent infinite loops. |

## Behavior

- Evaluates condition each iteration; runs body while true (product calls it a 'Repeat While' loop).
- Stops at first false condition OR at maxIterations (failsafe).

## Things to watch for

- Current Iteration Number starts at 0.
- Always set a sane failsafe (default 10000) during development.
- Requires inner blocks (double-click to edit the loop body).
- Stored as a groups[] entry (loopType REPEAT). Contrast List Iterator (uses `list`).

## Related

- [List Iterator](list-iterator.md)
- [Condition](condition.md)
- [Set Variables](set-variables.md)
