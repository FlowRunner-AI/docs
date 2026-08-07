"""MkDocs hook: give hand-authored (non-generated) pages the same two authoring
cues the Block Reference gets - `((UI Component))` -> `.fr-control` chips, and
`{{expression reference}}` -> `.fr-expr` wand pills.

The Block Reference pages get both from the refgen generator, so their committed
Markdown already contains the finished `<span>`s and no markers remain - this hook
is a no-op there. Narrative pages (First Steps, Platform, Build, Run & Monitor) are
plain Markdown that never passes through refgen, so this hook applies the same two
passes, in refgen's order (controlify, then exprify). We reuse refgen's own
functions so the two paths can never drift.
"""
import os
import sys

# mkdocs runs with the config dir (automations/) as cwd; make the refgen package importable.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.refgen.render import controlify, exprify  # noqa: E402


def on_page_markdown(markdown, **kwargs):
    return exprify(controlify(markdown))
