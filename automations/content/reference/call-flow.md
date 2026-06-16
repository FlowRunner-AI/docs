<!-- GENERATED FILE - do not edit. Source: block-knowledge/call-flow.yaml. Regenerate: make refgen -->
# Call Flow

Invoke another (LIVE) flow from within this flow, passing data in and (optionally) waiting for its [Return Result](return-result.md).

## How it works

A function call to another flow. Pass named params (Initial Data); syncCall=true waits and returns the callee's Return Result; async returns an executionId.

## When to use it

Compose flows: factor reusable logic into separate flows and orchestrate them.

## Configuration

| Field | Description |
| --- | --- |
| Flow Name | Required. The target flow (must be LIVE to be callable). |
| Initial Params | Named values passed to the called flow's Initial Data. |
| [Wait](wait.md) for Execution | true = wait + capture Return Result; false = fire-and-forget (returns executionId). |

## Behavior

- Starts an instance of the target flow with the mapped Initial Data params.
- syncCall=true: blocks until the callee finishes, captures its Return Result.
- syncCall=false: returns immediately with the executionId.

## Things to watch for

- Only LIVE flows can be called.
- Sync vs async changes the return (Return Result vs executionId).

## Related

- [SubFlow](subflow.md)
- [Return Result](return-result.md)
- [Synchronize](synchronize.md)
- initial-data-concept
