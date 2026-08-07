"""doclint CLI: scan documentation pages and fail on any error-level violation.

    python3 -m tools.doclint                 # scan the default narrative page set
    python3 -m tools.doclint path/to/page.md # scan specific files/dirs
    python3 -m tools.doclint --warnings      # also print warnings (always exit on errors)

Exit code is non-zero if any error-level violation exists, so it can gate a build.
"""
from __future__ import annotations

import sys
from pathlib import Path

from tools.refgen.paths import PROJECT
from tools.doclint.lint import lint_text, SEVERITY_ERROR, SEVERITY_WARN

# The narrative pages this gate governs by default: the concept pages, the platform
# pages, and the terminology page. Reference pages are generated and can be added
# explicitly when wanted.
DEFAULT_TARGETS = [
    PROJECT / "content" / "learn" / "concepts",
    PROJECT / "content" / "platform",
    PROJECT / "content" / "manage",
    PROJECT / "content" / "definitions.md",
]

RED = "\033[31m"
YEL = "\033[33m"
DIM = "\033[2m"
RST = "\033[0m"


def _iter_md(targets: list[Path]):
    for t in targets:
        if t.is_dir():
            yield from sorted(t.rglob("*.md"))
        elif t.suffix == ".md" and t.exists():
            yield t


def main(argv: list[str]) -> int:
    show_warn = "--warnings" in argv or "-w" in argv
    args = [a for a in argv if not a.startswith("-")]
    targets = [Path(a).resolve() for a in args] if args else DEFAULT_TARGETS

    total_err = total_warn = pages = 0
    for md_path in _iter_md(targets):
        pages += 1
        violations = lint_text(md_path.read_text(encoding="utf-8"), str(md_path))
        errs = [v for v in violations if v.severity == SEVERITY_ERROR]
        warns = [v for v in violations if v.severity == SEVERITY_WARN]
        total_err += len(errs)
        total_warn += len(warns)
        shown = errs + (warns if show_warn else [])
        if not shown:
            continue
        rel = md_path.relative_to(PROJECT) if PROJECT in md_path.parents else md_path
        print(f"\n{rel}")
        for v in shown:
            colour = RED if v.severity == SEVERITY_ERROR else YEL
            print(f"  {colour}{v.severity.upper():5}{RST} {DIM}L{v.line:<4}{RST} "
                  f"[{v.rule}] {v.message}")

    print(f"\n{DIM}doclint: {pages} pages, "
          f"{RED if total_err else ''}{total_err} errors{RST}{DIM}, "
          f"{total_warn} warnings{RST}")
    if total_err and not show_warn:
        print(f"{DIM}(run with --warnings to see {total_warn} warnings too){RST}")
    return 1 if total_err else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
