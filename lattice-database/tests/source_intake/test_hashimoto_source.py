"""Source-intake collation for Tables 10.2 and 10.3 of Hashimoto.

These tests exercise the importer/comparator against the archived transcription.
They are provenance checks, not mathematical certification of lattice records.
"""

from pathlib import Path

from latticedb import hashimoto

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def test_row_81_and_its_shared_rows_are_read_from_the_stored_tables() -> None:
    groups, invariants = hashimoto.stored(REPOSITORY / "sources" / "hashimoto")
    by_n = {row.n: row for row in groups}
    row = by_n[81]
    assert (row.order, row.discriminant_order, row.rank) == (960, 160, 19)
    assert row.coinvariant is not None
    assert (row.coinvariant.record, row.coinvariant.twist) == ("02AQ", -1)
    assert by_n[64].shares == 81
    assert by_n[73].shares == 81
    invariant = next(item for item in invariants if item.n == 81)
    assert len(invariant.lattices) == 1
    printed = invariant.lattices[0]
    assert (printed.record, printed.twist) == ("02AP", 2)
