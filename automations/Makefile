.PHONY: refgen-install refgen refgen-test refgen-check

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
