# Activating an External Callback

An external callback is useful in two scenarios:

1. Your flow may need to start in response to an external event - a payment provider announcing a charge,
   a form posting a submission, your own application saying the work it was given is finished.
2. Your flow may need to wait for something outside it to finish before it resumes - a user approves a
   transaction, confirms email copy, and so on.

The [External Callback](../reference/external-callback.md){.fr-block} block is the way to enable these
types of behavior. Place it at the beginning of your flow or in the middle, depending on the use case. The
block gets its own address (a URL). Whoever calls it either starts or resumes your flow.

This page is about making that call. Building the flow around it is covered in
[Waiting on an External System](../build/flow-control/external-callbacks.md).

!!! note "This is the callback block, not every trigger"
    Other triggers in FlowRunner come from the services they belong to, and are activated by those services
    in their own way. This page applies to the External Callback block, which is FlowRunner's own.

## Get the address

Select the External Callback block. Its ((Callback URL)) field holds the whole address, with a copy button
beside it. Copy it and give it to whichever system needs to activate the trigger in the flow.

![The External Callback block selected, its settings showing the generated Callback URL with a copy button.](../images/learn/quickstart-callback-url.png)

The URL automatically includes identifiers for the workspace, the flow and for this particular block:

```text
https://api.flowrunner.ai/{workspace-id}/{api-key}/automation/flow/{flow-id}/trigger/{block-id}/activate
```

Every External Callback block has its own URL. They are not interchangeable.

For real traffic, a version of the flow has to be **LIVE**. Call the address when nothing is published and
you get error `28010` - not because your request was malformed, but because there is nothing live to
receive it.

While you are building, two things make the URL answer without the flow being LIVE:

- **((Learning Mode))** captures one sample request and records its shape, so the fields become pickable in
  later steps.
- **((Run Block))** on the callback starts a debug execution that waits for your call.

## Make the call

The Callback URL accepts either `GET` or `POST`, and nearly every call carries data with it - the event
that happened, the record it happened to, whatever the flow needs in order to carry on.

Whatever you send becomes **this block's data**, read by later steps under the alias set on the block.

With `POST`, send it as a JSON body:

```bash
curl --request POST \
  --url "<Callback URL>" \
  --header "Content-Type: application/json" \
  --data '{"event":"payment.succeeded","orderId":"ORD-9001","amount":4999}'
```

With `GET`, send it as query parameters:

```bash
curl "<Callback URL>?event=payment.succeeded&orderId=ORD-9001&amount=4999"
```

On a `POST`, query parameters are ignored - apart from `execution`, which the rest of this page is about.

If there is nothing to send, the address on its own is a valid call:

```bash
curl "<Callback URL>"
```

## Starting a run, or continuing one

Both scenarios from the top of this page make the same call. What differs is what the call finds.

**If the callback is the first step**, there is no run yet. Your call creates one, and it begins with the
data you sent.

**If the callback sits further along**, the run was already under way - started by whatever starts that
flow - and it has arrived at the block and stopped, waiting for you. Your call lets it carry on, with the
data you sent now available to the steps that follow.

Only the second case asks more of you: a waiting run has to be identified.

## When more than one run is waiting

Picture an order-processing flow. It runs every few minutes, and each run reaches a callback and waits for
its own payment to clear. By mid-morning three runs are sitting at that same block, each waiting for a
different order.

Now a payment clears and the provider calls your address. Which of those three should continue?

The address cannot answer that on its own - it names the flow and the block, not the run. So the call says
which one, using the `execution` query parameter (`executionId` is accepted too):

```text
POST  <Callback URL>?execution={execution-id}
```

Which value you use depends on whether the waiting runs are worth telling apart:

| Value | Continues | Use it when |
| --- | --- | --- |
| `execution={execution-id}` | that one run | The runs are distinct - each waits for its own order, its own customer, its own document |
| `execution=any` | one waiting run, FlowRunner's choice | The runs are interchangeable and it does not matter which continues |
| `execution=all` | every run waiting at this block | One event releases all of them at once |

The response names the run that continued, or lists them comma-separated for `all`:

```json
{ "executionId": "4CE29875-0BD4-4AE4-B75C-60FCC55F4436" }
```

With `execution=all` and nothing waiting, the call still succeeds - HTTP 200, null id:

```json
{ "executionId": null }
```

## Where the execution id comes from

A run's id exists only once the run is under way, so it cannot be written into anything in advance. It
reaches the caller one of three ways.

**The flow hands out its own address.** This works however the run began - a schedule, an API call, another
flow. Every run knows its own ((Execution ID)) in the Expression Editor under **Flow Context**, so the step
that calls the outside system composes the return address from the Callback URL and that id, and sends it.
Whatever comes back points at this run.

![The Expression Editor of a step before the callback: an External Callback URL reference under External Callback URLs, and Execution ID under Flow Context, joined into one return address.](../images/build/externalcallback-url-reference.png)

**The caller started the run and was told.** A system that started the run through the
[Call Flow](call-flow.md) API received `executionId` in the response, and can quote it back.

**Nobody can carry a per-run address.** A webhook configured once in a vendor's dashboard posts to one
fixed URL and cannot append anything. Use `execution=any` on it.

[Waiting on an External System](../build/flow-control/external-callbacks.md) works all three through with
diagrams.

## When a call is refused
<!-- doclint: no-shot: an error reference, not a screen; each row carries the message FlowRunner returns and the fix -->

A refused call comes back as HTTP 400 with an error `code` and a message:

```json
{
  "code": 28056,
  "message": "Your trigger activation request format can be used only for a flow that starts with a trigger. Consider adding \"execution\" parameter to activate a \"middle of the flow\" trigger."
}
```

**The call did not identify a waiting run**

| Code | What FlowRunner tells you | What to do |
| --- | --- | --- |
| error `28056` | The request format can be used only for a flow that starts with a trigger; consider adding the `execution` parameter to activate a middle-of-the-flow trigger | You called a callback that sits later in a flow. Add `execution` |
| error `28059` | Pending trigger was not found. Ensure that passed execution ID is valid and flow execution is waiting on this trigger | The id is wrong, or that run is not sitting at this block |
| error `28060` | Pending trigger was not found. Ensure that flow execution is waiting on this trigger | You used `execution=any` and nothing was waiting |
| error `28099` | The trigger for this execution has already been activated | This run has already been let through this callback. A run passes a given block once; a later callback in the same flow is a separate wait with its own activation |

**The flow or the block cannot be reached**

| Code | What FlowRunner tells you | What to do |
| --- | --- | --- |
| error `28010` | Trigger with that flow element ID is not found in that flow; ensure the flow and trigger names are correct and that the flow has a live version | Re-copy the Callback URL, and publish the version |
| error `28011` | Trigger with that name is not found in that flow; same advice | As above |
| error `28042` | The flow version is not enabled, so its trigger cannot be executed | Set the version LIVE |
| error `28093` | Available only when the flow is in the LIVE state | Publish the version you are calling |

**The run is no longer there**

| Code | What FlowRunner tells you | What to do |
| --- | --- | --- |
| error `28068` | Execution context with that id not found | The id is wrong, or the run finished and was cleared |
| error `28136` | That execution is already terminated | The run ended before your call arrived |

**The caller is not allowed**

| Code | What FlowRunner tells you | What to do |
| --- | --- | --- |
| error `28025` | Unable to execute the callback. User is missing required security role(s) | Call with a user token carrying the required role |
| error `28061` | The user token is invalid | Obtain a fresh token |

Codes that any call can return - bad credentials, a malformed request, rate and plan limits - are listed
once on the [API overview](index.md).

!!! note "A call can also be accepted and still do nothing"
    A callback block can carry a condition deciding whether an incoming call counts. When the condition is
    false the call is accepted - HTTP 200, no error - and nothing happens: no run starts, and a waiting run
    stays waiting. If a call appears to succeed but the flow does not move, check that condition first.

## Related

- [Call Flow](call-flow.md) - starting a run over the API, and the executionId it returns
- [External Callback](../reference/external-callback.md){.fr-block} - the block itself, its Callback URL,
  conditions, and Learning Mode
- [Waiting on an External System](../build/flow-control/external-callbacks.md) - building the flow that
  pauses and continues
- [Workspace Settings](../manage/workspace-settings.md) - the credentials every call carries
