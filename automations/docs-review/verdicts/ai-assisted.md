# Verdict: content/extend/ai-assisted.md (Quick Start: Your First Extension (with AI))

- Date: 2026-09-22
- Verdict: **major-rework** (concept-page-review, 7 lenses, one run; not re-run per the one-net rule)
- doclint: 0 errors

## Gate summary (verbatim)

Not ready. The spine is sound (eight driven steps, one running example carried from the one-sentence request to
the Test Monitor, five shots that match their sections), so this is a re-drive of steps 4-8 plus a shot pass, not a
restructure. The theme: the page narrates one non-deterministic Claude Code run as the reader's guaranteed outcome
(the prompt never asks for the place-to-weather linkage steps 7-8 depend on, the report is never shown, and the
drive was `claude -p`, not the interactive session the page teaches); the lede advertises the coordinates path the
author dodged because FR-3635 drops decimals; "pass it every time" sets a `deploy -s prod` trap; the Custom
Extensions screen has no shot; the two canvas shots are composed with Start cut in half. Candidate rules: (1) a
walkthrough over GENERATED output says what is fixed and what varies, and its prompt asks for every property later
steps rely on; (2) a lede never advertises a path the page avoided because it is defective; (3) flag advice names
WHICH command; (4) drive the path you teach, not a proxy, or state where the reader's experience differs.

## Resolution (same day)

| # | Sev | Item | Resolution |
|---|---|---|---|
| 1 | blocker | one non-deterministic run narrated as guaranteed | Prompt tightened (asks for the action with a place dropdown OR coordinates); RE-RUN in a fresh project made with the printed init command -> one action + one dictionary, 42 tests; deployed and recaptured; "your run will not match line for line" + the could-not-reach-API caveat added; run logged. |
| 2 | blocker | Custom Extensions screen unshown | CAPTURED (TMDB + Open-Meteo rows, badge hidden, nav name swapped) as custom-extensions-list-ai.png with an alt naming both rows. |
| 3 | major | lede advertises the coordinates path | Lede = "the current weather for a place you pick from a dropdown". MARK RULED: no note about typed coordinates on the page. |
| 4 | major | "-s prod ... pass it every time" | "It is an `init` flag, so you pass it only here" + package-vs-command sentence, on both quick starts. |
| 5 | major | init -s prod never run verbatim | RUN verbatim in an empty dir (Server line prod, flowrunner.json prod); this IS the project the page's outputs come from. |
| 6 | major | drive was `claude -p`, not interactive | Still `claude -p` (an interactive TUI cannot be driven from here); the page now says "Approve the file edits and the test run when Claude Code asks" - the report itself recorded that `npm test` needed an approval the non-interactive session did not grant. Logged as NOT DRIVEN interactively. |
| 7 | major | Claude Code's report not shown | The end of the real report quoted, trimmed and labelled, at the top of step 5. |
| 8 | major | canvas shots: Start cut, dead gap, toggles differ | RECAPTURED from one continuous drive with the viewport set by script: Start whole, small gap, toggles identical across shots. The collapsed Test Monitor dock remains at the bottom-left of the canvas (editor layout, not chrome). |
| 9 | major | picker alt edited a duplicate row out | Typed `Berlin` (10 distinct rows); alt written to the exact rows in frame. |
| 10 | major | "FlowRunner agents" collides with the AI Agent feature | MARK RULED: one term everywhere - the CLI prints "FlowRunner agents", so the quick start says "Install the FlowRunner agents" / "Two FlowRunner agents for Claude Code". |
| 11 | major | step 5 packed sentence, no lead-ins, "module" | Retitled "The service and tests it wrote"; lead-ins; bullets; "service". |
| 12 | major | editor auto-refresh undriven | Driven on the TMDB service earlier today; this page's log points at that record; clause moved to the step-up bullet. |
| 13 | minor | npm test / deploy blocks not verbatim | Both now verbatim from the single-service project (workspace swap only). |
| 14 | minor | Test Monitor crop cut mid-row | Re-cropped on a complete row. |
| 15 | minor | picker prose gaps | "the picker you asked for opens, headed Select value for Place"; ((Place)) chipped; value = coordinates, name = label; "Leave Latitude and Longitude empty". Run with only Place set -> Success (driven). |
| 16 | minor | no "read the result" bullet | Added: {{Get Current Weather Result->temperature}} (the result is flat per the report and the run). NOT evaluated to a value. |
| 17 | minor | hero caption | Sentence above the image describing the end state. |
| 18 | minor | Test Panel / Test Monitor styling; chip case | ((Test Panel)) / **Test Monitor**; chips as seen on screen per Mark's ruling. |
| 19 | minor | cli.md links still say Let AI Build It | Repointed to the new titles. |
| 20 | minor | Node floor | "Node 18.20+, 20.12+ or 22+" on both quick starts (source: harness engines). |
| 21 | minor | ((Search)) unverified | DRIVEN: placeholder "Search". |
| 22 | minor | agents read the reference | DRIVEN: both agent files reference service-code-format/; roles confirmed. |
| 23 | nit | "nothing else to sign up for"; ™ placement | Fixed. |
| 24 | nit | em-dashes in quoted CLI output | MARK RULED: verbatim. Lead-ins added before every command. |
| 25 | nit | off-page claims | Log states the login/token reuse, the substitutions' location, and the second-flow check done for TMDB. |
