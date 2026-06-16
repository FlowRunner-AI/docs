<!-- GENERATED FILE — do not edit. Source: block-knowledge/custom-cloud-code.yaml. Regenerate: make refgen -->
# Custom Cloud Code

Run custom JavaScript inline as a flow step. Receives named Arguments as top-level variables and returns an object that becomes the block's result.
## How it works

A locked-down JS sandbox, not Node. Think "pure function": inputs via Arguments, value out via `return`. External data must be fetched by an upstream block (e.g. HTTP Request) and passed in as an Argument.
## When to use it

Custom data shaping/logic no built-in block covers; glue between blocks. NOT for I/O — the sandbox has no network/file access (fetch via an upstream block instead).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Open Code Editor | button |  | Opens the modal (Arguments pane + JS editor). |
| Arguments | repeatable name+expression |  | Each argument becomes a top-level variable in the code; value is static or an expression referencing prior block results / Initial Data. |
| Reference Result Data As | alias |  | Alias for the returned object, referenceable downstream. |
## Behavior

- async/await + Promises supported and awaited before result capture.
- A returned Promise is awaited and unwrapped.
- Uncaught throw of an Error -> block status Error, message = error.message.
- throw of a non-Error primitive -> Error but empty message (value lost) — always throw new Error().
- Arguments arrive as native typed JS values (arrays/objects/numbers/null), no stringification.
- Floating (un-awaited) promise rejection is ignored; block returns normally.
## Things to watch for

- V8 isolate ~ES2023, NOT Node: no require/fetch/process/Buffer/crypto/setInterval/btoa/structuredClone.
- Server timezone UTC; locale en-US; full ICU present.
- Result is JSON.stringify'd: Map/Set/RegExp -> {}; NaN/Infinity -> null; undefined/functions/Symbols dropped.
- Non-strict (sloppy) mode; fresh isolate per run — no state persists between runs/instances.
- 10s execution timeout; ~400MB allocation OK; deep recursion -> RangeError.
## Related

- expression-editor
- [HTTP Request](http-request.md)
- [Handle Error](handle-error.md)
