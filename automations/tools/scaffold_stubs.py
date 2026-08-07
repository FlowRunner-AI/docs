"""Create a stub Markdown page for every new IA leaf that doesn't exist yet.

Idempotent: never overwrites an existing file. index.md and definitions.md
already exist and are intentionally absent from this list.
"""
from pathlib import Path

from tools.refgen.paths import PROJECT

CONTENT = PROJECT / "content"

PAGES = {
    "learn/quickstart.md": "Quick Start",
    "learn/concepts/flows-and-instances.md": "Flows & Instances",
    "learn/concepts/triggers.md": "Triggers",
    "learn/concepts/blocks.md": "Blocks",
    "learn/concepts/variables.md": "Variables & Data Buckets",
    "learn/concepts/expressions.md": "Expressions",
    "learn/concepts/subflows.md": "Subflows",
    "learn/concepts/shared-memory.md": "Shared Memory",
    "learn/tutorials.md": "Tutorials",
    "build/flow-editor.md": "The Flow Editor",
    "build/data-and-variables.md": "Data & Variables",
    "build/flow-control.md": "Flow Control",
    "build/ai-in-flows.md": "AI in Flows",
    "build/integrations.md": "Integrations & I/O",
    "build/managing-flows.md": "Managing Flows",
    "run/testing.md": "Testing",
    "run/running-flows.md": "Running Flows",
    "run/scheduling.md": "Scheduling",
    "run/monitoring.md": "Monitoring & Analytics",
    "platform/forms.md": "Forms",
    "platform/knowledge-bases.md": "Knowledge Bases",
    "platform/mcp-servers.md": "MCP Servers",
    "platform/connections.md": "Connections",
    "platform/compliance-and-security.md": "Compliance & Security",
    "platform/workspace.md": "Workspace",
    "extend/custom-actions.md": "About Custom Actions",
}

STUB = "# {title}\n\n!!! note\n    This page is being written.\n"


def main() -> None:
    created = 0
    for rel, title in PAGES.items():
        path = CONTENT / rel
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(STUB.format(title=title))
        created += 1
    print(f"Created {created} stub page(s).")


if __name__ == "__main__":
    main()
