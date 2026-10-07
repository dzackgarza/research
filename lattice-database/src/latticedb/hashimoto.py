"""Stored transcription of Tables 10.2 and 10.3 of Hashimoto.

K. Hashimoto, "Finite symplectic actions on the K3 lattice", arXiv:1012.2682.
This module is source intake only: it parses the archived transcription and its
card/tag locators.  Mathematical verification of the stated lattices, forms,
embeddings and complements belongs to the research preamble, not to latticedb.
"""

import re
from collections.abc import Mapping
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

from dzack_research.preamble.categories.hashimoto_source_invariants import (
    basis_gives_isometry,
    lattice_summary,
    printed_summary,
    primitive_orthogonal_complements,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import corpus
from latticedb.model import Lattice, Tag

ZZ = session_ring_objects()["ZZ"]
K3_RANK = 22
K3_RECORD = "027E"
_SYMBOL = re.compile(r"(\d+)(?:_(?:II|\d))?\^\{([+-])(\d+)\}")


class Twist(BaseModel):
    """A record ``R`` and nonzero integer ``t`` naming the source lattice ``R(t)``."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    record: Tag
    twist: int


class GroupRow(BaseModel):
    """One stored row of Table 10.2."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    n: int
    order: int
    small_group: int
    group: str
    discriminant_order: int
    discriminant_form: str | None
    shares: int | None
    rank: int
    coinvariant: Twist | None = None


class InvariantLattice(BaseModel):
    """One printed Gram tensor of Table 10.3 and its stored card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    gram_tensor: tuple[tuple[int, ...], ...]
    record: Tag
    twist: int
    basis: tuple[tuple[int, ...], ...]


class InvariantRow(BaseModel):
    """One stored row of Table 10.3."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    n: int
    lattices: tuple[InvariantLattice, ...]


def stored(directory: Path) -> tuple[tuple[GroupRow, ...], tuple[InvariantRow, ...]]:
    """Return Tables 10.2 and 10.3 exactly as stored under ``directory``."""
    groups = TypeAdapter(tuple[GroupRow, ...]).validate_json(
        (directory / "table_10_2.json").read_text()
    )
    invariants = TypeAdapter(tuple[InvariantRow, ...]).validate_json(
        (directory / "table_10_3.json").read_text()
    )
    return groups, invariants


def symbol_group(symbol: str) -> list[int]:
    """Parse the prime-power cyclic-factor orders printed in a genus symbol."""
    terms = [term.strip() for term in symbol.split(",")]
    found = [_SYMBOL.fullmatch(term) for term in terms]
    if not all(found):
        raise ValueError(f"{symbol!r} is not a stored Hashimoto genus symbol")
    return sorted(
        int(match[1])
        for match in found
        if match is not None
        for _ in range(int(match[3]))
    )


def complements(
    invariant: tuple[Tag, int],
    coinvariant: tuple[Tag, int],
    k3: Lattice,
    morphisms: corpus.Held,
) -> bool:
    """Whether stored source morphisms contain primitive orthogonal complements in the K3 lattice."""
    ambient = Lattices(ZZ)(k3.gram_tensor)
    return primitive_orthogonal_complements(
        ambient,
        morphisms.get((invariant[0], K3_RECORD), ()),
        invariant[1],
        morphisms.get((coinvariant[0], K3_RECORD), ()),
        coinvariant[1],
    )


def check(
    groups: tuple[GroupRow, ...],
    invariants: tuple[InvariantRow, ...],
    lattices: Mapping[str, Lattice],
    morphisms: corpus.Held,
) -> list[str]:
    """Compare the stored transcription to card data using preamble-owned lattice computations."""
    found: list[str] = []
    by_n = {row.n: row for row in groups}
    assert sorted(by_n) == list(range(1, 82)), "Table 10.2 has the rows 1 to 81"
    owners = {row.n for row in groups if row.shares is None}
    if owners != {row.n for row in invariants}:
        found.append(
            f"Table 10.3 has the rows {sorted(row.n for row in invariants)}, the rows of Table 10.2 without a sharp sign are {sorted(owners)}"
        )
    for row in groups:
        if row.shares is not None:
            owner = by_n[row.shares]
            if owner.shares is not None or (
                owner.discriminant_order,
                owner.rank,
            ) != (row.discriminant_order, row.rank):
                found.append(
                    f"Table 10.2 row {row.n}: row {row.shares} is not a row with the same |q| and c"
                )
            continue
        assert row.coinvariant is not None and row.discriminant_form is not None
        lattice = lattices[row.coinvariant.record]
        owned = Lattices(ZZ)(lattice.gram_tensor).twist(row.coinvariant.twist)
        computed = lattice_summary(owned)
        stated = (
            row.rank,
            0,
            row.discriminant_order,
            tuple(symbol_group(row.discriminant_form)),
        )
        if computed != stated:
            found.append(
                f"Table 10.2 row {row.n}: (c, n_+, |q|, group of q) is {stated}, {row.coinvariant.record}({row.coinvariant.twist}) gives {computed}"
            )
    for invariant in invariants:
        row = by_n[invariant.n]
        for printed in invariant.lattices:
            target = Lattices(ZZ)(lattices[printed.record].gram_tensor).twist(
                printed.twist
            )
            source = Lattices(ZZ)(printed.gram_tensor)
            if not basis_gives_isometry(source, target, printed.basis):
                found.append(
                    f"Table 10.3 row {invariant.n}: P is not an isometry from the printed Gram tensor to {printed.record}({printed.twist})"
                )
            assert row.discriminant_form is not None
            expected_rank = K3_RANK - row.rank
            stated_invariants = (
                expected_rank,
                (3, expected_rank - 3),
                row.discriminant_order,
                tuple(symbol_group(row.discriminant_form)),
            )
            computed_invariants = printed_summary(source)
            if computed_invariants != stated_invariants:
                found.append(
                    f"Table 10.3 row {invariant.n}: (rank, signature, |q|, group of q) is {stated_invariants}, the printed Gram tensor gives {computed_invariants}"
                )
            assert row.coinvariant is not None
            if not complements(
                (printed.record, printed.twist),
                (row.coinvariant.record, row.coinvariant.twist),
                lattices[K3_RECORD],
                morphisms,
            ):
                pair = f"{printed.record}({printed.twist}) and {row.coinvariant.record}({row.coinvariant.twist})"
                found.append(
                    f"Table 10.3 row {invariant.n}: the source lattice cards hold no primitive orthogonal embeddings of {pair} in {K3_RECORD}"
                )
    return found


def stored_problems(root: Path, loaded: corpus.Corpus) -> list[str]:
    """Run the source-table comparison against the current cards."""
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    return check(
        *stored(root / "sources" / "hashimoto"),
        lattices,
        corpus.held(loaded),
    )
