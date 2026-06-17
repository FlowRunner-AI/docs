"""Render a block record into a Markdown reference page.

The page is assembled as a list of section strings joined by blank lines, so
Markdown block separation is always correct - in particular, a table is always
followed by a blank line before the next heading (otherwise the heading is
swallowed into the table).
"""
import re

HEADER = ("<!-- GENERATED FILE - do not edit. "
          "Source: block-knowledge/{id}.yaml. Regenerate: make refgen -->")

# Regions that must never be touched by link-insertion: HTML comments, fenced
# and inline code, existing links/images, and heading lines (the H1 is the
# block's own name and must stay a plain title, not a styled token).
_PROTECT = re.compile(
    r"<!--.*?-->|```.*?```|`[^`]*`|!\[[^\]]*\]\([^)]*\)|\[[^\]]*\]\([^)]*\)|(?m:^\#{1,6}[^\n]*)",
    re.DOTALL,
)


def linkify(md: str, name_by_id: dict, self_id: str) -> str:
    """Mark every block-name mention as a styled token (`.fr-block`) so block
    references stand out from ordinary copy; the first prose mention of another
    block is also a link to its reference page.

    Skips anything inside code or HTML comments and text already inside a
    Markdown link/image. Longer names match first so
    'Knowledge Base: Add Document' wins over 'Knowledge Base'.
    """
    stash: list[str] = []

    def put(s: str) -> str:
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    # Protect existing links/images, code, and comments from processing.
    text = _PROTECT.sub(lambda m: put(m.group(0)), md)

    linked: set[str] = set()
    for name, rid in sorted(((n, i) for i, n in name_by_id.items()),
                            key=lambda p: -len(p[0])):
        pattern = re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])")

        def repl(m: "re.Match", rid=rid) -> str:
            word = m.group(0)
            if rid != self_id and rid not in linked:
                linked.add(rid)
                token = f"[{word}]({rid}.md){{.fr-block}}"
            else:
                token = f'<span class="fr-block">{word}</span>'
            # Stash each token so later (shorter) names cannot match inside it.
            return put(token)

        text = pattern.sub(repl, text)

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
    items = []
    for ref in docs.get("cross_refs") or []:
        items.append(f"[{name_by_id[ref]}]({ref}.md)" if ref in name_by_id else str(ref))
    return _bullets(items) if items else ""


def render_page(record: dict, name_by_id: dict, common_defs: dict = None) -> str:
    docs = record.get("docs", {}) or {}
    common_defs = common_defs or {}
    sections = [
        HEADER.format(id=record["id"]) + f"\n# {record['name']}",
        (docs.get("purpose") or "").strip(),
    ]

    def add(title: str, body: str) -> None:
        body = (body or "").strip()
        if body:
            sections.append(f"## {title}\n\n{body}")

    add("How it works", docs.get("mental_model"))
    add("When to use it", docs.get("when_to_use"))
    if docs.get("example"):
        add("Example", _example(docs["example"]))
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
    return linkify(page, name_by_id, record["id"])
