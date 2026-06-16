<!-- GENERATED FILE — do not edit. Source: block-knowledge/call-flow.yaml. Regenerate: make refgen -->
# Call Flow

Invoke another (LIVE) flow from within this flow, passing data in and (optionally) waiting for its Return Result.
## How it works

A function call to another flow. Pass named params (Initial Data); syncCall=true waits and returns the callee's Return Result; async returns an executionId.
## When to use it

Compose flows: factor reusable logic into separate flows and orchestrate them.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Flow Name | dropdown (flowId) | Yes | The target flow (must be LIVE to be callable). |
| Initial Params | repeatable name+expression (initialDataParams) |  | Named values passed to the called flow's Initial Data. |
| Wait for Execution | toggle (syncCall) |  | true = wait + capture Return Result; false = fire-and-forget (returns executionId). |
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
