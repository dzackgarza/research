"""Bounded source-intake checks for the Höhn--Mason ancillary file.

These tests exercise one representative importer path. They are provenance
checks, not mathematical certification of lattice records.
"""

from pathlib import Path

from latticedb import hoehn_mason

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def test_row_81_entry_is_read_from_the_stored_ancillary_file() -> None:
    leech, entries = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")
    entry = next(item for item in entries if item.row == 81)
    assert (entry.i, entry.j, entry.record, entry.twist) == (5, 5, "02AQ", 1)
    assert leech.record == "028S"
    assert len(entry.stabilizer_generators) == 4
