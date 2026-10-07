"""Source-intake collation for Tables 10.2 and 10.3 of Hashimoto.

These tests exercise the importer/comparator against the archived transcription.
They are provenance checks, not mathematical certification of lattice records.
"""

from pathlib import Path

import frontmatter

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import hashimoto
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent.parent
ZZ = session_ring_objects()["ZZ"]


def _lattice(tag: str) -> Lattice:
    return Lattice.model_validate(
        frontmatter.load(str(REPOSITORY / "lattices" / f"{tag}.md")).metadata
    )


def _held(source: str, target: str):
    return tuple(
        (morphism.matrix, morphism.scale)
        for morphism in _lattice(source).morphisms
        if morphism.target == target
    )


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


def test_row_81_change_of_basis_lands_on_the_seeded_lattice_card() -> None:
    _, invariants = hashimoto.stored(REPOSITORY / "sources" / "hashimoto")
    printed = next(item for item in invariants if item.n == 81).lattices[0]
    source = Lattices(ZZ)(printed.gram_tensor)
    target = Lattices(ZZ)(_lattice(printed.record).gram_tensor).twist(printed.twist)
    assert hashimoto.basis_gives_isometry(source, target, printed.basis)


def test_row_81_embeddings_were_seeded_as_orthogonal_primitive_complements() -> None:
    held = {
        ("02AP", "027E"): _held("02AP", "027E"),
        ("02AQ", "027E"): _held("02AQ", "027E"),
    }
    assert hashimoto.complements(
        ("02AP", 2), ("02AQ", -1), _lattice("027E"), held
    )
