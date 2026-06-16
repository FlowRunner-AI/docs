"""Generate all Block Reference pages from block-knowledge records.

Usage (from automations/):  python -m tools.refgen.generate
"""
import sys
from pathlib import Path

from . import paths
from .loader import load_records
from .navgen import update_mkdocs_nav
from .render import render_page
from .schema import validate_record


def run(records_dir: Path, output_dir: Path, mkdocs_path: Path) -> list[str]:
    """Validate, render, write pages, and update the nav. Returns error list.

    On any validation error, nothing is written (fail fast, no partial output).
    """
    records = load_records(records_dir)

    errors: list[str] = []
    for r in records:
        errors.extend(validate_record(r))
    if errors:
        return errors

    name_by_id = {r["id"]: r["name"] for r in records}

    output_dir.mkdir(parents=True, exist_ok=True)
    for r in records:
        page = render_page(r, name_by_id=name_by_id)
        (output_dir / f"{r['id']}.md").write_text(page)

    mkdocs_path.write_text(update_mkdocs_nav(mkdocs_path.read_text(), records))
    return []


def main() -> int:
    errors = run(paths.RECORDS_DIR, paths.OUTPUT_DIR, paths.MKDOCS)
    if errors:
        print("Reference generation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"Generated reference pages into {paths.OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
