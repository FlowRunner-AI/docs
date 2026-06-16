<!-- GENERATED FILE — do not edit. Source: block-knowledge/set-variables.yaml. Regenerate: make refgen -->
# Set Variables

Create or update one or more variables, grouped into a named Data Bucket.
## How it works

Assign variables into a labeled namespace (the Data Bucket). Referenced downstream as "<Bucket> - <name>" in the Expression Editor's Variables tab.
## When to use it

Hold/compute values for use by later blocks (flags, counters, derived values).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Data Bucket | editable dropdown |  | Namespace for the variables; type a new name to create one. |
| Perform Changes | repeatable Name+Value |  | Each variable's name + value (literal or expression). |
## Behavior

- Writes each Name=Value into the chosen Data Bucket for this instance.
- Values can be literals or expressions (incl. referencing the variable itself).
## Things to watch for

- No result alias — output is the variables, not a block result.
- Variables are per-instance; for cross-instance persistence use Shared Memory.
- Referenced as '<Bucket> - <name>' pills.
## Related

- [Shared Memory: Read](shared-memory-read.md)
- [Transform Data](transform-data.md)
- expression-editor
