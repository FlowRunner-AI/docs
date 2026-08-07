# Retrieving Block Results

Reading back what the individual blocks of a run produced - not just the flow's final answer, but the input
and output of each step along the way - is new functionality.

!!! note "Not yet available"
    This is not released yet, so there is nothing to call. This page will be written once the feature ships
    to production.

Until then, block-by-block input and output is available inside FlowRunner rather than over the API:

- **While you are building**, the Test Monitor shows what each block took in and gave back as you run it.
  See [Testing](../run/testing.md).
- **After a run**, opening a run and selecting a block shows the same thing for a run that has already
  happened. See [Running Flows](../run/running-flows.md).

## Related

- [Call Flow](call-flow.md) - starting a run, and the `executionId` that identifies it
- [Activating an External Callback](activating-a-trigger.md) - letting a paused run continue
- [Testing](../run/testing.md) - reading block input and output while you build
