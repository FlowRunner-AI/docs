"""Tests for the doclint rules. These pin the behaviour of the gate itself, so the
gate cannot silently regress."""
from tools.doclint.lint import lint_text, split_sections, errors

PAGE = "# Title\n\nA plain lede sentence.\n\n"


def _rules(md):
    return {(v.rule, v.severity) for v in lint_text(md)}


# ---------- the hard gate: screenshot coverage ----------

def test_section_with_control_and_no_image_is_an_error():
    md = PAGE + "## Doing the thing\n\nYou open the ((Wand)) on a field.\n"
    errs = [v for v in errors(lint_text(md)) if v.rule == "screenshot-coverage"]
    assert len(errs) == 1
    assert "Wand" in errs[0].message


def test_section_with_control_and_an_image_passes():
    md = (PAGE + "## Doing the thing\n\nYou open the ((Wand)) on a field.\n\n"
          "![the wand on a field](../images/x.png)\n")
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage"]


def test_purely_conceptual_section_needs_no_screenshot():
    md = PAGE + "## A concept\n\nThis section only explains an idea, no UI.\n"
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage"]


def test_control_inside_code_does_not_count():
    md = PAGE + "## Syntax\n\nA literal marker in code:\n\n```\n((not a control))\n```\n"
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage"]


def test_inline_code_control_does_not_count():
    md = PAGE + "## Syntax\n\nWrite it as `((literal))` in a snippet.\n"
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage"]


def test_screenshot_needed_marker_is_still_an_error_but_flagged():
    md = (PAGE + "## Doing the thing\n\nUse the ((Panel)).\n\n"
          "<!-- SCREENSHOT NEEDED: the panel -->\n")
    errs = [v for v in errors(lint_text(md)) if v.rule == "screenshot-coverage"]
    assert len(errs) == 1
    assert "SCREENSHOT-NEEDED" in errs[0].message


def test_intro_section_is_covered_too():
    md = "# Title\n\nYou start at the ((Dashboard)).\n\n## More\n\nplain.\n"
    errs = [v for v in errors(lint_text(md)) if v.rule == "screenshot-coverage"]
    assert any("(intro)" in v.message for v in errs)


def test_unmarked_prose_ui_reference_warns():
    md = PAGE + "## Building one\n\nThe wand icon opens the editor.\n"
    warns = [v for v in lint_text(md) if v.rule == "screenshot-coverage-prose"]
    assert len(warns) == 1


def test_prose_ui_warn_suppressed_when_image_present():
    md = (PAGE + "## Building one\n\nThe wand icon opens the editor.\n\n"
          "![the wand](../x.png)\n")
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage-prose"]


def test_plain_concept_does_not_trip_prose_ui():
    md = PAGE + "## Idea\n\nA value the flow works out at run time from its data.\n"
    assert not [v for v in lint_text(md) if v.rule == "screenshot-coverage-prose"]


# ---------- structure ----------

def test_missing_h1_errors():
    assert ("structure", "error") in _rules("no title here\n\nbody\n")


def test_two_h1_errors():
    assert ("structure", "error") in _rules("# One\n\nlede\n\n# Two\n\nx\n")


def test_h4_errors():
    md = PAGE + "## Sec\n\ntext\n\n#### Too deep\n\nx\n"
    assert ("structure", "error") in _rules(md)


def test_missing_lede_errors():
    assert ("lede", "error") in _rules("# Title\n\n## Straight to a section\n\nx\n")


def test_lede_present_passes():
    assert ("lede", "error") not in _rules(PAGE + "## Sec\n\nplain concept.\n")


# ---------- style ----------

def test_em_dash_errors():
    assert ("em-dash", "error") in _rules(PAGE + "## Sec\n\nthis — that.\n")


def test_banned_word_warns():
    rules = _rules(PAGE + "## Sec\n\nThis is a powerful idea.\n")
    assert ("banned-word", "warn") in rules


def test_banned_word_in_code_ignored():
    assert ("banned-word", "warn") not in _rules(PAGE + "## Sec\n\n`powerful` flag.\n")


# ---------- trigger-start framing (a flow can start with anything) ----------

def test_trigger_start_framing_warns():
    md = PAGE + "## Sec\n\nA flow starts with a trigger that fires.\n"
    assert ("trigger-start", "warn") in _rules(md)


def test_trigger_start_payload_phrasing_warns():
    md = PAGE + "## Sec\n\nInitial Data is the payload from its trigger.\n"
    assert ("trigger-start", "warn") in _rules(md)


def test_correct_conditional_trigger_mention_does_not_warn():
    md = PAGE + "## Sec\n\nWhen a trigger starts the flow, its data is on the trigger block.\n"
    assert ("trigger-start", "warn") not in _rules(md)


def test_initial_trigger_term_does_not_warn():
    md = PAGE + "## Sec\n\nInitial Trigger reads it from the event that started the flow.\n"
    assert ("trigger-start", "warn") not in _rules(md)


def test_trigger_start_skipped_on_triggers_page():
    md = PAGE + "## Sec\n\nA flow starts with a trigger.\n"
    got = [v for v in lint_text(md, path="content/learn/concepts/triggers.md")
           if v.rule == "trigger-start"]
    assert got == []


def test_trigger_start_escape_suppresses():
    md = (PAGE + "## Sec\n\nA flow starts with a trigger.\n\n"
          "<!-- doclint: allow: trigger-start -->\n")
    assert ("trigger-start", "warn") not in _rules(md)


def test_trigger_start_in_code_ignored():
    md = PAGE + "## Sec\n\nLiteral: `a flow starts with a trigger`.\n"
    assert ("trigger-start", "warn") not in _rules(md)


# ---------- section-shot (a section documenting a block must SHOW it) ----------

def test_section_documenting_block_without_shot_warns():
    md = PAGE + "## Writing a value\n\nYou save it with [Put](../x.md){.fr-block}.\n"
    assert ("section-shot", "warn") in _rules(md)


def test_section_with_block_and_image_passes():
    md = (PAGE + "## Writing a value\n\nYou save it with [Put](../x.md){.fr-block}.\n\n"
          "![the Put block](../x.png)\n")
    assert ("section-shot", "warn") not in _rules(md)


def test_section_shot_noshot_marker_opts_out():
    md = (PAGE + "## Mentions a block\n\nUnlike [Put](../x.md){.fr-block}, this resets.\n\n"
          "<!-- doclint: no-shot: conceptual contrast, not a walkthrough -->\n")
    assert ("section-shot", "warn") not in _rules(md)


def test_related_section_not_flagged_for_shot():
    md = PAGE + "## Related\n\n- [Put](../x.md){.fr-block} - writes a value\n"
    assert ("section-shot", "warn") not in _rules(md)


def test_section_shot_not_double_reported_with_control():
    md = PAGE + "## Doing it\n\nOpen the ((Panel)) and use [Put](../x.md){.fr-block}.\n"
    rules = {v.rule for v in lint_text(md)}
    assert "screenshot-coverage" in rules
    assert "section-shot" not in rules


# ---------- section splitting ----------

# ---------- block-link coverage ----------

NAMES = ["External Callback", "Set Variables", "Wait"]


def _bl(md, names=NAMES):
    return [v for v in lint_text(md, block_names=names) if v.rule == "block-link"]


def test_linked_first_mention_passes():
    md = PAGE + "## Sec\n\nUse the [External Callback](../x.md) here.\n"
    assert _bl(md) == []


def test_unlinked_distinctive_name_errors():
    md = PAGE + "## Sec\n\nUse the External Callback here.\n"
    v = _bl(md)
    assert len(v) == 1 and v[0].severity == "error"


def test_unlinked_ambiguous_name_warns():
    md = PAGE + "## Sec\n\nA Wait can pause a flow.\n"
    v = _bl(md, names=["Wait"])
    assert len(v) == 1 and v[0].severity == "warn"


def test_block_name_in_code_ignored():
    md = PAGE + "## Sec\n\nThe `External Callback` token is literal.\n"
    assert _bl(md) == []


def test_block_name_in_heading_ignored():
    md = PAGE + "## External Callback\n\nPlain prose with no block mention.\n"
    assert _bl(md) == []


def test_block_name_in_image_alt_ignored():
    md = PAGE + "## Sec\n\n![shows the External Callback panel](../x.png)\n"
    assert _bl(md) == []


def test_second_unlinked_mention_is_fine_when_first_is_linked():
    md = PAGE + "## Sec\n\nFirst [External Callback](../x.md). Later External Callback again.\n"
    assert _bl(md) == []


def test_first_mention_bare_errors_even_if_linked_later():
    md = (PAGE + "## Sec\n\nA bare External Callback first.\n\n"
          "## Two\n\nNow [External Callback](../x.md).\n")
    v = _bl(md)
    assert len(v) == 1 and v[0].severity == "error"


def test_escape_hatch_suppresses_block_link():
    md = (PAGE + "## Sec\n\nUse the External Callback here.\n\n"
          "<!-- doclint: allow-unlinked: External Callback -->\n")
    assert _bl(md) == []


def test_plural_or_word_boundary_not_falsely_matched():
    md = PAGE + "## Sec\n\nThe waiter waited; nothing to see.\n"
    assert _bl(md, names=["Wait"]) == []


def test_block_name_in_html_comment_ignored():
    md = PAGE + "## Sec\n\n<!-- note: the External Callback wiring is unverified -->\n\nPlain prose.\n"
    assert _bl(md) == []


# ---------- section splitting ----------

def test_split_sections_counts_intro_plus_headings():
    secs = split_sections(PAGE + "## A\n\nx\n\n## B\n\ny\n")
    assert [s.title for s in secs] == ["(intro)", "A", "B"]


def test_heading_in_code_is_not_a_section():
    secs = split_sections(PAGE + "## Real\n\n```\n## fake\n```\n")
    assert [s.title for s in secs] == ["(intro)", "Real"]


# --- dead-anchor -------------------------------------------------------------------

def test_dead_anchor_same_page_and_inline_code_headings():
    from tools.doclint.lint import heading_slugs, anchor_violations
    md = ("# T\n\nlede\n\n## Endpoint (`GET` or `POST`)\n\n"
          "[bad](#endpoint) [ok](#endpoint-get-or-post)\n")
    assert heading_slugs(md) == {"t", "endpoint-get-or-post"}
    vs = anchor_violations(md, "x.md")
    assert [v.rule for v in vs] == ["dead-anchor"] and "#endpoint'" in vs[0].message


def test_dead_anchor_dash_run_collapses_like_toc():
    # "Dashboard - the flow" renders as one dash run; authored "---" is dead
    from tools.doclint.lint import anchor_violations
    md = "# T\n\nlede\n\n## Dashboard - the flow\n\n[a](#dashboard---the-flow)\n"
    assert len(anchor_violations(md, "x.md")) == 1
    md_ok = md.replace("#dashboard---the-flow", "#dashboard-the-flow")
    assert anchor_violations(md_ok, "x.md") == []


def test_dead_anchor_cross_page(tmp_path):
    from tools.doclint.lint import anchor_violations
    (tmp_path / "other.md").write_text("# O\n\n## Real Section\n", encoding="utf-8")
    md = "# T\n\nlede\n\n[ok](other.md#real-section) [bad](other.md#gone) [ext](https://x.com#frag)\n"
    vs = anchor_violations(md, str(tmp_path / "page.md"))
    assert len(vs) == 1 and "other.md" in vs[0].message and "#gone" in vs[0].message


# --- flow-vs-instance, verb form ---------------------------------------------------

def test_flow_runtime_verb_flags_completed_progress_only():
    from tools.doclint.lint import lint_text
    bad = "# T\n\nlede\n\nA flow that never reaches a Return Result gets the envelope.\n"
    hits = [v for v in lint_text(bad, "x.md", block_names=()) if v.rule == "flow-vs-instance"]
    assert len(hits) == 1
    # the idiomatic present-tense design description stays unflagged (owner decision, not a defect)
    ok = "# T\n\nlede\n\nWhen the flow reaches this block, it waits.\n"
    assert not [v for v in lint_text(ok, "x.md", block_names=()) if v.rule == "flow-vs-instance"]
    # a possessive already makes the run the subject
    poss = "# T\n\nlede\n\nIt does not mean the called flow's run has finished.\n"
    assert not [v for v in lint_text(poss, "x.md", block_names=()) if v.rule == "flow-vs-instance"]


def test_expression_tokens_are_not_block_mentions():
    from tools.doclint.lint import block_link_violations
    authored = "# T\n\nBuild it as {{HTTP Request Result->status}} in the editor.\n"
    assert block_link_violations(authored, ["HTTP Request"]) == []
    rendered = '# T\n\nBuilt as <span class="fr-expr">HTTP Request Result → status</span>.\n'
    assert block_link_violations(rendered, ["HTTP Request"]) == []
    # a real prose mention still errors
    prose = "# T\n\nAdd an HTTP Request to the flow.\n"
    assert len(block_link_violations(prose, ["HTTP Request"])) == 1


# --- split-list -------------------------------------------------------------------

def test_split_list_catches_image_and_leadin_glue_but_not_prose():
    from tools.doclint.lint import lint_text
    def hits(md):
        return [v for v in lint_text(md, "x.md", block_names=()) if v.rule == "split-list"]
    # round-22 defect: an image at column 0 ends the list, the next bullet is swallowed
    assert len(hits("# T\n\nlede\n\n- one\n\n![a](x.png)\n- two\n")) == 1
    # round-19 defect: a lead-in ending in ':' with no blank line before the bullets
    assert len(hits("# T\n\nlede\n\nThese controls decide:\n- one\n- two\n")) == 1
    # a wrapped prose clause that happens to start with a dash is not a list
    assert hits("# T\n\nlede\n\nRandom returns a number between 0 and 1\n- a seed for sampling.\n") == []
    # a correctly separated list is fine
    assert hits("# T\n\nlede\n\nThese controls decide:\n\n- one\n- two\n") == []
