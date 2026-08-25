<!-- GENERATED FILE - do not edit. Source: block-knowledge/return-result.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Return Result -->
# Return Result

This block lets you decide exactly what a caller sees back from a flow. You name the properties to return and give each a value, and the caller reads back only that object - the id, the token, the status you chose to expose - while everything the flow did to produce it stays hidden inside.

## How it works

A flow can do a lot of work, but a caller does not need to see all of it - it needs an answer.
<span class="fr-block">Return Result</span> is where you compose that answer. Its <span class="fr-control">Content Type</span> sets the format the caller
receives - <span class="fr-control">JSON</span>, <span class="fr-control">XML</span>, or <span class="fr-control">Plain Text</span>. Under JSON, the <span class="fr-control">Compose Result</span> toggle decides how
you build it. With it on, you compose an object from a list of <span class="fr-control">Property</span> and <span class="fr-control">Value</span> rows,
each row a name paired with an expression: you assemble the exact shape you want to hand back -
say { token, expiresAt } - from values the flow worked out along the way, and nothing else leaks
out. With it off - and always under XML and Plain Text - the block hands back a single value from one
<span class="fr-control">Result</span> expression instead, for when the answer is just one thing. Either way, the caller reads back
only what you returned and never sees the rest.

The block is also terminal: it has no outbound connector, so nothing can be wired after it. When a
path of the flow reaches it, the object is composed and that path ends there. The composed object is
what a [Call Flow](call-flow.md){.fr-block} block waiting on this flow, or a [SubFlow](subflow.md){.fr-block} block running it, reads back as its
result. The parent reads it through that caller block's result alias - if the <span class="fr-block">Call Flow</span> block is
named Issue Token, a later step in the parent reads a returned property as
<span class="fr-expr">Issue Token Result → token</span>, built in the Expression Editor under Block Data.

## When to use it

Reach for it - it lives in the block list's Utils group - at the end of any flow that another flow runs and reads back from: a flow invoked by a <span class="fr-block">Call Flow</span> block, or the steps inside a <span class="fr-block">SubFlow</span> block. Those callers only get back what a <span class="fr-block">Return Result</span> hands them, so this is how you decide what they see: the new record's id, a token, a status object, rather than the flow's whole internal workings. A flow with no <span class="fr-block">Return Result</span> still runs to completion, but it gives its caller nothing structured to read, so add this block whenever the caller needs an answer.

## Returning more than one result

A flow does not always have a single way out. Put a <span class="fr-block">Return Result</span> on each branch of a
[Condition](condition.md){.fr-block} and a run reaches one or the other depending on which way it forked. That is still
one result per run, and the caller reads back the plain composed object from whichever
block the run reached.

What changes the shape is how many results a single run produces. When a run reaches more
than one <span class="fr-block">Return Result</span> - two parallel branches that each end in one, say - or none at all, the
caller does not get back a single plain object. It gets back an envelope that wraps up
everything the run returned:

- the **first result** - the object from the first <span class="fr-block">Return Result</span> the run reached, so a caller
  that only wants "the answer" has one to read;
- the **list of all results** that ran, each one tagged with the name of the <span class="fr-block">Return Result</span>
  block it came from, so a caller can tell the branches apart and pick out the one it cares
  about;
- an overall **status** for the run.

So the shape depends on the run, not on how many <span class="fr-block">Return Result</span> blocks the flow contains. When
you want the caller to read a simple object directly, make sure a run can reach only one
<span class="fr-block">Return Result</span>; when several can run in the same pass, expect the envelope and read the result
you want out of it by the block name that produced it. The exact envelope is shown on
[Call Flow (Blocking)](../api/call-flow-blocking.md#response).

Switching on <span class="fr-control">Release Caller</span> changes when the caller hears back rather than what: the moment
the run reaches that block, the caller receives that block's composed value and is released,
while the run carries on with whatever else it still has to do. Its help text puts it as
"the flow sends the <span class="fr-block">Return Result</span> output back to the caller immediately and continues
executing. Applies only to synchronous calls." Leave it off when the caller should wait for the
whole run.

## Example

Suppose you build a <span class="fr-block">SubFlow</span> named Issue Token that authenticates against a service and gets back an access token and how long it stays valid. Earlier steps in that subflow have already landed those two values - the token sits in a Data Bucket variable named accessToken, and the expiry in expiresAt. You want the parent flow that runs this subflow to read both back, and nothing else.

Add a <span class="fr-block">Return Result</span> block at the end of the subflow. Leave <span class="fr-control">Content Type</span> on JSON, then add two rows to <span class="fr-control">Compose Result</span> - one property per row, each pairing a <span class="fr-control">Property</span> name with a <span class="fr-control">Value</span> expression:

```text
Content Type: JSON

Compose Result:
  token       =  {{Data Buckets:Auth - accessToken->}}
  expiresAt   =  {{Data Buckets:Auth - expiresAt->}}
```

When the subflow runs and a path reaches this block, it composes { "token": "...", "expiresAt": "..." } and ends there. Back in the parent flow, the result of the block that ran the subflow is that object, and you read each property through that block's result alias. If the <span class="fr-block">SubFlow</span> block is named Issue Token, the next step reads the token in the Expression Editor (under Block Data) as <span class="fr-expr">Issue Token Result → token</span> and uses it on a later call:

```text
Authorization  =  Bearer {{Issue Token Result->token}}
```

Anything the subflow did to obtain the token stays inside the subflow - the caller sees only the two properties you chose to return.

![The Return Result block with its configuration panel: a Content Type and a list of Property and Value rows that compose the result handed back to the calling flow.](../images/reference/return-result-config.png)

## Configuration

| Field | Description |
| --- | --- |
| Content Type | The format of the returned data. The default is JSON, which composes the object from the rows below. |
| Compose Result | The properties of the returned object. Each row is a property name paired with an expression that supplies its value. Together the rows make up the object the caller reads back. |
| Release Caller | Off by default. When on, the caller receives this block's value as soon as the run reaches it and is released, while the run continues; when off, a waiting caller hears back only once the run finishes. Applies to synchronous callers, such as the blocking <span class="fr-block">Call Flow</span> API. |

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Logging | What to log to the Logging panel while the flow is LIVE, both on start and on completion. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Things to watch for

- This block is terminal: it has no outbound connector, so nothing can be wired after it. The path that reaches it ends there - put it where that path's work is finished.
- The shape the caller reads back depends on how many <span class="fr-block">Return Result</span> blocks a single run reaches, not on how many the flow contains. One reached (for example one branch of a <span class="fr-block">Condition</span>) - the plain composed object. None, or more than one in the same run - an envelope holding the first result, a list of every result tagged with the block name that produced it, and the run's status. When you need the caller to read a simple object directly, make sure a run can reach only one <span class="fr-block">Return Result</span>.

## Related

- [Call Flow](call-flow.md)
- [SubFlow](subflow.md)
- [Condition](condition.md)
