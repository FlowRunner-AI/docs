<!-- GENERATED FILE — do not edit. Source: block-knowledge/wait.yaml. Regenerate: make refgen -->
# Wait

Pause flow execution for a specified duration.
## How it works

A sleep(n). Simple mode (D/H/M/S) or Advanced (expression -> seconds).
## When to use it

Delay subsequent steps: backoff before a retry, rate-limiting, scheduled-feeling delays.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Expression Mode | toggle |  | Off = simple Days/Hours/Minutes/Seconds; On = expression evaluating to seconds. |
| Days/Hours/Minutes/Seconds (delay) | numbers |  | The pause duration (at least one non-zero in simple mode). |
## Behavior

- Suspends the branch for `delay` seconds, then continues.
- Common pattern: Handle Error -> Wait (backoff) -> retry.
## Things to watch for

- Config field is `delay` (seconds when expression mode).
- Minimal block (no Skip/Logging/Test Panel in some builds).
## Related

- [Handle Error](handle-error.md)
- [Synchronize](synchronize.md)
