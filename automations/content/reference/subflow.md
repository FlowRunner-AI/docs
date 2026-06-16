<!-- GENERATED FILE - do not edit. Source: block-knowledge/subflow.yaml. Regenerate: make refgen -->
# SubFlow

Place a reusable block-sequence (defined once) into a flow; runs as a self-contained unit.

## How it works

An inline reusable component referenced by subFlowId. Unlike [Call Flow](call-flow.md) (which invokes a separate top-level flow), a SubFlow is reuse WITHIN flows.

## When to use it

Avoid duplicating the same logic across a flow; encapsulate a reusable step.

## Configuration

| Field | Description |
| --- | --- |
| SubFlow (subFlowId / subFlowVersionId) | Required. The reusable subflow definition to run. |
| Input Parameter Names / Initial Params | Values passed into the subflow. |

## Behavior

- Runs the referenced subflow with the passed params; captures its [Return Result](return-result.md).
- Edited/inspected by stepping into it (Expand).

## Things to watch for

- SubFlows cannot be nested (no SubFlow inside a SubFlow).
- Pairs with Return Result to produce output.
- Stored as a groups[] entry (type SUBFLOW).

## Related

- [Call Flow](call-flow.md)
- [Return Result](return-result.md)
