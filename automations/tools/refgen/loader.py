"""Load block-knowledge YAML records from disk."""
from pathlib import Path

import yaml

from .paths import NON_RECORD_FILES


def load_records(records_dir: Path) -> list[dict]:
    """Return all block records in `records_dir`, sorted by display name.

    Skips non-record files (README.md, VOICE.md). Each record must parse to a
    dict; anything else raises ValueError so a malformed file fails loudly.
    """
    records: list[dict] = []
    for path in sorted(records_dir.glob("*.yaml")):
        if path.name in NON_RECORD_FILES:
            continue
        data = yaml.safe_load(path.read_text())
        if not isinstance(data, dict):
            raise ValueError(f"{path.name}: expected a mapping, got {type(data).__name__}")
        records.append(data)
    records.sort(key=lambda r: r.get("name", r.get("id", "")))
    return records
