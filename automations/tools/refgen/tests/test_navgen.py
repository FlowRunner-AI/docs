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
