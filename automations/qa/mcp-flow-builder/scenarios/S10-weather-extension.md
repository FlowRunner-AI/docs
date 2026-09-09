# S10 — Weather (extension actions: Open-Meteo searchPlaces → getCurrentWeather, no account needed)

Driven 2026-09-02 03:03–03:11 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Given a city name, return its current temperature."

## Build (agent-chosen, 13 MCP calls + Console control)
list_extension_methods(openmeteo) → get_block_schema ×2 (params + sampleResult present for both) → add_block searchPlaces (params in config,
`{{Initial Data->city}}`, count 1 NUMBER) → add_block getCurrentWeather → add_block return-result → wire ×2 → resolve_dictionary(place,
"Berlin") → configure weather params (`{{City Matches->results.[0].latitude}}` / longitude, timezone auto) → configure return
{city, country, temperature `{{Weather->current.temperature_2m}}`, unit} → save_flow.
Flow B2E3B175-4323-4569-B520-D74713A16C4C, version 5E5216CA-1D7A-4786-90F4-4E4E569FD68F.

## Oracles
- **save_flow → status INVALID**, errorMessage `Block 'Find City' has an invalid configuration. 'Model name for Api Service action' is required…`
  while client-side issues were [] everywhere. **Blocked before O3.**
- **O1:** ELEMENT_LINK tokens with `subPathSegments [{key:results},{index:0},{key:latitude}]` — the `.[0]` syntax serialized correctly.
  Both openmeteo elements: hostType APP, modelName/lang absent. Control (SHARED telegram.sendMessage added then removed): modelName "v1", lang "JS".
  Control 2 (Console palette drop of the same block, autosaved): modelName null too.
- **O2:** S10-o2-canvas-invalid.png (first load showed "There are no blocks yet"; reload rendered 3 nodes with Not Ready badge).

## Findings
1. **Platform (not MCP): APP-hosted custom extension actions cannot be saved** — catalog definitions lack modelName/lang; server requires
   modelName. Reproduced from Console and MCP. Candidate Jira bug (search first).
2. resolve_dictionary works without a connection for a no-auth service (20 live Berlin matches). PASS.
3. get_block_schema for extension methods exposes `params` + `sampleResult` — the agent had everything needed (contrast F-S6-2).
4. `{{Initial Data->…}}` accepted inside add_block `params` for an extension ACTION.

## Teardown
Flow left INVALID with the Console-dropped 4th node; delete at end of phase. Not started.
