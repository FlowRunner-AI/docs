import yaml

from tools.refgen.navgen import (
    build_concept_nav,
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


def _records_with_concepts():
    return _records() + [
        {"id": "flow-memory-concept", "name": "Flow Memory", "category": "Concepts",
         "concept": True},
        {"id": "knowledge-bases-concept", "name": "Knowledge Bases", "category": "Concepts",
         "concept": True},
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


def test_reference_nav_excludes_concept_pages():
    frag = build_reference_nav(_records_with_concepts(), indent=4)
    assert "Concepts" not in frag                       # no concept category group
    assert "flow-memory-concept" not in frag
    assert "reference/ai-agent.md" in frag              # blocks still present


def test_concept_nav_is_a_flat_list_sorted_by_name():
    frag = build_concept_nav(_records_with_concepts(), indent=4)
    lines = [ln.rstrip() for ln in frag.splitlines() if ln.strip()]
    assert lines == [
        "    - 'Flow Memory': reference/flow-memory-concept.md",
        "    - 'Knowledge Bases': reference/knowledge-bases-concept.md",
    ]


def test_update_nav_injects_concepts_when_markers_present():
    # Concept Guides now live in a sub-section under Platform (6-space markers).
    mkdocs = (
        "nav:\n"
        "  - 'Platform':\n"
        "    - 'Concept Guides':\n"
        "      # BEGIN generated concept nav\n"
        "      # END generated concept nav\n"
        "  - 'Block Reference':\n"
        "    # BEGIN generated reference nav\n"
        "    # END generated reference nav\n"
    )
    out = update_mkdocs_nav(mkdocs, _records_with_concepts())
    data = yaml.safe_load(out)                           # must remain valid YAML
    nav = {list(s.keys())[0]: list(s.values())[0] for s in data["nav"]}
    # the concept pages render under Platform > Concept Guides
    concept_guides = next(v for item in nav["Platform"]
                          if isinstance(item, dict) and "Concept Guides" in item
                          for v in [item["Concept Guides"]])
    assert {"Flow Memory": "reference/flow-memory-concept.md"} in concept_guides
    # concept pages must NOT appear inside Block Reference
    assert "flow-memory-concept" not in str(nav["Block Reference"])


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
