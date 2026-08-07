.PHONY: refgen-install refgen refgen-test refgen-check doclint doclint-test

refgen-install:
	python3 -m pip install -r tools/refgen/requirements.txt

refgen:
	python3 -m tools.refgen.generate

refgen-test:
	python3 -m pytest tools/refgen/tests -v

# Anti-drift guard: regenerate, then fail if anything changed (artifact hand-edited
# or stale). Intended for CI and pre-commit verification.
refgen-check: refgen
	git diff --exit-code content/reference mkdocs.yml

# Definition-of-Done gate: fail the build if any narrative page points the reader at
# an on-screen control with no screenshot (and check structure/style). The step that
# turns VOICE.md from a "should" into a "must". Pass files/dirs via ARGS=..., e.g.
# `make doclint ARGS="content/learn/concepts/triggers.md"`.
doclint:
	python3 -m tools.doclint $(ARGS)

doclint-test:
	python3 -m pytest tools/doclint/tests -v
