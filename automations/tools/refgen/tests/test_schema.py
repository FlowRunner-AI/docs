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
