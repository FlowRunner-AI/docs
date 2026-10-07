# For Mark

The only file you need to read. Updated 2026-10-06.
Reply by number, for example "1: logs A, editor B; 2A; 3B". Each item is removed once you've answered it.

## Decisions

**Panic Mode:** waiting on FR-3717 (Discussion, assigned to Andriy Konoz), which asks how a workspace in Panic
Mode is unlocked and what it stops. The section gets rewritten, and tested, once that's answered.

## Waiting on you

- **Prompt to Flow:** the docs and the website brief are on hold until the 4 questions on FR-3247 (posted 09-29) are answered.
  - 3 and 4 are yours to answer; 1 and 2 are for engineering.
  - The questions: (1) which MCP clients are supported, (2) which design prod runs and when the redesign ships, (3) plan limits or quota, (4) the customer-facing name.
- **Extend > OAuth page:** stays out of the navigation until you sign in to GitHub once in the automation browser, so I can test the OAuth example.

## I'll do these unless you object

- **Billing, what happens when a trial ends:** the page says the workspace goes **past due** (FR-3321). FR-3349 says it drops to **Free**. I'll ask the engineer on FR-3349 and fix the page to match the answer.
- **Expression Editor:** I'll remove the Variables screenshot. It comes from what looks like a real customer's banking integration ("Set ARSC", "AGENT-BANKING-BRANCH-PROD").
- **Knowledge Bases:** I'll fix the reader-facing errors below on prod. Your 08-15 ruling covered not redoing screenshots, not leaving wrong facts in place.
- **From now on**, every check and screenshot is done as a customer on prod.

## Pages that mislead readers today

"To confirm" means not yet checked on prod.

- **Expression Editor:**
  - Says Live Preview shows what the expression comes to; it shows reference pills, not values.
  - A screenshot from a real customer's flow.
- **Compliance & Security:**
  - Panic Mode effects are untested (waiting on FR-3717).
  - The SLA Calendars screenshot shows a control that has been removed.
- **Extend pages:**
  - Everything else from today's full recheck is fixed: 47 wrong statements across the section.
- **Knowledge Bases:**
  - Says loading a document needs a flow; the Data tab appears to have a direct upload (to confirm).
  - Doesn't say the embedding key must come from an embedding provider. An Anthropic key can't do it.
  - Wrong about which settings are fixed after creation.
  - The MongoDB form is missing the required Index Name field (to confirm).
- **Flow Editor:**
  - The palette screenshots show the removed AI ASSISTANTS group, and your name and email.
  - Says the lightning icon runs the whole flow; the blocks before it don't run.
  - Says an unconnected block looks like any other; it actually gets a red badge (to confirm).
