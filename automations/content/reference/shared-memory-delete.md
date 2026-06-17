<!-- GENERATED FILE - do not edit. Source: block-knowledge/shared-memory-delete.yaml. Regenerate: make refgen -->
# Shared Memory: Delete

This block removes values from Shared Memory. You name the keys you want gone, and the block erases them from the store.

## How it works

Shared Memory is a key/value store that belongs to the flow and holds onto what you save in it between runs. This block reaches into that store and removes entries. You work it one of two ways. With **All** off you list the specific keys to remove, and only those are erased while everything else in the store stays put. With **All** on the block clears the entire store - every key the flow has ever saved - in one step. A key that was never written is harmless to name: the block simply has nothing to remove for it.

## When to use it

Reach for it when persisted state has done its job and should not carry into the next run. A cursor that marks how far a flow got last time, a counter you want to reset to its starting point, a one-time token you no longer need - removing the key makes the next run start clean, because a later read of a missing key falls back to its default. Naming the keys keeps the rest of the store intact, which is the careful choice; clearing everything with **All** is the blunt reset for when you want the flow to forget all of its memory at once.

## Example

Suppose a flow walks through a large list of records a batch at a time, and after each run it saves where it stopped in Shared Memory under the key `cursor`, so the next run picks up where the last one left off. A [Shared Memory: Read](shared-memory-read.md){.fr-block} block at the top reads `cursor` to find the starting point, and a [Shared Memory: Put](shared-memory-put.md){.fr-block} block at the end saves the new position.

Now say the flow finishes the very last batch - there is nothing left to process. You want the next run to start over from the beginning rather than resume past the end of the list. Drop a <span class="fr-block">Shared Memory: Delete</span> block on the path that runs when the work is done. Leave **All** off and name the single key to remove:

```text
All: off
Keys: cursor
```

When that path runs, the block erases `cursor` from Shared Memory and leaves any other saved keys untouched. On the next run, the <span class="fr-block">Shared Memory: Read</span> block looks up `cursor`, finds nothing stored, and returns its **Default Value** instead - so the flow starts fresh from the top of the list, exactly as it did the first time.

## Configuration

| Field | Description |
| --- | --- |
| All | When on, the block clears the entire Shared Memory store, removing every key. When off, you list the specific keys to remove and only those are erased. |
| Keys | The keys to remove when All is off. Name at least one. Listing a key that was never written does no harm - the block has nothing to remove for it. |

## Things to watch for

- With All on, the block clears the whole store - every key the flow has ever saved, not just the one you had in mind. Use it only when you mean to wipe all of the flow's memory; to remove a single value, leave All off and name the key.
- With All off you have to name at least one key, otherwise the block has nothing to remove.
- Removing a key does not break a later read of it. A <span class="fr-block">Shared Memory: Read</span> of a key that is gone returns that read's Default Value, the same as if the key had never been written.

## Related

- [Shared Memory: Read](shared-memory-read.md)
- [Shared Memory: Put](shared-memory-put.md)
