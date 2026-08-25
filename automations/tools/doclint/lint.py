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

# An authored expression token, `{{Initial Data->orderId}}`, renders as an .fr-expr pill - it is a
# value reference, not prose, so a block name inside one is not a linkable "mention" (same reason
# code spans and image alt text are excluded).
_EXPR_TOKEN = re.compile(
    r"\{\{.*?\}\}"                                    # authored form on narrative pages
    r"|<span class=\"fr-expr\">.*?</span>",             # rendered form on generated pages
    re.DOTALL,
)

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


# An API call, trigger, event, or schedule starts an INSTANCE (a run) - the flow itself is
# "started" only in the Start-flow/LIVE sense (Mark, 2026-08-24: "A flow MUST BE started in
# order for Call Flow to work. The API starts an instance. It is an important distinction").
# Keyed on an actor word so legitimate "start the flow" (the Start flow action) never flags.
# Runtime verbs belong to the RUN, not the flow: "a flow that never reaches a Return Result"
# (gate round 18) is the same correction in a verb form the actor-keyed pattern below cannot see.
# Deliberately narrow: only forms where the FLOW is the subject of one execution's completed or
# negated progress ("a flow that never reaches ...", "the flow has finished", "the flow terminated").
# The present-tense design description common in block references ("when the flow reaches this
# block") is NOT flagged - that is a corpus-wide house-style question for the product owner.
_FLOW_RUNTIME_VERB = re.compile(
    r"\bflows?\b(?!['’]s\s+run)(?![^.\n]{0,30}\bversions?\b)"
    r"[^.\n]{0,25}?\b(?:never|already|has|have|had)\b[^.\n]{0,15}?"
    r"\b(?:reach(?:es|ed)|finish(?:es|ed)|terminat(?:es|ed))\b",
    re.IGNORECASE,
)

_FLOW_VS_INSTANCE = re.compile(
    r"\b(?:request|call|api|endpoint|trigger|event|schedule|timer|webhook|activation|fetch)\b"
    r"[^.\n]{0,60}?\bstart(?:s|ing)?\s+(?:the|a|an|your)\s+flows?\b",
    re.IGNORECASE,
)

# A bullet list interrupted by a block-level image or paragraph at column 0: markdown ends the
# list there, and the bullets that follow the interruption are swallowed into that block's
# paragraph - they ship as a literal "- " line, not an <li>. Round 19 and round 22 both shipped
# this on the same page; doclint saw nothing because the source "looks" like a list.
_BULLET = re.compile(r"^[-*+]\s+\S")

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
    coded = _EXPR_TOKEN.sub(_blank_same_len, coded)           # expression pills are not prose
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




# --- dead anchors: an authored #fragment must match a real heading slug ---------------
# Mark's 2026-08-24 Endpoint retitle ("Endpoint" -> "Endpoint (`GET` or `POST`)") changed
# the heading's slug and silently killed every authored [.](#endpoint) link on the page.
# This check recomputes each heading's slug the way the site does (python-markdown's
# default toc slugify - the config sets no custom slugify) and errors on any authored
# same-page `#fragment`, or cross-page `page.md#fragment` when the target file is
# readable, that no heading produces.
_MD_LINK = re.compile(r"(?<!\!)\[(?:[^\]]|\](?!\())*\]\(([^)\s]+)\)")


def _toc_slug(title: str) -> str:
    """python-markdown's default toc slugify (the renderer this site uses)."""
    import unicodedata
    value = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def heading_slugs(md: str) -> set[str]:
    """Every anchor the rendered page owns, with toc's _1 dedup suffixes."""
    slugs: set[str] = set()
    seen: dict[str, int] = {}
    # detect headings on code-stripped text (a "#" inside a fence is not a heading),
    # but slug from the ORIGINAL line - inline code in a heading keeps its content
    for raw, safe in zip(md.splitlines(), _strip_code(md).splitlines()):
        if not re.match(r"^#{1,6}\s+\S", safe):
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*(?:\{[^}]*\})?\s*$", raw)
        if not m:
            continue
        title = re.sub(r"`([^`]*)`", r"\1", m.group(1))
        title = re.sub(r"\[((?:[^\]]|\](?!\())*)\]\([^)]+\)", r"\1", title)  # link text only
        base = _toc_slug(title)
        n = seen.get(base, 0)
        seen[base] = n + 1
        slugs.add(base if n == 0 else f"{base}_{n}")
    return slugs


def anchor_violations(md: str, path: str = "<page>") -> list[Violation]:
    """ERROR on authored fragments that no heading slug matches. Cross-page fragments
    are checked when the linked file can be read relative to `path`; unreadable or
    non-.md targets are left to the site build."""
    import os
    coded = _COMMENT.sub(_blank_same_len, _strip_code(md))
    own = heading_slugs(md)
    cache: dict[str, set[str] | None] = {}
    out: list[Violation] = []
    for m in _MD_LINK.finditer(coded):
        url = m.group(1)
        if "#" not in url or url.startswith(("http://", "https://", "mailto:")):
            continue
        target, frag = url.split("#", 1)
        if not frag:
            continue
        if target == "":
            slugs = own
        elif target.endswith(".md") and os.path.isfile(os.path.join(os.path.dirname(path), target)):
            if target not in cache:
                try:
                    with open(os.path.join(os.path.dirname(path), target), encoding="utf-8") as fh:
                        cache[target] = heading_slugs(fh.read())
                except OSError:
                    cache[target] = None
            slugs = cache[target]
        else:
            continue
        if slugs is not None and frag not in slugs:
            line = md[:m.start()].count("\n") + 1
            where = "this page" if target == "" else target
            out.append(Violation(SEVERITY_ERROR, line, "dead-anchor",
                f"link fragment '#{frag}' matches no heading on {where} - the heading "
                f"may have been retitled (slugs there: check `## ...` lines); fix the "
                f"fragment or the heading"))
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

    # --- chip-marker collision: "(((" renders a chip whose label swallows the adjacent paren ---
    for i, l in enumerate(safe.splitlines()):
        if "(((" in l:
            out.append(Violation(SEVERITY_ERROR, i + 1, "chip-paren-collision",
                                 "'(((' in source: a parenthesis abutting a ((chip)) marker is swallowed "
                                 "into the rendered chip label - restructure so '(' never touches '((' "
                                 "(Mark's Call Flow split, 2026-08-24: '(((Run Instance))' rendered a chip "
                                 "reading '(Run Instance')"))

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

    # --- split list (error): a bullet glued to the block above it is not a list item ---
    # python-markdown needs a blank line before a list that follows a paragraph or an image.
    # Without one, the bullet is swallowed into that block and ships as a literal "- " line.
    prev = ""
    # comments are author notes markdown never renders - a bullet inside one is not a list item
    listsafe = _COMMENT.sub(_blank_same_len, safe)
    for i, l in enumerate(listsafe.splitlines()):
        glued = (prev.strip() and not _BULLET.match(prev) and not prev[:1].isspace()
                 and (_IMAGE.match(prev.strip()) or prev.rstrip().endswith(":")))
        if _BULLET.match(l) and glued:
            out.append(Violation(SEVERITY_ERROR, i + 1, "split-list",
                "this bullet is glued to the line above it, so markdown folds it into that block "
                "and it ships as a literal '- ' instead of a list item. Put a blank line before the "
                "list (or indent the interrupting image two spaces to keep it inside the bullet)"))
        prev = l

    # --- flow-vs-instance (warn): a call/trigger/event starts an INSTANCE, not "the flow" ---
    for i, l in enumerate(safe.splitlines()):
        m = _FLOW_VS_INSTANCE.search(l)
        if m:
            out.append(Violation(SEVERITY_WARN, i + 1, "flow-vs-instance",
                f"'{m.group(0).strip()}': an API call, trigger, event, or schedule starts an "
                f"INSTANCE (a run) of the flow - the flow itself is started only in the "
                f"Start-flow/LIVE sense. Write 'starts an instance' / 'starts a run'"))

    # --- flow-vs-instance, verb form (warn): a RUN reaches/finishes/terminates, not the flow ---
    for i, l in enumerate(safe.splitlines()):
        m = _FLOW_RUNTIME_VERB.search(l)
        if m:
            out.append(Violation(SEVERITY_WARN, i + 1, "flow-vs-instance",
                f"'{m.group(0).strip()}': reaching a block, finishing, and terminating are things one RUN "
                f"(instance) does - the flow is the definition. Make the run the subject"))

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
            # author notes are not reader-facing prose
            hit = _PROSE_UI.search(_COMMENT.sub(_blank_same_len, _strip_code(sec.body)))
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

    # --- dead anchors: authored #fragments must match real heading slugs ---
    out.extend(anchor_violations(md, path))

    out.sort(key=lambda v: (v.line, 0 if v.severity == SEVERITY_ERROR else 1))
    return out


def errors(violations: list[Violation]) -> list[Violation]:
    return [v for v in violations if v.severity == SEVERITY_ERROR]
