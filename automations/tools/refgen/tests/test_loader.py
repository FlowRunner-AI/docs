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
