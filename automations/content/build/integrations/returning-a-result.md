# Returning a Result

Some flows produce a result - a token, a record id, an approval decision. A
[Return Result](../../reference/return-result.md){.fr-block} block is how that value leaves the flow and
reaches whatever called it. The caller sees only what you put there; the rest of what the run did stays
inside.

Not every flow needs one. A flow that files a record or sends a notification may have nothing to hand
back, and it runs to completion without a Return Result.

## Who reads what you return

<!-- doclint: no-shot: names the caller blocks only to say who reads the value; each is pictured on its own reference page -->

- a [Call Flow](../../reference/call-flow.md){.fr-block} block in another flow, which reads it through that
  block's own alias - a parent step reads {{Issue Token Result->token}};
- a [SubFlow](../../reference/subflow.md){.fr-block} block running these steps inline;
- an [AI Agent](../../reference/ai-agent.md){.fr-block} that has been given the flow as a tool - what you
  return is what the agent gets to reason with. See
  [Flows as Agent Tools](../../reference/flows-as-agent-tools-concept.md);
- a system calling the flow over the REST API on the blocking endpoint, which gets the composed result as
  the response body. See
  [Calling a flow that returns a value](../../api/call-flow.md#calling-a-flow-that-returns-a-value).

## Compose the answer

Put a Return Result at the end of the path the run will take, and decide two things: ((Content Type)) sets
the format the caller receives - JSON, XML, or plain text - and ((Compose Result)) decides how you build
it. With it on, you add a row per property, each pairing a ((Property)) name with a ((Value)) expression,
so you hand back exactly the object you meant to. With it off, the block returns a single value from one
expression, for when the answer is a single value.

![The Return Result block's panel: Content Type set to JSON, the Compose Result toggle on, and two Property and Value rows - status paired with approved, and amount with 5000 - above a plus to add another row.](../../images/reference/return-result-config.png)

## It ends the path it is on

Return Result is terminal: the block has no outbound connector, so nothing can be wired after it. A path
that reaches one composes its answer and ends there. Put it where that path's work is genuinely finished -
anything else the path has to do belongs before it.

## When more than one can run

<!-- doclint: no-shot: a design decision about the returned shape; the envelope's structure is documented on the Return Result reference -->

It is normal to put a Return Result on each branch of a
[Condition](../../reference/condition.md){.fr-block}, and that changes the shape the caller sees. Reach
more than one and the caller no longer gets a plain object - it gets an envelope holding the first result,
every result that ran tagged with the block name that produced it, and an overall status.

So make it a deliberate choice:

- **Want the caller to read a simple object?** Keep to one Return Result on any path a run can take.
- **Several genuinely can run?** Expect the envelope, and name those blocks meaningfully, because the
  caller picks its result out by the producing block's name.

## Design the answer for the caller

The result is your flow's contract with whoever calls it, so treat it like one:

- **Return what the caller needs to act on, not everything you have.** A new record's id and status beats
  the raw response you happened to get back from a service.
- **Keep the shape stable.** Callers build on the property names you return, so renaming one later breaks
  them.
- **Do not leak internals.** Credentials, raw third-party payloads, and ids that mean nothing outside this
  flow should stay inside it.

## Related

- [Return Result](../../reference/return-result.md){.fr-block} - every field, the envelope, and a worked
  example
- [Running Another Flow](running-another-flow.md) - the calling side, and reading what comes back
- [Flows as Agent Tools](../../reference/flows-as-agent-tools-concept.md) - what an agent does with a
  returned result
- [Calling an External Service](calling-a-service.md) - the other direction: your flow calling out
