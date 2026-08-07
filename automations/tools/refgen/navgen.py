"""Generate the Block Reference nav subtree and inject it into mkdocs.yml."""
from collections import OrderedDict

BEGIN = "    # BEGIN generated reference nav"
END = "    # END generated reference nav"
# Concept pages (records with `concept: true`) are not blocks, so they live in a
# 'Concept Guides' sub-section under Platform rather than masquerading as a block
# category. This second marked region holds them (nested one level deeper than the
# Block Reference region, hence 6-space indent on the markers and items).
BEGIN_CONCEPTS = "      # BEGIN generated concept nav"
END_CONCEPTS = "      # END generated concept nav"


def _is_concept(record: dict) -> bool:
    return bool(record.get("concept"))


def build_reference_nav(records: list[dict], indent: int = 4) -> str:
    """YAML nav lines for the BLOCK pages, grouped by category, then name.

    Concept pages are excluded - they render into the separate concept region
    (see `build_concept_nav`). `indent` is the column of the category items
    (they sit under the top-level 'Block Reference' nav key, i.e. 4 spaces in
    MkDocs' 2-space style).
    """
    groups: "OrderedDict[str, list[dict]]" = OrderedDict()
    for r in sorted((r for r in records if not _is_concept(r)),
                    key=lambda r: (r.get("category", ""), r.get("name", ""))):
        groups.setdefault(r.get("category", "Other"), []).append(r)

    pad = " " * indent
    child_pad = " " * (indent + 2)
    lines: list[str] = []
    for category, items in groups.items():
        lines.append(f"{pad}- '{category}':")
        for r in items:
            lines.append(f"{child_pad}- '{r['name']}': reference/{r['id']}.md")
    return "\n".join(lines) + "\n"


def build_concept_nav(records: list[dict], indent: int = 4) -> str:
    """YAML nav lines for the CONCEPT pages - a flat list sorted by name, with no
    category sub-grouping (they are not blocks). The pages still live in
    reference/, so links keep that prefix. Returns "" when there are none.

    A record with `manual_nav: true` is skipped here: its page is still generated
    into reference/, but its nav entry is hand-placed elsewhere in mkdocs.yml
    (e.g. Flow Scheduling lives under Run & Monitor, not Concept Guides)."""
    concepts = sorted((r for r in records if _is_concept(r) and not r.get("manual_nav")),
                      key=lambda r: r.get("name", ""))
    pad = " " * indent
    lines = [f"{pad}- '{r['name']}': reference/{r['id']}.md" for r in concepts]
    return ("\n".join(lines) + "\n") if lines else "\n"


def replace_marked_block(text: str, begin: str, end: str, replacement: str) -> str:
    """Replace the lines strictly between `begin` and `end` marker lines."""
    lines = text.splitlines(keepends=True)
    begin_i = end_i = None
    for i, ln in enumerate(lines):
        if ln.rstrip("\n") == begin:
            begin_i = i
        elif ln.rstrip("\n") == end:
            end_i = i
            break
    if begin_i is None or end_i is None or end_i <= begin_i:
        raise ValueError(f"markers not found or out of order: {begin!r} / {end!r}")
    repl = replacement if replacement.endswith("\n") else replacement + "\n"
    return "".join(lines[: begin_i + 1]) + repl + "".join(lines[end_i:])


def update_mkdocs_nav(mkdocs_text: str, records: list[dict]) -> str:
    text = replace_marked_block(mkdocs_text, BEGIN, END,
                                build_reference_nav(records, indent=4))
    # Inject the concept region only when its markers are present, so a nav
    # without a 'Concept Guides' section (e.g. in unit tests) is left untouched.
    if BEGIN_CONCEPTS in text and END_CONCEPTS in text:
        text = replace_marked_block(text, BEGIN_CONCEPTS, END_CONCEPTS,
                                    build_concept_nav(records, indent=6))
    return text
