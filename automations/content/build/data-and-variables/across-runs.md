# Sharing Data Across Runs & Flows

Every run starts with nothing. Variables are wiped when it ends, so a value written on Monday is gone by
Tuesday, and two runs happening at the same moment cannot see each other's data. That isolation is
deliberate. This page is for the times you need a value to cross it: when a value has to outlive
the run that produced it, or reach a different flow.

## Decide where the value should live

Work down this list and stop at the first one that fits:

- **Only this run needs it** - use a variable. See [Holding Values in Variables](holding-values.md).
- **Later runs of the same flow need it** - use Shared Memory, the flow's own key/value store. It holds
  what you put in it until you change or clear it.
- **Each customer, user, or session needs their own** - use Shared Memory with an anchor, so the flow keeps
  a separate store per caller rather than one shared by everybody.
- **Another flow needs it** - pass it. Shared Memory belongs to the flow that owns it, so data reaches a
  different flow by being handed over: send it in when you call that flow, and read what it returns. See
  [Running Another Flow](../integrations/running-another-flow.md).
- **It has to be queryable, permanent, or shared with systems outside FlowRunner** - put it in a real
  datastore and call that instead. Shared Memory is for flow state, not a database.

## What Shared Memory is good for

<!-- doclint: no-shot: names the three jobs and routes on; the Put and Read panels and the counter flow are pictured on the Shared Memory concept page -->

Three shapes cover most uses:

- **A counter that keeps counting across runs.** Read the current value with a default for the first run,
  add to it, write it back.
- **A cursor that marks where you got to.** Store the timestamp or id of the last record handled, then
  start the next run from there instead of reprocessing everything. This is what turns a scheduled flow
  into an incremental one.
- **Something expensive worth keeping.** A token, a fetched configuration, a computed lookup - written
  once and reused rather than fetched every run.

You write with [Shared Memory: Put](../../reference/shared-memory-put.md){.fr-block}, read with
[Shared Memory: Read](../../reference/shared-memory-read.md){.fr-block}, and remove with
[Shared Memory: Delete](../../reference/shared-memory-delete.md){.fr-block}.
[Shared Memory](../../learn/concepts/shared-memory.md) walks the counter pattern through end to end.

## Two settings to get right before you rely on it

<!-- doclint: no-shot: says which decisions matter and where they live; both dialogs are pictured on the Shared Memory concept page and walked through in Per-User Memory -->

Both live in the flow editor's right-hand panel, on its Flow Settings tab under Flow Memory:

- **The anchor.** By default a flow has one store shared by every run - right for a global counter, wrong
  for anything per-customer, where one caller would see another's data. Anchoring the store to something
  that identifies the caller keeps them separate. Setting it up, and deciding what happens when a caller
  arrives with no anchor value, is covered in
  [Per-User Memory](../../reference/per-user-memory-concept.md).
- **Expiration.** A store per caller is fine until you have a million stale ones. The expiration policy
  clears a store that has gone untouched for long enough, so short-lived sessions age out on their own.
  Keep it unlimited only for a value you genuinely mean to keep for the life of the flow.

## Related

- [Shared Memory](../../learn/concepts/shared-memory.md) - the store itself, writing and reading values, the
  counter pattern, anchoring, and expiration
- [Per-User Memory](../../reference/per-user-memory-concept.md) - a store per customer or session, end to end
- [Agent Memory](../../reference/flow-memory-concept.md) - what an AI agent remembers between runs
- [Running Another Flow](../integrations/running-another-flow.md) - handing data to a different flow
