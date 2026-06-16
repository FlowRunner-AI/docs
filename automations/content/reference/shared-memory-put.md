<!-- GENERATED FILE — do not edit. Source: block-knowledge/shared-memory-put.yaml. Regenerate: make refgen -->
# Shared Memory: Put

Write one or more key/value pairs into Shared Memory (persists across instances).
## How it works

A set() into the flow-scoped persistent store.
## When to use it

Persist state for later instances (update a counter, store a cursor/token).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Override | toggle |  | Replace the existing stored value (on) vs (off) presumably merge/keep — confirm off behavior. |
| Perform Changes | repeatable Name+Value |  | Keys + values (expressions) to store. |
## Behavior

- Writes each key=value into Shared Memory; persists for future instances.
- Override on replaces existing value for the key.
## Things to watch for

- No result alias (produces no referenceable result).
- Override off-behavior not yet fully verified — confirm.
## Related

- [Shared Memory: Read](shared-memory-read.md)
- [Shared Memory: Delete](shared-memory-delete.md)
