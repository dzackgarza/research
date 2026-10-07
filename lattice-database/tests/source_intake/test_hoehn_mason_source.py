"""Bounded source-intake checks for the Höhn--Mason ancillary file.

These tests exercise one representative importer path. They are provenance
checks, not mathematical certification of lattice records.
"""

from pathlib import Path

import frontmatter

from latticedb import hoehn_mason
from latticedb.model import Lattice, Morphism

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def _lattice(tag: str) -> Lattice:
    return Lattice.model_validate(
        frontmatter.load(str(REPOSITORY / "lattices" / f"{tag}.md")).metadata
    )


def _morphisms(source: str, target: str) -> tuple[Morphism, ...]:
    return tuple(
        morphism for morphism in _lattice(source).morphisms if morphism.target == target
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
    record = _lattice(entry.record)
    computed = hoehn_mason.automorphisms(leech, entry, record)
    held = _morphisms(entry.record, entry.record)
    seeded = {(morphism.matrix, morphism.scale) for morphism in held}
    assert all((matrix, 1) in seeded for matrix in computed)
    assert hoehn_mason.group_order(record, computed) == 960


def test_row_81_source_inclusion_is_the_seeded_leech_embedding() -> None:
    leech, entries = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")
    entry = next(item for item in entries if item.row == 81)
    held = _morphisms(entry.record, leech.record)
    seeded = {(morphism.matrix, morphism.scale) for morphism in held}
    computed = hoehn_mason.embedding(
        leech, entry, _lattice(leech.record), _lattice(entry.record)
    )
    assert (computed, entry.twist) in seeded
