"""Acceptance gate for research#672 (A29): which Sterk cusp carries the Coble 0-cusp.

The acceptance is a single sentence: "Done when the question is settled in ``writing/`` with a
proof, a disproof, or a computation record, and every page that cites the open form is updated."

  item 1   the question is settled on the page as a theorem with its proof, or as a disproof.
           Here the settlement is both: the identification with cusp 2 alone is false as a
           statement about the boundary lattice, and what is true is the chamber statement.
  item 2   every step cites a published source by authors, numbered statement and printed page,
           a lattice-database card or a Lean declaration, and every computed number names its
           record.

Each test names the smallest input that decides its item: the page's statement for the prose
items, the committed transcript for the computed ones.  Nothing here re-derives a computation.
Standard library only, so the file runs under ``python3 -m pytest`` as well as standalone.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/coble-moduli/cusp-correspondence-morphism-chain.md"
DIAGRAM_PAGE = ROOT / "writing/coble/cusp-correspondence/cusp-diagrams-by-moduli-space.md"
RECORD = ROOT / "computations/reports/coble_672-zero-cusp-sterk-two-run.txt"
SCRIPT = ROOT / "computations/reports/coble_672-zero-cusp-sterk-two.py"


def page() -> str:
    return PAGE.read_text(encoding="utf-8")


def record() -> str:
    return RECORD.read_text(encoding="utf-8")


# ------------------------------------------------------------------ item 1: the settlement

def test_a1_the_conjecture_is_gone_and_a_theorem_stands_in_its_place():
    text = page()
    assert "conj:coble-zero-cusp-sterk-two" not in text, "the open form is still on the page"
    assert re.search(r"::: \{\.theorem #thm:coble-zero-cusp-sterk-two", text)
    assert "::: {.proof}" in text


def test_a1_the_page_states_both_halves_of_the_settlement():
    text = page()
    # the boundary lattice is carried by all four cusps, so the identification with cusp 2
    # alone is false; the chamber is what singles cusp 2 out
    assert "boundary lattice" in text and "(9,9,1)_1" in text
    assert "singles out no cusp" in text
    assert "singles out cusp $2$" in text or "singles out cusp 2" in text


def test_a1_the_cusp_map_lemma_the_argument_rests_on_is_stated_and_proved():
    text = page()
    assert re.search(r"::: \{\.lemma #lem:cusp-map-of-a-period-lattice-embedding", text)


# ------------------------------------------------------------------ item 2: the evidence

def test_a2_every_computed_number_names_its_record():
    text = page()
    assert "computations/reports/coble_672-zero-cusp-sterk-two-run.txt" in text
    assert "computations/reports/coble_pair-semifan-cusps-run.txt" in text


def test_a2_the_source_citations_carry_printed_pages():
    text = page()
    for cite in ("printed p. 589", "printed p. 590", "printed pp. 594--595", "printed p. 144"):
        assert cite in text, cite


def test_a2_the_record_is_committed_beside_its_script_and_reproduces_the_counts():
    assert SCRIPT.exists() and RECORD.exists()
    text = record()
    # the boundary lattice at each of the four cusps is (9,9,1), and cusp 1 is not in T_Co
    assert text.count("invariants (r,a,delta) = (9,9,1)") == 4
    assert "not a vector of T_Co" in text
    # the chamber: nine walls at cusp 2 and 10, 10, 11 at cusps 3, 4, 5
    assert "9 distinct walls" in text
    assert "10 distinct walls" in text
    assert "11 distinct walls" in text


def test_a2_the_divisibility_in_T_dp_separates_cusp_2_from_the_other_three():
    text = record()
    rows = [ln for ln in text.splitlines() if re.match(r"\s+\d\s+-?\d+\s+0\s+1\s+", ln)]
    assert len(rows) == 5, rows
    dp = {}
    for ln in rows:
        parts = ln.split()
        dp[int(parts[0])] = int(parts[5])
    assert dp[2] == 2 and dp[3] == dp[4] == dp[5] == 1, dp


def test_a2_the_cusp_vectors_printed_on_the_diagram_page_are_the_transcript_ones():
    text = DIAGRAM_PAGE.read_text(encoding="utf-8")
    # the earlier printing named y_3 by a single root and was not isotropic
    assert "\\overline{\\alpha}_8$ | 2 | 1" not in text
    assert "y_3 = -(2\\alpha_1+3\\alpha_2+4\\alpha_3+6\\alpha_4" in text


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
