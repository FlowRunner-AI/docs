<!-- GENERATED FILE — do not edit. Source: block-knowledge/value-router.yaml. Regenerate: make refgen -->
# Value Router

Route the flow to a named branch by matching one input value against each branch's configured value(s). Deterministic (vs AI Router).
## How it works

A switch/case. Evaluate one value; first branch whose value(s) match wins; else "Everything Else".
## When to use it

Dispatch on a known value (product type, status code, category) into N paths.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Value to Evaluate | expression | Yes | The single value to match (e.g. Initial Data.ira_product_type). |
| Branch Name | string (repeatable branch) |  | Label = the output connector name. |
| Value Mode | dropdown |  | Single Value \| Collection (OR) \| Range (inclusive). |
| (branch value / values / range) | expression |  | What the branch matches. |
| Everything Else | built-in default branch |  | Taken when no branch matches. |
## Behavior

- Matches Value to Evaluate against each branch's value(s); first match routes there.
- No match -> Everything Else branch.
## Things to watch for

- Branches evaluated in order; first match wins.
- Collection mode uses OR; Range is inclusive.
- Everything Else is always present.
## Related

- [AI Router](ai-router.md)
- [Condition](condition.md)
