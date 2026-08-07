export const meta = {
  name: 'concept-page-review',
  description: 'Adversarial pre-handoff gate for a NARRATIVE concept page: educator + guideline-compliance + definition-of-done + product-fidelity lenses. Unlike the reference-page reviewer, product-fidelity and screenshot coverage DO gate the verdict. Emits ship | revise | major-rework + a work list.',
  phases: [
    { title: 'Review' },
    { title: 'Synthesize' },
  ],
}

// --- resolve the page path: accept a bare name ("shared-memory") or a full/relative path ---
// NO SILENT DEFAULT: named-workflow invocations have been observed to drop `args` entirely
// (2026-08-06: two runs meant for ai-in-flows silently reviewed shared-memory). If args are
// missing, fail loudly - the caller then copies this script and hard-sets the page.
const CONCEPTS = '/Users/mark/dev/documentation/automations/content/learn/concepts'
const RAW = (args && (args.page || args.path)) || (() => {
  throw new Error('concept-page-review: no {page} arg reached the script. Copy the script, hard-set RAW to the page path, and run via scriptPath.')
})()
// Relative paths are taken from automations/content/ - "build/x.md" and "content/build/x.md"
// both work; bare names resolve in the Learn concepts folder.
const PAGE = RAW.includes('/')
  ? (RAW.startsWith('/') ? RAW
    : `/Users/mark/dev/documentation/automations/content/${RAW.replace(/^content\//, '')}`)
  : `${CONCEPTS}/${RAW.replace(/\.md$/, '')}.md`

const ROOT = '/Users/mark/dev/documentation/automations'
const PATTERN = `${ROOT}/docs-review/CONCEPT-PAGE-PATTERN.md`
const VOICE = `${ROOT}/block-knowledge/VOICE.md`
const DOD = `${ROOT}/tools/doclint/DEFINITION_OF_DONE.md`
const LEDGER = `${ROOT}/docs-review/PLATFORM-REVIEW-LEDGER.md`

// Gating lenses (educator / guideline / definition-of-done) each return findings.
const FINDINGS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    lens: { type: 'string' },
    overall: { type: 'string', description: 'One-paragraph verdict from this lens' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          section: { type: 'string' },
          severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] },
          quote: { type: 'string', description: 'Short verbatim excerpt of the offending text (or the missing thing)' },
          rule: { type: 'string', description: 'The specific rule/principle from the rubric this violates' },
          issue: { type: 'string' },
          suggestion: { type: 'string' },
        },
        required: ['section', 'severity', 'issue', 'suggestion'],
      },
    },
  },
  required: ['lens', 'overall', 'findings'],
}

// Fidelity emits a checklist of falsifiable product claims. It cannot verify them itself,
// so it does not assign severities - but the synthesis GATES on high-risk unbacked claims.
const CHECKLIST_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    lens: { type: 'string' },
    overall: { type: 'string' },
    items: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          claim: { type: 'string', description: 'The exact UI label, value, location, operation, or behavior asserted' },
          location: { type: 'string', description: 'Section + short quote where it is asserted' },
          backing: { type: 'string', enum: ['screenshot', 'verification-note', 'prose-only'], description: 'What currently substantiates it in the page' },
          risk: { type: 'string', enum: ['high', 'medium', 'low'], description: 'How badly a reader is misled if it is wrong' },
          verify: { type: 'string', description: 'Exactly what to drive/click/read in the live product to confirm it' },
        },
        required: ['claim', 'location', 'backing', 'risk', 'verify'],
      },
    },
  },
  required: ['lens', 'overall', 'items'],
}

const REPORT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    verdict: { type: 'string', enum: ['ship', 'revise', 'major-rework'] },
    summary: { type: 'string' },
    workList: {
      type: 'array',
      description: 'Everything that must be fixed/verified before ship, ordered by severity. YOU (the author) clear these - never Mark.',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] },
          kind: { type: 'string', enum: ['educator', 'guideline', 'definition-of-done', 'verify-in-product'] },
          section: { type: 'string' },
          issue: { type: 'string' },
          fix: { type: 'string' },
          raisedBy: { type: 'array', items: { type: 'string' } },
        },
        required: ['severity', 'kind', 'section', 'issue', 'fix'],
      },
    },
  },
  required: ['verdict', 'summary', 'workList'],
}

const COMMON = `You are an adversarial reviewer of a NARRATIVE FlowRunner concept page (hand-authored, in the Learn nav). Your job is to FIND violations before Mark ever sees the page - Mark being the product owner who has repeatedly caught what earlier passes missed.

Read these first (use the Read tool), and treat them as the binding rubric - not your own taste:
- The page under review: ${PAGE}
- The educator method + recurring corrections: ${PATTERN}
- The voice, screenshot & formatting standard: ${VOICE}

Screenshots are Markdown images written as ![alt](../../images/AREA/NAME.png). Do NOT trust the alt text alone - it was written by the same author and can carry the same blind spot (this is exactly how a screenshot showing the DEFAULT of a setting slipped past a page teaching the NON-default). When your lens needs to judge an image, resolve its path to ${ROOT}/content/images/AREA/NAME.png and Read the actual PNG (you can see images); judge what the PIXELS actually show against what the section teaches, and whether the alt text matches the pixels.

CALIBRATION - do not assert a defect you cannot prove from the pixels (Mark, 2026-07-06, after the gate over-flagged two CORRECT Expression Editor shots). Two rules: (1) If you cannot confirm from the pixels that a screenshot is wrong - e.g. you SUSPECT a shot shows a different mode/state but cannot verify it - do NOT call it a blocker or assert the defect; record it as a low-confidence item of kind "verify" addressed to Mark ("verify this shot is <X> not <Y>"), severity minor. Assert a screenshot defect ONLY when the pixels plainly show it. (2) A fair prose DESCRIPTION of a group of UI controls in plain words (e.g. "your Data Bucket variables" for the VARIABLES groups) is NOT a label mismatch; flag a label error only when the prose QUOTES a literal UI label that the screen contradicts. Stay adversarial on what the pixels prove; downgrade what you merely suspect.

Be specific and stingy: every finding quotes the offending text (or names the missing thing), cites the exact rubric rule it breaks, names its section, and proposes a concrete fix. Do not invent problems to look thorough - if the page is strong on your lens, say so and return few or no findings. Severity: blocker (misleads, fails to teach, or breaks a hard rule), major (notably weakens the page or skips a required element), minor (polish), nit (trivial).`

const LENSES = [
  {
    key: 'educator',
    schema: FINDINGS_SCHEMA,
    prompt: `${COMMON}

YOUR LENS - Educator quality (CONCEPT-PAGE-PATTERN sections 0, 0b, 0c). This is a QUALITY judgment, not a checkbox. Ask:
- Does the LEDE open on VALUE/OUTCOME - what the builder's automation gets to DO - not on mechanics (any machine description, UI or data-plumbing)? If the lede could open an architecture spec, it is a blocker.
- Is EVERY section title a meaningful anchor - can a reader say what the section taught from the title alone?
- One idea per section; does each section open on value/purpose before mechanics?
- Does it build on what earlier Learn-nav pages already taught, without re-explaining, contradicting, or forward-referencing?
- Is it plain? Flag poetic scene-setting, over-explaining elementary ideas, "you already met / back in X" scaffolding, reflex cross-links, and defensive sentences that answer a question no one asked.
Anchor your bar to the approved exemplars (Variables, Expression Editor). Return findings.`,
  },
  {
    key: 'guideline',
    schema: FINDINGS_SCHEMA,
    prompt: `${COMMON}

YOUR LENS - Guideline compliance. Check the page against EVERY recurring correction in CONCEPT-PAGE-PATTERN sections 0d AND 0g, and the formatting rules in VOICE.md. Flag any breach, quoting it:
- Trigger-as-start framing (a flow can start with anything; Initial Data = data sent at start; a trigger's data lives on the trigger block).
- A main documented concept with no screenshot of its real scenario.
- Two distinct concepts combined under one heading (should be split); or a feature's INPUT and OUTPUT mixed in one section.
- A UI location asserted that reads as a guess rather than something verified.
- Expression syntax ({{...}} / {{+}}) presented as copy-pasteable text rather than built in the Expression Editor.
- Reference-hierarchy errors: block refs not green pills, UI controls not ((chips)), field labels/section names not bold, concept terms not glossary; misuse of the trademark (once, near top).
- em-dashes, banned filler words, "in order/then...then" implying linear-only execution.
- PRODUCT-TERM PRECISION: a word used that names a DIFFERENT product feature (e.g. "repetition" for why you make a subflow - repetition is the Repeat/List Iterator blocks; the right word is "reuse"). Flag any such collision.
- SCOPE NOT STATED: a feature page that never names the feature's boundary and escape hatch (e.g. a subflow is flow-scoped, not shared across flows -> Call Flow / Flows as Actions).
Return findings (blocker for the recurring-correction/term/scope breaches; major/minor for formatting).`,
  },
  {
    key: 'definition-of-done',
    schema: FINDINGS_SCHEMA,
    prompt: `${COMMON}

Also read: ${DOD} and ${LEDGER}.

YOUR LENS - Definition of done (BLOCKING). Confirm the page is actually finished, not just lint-clean. YOU MUST OPEN EACH IMAGE - Read every PNG the page references (resolve ../../images/AREA/NAME.png to ${ROOT}/content/images/AREA/NAME.png) and look at the actual pixels. For each:
- SHOT DEMONSTRATES ITS CONCEPT (the miss that got past five reviews): does the image actually SHOW the section's real scenario IN ACTION, or a default / empty / merely-related panel? A section teaching "anchor to the caller" whose shot shows the anchor at its DEFAULT value is a BLOCKER - the picture shows the opposite of the lesson. A section showing a value being written/read/deleted must show that, not a blank form.
- ALT-TEXT MATCHES PIXELS: the alt text describes what is actually in the image (right control, right values, right layout - e.g. block arrangement), not what the author wished it showed. A mismatch is a blocker.
- SCREENSHOT COVERAGE: every main documented concept/action carries a real screenshot of its REAL named scenario. A documented action with no shot is a blocker.
- LEDGER: this page has a section in PLATFORM-REVIEW-LEDGER.md and every item is cleared with evidence; flag any open or evidence-free item.
- No "SCREENSHOT NEEDED" / "@MARK TODO" / owed-shot markers left in the body.
- CONTROL COMPLETENESS: for every control the page NAMES that has multiple states or options (a toggle, a dropdown, a mode), does the page document ALL of them, or only the one a static shot happens to show? Flag any control described in a single state with its other states unmentioned ("Compose Result ON / JSON is described - where is OFF? what other Content Types exist?"). Check the page for a product-exploration log (an HTML comment recording every state the author drove); its ABSENCE for a page full of controls is itself a flag.
In each image finding, state WHAT THE PIXELS SHOW vs what the section needs. Return findings (a shot that shows the default/opposite of its concept, an alt/pixel mismatch, a missing shot, an under-documented control, or an open ledger item = blocker).`,
  },
  {
    key: 'quality',
    schema: FINDINGS_SCHEMA,
    prompt: `${COMMON}

YOUR LENS - Whole-page craft (HOLISTIC - judge the page as a whole, NOT paragraph by paragraph). Read the ENTIRE page once, start to finish, as a real reader would. Form an OVERALL impression first: does it read like the work of someone who knows and LIKES the product - coherent, purposeful, engaging from top to bottom - or like indifferent, box-ticking prose? Only after that overall read, point to the FEW specific places (if any) that genuinely drag the whole page down. Do NOT walk paragraph-by-paragraph emitting a verdict on each; do NOT return a finding per paragraph.

Flag ONLY genuinely weak spots that a real reader would notice: real filler or restatement a reader would skip; a passage that teaches nothing where it should; a place the page goes flat and loses the reader; or - the highest-value catch on this lens - a break in a RUNNING EXAMPLE, where a consecutive section swaps in an unrelated example or screenshot instead of building on the one before it (e.g. a Get New Token walkthrough whose middle shot shows a DIFFERENT subflow). Quote the spot and give a concrete fix.

CALIBRATION (mirror the screenshot rule - do NOT manufacture findings from taste): a paragraph that is merely plain, functional, or not to your personal taste but is clear, correct, and earns its place PASSES - say nothing about it. Flag a passage as failing ONLY when you can point to a concrete, defensible reason a real reader is worse off for it. A competent, clear page with no dead weight and a consistent running example is a PASS on this lens even if no single line dazzles - do NOT block a sound page hunting for sparkle, and do NOT keep a page open just because some line could be marginally livelier. Anchor to the approved exemplars (Variables, Expression Editor) as the bar to aim for, not as a demand that every line match them.

In 'overall', give your holistic read of the page's craft in two or three sentences. Severity: a genuinely boring/useless/teaching-free PASSAGE, or a running-example continuity break, is major; a smaller drag is minor. If the page reads well as a whole, return few or no findings and say so plainly.`,
  },
  {
    key: 'redteam',
    schema: FINDINGS_SCHEMA,
    prompt: `${COMMON}

YOUR LENS - Red team. The other lenses check a KNOWN checklist, and that checklist is built from failures Mark already caught - so it is, by construction, incomplete. Your ONLY job is to find a problem that NONE of the standing rules would catch. Assume the page has a defect the rubric is blind to, and go find it. Read the page as Mark would - a product owner who knows the product cold and cares about it - and ask: what would make him wince that no rule here mentions? Look especially for: a claim that is subtly WRONG about how the product actually behaves; an example or number that does not add up; a place where the reader is quietly left confused or mistrustful; an omission a real builder would hit within five minutes of trying this; a sentence that is technically allowed but that a person who cared would never ship. Do NOT just re-report obvious rule breaches the other lenses own. Name NEW classes of problem, quote the spot, and say what principle it violates (even if that principle is not yet written down) - those become tomorrow's rules. If you genuinely find nothing new, say so plainly rather than inventing filler. Return findings.`,
  },
  {
    key: 'fidelity',
    schema: CHECKLIST_SCHEMA,
    prompt: `${COMMON}

YOUR LENS - Product-fidelity checklist. You CANNOT open the product, so you do not pass judgment - you EXTRACT every concrete, falsifiable product claim the page makes and say how well the page currently backs it. List each: the exact claim (a UI label, a control's LOCATION, a dropdown's options, an operation name, a runtime behavior), where it appears, its backing, its risk (high = a wrong value or location misleads the reader or breaks their flow), and exactly what to drive in the live product to confirm it. Backing is one of: "screenshot" (a shot on the page visibly shows that exact label/option/location), "verification-note" (the page carries a dated HTML-comment note - of the form "verified DATE: what was driven and seen" - explicitly covering this claim, whether by a driven behavior, a documented V-run, or the product owner's direct confirmation), or "prose-only" (asserted with neither). A runtime behavior a static shot cannot show (e.g. "Override on = replace in place") is backed by a verification-note, not by a screenshot of the toggle alone. Be exhaustive about locations and option lists specifically - those are the claims that have been wrong before ("gear in the toolbar", the expiration options). Do NOT list generic prose that asserts no product fact. Return the checklist.`,
  },
]

phase('Review')
const results = await parallel(
  LENSES.map((l) => () => agent(l.prompt, { label: `review:${l.key}`, phase: 'Review', schema: l.schema }))
)
const [educatorR, guidelineR, dodR, qualityR, redteamR, fidelityR] = results
const gating = [educatorR, guidelineR, dodR, qualityR, redteamR].filter(Boolean)

phase('Synthesize')
const synth = await agent(
  `You are the editor consolidating an adversarial pre-handoff review of the FlowRunner concept page ${PAGE}. The rubric is ${PATTERN} + ${VOICE} + ${DOD}.

GATING lens findings (educator / guideline / definition-of-done / per-paragraph quality / red-team) - JSON:
${JSON.stringify(gating, null, 2)}

Note: the whole-page CRAFT lens and the RED-TEAM lens are both load-bearing. A page that reads as indifferent/box-ticking, or that breaks its running example, must NOT ship even if otherwise clean - BUT a clear, competent page with no dead weight and a consistent running example PASSES the craft lens even if no single line dazzles; do NOT keep such a page open for want of sparkle (the craft lens only emits MAJORS for genuinely weak passages, not for taste). And a real red-team finding (a NEW class of defect no rule covers) is gating too, AND should be flagged in the summary as a candidate new rule for the guidelines.

PRODUCT-FIDELITY checklist - JSON:
${JSON.stringify(fidelityR, null, 2)}

Produce a single report:
1) workList: merge everything the author must do before ship into one ordered punch-list. Include (a) every gating finding of severity blocker/major (and notable minors), tagged with its kind, deduped with raisedBy listing each lens; and (b) fidelity checklist items that are NOT yet substantiated - convert each into a work item of kind "verify-in-product". A claim counts as substantiated (do NOT make it a work item) when its backing is "screenshot" (a shot ON THE PAGE visibly shows that exact label/option/location - the author captured it live from the product) OR "verification-note" (the page carries a dated HTML-comment note recording that this claim was confirmed in-product - e.g. a runtime behavior driven in a demo flow, a documented V-run, or the product owner's direct confirmation). Only "prose-only" is unfinished: a prose-only high-risk claim becomes a work item at severity major, medium/low a minor. (A label/location/option shown in a page screenshot is done. A runtime BEHAVIOR needs a verification-note, since a static shot cannot show it.) IMPORTANT - a verification-note counts whether the note records the behavior as (i) driven live, (ii) the product owner's direct confirmation, or (iii) quoted verbatim from the product's OWN tooltip/documentation. A note that also honestly says a behavior was "not independently driven this session" is STILL substantiated if it carries one of those three backings - do NOT demand a live drive for it or downgrade it for the honesty caveat. Only a behavior with none of the three (pure author inference) is a work item.
2) verdict: "ship" ONLY IF there are no blocker or major items of ANY kind in the workList - i.e. the page teaches well, breaks no guideline, shows every concept, and every high-risk product claim is substantiated by a screenshot or a verification note. "revise" if there are majors but the spine is sound. "major-rework" if there are blockers or pervasive problems.
3) summary: two or three sentences - is it ready, and if not, what is the theme of what remains.

The author (not Mark) clears the work list, including driving the product to verify claims, then re-runs this review. Be honest and concrete; do not soften to reach "ship".`,
  { label: 'synthesize', phase: 'Synthesize', schema: REPORT_SCHEMA }
)
return synth
