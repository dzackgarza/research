"""Bounded source-intake checks for the Höhn--Mason ancillary file.

These tests exercise one representative importer path. They are provenance
checks, not mathematical certification of lattice records.
"""

from pathlib import Path

import frontmatter

from latticedb import hoehn_mason
from latticedb.model import Morphisms

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def _morphisms(source: str, target: str) -> Morphisms:
    return Morphisms.model_validate(
        frontmatter.load(
            str(REPOSITORY / "morphisms" / f"{source}-{target}.md")
        ).metadata
    )


def test_row_81_entry_is_read_from_the_stored_ancillary_file() -> None:
    leech, entries = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")
    entry = next(item for item in entries if item.row == 81)
    assert (entry.i, entry.j, entry.record, entry.twist) == (5, 5, "02AQ", 1)
    assert leech.record == "028S"
    assert len(entry.stabilizer_generators) == 4


def test_row_81_source_generators_are_the_seeded_self_isometries() -> None:
    leech, entries = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")
    entry = next(item for item in entries if item.row == 81)
    computed = hoehn_mason.automorphisms(leech, entry)
    held = _morphisms(entry.record, entry.record)
    seeded = {(morphism.matrix, morphism.scale) for morphism in held.morphisms}
    assert all((matrix, 1) in seeded for matrix in computed)
    assert hoehn_mason.group_order(computed) == 960


def test_row_81_source_inclusion_is_the_seeded_leech_embedding() -> None:
    leech, entries = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")
    entry = next(item for item in entries if item.row == 81)
    held = _morphisms(entry.record, leech.record)
    seeded = {(morphism.matrix, morphism.scale) for morphism in held.morphisms}
    assert (hoehn_mason.embedding(leech, entry), entry.twist) in seeded
