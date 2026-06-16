<!-- GENERATED FILE — do not edit. Source: block-knowledge/return-result.yaml. Regenerate: make refgen -->
# Return Result

Terminal block that defines the data a flow/subflow returns to its caller.
## How it works

A `return` statement for a flow. Composes the result object the caller receives.
## When to use it

End a SubFlow or a flow invoked via Call Flow, structuring the output for the caller.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Content Type | dropdown |  | Output format of the composed result. |
| Compose Result | repeatable Property+Value |  | The result's properties (names + expression values). |
## Behavior

- Marks the end of a branch and yields the composed result to the caller.
- Multiple Return Results in one flow -> a results[] array + first-reached result.
## Things to watch for

- Terminal — ends the execution branch.
- Single Return Result -> object; multiple -> { executionId, result(first-reached), results[], status }.
- Block name becomes blockName in the multiple-result structure.
## Related

- [Call Flow](call-flow.md)
- [SubFlow](subflow.md)
