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


def test_related_unknown_id_is_dropped():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p", "cross_refs": ["nope-concept", "y"]}}
    md = render_page(rec, name_by_id={"x": "X", "y": "Y"})
    assert "nope-concept" not in md                 # unresolved ref dropped, not a bare slug
    assert "[Y](y.md)" in md                         # a resolvable ref still links


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
    assert "[HTTP Request](http-request.md){.fr-block}" in md   # first mention linked + styled
    assert md.count("](http-request.md)") == 1                  # only the first mention links
    assert '<span class="fr-block">HTTP Request</span>' in md   # second mention styled, not linked


def test_self_name_never_linked_and_code_is_protected():
    rec = {"id": "x", "name": "Cool Block", "category": "Utils",
           "docs": {"purpose": "Cool Block pairs with HTTP Request.",
                    "example": [{"code": "// HTTP Request happens elsewhere\nreturn 1;"}]}}
    md = render_page(rec, name_by_id={"x": "Cool Block", "http-request": "HTTP Request"})
    assert "[Cool Block]" not in md                              # own name never linked
    assert '<span class="fr-block">Cool Block</span>' in md      # own name still styled
    assert "[HTTP Request](http-request.md){.fr-block}" in md    # prose mention linked + styled
    assert "// HTTP Request happens elsewhere" in md             # code mention untouched


def test_config_field_name_not_linkified_but_description_is():
    # A config field named like a block ("Condition") must NOT pill in the Field
    # column, but a block name in the Description column still links.
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p",
                    "config": [{"field": "Condition",
                                "description": "Mirrors the Condition block's test."}]}}
    md = render_page(rec, name_by_id={"x": "X", "condition": "Condition"})
    assert "| Condition |" in md                                 # field name stays plain
    assert "[Condition](condition.md){.fr-block}" in md          # but the description links it
    assert md.count("](condition.md)") == 1                      # only the description, not the field cell


def test_concept_guide_links_plainly_never_as_a_block_pill():
    # A concept guide is a page, not a canvas block: its mentions must link as
    # ordinary prose (no green .fr-block pill), first mention only, plain text after.
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "See Error Handling for recovery; Error Handling covers strategy."}}
    md = render_page(rec, name_by_id={"x": "X", "error-handling-concept": "Error Handling"},
                     concept_ids={"error-handling-concept"})
    assert "[Error Handling](error-handling-concept.md)" in md            # first mention: ordinary link
    assert "(error-handling-concept.md){.fr-block}" not in md             # never a block pill
    assert '<span class="fr-block">Error Handling</span>' not in md       # never a green span
    assert md.count("](error-handling-concept.md)") == 1                  # only the first mention links


def test_ui_component_markers_become_chips():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "Open ((Manage Capabilities)), set the ((System Prompt)), then turn on ((Force Parsed Output)).",
                    "gotchas": ["Leave ((Force Parsed Output)) off and the reply is plain text."]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert '<span class="fr-control">Manage Capabilities</span>' in md
    assert '<span class="fr-control">System Prompt</span>' in md
    # marked in both the lede and a gotcha (after the config block) - 2 chips
    assert md.count('<span class="fr-control">Force Parsed Output</span>') == 2
    assert "((" not in md and "))" not in md          # every marker consumed


def test_marker_inside_code_is_left_literal():
    rec = {"id": "x", "name": "X", "category": "Utils",
           "docs": {"purpose": "p",
                    "example": [{"lang": "text", "code": "result = ((not a chip))"}]}}
    md = render_page(rec, name_by_id={"x": "X"})
    assert "result = ((not a chip))" in md                          # code marker stays literal
    assert '<span class="fr-control">not a chip</span>' not in md


def test_marked_component_containing_a_block_name_not_split_by_linkify():
    # "Wait for completion" contains the Wait block name; the chip must stay whole.
    rec = {"id": "call-flow", "name": "Call Flow", "category": "Utils",
           "docs": {"purpose": "Turn on ((Wait for completion)) to pause for the result."}}
    md = render_page(rec, name_by_id={"call-flow": "Call Flow", "wait": "Wait"})
    assert 'Turn on <span class="fr-control">Wait for completion</span> to pause' in md
    assert '<span class="fr-block">Wait</span> for completion' not in md


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
