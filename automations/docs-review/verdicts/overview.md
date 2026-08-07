# Verdict — Welcome / landing page (content/index.md)

- **Date:** 2026-07-29
- **Status:** gate findings resolved; awaiting Mark's review. One [MAJOR] (positioning lede) is a deliberate owner decision, held for Mark. Mark is final authority.
- **doclint:** 0 errors, 0 warnings.

## Current state
- **Vision-led opening (Mark's brief, 2026-07-29):** agents are being created everywhere (Claude/ChatGPT accounts, QuickBooks, every app) → a team will run hundreds → that is chaos → FlowRunner is where you configure, run, and orchestrate them, with a person in the loop and an audit trail. This is the ONE place the docs wear a marketing hat; the rest of the page stays plain. Replaces the rejected "platform for building flows" technical framing and resolves the gate's [MAJOR].
- **Hero at top:** Mark's synthetic AI-Router flow screenshot (Form Submitted Trigger → Submission Intent AI Router → Billing / Technical / Everything Else → Gmail + Slack actions), verified rendering in the served site.
- **Section renamed** "What you build: a flow made of blocks" → **"What is a flow?"** (reader-question; pairs with the H1 and "How a flow runs").
- **No diagrams.** Both Mermaid diagrams removed at Mark's direction — the support-ticket one (superseded by the hero) and the Synchronize one ("out of place and out of context" on a Welcome page). Stale no-shot reasons referencing them were corrected; verified 0 mermaid blocks in the built page and all six H2s rendering.

## Gate (independent reviewer) — findings + resolution
- **[MAJOR] Lede reads as generic automation, not the AI-agent-orchestration identity.** HELD: Mark explicitly rejected the marketing-positioning lede earlier ("super shallow / reads like a marketing page"), so the informative framing is deliberate. Offered Mark a middle path — foreground "actions, AI agents, and human decisions" in sentence 1 without marketing-speak — for his decision.
- **[MINOR] Hero example followed the human-decision sentence but showed fully-automated routing (non-sequitur).** FIXED: reframed the lead-in to "Here is one that runs fully on its own…", tying it to para 2's "a flow can run fully on its own."
- **[MINOR] MCP bullet's closing sentence restated the prior one.** FIXED: cut it.
- **[MINOR] Mermaid strokes hardcode light-theme hex; dark-theme legibility.** VERIFIED earlier via a dark-mode screenshot (nodes legible, borders visible). No change.
- **[MINOR] Core Concepts link lands on Flows & Instances (2nd nav item; Workspace is 1st).** LEFT: defensible — no `concepts/` index page, and Flows & Instances is the natural conceptual entry.

## Verified clean (reviewer + doclint)
All 18 link paths resolve; hero alt text faithful to the flow; every product fact accurate (up-to-a-year wait / 30-day Growth; MCP one-registration → blocks + agent tools; Synchronize fan-in + Max Waiting Time; router semantics; start-with-any-block; results pool via Expression Editor; independent instances). Mechanically spotless: ™ once, no em-dashes, no banned words, meaningful section titles.
