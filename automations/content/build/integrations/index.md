# Integrations & I/O

<!-- Section index / map. Conceptual intro + a reader-question map + cross-routes. No screenshots:
this page operates no controls; every technique is taught (and verified) on its child page.
Depth ceiling: name the job + route to the page that does it; no block config on this page. -->

Few flows are self-contained. A flow reaches out to the systems your business already runs on, hands work
to other flows, and returns an answer to whatever called it. This section covers a flow's edges: what it
calls out to, what it gives back, and how you add new blocks when the built-in ones do not cover what you
need.

Find the one that matches what you are trying to do.

## Call a service outside FlowRunner

When a step needs something only another system has - a customer record, a payment charge, a message
posted to a channel - the flow calls it. Many services are already blocks you configure and drop in;
anything with a web API you can call directly. See [Calling an External Service](calling-a-service.md).

## Give an answer back to the caller

When a flow is run by something that is waiting on it - an app, another flow, an agent using it as a tool -
it has to hand back a result, and you decide what that result contains. See
[Returning a Result](returning-a-result.md).

## Hand work to another flow

When a stretch of work is used in several places, or a flow has grown too big to read, you build it once
as its own flow and call it from the others. See [Running Another Flow](running-another-flow.md).

## Add blocks that are not built in

When nothing built in fits, you add to what is available: install a pre-built action from the Marketplace,
connect an MCP server whose tools become blocks, or package your own. See
[Custom & Marketplace Actions](custom-actions.md).

## Related, outside Integrations & I/O

<!-- doclint: no-shot: cross-route link list, not a scenario; each destination shows its own screens -->

- [MCP Servers](../../platform/mcp-servers.md) - register a server once and its tools become blocks in
  flows and tools for your agents.
- [OAuth Connections](../../platform/oauth-connections.md) - authorizing FlowRunner to act against an
  outside service on your behalf.
- [Triggers](../../learn/concepts/triggers.md) - the other direction: an outside system starting or
  resuming a flow.
- [Waiting on an External System](../flow-control/external-callbacks.md) - pausing a run until an outside
  system reports back.
- [About Custom Actions](../../extend/custom-actions.md) - building and publishing your own blocks.
