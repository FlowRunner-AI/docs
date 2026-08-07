"""Core linting logic: turn a markdown page into a list of Violations.

Pure functions over text so the rules are unit-testable without touching disk.
"""
from __future__ import annotations

import functools
import re
from dataclasses import dataclass

# A ((Component)) marker - the authored signal that the prose points the reader at a
# real on-screen UI element. Identical pattern to render.py's _CONTROL_MARKER so the
# linter and the renderer agree on what a control reference is.
_CONTROL_MARKER = re.compile(r"\(\(\s*(.+?)\s*\)\)", re.DOTALL)

# Fenced and inline code: a ((...)) or a banned word inside code is literal content,
# not prose, so it must not count. Same protection render.py applies.
_CODE = re.compile(r"```.*?```|``(?:[^`]|`(?!`))*?``|`[^`]*`", re.DOTALL)

# A markdown image embed.
_IMAGE = re.compile(r"!\[(?:[^\]]|\](?!\())*\]\([^)]+\)")   # alt may contain ] (e.g. [0]); only ]( closes

# An acknowledged-gap marker authors leave where a screenshot is owed but not yet
# captured. It does NOT make a section "done" - it just distinguishes a known TODO
# from an unnoticed omission in the report.
_SHOT_NEEDED = re.compile(r"<!--\s*SCREENSHOT[ -]?NEEDED", re.IGNORECASE)

# VOICE.md banned filler/marketing words. Word-boundaried; reported as warnings
# because a few have safe homonyms ("just as") and they are a style signal, not the
# structural failure the hard gate is for.
_BANNED = re.compile(r"\b(simply|powerful|robust|seamless|effortless)\b", re.IGNORECASE)

# VOICE.md: no em-dashes. The literal em-dash character.
_EMDASH = re.compile(r"—")

# Plain-prose pointers at the screen that authors sometimes leave UNMARKED (no
# ((...)) around them), which is how Variables/Expressions escaped the precise gate
# while pointing the reader at "the wand icon", "the Expression Editor", etc.
# Heuristic, so it warns (the ((...)) rule and the adversarial review carry the hard
# gate). Tuned for high precision: a named UI surface, a "the X <ui-noun>" phrase, or
# an imperative UI verb.
_PROSE_UI = re.compile(
    r"\b[Tt]he\s+[\w'-]+\s+(?:icon|button|toggle|dropdown|drop-down|picker|wand|tab)\b"
    r"|\b[Tt]he\s+(?:Expression Editor|Flow Editor|canvas|palette|block list|"
    r"config(?:uration)? panel|properties panel|settings panel)\b"
    r"|\b(?:[Cc]lick|[Hh]over over|[Hh]over the)\b",
)

# The text part of a markdown link, `[text](url)`. Group 1 is the linkable text; its
# span tells us whether a block-name occurrence is already inside a link.
_LINK_TEXT = re.compile(r"\[((?:[^\]]|\](?!\())*)\]\([^)]+\)")

# Author escape hatch for the rare legitimate non-block use of a block's name:
# `<!-- doclint: allow-unlinked: HTTP Request, Wait -->`. Visible in the diff, so it
# can never be a silent skip.
_ALLOW_UNLINKED = re.compile(r"<!--\s*doclint:\s*allow-unlinked:\s*(.+?)\s*-->", re.IGNORECASE)

# Block names that are also ordinary English words: a bare "Wait" may be the verb, not
# the block, so their unlinked first mention WARNs (review decides) rather than ERRORs.
# Everything else - all multi-word names, plus distinctive single words like SubFlow -
# is unambiguous and ERRORs. (Mirrors the precise/fuzzy split already in this linter.)
AMBIGUOUS_BLOCK_NAMES = frozenset({"Break", "Condition", "Repeat", "Synchronize", "Wait"})

_TRAILING_PAREN = re.compile(r"\s*\([^)]*\)\s*$")

# HTML comments are author notes, not prose the reader sees - a block name inside one
# is not a "mention" and cannot carry a link.
_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)

# A FlowRunner flow can start with ANYTHING (an API call, a schedule, a manual launch,
# a trigger) - never frame the start as trigger-based (a product differentiator Mark
# has corrected repeatedly). High-precision phrasings only; the adversarial review
# carries the subtler cases. Skipped on the Triggers page and by an escape comment.
_TRIGGER_START = re.compile(
    r"payload\s+from\s+(?:its|the)\s+trigger"
    r"|from\s+its\s+trigger"
    r"|(?:flows?|runs?|instances?)\s+(?:starts?|start|begins?|begin)\s+(?:with|from)\s+(?:a|its|the)\s+trigger"
    r"|starts?\s+(?:a\s+)?(?:flow|run|instance)\s+with\s+(?:a|its|the)\s+trigger",
    re.IGNORECASE,
)
_TRIGGER_ALLOW = re.compile(r"<!--\s*doclint:\s*allow:\s*trigger-start\s*-->", re.IGNORECASE)

# A block reference rendered as a green pill: `[Name](...){.fr-block}` on narrative
# pages, `<span class="fr-block">` on generated pages. A section that names a block
# this way is documenting that block and should SHOW it (or consciously opt out).
_FRBLOCK = re.compile(r"\{\.fr-block\}|class=\"fr-block\"")

# Author's conscious "this section needs no screenshot, and here's why" opt-out. Visible
# in the diff, so a shot-less section is a decision on record, never an unnoticed gap.
_NO_SHOT = re.compile(r"<!--\s*doclint:\s*no-shot:", re.IGNORECASE)

SEVERITY_ERROR = "error"
SEVERITY_WARN = "warn"


@functools.lru_cache(maxsize=1)
def load_block_names() -> tuple[str, ...]:
    """The linkable names of every block-knowledge record, e.g. 'External Callback'.
    A trailing parenthetical ('Flow Memory (Agent Memory)') is stripped to the phrase
    a reader actually writes in prose ('Flow Memory'). Loaded once, from disk."""
    from tools.refgen.loader import load_records  # local import keeps lint_text pure
    from tools.refgen.paths import RECORDS_DIR
    names: list[str] = []
    for rec in load_records(RECORDS_DIR):
        name = _TRAILING_PAREN.sub("", rec.get("name", "")).strip()
        if name:
            names.append(name)
    return tuple(names)


@dataclass(frozen=True)
class Violation:
    severity: str
    line: int          # 1-based line in the file
    rule: str
    message: str


@dataclass
class Section:
    title: str         # heading text ("(intro)" for the lede block before the first h2)
    level: int         # 0 for the intro block, else the heading level
    start_line: int    # 1-based line of the heading (or 1 for the intro)
    body: str          # raw markdown of the section, heading line excluded


def _strip_code(md: str) -> str:
    """Replace code spans with blank space of the same length, so offsets are
    preserved (line numbers stay correct) but nothing inside code matches."""
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    return _CODE.sub(blank, md)


def split_sections(md: str) -> list[Section]:
    """Split a page into its intro block (before the first ## ) and one Section per
    ## / ### heading. Headings inside fenced code are ignored."""
    safe = _strip_code(md)
    lines = md.splitlines()
    safe_lines = safe.splitlines()
    heads: list[tuple[int, int, str]] = []  # (idx, level, title)
    for i, sline in enumerate(safe_lines):
        m = re.match(r"^(#{2,6})\s+(.*)$", sline)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))

    sections: list[Section] = []
    first = heads[0][0] if heads else len(lines)
    intro_body = "\n".join(lines[:first])
    sections.append(Section("(intro)", 0, 1, intro_body))

    for n, (idx, level, title) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        body = "\n".join(lines[idx + 1:end])
        sections.append(Section(title, level, idx + 1, body))
    return sections


def _controls(text: str) -> list[str]:
    return [m.group(1).strip() for m in _CONTROL_MARKER.finditer(_strip_code(text))]


def _images(text: str) -> int:
    return len(_IMAGE.findall(text))


def _blank_same_len(m: re.Match) -> str:
    return re.sub(r"[^\n]", " ", m.group(0))


def block_link_violations(md: str, block_names) -> list[Violation]:
    """The first body mention of a known block name must sit inside a markdown link.
    Bare -> ERROR (distinctive names) / WARN (ambiguous common words). Mentions inside
    code, image alt text, or headings do not count (they cannot carry a prose link)."""
    coded = _strip_code(md)                                   # blank code, keep length
    coded = _COMMENT.sub(_blank_same_len, coded)              # comments are not prose
    link_spans = [(m.start(1), m.end(1)) for m in _LINK_TEXT.finditer(coded)]

    search = _IMAGE.sub(_blank_same_len, coded)               # alt text is not prose
    lines = search.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^#{1,6}\s", line):                      # headings are not prose
            lines[i] = " " * len(line)
    search = "\n".join(lines)

    allowed = {n.strip() for m in _ALLOW_UNLINKED.finditer(md) for n in m.group(1).split(",")}

    out: list[Violation] = []
    for name in sorted(set(block_names), key=len, reverse=True):   # longest-first
        if name in allowed:
            continue
        m = re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", search)
        if not m:
            continue
        s, e = m.start(), m.end()
        if any(a <= s and e <= b for a, b in link_spans):         # already linked
            continue
        line = md[:s].count("\n") + 1
        if name in AMBIGUOUS_BLOCK_NAMES:
            out.append(Violation(SEVERITY_WARN, line, "block-link",
                f"first mention of '{name}' is not linked; if it means the block, "
                f"link it to its reference page"))
        else:
            out.append(Violation(SEVERITY_ERROR, line, "block-link",
                f"first mention of block '{name}' must link to its reference page "
                f"(e.g. [{name}](...)); add the link or a `doclint: allow-unlinked` comment"))
    return out


def lint_text(md: str, path: str = "<page>", block_names=None) -> list[Violation]:
    """Return all violations for one page's markdown."""
    out: list[Violation] = []
    safe = _strip_code(md)
    safe_lines = safe.splitlines()

    # --- structure: exactly one H1, present, first ---
    h1s = [i for i, l in enumerate(safe_lines) if re.match(r"^#\s+\S", l)]
    if len(h1s) == 0:
        out.append(Violation(SEVERITY_ERROR, 1, "structure", "no H1 title (a page needs one '# Title')"))
    elif len(h1s) > 1:
        out.append(Violation(SEVERITY_ERROR, h1s[1] + 1, "structure", "more than one H1; a page has exactly one"))

    # --- structure: no nesting deeper than h3 ---
    for i, l in enumerate(safe_lines):
        if re.match(r"^#{4,6}\s+\S", l):
            out.append(Violation(SEVERITY_ERROR, i + 1, "structure",
                                 "heading deeper than h3; split the page instead"))

    # --- em-dash ---
    for i, l in enumerate(safe.splitlines()):
        if _EMDASH.search(l):
            out.append(Violation(SEVERITY_ERROR, i + 1, "em-dash",
                                 "em-dash (—) is banned; use ' - ' or restructure"))

    # --- banned words (warn) ---
    for i, l in enumerate(safe.splitlines()):
        for m in _BANNED.finditer(l):
            out.append(Violation(SEVERITY_WARN, i + 1, "banned-word",
                                 f"banned filler/marketing word: '{m.group(0)}'"))

    # --- trigger-start framing (warn): a flow can start with anything, not a trigger ---
    if "trigger" not in path.lower() and not _TRIGGER_ALLOW.search(md):
        for i, l in enumerate(safe.splitlines()):
            if _TRIGGER_START.search(l):
                out.append(Violation(SEVERITY_WARN, i + 1, "trigger-start",
                    "a flow can start with anything, not just a trigger - do not frame the "
                    "start as trigger-based (Initial Data = the data sent when a run starts; a "
                    "trigger's data lives on the trigger block). Reword, or add "
                    "'<!-- doclint: allow: trigger-start -->' if this genuinely is about triggers"))

    sections = split_sections(md)

    # --- lede present: intro block must have prose after the H1 ---
    intro = sections[0]
    intro_after_h1 = re.sub(r"^#\s+.*$", "", intro.body, flags=re.MULTILINE).strip()
    # also strip the title line that lives before the first content line
    if h1s:
        first_h1_line = h1s[0]
        # text between the H1 and the first heading, minus HTML comments
        between = "\n".join(md.splitlines()[first_h1_line + 1:
                            (sections[1].start_line - 1) if len(sections) > 1 else len(md.splitlines())])
        between = re.sub(r"<!--.*?-->", "", between, flags=re.DOTALL).strip()
        if not between:
            out.append(Violation(SEVERITY_ERROR, first_h1_line + 1, "lede",
                                 "no lede: a page needs a plain-prose lede between the H1 and the first ## section"))

    # --- the hard gate: screenshot coverage, per section ---
    for sec in sections:
        ctrls = _controls(sec.body)
        imgs = _images(sec.body)
        if ctrls and imgs == 0:
            ack = bool(_SHOT_NEEDED.search(sec.body))
            distinct = sorted(set(ctrls))
            tag = " (SCREENSHOT-NEEDED marker present - still not done)" if ack else ""
            out.append(Violation(
                SEVERITY_ERROR, sec.start_line, "screenshot-coverage",
                f"section '{sec.title}' points the reader at on-screen controls "
                f"({', '.join(repr(c) for c in distinct[:6])}"
                f"{', ...' if len(distinct) > 6 else ''}) but has no screenshot{tag}",
            ))
        elif imgs == 0:
            # No marked controls, but plain prose may still point at the screen.
            hit = _PROSE_UI.search(_strip_code(sec.body))
            if hit:
                out.append(Violation(
                    SEVERITY_WARN, sec.start_line, "screenshot-coverage-prose",
                    f"section '{sec.title}' appears to point at the screen "
                    f"(\"{hit.group(0).strip()}\") with no screenshot and no (( )) "
                    f"marker - mark the control and add a shot, or confirm it is "
                    f"purely conceptual",
                ))

        # --- section-shot (warn): an H2 that documents a block should SHOW it ---
        # A section naming a block via a .fr-block pill, with no screenshot and no
        # conscious opt-out, is the Writing/Counter miss - forces a per-section decision.
        if (sec.level == 2 and imgs == 0 and not ctrls
                and sec.title.strip().lower() != "related"
                and _FRBLOCK.search(sec.body) and not _NO_SHOT.search(sec.body)):
            out.append(Violation(
                SEVERITY_WARN, sec.start_line, "section-shot",
                f"section '{sec.title}' documents a block but has no screenshot; add a real "
                f"shot of the scenario, or mark '<!-- doclint: no-shot: <reason> -->' to opt out",
            ))

    # --- block-link coverage: first mention of a block links to its reference ---
    names = load_block_names() if block_names is None else block_names
    out.extend(block_link_violations(md, names))

    out.sort(key=lambda v: (v.line, 0 if v.severity == SEVERITY_ERROR else 1))
    return out


def errors(violations: list[Violation]) -> list[Violation]:
    return [v for v in violations if v.severity == SEVERITY_ERROR]
