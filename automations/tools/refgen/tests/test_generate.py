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
