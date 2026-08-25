"""Strip HTML comments from page markdown before rendering.

Why: the per-page verification / product-exploration logs live in HTML comments
(mandated by tools/doclint/DEFINITION_OF_DONE.md). Markdown passes raw HTML
through, so without this hook every one of those comments - including security
notes and live ids - ships verbatim into the published page's view-source
(caught by the concept-page-review gate, 2026-08-24). doclint runs on the
SOURCE files and still sees the comments.

Fence-aware: comments inside ``` / ~~~ fenced code blocks are left alone so a
page can display a literal comment as code.
"""
import re

_FENCE = re.compile(r"^(\s*)(```|~~~)")
_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def _strip_outside_fences(md: str) -> str:
    out, buf, in_fence, marker = [], [], False, ""
    for line in md.split("\n"):
        m = _FENCE.match(line)
        if m:
            if not in_fence:
                out.append(_COMMENT.sub("", "\n".join(buf)))
                buf = []
                in_fence, marker = True, m.group(2)
                out.append(line)
            elif line.lstrip().startswith(marker):
                in_fence = False
                out.append(line)
            else:
                out.append(line)
        elif in_fence:
            out.append(line)
        else:
            buf.append(line)
    if buf:
        out.append(_COMMENT.sub("", "\n".join(buf)))
    return "\n".join(out)


def on_page_markdown(markdown, page, config, files):
    return _strip_outside_fences(markdown)
