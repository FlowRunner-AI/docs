"""Generate the Block Reference nav subtree and inject it into mkdocs.yml."""
from collections import OrderedDict

BEGIN = "    # BEGIN generated reference nav"
END = "    # END generated reference nav"


def build_reference_nav(records: list[dict], indent: int = 4) -> str:
    """YAML nav lines grouping pages by category, then name.

    `indent` is the column of the category items (they sit under a top-level
    'Block Reference' nav key, i.e. 4 spaces in MkDocs' 2-space style).
    """
    groups: "OrderedDict[str, list[dict]]" = OrderedDict()
    for r in sorted(records, key=lambda r: (r.get("category", ""), r.get("name", ""))):
        groups.setdefault(r.get("category", "Other"), []).append(r)

    pad = " " * indent
    child_pad = " " * (indent + 2)
    lines: list[str] = []
    for category, items in groups.items():
        lines.append(f"{pad}- '{category}':")
        for r in items:
            lines.append(f"{child_pad}- '{r['name']}': reference/{r['id']}.md")
    return "\n".join(lines) + "\n"


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
    fragment = build_reference_nav(records, indent=4)
    return replace_marked_block(mkdocs_text, BEGIN, END, fragment)
