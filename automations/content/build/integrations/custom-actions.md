# Custom & Marketplace Actions

The blocks built into FlowRunner cover a lot, but no built-in set covers everything. When the step you
need does not exist, you do not have to fall back to hand-built API calls for the rest of the flow's life -
you can add to the blocks available to you. Check what is already there first, then work down the ways to
add something, because the first that fits is nearly always the least work.

## First, check what already exists

<!-- doclint: no-shot: an ordering of the options, not a screen; the built-in categories are pictured on the Blocks concept page -->

A large library of **Extensions** ships with FlowRunner - blocks for outside services like Acumatica,
Airtable, Apollo, Asana, Slack, Stripe, and many more - with nothing to install. Beyond those, a
**Marketplace** offers pre-built actions you can install into your workspace. Before building anything,
check whether the capability you need is already covered. See [Blocks](../../learn/concepts/blocks.md).

## Add a service's tools with an MCP server
<!-- doclint: no-shot: routes to the MCP Servers page, which pictures registration, the tools, and attaching them to an agent -->

If the service publishes tools through the Model Context Protocol, registering its server once brings its
whole catalog in. Those tools then appear as blocks you drop into a flow, and they are simultaneously
available to your [AI Agent](../../reference/ai-agent.md){.fr-block} blocks as tools an agent can call on
its own. Nothing to build, nothing to host.

This is often the fastest route to a capability that has no built-in block. See
[MCP Servers](../../platform/mcp-servers.md).

## Turn your own flows into blocks

Work you have already built as a flow appears as a block under **Flows as Actions**, ready to place in
other flows, so a routine becomes a reusable step without writing anything new. This is the cheapest kind
of extension because you get it the moment the flow exists. See
[Running Another Flow](running-another-flow.md).

## Build your own action
<!-- doclint: no-shot: routes to the two build options, each pictured on its own page; the Custom Cloud Code screens are on its reference page -->

When nothing above fits - a proprietary system, a piece of logic that has to run as one unit - you can
package your own block as a [custom extension](../../extend/index.md). There are two ways to get one, and
they end in the same place: [let AI build it](../../extend/ai-assisted.md) from a description you write in
plain language, or [write it yourself](../../extend/getting-started.md). Neither requires the other.

For a one-off piece of code inside a single flow, nothing needs packaging at all - a
[Custom Cloud Code](../../reference/custom-cloud-code.md){.fr-block} block runs what you write, in place.

## Related

- [Blocks](../../learn/concepts/blocks.md) - the built-in categories and the extensions that ship with them
- [MCP Servers](../../platform/mcp-servers.md) - registering a server and attaching its tools to an agent
- [Calling an External Service](calling-a-service.md) - reaching a service that has no block of its own
- [Custom Cloud Code](../../reference/custom-cloud-code.md){.fr-block} - running your own code as a step
- [Custom Extensions](../../extend/index.md) - the two ways to build your own blocks, and how they deploy
