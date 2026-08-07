"""doclint - enforce the documentation Definition of Done as build-breaking gates.

The standard lives in block-knowledge/VOICE.md. The problem this package solves is
that a rule written down is not a rule enforced: pages kept shipping with prose that
points the reader at on-screen controls and NO screenshot, because nothing between
"drafted" and "done" could fail. doclint is that failing step.

The hard gate is screenshot coverage, stated verbatim in VOICE.md:

    "A screenshot goes WHEREVER the prose points the reader at something on screen -
     one per such place, applied per section, NEVER capped at one per page... The
     ONLY thing that gets no screenshot is purely conceptual prose with no on-screen
     referent."

The authored, machine-readable signal for "the prose points at an on-screen thing"
is the ((Component)) marker (the same one render.py turns into a .fr-control chip).
A section that contains one or more such markers and no image is an uncovered
section - a build break.
"""
