<!-- GENERATED FILE - do not edit. Source: block-knowledge/list-iterator.yaml. Regenerate: make refgen -->
# List Iterator

Loop over the items of a list, running an inner sub-flow once per item.

## How it works

A "for each item" container. Build the per-item logic INSIDE it; the current item is exposed as the system value "Current Iteration Item".

## When to use it

Process each element of an array (bulk/batch operations).

## Configuration

| Field | Description |
| --- | --- |
| List | Required. The array to iterate (e.g. a prior block result property). |

## Behavior

- Runs the inner sub-flow once per list item; inner blocks see Current Iteration Item.
- In analytics each inner block shows an N/N execution-count badge (N = item count).
- Analytics 'Iteration #' stepper inspects per-iteration per-block Input/Output.
- Empty list -> body executes 0 times.

## Things to watch for

- Empty list -> inner sub-flow skipped entirely.
- Inner logic edited by stepping INTO the loop (hover -> Expand; RETURN top-left to exit).
- Stored as a groups[] entry (loopType LIST_ITERATOR), not a leaf element.
- Can't `return` from inside; capture results via [Set Variables](set-variables.md) / [Transform Data](transform-data.md).

## Related

- [Repeat](repeat.md)
- current-iteration-item
- instances-concept
- [Set Variables](set-variables.md)
