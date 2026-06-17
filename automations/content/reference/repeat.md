<!-- GENERATED FILE - do not edit. Source: block-knowledge/repeat.yaml. Regenerate: make refgen -->
# Repeat

This block runs the same set of steps over and over for as long as a condition you set stays true. You build the steps inside it, and it keeps running them until the condition turns false.

## How it works

It is a block container that repeats the steps inside it for as long as your condition stays true - what other tools call a while loop. Before each pass it checks your condition; while the condition is true it runs the steps inside once more, then checks again. The moment the check comes back false, the loop stops and the flow moves on. Because the same steps run each pass, something inside the loop has to change a value the condition depends on - otherwise the check would stay true forever. So the loop also carries a failsafe: a cap on how many passes it will ever make, which stops it even if the condition never turns false. The pass count is available inside the loop as `Current Iteration Number`, counting up from 0 on the first pass.

## When to use it

Reach for it when you need to repeat work an unknown number of times until something becomes true - polling a status until it is finished, retrying a call until it succeeds, or building a value up until it is large enough. The deciding factor is that you do not have a list to walk: when you do have a list and want to touch every entry, [List Iterator](list-iterator.md){.fr-block} is the cleaner fit. <span class="fr-block">Repeat</span> is for the case where the number of passes depends on what happens at run time, not on a count you know in advance.

## Example

Suppose a flow places an order with a fulfilment service, and that order takes a little while to process. You want to wait for it to finish, but you do not know how long that will take. The plan is to keep checking the order's status until it reads "shipped", pausing between checks so you are not hammering the service.

First, outside the loop, a [Set Variables](set-variables.md){.fr-block} block reads the order's starting status into a Data Bucket variable named Order Status, seeded with its initial value of "processing". The <span class="fr-block">Repeat</span> block's [Condition](condition.md){.fr-block} then checks that variable: keep looping while Order Status is not "shipped".

```text
Condition:  Order Status   not equals   "shipped"
Max Iterations (failsafe):  20
```

Inside the loop you build a pause followed by a fetch-and-store. A [Wait](wait.md){.fr-block} block pauses for 30 seconds so the service has time to make progress, and then an [HTTP Request](http-request.md){.fr-block} block re-fetches the order and a <span class="fr-block">Set Variables</span> block writes the fresh status back into Order Status. Each pass the loop re-checks the condition against that updated value.

Here is how it plays out for an order that ships on the third check:

- **Pass 0** - Order Status is "processing", so the condition is true; the loop waits, re-fetches, and the status is still "processing".
- **Pass 1** - still "processing", condition true again; waits, re-fetches, now "in transit".
- **Pass 2** - "in transit" still is not "shipped", condition true; waits, re-fetches, and this time the status comes back "shipped".
- **Next check** - Order Status is "shipped", so the condition is false and the loop stops.

The flow carries on with Order Status holding "shipped". Had the service stalled and never shipped, the failsafe of 20 would have stopped the loop after 20 passes rather than letting it run forever, and the flow could then handle the timeout however you choose.

## Configuration

| Field | Description |
| --- | --- |
| <span class="fr-block">Condition</span> | Required. The loop keeps running while this is true and stops the moment it is false. It is re-checked before every pass, so a step inside the loop must change something the condition looks at, or the loop would never stop on its own. In the product this is called the <span class="fr-block">Repeat</span> While condition. |
| Max Iterations (failsafe) | A hard cap on the number of passes, defaulting to 10000. The loop stops when it reaches this many passes even if the condition is still true - a safety net against a loop that never ends. Set it to a sensible number for your case while you are building the flow. |

## Things to watch for

- The pass count, available inside the loop as `Current Iteration Number`, starts at 0 on the first pass, not 1.
- A step inside the loop has to change something the condition checks. If nothing inside ever makes the condition false, the loop runs until it hits the failsafe.
- Always set the failsafe to a sensible number while you build the flow, so a mistake in the condition cannot leave the loop running far longer than you intended.
- The loop needs steps inside it to do anything; step into it (hover the loop and choose Expand) to build the loop body, and use Return at the top-left to come back out.

## Related

- [List Iterator](list-iterator.md)
- [Condition](condition.md)
- [Set Variables](set-variables.md)
- [Wait](wait.md)
- [Break](break.md)
