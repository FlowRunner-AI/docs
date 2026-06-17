<!-- GENERATED FILE - do not edit. Source: block-knowledge/subflow.yaml. Regenerate: make refgen -->
# SubFlow

Place a reusable block-sequence (defined once) into a flow; runs as a self-contained unit.

## How it works

An inline reusable component referenced by subFlowId. Unlike [Call Flow](call-flow.md){.fr-block} (which invokes a separate top-level flow), a <span class="fr-block">SubFlow</span> is reuse WITHIN flows.

## When to use it

Avoid duplicating the same logic across a flow; encapsulate a reusable step.

## Configuration

| Field | Description |
| --- | --- |
| <span class="fr-block">SubFlow</span> (subFlowId / subFlowVersionId) | Required. The reusable subflow definition to run. |
| Input Parameter Names / Initial Params | Values passed into the subflow. |

## Behavior

- Runs the referenced subflow with the passed params; captures its [Return Result](return-result.md){.fr-block}.
- Edited/inspected by stepping into it (Expand).

## Things to watch for

- SubFlows cannot be nested (no <span class="fr-block">SubFlow</span> inside a <span class="fr-block">SubFlow</span>).
- Pairs with <span class="fr-block">Return Result</span> to produce output.
- Stored as a groups[] entry (type SUBFLOW).

## Related

- [Call Flow](call-flow.md)
- [Return Result](return-result.md)
