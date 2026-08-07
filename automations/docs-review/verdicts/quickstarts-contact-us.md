# Verdict — Quick Starts: A Contact Us Form (no-code + with code)

- **Date:** 2026-07-31
- **Status:** both pages complete, all images supplied by Mark and read back against their alt text. Awaiting Mark's final review — Mark is final authority.
- **doclint:** 0 errors, 0 warnings on both. Full site build: no broken links or missing images.
- **Pages:** `content/learn/quickstart.md` (309 lines), `content/learn/quickstart-code.md` (300 lines)

## What they are
The real flow behind the flowrunner.ai contact form, documented twice - once with a block per placeholder, once with a single Custom Cloud Code block - so the same job demonstrates both halves of "no-code or with code". Each page is standalone; a reader never has to jump between them (Mark, 2026-07-31: "I do not want the readers to jump back and forth between the articles").

## Mark's corrections, and what they changed
1. **"No instructions for placing/renaming blocks"** - every block now names its palette category, the drag, and the ((Name)) field, with *why* naming matters.
2. **"The URL belongs to the trigger, not the flow"** - corrected; a flow can hold several callback triggers, each with its own URL.
3. **"Learning Mode must be optional"** - now explicitly optional, with three tabbed ways to send the sample (live form, curl, browser tool such as reqbin).
4. **"Zero instructions for declaring a variable / they have not met the Expression Editor"** - the Expression Editor is introduced where it is first needed, and the variable is created field by field.
5. **"Zero instructions to select the Replace operation"** - the operation picker and all three fields are spelled out, using labels **verified in-product** (Text / Search String / Replacement string), not guessed.
6. **"THE MOST IMPORTANT TOPIC AND YOU'RE BLOWING IT"** (the write-back concept) - rewritten to reason from the problem: five gaps, filling one yields new text with four left, so each block must work on the previous result. Includes a table tracing one template line through Set Template -> Replace Name -> Replace Email, and the payoff that order does not matter because each block removes only its own placeholder.
7. **"No instructions for connecting the blocks"** - taught at the first block that needs it, then reinforced at every later one. Mark's own revision naming the ((chain)) icon's **lower-right corner** was verified correct against the screenshots and kept.
8. **"No instructions for the Send Email login"** - now a real step: the ((OAuth Connection)) field reading `OAuth Connection is required`, ((ADD ACCOUNT)), and the once-only nature of it.
9. **"Arguments are declared in the Code Editor popup"** - I had them as a separate panel section; corrected so the whole of step 6 happens inside the ((Open Code Editor)) window, arguments on the left and code on the right, ((APPLY)) keeping both.

## Defects I caught myself (with evidence)
- **Wrong trigger alias.** Mark's `quickstart-callback-url.png` showed `Reference Trigger Data As` = `Contact Us Form Submitted Data`. My text told readers to look for `Contact Us Form Submitted`, which does not exist in the picker. Fixed everywhere, plus an explanation of the "Data" suffix where the reader first meets it.
- **Alt text claiming more than the shot shows.** Both instance screenshots have the *trigger* selected, so Element Execution Details shows the trigger's output - not the code block's input/output, and not a step-through of the Replace blocks, as my text promised. Rewritten so the screenshots teach the real mechanism (select a block to see its Input and Output) instead of over-claiming.
- **Markdown list breakage, twice.** An unindented image between numbered items split step 6 into two `<ol>`s, so the code step rendered as "1" instead of "3"; and a wand-icon step's continuation lines lost their indent. Both found by inspecting the built HTML, not by assuming.
- **Left a `mkdocs serve` running**, which took port 8000 and broke Mark's own serve. Killed; verification now uses `mkdocs build`, which needs no port.

## Verified in-product (Documentation Flows only)
Replace's real field labels (Text / Search String / Replacement string) and the ((Assign to a Variable)) block-panel section were confirmed by placing a Transform Data block in the sandbox and reading the panel. The temporary block was deleted afterwards; the workspace was left exactly as found. No production or customer workspace was opened.

## Images
All 14 (no-code) and 13 (code) images are in place, supplied by Mark, and each was read back against its alt text. `quickstart-code-editor.png` matches the documented snippet character for character. `quickstart-instance.png` was recaptured by Mark after I flagged that it showed default block names, contradicting the guide's naming lesson; it now shows the guide's names, the `Contact Us Form Submitted Data` alias, and the same sample payload as step 4.

## Open
- Nav: **Tutorials** currently sits inside the **Quick Starts** group - flagged to Mark, may want to be a sibling.
- `learn/quickstart-agent.md` (the AI-agent quick start) is still a stub; story proposed, awaiting Mark's go-ahead and a flow.
