#!/usr/bin/env python3
"""PostToolUse hook: after an Edit/Write to a narrative content page, run doclint on
that file and surface the result to the model as additional context. Keeps the
mechanical floor running itself instead of relying on me to remember `make doclint`.

Reads the tool-call JSON on stdin; a no-op (exit 0, no output) for anything that is not
a narrative concept/platform/manage markdown page. Generated reference pages and image
files are skipped (they have their own gate / are not linted)."""
import json
import os
import subprocess
import sys

ROOT = "/Users/mark/dev/documentation/automations"


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tin = data.get("tool_input", {}) or {}
    fp = tin.get("file_path") or tin.get("path") or ""
    if not fp or not fp.endswith(".md"):
        return 0
    if "/automations/content/" not in fp:
        return 0
    if "/content/reference/" in fp or "/content/images/" in fp:
        return 0
    try:
        rel = os.path.relpath(fp, ROOT)
    except Exception:
        rel = fp
    try:
        r = subprocess.run(
            ["python3", "-m", "tools.doclint", fp, "--warnings"],
            cwd=ROOT, capture_output=True, text=True, timeout=60,
        )
        out = (r.stdout + r.stderr).strip()
    except Exception:
        return 0
    if not out:
        return 0
    msg = f"[doclint auto-run on {rel}]\n{out}"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
