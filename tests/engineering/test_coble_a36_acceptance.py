"""Acceptance gate for research#679 (A36), the semifan of a recognizable divisor.

The item, as the issue states it: "Describe the semifan $\\semifan{F}_R$ for a recognizable
divisor $R$ ... and it is open even for the rational-curve divisor $R_\\rcop$", accepted "when
the question is settled in `writing/` with a proof, a disproof, or a computation record, and
every page that cites the open form is updated."

What is settled, and lives on
writing/coble/compactifications/toroidal-and-semitoroidal.md:

    thm:semifan-stratum            the stratum description, for every recognizable divisor
    thm:semifan-recognizable-divisor  the closed form, conditional on (W)
    prop:semifan-coarsening-extension (W) <=> extension of the universal family
    prop:semifan-coarsening-fails  (W) fails for ABE22's elliptic divisor
    rmk:recognizable-gap           that divisor is not known recognizable, so (W) is open
    thm:cone-inventory-printed     the cones at the F_2 cusp, from AET23 p. 22
    rmk:missing-stable-limit       the contract of the operation the split needs

What is not settled is one computation: the KSBA stable limit of $(X,\\eps R_\\rcop)$ over a
cone, hence the split $I\\sqcup J$.  The row for it below is marked xfail(strict=True): it is
red today, and it turns red-for-the-opposite-reason the day a record lands without the page
being updated, which is the point of a strict marker here.

Run it with

    python3 -m pytest tests/engineering/test_coble_a36_acceptance.py -q -o addopts="" \\
        --confcutdir=tests/engineering

The two overrides drop the project's addopts (pytest-timeout, pytest-reportlog) and keep
tests/conftest.py, which imports dzack_research, out of a test that needs neither.
"""

import pathlib
import re
import subprocess
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]
PAGE = REPO / "writing/coble/compactifications/toroidal-and-semitoroidal.md"
REGISTER = REPO / "writing/open-questions.md"
DISSERTATION = REPO / "writing/dissertation/sections/2-part-moduli/4-chapter-cpt/300-semitoroidal.md"
REPORTS = REPO / "computations/reports"


def page_text():
    return PAGE.read_text(encoding="utf-8")


def writing_texts():
    """The authored pages, once each: `.book/` holds symlinks to them, not second copies."""
    return {
        path: path.read_text(encoding="utf-8", errors="replace")
        for path in (REPO / "writing").rglob("*.md")
        if ".book" not in path.parts and not path.is_symlink()
    }


def test_the_old_open_form_is_gone_from_the_whole_book():
    """Acceptance item 2: no page still carries the form the issue quotes."""
    stale = ("widely open", "coarsest subdivision", "characterized only")
    offenders = [
        "%s: %s" % (path.relative_to(REPO), phrase)
        for path, text in writing_texts().items()
        for phrase in stale
        if phrase in text
    ]
    assert offenders == []


def test_the_question_is_cited_only_by_the_page_and_the_register():
    citing = sorted(
        str(path.relative_to(REPO))
        for path, text in writing_texts().items()
        if "@qst:recognizable-semifan" in text
    )
    assert citing == [
        "writing/coble/compactifications/toroidal-and-semitoroidal.md",
        "writing/open-questions.md",
    ]


def test_the_general_theorem_is_on_the_page():
    text = page_text()
    for label in ("#thm:semifan-stratum", "#thm:semifan-recognizable-divisor",
                  "#prop:semifan-coarsening-extension", "#prop:semifan-coarsening-fails",
                  "#thm:cone-inventory-printed", "#rmk:missing-stable-limit"):
        assert label in text, label


def test_the_withdrawn_counterexample_is_not_back():
    """The referee's finding: the identification from R_rc to ABE22's divisor does not hold."""
    text = page_text()
    assert "#thm:recognizable-fails-W" not in text
    gap = text[text.index("#rmk:recognizable-gap"):]
    gap = gap[: gap.index("\n:::")] if "\n:::" in gap else gap
    assert "only up to proportionality" in gap
    assert "Whether a **recognizable** divisor can fail (W) is open" in gap
    assert "not known to be recognizable" in REGISTER.read_text(encoding="utf-8")
    dissertation = DISSERTATION.read_text(encoding="utf-8")
    assert "recognizable divisor failing the coarsening hypothesis" in dissertation


def test_the_proportionality_probe_reproduces_its_record():
    """The smallest deciding probe: exact arithmetic in the (s, f) lattice, re-run here."""
    script = REPORTS / "coble_679-proportionality.py"
    record = REPORTS / "coble_679-proportionality-run.txt"
    assert script.exists() and record.exists()
    produced = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=True
    ).stdout
    assert produced == record.read_text(encoding="utf-8"), "the transcript no longer matches the script"
    # the decision the probe delivers, restated so a change of the script cannot slip past
    page = page_text()
    assert "24s+48f" in page and "not proportional" in page, "the page no longer carries the probe's numbers"
    assert "which is the polarization $L$ itself" in page, "the page no longer records the second reading"
    assert "which is the polarization L" in produced
    assert "the degrees agree at m = 2" in produced
    assert "there the classes are proportional: False" in produced
    assert "that is m = (d+1)/24 = 1/12" in produced


def test_the_locus_probe_reproduces_its_record():
    """The second probe: in which family ABE22's divisor exists, and that it is polarizing there."""
    script = REPORTS / "coble_679-locus-probe.py"
    record = REPORTS / "coble_679-locus-probe-run.txt"
    assert script.exists() and record.exists()
    produced = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=True
    ).stdout
    assert produced == record.read_text(encoding="utf-8"), "the transcript no longer matches the script"
    assert "proper locus F in F_2: rank 3 > 1" in produced
    assert "D.s = 22 > 0" in produced
    page = page_text()
    assert "Picard group contains $U\\oplus\\langle-2\\rangle$, of rank $3$" in page
    assert "coble_679-locus-probe-run.txt" in page


def test_the_recognizability_inventory_reproduces_and_names_the_gap():
    """Which deposits assert recognizability, and for which divisor: the input of question 1."""
    script = REPORTS / "coble_679-recognizability-inventory.py"
    record = REPORTS / "coble_679-recognizability-inventory-run.txt"
    assert script.exists() and record.exists()
    produced = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=True
    ).stdout
    assert produced == record.read_text(encoding="utf-8"), "the transcript no longer matches the script"
    assert "lines speaking of recognizability: 9" in produced
    assert "[flex divisor]" in produced
    assert "whose paper does not use the word" in produced
    assert "coble_679-recognizability-inventory-run.txt" in page_text()


def test_the_four_records_of_the_unit_are_committed():
    for name in (
        "coble_679-rcop-split.py",
        "coble_679-rcop-split-run.txt",
        "coble_679-rcop-split-run-1800.txt",
        "coble_679-rcop-chamber.py",
        "coble_679-rcop-chamber-run.txt",
        "coble_679-rcop-chamber-controlling-vector-run.txt",
        "coble_679-elliptic-cone-inventory.py",
        "coble_679-elliptic-cone-inventory-run.txt",
        "coble_679-proportionality.py",
        "coble_679-proportionality-run.txt",
        "coble_679-locus-probe.py",
        "coble_679-locus-probe-run.txt",
        "coble_679-recognizability-inventory.py",
        "coble_679-recognizability-inventory-run.txt",
    ):
        assert (REPORTS / name).exists(), name


def test_the_two_blockers_of_the_open_rows_are_what_the_records_say():
    """The controls on the two red rows: if either blocker lifts, this fires and the row must be re-read.

    A red row is only honest while the reason it is red is true and machine-checked.  The two
    reasons are (i) the library has no operation for the stable limit of a pair over a cone,
    and (ii) the Vinberg walk at the F_2 cusp does not finish.  (i) is recorded by the two
    AttributeErrors of coble_679-rcop-split-run.txt; (ii) by the timeout lines of the three
    bounded attempts.  Both are asserted here, together with the bound each record carries, so
    a re-run that changes either number makes this test fail before the page goes stale.
    """
    split_record = (REPORTS / "coble_679-rcop-split-run.txt").read_text(encoding="utf-8")
    assert "stand_in.stable_pairs() -> AttributeError" in split_record
    assert "stand_in.wall_roots()[0].stable_pairs() -> AttributeError" in split_record
    assert "the missing operation is the KSBA stable limit of the pair over a cone" in split_record

    bounds = {
        "coble_679-rcop-split-run.txt": "the Vinberg walk on N did not finish in 900 s",
        "coble_679-rcop-split-run-1800.txt": "the Vinberg walk on N did not finish in 1800 s",
        "coble_679-rcop-chamber-run.txt": "the Vinberg walk on N did not finish in 2400 s",
        "coble_679-rcop-chamber-controlling-vector-run.txt": "the walk with the controlling vector did not finish in 1500 s",
    }
    for name, line in bounds.items():
        assert line in (REPORTS / name).read_text(encoding="utf-8"), name
    page = page_text()
    for bound in ("900", "1800", "2400", "1500"):
        assert bound in page, "the page no longer quotes the %s s bound" % bound


@pytest.mark.xfail(
    strict=True,
    reason="no record decides whether a recognizable divisor can fail (W): the only candidate, "
    "s + m sum f_i, is not known to be recognizable for the elliptic locus (rmk:recognizable-gap)",
)
def test_a_recognizable_divisor_failing_the_coarsening_is_exhibited():
    """Question 1 of qst:recognizable-semifan: a recognizable divisor whose semifan refines."""
    record = REPORTS / "coble_679-recognizable-W-fails-run.txt"
    assert record.exists(), "no record: no recognizable divisor is known to fail (W)"
    text = record.read_text(encoding="utf-8")
    assert "recognizable" in text and "coarsen" in text


@pytest.mark.xfail(
    strict=True,
    reason="no record decides the split: the KSBA stable limit of (X, eps R_rc) over a cone is "
    "not an operation of sage-extensions (rmk:missing-stable-limit), and the walk to the "
    "chamber at the F_2 cusp does not finish in 2400 s",
)
def test_the_split_for_the_rational_curve_divisor_is_decided():
    """Acceptance item 1's remaining clause: the split I | J and the cones for R_rc on F_2d."""
    record = REPORTS / "coble_679-rcop-split-decided-run.txt"
    assert record.exists(), "no decision record: the split is not computed"
    text = record.read_text(encoding="utf-8")
    assert re.search(r"^I = ", text, re.M), "the record does not state the relevant set I"
    assert re.search(r"^J = ", text, re.M), "the record does not state the irrelevant set J"
