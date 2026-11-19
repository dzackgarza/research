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
    computations/reports/coble_a13-chain-matrices-run.txt           the chain's matrices
    computations/reports/coble_explicit-sextic-run.txt              the sextic

and the construction research#81 asks for, which needs the Sage image, is
computations/reports/coble_a13-library-construction.py with its transcript; its reproduction
test runs under the Sage interpreter and skips, naming the reason, where there is none.

These tests read those transcripts and the two pages, and the last one re-runs the four scripts
and requires the committed transcripts to be reproduced line for line from the first numbered
section on.  That is the reusable part: every number below is re-derived, in seconds, from the
marking alone -- no provider, no container, no network.

Run it with

    python3 -m pytest tests/engineering/test_coble_a13_acceptance.py \
        -q -o addopts="" --confcutdir=tests/engineering

The two overrides are for a bare interpreter: `-o addopts=""` drops the project's addopts, which
require pytest-timeout and pytest-reportlog, and `--confcutdir` keeps tests/conftest.py out of the
run, that file importing dzack_research, whose install would pull pandoc-config, sage-extensions
and streamlit for a test that needs only sympy.

No workflow file of its own is needed.  The gate that runs on every push and pull request
(.github/workflows/development.yml) delegates to ai-review-ci's sage profile, whose
_sage-pytest-coverage collects every tests/**/test_*.py outside tests/acceptance/ and the QC
exclusions -- this file among them, as ai-review-ci's _sage-python-test-files prints -- and runs
it under the Sage interpreter with the project's own conftest and pytest configuration.  Nothing
here touches the sage image beyond that.  The explicit ubuntu-latest job prepared for this one
file was withdrawn: it repeats a run the gate already carries, and a push adding a file under
.github/workflows/ is refused without `workflows` permission, which is the refusal GitHub gave
for it.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

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
LIBRARY = (REPORTS / "coble_a13-library-construction.py",
           REPORTS / "coble_a13-library-construction-run.txt")
CHAIN = (REPORTS / "coble_a13-chain-matrices.py",
         REPORTS / "coble_a13-chain-matrices-run.txt")
SEXTIC = (REPORTS / "coble_explicit-sextic.py",
          REPORTS / "coble_explicit-sextic-run.txt")
RECORDS = (THETA, GLUING, COMPARISON, ROOTS, CHAIN, SEXTIC)


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
    # the A13 register question is now a remark pointing at the two theorems
    assert "The embedding matrices of the chain" in text
    assert "The folding conjecture for $\\theta_\\Co$, resolved" in text
    # the ids the question and the conjecture had are gone
    for gone in ("qst:coble-embedding-matrices", "qst:coble-explicit-equations",
                 "conj:horizontal-folding"):
        assert gone not in text, gone
    # and the two questions they asked are theorems
    assert "#thm:chain-matrices" in text or "thm:chain-matrices" in text
    assert "#thm:coble-explicit-sextic" in text
    # the falsified clause is recorded as falsified, with its reason
    assert "theta_\\Co(H) = H$, and that is false" in text


# --- 7. the reusable part: the records reproduce ---------------------------------------


STAMP = re.compile(r"^\s*\[\s*\d+\.\ds\]")


def _body(text):
    """The transcript from its first numbered section on, without the timing stamps.

    The two provider-based records (this issue's library construction and the A20/A21 record
    beside it) print an elapsed-time stamp per stage; those cannot reproduce and carry no
    mathematical content, so they are dropped before comparing.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("1. "):
            return [line for line in lines[i:] if not STAMP.match(line)]
    raise AssertionError("the record has no numbered section '1.'")


def test_the_six_records_reproduce_from_their_scripts():
    for script, record in RECORDS:
        run = subprocess.run([sys.executable, str(script)], capture_output=True,
                             text=True, timeout=900, cwd=str(ROOT))
        assert run.returncode == 0, (script.name, run.stderr[-2000:])
        fresh, committed = _body(run.stdout), _body(record.read_text())
        assert fresh == committed, "%s does not reproduce its transcript" % script.name


def test_the_library_construction_record_reproduces_under_sage():
    """The #81 construction, re-run in the interpreter that has the library.

    The QC gate's sage-tests step (_sage-pytest-coverage) runs this suite under the Sage
    interpreter, where the imports below resolve and this test runs; a plain CPython without
    Sage skips it, loudly, rather than passing it silently.
    """
    try:
        import sage.all  # noqa: F401
        import sage_extensions  # noqa: F401
    except Exception as exc:                                   # pragma: no cover
        pytest.skip("needs the Sage image and sage-extensions, absent from this interpreter "
                    "(%s: %s); the QC gate's sage-tests step runs this test under Sage"
                    % (type(exc).__name__, exc))
    run = subprocess.run([sys.executable, str(LIBRARY[0])], capture_output=True,
                         text=True, timeout=1800, cwd=str(ROOT))
    assert run.returncode == 0, (LIBRARY[0].name, run.stderr[-3000:])
    assert _body(run.stdout) == _body(LIBRARY[1].read_text()), \
        "%s does not reproduce its transcript" % LIBRARY[0].name


def test_the_library_construction_record_exists_with_its_transcript():
    """The #81 construction record needs the Sage image, so it is checked here, not re-run."""
    assert LIBRARY[0].exists() and LIBRARY[1].exists()
    text = LIBRARY[0].read_text()
    for call in ("L.O()", "L.reflection(", "primitive_sublattice_from(", "kernel()",
                 "orthogonal_complement(", "lattice_of(", "indefinite_isometry(",
                 "gluing_anti_isometry("):
        assert call in text, call
    record = LIBRARY[1].read_text()
    assert "sage-extensions imported from" in record and "sage-extensions at:" in record
    for marker in ("S_Co is isometric to I_{1,10}(2) = <2> + <-2>^10",
                   "T_Co is isometric to <2> + U(2) + E8(2)",
                   "the glue subgroup of A_{S_Co + T_Co} has order 2048"):
        assert marker in record, marker


def test_the_construction_records_no_failed_self_check():
    """#656: the record must not print a property as false beside its own claim that all hold.

    A revision of this record compared the arrow ``-(w . I_En)``, which is an arrow of the
    underlying free-module category and not of ``O(L)``, with the identity of ``O(L)``, and
    printed ``theta_Co^2 = 1: False`` immediately above a line asserting that every check
    held.  The order-two equation is now decided inside ``O(L)`` and again on the standard
    basis, both are asserted in the script, and the transcript of a record whose checks are
    asserts carries no failed one.
    """
    record = LIBRARY[1].read_text()
    assert "False" not in record, [line for line in record.splitlines() if "False" in line]
    assert "theta_Co^2 = 1, the library decision inside O(L): True" in record
    assert "theta_Co(v) = -J_Co(v) on all 22 basis vectors: True" in record
    script = LIBRARY[0].read_text()
    assert "assert theta * theta == L.O().one()" in script
    assert "assert all(theta(L.basis_vector(i)) == -J_Co(L.basis_vector(i)) for i in range(n))" in script


def test_the_eigenspaces_are_matched_by_exhibited_isometries():
    """#81 criterion two: an isometry, exhibited and checked, not the boolean of one existing.

    The five identifications print a matrix ``M`` and check ``M^T G M = G`` entry by entry,
    and each image is compared with the named sublattice in L, so the identification is a map
    onto the eigenspace itself and not only onto an isometric copy of it.
    """
    record = LIBRARY[1].read_text()
    assert record.count("satisfies M^T G M = G entry by entry: True") == 5, record.count(
        "satisfies M^T G M = G entry by entry: True")
    for name in ("S_Co", "T_Co", "T_En", "T_dP", "S_dP"):
        assert "so the image is %s itself: True" % name in record, name
        assert "images in L lie in %s: True" % name in record, name
    assert "T_Co = S_Co^perp through L.orthogonal_complement" in record
    assert "embedded sublattices of L are equal and not only isometric" in record


def test_the_page_states_the_E8_2_block_by_its_own_Gram_matrix():
    """The block is 2 . (-Cartan(E8)) of determinant 2^8, not the diagonal lattice <-4>^8."""
    page = PAGE.read_text()
    assert "\\mathrm{diag}(-4^{\\times8})" not in page
    assert "$-2\\,\\mathrm{Cartan}(E_8)$, of diagonal entries $-4$ and off-diagonal entries $0$ or $2$" in page
    assert "the two cross terms vanish because $E_{8,1}$ and $E_{8,2}$ are orthogonal" in page
    assert "not the diagonal lattice $\\generators{-4}^{8}$, whose determinant is $4^8$" in page


def test_the_conjugacy_proof_composes_maps_of_matching_domains():
    """The composite must be an isometry of q_{T'}, and the corrected isometry must enter it."""
    page = PAGE.read_text()
    assert "\\eta_0\\definedas\\bar\\varphi^{-1}\\gamma\\bar\\psi\\gamma'^{-1}" in page
    assert "\\bar\\varphi_1\\gamma' = \\bar\\varphi\\,\\bar\\varphi^{-1}\\gamma\\bar\\psi = \\gamma\\bar\\psi" in page
    assert "The composite $\\gamma\\,\\bar\\psi^{-1}\\,\\gamma'^{-1}$ is an isometry of $q_{T'}$" not in page


def test_the_AEGS25_lemma_is_cited_at_its_printed_page():
    """Lemma 3.9 is printed on p. 594; its neighbours, Def. 3.7 and Lemma 3.8, are on p. 593."""
    for path in (PAGE, OPEN_PROBLEMS):
        text = path.read_text()
        assert "Lemma 3.9, printed p. 593" not in text, path.name
        assert "Lemma 3.9, printed p. 594" in text, path.name


def test_every_citation_of_the_folding_lemma_carries_its_printed_page():
    """The rule the last review applied to two pages, applied to all of them.

    AEGS25's Lemma 3.9 is printed on p. 594, and a page that cites it without the page leaves
    the reader with a statement the source does not carry there.  Two pages outside this
    issue's own files cited it bare, so the check reads every page and not only those two.
    """
    missing = []
    for path in sorted((ROOT / "writing").rglob("*.md")):
        if ".book" in path.parts:
            continue
        if path.name == "annotated-bibliography.md":
            # An index of the deposited PDF: its "p. N" is the PDF's own page, matched by the
            # #page=N of its link, and it states nothing.  Its AEGS25 entries are consistent
            # with that convention -- "Definition 2.3, p. 6" is PDF p. 6, printed p. 586.
            continue
        for number, line in enumerate(path.read_text(errors="ignore").splitlines(), 1):
            if "AEGS25" not in line:
                continue
            # "Lemma 3.9", and the plural spellings a bare citation hides behind.
            if not re.search(r"Lemmas? 3\.9|Lems\. 3\.9", line):
                continue
            if "printed p" not in line or "594" not in line:
                missing.append("%s:%d" % (path.relative_to(ROOT), number))
    # The records cite the source too, and a transcript is what a reader checks a page against:
    # the diagram-roots record carried the refuted page in its script and in its committed
    # transcript while every Markdown page was right, so the scan reads the records as well.
    for path in sorted(REPORTS.glob("*")):
        if path.suffix not in (".py", ".txt"):
            continue
        for number, line in enumerate(path.read_text(errors="ignore").splitlines(), 1):
            if "Lemma 3.9" in line and "printed p. 594" not in line:
                missing.append("%s:%d" % (path.relative_to(ROOT), number))
    assert not missing, missing


def _theta_on(coordinates):
    """$\\theta_\\Co$ of @thm:theta-co-coordinates on a half-integral 22-vector.

    The action on the standard basis is the signed permutation of that theorem:
    e_0 <-> e_1, e_2 -> -e_4, e_4 -> -e_2, e_3 -> -e_5, e_5 -> -e_3, e_{6+k} -> -e_{14+k},
    e_{14+k} -> -e_{6+k}.  Exact, with Fractions, so a half-integral vector is allowed.
    """
    out = {}
    for index, value in coordinates.items():
        if index in (0, 1):
            image, sign = 1 - index, 1
        elif index in (2, 4):
            image, sign = 6 - index, -1
        elif index in (3, 5):
            image, sign = 8 - index, -1
        elif 6 <= index <= 13:
            image, sign = index + 8, -1
        else:
            image, sign = index - 8, -1
        out[image] = out.get(image, 0) + sign * value
    return {index: value for index, value in out.items() if value}


def test_the_image_of_b_under_theta_is_b_minus_H_and_not_H_minus_b():
    """One lemma, with its hypotheses: $H = e_2+e_3+e_4+e_5$, $b = -e_2+2e_4+e_5-e_6+e_{14}$.

    In the marking of @thm:theta-co-coordinates $\\theta_\\Co$ is $-\\id$ on $S_\\Co$ and
    $\\id$ on $T_\\Co$, so it fixes $H$'s sign and fixes $t = b-H/2$; hence
    $\\theta_\\Co(b) = -H/2+t = b-H$.  The theorem's proof printed $H-b$ in place of $b-H$,
    and $H-b = -\\theta_\\Co(b)$ is a different vector.  The probe below is the exact
    computation; the two page assertions then hold the proof to it.
    """
    from fractions import Fraction

    H = {2: 1, 3: 1, 4: 1, 5: 1}
    b = {2: -1, 4: 2, 5: 1, 6: -1, 14: 1}

    def shift(left, right):
        out = dict(left)
        for index, value in right.items():
            out[index] = out.get(index, 0) - value
        return {index: value for index, value in out.items() if value}

    theta_b = _theta_on(b)
    b_minus_H = shift(b, H)
    H_minus_b = shift(H, b)
    assert theta_b == b_minus_H, (theta_b, b_minus_H)
    assert theta_b != H_minus_b, (theta_b, H_minus_b)
    # the hypotheses the lemma uses: H^2 = 4, b^2 = 0, H.b = 2 in the form of lkt
    E8_EDGES = {(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)}

    def pairing(x, y):
        total = Fraction(0)
        for index, value in x.items():
            for other, weight in y.items():
                if index in (0, 1) or other in (0, 1):
                    gram = 1 if {index, other} == {0, 1} else 0
                elif index < 6 and other < 6:
                    gram = 1 if {index, other} in ({2, 3}, {4, 5}) else 0
                elif 6 <= index <= 13 and 6 <= other <= 13:
                    a, c = index - 6, other - 6
                    gram = -2 if a == c else (1 if (min(a, c), max(a, c)) in E8_EDGES else 0)
                elif 14 <= index <= 21 and 14 <= other <= 21:
                    a, c = index - 14, other - 14
                    gram = -2 if a == c else (1 if (min(a, c), max(a, c)) in E8_EDGES else 0)
                else:
                    gram = 0
                total += value * weight * gram
        return total

    assert pairing(H, H) == 4 and pairing(b, b) == 0 and pairing(H, b) == 2

    page = PAGE.read_text()
    assert r"\theta_\Co(b) = -H/2+t = b-H" in page
    assert r"\theta_\Co(b) = -H/2+t = H-b" not in page


def test_every_AEGS25_statement_cited_on_these_pages_carries_its_printed_page():
    """A statement of the source is cited by number *and* by the page that carries it.

    The rule was applied to the folding lemmas first, one page at a time; this is the same rule
    over every numbered statement the pages of this issue cite from AEGS25, and it also refuses
    the id form ``[@AEGS25, def:involutions]``, which names nothing the source prints.
    """
    pages = [PAGE,
             ROOT / "writing/coble/lattices-and-moduli/lattices.md",
             ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md",
             OPEN_PROBLEMS,
             ROOT / "writing/coble/coble-moduli/cusp-correspondence-morphism-chain.md",
             ROOT / "writing/coble/computations/sterk-root-counts-and-computed-chambers.md"]
    statement = re.compile(r"(Def\.|Definition|Lem\.|Lemmas?|Lems\.|Thm\.|Theorem|Props?\.|Propositions?|Cor\.|Corollary)")
    bad = []
    for path in pages:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            for match in re.finditer(r"\[@AEGS25[^\]]*\]", line):
                citation = match.group(0)
                if statement.search(citation) and "printed p" not in citation:
                    bad.append("%s:%d %s" % (path.name, number, citation))
                if re.search(r"\b(def|thm|lem|prop|cor):", citation):
                    bad.append("%s:%d %s" % (path.name, number, citation + "  -- an id, not a statement"))
    assert not bad, bad


def test_the_records_cite_the_pages_verified_against_the_deposited_sources():
    """Every page attribution the A13 records make, pinned to the page it was verified on.

    The pages were read off the deposited copies in tmp/sources on 2026-11-19, by printed
    number, and each names what stands there; a later edit that moves a number breaks this
    test rather than the attribution.

      Alexeev--Engel--Garza--Schaffler, Nagoya Math. J. 259 (2025) 581--624, deposited as
      aegs-2025-compact-moduli-of-enriques-surfaces-of-degree-2.pdf:
        Definition 2.3, printed p. 586 -- the three involutions I_dP, I_En, I_Nik;
        Lemma 3.9, printed p. 594 -- the reflection alpha_k -> alpha_{20-k};
        Figure 7, printed p. 594 -- the folded diagram of cusp 2.
      Nikulin, Math. USSR Izv. 14 (1980) 103--167:
        Theorem 3.6.2, printed p. 144 -- the genus of an even 2-elementary lattice.
      Bourbaki, Lie Groups and Lie Algebras, Ch. 4--6:
        Ch. VI Sec. 4, printed p. 208 -- "of nodes and bonds in the following way".
    """
    records = "".join(path.read_text(errors="ignore") for path in sorted(REPORTS.glob("coble_a13-*"))
                      if path.suffix in (".py", ".txt"))
    for citation in ("Def. 2.3, printed p. 586", "Lemma 3.9, printed p. 594",
                     "Fig. 7, printed p. 594", "Thm. 3.6.2, printed p. 144"):
        assert citation in records, citation
    audit = (REPORTS / "coble_a13-audit-record.txt").read_text()
    assert "Ch. VI Sec. 4, printed p. 208" in audit


def test_the_group_the_question_names_is_the_one_the_theorem_computes():
    """A13 asks for the comparison to $\\Gamma^\\En_\\Co(\\delta)$; the book must name it.

    The symbol stands for the image of the stabilizer of the Heegner vector in the degree-two
    Enriques group, which is the group the book writes $\\Gamma_{\\Co,2}$.  Unless the definition
    gives the symbol and the comparison states the identity, a reader sent to
    @thm:gamma-co-2-comparison cannot recognise the object A13 names.
    """
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text()
    assert r"\Gamma^{\En}_\Co(\delta)" in lattices
    page = PAGE.read_text()
    assert (r"\Gamma_{\Co,2} = \Gamma^{\En}_\Co(\delta) = "
            r"\Gamma^{\mathrm{cong}}_{\Co,2}") in page


def test_no_page_still_carries_the_open_form_of_the_question():
    """#656's acceptance: every page that cites the open form is updated."""
    moduli = (ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md").read_text()
    assert "What is an explicit description of $\\Gamma_{\\Co, 2}$?" not in moduli
    assert '\\arrow[d, "?"\']' not in moduli
    assert "The map $F_{\\Co,2}\\to \\fco$" not in moduli
    assert "The vertical map is $F_{\\Co}\\to F_{\\Co,2}$" in moduli
    assert "The group $\\Gamma_{\\Co,2}$, explicitly" in moduli
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text()
    assert "The proof does not evaluate that index" not in lattices
    page = PAGE.read_text()
    assert "states but leaves unevaluated" not in page
