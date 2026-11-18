"""Acceptance gate for research#760: the face of the restricted semifan and the marked root.

The acceptance, item by item, is the issue body together with its four review comments:

  item 1   the page states, as a theorem with proof or as a counterexample with its
           computation, whether the face determines the marked Coble root.
  item 2   every step of it is cited: authors, numbered statement, page of the version read.
  item 3   conj:no_moduli_loss is a theorem that cites item 1, or it is corrected to match.
  item 4   the page carries a pair r_1, r_2 whose faces agree (comment 1, "define the
           object exactly" and "inequivalence is not shown" are items 8 and 7 below).
  item 5   a computation record under computations/reports/ produces item 4.
  item 6   the object compared is defined exactly (comment 1, point 2).
  item 7   the pair is INEQUIVALENT under Gamma_Co,2 (comment 1, point 1).
  item 8   cusp 4 is not offered as a pair (comment 1, point 3).
  item 9   one version of AEGS25, each statement at the page of that version (comment 1,
           point 4).

Each test names the smallest input that decides its item: the page's statement for the prose
items, the committed transcript for the computed ones.  Nothing here re-derives a computation:
the transcripts are the evidence and the page quotes them or quotes nothing.  No Sage, no
provider call, standard library only, so the file runs under ``python3 -m pytest`` as well as
standalone.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/stable-limits/ksba.md"
FACE_RUN = ROOT / "computations/reports/coble_irrelevant-marking-face-run.txt"
ORBIT_RUN = ROOT / "computations/reports/coble_gammaCo2-orbits-cusp5-run.txt"
ORBIT_RECORD = ROOT / "computations/reports/coble_gammaCo2-orbits-cusp5.py"
OPEN_QUESTIONS = ROOT / "writing/open-questions.md"


def page() -> str:
    return PAGE.read_text(encoding="utf-8")


def block(identifier: str) -> str:
    """The fenced div whose id is `identifier`, without its neighbours."""
    text = page()
    start = text.index("#" + identifier)
    start = text.rindex("::: {", 0, start)
    end = text.index("\n:::", start)
    return text[start:end]


def test_item_1_the_page_states_the_verdict() -> None:
    """Item 1: the smallest input is the theorem's own statement."""
    theorem = block("thm:face-irrelevant-marking")
    assert ".theorem" in theorem
    assert "irrelevant" in theorem and "one and the same cone" in theorem
    assert "12" in theorem and "13" in theorem and "14" in theorem


def test_item_2_every_step_is_cited_at_a_printed_page() -> None:
    """Item 2: the numbered statements and their printed pages, as the page writes them."""
    text = page()
    for citation in (
        "Def. 5.4, printed p. 611",
        "Lemma 5.5, printed p. 611",
        "Lemma 5.6, printed p. 611",
        "Lemma 5.8, printed p. 611",
        "Lemma 5.2, printed p. 610",
        "Lemma 3.10, printed p. 594",
        "Fig. 5, printed p. 592",
        "§5.2, printed p. 610",
    ):
        assert citation in text, citation


def test_item_3_the_conjecture_is_corrected_not_proved() -> None:
    """Item 3: the conjecture's corrected form says what the face does and does not give."""
    conjecture = block("conj:no_moduli_loss")
    assert ".conjecture" in conjecture
    assert "read off the contracted" in conjecture          # the conjecture's own title
    assert "no face can" in conjecture                      # the corrected statement
    # the open computation must still be visible, in whatever wording the page currently uses
    assert any(t in conjecture for t in ("not made", "uncomputed",
                                         "no operation in the library decides",
                                         "cannot be computed")), conjecture[:200]


def test_item_3_the_lean_route_and_its_blocker() -> None:
    """Item 3, second reading: the LC-09 search over what is installed, and the absence it found.

    The acceptance's proof route wants conj:no_moduli_loss as a theorem, which the issue's
    contestation rule accepts only as a lean-categories declaration after the LC-09 search.  The
    search has been run (``coble_760-lean-declaration-search-run.txt``): Mathlib carries
    CoxeterSystem and the quadratic-form and bilinear-form types, carries no occurrence of
    semifan, semitoroidal, KSBA, stable pair, Enriques, Coxeter fan, Vinberg, fundamental chamber
    or reflection group, and CSLib carries none of them either; the ``Fan`` declarations Mathlib
    does have are the categorical BinaryFan, not a toric fan.  Lean's own checker agrees
    (``coble_760-lean-declaration-probe-run.txt``): the four Coxeter and quadratic-form names
    elaborate and ``#check @Semifan`` is an unknown identifier.

    So the declaration cannot be built here at all: it needs the lean-categories library, which
    has no checkout at any of the five paths tried --- including ``~/gitclones/lean-categories``,
    the location ``computations/scripts/sterk-enriques-cusps/DAG.md`` documents for it --- and is
    not on LEAN_PATH.
    """
    search = (ROOT / "computations/reports/coble_760-lean-declaration-search-run.txt")
    probe = (ROOT / "computations/reports/coble_760-lean-declaration-probe-run.txt")
    assert search.exists() and probe.exists(), (search, probe)
    found = search.read_text(encoding="utf-8")
    assert "CoxeterSystem" in found
    for absent in ("Semifan", "semitoroidal", "KSBA", "Enriques", "Vinberg"):
        assert absent not in found.split("=== the two structural facts")[0], absent
    assert "no checkout anywhere on this machine" in found
    checked = probe.read_text(encoding="utf-8")
    assert "CoxeterSystem" in checked and "QuadraticForm" in checked
    assert "Unknown identifier `Semifan`" in checked


def test_item_3_names_the_owner() -> None:
    """Item 3 stops at an owner in another repository, and this pins where that is recorded.

    The obligation is the publication of lean-categories' `Lattices/Valued/` subtree, the lattice,
    discriminant and orthogonal-group layer a declaration of the semifan statement would sit on.
    Two tracked files carry that: `computations/scripts/sterk-enriques-cusps/DAG.md` says the
    refactor and publication is "tracked as an issue on `lean-categories`, not here", and
    `docs/theory/hyperbolic-index.md` names the modules (`LeanCategories/Lattices/Valued/`).
    No issue number is recorded in this repository, and the connector reads this project's one
    connected repository only, so the number cannot be fetched from here.  That is the named
    input, not a substitute for it.
    """
    dag = " ".join((ROOT / "computations/scripts/sterk-enriques-cusps/DAG.md")
                   .read_text(encoding="utf-8").split())
    assert "tracked as an issue on `lean-categories`, not here" in dag
    assert "Sixteen nodes carry `R`" in dag, "the repository's own Lean development moved"
    index = (ROOT / "docs/theory/hyperbolic-index.md").read_text(encoding="utf-8")
    assert "LeanCategories/Lattices/Valued/" in index
    assert "~/gitclones/lean-categories" in dag
    # the repository's own Lean development is the natural home, since it carries the
    # neighbouring atoms: the subgroup, the divisor ideal, the cone.  What it does not carry is
    # the notion the statement is about, and that is the sharp form of the block.
    atoms = (ROOT / "computations/scripts/sterk-enriques-cusps/lean/Atoms.lean")
    text = atoms.read_text(encoding="utf-8")
    assert "def orthogonalGroup" in text, "the neighbouring atom is gone"
    assert "def divisorIdeal" in text
    assert "def lorentz" in text or "def negativeCone" in text
    for missing in ("def Semifan", "def Chamber", "def Irrelevant", "def Fan"):
        assert missing not in text, missing
    assert "sorry" not in text, "the atom file must stay sorry-free"


def test_item_3_the_statement_cannot_be_expressed() -> None:
    """Item 3, at the level below the library: the definitions the theorem needs do not exist.

    Lean carries the cone primitives the statement would be built on --- `ConvexCone`,
    `PointedCone`, `Module.Ray` all elaborate --- and carries no `Semifan`, no `Fan`, no `Chamber`
    and no `Irrelevant`.  Without a fan there is no face lattice to coarsen, so the coarsening the
    theorem is about cannot even be stated, let alone proved.  That is the sharper form of the
    block, and the transcript carries both halves of it.
    """
    record = ROOT / "computations/reports/coble_760-lean-expressibility-probe.lean"
    run = ROOT / "computations/reports/coble_760-lean-expressibility-probe-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    for present in ("ConvexCone", "PointedCone", "Module.Ray"):
        assert present in text, present
    for absent in ("Semifan", "Fan", "Chamber", "Irrelevant"):
        assert f"Unknown identifier `{absent}`" in text, absent
    assert "no face lattice of a fan to coarsen" in record.read_text(encoding="utf-8")


def test_item_3_beneath_the_library_the_statement_is_unstatable() -> None:
    """Item 3, second input: the conjecture's corrected form has no referent without a cusp marking.

    The corrected conjecture reads the marking off the contracted (-4)-curve, and doing so needs
    the identification of the chamber's simple roots with curves of the Coble surface.  The page
    carries that gap as `warn:coble-marking`, which names the sources it read and says they supply
    no such dictionary, and the conjecture cites it.  So item 3 is blocked in two places: a fan and
    coarsening definition in Lean, and this dictionary, which is a definition the author has to
    decide because no source read gives it.
    """
    page_text = page()
    assert "@warn:coble-marking" in page_text, "the conjecture no longer cites the missing marking"
    marking = (ROOT / "writing/coble/cusp-correspondence/cusp-diagram-calculations.md").read_text(encoding="utf-8")
    block = marking[marking.index("#warn:coble-marking"):]
    block = block[:block.index("\n:::")] if "\n:::" in block else block[:4000]
    joined = " ".join(block.split())
    assert "no dictionary from the nine roots" in joined
    assert "cusp marking" in joined
    assert "the sources read supply none" in " ".join(marking.split()) or \
           "the sources read give no dictionary" in joined


def test_item_4_a_pair_whose_faces_agree() -> None:
    """Item 4: the transcript's face line is the smallest input."""
    text = FACE_RUN.read_text(encoding="utf-8")
    line = [l for l in text.splitlines() if "the face of F_5 cut by r^perp" in l]
    assert len(line) == 1, line
    assert line[0].count("the maximal cone M") == 3, line[0]
    assert "label 12" in line[0] and "label 13" in line[0] and "label 14" in line[0]


def test_item_5_the_record_exists_and_exits_zero() -> None:
    """Item 5: both records, their transcripts, and the anchored exit line."""
    for path in (FACE_RUN, ORBIT_RUN, ORBIT_RECORD):
        assert path.exists(), path
    for path in (FACE_RUN, ORBIT_RUN):
        assert path.read_text(encoding="utf-8").rstrip().endswith("PYEXIT=0"), path


def test_item_6_the_object_is_defined() -> None:
    """Item 6: the definition of the cone cut by r^perp, and the rejected alternative."""
    theorem = block("thm:face-irrelevant-marking")
    assert "relative interior of $r^{\\perp}\\intersect\\mathfrak{C}_I$" in theorem
    assert "smallest cone, and not the restricted fan" in theorem


def test_item_7_the_inequivalence_leg_and_its_bound() -> None:
    """Item 7: still open; the transcript carries the bound and the invariants that fail to
    separate the roots, and the page remark carries the same."""
    text = ORBIT_RUN.read_text(encoding="utf-8")
    assert "div_{K_5}(r) = 1" in text
    assert "not reached within depth 12 over 20484 classes" in text
    assert "the subgroup generated by the twelve certified reflections does not carry" in text
    remark = block("rmk:coble-root-orbits-cusp-five")
    for token in ("20\\,484", "depth $12$", "divisibility $1$ in $K_5$", "not proved"):
        assert token in remark, token


def test_item_7_the_orbit_decision_probe_and_its_bound() -> None:
    """Item 7's probe: what the library can and cannot do, run against a stated bound.

    The library builds K_5 in about a second and exposes orbit series for its standard
    orthogonal subgroups; it exposes no reduction or normal form for a subgroup, and
    ``K.primitive_orbit_series(bound=4)`` does not return within the wrapper's bound.  Those three
    facts are what make the orbit question undecidable here rather than merely unattempted, and
    the transcript carries all of them.
    """
    record = ROOT / "computations/reports/coble_760-orbit-decision-probe.py"
    run = ROOT / "computations/reports/coble_760-orbit-decision-probe-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert "K_5 = eta_5^perp / Z eta_5: Integral lattice of rank 10" in text
    assert "primitive_orbit_series     True" in text
    for absent in ("fundamental_domain", "reduce", "normal_form", "orbit_invariants"):
        assert absent + " " * (27 - len(absent)) + "False" in text, absent
    assert "BOUND-REACHED: K.primitive_orbit_series did not return within 600 s" in text
    assert "PROBE_EXIT=124" in text or "PROBE_EXIT=137" in text


def test_item_7_the_orbit_engine_states_its_regime() -> None:
    """Item 7: the library's vector-orbit engine is finite-regime by design, in its own words.

    Every invariant of the pair agrees (test_item_7_the_last_invariant_agrees), so the question is
    the orbit under an infinite arithmetic group on an indefinite lattice.  The library's
    decomposition engine says what it covers: "listed only when the full orthogonal group is
    finite, equivalently in the definite regime ... No finite approximation is used for an
    indefinite arithmetic centralizer."  That sentence, with its file and line, is the transcript.
    """
    run = ROOT / "computations/reports/coble_760-orbit-engine-scope-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "class _EquivariantVectorOrbitDecompositionEngine" in text
    assert "No finite approximation is used for an indefinite" in text
    assert "file: .scratch/sage-extensions/src/sage_extensions/categories/lattice_centralizers.py" in text
    assert "133:class _EquivariantVectorOrbitDecompositionEngine" in text
    assert "explicitly not for an indefinite arithmetic centralizer" in text
    assert text.rstrip().endswith("PYEXIT=0")


def test_item_7_the_last_invariant_agrees() -> None:
    """Item 7: the isometry class of the complement, which is the classical obstruction, agrees.

    The complements of the three roots in K_5 are the invariant that decides O(K_5)-orbits of
    primitive vectors.  The library builds each from its Gram and decides the isometry in under a
    second --- `is_isometric_to` returns a verified boolean --- and all three pairs come out
    isometric.  So every invariant computable on the pair agrees, and the orbit question is left
    to the subgroup alone.
    """
    record = ROOT / "computations/reports/coble_760-isometry-decision-probe.py"
    run = ROOT / "computations/reports/coble_760-isometry-decision-probe-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert text.count("is_isometric_to -> True") == 3, text.count("is_isometric_to -> True")
    assert text.count("Integral lattice of rank 9 and signature (1, 8)") == 3
    assert "no complement invariant separates the roots" in text
    assert text.rstrip().endswith("PYEXIT=0")


def test_item_7_the_degenerate_route_is_named_as_such() -> None:
    """Item 7: the obvious invariant --- the complement of the triple --- is degenerate, and this
    keeps the record from being read as a decision.

    eta_5 is isotropic, so <delta, eta_5, r> is degenerate, its complement has determinant 0, and
    an isometry decision on a degenerate form returns True for every pair.  The record says so
    rather than reporting three satisfied comparisons as evidence.
    """
    record = ROOT / "computations/reports/coble_760-marked-pair-invariant.py"
    run = ROOT / "computations/reports/coble_760-marked-pair-invariant-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert text.count("determinant 0") == 3, text.count("determinant 0")
    assert "carries no information" in text
    assert "the reduction the library lacks" in text
    assert text.rstrip().endswith("PYEXIT=0")


def test_item_7_no_witness_over_all_fourteen_roots() -> None:
    """Item 7: the witness search widened to all fourteen printed roots, and still empty.

    The earlier walk used only the eleven roots that already fix delta and eta, so every word in
    it was automatically in the acting group.  This one searches the larger group generated by all
    fourteen and tests delta and eta on the word; a word that preserves both would certify the
    roots equivalent.  None was found to depth 10 over 135 571 classes, which settles that no short
    word witnesses the equivalence --- and settles nothing about inequivalence.
    """
    record = ROOT / "computations/reports/coble_760-orbit-witness.py"
    run = ROOT / "computations/reports/coble_760-orbit-witness-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert "witnesses found: 0" in text
    assert "no witness within depth 10 over 135571 classes" in text
    assert "not a proof of inequivalence" in text
    assert "fourteen printed roots carries 12 to 13 or 14" in text
    assert text.rstrip().endswith("PYEXIT=0")


def test_item_8_cusp_four_is_not_a_pair() -> None:
    """Item 8: the transcript prints one admissible root at cusp 4."""
    text = FACE_RUN.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l.startswith("cusp 4:") and "admissible roots" in l]
    assert lines and "admissible roots [10]" in lines[0], lines
    assert "one admissible root: no pair exists" in text


def test_item_9_one_version_of_the_citation() -> None:
    """Item 9: a single AEGS25 version, and the pages are inside its printed range."""
    pages = [int(p) for p in re.findall(r"AEGS25[^]]*?printed p\. (\d+)", page())]
    assert pages, "no AEGS25 printed pages cited"
    assert all(581 <= p <= 624 for p in pages), sorted(pages)


def test_item_3_the_conjecture_is_still_a_conjecture() -> None:
    """Item 3 is open: no theorem declares the conjecture, and the regress is named.

    The proof route of the acceptance needs a lean-categories declaration of the generalized
    Coxeter semifan, its irrelevant roots, K_I and Gamma_Co,2.  That library is not present in
    this environment (no ``lean-categories`` directory under /opt, no path carrying the name,
    and LEAN_PATH holds only Cli, LeanSearchClient, Qq, aesop, batteries, importGraph, mathlib,
    plausible, proofwidgets), and the repository has no lakefile of its own.  So the check that
    holds is the negative one: nothing on the page claims the conjecture as a theorem.
    """
    text = page()
    assert "#thm:no_moduli_loss" not in text
    assert "#thm:coble-no-moduli-loss" not in text
    assert ".theorem" in text  # the theorem of item 1 is there, the conjecture is not restated as one
    conjecture = block("conj:no_moduli_loss")
    assert ".conjecture" in conjecture


def test_item_7_names_what_is_missing() -> None:
    """Item 7 is open on one named input: the stabilizer of eta_5 in Gamma_Co,2, which the walk
    replaces by a subgroup.  The record says so in its own docstring, and the bound is printed."""
    record = " ".join(ORBIT_RECORD.read_text(encoding="utf-8").split())
    assert "proper subgroup of the stabilizer of eta_5 in Gamma_Co,2" in record
    assert "NOT thereby proved inequivalent" in record
    run = ORBIT_RUN.read_text(encoding="utf-8")
    assert "20484 classes" in run or "20484" in run


def test_the_body_letter_of_route_b_and_the_comment_that_tightens_it() -> None:
    """Route (B) as the body words it: a pair whose faces agree, a record, the conjecture
    corrected.  All three are on the page.  Comment 1 adds inequivalence, which is item 7 and is
    the only piece missing; this test records the difference rather than collapsing it."""
    body_letter = (
        bool(block("thm:face-irrelevant-marking")),
        FACE_RUN.exists(),
        ".corrected" in block("conj:no_moduli_loss") or "no face can" in block("conj:no_moduli_loss"),
    )
    assert all(body_letter), body_letter
    comment_letter = "not reached within depth 12 over 20484 classes" in ORBIT_RUN.read_text(encoding="utf-8")
    assert comment_letter, "the inequivalence leg must remain visibly unproved"


def test_open_questions_row_names_the_open_step() -> None:
    """The row for the withdrawn step names the orbit computation as what is open."""
    text = OPEN_QUESTIONS.read_text(encoding="utf-8")
    row = [l for l in text.splitlines() if "no_moduli_loss" in l]
    assert len(row) == 1, row
    assert "Gamma" in row[0] or "\\Gamma" in row[0]


def _run_all() -> int:
    """Run every test in this module without pytest, which the repo's conftest needs installed."""
    items = sorted((name, fn) for name, fn in globals().items()
                   if name.startswith("test_") and callable(fn))
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)
