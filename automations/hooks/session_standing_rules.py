#!/usr/bin/env python3
"""SessionStart hook: inject the docs standing rules so the process (the four failure
modes + the /docs-plan -> /docs-review -> /docs-feedback loop + "done = ship verdict")
is in context every session, not only when I happen to remember it."""
import json
import os
import sys

ROOT = "/Users/mark/dev/documentation/automations"
RULES = os.path.join(ROOT, "docs-review", "STANDING-RULES.md")


def main() -> int:
    try:
        with open(RULES, encoding="utf-8") as f:
            text = f.read().strip()
    except Exception:
        return 0
    if not text:
        return 0
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": text,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
