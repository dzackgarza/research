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
    # the conjecture's body still reads unconditionally, so its caveat must stay inside the same
    # block: the object it names has no referent, and that has to be said where the claim is made
    conj_block = block("conj:no_moduli_loss")
    assert "determines its marked Coble root" in conj_block
    assert "no referent" in conj_block, "the caveat has drifted out of the conjecture"
    marking = (ROOT / "writing/coble/cusp-correspondence/cusp-diagram-calculations.md").read_text(encoding="utf-8")
    warn_block = marking[marking.index("#warn:coble-marking"):]
    warn_block = warn_block[:warn_block.index("\n:::")] if "\n:::" in warn_block else warn_block[:4000]
    joined = " ".join(warn_block.split())
    assert "no dictionary from the nine roots" in joined
    assert "cusp marking" in joined
    assert "the sources read supply none" in " ".join(marking.split()) or \
           "the sources read give no dictionary" in joined


def test_item_3_the_cusp_marking_is_in_no_source_held_here() -> None:
    """Item 3's first block, checked against the sources rather than asserted.

    The corrected conjecture needs the identification of the cusp chamber's simple roots with
    curves of the Coble surface.  `warn:coble-marking` says no source read gives it; the search over
    the two sources that warning names, both held in tmp/sources, confirms it: AN06 never says
    "Coble" at all (it supplies the boundary lattice K_I), and DK13 section 8 describes the Coble
    surface through phi_h and its branch curve W without ever pairing a root with a curve.  The one
    root-to-component dictionary that does exist is the Enriques/K3 one, which is not this.
    """
    run = ROOT / "computations/reports/coble_760-cusp-marking-search-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "occurrences of 'Coble': 0" in text
    assert "section 8 begins at line" in text
    assert "lines in the whole article pairing a simple root with a curve: 0" in text
    verdict = " ".join(text.split())
    assert "it is a definition, not a citation" in verdict
    assert "author has to decide it" in verdict
    assert text.rstrip().endswith("PYEXIT=0")


def test_item_3_the_divisor_the_conjecture_rests_on_is_sourced() -> None:
    """Item 3: the half that is citation rather than decision, settled at the pages named.

    `def:coble-descended-ramification` cites AEGS25 §2.4 printed p. 588 and Prop. 6.1(2) printed
    p. 616.  Both resolve: Definition 2.10 is on 588, Proposition 6.1 is stated on 615, and its
    part (2) --- "R_Z = 1/2 rho_*(B_W) ... are reduced divisors and one has R = psi_*(R_Z)" --- is on
    616.  So the divisor the corrected conjecture reads off exists in the source; what is missing is
    the dictionary attaching a class of K_I to it, which is `warn:coble-marking`.
    """
    run = ROOT / "computations/reports/coble_760-descended-divisor-citations-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "Definition 2.10" in text
    assert "Proposition 6.1" in text
    assert "are reduced divisors and one has R = " in text
    assert "NOT FOUND" not in text
    verdict = " ".join(text.split())
    assert "not the divisor but the dictionary" in verdict


def test_the_restricted_diagram_keeps_the_conclusion() -> None:
    """The issue names the RESTRICTED semifan; the theorem is proved from the Enriques diagram.

    The restriction to the Coble hyperplane keeps the walls orthogonal to delta, and its irrelevant
    roots are the Enriques irrelevant ones among those.  At every marked cusp the admissible roots
    are still irrelevant there: cusp 3 keeps [12], cusp 4 keeps [10], cusp 5 keeps [7, 12, 13, 14].
    So the conclusion holds for the object the issue names and not merely for the diagram it was
    proved from.
    """
    run = ROOT / "computations/reports/coble_760-restricted-irrelevance-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "irrelevant in the RESTRICTED diagram: [12]" in text
    assert "irrelevant in the RESTRICTED diagram: [10]" in text
    assert "irrelevant in the RESTRICTED diagram: [7, 12, 13, 14]" in text
    assert text.count("all irrelevant after restriction: True") == 3
    assert "the semifan the issue names" in " ".join(text.split())


def test_item_3_the_marking_is_absent_from_the_whole_corpus() -> None:
    """Item 3: the dictionary is missing from every source held, not just the three read closely.

    The sweep scores each file in tmp/sources for "Coble", "root" and "curve", and prints the lines
    that mention a root and a curve together, so a lead can be judged without opening the file.  The
    eleven files with such a line are coincidental: the lines speak of root lattices attached to
    sextic curves, not of the cusp chamber's roots identified with curves of the Coble surface.
    """
    run = ROOT / "computations/reports/coble_760-marking-source-sweep-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "files swept:" in text
    assert "root/curve line" in text
    assert "the lines, so the lead can be judged without opening the file" in text
    assert "a root/curve line elsewhere in this" in " ".join(text.split())
    # and the three sources that describe Coble surfaces were read at their sections
    close = ROOT / "computations/reports/coble_760-cusp-marking-search-run.txt"
    assert "DZ01 (dolgachev-zhang 2001)" in close.read_text(encoding="utf-8")


def test_item_3_the_vacuity_claim_is_withdrawn_and_the_pair_named() -> None:
    """Item 3: the vacuity theorem of bdb78a77ce is withdrawn, and the page names the open pair.

    That commit argued that the three admissible roots at cusp 5 are one Gamma_Co,2-orbit and that
    conj:no_moduli_loss therefore holds vacuously.  The argument failed on membership in Gent: the
    12 <-> 13 witness is an integral isometry of T_En fixing delta and eta_5, but it does not
    preserve the two summands of A_{T_En}, so it is not in Gent = rho^{-1}(M) and proves only an
    O(T_En)-orbit (computations/reports/coble_760-gent-membership-run.txt).  The page must carry
    that withdrawal in place of the theorem, and it must not claim the hypothesis is never met.
    """
    text = page()
    assert "#thm:no-moduli-loss-vacuous}" not in text, "the withdrawn theorem is still declared"
    warning = block("warn:no-moduli-loss-vacuity")
    for step in ("bdb78a77ce", "coble_760-gent-membership-run.txt", "@AEGS25, Def. 2.6",
                 "@Ste91, Prop. 2.7", "13\\leftrightarrow14"):
        assert step in warning, step
    conj_block = block("conj:no_moduli_loss")
    assert "Open at one pair" in conj_block
    assert "Settled, vacuously" not in conj_block
    assert "holds vacuously: the marking is unique" not in text
    # the open pair is named in the remark, and the two surviving facts with it
    remark = block("rmk:coble-root-orbits-cusp-five")
    assert "undecided for $\\Gamma_{\\Co,2}$" in remark
    assert "13$ and $14$ are $\\Gamma_{\\Co,2}$-equivalent" in remark
    assert "lies outside $\\gent$" in remark
    assert "coble_760-gent-membership-run.txt" in remark


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
    for token in ("witness-13-14-run.txt", "witness-12-13-run.txt",
                  "undecided for $\\Gamma_{\\Co,2}$",
                  "the question the issue asks is open exactly at that pair"):
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


def test_item_7_the_cusp_symmetries_do_not_identify_the_roots() -> None:
    """Item 7: the diagram's own symmetries cannot witness the equivalence, and this is why.

    Of the eight automorphisms of Sterk's labelled cusp-5 Gram, two fix the Coble root's label
    (the root of label 11 is +-delta), one swaps labels 12 and 13, and that one does not fix label
    11: every symmetry that swaps the roots moves delta.  So no symmetry of the cusp identifies
    them while preserving the marking --- a negative about the diagram, which is why the question
    needs Gamma_Co,2's elements and not the chamber's.
    """
    record = ROOT / "computations/reports/coble_760-cusp-symmetry.py"
    run = ROOT / "computations/reports/coble_760-cusp-symmetry-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = " ".join(run.read_text(encoding="utf-8").split())
    assert "There are 8 symmetries of the labelled diagram, 2 of them fix the Coble root's label" in text
    assert "1 swap labels 12 and 13, and of those 0 fix label 11" in text
    assert "no symmetry of the cusp identifies 12 with 13 while preserving the Coble root's label" in text
    assert "not about Gamma_Co,2" in text
    # and the one pair a marking-preserving symmetry does exchange, with the lift named as the gap
    assert "fixes the Coble root's label 11, and exchanges labels 13 and 14" in text
    assert "Whether it lifts is an extension problem" in text


def test_item_7_the_mod_two_lift_test_has_no_obstruction() -> None:
    """Item 7: the cheapest necessary condition for the lift, run and found satisfied.

    An integral isometry acts on T_En/2T_En, so congruent roots must stay congruent.  Among the
    fourteen roots only labels 7 and 9 are congruent modulo 2, and both permutations at issue
    respect that, so the test removes no candidate and settles nothing.  Recording it matters:
    it is the one lift test that could have proven the roots inequivalent outright.
    """
    run = ROOT / "computations/reports/coble_760-mod2-lift-obstruction-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "pairs of roots congruent modulo 2: {7: [9]}" in text
    assert text.count("mod-2 congruences preserved: True") == 2
    verdict = " ".join(text.split())
    assert "no mod-2 obstruction to either permutation" in verdict
    assert "remains the open input for item 7" in verdict


def test_item_7_one_pair_is_settled_by_a_witness() -> None:
    """Item 7: roots 13 and 14 are Gamma_Co,2-equivalent, certified by an explicit isometry.

    The symmetry that fixes the Coble root's label and exchanges 13 with 14 lifts: the root span has
    rank 10, its complement rank 2, the two glue into T_En with index 2, and the gluing class
    (0, 1/2, 0, ..., 0 | 0, 0) is preserved.  The record builds the extension as a 12 x 12 integral
    matrix and checks it, so the equivalence is not asserted but exhibited.  What remains for item 7
    is root 12 against that pair.
    """
    run = ROOT / "computations/reports/coble_760-witness-13-14-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert text.count("g preserves the form: True") == 2, "both permutations lift as isometries"
    assert text.count("g maps every printed root as the permutation says: True") == 2
    # the 13/14 witness keeps delta and eta, so it is in Gamma_Co,2; the 12/13 one does not
    assert "g(delta) = delta: True" in text and "g(delta) = delta: False" in text
    assert "roots 13 and 14 are\n      Gamma_Co,2-equivalent at cusp 5" in text
    assert "witnesses only that the two" in text and "one O(T_En)-orbit" in text
    # the witness is already in the reflection group, so it adds no route to root 12
    assert text.count("same group on this orbit: True") == 3
    assert "root 12 is untouched by that route" in " ".join(text.split())


def test_item_7_the_finite_symmetry_group_separates_root_12() -> None:
    """Item 7: the finite group of lifted symmetries leaves root 12 alone.

    The two lifted permutations generate a group of order 8; two of its elements fix delta and
    eta_5 up to sign, and their orbits on the three admissible classes are [[12], [13, 14]].  So the
    finite symmetry group does not identify 12 with the pair already proved equivalent, and what is
    left is the infinite part of Gamma_Co,2 -- the reduction the library states it does not have.
    """
    run = ROOT / "computations/reports/coble_760-cusp-symmetry-group-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert "the group generated by the two lifted symmetries has order 8" in text
    assert "elements fixing +-delta: 2;  of those fixing +-eta_5: 2" in text
    assert "orbits of the three admissible classes" in text and "[[12], [13, 14]]" in text
    assert "not the whole stabilizer of eta_5 in Gamma_Co,2" in text


def test_item_7_the_pair_invariant_is_uniform_too() -> None:
    """Item 7: the last delta-sensitive invariant agrees on all three roots.

    The complement of the saturation of <delta, r> is the invariant that remembers the Coble root,
    and it is isometric for all three pairs.  With this, every invariant computable from one or two
    vectors is exhausted; what separates root 12 from 13, if anything does, is the orbit under the
    infinite stabilizer, which the library states it cannot compute.
    """
    run = ROOT / "computations/reports/coble_760-pair-complement-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    assert text.count("complements of <delta,r> isometric -> True") == 3
    assert text.count("det   1024") == 3
    verdict = " ".join(text.split())
    assert "does not separate root 12 from 13" in verdict
    assert "sage-extensions#370" in verdict


def test_item_3_the_semifan_arithmetic_is_done_and_the_marking_is_not() -> None:
    """Item 3: what is missing is the geometric dictionary, not the semifan arithmetic.

    Another record, `coble_pair-semifan-cusps.py`, computes the restricted chamber at each Coble
    0-cusp --- projected wall Gram, bond graph, coincident walls, inherited relevance, W_irr,
    maximal affine subdiagrams, the semifan-restriction hypotheses, and the chamber's volume --- and
    it reads its relevance input from this issue's own transcript.  So the arithmetic side of the
    restricted semifan is settled and cross-linked, and the only thing item 3 still lacks is the
    dictionary from the chamber's roots to curves of the Coble surface.
    """
    pair = ROOT / "computations/reports/coble_pair-semifan-cusps.py"
    assert pair.exists(), pair
    text = pair.read_text(encoding="utf-8")
    assert "coble_irrelevant-marking-face-run.txt" in text, "the relevance input is no longer read"
    assert "inherited relevance" in text or "irrelevant" in text
    # and its transcript reports a per-cusp verdict, so the computation ran
    run = ROOT / "computations/reports/coble_pair-semifan-cusps-run.txt"
    assert run.exists(), run
    assert "part D summary" in run.read_text(encoding="utf-8")


def test_item_7_the_third_pair_is_not_settled_by_that_witness() -> None:
    """Item 7: the 12 <-> 13 matrix is integral, but it is not in Gent, so the pair stays open.

    No symmetry of the printed diagram exchanges 12 and 13 while fixing the Coble root, and the span
    of delta, r12, r13 is not a direct summand (index 2).  The transposition of its two square-(-2)
    generators extended by the identity on the rank-9 complement is integral, of determinant -1,
    form-preserving, and it fixes delta and eta_5 --- but Gamma_Co,2 = R_Gent is the image of
    Stab_Gent(delta), Gent is the summand-preserving subgroup of O(T_En) ([AEGS25, Def. 2.6],
    [Ste91, Prop. 2.7]), and this matrix carries classes out of both summands of A_{T_En}.  It
    witnesses an O(T_En)-orbit and nothing more.
    """
    run = ROOT / "computations/reports/coble_760-witness-12-13-run.txt"
    assert run.exists(), run
    text = run.read_text(encoding="utf-8")
    for line in ("g integral: True", "g^T G g == G: True", "g(delta) == delta: True",
                 "g(eta) == eta: True", "g(r12) == r13: True"):
        assert line in text, line
    assert "det g: -1" in text
    gent = ROOT / "computations/reports/coble_760-gent-membership-run.txt"
    record = ROOT / "computations/reports/coble_760-gent-membership.py"
    assert gent.exists() and record.exists(), (gent, record)
    g = gent.read_text(encoding="utf-8")
    assert g.rstrip().endswith("PYEXIT=0"), "the record did not run to its anchor"
    # the two witnesses take opposite verdicts, and the calibration is on the page's own elements
    for line in ("12 <-> 13 witness (transposition on that span) integral True  form True  fixes delta,eta_5 True  in Gent False",
                 "13 <-> 14 witness (the diagram symmetry)       integral True  form True  fixes delta,eta_5 True  in Gent True",
                 "carried out of A_{E8(-2)} by the classes [d_6], [d_7], [d_11]",
                 "A_{U(2)}  generated by the classes [d_3], [d_4]      has order 4",
                 "A_{E8(-2)} generated by the classes [d_5], ..., [d_12] has order 256"):
        assert " ".join(line.split()) in " ".join(g.split()), line
    for lab in (1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14):
        line = "s_w, printed label %d" % lab
        assert line in g, line
    assert "in Gent True" in [l for l in g.splitlines() if l.startswith("s_w, printed label 12")][0]


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


def test_item_7_the_two_records_agree_on_what_is_open() -> None:
    """Item 7: the page's remark, the open-questions row and #759's swap record say the same thing.

    Three places now record the state of the orbit question: this issue's remark on the page, the
    open-questions row, and the parallel record `coble_759-swap-1213-run.txt`, which attacks the
    (12,13) pair by a direct-sum construction and reports the same obstruction this issue's probes
    found --- the pair's span is not a direct summand.  They must not drift apart.
    """
    remark = block("rmk:coble-root-orbits-cusp-five")
    assert "undecided for $\\Gamma_{\\Co,2}$" in remark
    assert "does not make the pair $\\gent$-inequivalent" in remark
    row = [l for l in OPEN_QUESTIONS.read_text(encoding="utf-8").splitlines()
           if "no_moduli_loss" in l][0]
    assert "roots $13$ and $14$ are one orbit" in row
    assert "the open step is the $\\Gamma_{\\Co,2}$-orbit of Sterk's label $12$ at cusp $5$" in row
    assert "is not settled by the integral isometry" in row
    assert "coble_760-gent-membership-run.txt" in row
    assert "holds vacuously" not in row
    # the parallel record's obstruction stays on file, as the reason no diagram symmetry sufficed
    swap = ROOT / "computations/reports/coble_759-swap-1213-run.txt"
    assert swap.exists(), swap
    text = " ".join(swap.read_text(encoding="utf-8").split())
    assert "P is not a direct summand (index 4)" in text


def test_item_7_the_mod_two_probe_is_one_sided_and_says_so() -> None:
    """Item 7: the mod-2 orbit of label 12 is a one-sided test, and nothing reads a decision off it.

    Gamma(2) is contained in ker rho, hence in Gent, so the class of a root mod 2T_En is invariant
    along a Gamma_Co,2-orbit and the mod-2 orbit is a necessary condition.  The orbit this record
    can compute is the orbit under a subgroup of Gent --- the elements it can build and check --- so
    a class missing from it is not a proof of inequivalence.  The record must carry that scope, and
    the page must not claim the pair is decided.
    """
    record = ROOT / "computations/reports/coble_760-mod2-orbit-probe.py"
    run = ROOT / "computations/reports/coble_760-mod2-orbit-probe-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert text.rstrip().endswith("PYEXIT=0"), "the probe did not run to its anchor"
    flat = " ".join(text.split())
    for line in ("generators checked and accepted as Gent elements: 23",
                 "orbit of the class of label 12: 512 classes",
                 "class of 13 in the orbit of 12: False",
                 "class of 14 in the orbit of 13: True",
                 "it shows that no product of these twenty-three elements carries r12 to r13, and not that Gent contains none",
                 "the intersection is built as a predicate and not resolved into generators"):
        assert line in flat, line
    doc = record.read_text(encoding="utf-8")
    assert "decides nothing about the pair" in doc
    assert "Nothing here is a substitute for it" in " ".join(doc.split())
    # the page states the pair open and cites no decision
    remark = block("rmk:coble-root-orbits-cusp-five")
    assert "undecided for $\\Gamma_{\\Co,2}$" in remark
    assert "mod2-orbit-probe" not in remark, "the page must not lean on a one-sided probe"


def test_item_7_the_gent_family_is_named_by_the_call_that_fails() -> None:
    """Item 7: the point A_{U(2)} is constructible; the preimage that would name Gent is killed.

    The decisive mod-2 triple test needs a complete generating family of Gent, that is
    rho^{-1} of the stabilizer of A_{U(2)} in O(A_L).  The point itself can be named in the
    discriminant module by integer coordinates, and the quadratic form confirms which pair of classes
    it is.  The preimage call is killed at the memory ceiling, which is the defect this record
    reports; it must not be reported as a missing *operation* on the page, and the page must not
    claim a decision from it.
    """
    record = ROOT / "computations/reports/coble_760-gent-family-probe.py"
    run = ROOT / "computations/reports/coble_760-gent-family-probe-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    for line in ("class e_3 -> q = [0]", "class e_3 + e_4 -> q = [1]",
                 "calling discriminant_point_stabilizer(point).group_generators()",
                 "killed: exit status 137 (SIGKILL, the memory ceiling), 625 s",
                 "r12 - r13 b(., e_i) mod 2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] in the radical: True",
                 "so no mod-2 pairing separates the two classes"):
        assert line in flat, line
    doc = " ".join(record.read_text(encoding="utf-8").split())
    assert "does not return" in doc
    assert "Nothing here is a substitute for either" in doc
    remark = block("rmk:coble-root-orbits-cusp-five")
    assert "gent-family-probe" not in remark, "the page must not lean on a killed computation"


def test_item_7_the_orbit_call_exists_and_its_family_is_refuted() -> None:
    """Item 7: the #370 orbit call runs and returns singletons; its acting family is incomplete.

    The call exists and is used, so the item is not "no operation".  What it returns is three
    singleton orbits, which by its own docstring decides nothing; and the family it acts with is
    refuted inside the record by an element of the group it claims to act with: g_{13<->14} fixes
    delta and eta_5 and lies in Gent, so it joins 13 and 14 in K_5, and the call separates them.
    """
    record = ROOT / "computations/reports/coble_760-cusp5-root-orbits.py"
    run = ROOT / "computations/reports/coble_760-cusp5-root-orbits-run.txt"
    assert record.exists() and run.exists(), (record, run)
    text = run.read_text(encoding="utf-8")
    assert text.rstrip().endswith("PYEXIT=0"), "the run did not reach its anchor"
    flat = " ".join(text.split())
    for line in ("returned 3 orbits:", "1 class(es): ['12']", "1 class(es): ['13']",
                 "1 class(es): ['14']",
                 "g_{13<->14}: integral True, isometry True, in Gent True",
                 "so its reduction lies in G_v and joins the classes of 13 and 14, which the call separates",
                 "complete generating family at a primitive isotropic line"):
        assert line in flat, line
    remark = block("rmk:coble-root-orbits-cusp-five")
    assert "coble_760-cusp5-root-orbits-run.txt" in remark
    assert "sage-extensions#312" in remark


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
