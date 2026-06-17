<!-- GENERATED FILE - do not edit. Source: block-knowledge/subflow.yaml. Regenerate: make refgen -->
# SubFlow

This block runs a reusable set of steps - a subflow - as a single step inside your flow. You define those steps once, then drop this block in wherever you need them, handing it the values it should work with and reading back what it produces.

## How it works

A subflow is a named, self-contained set of steps that lives inside your flow and can be placed more than once. When the flow reaches this block, it runs that set of steps as one unit, using the values you pass in, and the value those steps hand back with their [Return Result](return-result.md){.fr-block} block becomes this block's result. Because every placement points at the same definition, editing the steps once updates every place they run. To open the steps and edit them, you step into the block - hover it and choose Expand - and use Return at the top-left to come back out, the same way you work inside any block container.

## When to use it

Reach for it when the same handful of steps shows up in more than one spot in a flow and you do not want to rebuild or copy them each time - refreshing an access token before two different calls, or formatting a record the same way in several branches. Keeping that work as one subflow means a change lands everywhere it runs, instead of being fixed in one place and forgotten in another. The trade-off against a [Call Flow](call-flow.md){.fr-block} block is reach: a subflow stays inside this one flow, so if the same logic also needs to run from other flows, build it as its own flow and use a <span class="fr-block">Call Flow</span> block instead.

## Example

Suppose a flow makes two calls to a service that expects a fresh access token on each call, and the token expires quickly. Rather than build the get-a-token steps twice, you build them once as a subflow named Get New Token. Inside it, an [HTTP Request](http-request.md){.fr-block} authenticates and a <span class="fr-block">Return Result</span> block hands back the token it obtained:

```text
Inside the Get New Token subflow:
  HTTP Request   ->  POST /oauth/token   (authenticate)
  Return Result  ->  { token: <the access token from the response> }
```

Now place a <span class="fr-block">SubFlow</span> block before the first call, point it at Get New Token, and map the one value those steps need to start. Each input is a name paired with an expression: the name has to match a value the subflow expects, and the expression is where it comes from here:

```text
SubFlow:  Get New Token

Input parameters:
  clientId  <-  {{Data Buckets:Auth - clientId->}}
```

When the flow reaches the block, the Get New Token steps run as one unit and their <span class="fr-block">Return Result</span> hands back an object like `{ "token": "ey..." }`. That object becomes this block's result, so the next step reads the token from it and uses it on the first call. Place a second <span class="fr-block">SubFlow</span> block - again pointing at Get New Token - before the second call, and it produces a fresh token the same way. Because both placements run the one definition, the day the token endpoint changes you edit Get New Token once and both calls pick up the fix.

## Configuration

| Field | Description |
| --- | --- |
| <span class="fr-block">SubFlow</span> | Required. The subflow whose steps this block runs. You pick from the subflows defined for this flow, and the block always runs the version you selected. |
| Input parameters | The values handed to the subflow to work with. Each row pairs a name, which has to match a value the subflow expects, with an expression that supplies it from this flow. |

## Behavior

- Runs the chosen subflow's steps as one unit, using the mapped input parameters.
- Captures the object the subflow's <span class="fr-block">Return Result</span> block hands back as this block's result.
- You open and edit the steps by stepping into the block (Expand), the same as any block container.

## Things to watch for

- A subflow cannot contain another <span class="fr-block">SubFlow</span> block - you cannot place a subflow inside a subflow.
- The subflow only hands a result back if its steps reach a <span class="fr-block">Return Result</span> block. Without one, this block runs the steps but gives the rest of the flow nothing structured to read.
- Editing a subflow's steps changes every placement of it in the flow, since they all run the one definition. A fix in one place is a fix everywhere - which is the point, but means a change is never local to a single placement.

## Related

- [Call Flow](call-flow.md)
- [Return Result](return-result.md)
