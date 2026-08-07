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
