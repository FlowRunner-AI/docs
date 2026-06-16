<!-- GENERATED FILE — do not edit. Source: block-knowledge/transform-data.yaml. Regenerate: make refgen -->
# Transform Data

Apply a chosen data-transformation operation (from a large library) to reshape/derive data.
## How it works

A no-code "data function": pick an operation, give it inputs, get a result. (For anything beyond the library, use Custom Cloud Code.)
## When to use it

Extract/restructure values between blocks without writing code: get a property, pick/omit keys, build/merge/sort/filter arrays, date/math/text/logic ops.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Operation | dropdown (50+ ops) | Yes | e.g. Get Property Value, Pick/Omit, Create/Merge/Sort/Filter Array, If/Equals/Switch, date/math/text ops. |
| (operation-specific args) | varies |  | Inputs depend on the chosen operation (e.g. Object + Property Name). |
| Reference Result Data As | alias |  |  |
| Assign to a Variable | optional |  | Also write the result to a Data-Bucket variable. |
## Behavior

- Evaluates the selected operation over its inputs and returns the result.
- Optionally also assigns the result to a Data-Bucket variable.
## Things to watch for

- Operation is required; each operation has its own argument set.
- Has Assign to a Variable in addition to the result alias.
## Related

- [Set Variables](set-variables.md)
- [Custom Cloud Code](custom-cloud-code.md)
- expression-editor
