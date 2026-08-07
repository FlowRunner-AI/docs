# Verdict — flows-as-agent-tools-concept (content/reference/flows-as-agent-tools-concept.md)

Gate: concept-page-review. Run 2026-07-09 (wf_d8e2e6c1-c3b), diagnostic run requested by Mark → **major-rework** (1 blocker, 2 majors, 8 minors, 1 nit). Page had already passed Mark's read; the plain-style self-check handled register at draft time, so the gate surfaced product-fidelity/coherence gaps (its real strength).

APPLIED (Mark: "good feedback, apply it"):
- BLOCKER (LIVE requirement): added a plain statement in How-it-works — the agent runs the flow's current LIVE version, which is what the "Execute ... flow (LIVE version)" line on each attach entry means; a flow not yet set LIVE won't do anything when called. Verification note added (UI text + call-flow.md parity).
- MAJOR (opener leads on mechanics): How-it-works now opens on purpose — "Attaching a flow hands the agent that flow as one more tool it can choose to call" — then the open/go/add mechanics.
- MAJOR (scope/escape-hatch): added to When-to-use — "when you want one flow to call another directly, with no agent deciding when, use Call Flow instead," giving the Related Call Flow link its reason.
- MINOR: added FlowRunner™ on first mention; trimmed the repeated "one-shot" waiting restatement in When-to-use; folded the double "not on the agent" location clause into "the flow's own Flow Settings panel"; scoped the Compose Result claim ("rows shape what it returns," not "decide what the agent sees" — avoids the multi-Return-Result compound-structure inaccuracy).

LEFT (judgment calls / flagged, not silently dropped):
- MINOR {{Initial Data->question}} prose-only: kept — consistent with the established Initial Data model (SubFlow page); the prose shows the reference form, not "type this."
- MINOR descriptions shot cropped to the field groups (no panel title/tab): kept — the shot demonstrates the two descriptions (the concept); the panel location is stated in prose ("Flow Settings panel").
- MINOR human-in-the-loop trigger reconnection: kept — the return channels (trigger / External Callback) are product-owner-verified (2026-06-18 note); did not add reconnection mechanics that aren't verified.
- NIT "Manage Capabilities" vs window title "Manage AI Agent Capabilities": acceptable (control label vs window title).

Gate NOT re-run (one-time-net rule; Mark decides ship). doclint 0 errors / 0 warnings.
