<!-- GENERATED FILE - do not edit. Source: block-knowledge/handle-error.yaml. Regenerate: make refgen -->
# Handle Error

Catch a block's failure and route the flow to recovery logic instead of terminating.

## How it works

A try/catch target. You attach a Handle Error to a block (as its failure handler); if the block throws, control jumps to Handle Error, which exposes the error and continues down its own path.

## When to use it

Wrap any block that can fail (HTTP call, DB write, Cloud Code) so the flow can log, notify, retry, or fall back.

## Configuration

| Field | Description |
| --- | --- |
| Reference Result Data As | The caught error is exposed as this result (code/message/source). |

## Behavior

- When the guarded block fails, execution diverts to this block.
- Exposes the error (storeResult) and continues down its nextElementIds.
- Common pattern: Handle Error -> [Wait](wait.md) (backoff) -> retry the failed action.

## Things to watch for

- Minimal config — no Test Panel / Skip Block; it's a structural catch target.
- Attach it by connecting the failure-expecting block to it as a successor; that block keeps its normal success path and gains this failure path.
- Unhandled failures (no Handle Error) stop the flow.

## Related

- [Wait](wait.md)
- [Custom Cloud Code](custom-cloud-code.md)
- error-handling-concept
