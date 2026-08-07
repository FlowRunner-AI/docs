# Gate verdict — build/ai-in-flows.md

- **Date:** 2026-08-06
- **Gate verdict:** `major-rework` (concept-page-review, run wf_78186554-2d2 — 4 lenses + red-team)
- **doclint:** 0 errors / 0 warnings (with `--warnings`)
- **Status after clearing:** every work-list item resolved in one consolidated pass (details below).
  Two earlier gate runs (wf_0bea7a83, wf_80157d31) silently reviewed shared-memory.md because the
  Workflow harness dropped `args` on named invocation — the registry script now throws on missing
  args instead of defaulting, and this run's agents were verified to have read the right page.
- **Interleaved with Mark's own review round** (6 points: read-syntax inline, page-level Related,
  ready-made section placement, lede roadmap, §0b scaffold, model-first shot) — all applied before
  the gate result landed; the gate work list was cleared on top of them.

## Gate summary (verbatim)

Not ready — though the spine is genuinely strong (value-first lede, one coherent support-desk
story, six real-scenario screenshots that all match their pixels), two blockers gate it: the page
has no PLATFORM-REVIEW-LEDGER.md section, and the AI QUESTION section teaches runtime behavior the
page's own exploration log proves fails on every run (the 6-arguments bug) [...] The remaining
theme is show-the-read discipline plus a short verify-in-product list. Red-team surfaced two
candidate NEW rules: (1) never ship a worked example for a feature the author has proven currently
fails without the product owner's explicit call; (2) a page-wide "every X on this page" claim must
be verified on every surface the page's own roadmap enumerates.

## Work list and resolutions

| # | Sev | Item | Resolution |
|---|-----|------|-----------|
| 0 | blocker | AI QUESTION teaches a proven-failing operation | **Mark's explicit decision (2026-08-06): "Write it as designed + you file the bug."** RESOLVED 2026-08-07: the fix landed and both exits were verified live (Yes: refund message → Flag For Refund Team, Success `{"conditionResult": true}`; No: routine question → Mark As Routine); shot recaptured with the real result. No caveat remains. |
| 1 | blocker | No ledger section | Added — see PLATFORM-REVIEW-LEDGER.md "AI in Flows". |
| 2 | major | Transform read-HOW delegated | Delegating sentence cut; the example now shows the read: Look Up Order's URL "ends in the {{Extract Order Number Result}} pill". |
| 3 | major | Agent output not shown; flow dead-ended | Send Reply (HTTP Request, POST to helpdesk) wired into the real flow, Body = bound {{Draft Reply Result->output}} pill picked from the run's recorded properties in the EE "Select property" dialog (pixel evidence of `output`). Shot recaptured with all three nodes, read back. Reply-read paragraph moved after the shot; `output` now code-formatted. |
| 4 | major | "Every AI step" over-claim | Verified in-product: OpenAI Speech to Text action uses its own "Shared Extension" Configure connection, not the model/key pattern. Claim scoped to "the AI blocks and operations on this page"; exception sentence added. |
| 5 | minor | Memory toggle unnamed + contrast tail | Rewritten naming ((Messages History)); tail cut. Control was already in the exploration log (panel drive). |
| 6 | minor | Capabilities enumeration mismatch | Rewritten as a bulleted list matching the observed groups (extensions, flows, Knowledge Bases, Shared Memory, utilities) + conditional MCP sentence ("with an MCP server registered ... its tools join the list"). |
| 7 | minor | Key-fields shot context-free | Kept deliberately: the AI Model/AI API Key pair recurs identically on all four surfaces, so a block-specific panel header would wrongly bind the shot to one block. Trade-off recorded here + ledger. |
| 8 | minor | Alias named before its example | Reply-read paragraph moved after the example + shot (with #3). |
| 9 | minor | Boundary drawn twice (X-vs-Y) | Second sentence cut; its facts folded into the first ("fetch knowledge, take an action, carry a conversation"). |
| 10 | minor | AI QUESTION opener mechanics-first + back-reference | Reopened on the judgment-call need; route rephrased functionally ("[Yes/No Branching] covers building on them"). |
| 11 | minor | Unpilled block parentheticals | All three pilled (Transform Data, Condition, AI Router). |
| 12 | minor | Lede frame doesn't cover ready-made actions | Axis recast as "how much of the job the model gets", five items in page order. |
| 13 | minor | Manage Capabilities window not shown | Conscious altitude choice: the window shot lives on the AI Agent reference (ai-agent-capabilities.png); Related routes there. Recorded in ledger. |
| 14 | minor | Chip case MANAGE CAPABILITIES | Verified: button textContent "Manage Capabilities", uppercased by CSS — title-case chip kept, consistent with the Mark-approved AI Agent reference. |
| 15 | minor | Per-provider setup filtering unverified | Claim reworded to what is verified: "the field offers your saved setups" (filtering claim dropped; only one provider's setup exists to test with). |
| 16 | minor | Marketplace link unverified | Fetched live: resolves, heading "AI & LLMs", 150 integrations / 2,169 actions (Anthropic Claude, OpenAI, Google Gemini, Mistral, Groq...). Logged in the page comment. |
| 17 | nit | Bare placeholder string | Quoted: reads "Select model first". |
| 18 | nit | Duplicate section closes | Transform close reworded ("Fields and options live in..."). |

## Candidate new rules (encoded in VOICE.md 2026-08-06 entries, pending Mark's confirmation)

1. Never ship a worked example for a feature the author has proven currently fails, and never
   compose a screenshot's state to sidestep a logged failure — unless the product owner explicitly
   decides ship-pending-fix, and that decision is recorded in the ledger and the handoff.
2. A page-wide "every X on this page" claim must be verified on every surface the page's own
   roadmap enumerates; the lede's organizing frame must cover every section it promises.
