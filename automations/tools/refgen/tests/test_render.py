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
