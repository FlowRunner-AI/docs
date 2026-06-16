"""Canonical project paths, resolved relative to this file.

tools/refgen/paths.py -> parents[2] is the automations/ project root.
"""
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]          # .../automations
RECORDS_DIR = PROJECT / "block-knowledge"
OUTPUT_DIR = PROJECT / "content" / "reference"
MKDOCS = PROJECT / "mkdocs.yml"
TEMPLATES = Path(__file__).resolve().parent / "templates"

# Files in block-knowledge that are NOT block records:
NON_RECORD_FILES = {"README.md", "VOICE.md"}
