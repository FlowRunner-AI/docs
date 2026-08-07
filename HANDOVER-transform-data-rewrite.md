# Handover — Transform Data reference rewrite (and side items)

**Task:** Rewrite the **Transform Data** block reference to be story-driven — *worked examples for the non-obvious operations* (Mark's chosen depth), grounded in real in-product behavior. The current page is a dull flat catalogue of 90+ operations.

**Source of truth:** `automations/block-knowledge/transform-data.yaml` → `make refgen` → `automations/content/reference/transform-data.md` (generated; never hand-edit the .md).

**Sandbox (already built, reusable):** dev.flowrunner.ai → workspace **Documentation Flows** → flow **TD Sandbox** (id `C24408A2-1FA3-43DF-BB94-D4DE39D3DE29`). Current graph: **Set Variables** (Start; variable `objA` defined As JSON) → **Transform Data** (Get Property Value). Flow status **Ready**. Mark must be logged in (Google OAuth; I never do that).

---

## 1. Documentation changes to make (based on what was verified in-product)

### 1a. Transform Data page — verified facts to teach

**Operation input semantics (teach this explicitly — it's the #1 user trap):**
- An operation input is a **literal by default**. Typing `{"a":1}` yields the *string* `{"a":1}`, not an object.
- To enter a **literal object/list**, open the field's expression editor (wand icon) and turn on the **"As JSON"** toggle, then type the JSON.
- To **reference data** (a variable / Initial Data), you MUST build the reference **through the expression editor** (search the source, double-click to insert a token). Typing `{{…}}` as text is stored literally and will NOT resolve.
- Data Bucket variable reference syntax (as inserted by the editor): **`{{Data Buckets:Default - objA->}}`** (bucket `Default`, variable `objA`).

**Format Date (fully verified) — a genuinely non-guessable story:**
- Uses **Java SimpleDateFormat** tokens; **case is significant**.
- `1700000000000` + `YYYY-MM-DD HH:mm:ss` → `2023-11-**318** 22:13:20`  (⚠️ `DD` = day **of year** = 318).
- `1700000000000` + `yyyy-MM-dd EEEE, MMMM d` → `2023-11-14 Tuesday, November 14`.
- Tokens: `yyyy`=year, `MM`=month, `dd`=day-of-month, `DD`=day-of-year, `HH`=hour(0–23), `mm`=minute, `ss`=second, `EEEE`=weekday name, `MMMM`=month name, `d`=day (no pad).
- Runs in **UTC**. Trap to warn about: `MM` vs `mm`, `DD` vs `dd`, `YYYY` vs `yyyy`.

**Find / Map "by Expression" (partially verified):**
- The Expression must be a FlowRunner **`{{…}}` boolean expression**; a bare `price > 10` is rejected ("not a valid expression placeholder"). **NOT yet verified:** exactly how the current list item is referenced inside that expression — needs verification next session.

**Reorganize the catalogue** into teaching sections per category (Logic, Object, List, Date/Time, Math, Text). Rich worked input→output examples for the non-obvious ops; keep a compact grouped reference for the self-evident ones (Lower, Trim, Length, Reverse, etc.).

### 1b. Still-to-verify in-product (the object/list non-obvious ops — the heart of remaining work)
Each needs a full-flow run with variables (see §2). Capture real input→output for:
- **Get Property Value** — nested-path syntax (attempted `b.x`; run failed on empty bucket, unconfirmed: dot vs `->`).
- **Set Property Value** — does it create missing / nested keys?
- **Merge Objects** — which value wins on a key clash; shallow or deep?
- **Slice List** — index inclusivity, negatives.
- **Distinct List** — dedups objects by value?
- **Flatten List** — one level or deep?
- **Sort List** — by key on objects; order values; string vs numeric.
- **If Empty** — what counts as "empty" (`null` / `""` / `[]` / `{}` / `0` / `false`)? (scalar cases testable with literals)
- **Round with Fraction** — what "fraction" means. (scalar)
- **Replace** — literal or regex; all occurrences? (scalar)
- **Format Number** — decimals + separators config. (scalar)
- **Switch** — config shape.
- **Parse JSON to Object / List**.

### 1c. Doc-coverage gaps discovered (per Mark's rule: unknown gesture → check docs → if absent, log a TODO)
- **Building a flow by connecting blocks** — drag from a block's **source handle → another block's target handle**; the first wired block becomes the **Start**; the **Start anchor** toggles (hover it → it turns into an **X**/`fa-close`; click removes it and the Start moves to the first wired block). Verify **Build / Flow Editor** docs cover this; if not, create/expand. *(Likely the parallel BUILD tab's territory — coordinate.)*
- **Transform Data / expression inputs** — the literal-vs-expression distinction + "As JSON" toggle + Data Bucket reference syntax. Ensure it's taught (Transform Data page and/or the Expression Editor concept page — see pending question).

### 1d. Already COMPLETED this session (do NOT redo; changes are in the working tree, uncommitted)
- **Custom Cloud Code**: added an **"As an AI Agent tool"** section (per-argument **Value Type** + **Description** = "Prepare for AI Agent"; empty value → agent fills at runtime, filled value locked). Positioned **after the Example** via a new `position: after_example` field added to `automations/tools/refgen/render.py`. New screenshot `content/images/reference/custom-cloud-code-agent-tool.png`. refgen'd; doclint 0 errors; 36 refgen tests pass.
- **Removed Moderate Content / Speech to Text / Text To Speech** from Block Reference (moved to an extension). Their yamls are **parked** in `automations/block-knowledge/_parked-extensions/` (with a README), generated md deleted, nav regenerated. One orphan image left intentionally: `content/images/reference/ai-content-moderation-config.png`.

---

## 2. Next steps for the current task (Transform Data)

1. **Add the rest of the test variables** to the Set Variables block in TD Sandbox: `objB` (for Merge conflict/depth), a numbers list, a list of objects (people), a dups list, a nested list, some strings. Each object/list value: value field → expression editor → **As JSON ON** → type JSON with **real keystrokes** (programmatic value-injection does NOT register).
2. **Run the WHOLE FLOW to get results** — NOT single-block Run Block. *Root cause found:* Run Block executes only the selected block, so upstream Set Variables never runs and the bucket is empty (that's why Get Property Value returned "Input Empty"). Use **Run Instance from the element** / a full-flow test run so Set Variables populates the bucket first.
3. **Per non-obvious op:** set the operation → reference the needed variable(s) via the expression editor (double-click the `Default - <var>` source to insert the token) → set scalar params → run the flow → read the result. Record input→output.
4. **Scalar-input ops** (Format Date ✅, Round with Fraction, Format Number, Replace, If Empty, Parse Number, Substring/Split, case ops, To String, etc.) can be tested with **literals typed directly + single-block Run Block** — no variables needed.
5. **Rewrite** `block-knowledge/transform-data.yaml`: tighten purpose/mental_model/when_to_use; reorganize into teaching sections; add worked examples for the non-obvious ops (use `docs.sections` and/or `example`); teach the input mechanics. Keep the compact grouped reference for self-evident ops.
6. **Screenshots** (operation picker; a worked-example config), `make refgen` (coordinate with the BUILD tab — refgen only rewrites Block Reference + generated nav), **doclint 0 errors**, plain-style + teach-value self-review, then hand to Mark.

### In-product automation notes (to move faster next time)
- Add a block: DnD is HTML5 — simulate with a shared `DataTransfer` across `dragstart`→`dragover`→`drop` on `.react-flow__pane` (worked).
- Draw a connection: **real** `dragTo` from source handle → target handle (synthetic pointer events do NOT work).
- Open the operation picker: real click on the `.tw:truncate.tw:flex-1` value trigger; then set the `Search...` input and click the option.
- Insert a variable token: in the field's expression editor, search the source, then **double-click** the `Default - <var>` row (single click didn't insert).
- Reading results: **Block Results** tab shows Input echo + Output; for object results a bad input shows `{}` or "Empty".
- Verified mechanics also saved to memory: `flowrunner-transform-data-testing.md`.

---

## 3. Pending questions for Mark — ANSWERED 2026-07-15

1. **Test runs — RESOLVED, no billable LIVE instance involved.** Two acceptable in-editor ways to populate the bucket and read results:
   - **(a) Run block-by-block from where data becomes available.** If C depends only on B, run B first (populates the bucket), then run C — C now reads the populated bucket. This is the fix for the earlier "Input Empty" (Run Block on Transform Data alone never ran upstream Set Variables).
   - **(b) "Run instance from this element" icon** (on every block): runs all blocks sequentially; inspect each block's result via its **green checkmark / red warning** icon. **Reset** this state via the reset icon in the **top-level icon bar**.
   - **→ DOC-COVERAGE ITEM (Mark, emphatic): ALL of these run/test options MUST be documented** — the Testing topic (TEST & RUN section). Not the Transform Data page itself; log/coordinate for the testing docs. *(See §4 below.)*
2. **Find / Map by Expression** item-reference syntax — still to verify in-product myself (deferred; now unblocked by 1a/1b).
3. **Input-mechanics teaching placement — RESOLVED: Expression Editor concept page ONLY.** Transform Data reference does NOT re-teach literal-vs-expression / As JSON toggle / `{{Data Buckets:Default - var->}}` syntax; it cross-links. → DOC-COVERAGE ITEM: ensure the **Expression Editor** page covers all three. *(See §4.)*
4. **Connecting-blocks doc gap — RESOLVED: BUILD tab owns it.** Leave a note for that tab; do not write it on the Transform Data page. *(See §4.)*

---

## 3b. AGREED PAGE DESIGN (2026-07-15, after two Mark corrections)
Mark rejected the first structure/depth ("dull catalogue" + shallow one-liners) AND rejected a one-category "sample" that dropped coverage. **Binding design:**
- **Cover EVERY operation** — no operation left out. A pattern-lock must NEVER remove coverage of the others.
- **Deep per operation**, tiered: earned ops (non-obvious behavior) get a full worked entry — purpose → named inputs (`((chips))`) → real input→output block → a **Watch for** only when there's a genuine trap. Self-evident ops get a shorter entry that still has an illustrating example (more than one line).
- **One page**, grouped by the six picker categories (Logic, Object, List, Date & time, Math, Text); each operation is an `###` (feeds the ToC).
- **Screenshots only where the UI adds meaning** (~a handful: Find by Expression's Field-to-check token, Switch case rows, Create Object pairs, maybe Format Date) — captured LAST, after the content is locked.
- Every example value is **real engine output** captured this session (findings: `automations/.cache/orientation/td/findings.md`). Find-by-Expression documented at the verified mechanism level (`Field to check:` token) — no fabricated match result.

**STATUS:** full page written + rendered (`content/reference/transform-data.md`, ~600 lines), doclint 0 errors. Remaining: (a) capture the handful of meaningful screenshots + embed; (b) run `docs-content-review` gate + clear findings; then hand to Mark.

## 4. Doc-coverage items to hand off / log (do not drop)
- **Testing docs (TEST & RUN):** must teach (a) run **block-by-block** from where data becomes available; (b) **"Run instance from this element"** — sequential run, per-block green-check/red-warning result icons; (c) **reset run state** via the top icon-bar reset icon. *(Mark: "ALL THESE OPTIONS MUST MAKE IT TO THE DOCS.")*
- **Expression Editor concept page:** literal-by-default vs expression; the **As JSON** toggle; the `{{Data Buckets:Default - var->}}` reference syntax (built via the editor, not typed).
- **BUILD / Flow Editor tab:** connecting blocks by drawing source→target edge; first wired block becomes **Start**; Start anchor toggle (hover → X / `fa-close`, click removes, Start moves to first wired block).
