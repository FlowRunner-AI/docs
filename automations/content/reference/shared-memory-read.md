<!-- GENERATED FILE — do not edit. Source: block-knowledge/shared-memory-read.yaml. Regenerate: make refgen -->
# Shared Memory: Read

Read one value from Shared Memory (the flow's persistent key/value store) by key.
## How it works

A get() from a flow-scoped persistent store. Returns a Default Value when the key doesn't exist yet.
## When to use it

Retrieve state that must persist ACROSS instances (counters, cursors, last-seen).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Key | expression | Yes | The shared-memory key to read. |
| Default Value | expression |  | Value used when the key does not exist yet (first run). — The return value if the value for the key has not yet been put |
| Reference Result Data As | alias |  |  |
| Assign to a Variable | optional (Data Bucket + Variable Name) |  | Also drop the read value into a local variable. |
## Behavior

- Returns the stored value for the key, or the Default Value if absent.
- Optionally assigns the value to a Data-Bucket variable.
## Things to watch for

- Shared Memory persists BETWEEN instances (unlike Set Variables / Data Buckets).
- First run (no key yet) -> output is empty/None; the Default Value flows to the assigned variable.
- Large values may be offloaded to S3 internally (impl detail).
## Related

- [Shared Memory: Put](shared-memory-put.md)
- [Shared Memory: Delete](shared-memory-delete.md)
- [Set Variables](set-variables.md)
- flow-memory-settings
