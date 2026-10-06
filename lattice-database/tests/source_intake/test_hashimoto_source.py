"""Source-intake collation for Tables 10.2 and 10.3 of Hashimoto.

These tests exercise the importer/comparator against the archived transcription.
They are provenance checks, not mathematical certification of lattice records.
"""

from pathlib import Path

import frontmatter
from flint import fmpz_mat

from latticedb import hashimoto
from latticedb.model import Lattice, Morphisms

REPOSITORY = Path(__file__).resolve().parent.parent.parent


def _lattice(tag: str) -> Lattice:
    return Lattice.model_validate(
        frontmatter.load(str(REPOSITORY / "lattices" / f"{tag}.md")).metadata
    )


def _held(source: str, target: str) -> tuple[tuple[tuple[tuple[int, ...], ...], int], ...]:
    record = Morphisms.model_validate(
        frontmatter.load(
            str(REPOSITORY / "morphisms" / f"{source}-{target}.md")
        ).metadata
    )
    return tuple((morphism.matrix, morphism.scale) for morphism in record.morphisms)


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
    card = _lattice(printed.record)
    basis = fmpz_mat([list(row) for row in printed.basis])
    card_gram = fmpz_mat(
        [[printed.twist * int(value) for value in row] for row in card.gram_tensor]
    )
    source_gram = fmpz_mat([list(row) for row in printed.gram_tensor])
    assert abs(basis.det()) == 1
    assert basis.transpose() * card_gram * basis == source_gram


def test_row_81_embeddings_were_seeded_as_orthogonal_primitive_complements() -> None:
    held = {
        ("02AP", "027E"): _held("02AP", "027E"),
        ("02AQ", "027E"): _held("02AQ", "027E"),
    }
    assert hashimoto.complements(
        ("02AP", 2), ("02AQ", -1), _lattice("027E"), held
    )
