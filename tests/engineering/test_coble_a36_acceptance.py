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
    rmk:recognizable-gap           why that alone does not settle it, and the statement that does
    thm:cone-inventory-printed     the cones at the F_2 cusp, from AET23 p. 22
    rmk:missing-stable-limit       the contract of the operation a general cusp needs
    lem:rcop-refinement-criterion  proved: (W) fails for R_rcop at the F_2 cusp

What is not settled is the split $I\\sqcup J$ at the $0$-cusps of $F_{2d}$ for $d\\ge2$: AE23's
Introduction, printed p. 3, states that there is no explicit description of the rational-curve
semifan and calls one an interesting open question; a computation would need the KSBA stable
limit of $(X,\\eps R_\\rcop)$ over a cone, which is not an operation of `sage-extensions`
(rmk:missing-stable-limit), and the Coxeter fan at those cusps is not printed.
The row for it below is marked xfail(strict=True): it is red today, and it turns
red-for-the-opposite-reason the day a record lands without the page being updated.

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
    """The withdrawn theorem stays withdrawn; the gap is closed by a named source, not by it.

    The referee's finding stands: proportionality of divisor classes does not identify the two
    compactifications.  What replaces the withdrawn argument is AE23's own identification of
    the restriction of the semifan with ABE22's fan, through the stratum function, so the page
    must name that source and must not resurrect the withdrawn identifier.
    """
    text = page_text()
    assert "#thm:recognizable-fails-W" not in text
    gap = text[text.index("#rmk:recognizable-gap"):]
    gap = gap[: gap.index("\n:::")] if "\n:::" in gap else gap
    assert "only up to proportionality" in gap
    assert "does not by itself exhibit a recognizable divisor" in gap
    assert "AE23, Thm. 10.16, printed p. 38" in gap
    register = REGISTER.read_text(encoding="utf-8")
    assert "answered affirmatively by @lem:rcop-refinement-criterion" in register
    dissertation = DISSERTATION.read_text(encoding="utf-8")
    assert "That a recognizable divisor does fail it is @lem:rcop-refinement-criterion" in dissertation


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


def test_the_pages_that_discuss_the_semifan_state_the_hypothesis_as_one():
    """Item 2's substance, not only its wording: nothing implies coarsening is automatic.

    The research statement conjectures that the Coble semifan coarsens the Coxeter fan.  That is
    hypothesis (W) of @thm:semifan-recognizable-divisor for the Coble divisor, and the page and
    the statement must both say it is a hypothesis: the general theory does not supply it.
    """
    statement = (REPO / "writing/research-statement/ResearchStatement.md").read_text(encoding="utf-8")
    assert "Coarsening is a named hypothesis in that theory, not a consequence of it" in statement
    assert "thm:semifan-recognizable-divisor" in statement
    assert "a genuine statement about the Coble divisor and not a special case" in statement
    page = page_text()
    assert "#thm:semifan-stratum" in page and "hypothesis" in page


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
    assert "has a deposited witness; AE23 itself is not deposited" in produced
    page = page_text()
    assert "was proven to be recognizable in" in page and "@AE23a]" in page


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
        "coble_679-chamber-bound-probe.py",
        "coble_679-chamber-bound-probe-run.txt",
        "coble_679-recognizability-inventory.py",
        "coble_679-recognizability-inventory-run.txt",
    ):
        assert (REPORTS / name).exists(), name


def test_the_lemma_is_proved_from_the_published_sources():
    """lem:rcop-refinement-criterion is decided, and the proof names its sources by page.

    AE23 Prop. 10.10 (printed p. 36) identifies the rational-curve divisor on the unigonal
    locus, AE23 Thm. 10.16 (printed p. 38) identifies the restriction of its semifan to the
    unigonal hyperplane with the ABE22 fan and makes each of its maximal cones a cone of the
    semifan, and ABE22 Sec. 4C (printed p. 14) with its Fig. 1 (printed p. 12) supplies the
    two cutting vectors.  The proof must keep the page citations and the mirror-trace step.
    """
    page = page_text()
    start = page.index("#lem:rcop-refinement-criterion")
    block = page[start:page.index("#qst:recognizable-semifan")]
    assert "is not a union of cones of" in block
    assert "AE23, Prop. 10.10, printed p. 36" in block
    assert "AE23, Thm. 10.16, printed p. 38" in block
    assert "ABE22, §4C, printed p. 14" in block
    assert "ABE22, Fig. 1, printed p. 12" in block
    assert "AET23, Def. 4.1, printed p. 21" in block
    assert "AET23, §5C, printed p. 29; Fig. 1, printed p. 22" in block
    assert "mirror of a root other than $t^\\perp$" in block
    assert "@prop:semifan-coarsening-extension" in block
    assert "::: {.proof}" in block


def test_the_two_questions_are_reduced_to_one_inventory():
    """The inventory, and what the lemma leaves of it: the cusps of F_2d for d >= 2.

    The deposits carry a recognizability proof for two classes of divisor -- the ramification
    divisor in its fixed-locus and Enriques forms, and R_rc.  (W) is computed for the first
    class in three families and, for the second, at the unique F_2 cusp by
    lem:rcop-refinement-criterion; what remains is the second class at d >= 2.  The page must
    keep the inventory and the register row must keep the remaining question.
    """
    page = page_text()
    block = page[page.index("#rmk:two-questions-are-one"):]
    block = block[: block.index("\n:::")] if "\n:::" in block else block
    assert "only two classes of polarizing divisor carry a recognizability proof" in block
    assert "the fifty two-elementary lattices with $g\\ge2$" in block
    assert "hypothesis (W) fails for $R_{\\rcop}$ at the unique $0$-cusp of $F_2$" in block
    assert "for $d\\ge2$" in block
    register = REGISTER.read_text(encoding="utf-8")
    row = [line for line in register.splitlines() if "qst:recognizable-semifan" in line][0]
    assert "whether a *recognizable* divisor can fail" in row
    assert "at the $0$-cusps of $F_{2d}$ for $d\\ge2$" in row


def test_no_bound_on_the_search_delivers_the_chamber():
    """The chamber blocker, decided at the parameter: max_roots does not bring rank 19 into range.

    The probe bounds Vinberg's search at 1, 4, 12 and 24 roots and runs the rank-18 lattice as a
    control.  Rank 19 times out at every bound; the control returns all eighteen roots in 63-66
    seconds.  So the cost is the rank, not the number of roots searched, and no parameter of the
    call can supply the chamber the stable-limit operation needs.
    """
    record = (REPORTS / "coble_679-chamber-bound-probe-run.txt").read_text(encoding="utf-8")
    assert "max_roots= 1 -> timeout at 120 s" in record
    assert "max_roots=24 -> timeout at 120 s" in record
    assert "rank 18 (control)  max_roots= 1 -> 18 roots" in record
    assert "bounding the search cannot deliver the chamber" in record or "a bound on the" in record
    script = REPORTS / "coble_679-chamber-bound-probe.py"
    assert script.exists()
    page = page_text()
    assert "coble_679-chamber-bound-probe-run.txt" in page


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


def test_a_recognizable_divisor_failing_the_coarsening_is_exhibited():
    """Question 1 of qst:recognizable-semifan, decided in prose from the published sources.

    The issue accepts a proof, a disproof or a computation record.  The proof is
    lem:rcop-refinement-criterion: R_rcop is recognizable (AE23 Thm. 10.11, printed p. 36) and
    (W) fails for it at the unique F_2 cusp, so the universal family of stable pairs does not
    extend over the Coxeter toroidal compactification.  No computation record is claimed, and
    the test therefore asserts the proof rather than a transcript.
    """
    page = page_text()
    assert "the rational-curve divisor $R_{\\rcop}$ on $F_2$ is recognizable [@AE23, Thm. 10.11, printed p. 36]" in page
    assert "does not extend over the Coxeter toroidal compactification" in page
    assert "hypothesis (W) fails for $R_{\\rcop}$" in page


def test_the_citations_and_the_open_status_carry_their_printed_pages():
    """The referee's citation repair, and the source's own statement of what remains.

    The Coxeter-fan counts 19/82 and 10/46 are Corollary 4.3 in Section 4A of ABE22, printed
    p. 13, not Section 4C on p. 14; the two squares -8 and -4 are Section 4C, printed p. 14,
    and stay there.  The remaining cusps are not a gap of this repository: AE23, Introduction,
    printed p. 3, states that there is no explicit description of the rational-curve semifan
    and calls one an interesting open question, and the page, the register and the dissertation
    section must carry that sentence with its page.
    """
    page = page_text()
    assert "[@ABE22, Cor. 4.3, §4A, printed p. 13] prints the counts" in page
    assert "[@ABE22, §4C, printed p. 14] prints the counts" not in page
    assert "[@ABE22, §4C, printed p. 14]," in page, "the squares are still cited to Section 4C"
    assert "an interesting open question" in page
    assert "[@AE23, Intro., printed p. 3]" in page
    assert "[@AE22, §3A, printed p. 10]" in page, "the long-root convention is not recorded"
    assert "$h_\\beta=\\sigma_{22}\\cap\\beta_L^\\perp$" in page
    assert "the long root $g$ at $k=2$ is included in this and does not repair (W)" in page
    register = REGISTER.read_text(encoding="utf-8")
    assert "[@AE23, Intro., printed p. 3]" in register
    dissertation = DISSERTATION.read_text(encoding="utf-8")
    assert "[@AE23, Intro., printed p. 3]" in dissertation


def test_the_wall_criterion_is_on_the_page():
    """The p_* > 1 item's next step: what (W) forces on an 18-dimensional cone.

    A cone of the Coxeter semifan of dimension 18 is a facet of a chamber, hence lies in the
    mirror of a simple root (AET23, Lemma 4.4, printed p. 22); so an 18-dimensional cone of
    F_rc spanning a hyperplane that is no root mirror refutes (W).  At the cusps with
    d = p^2 the boundary lattice is the F_2 one and the root mirrors are the 24 printed ones.
    """
    page = page_text()
    assert "#lem:wall-criterion" in page
    assert "If $H$ is not the mirror of a vector of $\\bar T$ of square $-2$ or $-4$" in page
    assert "spans one of those $24$ root mirrors" in page


def test_the_p_greater_one_cusp_lattice_record_reproduces_and_the_page_states_it():
    """The p_* > 1 item's first datum: the boundary lattice, for general (p, k).

    AE23 Section 10C prints delta^perp/delta = <-2d/p_*> + H + E8^2 (p. 38).  For
    delta = g + p(e1 + k f1) in L_{2d} with d = p^2 k, the vector is primitive isotropic
    with p_*(delta) = p, and delta^perp/delta is <-2k> + U + E8(-1)^2 = <-2d/p_*^2> + ...
    so the printed formula would give <-2pk>, a lattice of the wrong discriminant.  At
    k = 1 (d = p^2) the lattice is the F_2 cusp lattice; for k >= 2 it is the unigonal
    cusp lattice of F_{2k}.  The record proves the cases and the page's lemma states them.
    """
    script = REPORTS / "coble_679-cusp-lattice.py"
    record = REPORTS / "coble_679-cusp-lattice-run.txt"
    assert script.exists() and record.exists()
    produced = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, check=True).stdout
    assert produced == record.read_text(encoding="utf-8"), "the transcript no longer matches the script"
    assert "d = 4, p = 2, k = 1" in produced
    assert "d = 8, p = 2, k = 2" in produced
    assert "d = 16, p = 2, k = 4" in produced
    assert "d = 18, p = 3, k = 2" in produced
    assert "first summand -2k = -4" in produced
    assert "printed first summand -2d/p_* = -8" in produced
    assert "J^perp/J: rank 17 = 1 + 16, first summand -2k = -2" in produced
    assert "1-cusp lattice E8(-1)^2 + A1(-1)" in produced
    page = page_text()
    assert "#lem:cusp-lattice-p-greater-one" in page
    assert "$\\langle-2k\\rangle\\oplus U\\oplus E_8(-1)^{\\oplus2}$" in page
    assert "boundary lattice of the unigonal cusp of $F_{2k}$" in page
    register = REGISTER.read_text(encoding="utf-8")
    assert "lem:cusp-lattice-p-greater-one" in register


def test_the_k_greater_one_comparison_group_is_not_a_lattice():
    """At k >= 2 the comparison group is not two-reflective, so the semifan is not a fan.

    N_k = <-2k> + U + E8(-1)^2 = U + K with K = <-2k> + E8(-1)^2 of rank 17 and
    discriminant Z/(2k).  For k >= 2, K is not 2-elementary and is not the rank-17 entry
    E8(-1)^2 + A1(-1) of Nikulin's list, so N_k is in neither branch of his Theorem 0.2.4;
    hence W_2(N_k) has infinite index in Orth(N_k), and by AET23 Def. 3.5 the Coxeter
    semifan is not a fan.
    """
    page = page_text()
    assert "#lem:k-not-two-reflective" in page
    assert "[@Nik79b, Thm. 0.2.2, printed p. 1403]" in page
    assert "[@Nik79b, Thm. 0.2.4, printed p. 1404]" in page
    assert "is not a fan" in page
    register = REGISTER.read_text(encoding="utf-8")
    assert "lem:k-not-two-reflective" in register


def test_the_k_greater_one_comparison_fan_is_not_a_prism():
    """What "unprinted" means at the k >= 2 cusps: the fan is not the printed one times a line.

    In N_k = <-2k> + U + E8(-1)^2 the vector r = g + (k-1)e + f has square -2, and its
    mirror meets the interior of Rg x C, where C is the chamber of U + E8(-1)^2; so the
    Coxeter chamber of N_k is strictly smaller than the prism, and for k >= 2 the fan at
    the cusp with d/p^2 = k cannot be read off the printed 24-root diagram.
    """
    page = page_text()
    assert "#lem:k-greater-one-fan-not-prism" in page
    assert "is not the product of the printed $F_2$ fan with a line" in page
    assert "$r=g+(k-1)e+f$" in page
    register = REGISTER.read_text(encoding="utf-8")
    assert "lem:k-greater-one-fan-not-prism" in register


def test_the_p_greater_one_cusp_shares_a_one_cusp_with_the_unigonal_one():
    """The link between the decided cusps and the open ones: a common 1-cusp.

    For delta = g + p(e1 + k f1) the vector e2 is a primitive isotropic vector with
    p_*(e2) = 1 (the unigonal cusp), orthogonal to delta, so J = Z delta + Z e2 is a
    primitive isotropic plane and the 1-cusp F_J carries both 0-cusps.  AE23 Def. 5.11,
    printed p. 14, requires the direction sublattice H_{J,delta} to be independent of
    delta in J, so the two 0-cusp semifans are tied at that 1-cusp.
    """
    page = page_text()
    assert "#lem:p-cusp-meets-unigonal" in page
    assert "#lem:shared-one-cusp-lattice" in page
    assert "\\langle-2k\\rangle\\oplus E_8(-1)^{\\oplus2}" in page
    assert "$J=\\ZZ\\delta\\oplus\\ZZ e_2$ is a primitive isotropic rank-two sublattice" in page
    assert "$H_{J,\\delta}=H_{J,e_2}$" in page
    assert "with $p_*(\\delta_\\eta)=p>1$" in page
    assert "k=d/p^2=d_0h^2" in page
    register = REGISTER.read_text(encoding="utf-8")
    assert "lem:p-cusp-meets-unigonal" in register


def test_the_mirror_trace_step_does_not_claim_the_lattice_has_no_minus_four_vector():
    """gamma_L itself is a vector of N of square -4, so the square -4 case is not empty.

    What excludes the two facets is that the Coxeter fan is cut by the (-2)-roots alone
    (AET23 Def. 4.1, printed p. 21), and that no (-2)-vector other than +-t has its mirror
    through h_gamma or h_beta.  The landed version said the square (-4) case was empty, by a
    count of N* that ignores gamma_L in U + E8(-1)^2; that sentence must not return.
    """
    page = page_text()
    block = page[page.index("#lem:rcop-refinement-criterion"):page.index("#qst:recognizable-semifan")]
    assert "$2s$ with $s\\in N^*$" not in block
    assert "and here that case is empty" not in block
    assert r"$\gamma_L$ itself has $\gamma_L^2=-4$" in block
    assert r"no $(-2)$-vector other than $\pm t$" in block


@pytest.mark.xfail(
    strict=True,
    reason="no record decides the split at the cusps of F_2d for d >= 2: the explicit description "
    "of the rational-curve semifan is open in the literature (AE23, Intro., printed p. 3), the "
    "KSBA stable limit of (X, eps R_rc) over a cone is not an operation of sage-extensions "
    "(rmk:missing-stable-limit), and the Coxeter fan at those cusps is not printed",
)
def test_the_split_for_the_rational_curve_divisor_is_decided():
    """Acceptance item 1's remaining clause: the split I | J and the cones for R_rc on F_2d."""
    record = REPORTS / "coble_679-rcop-split-decided-run.txt"
    assert record.exists(), "no decision record: the split is not computed"
    text = record.read_text(encoding="utf-8")
    assert re.search(r"^I = ", text, re.M), "the record does not state the relevant set I"
    assert re.search(r"^J = ", text, re.M), "the record does not state the irrelevant set J"
