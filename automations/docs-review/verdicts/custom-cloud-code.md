# Gate verdict — reference/custom-cloud-code.md

- **Date:** 2026-08-14
- **Gate verdict:** `ship` (docs-content-review, final run wf_7c9c4d54 — fourth gate round this
  session; the ship punch-list of minors/nits was applied immediately after, per the reviewer's
  own fixes, and regenerated)
- **doclint:** 0 errors / 0 warnings (page-level)
- **Trigger:** release 1.0.13 (FR-3102) replaced the Custom Cloud Code runtime — the page's
  "no require, fetch, process, Buffer, crypto..." limitation, the 10-second cap, the bare-scalar
  bug, and the BigInt false-Success bug were all obsolete, and one documented behavior REVERSED.

## What was verified in-product this session (Documentation Flows, "Runtime Probe" flow)

Full runtime re-probe of the new pod-based environment:

- **Now available:** `fetch` (real network - live GET to api.github.com and POST to postman-echo
  with plain-object headers + string body, response `.json()`/`.text()`/`.headers.get()` all
  verified), `Buffer` (base64/hex), `crypto` (`randomUUID`, `getRandomValues`, `subtle` -
  SHA-256 digest run), real timers (`setTimeout`/`setInterval`/`clearTimeout`),
  `queueMicrotask`, `TextEncoder`/`TextDecoder`, `atob`/`btoa`, `structuredClone`,
  `URL`/`URLSearchParams`, `AbortController`.
- **Still absent:** `require`, `import` (dynamic import throws), `process`, all Node modules,
  and the `Headers`/`Request`/`Response`/`FormData`/`Blob`/streams/`WebSocket` constructors.
- **Limits changed:** the 10-second cap is GONE (12s busy-wait and 65s async wait complete);
  memory is the real ceiling (100MB of allocations fine, 200MB crashes the pod with
  "Cloud Code execution was interrupted...").
- **Bugs fixed, behaviors changed:** `return 42` → 42 (old "Invalid status code" bug gone);
  BigInt/circular returns now FAIL the block with "Return value is not JSON-serializable"
  (old silent false-Success gone); a bare-string `throw` keeps its message (was lost);
  an un-awaited promise rejection now CRASHES the environment (was documented as ignored —
  the claim is reversed in the page). Fresh env per run, sloppy mode, UTC/en-US/full ICU all
  re-confirmed; Map/Set/RegExp→{} and NaN/Infinity→null serialization unchanged.
- **Agent tool (FR-3227):** the attach flow re-verified — ((Manage Capabilities)) → ((Utils))
  now lists Custom Cloud Code (with File Reader and HTTP Request); the added tool shows in the
  agent block's Tools row and opens an "AI Tool" config panel whose helper text confirms the
  empty-is-agent-filled / filled-is-locked semantics. The old invented "tools drawer" phrasing
  was replaced.
- **New canvas screenshot** (`custom-cloud-code-canvas.png`): a real Ready flow built for the
  worked example — Fetch Orders (HTTP Request) → Count Open Orders (the example code, `orders`
  bound via the Expression Editor) → Any Open? (Condition on openCount INT > 0) → Yes →
  Save Open Order Ids (Set Variables ← openIds). Both upstream blocks Run-Block-tested.

## Gate history this session

revise (wf_87733e73) → ship (wf_366cf500) → revise (wf_590f91c6, new panel raised the
canvas-shot floor + example-data majors) → **ship (wf_7c9c4d54)**. Every work-list item from
every round was applied; the final ship's punch-list (7 minors/nits — chip placement, screenshot
intro position, alias bridge, Arguments location anchor, jargon swaps) was applied verbatim
after the verdict and the page regenerated.

## Open questions for Mark (non-blocking)

- The Code Editor's ((Open Code Editor)) button renders uppercase in the UI; chips render
  uppercase by design, so authored case matches on screen.
- known_bugs is now empty — both pre-1.0.13 entries are fixed and were moved to Behavior/
  Limitations as correct behavior.
