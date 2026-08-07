# Data & Variables

<!-- Section index / map. Conceptual intro + a reader-question map + cross-routes. No screenshots:
this page operates no controls; every technique is taught (and verified) on its child page.
Depth ceiling: name the job + route to the page that does it; no block config on this page. -->

Data moves through a flow as it runs. A run starts with something - a form submission, an API payload, a
record - and each step adds to what the run knows, so later steps can act on what earlier ones produced.
Getting a value from where it is to where it is needed, in the shape the next step expects, is what this
section is about.

It is one part of building a flow. Deciding the path a run takes is
[Flow Control](../flow-control/index.md); giving an agent its instructions and the tools it can reach for
is [AI in Flows](../ai-in-flows.md); calling other systems and handing work to other flows is
[Integrations & I/O](../integrations/index.md).

Find the page below that matches what you are trying to do.

## Use one step's output in a later step

The everyday case: a block ran, it produced something, and a step further down needs it. You point the
later step at the earlier one's result and pick out the piece you want. See
[Passing Data Between Blocks](passing-data.md).

## Keep a value for later in the run

When a value has to outlive the block that produced it - a running total, a flag you set early and check
late, a message you assemble in pieces - you hold it in a named variable that the rest of the run can read
and update. See [Holding Values in Variables](holding-values.md).

## Change data into the shape a step needs

Data does not always arrive in the shape the next step wants. A date needs reformatting, a list needs
filtering or sorting, a set of numbers needs totalling, two values need merging into one object. See
[Reshaping Data](reshaping-data.md).

## Carry data beyond a single run

Every run starts fresh, so a value written in one run is gone by the next. When state has to survive - a
running count across runs, a cursor marking how far you got, a token to reuse - or be shared with another
flow, you need a store that outlives the run. See [Sharing Data Across Runs & Flows](across-runs.md).

## Related, outside Data & Variables

<!-- doclint: no-shot: cross-route link list, not a scenario; each destination shows its own screens -->

- [Variables & Data Buckets](../../learn/concepts/variables.md) - what a variable is, and how a Data
  Bucket groups them.
- [Expression Editor](../../learn/concepts/expressions.md) - the dialog where you build a value from
  references, operators, and fixed text.
- [Blocks](../../learn/concepts/blocks.md) - how a block's result becomes readable by the steps after it.
- [Shared Memory](../../learn/concepts/shared-memory.md) - the flow's own store, kept between runs.
