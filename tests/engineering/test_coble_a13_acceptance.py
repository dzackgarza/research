"""Acceptance gate for research#656 (A13) and for the three criteria of the absorbed #81.

The item, as the issue states it: "the 22 x 22 matrix of theta_Co on U^3 + E8^2, with the
polarization classes and the diagram's roots compared in that basis.  Existence and the
eigenlattices are proved (@prop:theta-co-exists); the coordinates, the gluing anti-isometry,
and the comparison to Gamma_Co^En(delta) are not."  The absorbed #81 adds three criteria: a
canonical construction returns the involution as an isometry on the chosen K3 lattice basis;
the computed (+1) and (-1) eigenspaces are matched semantically to the geometric lattices; and
the task integrates with the automorphism/orthogonal-complement workflow and produces a
reusable test.

The four theorems that decide it are on
writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md, and the
decisions are the four records

    computations/reports/coble_a13-theta-coordinates-run.txt        theta_Co, the matrix
    computations/reports/coble_a13-gluing-anti-isometry-run.txt     gamma_Co
    computations/reports/coble_a13-heegner-comparison-run.txt       the comparison at delta
    computations/reports/coble_a13-diagram-roots-run.txt            classes and roots

These tests read those transcripts and the two pages, and the last one re-runs the four scripts
and requires the committed transcripts to be reproduced line for line from the first numbered
section on.  That is the reusable part: every number below is re-derived, in seconds, from the
marking alone -- no provider, no container, no network.

Run it with

    python3 -m pytest tests/engineering/test_coble_a13_acceptance.py \
        -q -o addopts="" --confcutdir=tests/engineering

The two overrides are environment facts, not concessions: `-o addopts=""` drops the project's
addopts, which require pytest-timeout and pytest-reportlog, and `--confcutdir` keeps
tests/conftest.py out of the run, that file importing dzack_research, whose install would pull
pandoc-config, sage-extensions and streamlit for a test that needs only sympy.  Nothing here
touches the sage image, so the job that runs it is a plain ubuntu-latest python job; it is
prepared but not landed, a push touching .github/workflows/ needing `workflow` permission.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "computations/reports"

PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
OPEN_PROBLEMS = ROOT / "writing/coble/open-problems/open-problems.md"
OWNER_RECORD = REPORTS / "coble_a21-ambient-extension-run.txt"

THETA = (REPORTS / "coble_a13-theta-coordinates.py",
         REPORTS / "coble_a13-theta-coordinates-run.txt")
GLUING = (REPORTS / "coble_a13-gluing-anti-isometry.py",
          REPORTS / "coble_a13-gluing-anti-isometry-run.txt")
COMPARISON = (REPORTS / "coble_a13-heegner-comparison.py",
              REPORTS / "coble_a13-heegner-comparison-run.txt")
ROOTS = (REPORTS / "coble_a13-diagram-roots.py",
         REPORTS / "coble_a13-diagram-roots-run.txt")
RECORDS = (THETA, GLUING, COMPARISON, ROOTS)


def _lines(record, marker):
    return [line for line in record.read_text().splitlines() if marker in line]


def _line(record, marker):
    hits = _lines(record, marker)
    assert len(hits) == 1, (marker, hits)
    return hits[0]


# --- 0. the records are there, and say what they are -----------------------------------


def test_the_four_records_exist_with_their_scripts():
    for script, record in RECORDS:
        assert script.exists(), script
        assert record.exists(), record


def test_every_record_carries_its_provenance_and_its_marking():
    for _, record in RECORDS:
        text = record.read_text()
        assert "provenance" in text
        assert "no sage and no sage-extensions" in text
        assert ("@thm:theta-co-coordinates" in text or "@prop:theta-co-exists" in text)


def test_no_record_calls_the_provider():
    for script, _ in RECORDS:
        text = script.read_text()
        assert "sage_extensions" not in text and "from sage" not in text


# --- 1. #81, criterion one: a construction, not a stored matrix -------------------------


def test_theta_Co_is_integral_and_preserves_the_form():
    line = _line(THETA[1], "theta_Co integral True")
    assert "involution True" in line
    assert "isometry True" in line
    assert "det -1, trace 0" in line


def test_theta_Co_is_a_signed_permutation_on_the_standard_basis():
    assert _line(THETA[1], "theta_Co is a signed permutation matrix True")


def test_L_is_the_K3_lattice_in_the_chosen_basis():
    line = _line(THETA[1], "     L      rank 22")
    assert "det -1" in line and "even True" in line and "signature (3, 19)" in line


def test_the_involution_is_built_from_named_objects_not_stored():
    script = THETA[0].read_text()
    # the Enriques involution, the reflection in alpha, and the product
    assert "IEn[2, 4] = 1" in script
    assert "w = eye(N) - Rational(2, 1) / q_alpha * alpha * (G * alpha).T" in script
    assert "J = w * IEn" in script and "th = -J" in script
    # and the page states the same three objects
    page = PAGE.read_text()
    assert "\\theta_\\Co = -J_\\Co = -w\\,I_\\En" in page


# --- 2. #81, criterion two: the eigenspaces are the two Coble lattices ------------------


def test_the_two_eigenspaces_carry_the_Coble_invariants():
    line = _line(THETA[1], "     S_Co   rank 11")
    for piece in ("det 2048", "even True", "signature (1, 10)", "coparity delta = 1"):
        assert piece in line, (piece, line)
    line = _line(THETA[1], "     T_Co   rank 11")
    for piece in ("det -2048", "even True", "signature (2, 9)", "coparity delta = 1"):
        assert piece in line, (piece, line)


def test_the_two_eigenspaces_have_rank_eleven_each():
    line = _line(THETA[1], "rank(theta_Co - 1)")
    assert "= 11" in line and "rank(theta_Co + 1) = 11" in line


def test_the_gluing_index_of_the_pair_is_two_to_the_eleven():
    assert _line(THETA[1], "[L : S_Co + T_Co] = 2048 = 2^11")


def test_the_owner_record_agrees_with_this_marking():
    """The provider-based record of #664/#664's marking gives the same invariants."""
    line = _line(OWNER_RECORD, "S_Co = ker(J_Co - 1)")
    assert "rank 11, det 2048, signature (1, 10)" in line
    line = _line(OWNER_RECORD, "T_Co = S_Co^perp:")
    assert "rank 11, det -2048, signature (2, 9)" in line


def test_the_sign_assignment_is_not_a_choice_of_marking():
    text = THETA[1].read_text()
    assert "theta_Co and J_Co are not conjugate" in text
    line = _line(THETA[1], "keep everything and change the U_1 block")
    assert "integral True, involution True, isometry True" in _lines(
        THETA[1], "integral True, involution True, isometry True")[-1]
    assert "pert + rank 11, det 2048" in text
    assert "pert - rank 11, det -2048" in text


# --- 3. A13, the gluing anti-isometry --------------------------------------------------


def test_the_gluing_is_decided_class_by_class():
    decided = _lines(GLUING[1], "solutions 1  equal True")
    assert len(decided) == 11, len(decided)
    assert _line(GLUING[1], "every image is the announced one")


def test_the_gluing_reads_the_diagonal_class_of_w_as_the_antidiagonal_one():
    assert _line(GLUING[1], "->  + e_0/2 + e_1/2")
    assert _line(GLUING[1], "->  + e_2/2 - e_4/2")
    assert _line(GLUING[1], "gamma_Co([alpha/2]) = [beta/2]: True")


def test_the_gluing_vectors_generate_the_K3_lattice():
    assert _line(GLUING[1], "det[s_1..s_11, g_1..g_11] = 1")
    line = _line(GLUING[1], "every gluing vector is a single standard basis vector")
    assert "namely e_0, e_2, e_3, e_6, e_7, e_8, e_9, e_10, e_11, e_12, e_13" in line


def test_the_gluing_is_an_anti_isometry_on_all_2048_classes():
    assert _line(GLUING[1], "q_T(gamma x) + q_S(x) = 0 in Q/2Z for all 2048 classes: True")
    assert _line(GLUING[1], "b_T(gamma x, gamma x') + b_S(x, x') = 0 in Q/Z")


def test_the_gluing_is_block_compatible():
    assert _line(GLUING[1], "which is A_{Delta^-(U)}: True")
    assert _line(GLUING[1], "gamma_Co([alpha/2]) = [beta/2]: True")


def test_the_del_pezzo_vector_and_involution_are_exhibited():
    assert _line(GLUING[1], "t^2 = -1, 2t integral True")
    assert _line(GLUING[1], "J commutes with theta_Co of @thm:theta-co-coordinates: True")


def test_no_other_assignment_is_a_gluing():
    assert _line(GLUING[1], "the sum x + y is integral: False")


# --- 4. A13, the comparison with the Enriques group at delta ---------------------------


def test_the_comparison_is_one_group_and_one_coset():
    assert _line(COMPARISON[1], "[Gamma_{Co,2} : Gamma_{Co,2} cap Orth^+] = 2")
    assert _line(COMPARISON[1], "[Gamma_{Co,2} : Otilde^+(T_Co)] = 1393459200")


def test_the_index_in_the_whole_orthogonal_group_is_evaluated():
    assert _line(COMPARISON[1], "[Orth(T_Co) : Gamma_{Co,2}] = 67456")
    assert _line(COMPARISON[1], "67456, equal to the count")


def test_the_heegner_pair_and_the_reflection_are_in_place():
    assert _line(COMPARISON[1], "delta^2 = -2, zeta^2 = 2, delta.zeta = 0")
    assert _line(COMPARISON[1], "s_zeta fixes S_Co pointwise: True")
    assert _line(COMPARISON[1], "s_zeta lies in ker rho_{T_En}")
    assert _line(COMPARISON[1], "s_zeta acts trivially on A_{T_Co}")


# --- 5. the register row: the polarization classes and the diagram's roots --------------


def test_the_two_polarization_classes_are_one_and_theta_negates_it():
    assert _line(ROOTS[1], "h~_Co = h_En as vectors of lkt: True")
    assert _line(ROOTS[1], "theta_Co(H) = -H: True, and I_Co = -theta_Co(H) = H: True")


def test_the_nineteen_roots_are_the_diagram():
    assert _line(ROOTS[1], "every root has square -2: True")
    assert _line(ROOTS[1], "a tree, hence connected and without cycles: True")
    assert _line(ROOTS[1], "the nineteen roots have rank 18")
    assert _line(ROOTS[1], "the first block is -Cartan(E8) in that order: True")
    assert _line(ROOTS[1], "the second block is -Cartan(E8) in its order: True")


def test_the_involution_realises_the_diagram_reflection():
    assert _line(ROOTS[1], "the pairing is a bijection: True")
    assert _line(ROOTS[1], "it preserves the Gram matrix of the diagram")
    assert _line(ROOTS[1], "its fixed nodes are ['w_9']")
    assert _line(ROOTS[1], "it exchanges the two E8 subdiagrams: True")


def test_the_folded_roots_are_the_cusp_two_diagram():
    line = _line(ROOTS[1], "norms of w_k + w_{18-k}")
    assert "[-4, -4, -4, -4, -4, -4, -4, -4, -2, -4]" in line
    assert _line(ROOTS[1], "the cusp-2 diagram of the page's root table has norms")


def test_the_polarization_meets_exactly_two_roots():
    text = ROOTS[1].read_text().splitlines()
    got = [line.split("=")[-1].strip() for line in text
           if line.strip().startswith("H.w_") and "for Phi" not in line]
    assert got.count("1") == 2, got
    assert got.count("0") == 17, got
    assert _line(ROOTS[1], "delta.w_k = 0 for every root of Phi: True")


# --- 6. the pages state what the records decide ----------------------------------------


def test_the_page_carries_the_four_theorems():
    page = PAGE.read_text()
    for anchor in ("#thm:theta-co-coordinates", "#thm:gamma-co-coordinates",
                   "#thm:gamma-co-2-comparison", "#thm:diagram-roots-coordinates"):
        assert anchor in page, anchor


def test_the_page_carries_the_displays_the_records_decide():
    page = PAGE.read_text()
    for display in ("\\Theta =" , "e_0+e_1,\\; e_2-e_4", "e_0-e_1,\\; e_2+e_4",
                    "= 67\\,456", "(-4^{\\times 8},-2,-4)",
                    "w_{10} = \\tilde\\omega_8+e_2"):
        assert display in page, display


def test_the_register_item_is_closed_and_the_conjecture_is_replaced():
    text = OPEN_PROBLEMS.read_text()
    assert "#qst:coble-embedding-matrices" in text
    assert "the matrices of the chain of primitive embeddings" in text
    assert "Write the polarization classes" not in text
    assert "conj:horizontal-folding" not in text
    assert "The horizontal folding involution, resolved" in text
    assert "theta_\\Co(H) = H$, and that is false" in text


# --- 7. the reusable part: the records reproduce ---------------------------------------


def _body(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("1. "):
            return lines[i:]
    raise AssertionError("the record has no numbered section '1.'")


def test_the_four_records_reproduce_from_their_scripts():
    for script, record in RECORDS:
        run = subprocess.run([sys.executable, str(script)], capture_output=True,
                             text=True, timeout=900, cwd=str(ROOT))
        assert run.returncode == 0, (script.name, run.stderr[-2000:])
        fresh, committed = _body(run.stdout), _body(record.read_text())
        assert fresh == committed, "%s does not reproduce its transcript" % script.name
