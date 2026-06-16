<!-- GENERATED FILE — do not edit. Source: block-knowledge/http-request.yaml. Regenerate: make refgen -->
# HTTP Request

Call an external HTTP API (GET/POST/PUT/PATCH/DELETE/HEAD).
## How it works

A fetch() block. Configure URL/method/headers/body/query; the response body becomes the result.
## When to use it

Integrate with any web service/API not covered by an extension.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| URL | expression | Yes |  |
| HTTP Method | dropdown |  |  |
| Body | expression |  | Request payload (JSON/XML/text). |
| Query | expression |  |  |
| Headers | repeatable Name/Value |  | e.g. Content-Type, Authorization (API key / Bearer / Basic). |
| Reference Result Data As | alias |  |  |
## Behavior

- Performs the HTTP call and exposes the response body as the result.
- Test Mode run captures the actual response structure for downstream referencing.
## Things to watch for

- Returns the response BODY; status/headers must be inferred from the body or are not exposed.
- Use Run Block (Test Mode) to capture the real result shape for the Expression Editor.
## Related

- [Custom Cloud Code](custom-cloud-code.md)
- [Handle Error](handle-error.md)
- expression-editor
