#!/usr/bin/env python3
"""Stop hook (non-blocking reminder): if a concept page has been edited more recently
than the last time any tracking artifact (a verdict, the ledger, AWAITING-REVIEW) was
updated, say so. That is the real drift signal (failures #3 "done too early" and #4
"ledger not updated") - and it self-quiets the moment you update tracking, so it does
not cry wolf on every turn the way a whole-working-tree scan would. Never halts the
turn; prints to stderr and exits 0."""
import glob
import os
import sys

ROOT = "/Users/mark/dev/documentation/automations"
CONTENT_DIRS = [
    os.path.join(ROOT, "content", "learn"),
    os.path.join(ROOT, "content", "platform"),
    os.path.join(ROOT, "content", "manage"),
]
EXTRA_PAGES = [os.path.join(ROOT, "content", "definitions.md")]
TRACKING = [
    os.path.join(ROOT, "docs-review", "PLATFORM-REVIEW-LEDGER.md"),
    os.path.join(ROOT, "docs-review", "AWAITING-REVIEW.md"),
]
VERDICTS_GLOB = os.path.join(ROOT, "docs-review", "verdicts", "*.md")


def mtime(p: str) -> float:
    try:
        return os.path.getmtime(p)
    except OSError:
        return 0.0


def main() -> int:
    tracking_files = list(TRACKING)
    tracking_files += [p for p in glob.glob(VERDICTS_GLOB)
                       if os.path.basename(p).lower() != "readme.md"]
    newest_tracking = max((mtime(p) for p in tracking_files), default=0.0)

    pages = list(EXTRA_PAGES)
    for d in CONTENT_DIRS:
        for base, _dirs, files in os.walk(d):
            for f in files:
                if f.endswith(".md"):
                    pages.append(os.path.join(base, f))

    drifted = [p for p in pages if mtime(p) > newest_tracking]
    if not drifted:
        return 0
    names = ", ".join(os.path.basename(p) for p in sorted(drifted)[:5])
    more = "" if len(drifted) <= 5 else f" (+{len(drifted) - 5} more)"
    sys.stderr.write(
        "Docs process reminder: concept page(s) edited since the last tracking update ("
        + names + more + "). Before calling any of them done: run /docs-review to a "
        "`ship` verdict and update the ledger + AWAITING-REVIEW. (Reminder only - not a block.)\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
