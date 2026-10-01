"""The records and the morphism files satisfy every equation that Tables 10.2 and 10.3 of Hashimoto state, and a false transcription or a missing embedding is refused."""

from pathlib import Path

import pytest
from latticedb import corpus, hashimoto

REPOSITORY = Path(__file__).resolve().parent.parent
LOADED = corpus.load(REPOSITORY)
LATTICES = {entry.lattice.tag: entry.lattice for entry in LOADED.entries}
HELD = corpus.held(LOADED)
GROUPS, INVARIANTS = hashimoto.stored(REPOSITORY / "sources" / "hashimoto")


def test_the_records_satisfy_tables_10_2_and_10_3() -> None:
    assert hashimoto.check(GROUPS, INVARIANTS, LATTICES, HELD) == []


def test_the_group_of_a_genus_symbol_is_the_sum_of_its_cyclic_factors() -> None:
    assert hashimoto.symbol_group("2_II^{-2}, 8_1^{+1}, 5^{-1}") == [2, 2, 5, 8]


@pytest.mark.parametrize(
    ("n", "change", "expected"),
    [
        # Row 81 states |q| = 160; 161 is not the determinant of the record of Lambda_G.
        (81, {"discriminant_order": 161}, "Table 10.2 row 81"),
        # Row 81 states c = 19; Lambda^G has rank 22 - c = 3, so c = 18 contradicts both tables.
        (81, {"rank": 18}, "Table 10.3 row 81"),
        # Row 64 points to row 81; row 80 has |q| = 256, not the |q| = 160 of row 64.
        (64, {"shares": 80}, "Table 10.2 row 64"),
    ],
)
def test_a_false_row_of_table_10_2_is_refused(n: int, change: dict[str, int], expected: str) -> None:
    groups = tuple(row.model_copy(update=change) if row.n == n else row for row in GROUPS)
    assert any(expected in problem for problem in hashimoto.check(groups, INVARIANTS, LATTICES, HELD))


def test_a_basis_that_is_not_an_isometry_is_refused() -> None:
    row = INVARIANTS[-1]
    (printed,) = row.lattices
    swapped = printed.model_copy(update={"twist": -printed.twist})
    invariants = (*INVARIANTS[:-1], row.model_copy(update={"lattices": (swapped,)}))
    assert any("P is not an isometry" in problem for problem in hashimoto.check(GROUPS, invariants, LATTICES, HELD))


def test_the_invariant_and_coinvariant_lattices_of_row_81_are_orthogonal_complements_in_the_k3_lattice() -> None:
    assert hashimoto.complements(("02AP", 2), ("02AQ", -1), LATTICES["027E"], HELD)
    # The scale of each stored embedding is the twist of Tables 10.2 and 10.3; another twist names another lattice.
    assert not hashimoto.complements(("02AP", -2), ("02AQ", -1), LATTICES["027E"], HELD)
    # The stored embedding of the invariant lattice of row 80, also of rank 3, is not orthogonal to the stored embedding of the coinvariant lattice of row 81.
    assert not hashimoto.complements(("02AO", 4), ("02AQ", -1), LATTICES["027E"], HELD)


def test_a_row_without_its_embeddings_in_the_k3_lattice_is_refused() -> None:
    held = {pair: morphisms for pair, morphisms in HELD.items() if pair != ("02AQ", "027E")}
    problems = hashimoto.check(GROUPS, INVARIANTS, LATTICES, held)
    assert problems == ["Table 10.3 row 81: the morphism files hold no primitive orthogonal embeddings of 02AP(2) and 02AQ(-1) in 027E"]
