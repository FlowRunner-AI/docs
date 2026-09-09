# S6 — HTTP request with error handler

Driven 2026-09-02 02:56–02:58 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Call a URL and, if it fails, return {error:true, message}; otherwise return ok."

## Build (10 calls)
http-request "Call Service" (GET, url `{{Initial Data->url}}`) → plain wire to error-handler "On Failure" and to return-result "Success";
error-handler → return-result "Failure" {error `{{Yes}}`, message `{{Failure Details->message}}`, code `{{Failure Details->code}}`}.
Flow E4B6721D-34A7-44E3-8FAA-59A68B13E6BA, version CC21FE7A-E662-4D0E-97EB-241DEE593A28.

## Oracles
- **O1:** Call Service.nextElementIds = [Success], metaInfo.onFailElemId = On Failure (the plain wire was classified as the failure path,
  as the readme promises); valid=true; LIVE. PASS.
- **O2:** S6-o2-canvas.png.
- **O3:** POST url=httpbin /status/500 → `{"code":null,"error":true,"message":""}` (handler path, empty details);
  /status/200 → `{"ok":true,"statusCode":null}` (success path; my `statusCode` reference was a guess — see F-S6-2);
  unreachable host → `{"code":28082,"error":true,"message":"The URL address … is incorrect or does not exist."}`. Routing PASS.

## Findings
1. F-S6-2 No sampleResult for http-request → agent cannot know the result shape; wrong path references pass validation and yield null.
2. F-S6-1 HTTP 5xx reaches the handler with code null / message "" (engine; verify against handle-error docs before filing).
3. F-S6-3 Default saveToVariable prefilled on a fresh HTTP block (cosmetic).

## Teardown
stop_flow(CC21FE7A…). Flow kept for end-of-phase deletion.
