export const meta = {
  name: 'docs-content-review',
  description: 'Review a generated block-reference page: educator/story/beginner lenses gate the verdict; product-fidelity emits a separate verify-in-product checklist that never blocks the verdict',
  phases: [
    { title: 'Review' },
    { title: 'Synthesize' },
  ],
}

const PAGE = (args && args.page) || '/Users/mark/dev/documentation/automations/content/reference/list-iterator.md'
const VOICE = '/Users/mark/dev/documentation/automations/block-knowledge/VOICE.md'

// Teaching lenses (educator/story/beginner) produce findings that GATE the verdict.
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
          quote: { type: 'string', description: 'Short verbatim excerpt of the offending text' },
          issue: { type: 'string' },
          suggestion: { type: 'string' },
        },
        required: ['section', 'severity', 'issue', 'suggestion'],
      },
    },
  },
  required: ['lens', 'overall', 'findings'],
}

// The fidelity lens produces a CHECKLIST, not gating findings. It cannot verify product
// behavior, so it never assigns blocker/major - it lists claims to confirm in the live product.
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
          claim: { type: 'string', description: 'The exact product label, value, operation, or behavior asserted' },
          location: { type: 'string', description: 'Section + short quote where it is asserted' },
          backing: { type: 'string', enum: ['screenshot', 'prose-only'] },
          risk: { type: 'string', enum: ['high', 'medium', 'low'], description: 'How badly a reader is misled if the claim is wrong' },
          verify: { type: 'string', description: 'Exactly what to check in the live product' },
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
    verdict: { type: 'string', enum: ['ship', 'revise', 'major-rework'], description: 'Based ONLY on the teaching lenses; the fidelity checklist never changes it' },
    summary: { type: 'string' },
    prioritized: {
      type: 'array',
      description: 'Teaching findings (educator/story/beginner) that gate the verdict',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] },
          section: { type: 'string' },
          issue: { type: 'string' },
          fix: { type: 'string' },
          raisedBy: { type: 'array', items: { type: 'string' } },
        },
        required: ['severity', 'section', 'issue', 'fix', 'raisedBy'],
      },
    },
    verifyInProduct: {
      type: 'array',
      description: 'Deduped fidelity checklist - informational, ordered by risk; does NOT affect the verdict',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          claim: { type: 'string' },
          location: { type: 'string' },
          backing: { type: 'string', enum: ['screenshot', 'prose-only'] },
          risk: { type: 'string', enum: ['high', 'medium', 'low'] },
          verify: { type: 'string' },
        },
        required: ['claim', 'backing', 'risk', 'verify'],
      },
    },
  },
  required: ['verdict', 'summary', 'prioritized', 'verifyInProduct'],
}

const COMMON = `You are reviewing a generated FlowRunner documentation page for the Block Reference.

Read these two files first (use the Read tool):
- The page under review: ${PAGE}
- The voice & content standard it must meet: ${VOICE}

The page is generated from a YAML record; do NOT flag formatting the generator controls (heading order, tables, link syntax, blank lines). Screenshots are referenced by Markdown image alt text - treat the alt text as a faithful description of what each screenshot shows, and review the teaching, not the pixels.

Be specific and stingy. Every finding must quote the offending text, name its section, and propose a concrete fix. Do not invent problems to look thorough - if the page is strong on your lens, say so and return few or no findings. Severity: blocker (misleads or fails to teach), major (notably weakens learning), minor (polish), nit (trivial).`

const TEACHING = [
  {
    key: 'educator',
    prompt: `${COMMON}

YOUR LENS - Educator / core message. For each section ask: does it do its ONE job? The lede says what the block does; How it works teaches how THIS block works; When to use frames the decision; the Example is one worked scenario. Flag:
- General, cross-cutting FlowRunner facts placed in a section whose job is narrower (e.g. platform-wide expression syntax inside How it works). A true detail in the wrong section is a defect.
- Restating the lede, cataloguing details instead of teaching a model, or burying the core message under tangents.
- Anything that makes a reader stop to absorb a side-fact instead of the section's single idea.
Return findings.`,
  },
  {
    key: 'story',
    prompt: `${COMMON}

YOUR LENS - Story / progressive build-up. Read the Example as a narrative. Ask:
- Is the goal stated before the machinery is built, so each step has a target?
- Is it ONE coherent worked scenario, carried through with consistent data and names?
- Is anything used before it is introduced (a value, variable, or term)? Does each step build on the prior one?
- Does it pay off - does the reader end knowing what happened and what they now have?
- Do the screenshots land at the right moment, each earning its place?
Flag gaps, jumps, or out-of-order steps. Return findings.`,
  },
  {
    key: 'beginner',
    prompt: `${COMMON}

YOUR LENS - Beginner accessibility. Assume the reader is new to FlowRunner. Ask:
- Is any term, label, or concept used without being grounded the first time it appears? (Exception: terms VOICE.md marks as glossary terms are correctly linked, not redefined inline - do not ask to unpack those.)
- Are there leaps that assume knowledge a newcomer would not have?
- Is the language plain and concrete, or abstract where a concrete word would teach better?
Flag the specific spots a beginner would stall. Do NOT ask for more jargon or more caveats - flag only what blocks understanding. Return findings.`,
  },
]

const FIDELITY_PROMPT = `${COMMON}

YOUR LENS - Product-fidelity CHECKLIST. You CANNOT verify product behavior, and you do NOT assign severities or gate the verdict. Your sole job is to emit a checklist of the concrete, falsifiable product claims the page asserts - exact labels, values, operation names, field names, and runtime behaviors - that a maintainer must confirm against the live product. For each: quote where it appears, mark whether it is backed by a screenshot or prose-only, rate the risk (high = a wrong value breaks the reader's flow or every expression; low = cosmetic), and say exactly what to check in the UI. Examples of claims to list: an operation named "Add To List", an "Empty List" value, an "As JSON" toggle, a "List" field, "Break ends the loop", a property read with "->", "Current Iteration Item" as the whole item. Do NOT list generic prose with no product claim. Return the checklist.`

phase('Review')
const [educatorR, storyR, beginnerR, fidelityR] = await parallel([
  () => agent(TEACHING[0].prompt, { label: 'review:educator', phase: 'Review', schema: FINDINGS_SCHEMA }),
  () => agent(TEACHING[1].prompt, { label: 'review:story', phase: 'Review', schema: FINDINGS_SCHEMA }),
  () => agent(TEACHING[2].prompt, { label: 'review:beginner', phase: 'Review', schema: FINDINGS_SCHEMA }),
  () => agent(FIDELITY_PROMPT, { label: 'checklist:fidelity', phase: 'Review', schema: CHECKLIST_SCHEMA }),
])
const teaching = [educatorR, storyR, beginnerR].filter(Boolean)

phase('Synthesize')
const synth = await agent(
  `You are the editor consolidating a review of the FlowRunner page ${PAGE}.

TEACHING reviews (these GATE the verdict) - JSON:
${JSON.stringify(teaching, null, 2)}

FIDELITY checklist (informational only - NEVER affects the verdict) - JSON:
${JSON.stringify(fidelityR, null, 2)}

Produce three things:
1) prioritized: merge the teaching findings into one punch-list, dedupe (in raisedBy list every lens that raised each), drop anything that contradicts the page's own standard in ${VOICE}, order by severity.
2) verdict: based ONLY on the teaching findings - "ship" (no blockers or majors), "revise" (majors but fixable), or "major-rework" (blockers or pervasive). The fidelity checklist must NOT change this verdict.
3) verifyInProduct: dedupe the fidelity checklist and order by risk (high first). This is a maintainer to-do, not a blocker.

Be honest and concrete. The goal is to decide whether the page TEACHES well enough to ship, and separately hand back a clean list of product claims to confirm in-app.`,
  { label: 'synthesize', phase: 'Synthesize', schema: REPORT_SCHEMA }
)
return synth
