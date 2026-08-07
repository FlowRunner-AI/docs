# Parked: extension blocks (not part of the core product)

These block records were moved out of the core Block Reference because the blocks
themselves were moved into a **FlowRunner extension**, not the core product.

They are kept here — out of `refgen`'s and `doclint`'s path (the loader globs
`block-knowledge/*.yaml` non-recursively, so this subdirectory is ignored) — so the
runtime-verified knowledge is preserved for the eventual extension documentation.

- `ai-content-moderation.yaml` — Moderate Content
- `ai-speech-to-text.yaml` — Speech to Text
- `ai-text-to-speech.yaml` — Text To Speech

To restore one to the core reference: move the `.yaml` back up to `block-knowledge/`
and run `make refgen`. (The Moderate Content config screenshot is still at
`content/images/reference/ai-content-moderation-config.png`.)
