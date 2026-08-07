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
