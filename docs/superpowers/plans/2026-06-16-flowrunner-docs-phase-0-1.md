# FlowRunner Docs Rewrite — Phase 0 + 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the new docs IA in `mkdocs.yml` and build a tested generator that turns the 31 `block-knowledge/*.yaml` records into committed Block Reference pages, then calibrate the voice and author/generate all reference pages.

**Architecture:** A small Python package `automations/tools/refgen/` reads the YAML records, validates them, renders one Markdown page per block from a Jinja2 template, writes committed artifacts to `content/reference/<id>.md`, and rewrites the Block Reference subtree of `mkdocs.yml` between marker comments. Generated pages carry a do-not-edit header; a `make refgen-check` target regenerates and `git diff --exit-code`s to catch drift. Phase 1 then enriches each record's prose fields and regenerates.

**Tech Stack:** Python 3.11, PyYAML, Jinja2, pytest, MkDocs 1.6.1 (Material). Working dir is `automations/`.

**Spec:** `docs/superpowers/specs/2026-06-16-flowrunner-docs-rewrite-design.md`

**Fixed constraints:** Do not modify `content/css/flowrunner-mkdocs.css`. Follow `MKDOCS_GUIDE.md` (≤2 admonitions/page, no inline `<style>`, light default) and `CLAUDE.md` (terminology, formatting). Do not name SurveyJS. All commands run from `automations/`.

---

## File Structure

```
automations/
  tools/
    __init__.py                  # package marker
    refgen/
      __init__.py
      paths.py                   # canonical project paths (records dir, output dir, mkdocs path)
      loader.py                  # load_records(dir) -> list[dict]
      schema.py                  # validate_record(record) -> list[str]
      render.py                  # render_page(record, name_by_id) -> str
      navgen.py                  # build_reference_nav / replace_marked_block / update_mkdocs_nav
      generate.py                # CLI entry: validate -> render -> write -> update nav
      templates/
        block.md.j2              # the page template
      tests/
        __init__.py
        conftest.py              # sample-record + tmp fixtures
        test_loader.py
        test_schema.py
        test_render.py
        test_navgen.py
        test_generate.py         # integration
    requirements.txt             # pyyaml, jinja2, pytest
  Makefile                       # refgen / refgen-test / refgen-check / refgen-install
  mkdocs.yml                     # nav restructured to new IA + reference markers
  block-knowledge/
    VOICE.md                     # NEW (Phase 0 seed; Phase 1 grows)
    *.yaml                       # source records (Phase 1 enriches prose)
  content/
    reference/<id>.md            # GENERATED, committed
    <new stub pages>.md          # IA scaffolding
```

Run from `automations/`: `python -m tools.refgen.generate`, `pytest tools/refgen/tests`.

---

## Task 1: Package skeleton + dependencies

**Files:**
- Create: `automations/tools/__init__.py`, `automations/tools/refgen/__init__.py`, `automations/tools/refgen/tests/__init__.py`
- Create: `automations/tools/refgen/requirements.txt`
- Create: `automations/tools/refgen/paths.py`

- [ ] **Step 1: Create the package markers (empty files)**

```bash
cd automations
mkdir -p tools/refgen/templates tools/refgen/tests
: > tools/__init__.py
: > tools/refgen/__init__.py
: > tools/refgen/tests/__init__.py
```

- [ ] **Step 2: Write `tools/refgen/requirements.txt`**

```
pyyaml>=6.0
jinja2>=3.1
pytest>=8.0
```

- [ ] **Step 3: Install dependencies**

Run: `cd automations && python3 -m pip install -r tools/refgen/requirements.txt`
Expected: installs/refreshes pyyaml, jinja2, pytest (no errors).

- [ ] **Step 4: Write `tools/refgen/paths.py`**

```python
"""Canonical project paths, resolved relative to this file.

tools/refgen/paths.py -> parents[2] is the automations/ project root.
"""
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]          # .../automations
RECORDS_DIR = PROJECT / "block-knowledge"
OUTPUT_DIR = PROJECT / "content" / "reference"
MKDOCS = PROJECT / "mkdocs.yml"
TEMPLATES = Path(__file__).resolve().parent / "templates"

# Files in block-knowledge that are NOT block records:
NON_RECORD_FILES = {"README.md", "VOICE.md"}
```

- [ ] **Step 5: Verify paths resolve**

Run: `cd automations && python3 -c "from tools.refgen import paths; print(paths.RECORDS_DIR.is_dir(), paths.MKDOCS.is_file())"`
Expected: `True True`

- [ ] **Step 6: Commit**

```bash
cd automations
git add tools/__init__.py tools/refgen/__init__.py tools/refgen/tests/__init__.py tools/refgen/requirements.txt tools/refgen/paths.py
git commit -m "build(refgen): package skeleton, deps, and canonical paths"
```

---

## Task 2: Record loader

**Files:**
- Create: `automations/tools/refgen/loader.py`
- Test: `automations/tools/refgen/tests/conftest.py`, `automations/tools/refgen/tests/test_loader.py`

- [ ] **Step 1: Write the fixtures in `tests/conftest.py`**

```python
import textwrap
import pytest


@pytest.fixture
def sample_record():
    """A minimal but valid block record (dict), mirroring the YAML schema."""
    return {
        "id": "demo-block",
        "name": "Demo Block",
        "category": "Utils",
        "kind": "native",
        "api": {"element_type": "ACTION", "meta_type": "DEMO"},
        "docs": {
            "purpose": "Does a demo thing.",
            "mental_model": "Think of it as a stand-in.",
            "when_to_use": "When you need a stand-in.",
            "config": [
                {"field": "Key", "type": "expression", "required": True,
                 "description": "The key to use.", "help_tooltip": "The lookup key."},
            ],
            "gotchas": ["It is only a demo."],
            "cross_refs": ["other-block"],
            "terminology": ["Demo"],
        },
        "behavior": ["Returns a demo result."],
        "assertions": [{"id": "x", "expect": "y"}],
        "known_bugs": [],
        "provenance": {"confidence": "V-config"},
    }


@pytest.fixture
def records_dir(tmp_path):
    """A temp block-knowledge dir with one record + a README to be ignored."""
    import yaml
    d = tmp_path / "block-knowledge"
    d.mkdir()
    (d / "README.md").write_text("schema docs, not a record\n")
    (d / "demo-block.yaml").write_text(yaml.safe_dump({
        "id": "demo-block", "name": "Demo Block", "category": "Utils",
        "docs": {"purpose": "Does a demo thing."},
    }, sort_keys=False))
    return d
```

- [ ] **Step 2: Write the failing test `tests/test_loader.py`**

```python
from tools.refgen.loader import load_records


def test_loads_yaml_records_and_skips_non_records(records_dir):
    records = load_records(records_dir)
    ids = [r["id"] for r in records]
    assert ids == ["demo-block"]          # README.md skipped


def test_records_sorted_by_name(tmp_path):
    import yaml
    d = tmp_path / "kb"
    d.mkdir()
    for rid, name in [("b", "Beta"), ("a", "Alpha")]:
        (d / f"{rid}.yaml").write_text(
            yaml.safe_dump({"id": rid, "name": name, "category": "X",
                            "docs": {"purpose": "p"}}, sort_keys=False))
    records = load_records(d)
    assert [r["name"] for r in records] == ["Alpha", "Beta"]
```

- [ ] **Step 3: Run it to verify it fails**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_loader.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.refgen.loader'`

- [ ] **Step 4: Write `tools/refgen/loader.py`**

```python
"""Load block-knowledge YAML records from disk."""
from pathlib import Path

import yaml

from .paths import NON_RECORD_FILES


def load_records(records_dir: Path) -> list[dict]:
    """Return all block records in `records_dir`, sorted by display name.

    Skips non-record files (README.md, VOICE.md). Each record must parse to a
    dict; anything else raises ValueError so a malformed file fails loudly.
    """
    records: list[dict] = []
    for path in sorted(records_dir.glob("*.yaml")):
        if path.name in NON_RECORD_FILES:
            continue
        data = yaml.safe_load(path.read_text())
        if not isinstance(data, dict):
            raise ValueError(f"{path.name}: expected a mapping, got {type(data).__name__}")
        records.append(data)
    records.sort(key=lambda r: r.get("name", r.get("id", "")))
    return records
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_loader.py -v`
Expected: PASS (2 passed)

- [ ] **Step 6: Commit**

```bash
cd automations
git add tools/refgen/loader.py tools/refgen/tests/conftest.py tools/refgen/tests/test_loader.py
git commit -m "feat(refgen): YAML record loader"
```

---

## Task 3: Record validation

**Files:**
- Create: `automations/tools/refgen/schema.py`
- Test: `automations/tools/refgen/tests/test_schema.py`

- [ ] **Step 1: Write the failing test `tests/test_schema.py`**

```python
from tools.refgen.schema import validate_record


def test_valid_record_has_no_errors(sample_record):
    assert validate_record(sample_record) == []


def test_missing_top_level_fields_reported():
    errors = validate_record({"docs": {"purpose": "p"}})
    joined = " ".join(errors)
    assert "id" in joined and "name" in joined and "category" in joined


def test_missing_purpose_reported():
    errors = validate_record({"id": "x", "name": "X", "category": "Utils", "docs": {}})
    assert any("purpose" in e for e in errors)


def test_purpose_must_be_non_empty():
    errors = validate_record({"id": "x", "name": "X", "category": "Utils",
                              "docs": {"purpose": "   "}})
    assert any("purpose" in e for e in errors)


def test_config_must_be_a_list_when_present():
    errors = validate_record({"id": "x", "name": "X", "category": "Utils",
                              "docs": {"purpose": "p", "config": "nope"}})
    assert any("config" in e for e in errors)
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_schema.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.refgen.schema'`

- [ ] **Step 3: Write `tools/refgen/schema.py`**

```python
"""Validate block records against the doc-facing requirements.

Returns a list of human-readable error strings (empty == valid). Only checks
what the generator needs to render a correct page; the full schema lives in
block-knowledge/README.md.
"""

REQUIRED_TOP = ("id", "name", "category")


def validate_record(record: dict) -> list[str]:
    rid = record.get("id", "<unknown>")
    errors: list[str] = []

    for key in REQUIRED_TOP:
        value = record.get(key)
        if not (isinstance(value, str) and value.strip()):
            errors.append(f"{rid}: missing/empty required field '{key}'")

    docs = record.get("docs")
    if not isinstance(docs, dict):
        errors.append(f"{rid}: 'docs' must be a mapping")
        return errors

    purpose = docs.get("purpose")
    if not (isinstance(purpose, str) and purpose.strip()):
        errors.append(f"{rid}: 'docs.purpose' (the page lede) is required and must be non-empty")

    config = docs.get("config")
    if config is not None and not isinstance(config, list):
        errors.append(f"{rid}: 'docs.config' must be a list when present")

    return errors
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_schema.py -v`
Expected: PASS (5 passed)

- [ ] **Step 5: Commit**

```bash
cd automations
git add tools/refgen/schema.py tools/refgen/tests/test_schema.py
git commit -m "feat(refgen): record validation"
```

---

## Task 4: Page template + renderer

**Files:**
- Create: `automations/tools/refgen/templates/block.md.j2`
- Create: `automations/tools/refgen/render.py`
- Test: `automations/tools/refgen/tests/test_render.py`

- [ ] **Step 1: Write the failing test `tests/test_render.py`**

```python
from tools.refgen.render import render_page


def test_page_has_header_and_lede(sample_record):
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block"})
    assert md.startswith("<!-- GENERATED FILE")
    assert "block-knowledge/demo-block.yaml" in md.splitlines()[0]
    assert "# Demo Block" in md
    assert "Does a demo thing." in md


def test_page_renders_doc_sections(sample_record):
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block"})
    assert "## How it works" in md
    assert "## When to use it" in md
    assert "## Configuration" in md
    assert "| Key |" in md                         # config table row
    assert "## Behavior" in md
    assert "## Things to watch for" in md


def test_page_excludes_internal_fields(sample_record):
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block"})
    assert "provenance" not in md.lower()
    assert "assertion" not in md.lower()
    assert "V-config" not in md


def test_related_links_resolve_known_ids(sample_record):
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block",
                                                "other-block": "Other Block"})
    assert "[Other Block](other-block.md)" in md


def test_related_unknown_id_is_plain_text():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "cross_refs": ["nope-concept"]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "nope-concept" in md
    assert "[nope-concept]" not in md               # no dangling link


def test_config_description_merges_help_tooltip(sample_record):
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block"})
    assert "The key to use." in md
    assert "The lookup key." in md                  # tooltip folded into the cell


def test_omitted_sections_when_absent():
    rec = {"id": "x", "name": "X", "category": "Utils", "docs": {"purpose": "Just a lede."}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "## Configuration" not in md
    assert "## Behavior" not in md
    assert "## Things to watch for" not in md
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_render.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.refgen.render'`

- [ ] **Step 3: Write the template `tools/refgen/templates/block.md.j2`**

```jinja
<!-- GENERATED FILE — do not edit. Source: block-knowledge/{{ record.id }}.yaml. Regenerate: make refgen -->
# {{ record.name }}

{{ record.docs.purpose | trim }}
{% if record.docs.mental_model %}
## How it works

{{ record.docs.mental_model | trim }}
{% endif %}
{% if record.docs.when_to_use %}
## When to use it

{{ record.docs.when_to_use | trim }}
{% endif %}
{% if config_rows %}
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
{% for row in config_rows %}| {{ row.field }} | {{ row.type }} | {{ row.required }} | {{ row.description }} |
{% endfor %}
{% endif %}
{% if record.behavior %}
## Behavior

{% for b in record.behavior %}- {{ b | trim }}
{% endfor %}
{% endif %}
{% if record.docs.gotchas %}
## Things to watch for

{% for g in record.docs.gotchas %}- {{ g | trim }}
{% endfor %}
{% endif %}
{% if related %}
## Related

{% for r in related %}- {{ r }}
{% endfor %}
{% endif %}
```

- [ ] **Step 4: Write `tools/refgen/render.py`**

```python
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


def render_page(record: dict, name_by_id: dict) -> str:
    docs = record.get("docs", {})
    # help_tooltips can live at the record top level too; fold it into docs view.
    docs_view = dict(docs)
    if "help_tooltips" in record and "help_tooltips" not in docs_view:
        docs_view["help_tooltips"] = record["help_tooltips"]
    template = _env.get_template("block.md.j2")
    return template.render(
        record=record,
        config_rows=_config_rows(docs_view),
        related=_related(docs, name_by_id),
    )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_render.py -v`
Expected: PASS (7 passed). If a StrictUndefined error fires on a record missing `behavior`, note the template guards each section with `{% if %}`; `record.behavior` is accessed only inside its guard, and Jinja attribute access on a missing key yields Undefined which is falsy in the `{% if %}` — but StrictUndefined raises on *use*, not on the truthiness test, so the guards are safe.

- [ ] **Step 6: Commit**

```bash
cd automations
git add tools/refgen/templates/block.md.j2 tools/refgen/render.py tools/refgen/tests/test_render.py
git commit -m "feat(refgen): page template and renderer"
```

---

## Task 5: Reference nav generation

**Files:**
- Create: `automations/tools/refgen/navgen.py`
- Test: `automations/tools/refgen/tests/test_navgen.py`

The Block Reference nav is owned by the generator and injected into `mkdocs.yml` between two marker lines. `build_reference_nav` groups pages by `category` and emits YAML list lines at the indentation MkDocs expects under a top-level nav section.

- [ ] **Step 1: Write the failing test `tests/test_navgen.py`**

```python
import yaml

from tools.refgen.navgen import (
    build_reference_nav,
    replace_marked_block,
    update_mkdocs_nav,
    BEGIN,
    END,
)


def _records():
    return [
        {"id": "ai-agent", "name": "AI Agent", "category": "AI"},
        {"id": "condition", "name": "Condition", "category": "Control Flow"},
        {"id": "ai-router", "name": "AI Router", "category": "AI"},
    ]


def test_nav_groups_by_category_then_name():
    frag = build_reference_nav(_records(), indent=4)
    lines = [ln.rstrip() for ln in frag.splitlines() if ln.strip()]
    assert lines == [
        "    - 'AI':",
        "      - 'AI Agent': reference/ai-agent.md",
        "      - 'AI Router': reference/ai-router.md",
        "    - 'Control Flow':",
        "      - 'Condition': reference/condition.md",
    ]


def test_replace_marked_block_replaces_between_markers():
    text = "a\n# BEGIN x\nOLD\n# END x\nb\n"
    out = replace_marked_block(text, "# BEGIN x", "# END x", "NEW1\nNEW2")
    assert out == "a\n# BEGIN x\nNEW1\nNEW2\n# END x\nb\n"


def test_replace_marked_block_missing_marker_raises():
    import pytest
    with pytest.raises(ValueError):
        replace_marked_block("no markers here", "# BEGIN x", "# END x", "X")


def test_update_mkdocs_nav_keeps_valid_yaml_and_injects_pages():
    mkdocs = (
        "nav:\n"
        "  - 'Learn':\n"
        "    - 'Overview': index.md\n"
        "  - 'Block Reference':\n"
        "    # BEGIN generated reference nav\n"
        "    # END generated reference nav\n"
    )
    out = update_mkdocs_nav(mkdocs, _records())
    data = yaml.safe_load(out)                       # must remain valid YAML
    nav = {list(s.keys())[0]: list(s.values())[0] for s in data["nav"]}
    ref = nav["Block Reference"]
    # AI group with two children present
    ai = [g for g in ref if "AI" in g][0]
    assert {"AI Agent": "reference/ai-agent.md"} in ai["AI"]
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_navgen.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.refgen.navgen'`

- [ ] **Step 3: Write `tools/refgen/navgen.py`**

```python
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
```

`BEGIN`/`END` carry the 4-space indent of the marker lines as they appear in
`mkdocs.yml`, so the same constants drive both the file format and the test.

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_navgen.py -v`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
cd automations
git add tools/refgen/navgen.py tools/refgen/tests/test_navgen.py
git commit -m "feat(refgen): reference nav generation + mkdocs injection"
```

---

## Task 6: Generator CLI (orchestration) + integration test

**Files:**
- Create: `automations/tools/refgen/generate.py`
- Test: `automations/tools/refgen/tests/test_generate.py`

- [ ] **Step 1: Write the failing integration test `tests/test_generate.py`**

```python
import yaml

from tools.refgen.generate import run


def _write(d, rid, name, category, purpose):
    (d / f"{rid}.yaml").write_text(yaml.safe_dump(
        {"id": rid, "name": name, "category": category, "docs": {"purpose": purpose}},
        sort_keys=False))


def test_run_generates_pages_and_updates_nav(tmp_path):
    records = tmp_path / "block-knowledge"
    records.mkdir()
    (records / "README.md").write_text("schema\n")
    _write(records, "ai-agent", "AI Agent", "AI", "Calls a model.")
    _write(records, "condition", "Condition", "Control Flow", "Branches on a test.")

    out = tmp_path / "content" / "reference"
    mkdocs = tmp_path / "mkdocs.yml"
    mkdocs.write_text(
        "nav:\n"
        "  - 'Block Reference':\n"
        "    # BEGIN generated reference nav\n"
        "    # END generated reference nav\n"
    )

    errors = run(records_dir=records, output_dir=out, mkdocs_path=mkdocs)

    assert errors == []
    assert (out / "ai-agent.md").read_text().startswith("<!-- GENERATED FILE")
    assert "# Condition" in (out / "condition.md").read_text()
    nav_yaml = yaml.safe_load(mkdocs.read_text())   # still valid
    assert "AI" in str(nav_yaml)


def test_run_reports_validation_errors_and_writes_nothing(tmp_path):
    records = tmp_path / "block-knowledge"
    records.mkdir()
    (records / "broken.yaml").write_text(yaml.safe_dump(
        {"id": "broken", "name": "Broken", "category": "X", "docs": {}}, sort_keys=False))
    out = tmp_path / "content" / "reference"
    mkdocs = tmp_path / "mkdocs.yml"
    mkdocs.write_text("nav:\n  - 'Block Reference':\n    # BEGIN generated reference nav\n    # END generated reference nav\n")

    errors = run(records_dir=records, output_dir=out, mkdocs_path=mkdocs)

    assert any("purpose" in e for e in errors)
    assert not out.exists() or not list(out.glob("*.md"))   # nothing written on failure
```

- [ ] **Step 2: Run it to verify it fails**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_generate.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.refgen.generate'`

- [ ] **Step 3: Write `tools/refgen/generate.py`**

```python
"""Generate all Block Reference pages from block-knowledge records.

Usage (from automations/):  python -m tools.refgen.generate
"""
import sys
from pathlib import Path

from . import paths
from .loader import load_records
from .navgen import update_mkdocs_nav
from .render import render_page
from .schema import validate_record


def run(records_dir: Path, output_dir: Path, mkdocs_path: Path) -> list[str]:
    """Validate, render, write pages, and update the nav. Returns error list.

    On any validation error, nothing is written (fail fast, no partial output).
    """
    records = load_records(records_dir)

    errors: list[str] = []
    for r in records:
        errors.extend(validate_record(r))
    if errors:
        return errors

    name_by_id = {r["id"]: r["name"] for r in records}

    output_dir.mkdir(parents=True, exist_ok=True)
    for r in records:
        page = render_page(r, name_by_id=name_by_id)
        (output_dir / f"{r['id']}.md").write_text(page)

    mkdocs_path.write_text(update_mkdocs_nav(mkdocs_path.read_text(), records))
    return []


def main() -> int:
    errors = run(paths.RECORDS_DIR, paths.OUTPUT_DIR, paths.MKDOCS)
    if errors:
        print("Reference generation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"Generated reference pages into {paths.OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd automations && python3 -m pytest tools/refgen/tests/test_generate.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Run the whole suite**

Run: `cd automations && python3 -m pytest tools/refgen/tests -v`
Expected: PASS (all green)

- [ ] **Step 6: Commit**

```bash
cd automations
git add tools/refgen/generate.py tools/refgen/tests/test_generate.py
git commit -m "feat(refgen): generator CLI + integration tests"
```

---

## Task 7: Makefile (generate / test / check / install)

**Files:**
- Create: `automations/Makefile`

- [ ] **Step 1: Write `automations/Makefile`**

```makefile
.PHONY: refgen-install refgen refgen-test refgen-check

refgen-install:
	python3 -m pip install -r tools/refgen/requirements.txt

refgen:
	python3 -m tools.refgen.generate

refgen-test:
	python3 -m pytest tools/refgen/tests -v

# Anti-drift guard: regenerate, then fail if anything changed (artifact hand-edited
# or stale). Intended for CI and pre-commit verification.
refgen-check: refgen
	git diff --exit-code content/reference mkdocs.yml
```

- [ ] **Step 2: Verify targets run**

Run: `cd automations && make refgen-test`
Expected: pytest runs green.

- [ ] **Step 3: Commit**

```bash
cd automations
git add Makefile
git commit -m "build(refgen): make targets for generate/test/check"
```

---

## Task 8: Restructure mkdocs.yml to the new IA + scaffold stub pages

This replaces the entire `nav:` block with the approved IA and creates a stub page for every leaf so the site builds. The Block Reference section holds only the marker pair (filled by the generator in Task 10).

**Files:**
- Modify: `automations/mkdocs.yml` (the `nav:` block only — lines 4–131 per current file; do NOT touch theme/plugins/extensions below it)
- Create: `automations/tools/scaffold_stubs.py` (one-off, lists every stub page) + the stub `.md` files it writes

- [ ] **Step 1: Replace the `nav:` block in `mkdocs.yml`**

Open `mkdocs.yml`. Replace everything from the line `nav:` up to (but not including) the line `docs_dir: content` with exactly:

```yaml
nav:
  - 'Learn':
    - 'Overview': index.md
    - 'Terminology': definitions.md
    - 'Quick Start': learn/quickstart.md
    - 'Core Concepts':
      - 'Flows & Instances': learn/concepts/flows-and-instances.md
      - 'Triggers': learn/concepts/triggers.md
      - 'Blocks': learn/concepts/blocks.md
      - 'Variables & Data Buckets': learn/concepts/variables.md
      - 'Expressions': learn/concepts/expressions.md
      - 'Subflows': learn/concepts/subflows.md
      - 'Shared Memory': learn/concepts/shared-memory.md
    - 'Tutorials': learn/tutorials.md
  - 'Build':
    - 'The Flow Editor': build/flow-editor.md
    - 'Data & Variables': build/data-and-variables.md
    - 'Flow Control': build/flow-control.md
    - 'AI in Flows': build/ai-in-flows.md
    - 'Integrations & I/O': build/integrations.md
    - 'Managing Flows': build/managing-flows.md
  - 'Run & Monitor':
    - 'Testing': run/testing.md
    - 'Running Flows': run/running-flows.md
    - 'Scheduling': run/scheduling.md
    - 'Monitoring & Analytics': run/monitoring.md
  - 'Platform':
    - 'Forms': platform/forms.md
    - 'Knowledge Bases': platform/knowledge-bases.md
    - 'MCP Servers': platform/mcp-servers.md
    - 'Connections': platform/connections.md
    - 'Compliance & Security': platform/compliance-and-security.md
    - 'Workspace': platform/workspace.md
  - 'Block Reference':
    # BEGIN generated reference nav
    # END generated reference nav
  - 'Extend':
    - 'About Custom Actions': extend/custom-actions.md
```

- [ ] **Step 2: Verify the edited file is valid YAML**

Run: `cd automations && python3 -c "import yaml; yaml.safe_load(open('mkdocs.yml')); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Write `tools/scaffold_stubs.py`**

```python
"""Create a stub Markdown page for every new IA leaf that doesn't exist yet.

Idempotent: never overwrites an existing file. index.md and definitions.md
already exist and are intentionally absent from this list.
"""
from pathlib import Path

from tools.refgen.paths import PROJECT

CONTENT = PROJECT / "content"

PAGES = {
    "learn/quickstart.md": "Quick Start",
    "learn/concepts/flows-and-instances.md": "Flows & Instances",
    "learn/concepts/triggers.md": "Triggers",
    "learn/concepts/blocks.md": "Blocks",
    "learn/concepts/variables.md": "Variables & Data Buckets",
    "learn/concepts/expressions.md": "Expressions",
    "learn/concepts/subflows.md": "Subflows",
    "learn/concepts/shared-memory.md": "Shared Memory",
    "learn/tutorials.md": "Tutorials",
    "build/flow-editor.md": "The Flow Editor",
    "build/data-and-variables.md": "Data & Variables",
    "build/flow-control.md": "Flow Control",
    "build/ai-in-flows.md": "AI in Flows",
    "build/integrations.md": "Integrations & I/O",
    "build/managing-flows.md": "Managing Flows",
    "run/testing.md": "Testing",
    "run/running-flows.md": "Running Flows",
    "run/scheduling.md": "Scheduling",
    "run/monitoring.md": "Monitoring & Analytics",
    "platform/forms.md": "Forms",
    "platform/knowledge-bases.md": "Knowledge Bases",
    "platform/mcp-servers.md": "MCP Servers",
    "platform/connections.md": "Connections",
    "platform/compliance-and-security.md": "Compliance & Security",
    "platform/workspace.md": "Workspace",
    "extend/custom-actions.md": "About Custom Actions",
}

STUB = "# {title}\n\n!!! note\n    This page is being written.\n"


def main() -> None:
    created = 0
    for rel, title in PAGES.items():
        path = CONTENT / rel
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(STUB.format(title=title))
        created += 1
    print(f"Created {created} stub page(s).")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the scaffolder**

Run: `cd automations && python3 -m tools.scaffold_stubs`
Expected: `Created 26 stub page(s).`

- [ ] **Step 5: Commit**

```bash
cd automations
git add mkdocs.yml tools/scaffold_stubs.py content/learn content/build content/run content/platform content/extend
git commit -m "docs: restructure nav to new IA + scaffold stub pages"
```

---

## Task 9: Seed VOICE.md + park-markers

**Files:**
- Create: `automations/block-knowledge/VOICE.md`
- Modify: `automations/content/extend/custom-actions.md`, create `automations/content/run/scheduling.md` SLA note (the stub already exists; add the park note)

- [ ] **Step 1: Write `block-knowledge/VOICE.md` (seed; grows during calibration)**

```markdown
# Block Reference — Voice & Style

This spec governs the **authored prose fields** in the block-knowledge records
(`docs.purpose`, `docs.mental_model`, `docs.when_to_use`) that the reference
generator renders. It **extends** `automations/CLAUDE.md` (terminology, formatting,
tone) and `automations/MKDOCS_GUIDE.md` (design system) — it does not duplicate them.

The markdown in `content/reference/` is generated. Never hand-edit those files.
Edit the YAML records and regenerate (`make refgen`).

## Voice (seed — refined during calibration)

- Beginner-first, conversational, precise. Address the reader as "you".
- The **lede** (`docs.purpose`) says what the block does in one or two plain sentences.
  No marketing ("powerful", "seamless"), no restating the block name back at the reader.
- The **mental model** gives a concrete analogy or framing — not a restatement of the lede.
- **When to use it** is about the decision: when to reach for this block vs. a neighbour.
- Banned words/phrases: "simply", "just", "powerful", "robust", "seamless", "easy".

## Calibration log

(Generalizable rules extracted from review feedback land here, newest first.)
```

- [ ] **Step 2: Add the parked note to `content/extend/custom-actions.md`**

Replace its contents with:

```markdown
# About Custom Actions

!!! note "Coming soon"
    Custom Actions have been rebuilt. This section will be written once the redone
    feature ships to production.
```

- [ ] **Step 3: Add the parked SLA note to `content/run/scheduling.md`**

Replace its contents with:

```markdown
# Scheduling

!!! note
    This page is being written.

<!-- PARKED: SLA (Service Level Agreements) is a Business-plan feature. The end-to-end
     mechanism (SLA Calendars ↔ per-flow SLA Goals ↔ per-block Compliance Condition)
     will be documented after the app is upgraded and reviewed. See the design spec. -->
```

- [ ] **Step 4: Commit**

```bash
cd automations
git add block-knowledge/VOICE.md content/extend/custom-actions.md content/run/scheduling.md
git commit -m "docs: seed VOICE.md and add SLA + Custom Actions park-markers"
```

---

## Task 10: First generation of all reference pages (pre-calibration baseline)

Generate pages from the current records (recon-quality prose) so the pipeline is proven end-to-end and the site builds. Phase 1 calibration then improves the prose in place.

**Files:**
- Create (generated): `automations/content/reference/*.md`
- Modify (generated): `automations/mkdocs.yml` (reference nav between markers)

- [ ] **Step 1: Run the generator on the real records**

Run: `cd automations && make refgen`
Expected: `Generated reference pages into .../content/reference` and no validation errors. If validation errors print, fix the offending record's `docs.purpose` and re-run.

- [ ] **Step 2: Verify the site builds**

Run: `cd automations && mkdocs build --strict 2>&1 | tail -20`
Expected: build completes. Resolve any `--strict` nav/link warnings caused by the new structure (e.g., a stub link target). Cross-references from reference pages to not-yet-written concept pages are plain text (not links), so they will not error.

- [ ] **Step 3: Confirm anti-drift check passes on a clean tree**

Run: `cd automations && git add content/reference mkdocs.yml && git commit -m "docs(reference): generate baseline reference pages from records" && make refgen-check`
Expected: `make refgen-check` exits 0 (regenerating produces no diff).

- [ ] **Step 4: Sanity-check one generated page**

Run: `cd automations && sed -n '1,30p' content/reference/list-iterator.md`
Expected: do-not-edit header, `# List Iterator`, lede, sections.

---

## Task 11 (Phase 1): Calibrate VOICE.md on Custom Cloud Code

This is collaborative authoring. The prose is written **during execution** with Mark's review — it is not pre-written here. The steps define the loop, not the content.

**Files:**
- Modify: `automations/block-knowledge/custom-cloud-code.yaml` (`docs.purpose`, `docs.mental_model`, `docs.when_to_use`)
- Modify: `automations/block-knowledge/VOICE.md` (calibration log)
- Modify (generated): `automations/content/reference/custom-cloud-code.md`

- [ ] **Step 1: Read the current record and VOICE.md**

Run: `cd automations && sed -n '1,60p' block-knowledge/custom-cloud-code.yaml && echo --- && cat block-knowledge/VOICE.md`

- [ ] **Step 2: Rewrite the three prose fields** (`docs.purpose`, `docs.mental_model`, `docs.when_to_use`) in the FlowRunner voice, following VOICE.md. Keep all factual fields (config, behavior, gotchas, api) unchanged.

- [ ] **Step 3: Regenerate and show the rendered page to Mark**

Run: `cd automations && make refgen && sed -n '1,40p' content/reference/custom-cloud-code.md`
Then present the rendered page and ask Mark for feedback.

- [ ] **Step 4: Apply Mark's feedback to the record; extract every generalizable rule into the VOICE.md "Calibration log".** Regenerate. Repeat Step 3–4 until Mark approves.

- [ ] **Step 5: Commit**

```bash
cd automations
git add block-knowledge/custom-cloud-code.yaml block-knowledge/VOICE.md content/reference/custom-cloud-code.md
git commit -m "docs(reference): calibrate voice on Custom Cloud Code"
```

---

## Task 12 (Phase 1): Validate the voice on List Iterator

**Files:**
- Modify: `automations/block-knowledge/list-iterator.yaml`, `automations/block-knowledge/VOICE.md`, `automations/content/reference/list-iterator.md`

- [ ] **Step 1: Draft the three prose fields** for `list-iterator.yaml` following the now-seeded VOICE.md (the draft should already be closer to target).

- [ ] **Step 2: Regenerate and review with Mark**

Run: `cd automations && make refgen && sed -n '1,40p' content/reference/list-iterator.md`
Present to Mark; capture only *new* generalizable rules into VOICE.md (there should be fewer than for the first block).

- [ ] **Step 3: Commit**

```bash
cd automations
git add block-knowledge/list-iterator.yaml block-knowledge/VOICE.md content/reference/list-iterator.md
git commit -m "docs(reference): validate voice on List Iterator"
```

---

## Task 13 (Phase 1): Author prose for the remaining records (in waves)

29 remaining records. Work in **waves of ~6** so Mark reviews in digestible batches; the voice is now stable, so reviews are lighter and mostly about block-specific facts.

Suggested wave grouping (by category, so related blocks are reviewed together):
1. Control flow: `condition`, `value-router`, `repeat`, `wait`, `synchronize`, `handle-error`
2. Data/result: `set-variables`, `transform-data`, `return-result`, `assign-instance-name`
3. AI + KB blocks: `ai-agent`, `ai-router`, `knowledge-base-add-document`, `knowledge-base-list-documents`, `knowledge-base-delete-document`, `knowledge-base-delete-by-filter`
4. Integration/system: `http-request`, `call-flow`, `external-callback`, `start-scheduled-runs`, `stop-scheduled-runs`
5. Memory + groups + reusability + concepts: `shared-memory-read`, `shared-memory-put`, `shared-memory-delete`, `actions-group`, `triggers-group`, `subflow`, `knowledge-bases-concept`, `flow-scheduling-concept`

- [ ] **Step 1: For each wave** — draft the three prose fields for every record in the wave (facts unchanged), then `make refgen`.

- [ ] **Step 2: Review the wave with Mark**

Run: `cd automations && for f in <wave ids>; do echo "=== $f ==="; sed -n '1,30p' content/reference/$f.md; done`
Apply feedback; fold any new generalizable rule into VOICE.md.

- [ ] **Step 3: Commit each wave**

```bash
cd automations
git add block-knowledge/*.yaml block-knowledge/VOICE.md content/reference/*.md
git commit -m "docs(reference): author voice for <wave N category>"
```

- [ ] **Step 4: Repeat for all five waves.**

---

## Task 14 (Phase 1): Final regeneration + drift check

- [ ] **Step 1: Regenerate everything and confirm no drift**

Run: `cd automations && make refgen && make refgen-check`
Expected: `refgen-check` exits 0 (committed output already matches a fresh generation).

- [ ] **Step 2: Strict build**

Run: `cd automations && mkdocs build --strict 2>&1 | tail -20`
Expected: builds clean.

- [ ] **Step 3: Run the generator unit suite once more**

Run: `cd automations && make refgen-test`
Expected: all green.

- [ ] **Step 4: Final commit (if anything changed)**

```bash
cd automations
git add -A content/reference mkdocs.yml block-knowledge
git commit -m "docs(reference): finalize Phase 1 reference pages" || echo "nothing to commit"
```

---

## Self-Review

- **Spec coverage:** Phase 0 — new IA in mkdocs.yml (Task 8), generator with schema validation (Tasks 2–6), committed artifacts + do-not-edit header (Task 4 template + Task 6) + regen-diff check (Task 7), VOICE.md seed + park-markers (Task 9). Phase 1 — calibrate on Custom Cloud Code + List Iterator (Tasks 11–12), author all 31 (Tasks 11–13), generate + commit (Tasks 10, 13–14). Doc-facing vs internal fields enforced by template + `test_render.py::test_page_excludes_internal_fields`. Committed-not-build-time satisfied by Task 6 writing files + Task 7 check. ✔
- **Placeholders:** none — every code/template/Makefile/nav block is complete. Phase 1 tasks (11–13) intentionally do not pre-write prose because that prose IS the collaborative deliverable; the steps fully specify the loop, files, and commands.
- **Type/name consistency:** `run(records_dir, output_dir, mkdocs_path)`, `render_page(record, name_by_id)`, `validate_record(record)`, `load_records(records_dir)`, `build_reference_nav(records, indent)`, `replace_marked_block(text, begin, end, replacement)`, `update_mkdocs_nav(mkdocs_text, records)`, marker constants `BEGIN`/`END` — used consistently across tasks and tests.
- **Known soft spots:** the stub count in Task 8 Step 4 ("26") assumes `index.md` and `definitions.md` already exist (they do, per the current nav). If a strict build flags a stub nav target, create the missing file with the Task 8 STUB content.
