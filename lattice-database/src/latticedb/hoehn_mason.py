"""Stored transcription of the Höhn--Mason Leech-lattice ancillary file.

G. Höhn and G. Mason, "The 290 fixed-point sublattices of the Leech lattice",
arXiv:1505.06420.  This module parses the archived source and its card/tag
locators only. Coordinate changes, isometries, stabilizer actions and group
orders are mathematical computations owned by the research preamble.
"""

from pathlib import Path
from collections.abc import Mapping

from pydantic import BaseModel, ConfigDict, TypeAdapter

from dzack_research.preamble.categories.hoehn_mason_source_invariants import (
    actions_are_integral,
    automorphism_matrices,
    complementary_orthogonal_sublattices,
    embedding_matrix,
    generated_group_order,
    leech_record_basis_isometry,
    record_basis_isometry,
    stabilizers_fix_second_and_preserve_gram,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import corpus, hashimoto
from latticedb.corpus import Matrix
from latticedb.model import Lattice, Tag

ZZ = session_ring_objects()["ZZ"]
LEECH_RANK = 24

class Leech(BaseModel):
    """The stored ``leech[1]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    basis: Matrix
    inner_product: tuple[tuple[str, ...], ...]
    record: Tag
    record_basis: Matrix


class Entry(BaseModel):
    """One stored ``lattices[i,j]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    i: int
    j: int
    coinvariant_basis: Matrix
    fixed_basis: Matrix
    stabilizer_generators: tuple[Matrix, ...]
    row: int
    record: Tag
    twist: int
    record_basis: Matrix


def stored(directory: Path) -> tuple[Leech, tuple[Entry, ...]]:
    """Return the archived Leech datum and all ancillary entries."""
    leech = Leech.model_validate_json((directory / "leech.json").read_text())
    entries = tuple(
        TypeAdapter(Entry).validate_json(path.read_text())
        for path in sorted(directory.glob("lattices_*.json"))
    )
    return leech, entries


def embedding(leech: Leech, entry: Entry) -> Matrix:
    """Return the source-record inclusion into the Leech record, computed by preamble."""
    return embedding_matrix(
        leech.basis,
        leech.record_basis,
        entry.coinvariant_basis,
        entry.record_basis,
    )


def automorphisms(leech: Leech, entry: Entry) -> list[Matrix]:
    """Return the stabilizer-generator matrices on the selected record basis."""
    return list(
        automorphism_matrices(
            leech.basis,
            entry.coinvariant_basis,
            entry.stabilizer_generators,
            entry.record_basis,
        )
    )


def group_order(generators: list[Matrix]) -> int:
    """Return the order of the generated matrix group through the preamble owner."""
    return generated_group_order(generators)


def check(
    leech: Leech,
    entries: tuple[Entry, ...],
    groups: tuple[hashimoto.GroupRow, ...],
    lattices: Mapping[str, Lattice],
    morphisms: corpus.Held,
) -> list[str]:
    """Compare the archived ancillary data to card data through preamble computations."""
    found: list[str] = []
    leech_lattice = Lattices(ZZ)(lattices[leech.record].gram_tensor)
    if not leech_record_basis_isometry(
        leech.inner_product, leech.basis, leech.record_basis, leech_lattice
    ):
        found.append(
            f"leech[1]: the stored basis is not an isometry from {leech.record} to leech[1]"
        )
    by_n = {row.n: row for row in groups}
    rows = sorted(entry.row for entry in entries)
    owners = sorted(row.n for row in groups if row.shares is None)
    if rows != owners:
        found.append(
            f"lattices.txt: the entries name the rows {rows} of Table 10.2, the rows without a sharp sign are {owners}"
        )
    for entry in entries:
        name = f"lattices[{entry.i},{entry.j}]"
        if not complementary_orthogonal_sublattices(
            leech.inner_product,
            leech.basis,
            entry.coinvariant_basis,
            entry.fixed_basis,
        ):
            found.append(
                f"{name}: A and B are not orthogonal sublattices of leech[1] of complementary rank"
            )
            continue
        if not stabilizers_fix_second_and_preserve_gram(
            leech.inner_product,
            leech.basis,
            entry.fixed_basis,
            entry.stabilizer_generators,
        ):
            found.append(
                f"{name}: a generator of C is not an isometry of leech[1] that fixes B"
            )
            continue
        if not actions_are_integral(
            leech.basis, entry.coinvariant_basis, entry.stabilizer_generators
        ):
            found.append(f"{name}: a generator of C does not map A to itself")
            continue
        lattice = lattices[entry.record]
        owned = Lattices(ZZ)(lattice.gram_tensor)
        if not record_basis_isometry(
            leech.inner_product,
            leech.basis,
            entry.coinvariant_basis,
            entry.record_basis,
            entry.twist,
            owned,
        ):
            found.append(
                f"{name}: the stored basis is not an isometry from {entry.record}({entry.twist}) to A"
            )
            continue
        row = by_n[entry.row]
        stated = (row.coinvariant.record, -row.coinvariant.twist) if row.coinvariant else None
        if stated != (entry.record, entry.twist):
            found.append(
                f"{name}: Table 10.2 row {entry.row} gives Lambda_G(-1) = {stated}, the entry gives {(entry.record, entry.twist)}"
            )
        generated = automorphisms(leech, entry)
        order = group_order(generated)
        if order != row.order:
            found.append(
                f"{name}: C acts on A with a group of order {order}, Table 10.2 row {entry.row} states |G| = {row.order}"
            )
        if (embedding(leech, entry), entry.twist) not in morphisms.get(
            (entry.record, leech.record), ()
        ):
            found.append(
                f"lattice card {entry.record} does not hold the inclusion of {name} into {leech.record}"
            )
        held = morphisms.get((entry.record, entry.record), ())
        if any((generator, 1) not in held for generator in generated):
            found.append(
                f"lattice card {entry.record} does not hold the self-isometry generators of C of {name}"
            )
    return found


def stored_problems(root: Path, loaded: corpus.Corpus) -> list[str]:
    """Run the source comparison against the current lattice cards."""
    groups, _ = hashimoto.stored(root / "sources" / "hashimoto")
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    return check(
        *stored(root / "sources" / "hoehn_mason"),
        groups,
        lattices,
        corpus.held(loaded),
    )
