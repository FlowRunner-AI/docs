"""Render a block record into a Markdown reference page.

The page is assembled as a list of section strings joined by blank lines, so
Markdown block separation is always correct - in particular, a table is always
followed by a blank line before the next heading (otherwise the heading is
swallowed into the table).
"""
import re

HEADER = ("<!-- GENERATED FILE - do not edit. "
          "Source: block-knowledge/{id}.yaml. Regenerate: make refgen -->")

# A page names itself in its own prose; doclint's block-link rule keys on the name
# with any trailing parenthetical stripped (matching tools/doclint load_block_names),
# so we emit an allow-unlinked for that exact form. A page never links to itself.
_SELF_PAREN = re.compile(r"\s*\([^)]*\)\s*$")

# Regions that must never be touched by link-insertion: HTML comments, fenced
# and inline code, existing links/images, and heading lines (the H1 is the
# block's own name and must stay a plain title, not a styled token).
_PROTECT = re.compile(
    r'<span class="fr-control">.*?</span>|'                # control chips - leave whole, so a block
    r'<span class="fr-expr">.*?</span>|'                  # expression-reference tokens - leave whole
                                                          # name inside one (Wait in "Wait for
                                                          # completion") is not split out
    r"(?m:^\|[^|\n]*\|)|"                                  # a table row's FIRST cell (the Config /
                                                          # Common-settings Field-name column) - a
                                                          # field named like a block must not pill
    r"<!--.*?-->|```.*?```|"
    r"``(?:[^`]|`(?!`))*?``|`[^`]*`|"                      # inline code: double-backtick spans (which may
                                                          # wrap an inner single-backtick, e.g.
                                                          # ``{{Result->files[0]}}``) BEFORE single, so a
                                                          # block name inside them is never linkified
    r"!\[(?:[^\]]|\](?!\())*\]\([^)]*\)|"                  # images: alt may contain ] (e.g. [0], ["a"]);
                                                          # only ]( closes, so the whole ![alt](url) -
                                                          # alt included - is protected from link-insertion
    r"\[(?:[^\]]|\](?!\())*\]\([^)]*\)|"                   # existing links, same ]-in-text tolerance
    r"(?m:^\#{1,6}[^\n]*)",
    re.DOTALL,
)


def linkify(md: str, name_by_id: dict, self_id: str, concept_ids: set = None) -> str:
    """Mark every block-name mention as a styled token (`.fr-block`) so block
    references stand out from ordinary copy; the first prose mention of another
    block is also a link to its reference page.

    Concept guides (ids in `concept_ids`) are pages, not canvas blocks, so they
    are NEVER given the green `.fr-block` pill: the first mention links as
    ordinary prose and later mentions stay plain text. The green pill is reserved
    for things you place on the canvas.

    Skips anything inside code or HTML comments and text already inside a
    Markdown link/image. Longer names match first so
    'Knowledge Base: Add Document' wins over 'Knowledge Base'.
    """
    concept_ids = concept_ids or set()
    stash: list[str] = []

    def put(s: str) -> str:
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    # Protect existing links/images, code, and comments from processing.
    text = _PROTECT.sub(lambda m: put(m.group(0)), md)

    # Also match the paren-stripped form of a name ('Knowledge Bases' for
    # 'Knowledge Bases (RAG stores)'), since that is what a reader writes in prose
    # and what doclint keys on. Both aliases resolve to the same record id.
    pairs: list[tuple[str, str]] = []
    for rid, name in name_by_id.items():
        pairs.append((name, rid))
        stripped = _SELF_PAREN.sub("", name).strip()
        if stripped and stripped != name:
            pairs.append((stripped, rid))

    linked: set[str] = set()
    for name, rid in sorted(pairs, key=lambda p: -len(p[0])):
        pattern = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])")

        def repl(m: "re.Match", rid=rid) -> str:
            word = m.group(0)
            first = rid != self_id and rid not in linked
            if rid in concept_ids:
                # Concept guide: ordinary link on first mention, plain text after;
                # no .fr-block pill (a concept is not a canvas block).
                if first:
                    linked.add(rid)
                    token = f"[{word}]({rid}.md)"
                else:
                    token = word
            elif first:
                linked.add(rid)
                token = f"[{word}]({rid}.md){{.fr-block}}"
            else:
                token = f'<span class="fr-block">{word}</span>'
            # Stash each token so later (shorter) names cannot match inside it.
            return put(token)

        text = pattern.sub(repl, text)

    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


# UI-component chips are placed by INTENT, not by string-matching. The author marks
# a reference to a real product UI element (a field, toggle, button, dropdown, or
# dialog) inline as ((Component Name)); the generator renders it as a .fr-control
# chip. Because placement is authored, there is nothing to misfire - "((Expand))"
# chips, the ordinary verb "expand" does not, with no per-word rules to maintain.
_CONTROL_MARKER = re.compile(r"\(\(\s*(.+?)\s*\)\)", re.DOTALL)
# Markers inside code are left literal (a `((...))` in a snippet is real code).
_CODE_PROTECT = re.compile(r"```.*?```|`[^`]*`", re.DOTALL)


def controlify(md: str) -> str:
    """Render ((...)) UI-component markers as `.fr-control` chips, leaving any
    marker that falls inside fenced or inline code untouched."""
    stash: list[str] = []

    def put(s: str) -> str:
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    text = _CODE_PROTECT.sub(lambda m: put(m.group(0)), md)
    text = _CONTROL_MARKER.sub(
        lambda m: f'<span class="fr-control">{m.group(1).strip()}</span>', text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


# Expression-Editor references. A value that goes into a field through the
# Expression Editor is a token the author INSERTS - never text they type or
# paste - so it gets its own cue (`.fr-expr`), distinct from the monospace `code`
# used for typed literals. Authored the natural way, as {{...}}, right in the
# prose. Markers inside code are left literal (a `{{...}}` in a snippet is real).
_EXPR_MARKER = re.compile(r"\{\{\s*(.+?)\s*\}\}", re.DOTALL)


def exprify(md: str) -> str:
    """Render {{...}} expression references as `.fr-expr` chips, leaving any
    {{...}} inside fenced or inline code untouched. A `->` property step inside
    the reference is rendered as a `→` arrow so the pill reads as the editor
    shows it."""
    stash: list[str] = []

    def put(s: str) -> str:
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    text = _CODE_PROTECT.sub(lambda m: put(m.group(0)), md)

    def render(m: "re.Match") -> str:
        label = re.sub(r"\s*->\s*", " → ", m.group(1).strip())
        return f'<span class="fr-expr">{label}</span>'

    text = _EXPR_MARKER.sub(render, text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def _behavior(items) -> str:
    """Bullets, each optionally followed by a short code example indented under it."""
    out = []
    for it in items:
        if isinstance(it, dict):
            out.append(f"- {(it.get('note') or '').strip()}")
            ex = (it.get("example") or "").strip()
            if ex:
                fence = f"```{it.get('lang', '')}\n{ex}\n```"
                out.append("\n".join("  " + line for line in fence.splitlines()))
        else:
            out.append(f"- {str(it).strip()}")
    return "\n".join(out)


def _cell(text) -> str:
    """Flatten any value into a single safe Markdown table cell."""
    s = "" if text is None else str(text)
    return s.replace("\n", " ").replace("|", r"\|").strip()


def _bullets(items) -> str:
    return "\n".join(f"- {str(i).strip()}" for i in items)


def _config_table(docs: dict) -> str:
    """Field / Description table. 'Required' is folded into the description (as a
    leading 'Required.') only when a field actually is; a field's help tooltip is
    folded in too."""
    tooltips = docs.get("help_tooltips") or {}
    rows = []
    for c in docs.get("config") or []:
        field = c.get("field", "")
        desc = (c.get("description") or "").strip()
        tip = c.get("help_tooltip") or tooltips.get(field)
        if tip:
            desc = f"{desc} {tip}".strip()
        if c.get("required"):
            desc = f"Required. {desc}".strip()
        rows.append((field, desc))
    if not rows:
        return ""
    lines = ["| Field | Description |", "| --- | --- |"]
    lines += [f"| {_cell(f)} | {_cell(d)} |" for f, d in rows]
    return "\n".join(lines)


def _common_table(common_defs: dict, keys) -> str:
    """A 'Common settings' table built from the shared _common.yaml definitions,
    listing only the keys this block opts into (docs.common: [...])."""
    rows = []
    for key in keys or []:
        d = common_defs.get(key)
        if d:
            rows.append((d.get("field", key), d.get("description", "")))
    if not rows:
        return ""
    lines = ["**Common settings** (available on most blocks):", "",
             "| Field | Description |", "| --- | --- |"]
    lines += [f"| {_cell(f)} | {_cell(d)} |" for f, d in rows]
    return "\n".join(lines)


def _example(steps) -> str:
    """A worked example is a sequence of steps rendered in order. Each step may
    carry prose (`text`), a code/JSON block (`code` + `lang`), and/or a screenshot
    (`image` + `alt`) - so an example can interleave narration, data, and visuals."""
    parts = []
    for s in steps or []:
        if (s.get("text") or "").strip():
            parts.append(s["text"].strip())
        if (s.get("code") or "").strip():
            parts.append(f"```{s.get('lang', '')}\n{s['code'].strip()}\n```")
        if (s.get("image") or "").strip():
            parts.append(f"![{(s.get('alt') or '').strip()}]({s['image'].strip()})")
    return "\n\n".join(parts)


def _related(docs: dict, name_by_id: dict) -> str:
    # Only render refs that resolve to a real page; an unresolved ref (a concept
    # page not built yet) is dropped rather than printed as a bare slug.
    items = [f"[{name_by_id[ref]}]({ref}.md)"
             for ref in (docs.get("cross_refs") or []) if ref in name_by_id]
    return _bullets(items) if items else ""


def render_page(record: dict, name_by_id: dict, common_defs: dict = None,
                concept_ids: set = None) -> str:
    docs = record.get("docs", {}) or {}
    common_defs = common_defs or {}
    self_name = _SELF_PAREN.sub("", record["name"]).strip()
    header = HEADER.format(id=record["id"])
    if self_name:
        header += f"\n<!-- doclint: allow-unlinked: {self_name} -->"
    sections = [
        header + f"\n# {record['name']}",
        (docs.get("purpose") or "").strip(),
    ]

    def add(title: str, body: str, image: str = None, alt: str = None) -> None:
        body = (body or "").strip()
        if body:
            if (image or "").strip():
                body = f"{body}\n\n![{(alt or '').strip()}]({image.strip()})"
            sections.append(f"## {title}\n\n{body}")

    # How it works / When to use it may each carry a screenshot, so a control
    # introduced in the prose is illustrated right where the reader meets it.
    add("How it works", docs.get("mental_model"),
        docs.get("mental_model_image"), docs.get("mental_model_alt"))
    add("When to use it", docs.get("when_to_use"),
        docs.get("when_to_use_image"), docs.get("when_to_use_alt"))
    # Optional custom sections (e.g. a deep-dive on a flagship feature). Each is
    # {title, body, image?, alt?, position?}. They render between When-to-use and
    # the Example by default, or after it when position is "after_example".
    def _add_sections(where: str) -> None:
        for sec in docs.get("sections") or []:
            if (sec.get("position") or "before_example") != where:
                continue
            body = (sec.get("body") or "").strip()
            if (sec.get("image") or "").strip():
                body = f"{body}\n\n![{(sec.get('alt') or '').strip()}]({sec['image'].strip()})".strip()
            add(sec.get("title", "").strip(), body)

    _add_sections("before_example")
    if docs.get("example"):
        add("Example", _example(docs["example"]))
    _add_sections("after_example")
    config_parts = [_config_table(docs), _common_table(common_defs, docs.get("common"))]
    add("Configuration", "\n\n".join(p for p in config_parts if p))
    if record.get("behavior"):
        add("Behavior", _behavior(record["behavior"]))
    if docs.get("limitations"):
        add("Limitations", _bullets(docs["limitations"]))
    elif docs.get("gotchas"):
        add("Things to watch for", _bullets(docs["gotchas"]))
    add("Related", _related(docs, name_by_id))

    page = "\n\n".join(s for s in sections if s.strip()) + "\n"
    # Controls first: a marked component can contain a block name ("Wait for
    # completion" contains the Wait block), and chipping it first stops linkify from
    # splitting "Wait" out of it. linkify then protects the finished control chips.
    page = controlify(page)
    page = exprify(page)
    return linkify(page, name_by_id, record["id"], concept_ids)
