<!-- GENERATED FILE - do not edit. Source: block-knowledge/wait.yaml. Regenerate: make refgen -->
# Wait

This block pauses for a set amount of time before the flow carries on. The path of the flow that reaches it waits out the delay and then continues to the next step.

## How it works

A flow can split into several paths, or branches; only the one that reaches this block waits, and it waits for exactly the duration you set before picking up where it left off. You set the duration one of two ways. With **Expression Mode** off you fill in plain **Days**, **Hours**, **Minutes**, and **Seconds** fields, and at least one has to be non-zero. With **Expression Mode** on you supply an expression that works out to a number of seconds, so the wait can be computed at run time rather than fixed when you build the flow.

## When to use it

Reach for it whenever a step should not happen immediately. The most common case is backing off before a retry: after a call fails, you pause so the thing you are calling has a moment to recover before you try again. It also paces work that would otherwise run too fast - spacing out repeated calls so you stay under a rate limit (the cap on how often a service will accept calls before it starts rejecting them), or holding for a stretch before a follow-up step. It is a single block for the job, rather than rigging up timing logic out of other blocks.

## Example

Suppose an [HTTP Request](http-request.md){.fr-block} block calls a payment provider, and that provider sometimes returns an error when it is briefly busy. You want to give it one more try, but not the instant it failed. Wire a [Handle Error](handle-error.md){.fr-block} block off the failing call - that gives you a separate branch that only runs when the request fails - and on that branch place a <span class="fr-block">Wait</span> before you run the same <span class="fr-block">HTTP Request</span> again.

Leave **Expression Mode** off and set the fields to one minute - **Minutes** is 1, the rest are 0:

```text
Days: 0   Hours: 0   Minutes: 1   Seconds: 0
```

Now when the call fails, the error path reaches the <span class="fr-block">Wait</span>, the branch pauses for 60 seconds, and only then does it run the same <span class="fr-block">HTTP Request</span> again.

## Configuration

| Field | Description |
| --- | --- |
| Expression Mode | Off = simple Days/Hours/Minutes/Seconds; On = an expression that works out to a number of seconds. |
| Days/Hours/Minutes/Seconds (delay) | The pause duration (at least one non-zero in simple mode). |

## Behavior

- Suspends the branch for the duration you set, then continues.
- Common pattern: <span class="fr-block">Handle Error</span> -> <span class="fr-block">Wait</span> (backoff) -> retry.

## Things to watch for

- In Expression Mode the expression has to work out to a number of seconds, not minutes or hours - to wait five minutes it must produce 300.

## Related

- [Handle Error](handle-error.md)
- [Synchronize](synchronize.md)
