#!/usr/bin/env bash
# PostToolUse hook: append every FlowRunner MCP Flow Builder tool call + response to a JSONL run log.
# Claude Code pipes the hook payload (session_id, tool_name, tool_input, tool_response, ...) on stdin.
set -u
ROOT="${CLAUDE_PROJECT_DIR:-/Users/mark/dev/documentation}"
OUT_DIR="$ROOT/automations/.cache/mcp-qa"
mkdir -p "$OUT_DIR"
OUT="$OUT_DIR/run-$(date +%Y-%m-%d).jsonl"
python3 -c '
import json, sys, datetime
out = sys.argv[1]
raw = sys.stdin.read()
try:
    p = json.loads(raw)
except Exception:
    p = {"_unparsed": raw}
rec = {
    "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "session_id": p.get("session_id"),
    "tool_name": p.get("tool_name"),
    "tool_input": p.get("tool_input"),
    "tool_response": p.get("tool_response"),
}
with open(out, "a") as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
' "$OUT"
exit 0
