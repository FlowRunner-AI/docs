# Flow Control

<!-- Section index / map (2026-07-18). Conceptual intro + a reader-question map + cross-routes. No
screenshots: this page operates no controls; every concept is taught (and verified) on its child page.
Depth ceiling: name the work + route to the child page; no block names/config/modes on this page. -->

Real work rarely runs in a straight line. A paid order goes one way and an unpaid one another; a list has
to be worked item by item; three lookups can run at once; a step waits for a payment to clear; a call to a
flaky service has to survive a hiccup. Flow control is how you shape a run's path to fit the work - the
decisions, loops, parallel steps, waits, and recoveries you reach for.

The tools below are peers, and a real flow often uses several. Find the one that answers your question.

## Send a run down the right path

When the next step depends on a test - is the order paid, which plan is the customer on - you split the
run so each case is handled on its own terms. A yes/no test sends it one of two ways; a value picks among
several. See [Yes/No Branching](branching.md) and [Routing on a Value](routing.md).

## Repeat a stretch of work

When the same steps have to run more than once - over and over until something becomes true, or once for
every item in a list. See [Repeating Steps](repeating.md) and [Working Through a List](collections.md).

## Run steps at the same time

When independent steps do not depend on each other, run them together so the flow finishes at the speed of
its slowest step, not the sum of them all. See [Running Steps in Parallel](parallel.md).

## Wait before continuing

When a step should not happen yet - hold for a set time, or until an outside system reports back. See
[Adding a Delay](waiting.md) and [Waiting on an External System](external-callbacks.md).

## Keep going when a step fails

By default a failure stops the run. Instead you catch it and send the run down a recovery path you build -
log what went wrong, fall back to a default, alert someone, or retry. See
[Handling Errors](error-handling.md).

## Related, outside Flow Control

<!-- doclint: no-shot: cross-route link list, not a scenario; each destination shows its own screens -->

- [AI Router](../../reference/ai-router.md){.fr-block} - route a run on a decision only an AI can make,
  like free-text intent or an image.
- [Triggers](../../learn/concepts/triggers.md) - what starts a run of a flow, such as an outside event.
- [Scheduling](../../reference/flow-scheduling-concept.md) - run a flow on a timetable.
- [Subflows](../../learn/concepts/subflows.md) and [Call Flow](../../reference/call-flow.md){.fr-block} -
  hand a stretch of work to another flow.
