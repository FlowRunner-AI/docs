# Verdict: content/extend/getting-started.md (Quick Start: Your First Extension (code))

- Date: 2026-09-22 (second gate run of the day; the first, on the long "Write It Yourself" page, is superseded by
  the rewrite into a quick start per Mark's direction)
- Verdict: **major-rework** (concept-page-review, 7 lenses, one run; not re-run per the one-net rule)
- doclint: 0 errors on the whole extend/ folder after the fixes below

## Gate summary (verbatim)

Not ready. The prose spine is sound (every lens, including craft, passes the nine-step walkthrough and its single
TMDB/693134/Dune running example), but three of the eight shots (Configuration, Execute, Test Monitor) are
2026-08-31 dev captures of the pre-`.secret()` build ... and the rewrite outran its housekeeping (three
build-breaking dead anchors, an open ledger item covering exactly those shots, a stale exploration log, no gate
verdict on the rewritten page). Red-team candidates: (1) when TAUGHT CODE changes, every shot of the surface that
code renders goes on a recapture list keyed to the code edit; (2) a CLI flag's meaning is per-command, so never
write "always pass FLAG" without naming the command; (3) when a page shows real output beside a declared sample of
it, reconcile the gap the reader can see.

## Resolution (same day)

| # | Sev | Item | Resolution |
|---|---|---|---|
| 1 | blocker | Configuration shot: clear-text key, pre-`.secret()`, dev | RECAPTURED on prod: dummy value typed (not saved) -> dots + Show value eye + SAVE CONFIGURATION; alt rewritten (also on deploying.md). Help icon found beside the label with the `.describe()` tooltip -> FR-3634 RETRACTED, prose says the description sits behind the question mark. |
| 2 | blocker | dead anchors + six "Write It Yourself" links | FIXED: repointed to `#6-give-the-workspace-your-tmdb-key` / `#7-run-it-by-hand`; link texts renamed on 5 pages; folder lint 0 errors. |
| 3 | blocker | ledger items open without evidence; no verdict for the rewrite | This file; ledger updated; the key-dependent shots done once Mark saved the v3 key. |
| 4 | major | Execute + Test Monitor shots stale (dev, blue icon, cut mid-line, no title in frame) | RECAPTURED on prod with Mark's v3 key: both scrolled so the title row is in frame; alts rewritten to the pixels. (First paste was the v4 token -> `[object Object]` -> FR-3637.) |
| 5 | major | hero shows Set Variables the steps never build | Option (b) applied: Set Variables deleted from the kept flow, hero RECAPTURED (Start whole, block, panel to Reference Result Data As); setup sentence above the image; step 8 says "after Start"; next-steps bullet trimmed. |
| 6 | major | "-s prod ... pass it every time"; cli.md init lacks -s | FIXED: "It is an `init` flag, so you pass it only here" + package-vs-command sentence (both quick starts); `-s prod` added to cli.md's two init examples. |
| 7 | major | editor auto-refresh claim undriven | DRIVEN earlier today (label v2 deploy -> palette refreshed without reload, placed block kept its name; restore -> same) and now logged on the page; clause moved to the "Change it and deploy again" step-up bullet. |
| 8 | major | real output vs declared sample | Sentence added: TMDB returns more than the sample, the block hands all of it on; type a property name into the picker's "Select or type..." box or add it to `result`. (Typing a property not in the sample NOT run to a value.) |
| 9 | minor | init -s prod never run verbatim | DRIVEN verbatim in an empty dir: Server line prod, flowrunner.json prod. Logged. |
| 10 | minor | config survives a redeploy | NOT DRIVEN (no key saved yet); listed in the log. |
| 11 | minor | themoviedb.org key path | Mark's own paste showed the trap: the page next to the v3 key offers the v4 Read Access Token (239 chars, starts eyJ), which the service rejects. Wording sharpened to name both and say which one. |
| 12 | minor | pill never evaluated | NOT DRIVEN; listed in the log. |
| 13 | minor | "every flow in your workspace" | DRIVEN: the CUSTOM EXTENSIONS group appears in a second flow's palette without a reload. |
| 14 | minor | chip case vs pixels | MARK RULED: chips as the reader sees them - ((SAVE CONFIGURATION)), ((EXECUTE)), ((run block)) applied on both quick starts and deploying.md; rule in VOICE. |
| 15 | minor | Node floor jargon | "Node 18.20+, 20.12+ or 22+" on both quick starts (source: harness engines; logged). |
| 16 | minor | list shot: nav sliced, 99+ badge | RECAPTURED with the badge hidden, cropped to end on the Custom Extensions nav row (see ledger). |
| 17 | minor | stale exploration log | REWRITTEN as one dated log with a per-image list. |
| 18 | minor | ((Movie ID)), Test Panel/Monitor styling, Run Block pointer | ((Movie ID)) and ((Start)) chipped; ((Test Panel)) / **Test Monitor**; the Test Panel is in the hero shot. |
| 19 | minor | step 4 title/actor; icon.svg | "Paste the extension code"; configItems = the form you fill in on the extension's page (step 6); step 3 names public/icon.svg. |
| 20 | nit | "an assistant"; double link; hero caption | Fixed. |
| 21 | nit | fence-first; em-dash in quoted CLI output | MARK RULED: a lead-in before every command ("Open a terminal and enter the following command:" then "Run the following command:") - applied; quoted output stays verbatim. |
| 22 | nit | ((Search)) unverified | DRIVEN: the palette box's placeholder is "Search". |
