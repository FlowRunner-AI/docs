# Verdict: content/extend/parameters-and-types.md

- Date: 2026-09-09
- Verdict: **major-rework**
- doclint: 0 errors, 0 warnings (`--warnings`)

## Summary

Not ready. The driven facts and the TMDB running example are sound through the first two-thirds, but the page ships one screenshot for ten teaching sections and that shot's List row contradicts the table and alt; three recurring-correction breaches (trigger-as-start reasoning, "hint under the field" vs the help icon the sibling shots show, "repeating fields" colliding with the Repeat block) plus an evidence-free dynamicParams section make this a rebuild of the visual and evidentiary layer, not a copy-edit. The theme of what remains: the tissue around the driven facts - invented mechanisms ("both travel as strings", "the editor cannot check", "nothing has run yet") that the page's own later sections, sibling pages, or the runtime docs contradict, and UI claims no pixel on the page proves. Red-team candidate rules for the guidelines: (1) a page's one-line explanation of a visible label must agree with the page's own later mechanism section; (2) a page-wide guarantee ("every rule is checked", "fails the deploy", "unknown fields stripped") is a claim about every slot the page covers and must survive the sibling page it links to; (3) when two listed modifiers can be chained and the pair behaves differently from either alone, state the pair; (4) a simplifier ("keep to the eight") must not ban the only documented fix for a trap the same page half-describes.

## Work list

### [blocker] definition-of-done - Whole page - screenshot coverage (Leaving a field blank / Showing a label, sending a value / What is checked / Grouping)

**Issue:** One screenshot (param-widgets.png) for ten teaching sections. The page's own deployed TMDB Discover Movies block (9c62d40f5cc6, rendered in TD Sandbox per the log) is never shown, yet four sections point the reader at the screen: the empty Sort By dropdown (default not pre-filled), the Sort By dropdown open showing Most popular / Newest first / Highest rated (.labels(), the FR-3425 fix this revision exists for - never observed, only an empty dropdown is logged), the «Minimum Rating» must be at most 10 failure, and a list-of-objects entry 'rendered as its own group of fields, with controls to add and remove entries'.

**Fix:** On dev.flowrunner.ai / Documentation Flows, viewport >= 1600x1000, capture and read back each: (1) Discover Movies panel as first opened - Sort By empty, Release Year / Minimum Rating as number inputs, the .describe hint visible - at 'Leaving a field blank'; (2) the Sort By dropdown open showing the three labels, at 'Showing a label, sending a value' - then pick Highest rated, run, confirm the outgoing query carries sort_by=vote_average.desc; (3) the failed run with Minimum Rating = 11 showing the message, at 'What is checked', naming WHERE the reader reads it; (4) the Boxes list (or its TMDB-continuity replacement, see the Grouping item) with two entries and the add/remove controls in frame, at 'Grouping'. Introduce each shot in the sentence before it; log every capture with date in the exploration comment.

Raised by: guideline, definition-of-done, educator, fidelity, red-team

### [blocker] definition-of-done - What each type renders as - param-widgets.png and the z.array row

**Issue:** PIXELS: the List [list] row shows one empty '(no value)' expression box with a wand, a green list icon and a green minus - no rows, no add control. The table promises 'a repeatable list, with controls to add and remove entries' and the alt says 'List with add and remove controls'. The console's ui-widgets.md confirms a list of plain strings/numbers opens as a single expression box and the builder switches to the row editor with a view toggle; only lists of enums / dictionary fields / objects open as rows. The page's own Grouping example declares tags: z.array(z.string()), so the first author who follows it sees one text box. The shot also shows a purple mode toggle on Text/Number/Boolean/Date/Enum and none on String (z.string() IS the expression input), which the prose never names; the frame clips the Object group's closing edge and the panel bottom; the shot is dated 2026-08-31, before the 2026-09-07 runtime release, and the log self-certifies 'unchanged' without a re-check.

**Fix:** Recapture on dev (dated) with the List switched to the row editor holding two entries so add and remove are in frame, and with the Object group's closing edge and panel bottom included. Hover the green list icon and the minus and name what they do. Split the table row: a list of enums / dictionary fields / objects opens as rows with add and remove; a list of plain strings or numbers opens as a single expression box that the view toggle beside the label switches to rows - repeat this under Grouping where tags is declared. Name the mode toggle in the expression-mode sentence: 'the switch beside the label flips a control to an expression input; a z.string() field has no switch because it already is one - which is why the String row shows a wand and no toggle.' Rewrite the alt to the pixels. Log both list states and the toggle on/off drive.

Raised by: definition-of-done, red-team, fidelity, educator, guideline

### [blocker] guideline - What each type renders as (line 44)

**Issue:** Trigger-as-start framing: 'A trigger's params have no expression mode, because nothing has run yet.' The fact is confirmed by trigger-config-panel.png (Payload > Genre has no wand or toggle), but the reason assumes the trigger is first in the flow; the section's own index.md / triggers.md teach mid-flow triggers. The reason is also in neither the DRIVEN nor SOURCE-DERIVED log - a mechanism outrunning the drive.

**Fix:** Delete the reason: 'A trigger's params have no expression mode.' Move this fact, together with 'A trigger's params are flat' (line 202), into one bold run-in **On a trigger.** under 'Designing fields a flow builder can use' (params render under **Payload**; plain fields only; no expression mode) and link [Triggers](triggers.md). Grep the page for 'starts a run|starts the flow|nothing has run' before handoff.

Raised by: guideline, educator

### [blocker] guideline - The plugins - .describe() row (line 60)

**Issue:** 'The hint under the field' is a UI location the sibling pixels contradict: block-in-flow.png renders this page's own movieId field (declared with .describe in the lede code) as 'Movie ID [string]' with a '?' help icon beside the label and nothing under the field; ai-built-block-config.png shows the same '?'; service-structure.md line 61 says 'behind its help icon'. Two sibling pages now name two different places. The derived text is also truncated (source: 'Expects an email address, e.g. foo@bar.com') and set in italics where the hierarchy gives read-text bold.

**Fix:** Drive it: open Discover Movies on dev, find where .describe('TMDB score out of 10') on Minimum Rating appears on a block param, and deploy a z.email() with no .describe() to read the exact derived hint. Reword the row to what the pixels show ('The help text behind the ? icon beside the label' if that is what the drive shows), quote the derived text in full in bold or paraphrase without italics, capture one field with its help tooltip open (covered by shot 1 in the coverage item), and make service-structure.md say the identical thing.

Raised by: guideline, fidelity, red-team

### [blocker] guideline - Grouping and repeating fields (heading line 171; line 173; table row line 28)

**Issue:** Term collision: 'repeating' / 'repeats' / 'repeatable' is the Repeat block (and List Iterator) - repetition in a flow. Here it means a list-valued field; a reader scanning the ToC reads 'repeating fields' as fields inside a loop.

**Fix:** Heading: 'Nested fields and lists'. Line 173: 'z.object() nests fields; z.array() makes a list of them.' Table row: 'a list, with controls to add and remove entries' (then split per the List-row item). Grep the page for repeat|repeating|repeatable after the edit.

Raised by: guideline

### [blocker] definition-of-done - Fields that depend on a choice

**Issue:** Evidence-free and gestural: dynamicParams is in neither the DRIVEN nor the SOURCE-DERIVED log, has no scenario, no code, no shot, and asserts live editor behaviour ('change one of those fields and the generated ones are resolved again', 'resolve runs while the form is half-filled') that appears in NO source read - the console marks the client render contract for top-level dynamicParams an open item and metaInfo.dynamicParams 'provisional'. It is also the one slot where the page's guarantees are false: a non-z.object return fails when the console first calls resolve, not at deploy, and an action with dynamicParams carries undeclared keys through (validation.md).

**Fix:** Drive it on dev: add a dynamicParams action to the TMDB service (criteria = a resource/show enum, resolve returns a field named from the choice), deploy, open the block, change the criteria field, watch the generated field appear / re-resolve, and log whether resolve fires before required criteria are filled. If it works: give the section a concrete scenario in sentence one, the dynamicParams: { criteria: z.object({...}), resolve: async ({ criteria, apiRequest }) => z.object({...}) } code built on it, a shot of the generated field appearing, and scope the resolve row ('must return a z.object; this is the one slot the deploy cannot check - a bad return fails when the console first calls it; undeclared keys are not stripped here'). If it does not render in the builder: cut to the declaration table + a routing sentence, file the ticket, and record Mark's ship-pending-fix decision in the ledger.

Raised by: definition-of-done, educator, guideline, craft, fidelity, red-team

### [major] educator - Lede

**Issue:** Opens on the mechanism ('A block's fields are its params, declared as a zod object') - the exact 'a variable is a container' opener §0 forbids; the sibling Dictionaries lede shows the right shape. The second paragraph is a four-clause enumeration that pre-states what 'Leaving a field blank' and 'What is checked' teach, and the universal 'Every rule on a field is checked before your handler runs' is contradicted by actions.md's strictness table (polling trigger params: lenient). WHERE is never said (params render under the block panel's **Body Params** group; a trigger's under **Payload**). The craft lens notes Actions opens the same way, so this is also an Extend-section register call for Mark.

**Fix:** Add one leading sentence from the flow builder's seat, then the existing mechanism: 'The fields a flow builder fills in on your block - a Movie ID to type, a Release Year that only takes a number, a Genre picked from a dropdown - and the checking that stops bad input before it reaches your code, all come from one declaration: params, a zod object. Pick a type and the editor draws the matching control under the block's **Body Params** section; chain a plugin and the field gets its label, hint and default.' Keep the code block. Replace paragraph two with 'execute receives exactly what you declared, parsed and typed:' + three short bullets (converted to the declared type; unknown fields stripped; a blank resolved the way you declared it - see Leaving a field blank). Scope the enforcement sentence to an action's params (or cut it - the validation section carries it). Put to Mark whether the same leading sentence goes on Actions / Service Structure so the section stays uniform.

Raised by: educator, craft, guideline, red-team

### [major] verify-in-product - What each type renders as (lines 45-47) / What is checked before your handler runs (lines 131-132)

**Issue:** Undriven framing that the flow EDITOR validates declared rules on block params at design time: 'render as a plain text field that the editor cannot check, and are only validated when the flow runs' and 'a value the editor accepts may still be rejected by a run, never the other way round'. Every driven params failure on record (minRating 11) surfaced at RUN time; the source states editor-side checking only for the config dialog (FR-3387), and 02-zod-types.md says the console checks the same schema with function-backed rules as the ONLY exception - so 'the editor cannot check' unions/tuples/records is asserted against the source. union/tuple are not even in the source's SINGLE_LINE_TEXT list (record/unknown/literal are).

**Fix:** Drive on dev: type 11 into Minimum Rating on Discover Movies and look for an inline error before any run; deploy a param declared z.union([z.string(), z.number()]) with 0.0.10, confirm deploy succeeds, what it draws, and whether the editor flags anything before a run. Then write only what was seen: either 'the block panel flags it as you type; .refine() rules are only seen by a run' or drop every editor claim and keep 'a violation fails the block before execute runs'. Reword the degrade bullet as a plain statement: 'Types outside the table deploy, but they render as a plain text field and are validated at run time.'

Raised by: definition-of-done, red-team, fidelity

### [major] guideline - What each type renders as (lines 35-36) / Dates

**Issue:** Internal contradiction created by an invented reason: '[string]' is explained as 'both travel as strings, and only their widget differs', while the Dates section says the picker sends epoch milliseconds and type-date.md confirms 'finite number - epoch millis'. FR-3537 says [string] is the PUBLISHED param type, not the transport. A reader of both sections cannot reconcile them; a reader of the first writes a handler that assumes a string.

**Fix:** State the fact without the transport claim: 'The editor prints the published param type beside each label, which is why Date and Enum read as [string]: the type is string, the widget is what differs. What a date field actually hands your handler is under [What a date field hands your handler].'

Raised by: red-team

### [major] educator - What each type renders as (lines 38-51)

**Issue:** One section carries four ideas under a counted, flourishy lead-in ('Three more things worth knowing about the table:') that goes false on the next edit: string formats that validate (a checking fact), expression mode + the trigger exception (a flow-builder fact), unsupported types degrading, and the container-must-be-z.object / FR_EXT_INVALID_SCHEMA deploy rule (a deploy-validity fact a reader searching 'why did my deploy fail' will not find here). 'not refused, they degrade' is a banned contrast form.

**Fix:** Keep the table, the shot, the [string] note and the mode-toggle sentence as the section. Move 'A string format is a single-line field that validates' into 'What is checked before your handler runs'. Move the trigger sentence to the **On a trigger.** run-in (see the trigger item). Keep 'Other zod types' as a bold run-in with a countless lead-in, and add the z.array(z.array()) case (no row editor; renders as one input). Move the container rule to a bold run-in beside the lede's declaration ('**The container is always a z.object.** ...') or into Troubleshooting under FR_EXT_INVALID_SCHEMA.

Raised by: educator, guideline, craft

### [major] educator - Lede / The plugins / Leaving a field blank

**Issue:** What a blank field arrives as is taught three times (lede clause; plugin-table rows for .optional / .nullable / .default; the section's own table), and the section that owns the idea is the third telling. The .nullish() row makes the reader work out 'whichever the editor sent' = null when the paragraph above already said the editor sends null.

**Fix:** Plugin table: reduce the three rows to purpose ('Marks the field not required' / 'Supplies the value used when the field is left blank') with one pointer 'what a blank arrives as is under Leaving a field blank'. Lede: one clause. .nullish() row: 'null - the editor sends null for an untouched field'. Line 82: 'The modifier on the declaration decides what your handler receives.'

Raised by: educator, guideline

### [major] educator - The plugins (heading) / Dates (heading + body)

**Issue:** Two headings are bare nouns, not anchors. Dates teaches the trap before the remedy and buries z.coerce.date() in TypeScript-inference jargon; its absolute is wrong ('the only declaration whose inferred type matches what arrives' - FR-3537 / type-date.md: z.date() is the one declaration whose inference LIES; z.iso.* infer string and hand back string); the sample label «Since» belongs to no field on the page; 'instead of rejecting it' is a contrast form; the ISO formats draw as plain text boxes, not pickers, which the page omits. The shared-param naming convention (Param suffix, one plugin per line) is a code-organisation tip parked under the plugin catalogue.

**Fix:** Retitle 'Giving a field its label, hint and default' and 'What a date field hands your handler'. Dates: open on the recommendation ('Declare z.coerce.date() and your handler gets a Date whether the value was picked, typed or bound'), then the plain z.date() behaviour as the reason (ISO string when typed or bound, epoch milliseconds from the picker - z.date() is the one declaration whose inferred type lies), then validation, then the ISO reshaping with a note that z.iso.* render as plain text boxes. Declare the date on the running example (e.g. releasedAfter: z.date().label('Released After')) and use that label in the message. Move the shared-param convention to a bold run-in **Sharing a param across actions.** or to the Designing section.

Raised by: educator, guideline, craft, red-team, fidelity

### [major] guideline - Grouping and repeating fields (lines 185-200)

**Issue:** Undriven readability claim ('Three does not, and a flow builder wiring an expression into a deeply nested field has a poor time of it') and an unsubstantiated generalisation ('the one most APIs actually need') replace the sourced hard limit (z.array(z.array()) has no row editor; renders as one input). Two 'rather than' contrast forms and a four-clause sentence. The section swaps domains twice (recipient/email, then shipping boxes) after 170 lines of TMDB, and the nested-error wording two sections earlier cites «City» (declared nowhere) and «Tags item 2» (declared only here).

**Fix:** Stay on TMDB: e.g. genres: z.array(genreIdParam).label('Genres') for the list and a group such as releaseWindow: z.object({ from, to }) or castFilters: z.array(z.object({ personId, role })) for the list of groups. Move the nested-error sentence here, right after the declaration, citing fields that exist on it. Replace the readability paragraph: 'A list of groups is the common shape - boxes, recipients, line items. Keep nesting to two levels: give an entry plain fields, not another list. A list inside a list has no row editor and renders as one plain input.' Note: if the Boxes example is dropped, capture shot (4) on the replacement.

Raised by: definition-of-done, guideline, craft, educator

### [major] verify-in-product - What is checked before your handler runs

**Issue:** Messages are printed bare while actions.md:65 and troubleshooting.md:63 show the string the builder meets: [flow-extension:tmdb] invalid params for method "discoverMovies" — minRating: «Minimum Rating» must be at most 10 (prefix, method, KEY before label). WHERE and WHEN the message surfaces is never said. 'Every offending field is reported at once' is hand-written-source only. The max-10 drive is in the ledger but missing from the on-page note.

**Fix:** Show the message once in the driven form, identical to actions.md; state where it appears (the block's error in the failed instance / test run). Drive on dev: leave Genre blank AND set Minimum Rating 11 in one run; confirm both fields are named. Add the max-10 drive and the TD Sandbox nulls -> Success run to the on-page note (both are already in the ledger).

Raised by: definition-of-done, red-team, fidelity

### [major] verify-in-product - Lede / What is checked / trigger params

**Issue:** 'Every rule on a field is checked before your handler runs' vs actions.md 'Polling trigger params | Lenient. The runtime polls with whatever the instance was saved with' vs the runtime README ('trigger data ... the poll fails'). Three documents, three answers.

**Fix:** Drive on dev: deploy a polling trigger with z.number().min(1) on a param, save an instance with 0, and watch whether the poll fails or runs. Scope the lede to an action's params or state the trigger exception in the **On a trigger.** run-in, and make actions.md say the same thing.

Raised by: red-team

### [major] verify-in-product - Leaving a field blank

**Issue:** The page teaches the required-string half of the '' rule and omits the sharper half the runtime authors flag as having 'shipped at least once' (16-gotchas): a CLEARED text box sends '', and on a format field (z.email().optional(), z.url().optional()) '' is a value, so it reaches the format check and fails with «Email» is invalid although the field is optional. The page's own example declares email: z.email(). The documented fix is z.union([z.email(), z.literal('')]).optional(), and this page says unions 'degrade' and 'Keep to the eight' - it bans the only escape.

**Fix:** Drive the cleared-field case on dev (does the editor send '' or null for a cleared text field?). Then add the mirror sentence: 'The same '' reaches a format check, so an optional z.email() or z.url() that a flow builder cleared is reported as invalid, not unset. Where blank must mean not set, declare z.union([z.url(), z.literal('')]).optional() - the one place a union earns its keep.' Soften the union ban to 'outside that case, keep to the eight'.

Raised by: red-team

### [major] guideline - Leaving a field blank (lines 107-109)

**Issue:** 'The declared default is published to the editor but not pre-filled into the field, so a flow builder sees an empty dropdown' is taught as settled behaviour with no product-owner ruling and no Jira ticket (FR project, default + extension, 120 days) - an empty dropdown whose blank silently means Most popular is what a bug report looks like. Even if intended, the author is handed nothing to do about it.

**Fix:** Put it to Mark as a self-contained decision: page + what the flow builder sees (empty Sort By, runtime fills popularity.desc) + options: (a) intended - keep the sentence and add the practice '.describe("Defaults to Most popular")' because the builder cannot see the default; (b) defect - file it with the fresh repro and drop the sentence to 'a blank arrives as the default'. Recommendation: (a) until the product owner says otherwise, with (b) filed only on his call.

Raised by: red-team

### [major] guideline - Showing a label, sending a value

**Issue:** Scope and escape hatch not stated for .labels(): the enum list is fixed when the service is written, and the section never says what to reach for when the options live in the API; the reader meets dictionaries only two sections later as advice. Line 154 ('A choice outside the declared list is refused before execute runs') restates the validation section.

**Fix:** After the example add: '.labels() is for a list you know when you write the service. When the options come from the API - genres, projects, folders - use a [dictionary](dictionaries.md) instead.' Delete line 154.

Raised by: guideline, educator

### [major] definition-of-done - PLATFORM-REVIEW-LEDGER.md - EXTEND section

**Issue:** No page-level ledger section exists; the page is one word in a 'Pages changed' sweep line. Nothing records the pixel read-back of param-widgets.png, the control-state drives (mode toggle, list view toggle), the missing worked-example shots, or the dynamicParams evidence gap.

**Fix:** Add a 'Parameters & Types (content/extend/parameters-and-types.md)' section listing each DoD item with dated evidence: every PNG and what its pixels show, control states driven, dynamicParams drive or Mark's decision, the default-not-prefilled ruling, and the fresh verdict file from the re-run gate.

Raised by: definition-of-done

### [minor] guideline - The plugins - .secret() and .example() rows / .nullable().default()

**Issue:** .secret() is scoped to config with no reason, on the page where an author naturally tries it on a token param (the runtime excludes params on purpose: a param's value is saved in the flow and readable over the API - a security fact). .example(v) is described only by its result-side effect while Applies-to says 'field or result'; no source says what it does on a param. Both tables state .default(v) absorbs every blank, but optionality.md shows .nullable().default(v) hands over null when null was sent - which is exactly what the editor sends.

**Fix:** .secret() cell: 'On a param it does nothing, on purpose - a param's value is saved in the flow and readable over the API, so a credential belongs in config, never in a block field.' .example(): drive .example(693134) on Movie ID on dev and state where it surfaces, or narrow Applies-to to 'result'. Under the blank table add: 'Do not pair .nullable() with .default(): the editor's null is handed over as null and the default never fires. .optional().default(v) behaves as plain .default(v).' Drive .nullable() and .nullish() in the harness (not covered) and log typeof.

Raised by: red-team, fidelity

### [minor] verify-in-product - Prose-only claims of medium/low risk not yet substantiated

**Issue:** Backed only by hand-written source, none driven with 0.0.10 or shown on this page: (a) FR_EXT_INVALID_SCHEMA for a bare shape / single field / z.object().optional(); (b) .map() fails to load naming .labels(); (c) a trigger's object/list param renders as a single text field; (d) humanized key without .label() (releaseYear -> Release Year); (e) expression-bound param reaches execute typed (bind Release Year to a string '2024', log typeof); (f) nested error wording «Tags item 2» must be a string (1-based); (g) required z.string() param accepts '' (driven only on the config form).

**Fix:** Run each on dev / the 0.0.10 CLI and add a dated line per drive to the on-page note: (a) three scratch deploys, capture the exact abort text; (b) add .map() to a scratch enum, deploy, capture the load error; (c) add a z.object() param to On Movie Released, open the trigger; (d) deploy a field with no .label(); (e) bind and log; (f) bind Tags to ['a', {}] via expression and run; (g) clear Movie ID on Get Movie Details and run. State in the handoff anything left undriven.

Raised by: fidelity

### [minor] guideline - Whole page - plain-style and flow-vs-instance sweep

**Issue:** Greppable constructions the pre-handoff check bans: 'not by what the editor sent', four 'rather than', 'not refused, they degrade', 'instead of rejecting it', 'has a poor time of it'. 'only validated when the flow runs' / 'run only when the flow runs' say the flow runs (an instance runs) - the same idiom is on dictionaries.md, triggers.md, index.md.

**Fix:** Rewrite each per the educator suggestions (lines 82, 119, 128, 186, 199-200); 'at run time, inside an instance' for the two flow-runs lines and sweep the four Extend pages together or put the idiom to Mark as one section-wide ruling. Run the greppable plain-style check before handoff.

Raised by: educator, guideline, craft

### [minor] educator - Designing fields a flow builder can use

**Issue:** The dictionary bullet repeats the Dictionaries lede almost verbatim without linking it, on the page that precedes Dictionaries in the nav.

**Fix:** 'Back id-like fields with a [dictionary](dictionaries.md).' and keep the one-line payoff. Add the shared-param convention as its own bullet if moved here.

Raised by: educator, guideline

### [nit] guideline - Whole page - product name

**Issue:** FlowRunner is never named, so there is no ™ mark; actions.md / dictionaries.md / service-structure.md follow the same convention while index.md / getting-started.md carry ™.

**Fix:** Leave as is; note for Mark whether every Extend page should name 'the FlowRunner™ flow editor' once in its lede.

Raised by: guideline
