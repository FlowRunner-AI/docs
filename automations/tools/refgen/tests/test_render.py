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


def test_sections_separated_by_blank_lines(sample_record):
    import re
    md = render_page(sample_record, name_by_id={"demo-block": "Demo Block"})
    for heading in ["## How it works", "## When to use it", "## Configuration",
                    "## Behavior", "## Things to watch for"]:
        assert f"\n\n{heading}" in md                 # heading never glued to prior block
    # regression: a table row directly followed by a heading (no blank line) swallows it
    assert "| Key |" in md
    assert re.search(r"\|\n## ", md) is None


def test_config_table_two_columns_required_folded():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "config": [
               {"field": "Key", "type": "t", "required": True, "description": "the key"}]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "| Field | Description |" in md             # 2 columns: no Type, no Required
    assert "| Type |" not in md
    assert "Required. the key" in md


def test_prose_block_names_are_linked_first_occurrence_only():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "Use a HTTP Request first, then more HTTP Request work."}}
    md = render_page(rec, name_by_id={"x": "X", "http-request": "HTTP Request"})
    assert "[HTTP Request](http-request.md)" in md
    assert md.count("[HTTP Request](http-request.md)") == 1     # first mention only
    assert "then more HTTP Request work" in md                  # second stays plain


def test_self_name_never_linked_and_code_is_protected():
    rec = {"id": "x", "name": "Cool Block", "category": "Utils",
           "docs": {"purpose": "Cool Block pairs with HTTP Request.",
                    "example": [{"code": "// HTTP Request happens elsewhere\nreturn 1;"}]}}
    md = render_page(rec, name_by_id={"x": "Cool Block", "http-request": "HTTP Request"})
    assert "[Cool Block]" not in md                              # own name never linked
    assert "[HTTP Request](http-request.md)" in md               # prose mention linked
    assert "// HTTP Request happens elsewhere" in md             # code mention untouched


def test_behavior_item_with_example_renders_indented_fence():
    rec = {"id": "x", "name": "X", "category": "Utils", "docs": {"purpose": "p"},
           "behavior": [{"note": "Throwing fails the block.", "lang": "javascript",
                         "example": 'throw new Error("nope");'},
                        "A plain bullet with no example."]}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "- Throwing fails the block." in md
    assert "  ```javascript" in md                              # fence indented under bullet
    assert '  throw new Error("nope");' in md
    assert "- A plain bullet with no example." in md


def test_common_settings_table_built_from_shared_defs():
    common = {"name": {"field": "Name", "description": "A label."},
              "logging": {"field": "Logging", "description": "What to log."}}
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "common": ["name", "logging"],
                    "config": [{"field": "Key", "description": "the key"}]}}
    md = render_page(rec, name_by_id={"x": "X"}, common_defs=common)
    assert "## Configuration" in md
    assert "| Key |" in md                              # block-specific field still shown
    assert "**Common settings**" in md
    assert "| Name | A label. |" in md
    assert "| Logging | What to log. |" in md

    # opted out -> no common-settings table
    rec2 = {"id": "y", "name": "Y", "category": "Utils",
            "docs": {"purpose": "p", "config": [{"field": "Key", "description": "k"}]}}
    assert "**Common settings**" not in render_page(rec2, name_by_id={"y": "Y"}, common_defs=common)


def test_example_renders_interleaved_steps_in_order():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "example": [
               {"text": "Like so:"},
               {"lang": "json", "code": '[{"id": 1}]'},
               {"text": "Then the loop runs."},
               {"image": "../images/reference/x.png", "alt": "x in the editor"},
               {"text": "Done."}]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "## Example" in md
    # order is preserved: intro text, then code, then the next text, then image, then closing text
    order = [md.index("Like so:"), md.index("```json"), md.index("Then the loop runs."),
             md.index("![x in the editor]"), md.index("Done.")]
    assert order == sorted(order)
    assert '[{"id": 1}]' in md


def test_limitations_section_preferred_over_gotchas():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "limitations": ["No network access."],
                    "gotchas": ["should be ignored when limitations present"]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "## Limitations" in md
    assert "No network access." in md
    assert "## Things to watch for" not in md
