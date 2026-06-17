<!-- GENERATED FILE - do not edit. Source: block-knowledge/http-request.yaml. Regenerate: make refgen -->
# HTTP Request

This block calls a web service over HTTP and hands the response back to your flow. You set the address and the method, fill in any data the service needs, and the block's result is whatever the service sends back.

## How it works

Each time the flow reaches this block, it sends one request to the address in the URL field and waits for the reply. The Method tells the service what you want to do - GET reads, POST creates, PUT and PATCH update, DELETE removes, HEAD checks. You attach the pieces a request can carry: a Body (the data you are sending, usually JSON), a Query (the extra parameters tacked onto the end of the URL, like a search term or a page number), and Headers (named values that travel alongside the request, most often the ones that prove who you are). When the reply comes back, the block's result is the response body - the data the service returned - ready for the next step to read.

## When to use it

Reach for it whenever your flow needs to talk to a service that FlowRunner does not already have a dedicated block for: pulling records from a third-party API, posting an update to a webhook, kicking off a job in another system. If a purpose-built block exists for the service you are calling, that block is usually less work because it handles the address and the authentication for you. This block is the general-purpose option for everything else - any service with a web API is reachable from here.

## Example

Suppose you want to list the public organizations a GitHub user belongs to. GitHub's API answers that at a fixed address, so set the Method to GET and the URL to the endpoint for that user:

```text
https://api.github.com/users/octocat/orgs
```

GitHub asks callers to identify the kind of response they want, so add one Header - a Name of Accept and a Value of application/vnd.github+json. A GET request like this carries no Body, since you are reading rather than sending. With that filled in, run the block on its own with Run Block in Test Mode - this sends the real request once, so you can see exactly what comes back before you wire anything downstream. The response body is a list of organizations, each one an object:

```json
[
  { "login": "github",     "id": 9919,   "url": "https://api.github.com/orgs/github" },
  { "login": "octo-org",   "id": 583231, "url": "https://api.github.com/orgs/octo-org" }
]
```

That captured shape is what makes the result easy to use next. A following block can now reach into it - for example, the first organization's login is the result's first item's login property - and the Expression Editor offers those names for you because the Test run showed it the real structure. The payoff: one block turned a public API into structured data your flow can act on.

## Configuration

| Field | Description |
| --- | --- |
| URL | Required. The full web address to send the request to. It can be a fixed address or an expression that builds the address from earlier values. |
| HTTP Method | What you want to do at that address: GET reads, POST creates, PUT and PATCH update, DELETE removes, HEAD checks. Defaults to GET. |
| Body | The data you are sending with the request, usually JSON. Used by methods that write, such as POST, PUT, and PATCH; a GET typically has none. |
| Query | Extra parameters appended to the URL, such as a search term, a page number, or a filter the service understands. |
| Headers | Named values sent alongside the request, each a Name and a Value. Most often used for authentication (an API key, a Bearer token, or Basic credentials) and to declare the content type. |

## Behavior

- Sends one request to the configured address and exposes the response body as the result.
- Running the block in Test Mode captures the real response shape so later blocks can reference its fields.

## Things to watch for

- The result is only the response body - the data the service sent back. The status code and the response headers are not handed to you separately, so if you need to know whether a call succeeded, check for a value the body itself contains.
- Before you reference the result in later blocks, run this block once with Run Block in Test Mode. That sends the real request and captures the actual shape of the response, so the Expression Editor can offer you the right field names. Until then, downstream blocks only have a placeholder to work from.
- Authentication usually travels in a Header. If a call comes back rejected, the first thing to check is whether the right auth header (an API key, a Bearer token, or Basic credentials) is present and correct.

## Related

- [Custom Cloud Code](custom-cloud-code.md)
- [Handle Error](handle-error.md)
- expression-editor
