# TUTORIAL-MAP.md - the program's traceability matrix

The single machine- and human-readable source for every training unit. Jobs:
1. **Production tracking** - the Status column: `planned | scripted | recorded | published | needs-rerecord`.
2. **Docs-to-lesson mapping** - a docs page change greps this file to find affected units.
3. **Map generation** - `map-data.json` for the Flowland Map is generated from this file at build time; it is never hand-authored.

Rules: codes renumber freely until a unit enters production and FREEZE once its script is written; later additions append. Every row keeps its Sources and Surfaces current - a row whose sources changed goes to `needs-rerecord` until triaged. The Video column is filled as lessons publish.


## FR-101 - FlowRunner Foundations

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-101.1.1 | Your first automation, in one sitting | 12 | learn/quickstart.md (compressed); Flowland Contact page | planned | |
| FR-101.2.1 | Meet Flowland - and the work you are about to hand to a flow | 5 | index.md | planned | |
| FR-101.2.2 | The workshop: your workspace and the Flow Editor | 6 | platform/workspace.md; build/flow-editor.md | planned | |
| FR-101.2.3 | Fifty inquiries at once: flows, instances, and why they never collide | 6 | learn/concepts/flows-and-instances.md; learn/concepts/blocks.md | planned | |
| FR-101.2.4 | Something happened at the shop: triggers | 4 | learn/concepts/triggers.md | planned | |
| FR-101.3.1 | Create the flow and give the website somewhere to post | 6 | learn/quickstart.md (steps 1-3) | planned | |
| FR-101.3.2 | See exactly what the customer sent | 5 | learn/quickstart.md (step 4) | planned | |
| FR-101.3.3 | Draft the reply once: the template in a variable | 5 | learn/quickstart.md (step 5); learn/concepts/variables.md | planned | |
| FR-101.3.4 | Personalize every reply: filling the template from submitted data | 8 | learn/quickstart.md (steps 6-9) | planned | |
| FR-101.3.5 | Send it: the reply goes out, end to end | 5 | learn/quickstart.md (step 10) | planned | |
| FR-101.4.1 | Try it without customers: the Test Monitor | 7 | run/testing.md | planned | |
| FR-101.4.2 | Ready, then LIVE | 5 | run/running-flows.md; build/flow-editor.md | planned | |
| FR-101.4.3 | Watch the shop run | 6 | run/running-flows.md; run/inspecting-a-run.md | planned | |
| FR-101.4.4 | Prove it - and name Your One Process | 6 | learn/quickstart.md; Flowland Contact page; training-owned | planned | |

## FR-102 - Working with Data

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-102.1.1 | What every step leaves behind: the pool of results | 6 | build/data-and-variables/passing-data.md; learn/concepts/blocks.md | planned | |
| FR-102.1.2 | Reading an order without fear: JSON in plain language | 7 | (training-owned; grounded in learn/concepts/expressions.md and Flowland /api/shop/orders) | planned | |
| FR-102.1.3 | Compose any value: the Expression Editor | 8 | learn/concepts/expressions.md | planned | |
| FR-102.2.1 | Keep it for later: variables through the life of a run | 7 | learn/concepts/variables.md; build/data-and-variables/holding-values.md | planned | |
| FR-102.2.2 | A running total: building a value up as the run goes | 5 | build/data-and-variables/holding-values.md | planned | |
| FR-102.2.3 | The export nobody loves: reshaping the legacy orders | 8 | build/data-and-variables/reshaping-data.md; reference/transform-data.md; Flowland /api/shop/legacy/orders | planned | |
| FR-102.3.1 | A value the next run needs: Shared Memory | 6 | build/data-and-variables/across-runs.md; learn/concepts/shared-memory.md | planned | |
| FR-102.3.2 | Counting customers across runs: the counter pattern | 8 | learn/concepts/shared-memory.md; reference/shared-memory-put.md / -read.md / -delete.md | planned | |
| FR-102.3.3 | Capstone: the order digest | 8 | course material; Flowland shop APIs | planned | |

## FR-103 - Controlling the Flow

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-103.1.1 | Refund or reply? Yes/no branching with Condition | 7 | build/flow-control/branching.md; reference/condition.md | planned | |
| FR-103.1.2 | Two checks at once: compound conditions and evaluation order | 5 | build/flow-control/branching.md | planned | |
| FR-103.1.3 | Sort inquiries three ways: routing on a value | 7 | build/flow-control/routing.md; reference/value-router.md | planned | |
| FR-103.2.1 | Every item in the order: working through a list | 8 | build/flow-control/collections.md; reference/list-iterator.md | planned | |
| FR-103.2.2 | Keep checking until it is ready: Repeat and the failsafe | 7 | build/flow-control/repeating.md; reference/repeat.md | planned | |
| FR-103.2.3 | Found it - stop looking: Break and the iteration number | 5 | build/flow-control/repeating.md; reference/break.md | planned | |
| FR-103.3.1 | Three lookups at once: parallel branches and Synchronize | 8 | build/flow-control/parallel.md; reference/synchronize.md; reference/actions-group.md | planned | |
| FR-103.3.2 | Give it a moment: deliberate delays | 4 | build/flow-control/waiting.md; reference/wait.md | planned | |
| FR-103.4.1 | A flow stops at the first failure - unless you catch it | 7 | build/flow-control/error-handling.md; reference/handle-error.md; Flowland Inventory console | planned | |
| FR-103.4.2 | Read the error, retry with backoff | 7 | build/flow-control/error-handling.md; reference/error-handling-concept.md | planned | |
| FR-103.4.3 | Capstone: the inquiry-triage pipeline | 10 | course material; Flowland site | planned | |

## FR-104 - Connecting to the Outside World

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-104.1.1 | Call anything: connector blocks first, HTTP Request for the rest | 8 | build/integrations/calling-a-service.md; reference/http-request.md | planned | |
| FR-104.1.2 | Keys in one drawer: API keys and OAuth connections | 6 | platform/api-keys.md; platform/oauth-connections.md | planned | |
| FR-104.1.3 | A front door for people: Forms | 7 | platform/forms.md | planned | |
| FR-104.2.1 | Answer the caller: Return Result | 6 | build/integrations/returning-a-result.md; reference/return-result.md | planned | |
| FR-104.2.2 | Start a flow from anywhere: the Call Flow API | 8 | api/call-flow-blocking.md; api/call-flow-nonblocking.md; api/block-results.md | planned | |
| FR-104.3.1 | Wait for the manager: External Callbacks | 8 | build/flow-control/external-callbacks.md; reference/external-callback.md; Flowland Approvals Desk | planned | |
| FR-104.3.2 | Learn the payload, filter the calls | 7 | build/flow-control/external-callbacks.md; api/activating-a-trigger.md | planned | |
| FR-104.3.3 | Wait for several things at once: Triggers Group | 5 | reference/triggers-group.md | planned | |
| FR-104.4.1 | Build once, reuse everywhere: subflows | 7 | learn/concepts/subflows.md; reference/subflow.md | planned | |
| FR-104.4.2 | One process starts another: Call Flow between flows | 6 | build/integrations/running-another-flow.md; reference/call-flow.md | planned | |
| FR-104.4.3 | A thousand new blocks: MCP servers and marketplace actions | 7 | platform/mcp-servers.md; build/integrations/custom-actions.md | planned | |
| FR-104.4.4 | Make it real: swap Flowland for your own services | 7 | build/integrations/calling-a-service.md; platform/api-keys.md; platform/oauth-connections.md | planned | |
| FR-104.4.5 | Capstone: the quote-approval workflow | 10 | course material; Flowland site | planned | |

## FR-105 - AI-Powered Automation

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-105.1.1 | Before any AI step: a model and your key | 5 | build/ai-in-flows.md; platform/api-keys.md | planned | |
| FR-105.1.2 | Describe the change: AI transforms | 6 | build/ai-in-flows.md | planned | |
| FR-105.1.3 | Questions rules cannot answer: AI questions and AI routing | 7 | build/ai-in-flows.md; reference/ai-router.md; Flowland Contact page examples | planned | |
| FR-105.2.1 | Add the agent and give it its job | 8 | learn/quickstart-agent.md (steps 1-6); reference/ai-agent.md | planned | |
| FR-105.2.2 | Hand it tools - and watch it choose | 8 | learn/quickstart-agent.md (steps 7-9); reference/flows-as-agent-tools-concept.md; Flowland /api/shop/orders | planned | |
| FR-105.2.3 | One step among many: using the agent's answer in the flow | 5 | learn/quickstart-agent.md; build/ai-in-flows.md | planned | |
| FR-105.3.1 | Ground it in the shop's own policies: Knowledge Bases | 8 | reference/knowledge-bases-concept.md; reference/knowledge-base-add-document.md; Flowland knowledge pack | planned | |
| FR-105.3.2 | Keep the knowledge fresh: maintaining a KB from a flow | 6 | reference/knowledge-base-list-documents.md; -delete-document.md; -delete-by-filter.md | planned | |
| FR-105.3.3 | It remembers Alice, not Bob: agent memory and per-user memory | 7 | reference/flow-memory-concept.md; reference/per-user-memory-concept.md; Flowland chat widget | planned | |
| FR-105.3.4 | Capstone: the accountable support agent | 10 | course material; Flowland site | planned | |

## FR-106 - Running and Operating Flows

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-106.1.1 | Change a live flow without breaking it: versions | 6 | manage/flows.md; build/flow-editor.md; definitions.md | planned | |
| FR-106.1.2 | Run it every night: scheduling and the execution policy | 7 | reference/flow-scheduling-concept.md; reference/start-scheduled-runs.md; -stop-.md | planned | |
| FR-106.2.1 | Order #4 breaks the flow: find the failure | 7 | run/monitoring.md; Flowland Order Replayer | planned | |
| FR-106.2.2 | Anatomy of a failed run | 7 | run/inspecting-a-run.md | planned | |
| FR-106.2.3 | Fix, re-version, switch LIVE, replay to prove it | 7 | manage/flows.md; run/testing.md; Flowland Order Replayer | planned | |
| FR-106.2.4 | The shop at a glance - at honest scale | 6 | run/monitoring.md | planned | |
| FR-106.3.1 | Do the orders match the payments? Reconciliation | 8 | run/monitoring.md; Flowland /api/shop/payments; /seed/KNOWN-MISMATCHES.md | planned | |
| FR-106.3.2 | Paid but never shipped: the exception report | 7 | course material; Flowland shop datasets | planned | |
| FR-106.4.1 | Four business hours: SLA goals and calendars | 6 | platform/sla-goals.md; platform/compliance-and-security.md | planned | |
| FR-106.4.2 | Who did what: audit log, compliance, Panic Mode | 5 | platform/compliance-and-security.md | planned | |
| FR-106.4.3 | The team and the bill | 6 | manage/team.md; manage/workspace-settings.md; manage/billing.md | planned | |
| FR-106.4.4 | Capstone: the operations drill | 9 | course material; Flowland site | planned | |

## FR-210 (developer track) - FlowRunner for Developers

| Code | Title | Min | Sources | Status | Video |
|---|---|---|---|---|---|
| FR-210.1.1 | Flows are processes, instances are executions | 6 | index.md; learn/concepts/flows-and-instances.md; learn/concepts/blocks.md | planned | |
| FR-210.1.2 | The editor and the Test Monitor, at speed | 6 | build/flow-editor.md; run/testing.md | planned | |
| FR-210.2.1 | Ten blocks or fifteen lines: your first code block | 8 | learn/quickstart-code.md; reference/custom-cloud-code.md | planned | |
| FR-210.2.2 | Bind data in, expose results out | 6 | learn/quickstart-code.md; reference/custom-cloud-code.md; learn/concepts/expressions.md | planned | |
| FR-210.2.3 | Generate it: AI-written block code | 6 | reference/custom-cloud-code.md; training-owned material | planned | |
| FR-210.2.4 | When blocks beat code | 6 | build/ai-in-flows.md; reference/error-handling-concept.md; build/flow-control/waiting.md | planned | |
| FR-210.3.1 | Write a custom action: your code as a palette block | 8 | extend/index.md + extend/getting-started.md; build/integrations/custom-actions.md | planned | |
| FR-210.3.2 | Write a custom trigger | 7 | release documentation (staging capability) | planned | |
| FR-210.3.3 | Reuse and share: your blocks across flows and teams | 6 | release documentation (staging capability) | planned | |
| FR-210.4.1 | The whole API in one lesson: launch, results, activate | 7 | api/call-flow-blocking.md; api/call-flow-nonblocking.md; api/block-results.md; api/activating-a-trigger.md | planned | |
| FR-210.4.2 | Async without infrastructure | 7 | build/flow-control/external-callbacks.md; reference/flow-scheduling-concept.md; reference/error-handling-concept.md | planned | |
| FR-210.4.3 | MCP and agents: your services and flows as tools | 6 | platform/mcp-servers.md; reference/flows-as-agent-tools-concept.md | planned | |
| FR-210.4.4 | Capstone: build it your way | 9 | course material; Flowland site | planned | |

## Flowland Playbook

| Code | Recipe | Skills explained in | Flowland surfaces | Starter flow | Status | Video | Written tutorial |
|---|---|---|---|---|---|---|---|
| QW-01 | Turn any form into an automated reply, in 15 minutes | none | Contact page + starter flow import | /flows/QW-01.flow (TBD) | planned | | |
| QW-02 | AI drafts your support replies, in 10 minutes | none | Agent quickstart (product); chat widget once site Phase C lands | /flows/QW-02.flow (TBD) | planned | | |
| QW-03 | When an order lands, notify yourself: event-driven in 10 minutes | none | Checkout (site Phase B) + starter flow import | /flows/QW-03.flow (TBD) | planned | | |
| PB-01 | Customer 360: one view of a customer across orders and payments | FR-102 | Static orders, payments, customers APIs | /flows/PB-01.flow (TBD) | planned | | |
| PB-02 | Find your VIPs: lifetime value and repeat-purchase tagging | FR-102 | Static customers/orders | /flows/PB-02.flow (TBD) | planned | | |
| PB-03 | Rescue the legacy order export | FR-102 | Legacy endpoint | /flows/PB-03.flow (TBD) | planned | | |
| PB-04 | Process only what is new: incremental sync with checkpoints | FR-102 | Static orders (timestamps) | /flows/PB-04.flow (TBD) | planned | | |
| PB-05 | Route every inquiry to the right team | FR-103 | Contact page | /flows/PB-05.flow (TBD) | planned | | |
| PB-06 | Qualify the lead: is this inquiry sales-worthy? | FR-103 | Contact page (wholesale examples) | /flows/PB-06.flow (TBD) | planned | | |
| PB-07 | Validate the order before you trust it | FR-103 | Checkout, replay orders | /flows/PB-07.flow (TBD) | planned | | |
| PB-08 | Is it in stock? A check that survives a flaky service | FR-103 | Inventory console | /flows/PB-08.flow (TBD) | planned | | |
| PB-09 | Check five SKUs at once | FR-103 | Inventory API | /flows/PB-09.flow (TBD) | planned | | |
| PB-10 | Partially in stock: hold, split, or cancel? | FR-103 | Inventory API (seeded zero/low SKUs) | /flows/PB-10.flow (TBD) | planned | | |
| PB-11 | Ship from the right warehouse | FR-103 | Inventory warehouses | /flows/PB-11.flow (TBD) | planned | | |
| PB-12 | Free shipping, or not? Policy logic in the quote flow | FR-103 | Checkout quote flow | /flows/PB-12.flow (TBD) | planned | | |
| PB-13 | The $500 order: manager approval above a threshold | FR-104 | Checkout + Approvals Desk | /flows/PB-13.flow (TBD) | planned | | |
| PB-14 | Payment failed - recover without losing the order | FR-104 | External Systems Console (payments) | /flows/PB-14.flow (TBD) | planned | | |
| PB-15 | The same webhook arrived twice | FR-104 | Console 'Send duplicate' | /flows/PB-15.flow (TBD) | planned | | |
| PB-16 | Track the package: react to carrier events | FR-104 | Console shipping tab | /flows/PB-16.flow (TBD) | planned | | |
| PB-17 | The shipment that never arrived | FR-104 | Console 'Stop sequence' | /flows/PB-17.flow (TBD) | planned | | |
| PB-18 | 'Delivered' before 'in transit': out-of-order events | FR-104 | Console 'Send out of order' | /flows/PB-18.flow (TBD) | planned | | |
| PB-19 | Do not fulfill until payment AND approval | FR-104 | Console + Approvals Desk | /flows/PB-19.flow (TBD) | planned | | |
| PB-20 | The abandoned cart follow-up | FR-104 | Checkout abandon control | /flows/PB-20.flow (TBD) | planned | | |
| PB-21 | Read the customer's mind: AI intent classification | FR-105 | Contact page canned examples | /flows/PB-21.flow (TBD) | planned | | |
| PB-22 | The return request: policy + AI judgment + approval + refund | FR-105 | Return Request page, Approvals Desk, payments | /flows/PB-22.flow (TBD) | planned | | |
| PB-23 | Moderate the reviews: normal, spam, or needs a human? | FR-105 | Review page + static reviews | /flows/PB-23.flow (TBD) | planned | | |
| PB-24 | The agent that knows when to stop: escalation to a human | FR-105 | Chat widget + Approvals Desk | /flows/PB-24.flow (TBD) | planned | | |

## Program-level units

| Code | Unit | Depends on | Status |
|---|---|---|---|
| RTS-01 | Run the Shop capstone (passing bar: end-to-end green + 5 replay defects handled + all seeded mismatches found) | FR-106 published | planned |
| DEMO-01 | House demo flow (Contact page demo mode) | FlowRunner workspace + site Phase A | planned |
