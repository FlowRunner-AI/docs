# Handover: "What happens if I stop paying?" — FAQ for the website pricing page

**For:** the website project
**From:** the docs project (FlowRunner docs rebuild)
**Date:** 2026-08-25
**Status:** draft copy, ticket-sourced — **needs one in-product confirmation before publishing** (see
[Before you publish](#before-you-publish))

---

## Why this belongs on the pricing page, not in the docs

FlowRunner suspends a workspace when its billing lapses, and a suspended workspace shows a
full-screen blocked state instead of the normal Console. Somebody who hits that screen has already
lost access to the product, so an answer buried in the product documentation is an answer they
cannot reach. The question is also asked *before* purchase — "what happens if I cancel?" is a
standard pre-sale objection — which is a pricing-page job, not a docs job.

The docs' Billing page (`content/manage/billing.md`) covers plans, allowances, and payment profiles,
and will link here rather than duplicate this.

## What the product actually does

Shipped in release **v1.0.12** (2026-07-28) under FR-2730 *"Block workspace if subscription
cancelled/expired"*, with its behavior defined across four subtasks. Sources are listed at the
bottom.

**What triggers it.** A billing problem on the workspace's subscription: the subscription is
cancelled or expires, the monthly renewal cannot be paid, or the card on file is declined.

**What happens to running work.** Running and queued flows are **stopped** when the workspace is
suspended, and API calls into that workspace's flows are refused with a `40X` and an error message.
This is the part customers care about most: automation stops, it does not queue up and catch up
later.

**What the customer sees.** Selecting a suspended workspace in the Console shows a full-screen
"blocked" screen in place of the normal view. From it they can do exactly three things:

1. Follow a link to Stripe to fix the billing problem — update the payment method, or reactivate the
   subscription.
2. Delete the workspace.
3. Switch to another workspace, if they have one. (If the account has no other workspace, no such
   option is shown.)

Nothing else in the Console is reachable while the workspace is suspended. **Flow export is not
available** — a customer cannot pull their work out of a suspended workspace, which is worth being
straight about rather than letting them discover it.

**Getting back.** Once the billing problem is resolved and the subscription is reactivated, the
workspace becomes accessible again. **Flows have to be restarted by hand** — they do not resume on
their own. Anyone relying on a scheduled or LIVE flow needs to know this, because a reactivated
workspace with every flow stopped looks fine and does nothing.

**Self-service billing.** Since **v1.0.14** (2026-08-18, FR-3250) customers can manage their own
subscription through the Stripe Customer Portal, so "update my card" and "reactivate" no longer need
a support ticket.

## Draft FAQ copy

Lift and edit freely — this is written to the website's audience, not the docs'.

> **What happens if my payment fails or I cancel?**
>
> Your workspace is suspended. Flows that are running stop, queued runs are dropped, and API calls to
> your flows are refused until billing is sorted out. Opening a suspended workspace shows a billing
> screen instead of the usual Console, with a link to Stripe where you can update your payment method
> or restart your subscription.
>
> **Can I still get to my flows while a workspace is suspended?**
>
> No. A suspended workspace shows only the billing screen, so you cannot open or export your flows
> until the subscription is active again. Nothing is deleted while you sort it out.
>
> **What happens after I fix the billing problem?**
>
> Your workspace opens up again with everything as you left it — but your flows stay stopped until
> you start them yourself. If you rely on scheduled or live flows, check them and start them again
> after reactivating; they will not pick up on their own.
>
> **Can I manage my own subscription?**
>
> Yes. You can update your card, change your plan, and cancel or restart your subscription through
> the Stripe customer portal, without contacting support.

## Before you publish

Two things to settle, both cheap:

1. **Confirm the blocked screen in-product.** Everything above comes from the implementation tickets
   and Mark's own approval comments on them, not from a suspended workspace being observed. The docs
   project could not verify it: suspending a workspace is destructive and there is no safe workspace
   to do it to. Someone with a disposable workspace or a Stripe sandbox account should confirm the
   screen's wording and the three available actions before this copy goes live. **Do not publish the
   "no export" claim without confirming it** — it is the one that will annoy people if it is wrong in
   either direction.

2. **Do not mention free credit — it is being retired.** Confirmed by Mark on 2026-08-25: FlowRunner is
   moving off the free-credit model to a **trial plus a free plan**. FR-3200, which added a "your free
   credit is used up" notification, was closed on 2026-08-05 for the same reason. Any pricing-page copy
   describing free credit is describing a model on its way out, and the FAQ draft above deliberately
   does not mention it. Get the trial length and the free plan's limits from Mark before writing the
   plan copy around them. The docs' own Billing page still refers to a free-credit balance and carries
   the same correction on the docs project's list.

## Sources

| Ticket | What it defines | Release |
| --- | --- | --- |
| [FR-2730](https://backendless.atlassian.net/browse/FR-2730) | Parent: block workspace if subscription cancelled/expired | v1.0.12 (2026-07-28) |
| [FR-2732](https://backendless.atlassian.net/browse/FR-2732) | The blocked-workspace screen: full-screen state, Stripe link, delete workspace, no other Console access; flows stopped on suspend and API calls refused with 40X; manual restart after reactivation | v1.0.12 |
| [FR-2731](https://backendless.atlassian.net/browse/FR-2731) | The pre-suspension prompt to add a card; Mark's comment defines the trigger as "not enough money to renew monthly cycle or if the card is declined" | v1.0.12 |
| [FR-2936](https://backendless.atlassian.net/browse/FR-2936) | The Stripe link used by the blocked screen | v1.0.12 |
| [FR-2884](https://backendless.atlassian.net/browse/FR-2884) | Switching to another workspace from the blocked state | — |
| [FR-3250](https://backendless.atlassian.net/browse/FR-3250) | Stripe Customer Portal for self-service subscription management | v1.0.14 (2026-08-18) |
| [FR-3200](https://backendless.atlassian.net/browse/FR-3200) | Free-credit-exhausted notification — **closed**, superseded by trial + free plan (confirmed by Mark 2026-08-25) | — |
