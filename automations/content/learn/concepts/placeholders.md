<!-- Verified in-product 2026-08-26 (Documentation Flows, throwaway flows "Ticket Triage"
     BA35089A-F8DF-42E4-AE96-6AF4EDAC0233 and "Live Placeholder Test" CD3F8A0B, both created and DELETED;
     no existing flow was edited).
     ROUND-3 CORRECTIONS FROM MARK (2026-08-26), all three of them my errors:
     (1) THE EXAMPLE WAS WRONG AT THE ROOT. Earlier drafts used a weather flow whose placeholders were the
     city and the forecast length - values that vary per RUN, which a reader rightly reads as hard-coding.
     Placeholders earn their keep on values that are identical for every run of a flow but differ per
     DEPLOYMENT. The page is rebuilt on a support-triage flow: the ticket arrives per run as Initial Data;
     the channel, the escalation threshold and the weekend switch are configuration.
     (2) API KEY IS AI-ONLY. Mark, 2026-08-25: "API keys apply only to AI API keys." An earlier draft
     ignored that and shipped a section, an example AND a screenshot calling it a weather-service key. The
     type now appears only in the type list plus one honest note; there is NO worked API-key example,
     because no block can consume the type yet - see FR-3443.
     (3) THE LIVE-VERSION CLAIM WAS INVENTED. Mark answered "placeholder for LIVE flow is uneditable" and
     I wrapped that in mechanics I had never observed ("opening its settings is not how you change it").
     NOW DRIVEN, and the truth is different again: starting a version navigates to /version/1/view, and
     VIEW MODE HAS NO RIGHT-HAND TAB STRIP AT ALL - no Blocks List, no Block Configuration, no Flow
     Settings. Clicking a block opens a read-only config panel; there is no route to Placeholder Data. The
     /edit URL of a LIVE version is still reachable (bookmark, back button) and THERE the Flow Settings tab
     renders and CRASHES the editor - FR-3442, whose repro was sharpened with this finding.
     FR-3442 RE-DRIVEN 2026-08-31 on dev.flowrunner.ai (Documentation Flows, TD Sandbox): THE HOLE IS
     CLOSED. Navigating directly to /version/1/edit on a LIVE version no longer renders the editor - it
     REDIRECTS to /version/1/view, so the crash path this note describes is unreachable and the Flow Settings
     tab cannot be opened on a LIVE version by any route. Verified both sides: LIVE -> forced to /view with
     no tab strip; the same flow stopped -> /edit with all three tabs (Blocks List, Block Configuration,
     Flow Settings), and Flow Settings opens clean (Flow Memory: Memory Anchor, Missing Anchor Policy
     "Terminate on Memory Access", Memory Expiration Policy "Never"; Placeholder Data; Flow Description) with
     no "Something went wrong". This page's "Changing a value on a LIVE version" section was already correct
     and needed no change; the constraint was added to reference/flow-memory-concept.md, which routed readers
     to Flow Settings without it.
     ALSO DRIVEN: the + dialog takes Name / Data Type / Description; SAVE is refused without a Name
     ("Name is required") and names must be unique per version ("Name must be unique"). The Data Type list
     offers exactly eight values in this order: STRING, INT, DOUBLE, BOOLEAN / CHECKBOX, DATETIME,
     JSON OBJECT, JSON ARRAY, API KEY (pictured). Saved rows render "name[type]" in lower case against the
     dropdown's upper case. Value controls observed for every type: text box (string/int/double), Yes/No
     dropdown - only two options - (boolean), "Select date & time" + calendar (datetime), text box with a
     </> JSON editor (object/array), select over saved AI key setups by label (api_key; this workspace has
     one, "Demo Key"). A Description surfaces as a "?" icon beside the name (all four rows in the panel
     shot). TYPE PRESERVATION: escalateAbove (int, 8) bound into a Set Variables row named "Escalation
     Threshold" -> Run Block returned {"Escalation Threshold": 8}, a NUMBER. An earlier drive on a string
     placeholder returned its text. VERSIONS: cloning carried declarations AND values, including the
     api_key row's chosen setup.
     NOT DRIVEN, so NOT CLAIMED: what a missing value does at run time; type validation on save; export /
     import contents; loop and SubFlow scope; whether any non-AI key can ever appear in the api_key picker.
     FR-3257 (Flow Catalog) is OPEN - nothing about the catalog is written in present tense.
     ROUND-7 (2026-08-26), throwaway "Ticket Triage" 2EF455EB (deleted). The aiKey row was CUT from the
     example: it was the source of three separate defects (the lede counted three values while the panel
     showed four; the closing payoff promised an adopter fills in "their key" when nothing consumes it;
     and the API KEY bullet contradicted the reading section). API KEY remains one line in the type list.
     WORKED EXAMPLE REPLACED: the old Set Variables demo copied a placeholder into a variable, which is
     the duplication placeholders exist to remove and taught a pattern a reader must not copy with a key.
     It is now a Condition, "Urgent enough to escalate?", whose Value to Check is Initial Data->urgency
     and whose comparison Value is the escalateAbove reference, Operation GREATER THAN, Value Data Type
     INT - run data measured against configuration, which is the page's thesis.
     ROW AFFORDANCES DRIVEN (previously inferred from icon shapes): the gear reopens the dialog with BOTH
     Name and Data Type still editable; the trash asks "Delete Placeholder Data Item?" with CANCEL /
     CONFIRM before removing.
     RENAME HAZARD DRIVEN AND NOW DOCUMENTED: renaming escalateAbove -> escalationFloor did NOT re-point
     the Condition. The field still read escalateAbove and gained the error "The placeholder data item is
     not available", and the block's error count went 1 -> 2. This is the OPPOSITE of a block result
     alias, which follows its block on rename (flow-editor.md) - so the page states the difference.
     ROUND-8 (2026-08-26) - MARK'S FRAMING CORRECTION, the most important one on this page. Earlier drafts
     explained placeholders through a use case I INVENTED (a triage flow whose channel and threshold happen
     to be configuration) while withholding the reason the concept exists, which Mark had already given me
     on 2026-08-25: a flow published to the Flow Catalog declares its configuration as placeholders, and
     the install wizard prompts whoever installs it to supply the values (FR-3257: manifest carries each
     placeholder's label, description, value type and required flag; step 2 of the wizard prompts them;
     placeholders carry any value EXCEPT OAuth connections). I had treated "do not document an unshipped
     feature in present tense" as "do not explain the concept's purpose" - the wrong rule. The lede now
     leads with the purpose (a flow states what it needs from whoever SETS IT UP - round 9 corrected an
     earlier "whoever runs it", which names the one person who cannot supply a value) and the closing section
     names the Catalog explicitly as what this is built around, in future tense, with the triage flow kept
     as the illustration rather than the justification.
     ROUND-9 (2026-08-26), throwaway "Ticket Triage" A47E6D2B (deleted). ALT-TEXT SWEEP: the round-7 edit
     changed the PNGs but not their alt strings, so the panel alt still claimed four rows including
     aiKey/"Demo Key" (pixels: three rows) and the Expression Editor alt still claimed a
     "Set Variables > Perform Changes" breadcrumb and a fourth pill (pixels: "Urgent enough to escalate?
     > Condition - Value", three pills). Both rewritten against the pixels and read back. RULE LEARNED:
     when a worked example changes, every alt string is part of the example and must be swept with it.
     WORKED-EXAMPLE SHOT RECAPTURED: the previous one showed the Condition on canvas carrying a red error
     badge "1" and no outgoing branches - and the page teaches that exact badge as the tell for a BROKEN
     placeholder reference, so the picture of "correct" looked identical to the description of "broken".
     Wiring the branches could not be driven through automation (React Flow ignored the synthetic and
     Playwright drags), so the shot is now the block's CONFIGURATION PANEL alone, which carries its own
     header ("Condition") and the Name field, is self-identifying, and shows no canvas state.
     MISSING VALUE DRIVEN (was on the NOT-DRIVEN list): clearing escalateAbove's value flags the field
     that reads it with "The placeholder \"escalateAbove\" has no value", raises the block's error count,
     and DISABLES the Start control - so a version cannot be started with an unfilled placeholder that a
     block reads. The page now states this; the section opener no longer implies enforcement it had not
     earned.
     ROUND-10 (2026-08-26), throwaway "Ticket Triage" 9D713BEA (deleted). Two blockers were both in the
     lede I had rewritten one round earlier, each an over-correction of the previous note:
     (a) "what it needs from whoever RUNS it" names the one person who CANNOT supply a value (the launch
     dialog's section is inert, FR-3460) - corrected to "whoever SETS IT UP", and the page now uses one
     noun for that person throughout instead of five;
     (b) the lede stated the Flow Catalog in PRESENT tense with non-product verbs ("a flow you publish",
     "the person installing it"), which the closing section then contradicted. Mark's instruction was
     future tense; the Catalog now appears only in the closing paragraph, and "publish"/"install" are
     replaced with wording that does not imply product actions that do not exist.
     TWO ERROR STATES NOW PICTURED (previously taught by quoting their UI strings with no pixels):
     placeholders-no-value.png (value cleared -> the reference turns RED with a warning triangle above
     "The placeholder \"escalateAbove\" has no value"; Start disabled) and placeholders-renamed-break.png
     (rename -> same red treatment above "The placeholder data item is not available").
     SHOT ORDER FIXED: the panel shot now leads "Declaring a placeholder", where the tab, the panel and
     the + are named, instead of sitting a section below them.
     ALIAS CONTRAST QUALIFIED: flow-editor.md records that only a block's DEFAULT alias follows a rename
     (a hand-typed one does not), so the warning now says "default result alias".
     SCOPE CLAIM NARROWED to what was driven (top-level and inside a loop); SubFlow remains unclaimed.
     ROUND-11 (2026-08-26), throwaway "Export Probe" 9D7388BD (deleted). EXPORT CONTENTS DRIVEN - this was
     on the NOT-DRIVEN list and the gate was right that it gated the hand-off claim. Exporting a version
     downloads "<Flow> Flow (version N).json"; its flowVersion.metaInfo.executionStaticData holds one
     entry per placeholder carrying name, type, description AND VALUE:
       {"name":"notifyChannel","type":"STRING","description":"","value":"#support-triage","error":null}
     So a copy - cloned or exported/imported - arrives PRE-FILLED with the author's values, valid and
     startable. None of the page's safeguards fire: nothing is empty so Start is not blocked, nothing is
     broken so no field is flagged. The closing section had promised the opposite ("they fill in their own
     values") and now states the real behaviour, with replacing the inherited values named as the
     receiver's first job. Only a STRING placeholder was exported; whether an api_key row exports its
     chosen setup id is NOT DRIVEN and is not claimed.
     ALSO ROUND 11: the lede's "any block reads it" contradicted the API KEY bullet (nothing reads that
     type) - scoped to "the fields that need it"; the API KEY caveat was told three times and is now told
     once, on the type-list bullet where a reader is choosing a type; "This is the whole point of the
     concept" (meta-commentary, and a second claim to the page's point) cut.
     ROUND-12 (2026-08-26), throwaways "Import Source" 9F1B9B1F and "Imported Triage" D4AB6992 (both
     deleted). IMPORT DRIVEN - round 11 drove EXPORT only and I then wrote that an import "opens a flow
     already filled in and already valid" and "will start up quite happily", which was inference stated as
     observation. The gate caught it; it is the same failure class Mark called a MAJOR FAILURE on 2026-08-26.
     Now actually driven: exported Import Source (notifyChannel=#support-triage, escalateAbove=8), created a
     new flow through Create a New Flow > Import a Flow Version > Browse, and the imported flow's
     Placeholder Data list carried BOTH values, unflagged. The page now says exactly that and NOTHING about
     startability - the probe flow had no blocks, so its Start control was disabled for an unrelated reason
     ("The flow does not contain blocks"); the earlier "Start is not blocked" claim is CUT.
     EXPRESSION TOKENS: every reference the prose means as a value sitting in a field is now authored as
     {{escalateAbove}} so exprify renders the .fr-expr wand pill (three in the built page) - VOICE lines
     181-187 and my own encoded rule; backticks are kept only where the name is discussed as a declaration
     name ("Rename `escalateAbove` to `escalationFloor`"), matching blocks.md / subflows.md.
     LEDE SCOPED: "Everything the flow needs ... none of it buried in a block" was revoked by the page's own
     AI-key paragraph; now "The settings it needs are gathered in one place".
     SECTION RETITLED: "Configuration somebody else fills in" asserted the belief the section exists to
     correct - now "A copy arrives with your values in it".
     GLOSSARY DEFECT FIXED: the bare *[Placeholder]: / *[Placeholders]: abbreviation entries this page
     added were retroactive and fired on quickstart.md:139 and quickstart-code.md:147, where the word
     means {email} template markers. Both bare entries removed; *[Placeholder Data]: kept.
     ROUND-6 (2026-08-26), throwaway "Type Tag Probe" B891988E (deleted): ALL EIGHT TYPE TAGS DRIVEN by
     declaring one placeholder of every type - [string] [int] [double] [boolean] [datetime] [object]
     [array] [api_key]. An earlier draft DERIVED the tag as a lower-cased dropdown label and used
     JSON OBJECT -> [object] as its illustration; the derivation is WRONG (API KEY -> api_key keeps an
     underscore, JSON OBJECT -> object drops a word) even though that one example happened to be right.
     The page now lists the observed tags instead of a rule. ALSO DRIVEN: the Expression Editor inside a
     List Iterator's inner canvas shows the full PLACEHOLDER DATA group (all eight), so the scope claim
     is now "any field with an Expression Editor, including inside a loop" rather than an untested
     absolute. SUBFLOW SCOPE STILL NOT DRIVEN - the attempt used a wrong palette elementId and crashed
     the editor (my error, not a product defect); the page does not claim it. FR-3460 is now NAMED on the
     page: the gate was right that silence about the launch dialog's inert Placeholder Data section would
     leave a reader believing the page's central claim is false, so two driven sentences state what that
     section actually does without describing the bug.
     ROUND-5 (2026-08-26): the gate flagged that the Launch Flow Instance dialog carries its own
     "Placeholder Data" section, which would falsify "holds for every run of that version". DRIVEN on a
     throwaway ("Placeholder Override Probe", deleted): the version stored escalateAbove = 8; the launch
     dialog's Placeholder Data section was set to 99 and LAUNCHed. Run 101CDF04 recorded
     "Initial Data: escalateAbove: 99" and the Set Variables block still resolved the placeholder to 8.
     So the dialog's entry travels as INITIAL DATA and does NOT override the placeholder - the page's
     claim stands and is now driven. The misleading control is filed as FR-3460 and is deliberately NOT
     documented here; documenting a control that does not do what its label says would be worse than
     silence. Also reconciled this round: platform/api-keys.md carried a worked recipe (an API KEY
     placeholder read from an HTTP Request Authorization header) that FR-3443 shows is not possible - it
     was my own earlier text and is corrected; definitions.md and the glossary entry no longer offer an
     API key as the example use.

     ROUND 15 (2026-08-26) - fixes for gate run wf_fcedb4a7-d13.
     ROOT-CAUSE FIX: the example flow was Not Ready because the Condition's branches were unwired, which
     is why every earlier import capture carried a red chip. Wired THEN -> "Escalate ticket" (queue =
     escalations) and ELSE -> "Queue normally" (queue = standard). Flow 88C3EE86 is now Ready with no
     error badge, so the import shot is a real payoff rather than a crop that hides a defect.
     TYPE CLAIM CORRECTED, NOT JUST RE-SOURCED: launching with urgency from the launch form FAILS -
     "'GREATER_THAN' operation requires all values be numbers. One of values is 'String'". The same
     comparison SUCCEEDS under Run Block ({"conditionResult": true}), and both runs used the same
     placeholder value, so the placeholder is not the string: a placeholder does arrive as its declared
     type, but the other operand still has to be a number, and Value Data Type does not convert either
     side. The page said "needs no conversion"; that was wrong and is gone.
     LIVE EVIDENCE: started flow 88C3EE86, captured placeholders-live-view-mode.png (green "Live" chip,
     first tab "View", entire right-hand side empty - no tab strip), then STOPPED it; back to Ready.
     LAUNCH DIALOG: its Placeholder Data section lists only placeholders the flow READS (escalateAbove
     alone here), which reconciles run/testing.md - that page screenshots a flow with no placeholders.
     TAB LABEL: the three tab title attributes are exactly "Blocks List", "Block Configuration",
     "Flow Settings" - confirms this page and across-runs.md:46.
     MY OWN ROUND-13 ERROR: the Shared Memory escape hatch called it a workspace-wide store. It is
     flow-scoped (abbreviations.md:9, shared-memory.md:3). Rewritten to Call Flow.
     NOT DRIVEN, SO NOT CLAIMED: SubFlow scope. The two-item hedge that invited the question was removed
     rather than answered; the claim now sits at the version altitude that was driven.

     ROUND 16 (2026-08-26) - fixes for gate run wf_9e75a542-44b, whose blocker was that round 15 left the
     worked example documented as FAILING with no remedy.
     THE FAILURE IS A PRODUCT DEFECT, NOT A PLACEHOLDER FACT - and is now out of the page. Driven four
     ways on the same flow and the same values: (1) launch-dialog form, urgency=10 -> FAILS
     ("'GREATER_THAN' operation requires all values be numbers. One of values is 'String'"), reproduced
     twice; (2) the GET URL THE DIALOG ITSELF GENERATES from those same form values
     (.../activate?urgency=10&escalateAbove=8) -> execution 2624D359, COMPLETED / NORMAL / hasErrors
     false; (3) POST {"urgency": 10} -> execution 8ABAF1EE, COMPLETED / NORMAL; (4) run block ->
     {"conditionResult": true}. The placeholder resolves to a number on every route, so the launch FORM is
     the only producer of a string. Filed as FR-3461. Documenting a filed defect's symptom as behaviour is
     the FR-3460 mistake, so the page states the type rule and shows the successful evaluation
     (placeholders-condition-result.png) instead of narrating the bug.
     ALSO THIS ROUND: split two overloaded h2s into nine (the type rule, the version boundary and the
     Catalog payoff each reachable from the ToC); captured placeholders-launch-dialog.png; lifted the LIVE
     teaching out of its admonition; retitled the LIVE section off "a flow that is already running";
     chipped all eight Data Type options; dropped the Call Flow escape hatch, which did not solve the
     problem it was offered for; and rewrote the export warning, which had told the reader to clear a
     value the page elsewhere says makes the version unstartable.

     ROUND 17 (2026-08-26) - fixes for gate run wf_2a202a9d-fd4, whose blocker was the deepest one yet:
     THE EXAMPLE DECLARED THREE PLACEHOLDERS AND THE FLOW READ ONLY ONE. notifyChannel and
     notifyOnWeekends were decoration; the page's own launch-dialog shot proved it by listing a single row.
     Fixed in the product, not in the prose: replaced the "Escalate ticket" Set Variables with an
     HTTP Request "Post summary to Slack" whose Body is {"channel": {{notifyChannel}}, "text": ...}, and
     DELETED notifyOnWeekends, which nothing read. Flow 88C3EE86 is Ready with two placeholders, both
     genuinely consumed - escalateAbove by the Condition, notifyChannel by the request body. Recaptured
     placeholders-panel.png, placeholders-imported-prefilled.png (canvas now shows the HTTP block) and
     placeholders-launch-dialog.png (now lists BOTH placeholders, which is the same evidence that
     exposed the original defect).
     ALSO: the launch-dialog shot no longer depicts the FR-3461 configuration - the urgency value box is
     cleared, so the frame shows the dialog's structure without handing the reader a recipe that fails.
     BLOCKER 2, LIVE remediation: cloning was taught as the only route. Stopping a LIVE version hands it
     back as an editable draft - driven twice this session (started 88C3EE86, stopped it, chip returned to
     Ready at /edit) and corroborated by run/running-flows.md:46. Both routes now stated with the
     trade-off. Launch-dialog material promoted out of the LIVE section (it is not LIVE-specific) into its
     own h2. Read-only and scope split into two h2s.

     ROUND 18 (2026-08-26) - fixes for gate run wf_3bf25eca-b2f. Both blockers were MY fallout from the
     round-17 flow change: I edited the flow and did not re-open every PNG.
     STALE SHOTS REPLACED: placeholders-expression-editor.png still listed the deleted notifyOnWeekends
     (recaptured; PLACEHOLDER DATA now holds exactly notifyChannel and escalateAbove);
     placeholders-live-view-mode.png still showed the superseded "Escalate ticket" block (re-started the
     flow, recaptured with "Post summary to Slack" on the Yes branch, stopped it - chip back to Ready).
     RULE FOR NEXT TIME: when the worked example changes, re-open EVERY image, not just the ones the
     change obviously touched, and write alts that name blocks so a stale frame cannot hide behind a
     generic description.
     NEW EVIDENCE: placeholders-in-request-body.png - the HTTP Request panel showing {{notifyChannel}}
     bound INSIDE a JSON body, which is what round 17 existed to make true and had left unshown.
     placeholders-panel.png recaptured wide enough to include the gear tab strip the prose names.
     CORRECTED AGAINST THE PIXELS: Value Data Type sits ABOVE Operation, not beside it (panel order read
     off the live DOM: Value to Check 415, Value Data Type 482, Operation 545, Value 608).
     ALTITUDE FIXED: "whatever starts the run has to supply urgency as a number" was broader than the
     round-16 drive supports - the generated GET URL completed NORMAL. Now names the three routes that
     were actually driven.
     JSON FENCE RE-VERIFIED: the gate flagged it against the round-11 note (description:""), but a fresh
     export today matches the fence byte-for-byte, key order included (description, error, name, type,
     value). Not a defect; recorded here so it is not re-raised.

     ROUND 19 (2026-08-26) - Mark chose Option A on the round-18 blocker: make the WEBHOOK the placeholder.
     The example previously typed the Slack webhook URL straight into the HTTP Request - the one value in
     the scenario that is both per-deployment and secret - one line under "neither value is typed into a
     block", and parameterised a channel name a Slack app webhook ignores. Rebuilt in-product:
     notifyChannel renamed to notifyWebhook (STRING, https://hooks.example.com/triage/T29F4B1, described
     "Incoming webhook the triage summary is posted to") and bound into the HTTP Request's URL field; the
     block renamed "Post escalation summary"; its Body now reads Initial Data -> urgency so the request
     carries the ticket rather than a constant. Two placeholders, both genuinely read; flow Ready.
     The rename BROKE the old body binding and the flow went Not Ready until rebound - a live confirmation
     of the rename warning this page teaches.
     Recaptured all six affected shots and re-read each: panel, description-tooltip, expression-editor,
     in-request-body, launch-dialog, imported-prefilled. Re-exported; the JSON fence is verbatim again and
     now carries the webhook, which is what makes the export warning concrete.
     ALSO FIXED THIS ROUND (round-18 blockers 1-4): the type-tag list is back to all eight driven tags (my
     round-17 "label in lower case" derivation was wrong for [boolean] and [array]); "Setting a
     placeholder's value" now says where the value is typed and that the gear dialog has no value field;
     the launch dialog is documented positively (what you type travels as Initial Data under the
     placeholder's name); and every route claim is gone from the type section - see the drive below.
     ROUTE CLAIMS RETRACTED AND FR-3461 CORRECTED: re-driven, GREATER_THAN accepts a numeric STRING on
     every API path (POST 10, POST "10", GET ?urgency=10, and both operands as strings). So the page can
     claim nothing about what the other operand must be, and my FR-3461 description ("the form sends
     values as strings") was wrong - corrected in a ticket comment. The dialog-vs-API divergence is real
     and the ticket stands; only my explanation was wrong.

     ROUND 20 (2026-08-26) - fixes for gate run wf_6ff7d717-372.
     STALE SHOT (mine, again): placeholders-new-dialog.png was never recaptured in round 19 - its
     background panel still read notifyChannel / #support-triage, and my alt hid it behind "the settings
     panel showing at the right edge". Recaptured; the alt now NAMES what sits behind the dialog. The four
     shots not recaptured in round 19 (bound-in-block, condition-result, no-value, renamed-break) were
     re-opened and confirmed: they show only the Condition and escalateAbove, which the rename did not
     touch.
     PRODUCT-FACT ERROR CORRECTED: I had written that cloning "leaves the LIVE version running" and to
     "start the clone when it is ready", which reads as two LIVE versions. Only one version is LIVE at a
     time (flows-and-instances.md:23, running-flows.md:13); starting the clone makes IT live and the
     original steps aside (flow-editor.md:290). Rewritten to that mechanic, and the stop control is now
     located.
     EVIDENCE STRENGTHENED: the export fence carries BOTH rows, so "value": 8 appears unquoted beside the
     quoted string - the INT claim is now checkable in the artifact the page shows. Dropped the
     "guarantees" framing, which had no observable consequence anywhere on the page.

     ROUND 21 (2026-08-26) - gate wf_1a57df9d-69d moved to `revise` (no blockers).
     CORRECTNESS, MINE: I had justified making the webhook a placeholder with "the value you would least
     want to hand out". A placeholder gives NO confidentiality, and this page's own shots prove it three
     times - the URL is in the clear in Flow Settings, in the Launch dialog, and in the imported copy. The
     secrecy clause is cut, and the boundary is now stated once, honestly: a placeholder parameterises a
     value, it does not protect one; only the workspace API key store holds a value out of sight.
     LOCATOR CORRECTED BY DRIVING IT: I wrote that stop sits "beside the Live chip". Read off the live
     DOM, the LIVE toolbar runs pause(677) stop(712) clock(747) clone(782) export(817) RunInstance(852),
     so the icon beside the chip is Run Instance. Hovering the square gives the tooltip "Stop". Prose now
     locates it as the square where a Ready version shows play, and names pause as the different thing.
     EMPTY-VALUE CLAIM NOW PICTURED AND DRIVEN ON A FLOW WITH BLOCKS: cleared escalateAbove on 88C3EE86 -
     Condition gained a red "1" badge, chip went Not Ready, and the toolbar play control was disabled
     (button.disabled === true). Recaptured placeholders-no-value.png as ONE frame carrying all three,
     replacing a four-field crop that showed none of them. Value restored to 8; flow Ready.
     PHANTOM PLACEHOLDER REMOVED FROM A SHOT: the round-20 dialog capture invented a third placeholder
     (ticketQueue, declared INT for a queue name) that exists nowhere else. Recaptured by reopening the
     real escalateAbove through its gear, which is also what the surrounding prose now describes.
     ALSO: lede scoped to fields that offer the Expression Editor (an API KEY field and any fixed-choice
     list cannot read one); "the one shared store" absolute cut; the JSON fence now parses (wrapped in its
     executionStaticData array); duplicated type-to-control mapping and clone-carries-values removed.

     ROUND 22 (2026-08-26) - the Stop locator was wrong a SECOND time and the gate caught it again. Round
     21 said "the square where a Ready version shows the play control", but my own DOM read shows pause at
     x=677 and stop at x=712, and on a Ready version play sits at 677 - so PAUSE occupies play's slot and
     my sentence pointed the reader at the one control the same paragraph warns about. The page ships both
     toolbars (placeholders-live-view-mode.png LIVE, placeholders-no-value.png Ready), so this was
     falsifiable from the artifacts I had already shipped. Now: "the square, second from the left,
     immediately right of pause".
     RULE THIS EARNED: a locator repaired in a later round must be re-read against the page's OWN
     before/after screenshots, not against the note that produced the repair. Two wrong locators in one
     sentence across two rounds is the cost of checking a fix against my own working data instead of
     against the pixels the reader will see.

     ROUND 23 (2026-08-26) - gate wf_057553ea-1b8, four blockers.
     THIRD WRONG LOCATOR, then driven: the prose had sent the reader to the Version Admin tab to clone -
     hovering the toolbar copy icon gives the tooltip "Clone". Prose now names the toolbar control. Stop
     was wrong twice before this. All three were written from a note or a DOM dump instead of being read
     back against the screenshots this page ships.
     DESTRUCTIVE OPERATION WAS UNSTATED: the page gave rename a full admonition and presented the trash as
     neutral housekeeping, though deleting a row flags every field that read it AND cannot be undone by
     typing the name back. Consequence now stated where the trash is introduced.
     LEAD-IN/SHOT ORDER: my round-21 edit left "here on escalateAbove, with the Data Type list open:"
     sitting above the PANEL shot, with the dialog shot dropped in cold two images later. Re-matched.
     Ledger screenshot lines and the verdict file were both stale; both rewritten from current pixels.
     STANDING BACK: 22 gate rounds. The page is ~220 body lines / 12 shots against exemplars at 50-75 / 3-6
     (variables.md is 54/4). Round 22 names the cause as accretion and prescribes SUBTRACTION, not a split.
     That is a scope decision for Mark, recorded in the verdict file under "Where this stands".

     ROUND 24 (2026-08-26) - SUBTRACTION PASS. Mark chose Option A: cut to exemplar scale rather than
     split or keep the depth. Result: 224 -> 160 body lines, 12 -> 7 screenshots, 11 -> 7 h2.
     WHAT WENT: the standalone "type you declared", "nothing writes back" and "belongs to one flow
     version" sections (folded into Reading and LIVE, one sentence each); the Launch-dialog h2 (folded
     into Setting a value); the LIVE toolbar geography (two wrong locators lived there - it is now a
     pointer to Running Flows, which owns those controls); duplicated statements of the gear affordance,
     the type-to-control mapping and clone-carries-values.
     WHAT STAYED, deliberately: the eight type tags (a lookup that was wrong twice when derived), the
     empty-value frame (one shot carrying disabled Start + Not Ready + block badge + red field), the
     delete hazard, the "held in the clear" boundary, and the export fence (the page's only checkable
     artifact for the type claim).
     FIVE SHOTS RETIRED with the sections that carried them: bound-in-block, condition-result,
     description-tooltip, launch-dialog, live-view-mode. Files deleted rather than left orphaned; all are
     recapturable from flow 88C3EE86, which is Ready and unchanged.

     ROUND 25 (2026-08-26) - the subtraction pass left CUT RESIDUE and the gate named the class precisely:
     sections were cut and their screenshots deleted while the sentences depending on them stayed behind.
     RESTORED, because each carried a claim with no substitute anywhere on the site:
       - placeholders-live-view-mode.png. The LIVE h2 was teaching a purely VISUAL claim (no right-hand
         tab strip) with zero pixels. This page's history records that same claim as invented in round 3,
         so shipping it evidence-free was the worst possible cut.
       - placeholders-launch-dialog.png. The dialog is load-bearing twice - it is one of the three proofs
         that a value is held in the clear, and the subject of the FR-3460 counter-intuitive claim - and
         the reader could see none of it.
     RETIRED INSTEAD (the gate's own suggested trade): placeholders-renamed-break.png. Its ~320px crop
     showed neither the block nor the error badge the prose promised, and the red-field treatment is
     already shown in placeholders-no-value.png; the rename message is now quoted in the admonition.
     Net 7 -> 8 shots.
     OTHER RESIDUE FIXED: "Setting a placeholder's value" said nothing about WHERE a value is typed (round
     19 added it, round 24 cut it as duplication) - restored, along with the value box in the row
     inventory. The JSON-body sentence pointed at a frame whose body holds an Initial Data reference, not
     a placeholder (round-19 fallout, never swept) - reworded to what the pixels show, which lands the
     configuration-vs-run-data thesis a second time. The cross-flow scope was buried under the LIVE
     heading with an unattributed escape hatch - promoted to its own h2 with Call Flow pilled.
     Also: Start flow named as the product does, the Expression Editor group named, the export
     admonition retitled to what it instructs, and the AI-key aside split out of the receiver's job.

     ROUND 27 (2026-08-26) - gate wf_9c6d076e-edb, down to ONE blocker from four.
     THE BLOCKER, and it was a good catch: the LIVE section said "Placeholder Data has no route there"
     while this page's OWN two shots show Run Instance sitting in the LIVE toolbar and its dialog carrying
     an editable Placeholder Data section. A reader on a LIVE version would find that route, type a new
     threshold and believe they had changed the live configuration - the exact FR-3460 trap the page
     corrects two sections earlier but never joined to the place the reader acts. The clause is now there.
     CONTROL NAMED FROM ITS TOOLTIP: hovering the lightning icon gives "Run Instance"; the dialog it opens
     is titled "Launch Flow Instance". Both are now named correctly. That is the fourth toolbar control on
     this page driven from a tooltip rather than assumed, after Stop (wrong twice) and Clone.
     ABSOLUTE NARROWED BACK: the round-24 subtraction had cut the driven qualifier off "a placeholder
     reaches any field that offers the Expression Editor", leaving an absolute that silently covered
     SubFlow scope - which this log has recorded as NOT DRIVEN since round 6. Restored to "top level and
     inside a loop alike", which is what was actually driven.

     ROUND 29 (2026-08-26) - gate wf_0933c636-b62 reached `revise` (no blockers). Three claims driven on
     the imported copy 873FE6CD so the canonical example was never damaged; the copy was restored to Ready
     afterwards (escalateAbove back to INT 8).
     I HAD THE DELETE CONSEQUENCE WRONG. The page implied re-declaring the name does NOT re-bind ("gone
     rather than recoverable by typing the name back"). Driven: deleting escalateAbove flags the Condition
     with "The placeholder data item is not available" - the SAME message a rename produces - and then
     declaring a placeholder named escalateAbove again flips that field to "The placeholder \"escalateAbove\"
     has no value", i.e. it RE-BINDS by name, and does so even though I re-declared it as STRING against
     an original INT. Binding is by name, independent of type. What does not come back is the value and
     the description. Page corrected to say exactly that. This is the second time an inferred consequence
     shipped as fact on this page; both times the drive contradicted the inference.
     RUN INSTANCE ON A LIVE VERSION: previously composed from two shots taken in two different states.
     Driven properly - started the copy, clicked the lightning control on the LIVE toolbar, and read the
     dialog: it opens, lists both placeholders, and its inputs report readOnly=false / disabled=false.
     The corrective clause is now MERGED into the frozen-values claim instead of parked beside it.
     ALSO: the scope heading said "belongs to one flow" while the page teaches version scope and the LIVE
     remedy depends on two versions holding independent values - retitled to "Placeholders are not shared
     between flows". The security boundary was the tail of a 60-word sentence; it now has a bold run-in.
     "parameterises" and "Sanitise" (the only occurrences of either in content/) are gone.

     ROUND 31 (2026-08-26) - gate wf_664ee969-306, four blockers, TWO OF THEM MY ROUND-29 REGRESSIONS.
     1. THE SECRECY REMEDY WAS A DEAD END. I had written "for a value that has to stay out of sight, use
        the workspace's saved API keys" - for a webhook URL bound into an HTTP Request URL field. But
        api-keys.md:63 says the only flow-side consumer of that store is the AI API Key field on AI
        blocks, and http-request.md has no credentials field: the reader would save the webhook there and
        find nothing able to read it back. This is the SAME defect as the Call Flow escape hatch I removed
        in round 16 - an escape hatch that does not solve the problem it is offered for. Now the boundary
        is stated with no false remedy, and the AI-key exception is scoped to why it works (picked on the
        block, never travels in the flow).
     2. I CREDITED THE PLACEHOLDER FOR THE CONDITION DROPDOWN'S WORK. "escalateAbove is an INT, so the
        Condition gets the number 8" - but branching.md:67 and condition.md both say Value Data Type is
        what decides the comparison, and my OWN round-19 drive showed GREATER_THAN accepts a numeric
        string. Cut to what the export actually proves.
     3. Delete hazard was fused into Declaring and explained by forward-reference to a rename taught two
        sections later. Merged into one h2 covering both, with the shared error string taught once.
     4. Ledger and verdict file stale again; both reconciled.
     EVIDENCE RESTORED: placeholders-renamed-break.png recaptured at full framing (Not Ready chip, error
     badge, red field, message) on the copy flow 873FE6CD, which was renamed and then renamed back; the
     copy is Ready and unchanged.
     THE PATTERN, recorded honestly: round 28 reached `revise` with no blockers and round 29's repairs
     created two. Third time a repair round has added substantive errors. The driven facts hold; what
     keeps failing is the explanation I write around them - a mechanism, a remedy, a reason that went
     past the drive.

     ROUND 33 (2026-08-26) - gate wf_5ab9dd6e-22f, three blockers, all mine again.
     1. MIS-INDENTED ADMONITION. My round-31 edit indented the warning's first body line 8 spaces instead
        of 4, so Python-Markdown rendered that sentence as a CODE BLOCK and orphaned the rest. doclint is
        0/0 on it - nothing mechanical catches this. Fixed, and this time VERIFIED BY RENDERING: ran the
        fragment through markdown+admonition and asserted no <pre> in the output. Render-check, do not
        eyeball the source.
     2. I DENIED A STORE THAT EXISTS. "There is no store a flow can read a secret back from at run time"
        is disproved by platform/oauth-connections.md (sign in once, every block from that extension picks
        the connection up) and by api-keys.md's Custom tab. Worse, the worked example posts to Slack -
        a service that workspace has an OAuth connection for - so the reader with a real answer was told
        none exists. Rewritten to ROUTE (OAuth connection for an account you sign in to, API Keys for an
        AI provider key, both picked on the block) and to keep only the true residue: a bare URL or token
        with no field to pick it in has nowhere else to go.
        This is the SECOND round running that I over-reached on this exact paragraph, and the second time
        the fix was to state less and route more.
     3. LEDGER SAID EIGHT SHOTS, PAGE SHIPPED NINE, and listed the restored renamed-break as retired -
        while my round-31 row claimed both files were "reconciled". Corrected.
     ALSO: the round-31 rename shot was captured on the imported copy, so its breadcrumb read "Triage
     (from Ops)" four sections before the page introduces that flow. Recaptured on the canonical Ticket
     Triage (renamed, captured, renamed back; flow is Ready).

     ROUND 34 (2026-08-27) - MARK'S OWN REVIEW, 15 items. This is the review that mattered; the gate had
     been polishing prose that was fundamentally over-written. His verdict: "The further I go in the
     article, the more hard to read and hard to understand your language gets... YOU are inventing PhD
     level constructs to describe a children's toy."
     STRUCTURAL: Flow Catalog moved up to the intro (was the closing section) and no longer claims the
     Catalog "is being built around placeholders" - it uses them; do not elevate a technical detail into
     the whole purpose. 191 -> 150 body lines, 9 -> 8 sections.
     CUT ENTIRELY, all as irrelevant or confusing to a reader: the credentials/OAuth/API-Keys paragraph
     (Mark: "Why even bring up credentials, oauth, etc here?"); the Shared Memory sentence (unrelated
     concepts); the raw export JSON fence ("We do not study or document that format anywhere"); the
     "Nothing about an imported flow looks wrong..." paragraph; the HTTP body / Initial Data aside
     ("Who cares about the Body here?"); "Starting a run is not a second way in"; "top level of the flow
     and inside a loop alike"; "a field that offers only a fixed list of choices cannot be pointed at
     one" (Mark: "I invented this product and still do not know what you meant here").
     REWRITTEN SIMPLER: the type list is now a TABLE (Data Type / how you enter the value / how it shows
     in the list) - the old run-on prose and "a saved row wears its type as a lower-case tag" were
     unintelligible even to Mark. Reading a placeholder is now one sentence: every placeholder appears as
     a pill in the Expression Editor. Setting a value: "type it into the box on its row". The LIVE
     sentence is completed ("opens read-only, in view mode").
     BEHAVIOUR CORRECTED PER MARK: the Launch Flow Instance dialog's Placeholder Data section is a BUG
     (FR-3460) and will be correct in production before this publishes - values entered there stay with
     the placeholders and apply to that run. The page now documents that expected behaviour, NOT the
     current defect, and no longer says the values land in Initial Data.
     Also: the INT declaration is recalled where escalateAbove is used, so the reader does not scroll
     back; and no runtime claim is attached to it (the Value Data Type mechanism stays on Branching).

     ROUND 35 (2026-08-27) - THE TYPE TABLE, NOW DRIVEN. Every one of the eight rows was exercised on
     Triage (from Ops) (873FE6CD-...) by declaring one throwaway placeholder and cycling its Data Type
     through the list, reading the value control and the list tag off the live DOM each time. The
     throwaway was deleted; the flow's own two placeholders and their values are untouched.
     TWO ROWS WERE WRONG and are corrected: JSON OBJECT and JSON ARRAY have NO JSON editor beside the
     field - the value control is a plain text input, identical to STRING's (w=262), and each row carries
     exactly two buttons, a settings/edit and a trash, the same pair every other row carries. That claim
     came from June orientation notes and had never been re-observed.
     ALSO SHARPENED: INT and DOUBLE are input type=number (a number box, not a plain text box). DATETIME
     opens an rdp calendar popover whose lower half reads Time / 00:00 / Hour / Minute with NOW and DONE
     buttons - hence "pick a date on a calendar, then an hour and a minute".
     CONFIRMED AS WRITTEN: BOOLEAN / CHECKBOX is a dropdown offering exactly Yes and No; API KEY is a
     picker; tags render [string] [int] [double] [boolean] [datetime] [object] [array] [api_key]; the
     Data Type list holds exactly those eight options in that order. -->
# Placeholders

A flow you hand to someone else has to say what it needs from whoever sets it up. In **FlowRunner™** you
declare each of those settings on the flow version as a **placeholder** - a name, a type and a description
- and any field that needs the setting reads it from that one list.

Take a support flow that triages incoming tickets. The ticket differs every run, arriving with the run as
Initial Data or on the trigger block that started the run. How urgent a ticket has to be before it is
escalated, and the webhook its summary is posted to, are the same on every run and different for every
team that adopts the flow. Those two are its placeholders - `escalateAbove` and `notifyWebhook`.

This is also how a flow published to the **Flow Catalog** will state its configuration: whoever installs
it will be asked for each placeholder in turn, described in the words you wrote.

## Declaring a placeholder

Placeholders belong to a flow version, and you manage them in the flow editor's ((Flow Settings)) tab -
the gear at the top of the right panel - under **Placeholder Data**:

![The flow editor's right panel with the gear tab selected in its three-icon tab strip. Below a Flow Memory card, the Placeholder Data card lists two rows, each with a question-mark icon, a gear and a trash icon: notifyWebhook [string] set to https://hooks.example.com/triage/T29F4B1, and escalateAbove [int] set to 8. A plus sits below the list.](../../images/learn/placeholders-panel.png)

The plus below the list opens a dialog to declare a new placeholder. You give it a ((Name)), a
((Data Type)) and a ((Description)). The name has to be unique within the version, and the dialog will
not save without one. The gear beside a saved row reopens the same dialog, where you can change the name
and the type:

![The placeholder dialog reopened on escalateAbove: Name reads escalateAbove, Description reads "Urgency score above which a ticket is escalated", and the Data Type control shows INT. Its open list runs STRING, INT, DOUBLE, BOOLEAN / CHECKBOX, DATETIME, JSON OBJECT, JSON ARRAY and API KEY, each with an icon and INT ticked, and while open it covers the dialog's CLOSE and SAVE row. Behind the dialog the Placeholder Data card shows the flow's notifyWebhook row.](../../images/learn/placeholders-new-dialog.png)

The ((Data Type)) decides how you enter the value, and each saved placeholder shows its type next to its
name in the list:

| Data Type | How you enter the value | Shown in the list as |
| --- | --- | --- |
| ((STRING)) | Type it into a text box | `[string]` |
| ((INT)) | Type it into a number box | `[int]` |
| ((DOUBLE)) | Type it into a number box | `[double]` |
| ((BOOLEAN / CHECKBOX)) | Pick Yes or No | `[boolean]` |
| ((DATETIME)) | Pick a date on a calendar, then an hour and a minute | `[datetime]` |
| ((JSON OBJECT)) | Type the JSON into a text box | `[object]` |
| ((JSON ARRAY)) | Type the JSON into a text box | `[array]` |
| ((API KEY)) | Pick one of the AI keys saved in the workspace | `[api_key]` |

((API KEY)) draws on the workspace's [API Keys](../../platform/api-keys.md) and holds an AI provider key
only. No block reads a key from a placeholder yet.

Write the ((Description)) even though it is optional. It shows on the question-mark beside the name, and
it is the only explanation that travels with the flow. The trash removes a row, after a confirmation.

## Setting a value

To give a placeholder its value, type it into the box on its row in ((Flow Settings)). That value is what
every run of this version uses.

You can also supply a value for one run without changing the version: ((Run Instance)) - the lightning
icon in the toolbar - opens a ((Launch Flow Instance)) dialog with a **Placeholder Data** section, filled
in from the version. Change a value there and that run uses it.

![A Launch Flow Instance dialog. Under Configuration Data, an Initial Data table lists the key urgency with its value box empty, and a Placeholder Data card below it holds escalateAbove[int] set to 8 and notifyWebhook[string] set to https://hooks.example.com/triage/T29F4B1.](../../images/learn/placeholders-launch-dialog.png)

Leave a value empty and every field reading it turns red, which takes the version to **Not Ready** and
leaves ((Start flow)), the play control in the toolbar, disabled until every placeholder a block reads has
a value:

![The Ticket Triage flow with escalateAbove's value cleared. In the toolbar the play control is greyed out and the version chip reads Not Ready; on the canvas the "Urgent enough to escalate?" Condition carries a red 1 error badge; and in its configuration panel the Value field shows the escalateAbove reference in red with a warning triangle, above the message "The placeholder \"escalateAbove\" has no value".](../../images/learn/placeholders-no-value.png)

A placeholder value is stored as you typed it. It is readable in ((Flow Settings)), it shows in the
((Launch Flow Instance)) dialog, and it travels in the export file, so anyone who can open the flow can
read it.

## Reading a placeholder in a flow

Every placeholder you declare appears as a pill in the [Expression Editor](expressions.md), in a
**Placeholder Data** group of its own:

![The Expression Editor dialog, subtitled "Urgent enough to escalate? > Condition - Value", with the Variables tab selected. A FLOW CONTEXT group lists Workspace ID, Execution ID, Flow ID, Initial Data and Shared Memory; a PLACEHOLDER DATA group below it holds exactly two pills, notifyWebhook and escalateAbove; OPERATORS and COMMON VALUES groups sit below that; and the expression canvas on the right holds an inserted escalateAbove reference.](../../images/learn/placeholders-expression-editor.png)

Pick the pill and the field reads that placeholder. Here the
[Condition](../../reference/condition.md){.fr-block} compares each ticket's urgency against
{{escalateAbove}} - the ((INT)) placeholder declared earlier - and the Post escalation summary step
([HTTP Request](../../reference/http-request.md){.fr-block}) posts to {{notifyWebhook}}:

![The configuration panel of an HTTP Request block named "Post escalation summary": the URL field holds a single purple notifyWebhook token, HTTP Method reads POST, and the Body reads {"urgency": followed by a purple Initial Data to urgency token, then , "text": "Ticket escalated"}.](../../images/learn/placeholders-in-request-body.png)

The field holds a reference, not a copy of the value, so changing the value in ((Flow Settings)) reaches
every field that reads it and no block has to be reopened. Nothing writes back the other way: a value
that has to change while a run works is a [Data Bucket variable](variables.md).

## Renaming or removing a placeholder breaks the fields that read it

Both leave every field that read the placeholder flagged with "The placeholder data item is not
available", an error marker on the block, and the version back to **Not Ready**:

![The Ticket Triage flow after escalateAbove was renamed. The toolbar's play control is greyed out and the version chip reads Not Ready; the "Urgent enough to escalate?" Condition on the canvas carries a red 1 error badge; and in its configuration panel the Value field shows the escalateAbove reference in red with a warning triangle, above the message "The placeholder data item is not available".](../../images/learn/placeholders-renamed-break.png)

!!! warning "The fields do not re-point themselves"

    A block's default result alias follows the block when you rename it, and the steps reading it
    re-point themselves. A placeholder does not: rename `escalateAbove` to `escalationFloor` and the
    [Condition](../../reference/condition.md){.fr-block} still asks for {{escalateAbove}}. You have to
    repoint every field yourself, so name a placeholder before you start binding it.

    Deleting is the one with a way back. Declare a placeholder with the same name again and those fields
    re-point to it - they then ask for a value. What does not come back is the value and the description
    you had.

## Changing a value on a LIVE version

Open a **LIVE** version in the editor and it opens read-only, in view mode: there is no right-hand tab
strip, so ((Flow Settings)) is not there and its values cannot be changed while it stays LIVE.

![The Ticket Triage flow open at Version 1 with a green Live chip in the toolbar. The first tab reads View rather than Edit. On the canvas, Start leads into the "Urgent enough to escalate?" Condition, whose Yes branch runs "Post escalation summary" and whose No branch runs "Queue normally". The whole right-hand side of the window is empty - no tab strip and no settings panel.](../../images/learn/placeholders-live-view-mode.png)

Only one version is LIVE at a time, so there are two ways to change a value. Stop the version and it comes
back as an editable draft, but nothing runs while it is down. Or clone it, change the value on the copy
and start the copy: the copy takes over and the original steps aside, so the automation never stops.
[Running Flows](../../run/running-flows.md) covers both controls. A clone carries the declarations and
their values, so the copy already holds the configuration you had.

## Placeholders are not shared between flows

<!-- doclint: no-shot: a scope boundary, not a surface - there is nothing on screen that shows the
     absence of sharing, and the Call Flow mention is a cross-reference to that block's own page -->

A second flow declares its own placeholders. Where one flow calls another, a
[Call Flow](../../reference/call-flow.md){.fr-block} step can pass the value in as Initial Data, and the
called flow reads it there instead of declaring its own.

## A copy arrives with your values in it

A flow travels by being exported to a file and imported somewhere else - see
[Flows](../../manage/flows.md) - and the placeholder values travel with it. The imported copy already
holds the values the author had, so the first thing to do with a flow you receive is work down the list
and replace them with your own:

![The flow editor for a flow named "Triage (from Ops)" in the breadcrumb, freshly created by importing an exported file. The version chip reads Ready. On the canvas, Start leads into a Condition named "Urgent enough to escalate?" whose Yes branch runs "Post escalation summary" and whose No branch runs "Queue normally", with no error marker on any block. The Placeholder Data card on the right already holds notifyWebhook set to https://hooks.example.com/triage/T29F4B1 and escalateAbove set to 8.](../../images/learn/placeholders-imported-prefilled.png)

!!! warning "Replace live values before you export"

    A webhook URL is live, and anyone holding the export file can post to it. Clone the version, put
    stand-ins on the clone, export the clone and delete it, so the version you actually run is untouched.
    Say in the ((Description)) what has to be replaced.

## Related

- [Variables and Data Buckets](variables.md) - values that change while a run works
- [Shared Memory](shared-memory.md) - values that outlive a single run
- [Expressions](expressions.md) - how a field reads a placeholder, and what else it can read
- [API Keys](../../platform/api-keys.md) - the workspace store an API KEY placeholder draws on
- [Flows](../../manage/flows.md) - versions, cloning, export and import
- [Running Flows](../../run/running-flows.md) - starting, pausing and stopping a version
