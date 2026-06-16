"""Render a block record into a Markdown reference page."""
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .paths import TEMPLATES

_env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)


def _cell(text) -> str:
    """Flatten any value into a single safe Markdown table cell."""
    s = "" if text is None else str(text)
    return s.replace("\n", " ").replace("|", r"\|").strip()


def _config_rows(docs: dict) -> list[dict]:
    rows = []
    tooltips = docs.get("help_tooltips") or {}      # some records carry a top-level-ish map
    for c in docs.get("config") or []:
        field = c.get("field", "")
        description = c.get("description", "") or ""
        tip = c.get("help_tooltip") or tooltips.get(field)
        if tip:
            description = f"{description} — {tip}" if description else tip
        rows.append({
            "field": _cell(field),
            "type": _cell(c.get("type", "")),
            "required": "Yes" if c.get("required") else "",
            "description": _cell(description),
        })
    return rows


def _related(docs: dict, name_by_id: dict) -> list[str]:
    out = []
    for ref in docs.get("cross_refs") or []:
        if ref in name_by_id:
            out.append(f"[{name_by_id[ref]}]({ref}.md)")
        else:
            out.append(str(ref))                    # concept not yet a reference page
    return out


class _DictProxy:
    """Attribute-access wrapper for a dict that returns None for missing keys.

    Avoids StrictUndefined errors when the template tests optional fields with
    ``{% if record.behavior %}`` — missing keys become None (falsy) rather
    than raising UndefinedError.  Nested dicts are also wrapped on access.
    """

    def __init__(self, d: dict):
        self._d = d

    def __getattr__(self, name: str):
        val = self._d.get(name)
        if isinstance(val, dict):
            return _DictProxy(val)
        return val

    def __getitem__(self, name: str):
        return self.__getattr__(name)

    def __bool__(self):
        return bool(self._d)

    def __iter__(self):
        return iter(self._d)


def render_page(record: dict, name_by_id: dict) -> str:
    docs = record.get("docs", {})
    # help_tooltips can live at the record top level too; fold it into docs view.
    docs_view = dict(docs)
    if "help_tooltips" in record and "help_tooltips" not in docs_view:
        docs_view["help_tooltips"] = record["help_tooltips"]
    template = _env.get_template("block.md.j2")
    # Use _DictProxy so optional fields return None (falsy) rather than raising
    # StrictUndefined when the template guards with {% if record.behavior %} etc.
    return template.render(
        record=_DictProxy(record),
        config_rows=_config_rows(docs_view),
        related=_related(docs, name_by_id),
    )
