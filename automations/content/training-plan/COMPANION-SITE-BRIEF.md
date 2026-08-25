# FlowRunner Training Companion Site - Build Brief (v4)

**Working name:** Flowland Seed Co. - a small fictional online seed shop (flower and vegetable seeds). Keep the name a single constant. Theme rationale: seed/flower imagery is abundant as stock photography with no copyright friction. Product images are supplied separately by the owner; build against `/public/img/products/` with the naming convention `{sku}.jpg` and a neutral placeholder for missing files.

**What this is:** an open-source site that plays the *entire periphery* for FlowRunner training tutorials - a small business ecosystem exposing nearly every general-purpose automation pattern. Learners never build test harnesses, fake APIs, or webhook receivers. The learner's time goes 100% into FlowRunner. The training arc it serves: by the end of the program, the learner has automated this entire business ("Run the Shop" capstone; see the training plan's two-layer architecture and Flowland Playbook).

**What this is not:** a marketing or demo asset, a FlowRunner-branded property, or a general webhook-testing tool. Training only. No accounts, no real payments, no real emails.

**Stack (decided):** pure HTML/JS front end (no framework, no build step) on Cloudflare Pages + Pages Functions for all dynamic behavior. Durable Objects for per-sandbox state and delayed callbacks (DO alarms). Verify current free-plan limits for DO/SQLite before finalizing; if a feature requires a paid plan, say so in the README rather than silently depending on it.

**Site structure:** two zones. The **shop** (storefront, product pages, cart/checkout, contact, return request, reviews) - what a customer would see. The **back office** (Approvals Desk, External Systems Console, Inventory Service Console, Order Replayer) - where the learner plays shop staff or an external system. Both zones share the Tutorial Assets panel (Section 2.2).

---

## 1. Product principles

1. **Realism is the quality bar.** Payloads, latencies, and failure modes resemble what learners meet at work: Stripe/Shopify-like JSON shapes, amounts in cents, ISO-8601 timestamps, paginated lists, occasional 429s and timeouts. Nothing that looks like `{"foo": "bar"}`.
2. **Functional areas are URLs, not subsystems.** A new business area (shipments, returns, reviews, suppliers) is, wherever possible, a new static dataset endpoint plus at most a small page or a console tab reusing existing machinery - never a new subsystem.
3. **Static variety over mutable state.** Scenarios that need "an order in status X" get a dataset containing orders in every status, not orders that change state. Static datasets carry deliberately seeded inconsistencies (mismatches, defects) so reporting, reconciliation, and debugging lessons have real material. Per-learner mutable state exists only where isolation is required: inventory failure config, approvals, registered payments.
4. **Configuration lives on the page that uses it.** No separate setup page a learner can miss. Every page carries the Tutorial Assets panel; a learner can land directly on any page from a lesson link and configure everything right there.
5. **One consistent teaching surface.** The Tutorial Assets panel is always in the same place and always means the same thing: everything for and about the tutorial lives there. Learners are trained on this convention from lesson one.
6. **Fail on purpose, deterministically when asked.** Failure injection must be reproducible: a lesson says "set Inventory to fail twice then succeed" and every learner sees identical behavior.
7. **The site maps to the curriculum and the Playbook.** Every page and dataset exists because a course lesson or Playbook recipe needs it. `TUTORIAL-MAP.md` maintains the mapping.

## 2. Sandbox and the Tutorial Assets panel

### 2.1 Sandbox (stateful features only)
- Needed only for back-office services (inventory config, approvals, registered payments/events). On the first request that needs state, the front end calls `POST /api/sandbox` and receives `{ "token": "..." }` (10 chars, unambiguous alphabet). Stored in `localStorage` as `fr_sandbox_token`, shown in the back-office header with a "Reset sandbox" control.
- All per-learner server state is keyed by token. TTL: 7 days after last write. Nothing is permanent.
- Sandbox creation is invisible; there is no setup page.

### 2.2 Tutorial Assets panel (the standard component)
A collapsible panel rendered in the same position on every page (shop and back office). Its name and position are a convention the training teaches explicitly: *this panel always holds everything for and about the tutorial.* Contents per page, in fixed order:

1. **Connect your flow** - the URL field(s) this page uses, each with a one-line hint of where in FlowRunner to copy the URL from and a link to the matching lesson. Values persist in `localStorage` (keys below) and prefill wherever the same key is used. Status chip per field: **Not connected** / **Connected** / **Last call: 200 OK, 340 ms**. A **Send test** button where meaningful. Client-side validation mirrors server rules (Section 5): `https://` only, no IP-literal hosts, plain-language errors.
2. **APIs on this page** - the endpoints this page's exercises use, with copy buttons and sample payloads. (On the storefront this is the shop API list; there is no separate API explorer page.)
3. **Downloads** - where relevant (knowledge pack, sample payloads).
4. **Activity** - the transparency log: every HTTP exchange this page performed (method, URL, request headers/body, response status/headers/body), newest first, copy-as-curl, bodies truncated at 64 KB.

If the learner triggers an action while a required URL is missing, do not silently fail: expand the panel, focus the field, explain, and run the action after they save.

`localStorage` keys: `fr_sandbox_token`, `fr_url_contact_trigger`, `fr_url_checkout_trigger`, `fr_url_shipping_quote`, `fr_url_support_agent`, `fr_url_returns_trigger`, `fr_url_review_trigger`, `fr_url_events_callback`.

### 2.3 Common conventions
- Outbound calls to learner URLs: `Content-Type: application/json`, 10 s timeout (30 s for the two blocking calls: shipping quote, support chat), no redirects.
- Site API errors: `{ "error": { "code": "string", "message": "human readable" } }` with correct HTTP status.
- No auth headers anywhere; FlowRunner's HTTP Request block can call every endpoint bare.
- All outbound webhooks/callbacks carry `X-Signature: sha256=<HMAC-SHA256 of raw body>` (key = sandbox token, or the literal string `static` for calls not tied to a sandbox) and `User-Agent: Flowland-TrainingSim/1.0 (+<repo URL>)`.
- All outbound events carry a stable `event_id` (`evt_` prefix). Duplicate sends reuse the same `event_id` - that is the point of the dedup lessons.

## 3. Scenario surfaces

Each scenario: **Story** (how the page and the learner's tutorial flow interact), **Page spec**, **API spec**.

### 3.1 Contact page - FR-101

**Story.** In FR-101 the learner builds the course's first flow: a form-submission trigger feeding an email reply. In FlowRunner they copy the trigger's address ("the address the form will post to" step in the quickstart). They open the Contact page, paste it into the Tutorial Assets panel's "Your FlowRunner trigger URL" field, fill the form as a customer asking about germination, and click Send. The site POSTs the submission to their trigger; their flow wakes up, fills the email template, and sends the reply. The Activity section shows the exact request their trigger received - the same payload they see as Initial Data inside FlowRunner. Later, the same form powers Playbook recipes: routing by topic, AI intent classification (the free-text message is written for it), and lead qualification.

**Page spec.**
- Realistic shop contact page. Form fields: Name (text, required), Email (email, required), Topic (select: `order`, `product`, `growing-advice`, `wholesale`, `other`), Message (textarea, required).
- Tutorial Assets panel: connect field bound to `fr_url_contact_trigger`; **Send test submission** button; a small set of canned example messages selectable for AI-classification recipes (a wholesale lead, an angry complaint, a vague question).
- Submit success state: "Sent - your flow received it (HTTP 200 in 340 ms)". Failure states distinguish timeout, connection refused, non-2xx (status + body excerpt).

**API spec.** Outbound only:
```json
{
  "type": "contact.submitted",
  "event_id": "evt_c81k2m",
  "submitted_at": "2026-08-24T17:41:03Z",
  "name": "Alice Nguyen",
  "email": "alice@example.test",
  "topic": "growing-advice",
  "message": "Do your poppy seeds need cold stratification before sowing?"
}
```

### 3.2 Shop data APIs - FR-102 / FR-103 / FR-106 (static, no token)

**Story.** The learner's flows read the business through these APIs: iterating orders (FR-102), aggregating for reports and reconciliation (FR-106 and Playbook recipes like Customer 360, VIP detection, exception reports), and normalizing the legacy export. URLs are static and identical for everyone: lessons print them literally, screenshots match the video, responses are edge-cacheable. The datasets deliberately contain the inconsistencies the operations recipes need to find.

**Page spec.** The storefront (product grid, product detail pages) doubles as the browsing surface; its Tutorial Assets panel carries the endpoint list, sample payloads, and query parameter documentation. No separate API page.

**API spec.** One fixed, versioned dataset committed to the repo (`/seed/`): ~40 products, ~120 orders, ~30 customers, plus companion datasets below. All list endpoints share the pagination conventions: `page` (default 1), `limit` (default 20, max 100), `sort`; headers `X-Total-Count` and RFC-5988 `Link`.

- `GET /api/shop/products` - seed packets:
```json
{
  "sku": "FLS-POPPY-ICE", "title": "Iceland Poppy", "species": "Papaver nudicaule",
  "category": "flower", "days_to_germinate": 14, "sow_season": ["early-spring", "fall"],
  "packet_size_grams": 0.5, "seeds_per_packet": 250, "price_cents": 449,
  "image_url": "/img/products/FLS-POPPY-ICE.jpg", "in_catalog": true
}
```
- `GET /api/shop/orders`, `GET /api/shop/orders/{id}` - filter `status` (`pending|paid|shipped|delivered|cancelled`). Statuses are distributed across the dataset so state-dependent recipes (cancellation windows, review requests) branch on real variety. Order shape:
```json
{
  "id": "ord_8h2k1x", "created_at": "2026-08-21T09:14:22Z", "status": "paid",
  "currency": "USD",
  "customer": { "id": "cus_ali01", "name": "Alice Nguyen", "email": "alice@example.test" },
  "shipping_address": { "line1": "482 Fern Hollow Rd", "city": "Missoula", "region": "MT", "postal_code": "59801", "country": "US" },
  "line_items": [ { "sku": "FLS-POPPY-ICE", "title": "Iceland Poppy", "quantity": 3, "unit_price_cents": 449 } ],
  "subtotal_cents": 1347, "shipping_cents": 599, "tax_cents": 97, "total_cents": 2043
}
```
- `GET /api/shop/customers` - id, name, email, orders_count, first_order_at, lifetime_value_cents (supports VIP/segmentation recipes without aggregation when the lesson wants a shortcut; the recipes that teach aggregation ignore it).
- `GET /api/shop/payments` - static payment records crossing the orders. **Seeded mismatches:** a few orders paid twice, a few paid-but-cancelled, a few shipped-but-unpaid. Fields: payment_id, order_id, amount_cents, status, method, processed_at. Reconciliation and exception-report recipes are built on these known defects, listed in `/seed/KNOWN-MISMATCHES.md`.
- `GET /api/shop/shipments` - static shipment records: shipment_id, order_id, carrier, status (`created|in_transit|delivered|delayed|lost`), events[] with timestamps. Includes mismatches (shipment for a cancelled order; delivered order with no shipment record).
- `GET /api/shop/reviews` - static product reviews: review_id, sku, customer_id, rating (1-5), text, submitted_at. Text written to span the moderation classes: normal, glowing, harsh-but-legitimate, spam, abusive - so classification recipes have ground truth (labels in `/seed/reviews-labels.md`, not exposed by the API).
- `GET /api/shop/returns` - static return requests in various states (`requested|approved|rejected|refunded`) with free-text reasons written for AI-interpretation recipes.
- `GET /api/shop/legacy/orders` - the same orders deliberately mangled for Transform Data lessons: flat denormalized rows, inconsistent key casing (`OrderID`, `customer_name`, `Total`), numbers as strings, dollars not cents, `MM/DD/YYYY` dates, nulls, line items as one semicolon-delimited string. Mangling rules fixed and documented.

### 3.3 Inventory Service Console - FR-103 (back office, token)

**Story.** The FR-103 error-handling lesson has the learner call an inventory check they *know* will fail, and survive it. In the back office they open the Inventory Service Console and click the lesson's preset ("Fail next 2 requests, then succeed"). In FlowRunner they wire HTTP Request -> Handle Error -> retry with backoff and watch attempt one fail, attempt two fail, attempt three succeed - reproducibly. The warehouse dimension powers fulfillment-routing recipes; low quantities in the dataset power low-stock alert and reorder recipes.

**Page spec.** Console shows: current failure profile, preset buttons labeled with lesson codes, manual controls, a live log of the last 20 requests to this sandbox's inventory endpoint (timestamp, outcome, injected behavior), and the tokenized endpoint URL in the Tutorial Assets panel.

**API spec.**
- `GET /api/{token}/inventory/{sku}` -> per-warehouse availability (quantities are static per dataset; the token scopes only the failure profile):
```json
{ "sku": "FLS-POPPY-ICE",
  "warehouses": [ { "code": "WEST", "quantity": 118 }, { "code": "EAST", "quantity": 0 } ],
  "total_quantity": 118 }
```
Unknown SKU -> 404, standard error shape. Some SKUs are deliberately zero or low in one or both warehouses (documented) for partial-availability and low-stock recipes.
- `GET/POST /api/{token}/inventory-config` body `{ "fail_next": 2, "timeout_next": 0, "rate_limit_next": 0, "fail_rate": 0.0, "latency_ms": 200, "latency_jitter_ms": 150, "malformed_next": 0 }` (all optional; POST merges). Deterministic `*_next` counters take precedence over `fail_rate` and decrement per request.
- Injected behaviors: 500 with realistic JSON body; 429 with `Retry-After: 5`; timeout mode responds after 35 s; malformed mode returns invalid JSON labeled `application/json`.
- One-off overrides via query params (`?fail_next=1`).

### 3.4 Checkout - FR-104

**Story.** Two FR-104 lessons meet here. First, the learner builds a *shipping quote* flow exposed through the blocking Call Flow API: it receives the cart, computes a price from total weight, and returns `{label, amount_cents, eta_days}` from a Return Result block - their own flow's answer renders inside a real checkout UI. Second, the learner builds an *order processing* flow with a trigger; placing an order delivers `order.created` to it, typically continuing into payments (3.6) and approval (3.5). Playbook recipes reuse the same page for shipping-method selection and free-shipping-policy logic (the quote flow decides), and the abandoned-cart recipe uses the panel's abandon control.

**Page spec.**
- Storefront cart drawer + checkout page with a fake customer identity (prefilled editable fields, labeled "test customer - not real").
- Panel connect fields: `fr_url_shipping_quote`, `fr_url_checkout_trigger`. Panel test controls include **Abandon cart**: sends a `cart.abandoned` event (cart contents, customer, `abandoned_at`) to the checkout trigger URL, immediately or with a chosen delay (10-300 s, DO alarm) for follow-up recipes.
- "Get shipping quote": blocking call, 30 s spinner. Success renders the quote line. A response not matching the expected shape renders raw (still success - realism over rigidity). Timeout/non-2xx: error state plus flat-rate fallback (`Standard - $5.99`) so checkout stays usable.
- "Place order": requires the trigger URL (missing-URL behavior per 2.2). Sends `order.created`, shows confirmation with order id.

**API spec.** Outbound only.
- Shipping quote request (POST, blocking, 30 s):
```json
{
  "type": "shipping.quote_requested",
  "destination": { "postal_code": "59801", "country": "US" },
  "line_items": [ { "sku": "FLS-POPPY-ICE", "quantity": 3, "packet_size_grams": 0.5 } ],
  "total_weight_grams": 1.5, "subtotal_cents": 1347
}
```
Expected (not enforced) response: `{ "label": "USPS Ground", "amount_cents": 599, "eta_days": 4 }`.
- Order event: the canonical order shape wrapped as `{ "type": "order.created", "event_id": "evt_...", "created_at": "...", "order": { ... } }`, `status: "pending"`, order id newly generated (`ord_` prefix).
- `cart.abandoned` event: `{ "type": "cart.abandoned", "event_id": "evt_...", "abandoned_at": "...", "customer": {...}, "line_items": [...], "subtotal_cents": ... }`.

### 3.5 Approvals Desk - FR-104 (back office, token)

**Story.** The learner's order flow must not ship a high-value order without a manager. In FlowRunner they add an External Callback block and, just before it, an HTTP Request that registers the approval with the site - passing a `callback_url` composed of the callback's address plus the execution id (the docs' "system accepts a callback address per request" pattern). They place a big order; the flow registers the approval and pauses. On the Desk, the learner plays the manager: Approve posts the decision to the callback URL and the paused instance resumes on the approved path. The same Desk serves every human-in-the-loop Playbook recipe: risky-order review, refund approval, human-approved AI actions, support escalation. Auto mode approves after a delay for solo async lessons.

**Page spec.**
- Desk lists this sandbox's approvals, newest first: title, details, requested_at, status (`pending/approved/rejected/expired`), Approve / Reject, optional comment. Polls every 5 s.
- Decided cards show callback delivery result ("Decision delivered - callback returned 200" or the failure), so a wrong execution id is diagnosable here.
- Auto-mode control: `manual` (default) / `auto-approve` / `auto-reject`, delay 5-300 s.

**API spec.**
- `POST /api/{token}/approvals` body `{ "title": "Approve order ord_8h2k1x ($20.43)", "details": "3 items, new customer", "callback_url": "https://...", "metadata": { } }` -> `201 { "approval_id": "apr_2f8k", "status": "pending" }`. `callback_url` validated per Section 5 at registration; invalid -> 422.
- `GET /api/{token}/approvals`, `GET .../approvals/{id}`.
- `POST /api/{token}/approvals/{id}/decision` body `{ "decision": "approved", "comment": "ok" }` (Desk UI; also directly callable for scripted lessons).
- On decision (manual, or auto via DO alarm), POST to `callback_url`:
```json
{
  "type": "approval.decided", "approval_id": "apr_2f8k", "decision": "approved",
  "approver": "Dana (Ops Manager)", "comment": "ok", "decided_at": "2026-08-24T18:02:11Z",
  "metadata": { }
}
```
- Pending approvals expire (`expired`, no callback) after 24 h.

### 3.6 External Systems Console - FR-104 / Playbook (back office, token)

**Story.** Real integrations answer "pending" now and the truth later, by events. This console is where the learner plays *every* external system, one tab per role. As the **payment processor**, they see the pending payment their flow registered and click "Send success webhook" - or "Send duplicate" to teach idempotency. As the **shipping carrier**, they walk an order through `shipment.created -> in_transit -> delivered`, or send `delayed`, `lost`, a duplicate, or events out of order - the raw material for the event-reliability recipes (dedup, out-of-order handling, watchdogs for events that never arrive). As the **supplier**, they send `supplier.order_accepted` and `inventory.restocked` events for reorder and backorder recipes. Each tab opens with role-play copy: in the real world, this button is a company's production system.

**Page spec.** One console, three tabs sharing one event-sender machine (event catalog per tab, target URL, delivery log with status/latency, DO-alarm scheduling for delayed and sequenced sends):
- **Payments tab.** Lists this sandbox's registered payments (payment_id, order_id, amount, status, registered_at). Pending rows: **Send success webhook** / **Send failure webhook** (reason: `card_declined` / `insufficient_funds`). All rows: **Send duplicate** (re-sends the exact prior event, same `event_id`). Auto-mode: `manual` (default) / `auto` with delay 5-120 s and outcome `random (85/15)` / `succeeded` / `failed`.
- **Shipping carrier tab.** The learner enters or picks an order id, sets the target URL (`fr_url_events_callback` by default), and either sends individual lifecycle events (`created`, `in_transit`, `delivered`, `delayed`, `lost`) or presses **Play normal delivery** (the sequence auto-sends over ~60 s via alarms). Extra controls: **Send duplicate**, **Send out of order**, **Stop sequence** (for missing-event/watchdog recipes).
- **Supplier tab.** Manual events: `supplier.order_accepted` (in response to a purchase-request recipe), `supplier.shipment_arrived`, `inventory.restocked { sku, quantity }`. No mutable inventory in this phase: the event is the teaching payload; recipes react to it. (True stock mutation is explicitly deferred - see Section 8.)

**API spec.**
- `POST /api/{token}/payments` body `{ "order_id": "ord_8h2k1x", "amount_cents": 2043, "callback_url": "https://..." }` -> `202 { "payment_id": "pay_7f3m", "status": "pending" }`. `GET /api/{token}/payments`, `GET .../payments/{id}`.
- Payment webhook (button or alarm):
```json
{
  "id": "evt_9k2mq1", "type": "payment.succeeded", "created_at": "2026-08-24T18:03:40Z",
  "data": { "payment_id": "pay_7f3m", "order_id": "ord_8h2k1x", "amount_cents": 2043,
            "status": "succeeded", "failure_reason": null }
}
```
- Shipping events: `{ "id": "evt_...", "type": "shipment.in_transit", "created_at": "...", "data": { "shipment_id": "shp_...", "order_id": "...", "carrier": "FlowPost", "status": "in_transit", "estimated_delivery": "..." } }`. Duplicate sends reuse the `id`; out-of-order sends are genuinely out of sequence.
- Supplier events: `{ "id": "evt_...", "type": "inventory.restocked", "created_at": "...", "data": { "sku": "FLS-POPPY-ICE", "quantity": 200, "warehouse": "EAST" } }`.
- Console-initiated sends target `fr_url_events_callback` unless a per-send URL is entered; all URLs validated per Section 5.

### 3.7 Return Request page - FR-104 / FR-105 (shop)

**Story.** The single densest business scenario in the program. A customer (the learner) opens Return Request, picks one of the static orders, chooses items, and writes a free-text reason ("the lupine seeds never came up, though I followed the instructions"). Their returns flow receives it and runs the full gauntlet across recipes: look up the order and the policy window (static data + knowledge pack), interpret the reason with AI, branch on eligibility, route high-value refunds through the Approvals Desk, issue the refund (payments machinery), and notify the customer. One small form; policy + lookup + AI judgment + human approval + orchestration.

**Page spec.** Form: order id (picker over static orders, or free entry), items (from the chosen order), reason category (select: `not-germinated`, `damaged`, `wrong-item`, `changed-mind`, `other`), free-text reason (textarea, required), preferred resolution (`refund` / `replacement`). Panel connect field: `fr_url_returns_trigger`; canned example requests (one clearly eligible, one clearly out of policy, one ambiguous - for AI-judgment recipes).

**API spec.** Outbound only:
```json
{
  "type": "return.requested", "event_id": "evt_...", "submitted_at": "...",
  "order_id": "ord_8h2k1x", "customer": { "id": "cus_ali01", "name": "Alice Nguyen", "email": "alice@example.test" },
  "items": [ { "sku": "FLS-LUP-BLUE", "quantity": 1 } ],
  "reason_category": "not-germinated",
  "reason_text": "Sowed per the packet in May, kept moist, nothing came up after six weeks.",
  "preferred_resolution": "refund"
}
```

### 3.8 Review page - FR-105 (shop)

**Story.** A one-field form with outsized teaching value. The learner submits reviews (or uses the canned set spanning normal / glowing / harsh-but-legitimate / spam / abusive) to their moderation flow: AI classification, sentiment, spam detection, negative-review escalation to the Approvals Desk, and a customer-recovery follow-up. The static `/api/shop/reviews` dataset (3.2) supports batch-moderation recipes over existing data.

**Page spec.** Product picker, star rating, review text, submit. Panel connect field: `fr_url_review_trigger`; canned examples selectable.

**API spec.** Outbound only: `{ "type": "review.submitted", "event_id": "evt_...", "submitted_at": "...", "sku": "FLS-POPPY-ICE", "customer": {...}, "rating": 1, "text": "..." }`.

### 3.9 Knowledge pack + site-wide Support chat - FR-105

**Story.** The learner builds the course's support agent: an AI Agent with the shop's knowledge base attached, exposed via a blocking Call Flow URL. They download the Knowledge pack, load it into a FlowRunner Knowledge Base, attach it to the agent, and paste the flow's URL into the chat widget's connect field. The widget floats on *every* page - the learner's agent becomes the shop's support widget. "What's your return window?" gets "45 days," a fact that exists only in the pack. The tools recipes go further: an order-lookup tool (a flow calling `GET /api/shop/orders/{id}`) answers "what's the status of order ord_8h2k1x?"; the policy-aware-support recipe combines pack facts with live order data; the escalation recipe has the agent hand off to the Approvals Desk when it should stop. The persona switcher (Alice / Bob / Guest) drives per-user memory: Alice's "I only grow natives" shapes Alice's answers, not Bob's.

**Page spec.**
- **Chat widget:** floating launcher on every page (shop and back office). Header: persona switcher (Alice Nguyen `cus_ali01` / Bob Tran `cus_bob02` / Guest `guest`) and a connect control bound to `fr_url_support_agent` (inline when unconfigured, per 2.2). History is client-side, per persona, cleared on persona reset. Blocking send, 30 s, typing indicator; render `{"reply": "..."}` or a plain-string body; anything else renders raw; timeouts/errors appear as system messages.
- **Knowledge pack page:** downloads (markdown + generated PDFs): `faq.md`, `returns-policy.md`, `shipping-policy.md`, three growing guides, `catalog.csv`. Specific checkable facts (return window 45 days; free shipping over $35; 1-year germination guarantee; poppies need cold stratification), listed with sources in `knowledge-pack/FACTS.md`.

**API spec.** Outbound chat request:
```json
{
  "type": "support.message",
  "customer_id": "cus_ali01", "customer_name": "Alice Nguyen",
  "conversation_id": "conv_local_uuid", "message": "Do you ship to Canada?"
}
```

### 3.10 Order Replayer - FR-106 (back office)

**Story.** Debugging lessons need *specific known failures*. The learner sets their order flow LIVE, opens the Replayer, and sends test order #4 - the one with a zero-quantity line item. Their flow fails exactly where the lesson says it will; they find the failed instance in FlowRunner's monitoring, diagnose it, fix the flow in a new version, switch LIVE over, and replay the same order to prove the fix. "Send all 8" populates monitoring with a realistic mix; "burst x10" sends ten clean orders. Combined with the seeded mismatches in the static payments/shipments datasets, this gives the redesigned FR-106 its material: find, diagnose, fix, re-version, replay, reconcile.

**Page spec.** Lists the 8 curated replay orders: number, one-line description, defect (or "clean"), Send button per row; **Send all 8** and **Burst x10 (clean)** (sequential, 2 s spacing, simple loop - no job system). Each send POSTs `order.created` to `fr_url_checkout_trigger` (missing-URL behavior per 2.2) and logs the response in Activity. Catalog: 3 clean; 5 defective - missing customer email, zero-quantity line item, unknown SKU, malformed date, order total mismatch. Documented in `/seed/replay-orders.md`.

**API spec.** Outbound only; same `order.created` envelope as 3.4, payloads fixed in the repo.

## 4. Repo and deployment

- MIT license. Root: `README.md` (what it is, one-click **Deploy to Cloudflare** button, local dev via `wrangler pages dev`), `TUTORIAL-MAP.md`, `CONTRIBUTING.md`, `wrangler.toml`, `/public` (static pages; `/public/img/products/` per naming convention), `/functions` (Pages Functions), `/seed` (fixed datasets incl. `replay-orders.md`, `KNOWN-MISMATCHES.md`, `reviews-labels.md`), `/knowledge-pack`.
- Self-hosting is first-class: fork-and-deploy in minutes from the README alone; also the escape hatch for anyone whose FlowRunner endpoints the hosted instance's URL rules would block.
- No analytics beyond Cloudflare's own aggregate metrics.

## 5. Security and abuse (non-negotiable before public deploy)

The site makes outbound HTTP to user-supplied URLs; treat it as a potential open relay:
- **Outbound URL rules** (enforced server-side at call time and at registration for stored callback URLs; mirrored client-side in the panel): `https://` only; hostname must not resolve to private/link-local/loopback ranges; no IP-literal hosts; redirects not followed; 10 s timeout (30 s for shipping quote and support chat); response bodies capped at 64 KB.
- **Rate limits:** per-IP caps on every outbound-calling endpoint, plus per-sandbox caps on back-office services (Cloudflare rate-limiting rules + in-DO counters). Replayer and console sequences capped server-side at their documented volumes.
- **Payload caps:** inbound bodies capped at 32 KB; no file uploads anywhere.
- **No stored learner URLs** beyond pending callback/event jobs (deleted on delivery, decision, or 24 h expiry). No server-side logs containing form field values.
- **Abuse contact** in README and in the outbound User-Agent.

## 6. Build phases (aligned to course rollout)

| Phase | Ships with | Contents |
|---|---|---|
| A | FR-101 | Site shell (shop zone), Tutorial Assets panel component, Contact page, static shop APIs incl. legacy endpoint |
| B | FR-103/104 | Back office shell + sandbox, Inventory Service Console (with warehouses), storefront cart/Checkout (incl. abandon control), Approvals Desk, External Systems Console (payments + shipping tabs), webhook signing, static payments/shipments datasets |
| C | FR-105/106 | Knowledge pack, site-wide chat widget + personas, Return Request page, Review page, static returns/reviews datasets, Order Replayer, supplier tab |

Each phase lands with its acceptance checks green and `TUTORIAL-MAP.md` updated.

## 7. Acceptance checks (curl-able / scriptable)

1. `GET /api/shop/orders?limit=5` (no token) returns 5 orders with `X-Total-Count` and `Link` headers, identical across sandboxes and cacheable; statuses span the documented set; the legacy endpoint returns the same order recognizably mangled per the documented rules.
2. `GET /api/shop/payments` and `/api/shop/shipments` contain exactly the seeded mismatches listed in `/seed/KNOWN-MISMATCHES.md`; `/api/shop/reviews` items match `/seed/reviews-labels.md`.
3. Contact page with no URL configured: Submit expands the Tutorial Assets panel instead of failing; after saving a URL, the pending submission sends the documented payload and appears in Activity.
4. The panel rejects `http://...`, `https://10.0.0.1/...`, `https://localhost/...` client-side; the server independently rejects the same at call/registration time.
5. Inventory with `fail_next=2` fails exactly twice (500, JSON body), then succeeds; 429 mode includes `Retry-After`; per-warehouse quantities match the dataset; a second sandbox's failure profile is unaffected.
6. Checkout shipping quote renders the body returned by a stub blocking endpoint; a stub answering in 31 s produces the timeout state and flat-rate fallback; place-order delivers `order.created`; **Abandon cart** with a 15 s delay delivers `cart.abandoned` at ~15 s.
7. `POST /approvals` appears on the Desk within one poll cycle; Approve delivers the decision payload within 2 s and shows delivery status; auto-approve at 10 s delivers at ~10 s; a pending approval expires after 24 h without a callback.
8. External Systems Console: **Send failure webhook** with `card_declined` delivers `payment.failed` with that reason and a valid `X-Signature`; **Send duplicate** delivers a byte-identical event with the same `event_id`; **Play normal delivery** delivers `created`/`in_transit`/`delivered` in order over ~60 s; **Send out of order** genuinely violates the sequence; **Stop sequence** halts remaining alarms; supplier tab delivers `inventory.restocked` with the entered SKU/quantity.
9. Return Request and Review pages deliver their documented payloads; each page's canned examples match the repo fixtures.
10. Chat widget appears on every page; renders `{"reply": "..."}` and plain-string responses; per-persona history survives switching; a fact question answered by a stub returning pack content matches `knowledge-pack/FACTS.md`.
11. Replay order #4 matches `/seed/replay-orders.md` byte-for-byte; **Send all 8** delivers sequentially at ~2 s spacing; **Burst x10** sends exactly 10 clean orders and respects the server-side cap.
12. A fresh fork deploys to Cloudflare Pages from the README instructions alone.

## 8. Explicitly out of scope (this version)

Learner accounts and auth; real payment/email providers; **mutable inventory / true restocking state** (supplier events are simulated sends only; revisit if backorder recipes need stock that actually changes); persistence beyond the 7-day sandbox TTL; FlowRunner branding; marketing/landing content; multi-language; mobile apps.
