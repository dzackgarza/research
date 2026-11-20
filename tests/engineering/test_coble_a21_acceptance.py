"""Acceptance gate for research#664 (A21), item 1: the two overlattices inside one copy of L_K3.

The item, as the issue states it, is a computation record rather than a page statement:

  "constructs L_K3 = 3U + 2E8(-1) and the four summand lattices with their Gram data and
   source invariants ..., then realises both primitive embeddings inside one copy of L_K3
   through `overlattice`/`even_overlattice_inclusions`: the S_Co + T_Co overlattice of index
   2048 and the S_En + T_En overlattice of index 1024, verifying unimodularity, evenness,
   signature (3,19), isometry to II_{3,19}, the index against the discriminant orders, and the
   complement identities (T_Co = S_Co^perp, T_En = S_En^perp of rank 12) by rank and
   determinant.  The record states what it does not build: delta with delta^perp = T_Co (#279)
   and gamma as the morphism induced by the embedding (#276), and prints the glue subgroup as
   the graph of an anti-isometry so that #276's object is isolated."

The record is `computations/reports/coble_a21-embedding-build.py`, its transcript
`computations/reports/coble_a21-embedding-build-run.txt`, run in the adopted runtime
(Sage 11.0.beta5) against sage-extensions main `1488acf`.  These tests read the archived
transcript and the script: they decide the item and do not re-run the container.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "computations/reports/coble_a21-embedding-build.py"
RECORD = ROOT / "computations/reports/coble_a21-embedding-build-run.txt"


def _line(marker):
    """The single line of the transcript that carries `marker`."""
    hits = [line for line in RECORD.read_text().splitlines() if marker in line]
    assert len(hits) == 1, (marker, hits)
    return hits[0]


def _lines(marker):
    return [line for line in RECORD.read_text().splitlines() if marker in line]


def test_the_record_exists_and_carries_its_provenance():
    text = RECORD.read_text()
    assert "1488acf" in text, "the provider pin must be in the record"
    assert "Sage 11.0.beta5" in text
    assert "L_K3 = 3U + 2E8(-1) = II_{3,19}" in text


def test_L_K3_is_built_and_unimodular_of_signature_3_19():
    line = _line("rank 22, determinant -1")
    assert "even True" in line and "signature (3, 19)" in line


def test_the_four_summands_carry_their_rank_determinant_and_signature():
    want = {
        "S_Co": ("rank 11", "det   2048", "sig (1, 10)"),
        "T_Co": ("rank 11", "det  -2048", "sig (2, 9)"),
        "S_En": ("rank 10", "det  -1024", "sig (1, 9)"),
        "T_En": ("rank 12", "det   1024", "sig (2, 10)"),
    }
    for name, pieces in want.items():
        line = next(l for l in RECORD.read_text().splitlines()
                    if l.strip().startswith(name) and "rank" in l)
        for piece in pieces:
            assert piece in line, (name, piece, line)
        assert "even True" in line


def test_the_Gram_data_of_all_four_summands_is_printed():
    assert len(_lines("Gram matrix in the embedding's basis")) == 4


def test_each_summand_is_isometric_to_the_type_its_source_fixes():
    for name in ("S_Co", "T_Co", "S_En"):
        assert _line("isometric to the abstract %s: True" % name)
    assert _line("isometric to U + U(2) + E8(-2): True")


def test_the_complement_identities_hold_by_rank_and_determinant():
    line = _line("rank S_Co = 11, rank T_Co = 11, sum = 22 = rank L_K3")
    assert "2048 . -2048 = -4194304" in line
    line = _line("rank S_En = 10, rank T_En = 12, sum = 22 = rank L_K3")
    assert "-1024 . 1024 = -1048576" in line


def test_both_overlattices_have_the_recorded_index_and_invariants():
    for index in (2048, 1024):
        line = _line("overlattice: index %d;" % index)
        assert "det -1" in line and "even True" in line
        assert "sig (3, 19)" in line and "unimodular True" in line
    assert len(_lines("isometric to L_K3 = II_{3,19}: True")) == 2


def test_the_index_equals_the_discriminant_order():
    assert _line("index / |A_S| = 2048 / 2048 = 1")
    assert _line("index / |A_S| = 1024 / 1024 = 1")


def test_the_glue_is_the_graph_of_an_anti_isometry_on_all_classes():
    for size in (2048, 1024):
        assert _line("the glue subgroup of A_{S+T}: %d classes" % size)
        assert _line("the projection of the glue to A_S is injective: True (%d distinct images)"
                     % size)
        assert _line("q_S(x) + q_T(gamma x) = 0 on all %d glue classes: True" % size)
    assert len(_lines("b_S(x,y) + b_T(gamma x, gamma y) = 0 in Q/Z")) == 2


def test_the_construction_goes_through_the_owners_operations():
    script = SCRIPT.read_text()
    assert "overlattice(*classes)" in script
    assert "divided_discriminant_class" in script
    assert "primitive_sublattice_from" in script and "orthogonal_complement" in script
    assert "is_isometric_to" in script


def test_the_record_names_the_two_operations_it_does_not_use():
    text = RECORD.read_text()
    assert "sage-extensions#279" in text and "vectors_of_square_with_complement" in text
    assert "sage-extensions#276" in text and "gluing_anti_isometry" in text
    assert "even_overlattice_inclusions" in text
