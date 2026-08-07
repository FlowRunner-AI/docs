#!/usr/bin/env bash
# Launch @playwright/mcp under a Node >= 20 runtime.
#
# Why this exists: this machine's default nvm node is v18, but @playwright/mcp@latest
# dropped Node 18 support ("Playwright requires Node.js 20 or higher"), so a bare
# `npx @playwright/mcp@latest` fails to connect. We prepend the newest installed
# Node 20/22 to PATH so the MCP server starts under a supported runtime, then exec
# npx with whatever flags .mcp.json passes through.
set -euo pipefail

n20="$(ls -d "$HOME"/.nvm/versions/node/v2* 2>/dev/null | sort -V | tail -1 || true)"
if [ -n "${n20:-}" ] && [ -x "$n20/bin/node" ]; then
  export PATH="$n20/bin:$PATH"
fi

exec npx -y @playwright/mcp@latest "$@"
