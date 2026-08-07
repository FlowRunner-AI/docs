# Docs screenshot harness (hybrid capture)

Screenshots stopped being "rare diamonds" here. This is the repeatable recipe + helpers so an
in-product shot is a few consistent steps instead of ad-hoc fumbling. Mark captures the
branded/fiddly shots (e.g. the Survey Creator form builder) from numbered shot-lists; everything
repeatable in-product is captured this way.

## The recipe (per shot)

1. **Navigate** to the screen in the authenticated product session (Playwright).
2. **Set up the named scenario** so the shot depicts the REAL thing the prose describes — not a
   bare placeholder. Configure the actual block/field/value the page talks about. (Use
   `browser_evaluate` to set field values precisely when clicking is fiddly.)
3. **Redact PII** before capturing — inject `redact.js` and call `__redact({...})` to swap real
   emails/names/keys for placeholders in the live DOM (text nodes + input values). See redact.js.
4. **Tag the element** to shoot: `el.setAttribute('data-shot','x')`, then element-screenshot
   `[data-shot="x"]` (a dialog/panel element screenshot excludes the page backdrop and the
   left-nav, which carries the signed-in user's email).
5. **Crop** the raw capture to a clean frame:
   `python3 tools/shots/crop.py RAW.png content/images/<area>/<name>.png --box L,T,R,B`
6. **Eyeball** the saved PNG. No clipping, no dark backdrop bleed, no branding leakage, no PII.
   The subject sits beside its panel with a clean gap.

## Files
- `crop.py` — crop a raw capture to a box and save into `content/images/`.
- `redact.js` — DOM PII-redaction snippet to inject before capture.

## Conventions
- Save under `content/images/<area>/<descriptive-name>.png` (area = learn / platform / manage / reference).
- Alt text describes the REAL configured scenario shown (VOICE.md screenshot rules).
- Every concept page that names a UI control SHOWS it. If a shot can't be captured cleanly
  in-product (branding/licensing), add it to the shot-list for Mark rather than ship prose-only.
