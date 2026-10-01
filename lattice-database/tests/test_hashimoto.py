"""The records of the corpus satisfy every equation that Tables 10.2 and 10.3 of Hashimoto state, and a false transcription is refused."""

from pathlib import Path

import pytest
from latticedb import corpus, hashimoto

REPOSITORY = Path(__file__).resolve().parent.parent
LATTICES = {entry.lattice.tag: entry.lattice for entry in corpus.load(REPOSITORY).entries}
GROUPS, INVARIANTS = hashimoto.stored(REPOSITORY / "sources" / "hashimoto")


def test_the_records_satisfy_tables_10_2_and_10_3() -> None:
    assert hashimoto.check(GROUPS, INVARIANTS, LATTICES) == []


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
    assert any(expected in problem for problem in hashimoto.check(groups, INVARIANTS, LATTICES))


def test_a_basis_that_is_not_an_isometry_is_refused() -> None:
    row = INVARIANTS[-1]
    (printed,) = row.lattices
    swapped = printed.model_copy(update={"twist": -printed.twist})
    invariants = (*INVARIANTS[:-1], row.model_copy(update={"lattices": (swapped,)}))
    assert any("P is not an isometry" in problem for problem in hashimoto.check(GROUPS, invariants, LATTICES))
