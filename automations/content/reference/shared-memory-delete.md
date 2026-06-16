<!-- GENERATED FILE - do not edit. Source: block-knowledge/shared-memory-delete.yaml. Regenerate: make refgen -->
# Shared Memory: Delete

Remove key(s) from Shared Memory.

## How it works

A delete()/clear() on the persistent store.

## When to use it

Reset/clear persisted state (e.g. clear a counter or all flow memory).

## Configuration

| Field | Description |
| --- | --- |
| Mode (All) | All on = delete ALL keys; off = specify individual Keys. |
| Keys | The specific keys to delete (when All is off). |

## Behavior

- Deletes the specified key(s), or all keys when Mode=All.

## Things to watch for

- All=on wipes the whole store; otherwise at least one key required.
- No result alias.

## Related

- [Shared Memory: Read](shared-memory-read.md)
- [Shared Memory: Put](shared-memory-put.md)
