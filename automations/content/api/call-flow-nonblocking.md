<!-- doclint: allow-unlinked: Call Flow -->
<!-- On this page "Call Flow" names the HTTP API, not the block of the same name.
     The block is linked explicitly under Related. -->
<!-- Split from api/call-flow.md 2026-08-24 at Mark's direction: one page per call, full copy-ready URLs,
     a self-contained section per method. Verified in-product 2026-08-18 (Documentation Flows workspace,
     curl against api.flowrunner.ai; full log in .cache/api-spec/verification-2026-08-18.md; example flow
     "Order Lookup" 07E7DA91, kept LIVE): activate took the flow ID only (name -> 28053; ids are
     case-sensitive, a lower-case GUID -> 28053) [SUPERSEDED by FR-3408 - see the 2026-08-31 re-drive below]; the body is exactly {"executionId": "<GUID>"} in every
     captured response (dozens across the log); renaming the flow leaves this URL unaffected; a paused
     version ("On hold") -> 28053; POST body + query params merge into Initial Data, same key in both ->
     400/28064; GET query values arrive as strings, POST JSON keeps types; POST body without Content-Type:
     application/json -> HTTP 415; POST with no body -> 200; PUT -> HTTP 405; error 9000 = unknown workspace
     id; waitResponseTimeoutSeconds sent to this endpoint is NOT consumed - it lands in Initial Data
     (instance FC8A3D97); the editor address /flow/07E7DA91-.../version/1/... carries the id this endpoint
     accepts and the id the dialog writes into the non-blocking URL; an External Callback-first LIVE flow is
     STARTED by this call (200 + a run waiting at the callback - driven on the throwaway "Callback Probe");
     the dialog writes the non-blocking URL by id for a flow with no Return Result (Order Poller, pictured;
     driven on the blocking page's log). 2026-08-24: HEAD is answered like GET and STARTS A RUN (200; instance
     D389B25E on Order Lookup); DELETE -> HTTP 405; PUT -> HTTP 405 (2026-08-18). 28045 was driven 2026-07-08
     against the NAME-based blocking endpoint (flow-scheduling-concept.yaml); not re-driven against this
     id-based endpoint.
     2026-08-25: the "No call returns a run's outcome by id" claim was RETRACTED - the Execution Status &
     Results API shipped (FR-3242 v1.0.12 2026-07-28, FR-3243 1.0.13 2026-08-10, paths finalised by FR-3342
     v1.0.14 2026-08-18) and is driven in .cache/api-spec/verification-2026-08-25-execution-api.md. The
     outcome-by-id routes now point at execution-status.md and block-results.md; the flow-delivers-its-own-
     answer workaround is KEPT because a Return Result block has no result alias, so neither read endpoint
     can return the flow's answer (verified in the Order Lookup editor). KNOWN, REPORTED TO MARK, NOT DOCUMENTED: the API key segment is not checked;
     malformed JSON returns HTTP 500 with a stack trace. 2026-08-24: 2002 not reproducible (all wrong-workspace
     shapes -> 9000) - dropped, restore when driven; 8007/8008 dropped (nothing on this endpoint can produce
     them); 2026-08-24 drive: POST body [1,2,3] and "x" -> 200 (runs 37B304A5, 072A3F8D) - a non-object JSON body is
     not refused, nothing lands in Initial Data by name. The rate/plan-limit rows are carried from the removed api/index.md shared table (Mark-reviewed
     2026-08-06 lineage), not driven.
     2026-08-27: the GET paragraph's advice was NARROWED. It read "when the flow needs real numbers,
     booleans, or structured values (objects, lists), call with POST instead", which reads as "a GET cannot
     carry a number the flow can use". Drives on 2026-08-24 disproved that as stated: Condition's
     GREATER_THAN accepted a numeric STRING on all five routes, including the GET. The wire fact is
     untouched - query values arrive as text - and the sentence now says only what POST buys you (values
     arrive typed), asserting nothing about which blocks do or do not coerce. No coercion rule is claimed
     anywhere on this page, because none has been driven across blocks.

     RE-DRIVEN 2026-08-31 for FR-3408 (Documentation Flows workspace on dev.flowrunner.ai - host
     dev-api.flowrunner.ai; flow "TD Sandbox" C24408A2, published LIVE for the test and returned to Ready).
     activate now accepts the flow NAME as well as the ID, over GET and POST - all eight combinations
     (activate | activate-blocking x id | name x GET | POST) returned HTTP 200, so the ID-only rule above is
     superseded. 28053 is unchanged for this endpoint but is now ALSO what activate-blocking answers, and its
     message reads "Flow with ID or name 'X' and status 'LIVE' is not found." Re-confirmed: identifiers are
     case-sensitive (td%20sandbox -> 28053) and a name must be percent-encoded (TD+Sandbox -> 28053; a `+` is
     not decoded to a space in a path segment). Driven three ways for the code: unknown id, unknown name, and
     a good identifier with the flow stopped.
     The Launch Flow Instance dialog still writes the ID form here, and the NAME form on the blocking page -
     verified by adding a Return Result to TD Sandbox, publishing, reading the dialog
     (.../automation/flow/TD%20Sandbox/activate-blocking?waitResponseTimeoutSeconds=300, tabs GET URL / cURL)
     and then deleting the block. So the id/name split is now a property of the DIALOG, not of the endpoints.
     -->
# Call Flow (Non-Blocking)

The non-blocking Call Flow endpoint starts an instance of a **FlowRunner™** flow with one `GET` or `POST`
request and returns at once: the response carries the new run's `executionId`, and the run continues on its own. Use it when you only need the work started -
a long job, a batch, a flow that pauses at an
[External Callback](../reference/external-callback.md){.fr-block} - or when the run may outlast the blocking
call's 300-second maximum wait. When your code needs the flow's result in the same request, use
[Call Flow (Blocking)](call-flow-blocking.md) instead.

## Endpoint
<!-- doclint: no-shot: the URL contract, not a screen; the Credentials section is pictured on Workspace Settings and the dialog that writes this URL is pictured below -->

```text
https://api.flowrunner.ai/{workspace-id}/{api-key}/automation/flow/{flow}/activate
```

| Placeholder | Value | Where it comes from |
| --- | --- | --- |
| `{workspace-id}` | The workspace the flow belongs to | **Workspace Settings ▸ General ▸ Credentials** - see [Workspace Settings](../manage/workspace-settings.md#name-and-credentials) |
| `{api-key}` | The workspace's API key | Same place |
| `{flow}` | The flow's **id**, or its **name** URL-encoded (`Order%20Lookup`) - either one works | The id is the segment after `/flow/` in the address bar while the flow is open; the name is in the breadcrumb and the flows list - see [Flows](../manage/flows.md). Both forms are case-sensitive. An id URL survives a rename; a name URL does not. The **Launch Flow Instance** dialog writes the id form |

Every query parameter, and every property of a `POST` body, becomes one value in the run's Initial Data - this
endpoint has no parameters of its own, so leave `waitResponseTimeoutSeconds` out (here it would land in
Initial Data like any other name). The endpoint answers only while a version of the flow is LIVE;
otherwise the call is refused with error `28053`.

## Calling with GET

Copy, fill in the placeholders, and run - the flow's values travel in the query string:

```bash
curl "https://api.flowrunner.ai/{workspace-id}/{api-key}/automation/flow/{flow}/activate?orderId=1042"
```

A `GET` needs no headers. Each query parameter becomes one value in the run's Initial Data, under its own
name. Query values arrive as text: `orderId=1042` reaches the flow as `"1042"`. A query string carries text
only, so call with `POST` when the flow needs numbers, booleans, or structured values to arrive typed. Any fetch of this URL starts a real run - a `HEAD` request, a
chat link preview, a browser prefetch, or an uptime monitor included - and this call returns at once, so an
accidental run is easy to miss. Share the URL as text, never a clickable link.

## Calling with POST

The same call with the flow's values as a JSON body:

```bash
curl --request POST \
  --url "https://api.flowrunner.ai/{workspace-id}/{api-key}/automation/flow/{flow}/activate" \
  --header "Content-Type: application/json" \
  --data '{
    "orderId": 1042
  }'
```

A `POST` body is a JSON object, sent with `Content-Type: application/json` (a `charset` parameter is
fine; any other media type is refused with HTTP 415). Each top-level property becomes one value in the
run's Initial Data, with its JSON type kept: `{"orderId": 1042}` reaches the flow as the number `1042`. An
empty object `{}` is valid, and so is a `POST` with no body at all.

When a `POST` carries both a body and query parameters, FlowRunner merges the query parameters into the
body object. Two rules follow from that, and both are refusals rather than silent surprises: a key sent
both ways is refused with `28064`, and a body that is valid JSON but **not an object** - an array, a bare
string - is refused with `28064` too, because there is no object to merge into. A non-object body on its
own, with no query parameters, is still accepted: the run starts with nothing for Initial Data to pick up
by name.

## Response
<!-- doclint: no-shot: the one-line response body and what the id is for; the HTTP Request block named in the delivery recipe is pictured on its own reference page and the recipe is worked through on Waiting on an External System -->

The call returns HTTP 200 as soon as the run exists. The body carries the run's identity and nothing else,
because the run has not finished:

```json
{
  "executionId": "4CE29875-0BD4-4AE4-B75C-60FCC55F4436"
}
```

The id finds the run on the flow's Instances tab (see
[Running Flows](../run/running-flows.md#watching-the-runs)), and names the run when you continue it at an
External Callback. It is also how your code asks what became of the run: hand it to
[Checking a Run's Status](execution-status.md) to learn whether the run is still going and how it ended,
or to [Retrieving Block Results](block-results.md) to read what an individual block produced. Neither
returns the flow's own answer - a [Return Result](../reference/return-result.md){.fr-block} block has no
result alias - so when you need that value, either use
[Call Flow (Blocking)](call-flow-blocking.md) and let it wait, or have the flow deliver the answer itself:
an [HTTP Request](../reference/http-request.md){.fr-block} from the flow to your endpoint, carrying the
result and the run's Execution ID. Every step can read that id under Flow Context -
[Waiting on an External System](../build/flow-control/external-callbacks.md) shows how. Match it to the
`executionId` this call gave you.

## Errors
<!-- doclint: no-shot: an error reference, not a screen; each row names the condition and the fix -->

Most refusals come back as HTTP 400 with a JSON `code`, `message`, and `details`; a wrong media type or
method is refused at the HTTP level (415 / 405) with no code. This is what the endpoint returns when it is
given the flow's name, because it expects the id:

```json
{
  "code": 28053,
  "details": {},
  "message": "Flow with ID 'Order Lookup' and status 'LIVE' is not found."
}
```

| Code | What it means | What to do |
| --- | --- | --- |
| `28053` | No LIVE flow with that id or name | Check the identifier is cased exactly as FlowRunner shows it - a name also has to be URL-encoded (`Order%20Lookup`), and a `+` is not read as a space - and that a version is LIVE. A paused version (On hold) answers this too, so put it back with **Resume flow** in the flow's toolbar (see [Running Flows](../run/running-flows.md#stopping-and-replacing-a-live-flow)). Renaming the flow breaks a name URL but leaves an id URL working |
| `2027` | The API key is not this workspace's key | Re-copy the API Key from **Workspace Settings ▸ General ▸ Credentials**. Regenerating the key invalidates every URL built on the old one |
| `9000` | No workspace with that id | Re-copy the Workspace ID from **Workspace Settings ▸ General ▸ Credentials** |
| `28064` | Query parameters could not be merged into the body: either the same key was sent both ways, or the body is valid JSON but not an object | Read the `message` - it names the duplicated key, or says the body is not an object. Send each value once, and make the body an object whenever you also send query parameters |
| `28045` | The flow can be called only by its schedule | Turn off **Allow only scheduled flow instances** in the version's **Flow Execution Policy** - see [Flow Scheduling](../reference/flow-scheduling-concept.md#the-flow-execution-policy) |
| HTTP 415 | A `POST` body sent without `Content-Type: application/json` | Send that header |
| HTTP 405 | `PUT` and `DELETE` are refused | Use `GET` or `POST`. `HEAD` is not refused - it is answered like `GET` and starts a run |

**Rate and plan limits**

| Code | What it means |
| --- | --- |
| `999` / `997` / `995` | A request-rate limit was exceeded - back off |
| `998` | Too many requests are in flight at once - back off |
| `28083` | The workspace's monthly execution allowance is exhausted - wait for the month to reset, or raise the plan (see [Billing](../manage/billing.md)) |
| `28087` / `28132` | Too many runs are executing at once / the execution maximum is reached - retry once some finish |
| `28086` | The maximum number of active flows has been exceeded - stop a LIVE flow you no longer need, or raise the plan |

## Starting a flow that waits for a callback
<!-- doclint: no-shot: explains why this endpoint fits callback flows and why the run's id matters, not a screen; the trigger's panel is on External Callback and the resume call on Activating an External Callback -->

A flow that contains an External Callback trigger does not run start to finish. The run stops at that block
and waits for an outside call before it continues. This endpoint is the right way to start such a flow: a
blocking call would sit waiting at the trigger until its timeout ran out, leaving you no id for the waiting
run (see [Call Flow (Blocking) ▸ Timeout](call-flow-blocking.md#how-long-the-call-waits)).

Keep the `executionId` this call returns. Several runs can wait at the same block, and the block's URL names
the flow and the block, not the run - so when the outside system calls back, the `executionId` is what tells
FlowRunner which run to continue. See [Activating an External Callback](activating-a-trigger.md) for that
call, including the cases where you do not need the id.

## Let FlowRunner write the call for you

For a flow with no [Return Result](../reference/return-result.md){.fr-block} block, the ((Launch Flow
Instance)) dialog writes this page's URL, with the flow's id and your credentials already filled in, on its
((GET URL)) and ((cURL)) tabs. Open it with ((Run Instance)) in the toolbar at the top of the flow - the
dialog is pictured in full on
[Call Flow (Blocking)](call-flow-blocking.md#let-flowrunner-write-the-call-for-you). Here it is for Order
Poller, which reads nothing from Initial Data, so no form is shown:

![The Launch Flow Instance dialog for a flow without a Return Result block (Order Poller): a Previous Instance selector, no Initial Data form, and the GET URL tab explaining that the flow has no Return Result block so a non-blocking request URL is provided; the box labelled "GET URL - Non-blocking request" holds the URL ending in the flow's id followed by /activate.](../images/api/callflow-launch-nonblocking.png)

For a flow that has a Return Result, the dialog writes the blocking URL instead - to start such a flow
without waiting, build this page's URL yourself from the [Endpoint](#endpoint) template, with the id from
the flow's address bar.

## Related

- [Call Flow (Blocking)](call-flow-blocking.md) - starting a run and waiting for its answer
- [Activating an External Callback](activating-a-trigger.md) - letting a specific waiting run continue
- [Checking a Run's Status](execution-status.md) - asking what became of a run, by its `executionId`
- [Retrieving Block Results](block-results.md) - reading what an individual block of the run produced
- [Workspace Settings](../manage/workspace-settings.md#name-and-credentials) - where the Workspace ID and API Key live
- [Call Flow](../reference/call-flow.md){.fr-block} - the block that does the same job from inside another
  flow
