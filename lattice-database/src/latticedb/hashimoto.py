"""Stored transcription of Tables 10.2 and 10.3 of Hashimoto.

K. Hashimoto, "Finite symplectic actions on the K3 lattice", arXiv:1012.2682.
This module is source intake: it parses the archived transcription and its
card/tag locators, and compares each printed row with the values that public
preamble operations return for the named cards.  The signatures, discriminant
groups, form preservation, bijectivity and primitivity it compares are computed
by the preamble.
"""

import re
from collections.abc import Mapping
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

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


def _discriminant_prime_powers(lattice) -> tuple[int, ...]:
    """The orders of the cyclic prime-power factors of the discriminant group, in increasing order.

    The preamble splits the discriminant group into its primary components; the
    invariant factors of the `p`-primary component are powers of `p`.
    """
    components = lattice.discriminant_group().primary_components()
    return tuple(
        sorted(
            abs(int(order))
            for prime in components.index_set()
            for order in components[prime].invariant_factors()
        )
    )


def _coinvariant_summary(lattice) -> tuple[int, int, int, tuple[int, ...]]:
    """`(c, n_+, |q|, group of q)` as Table 10.2 prints them."""
    signature = lattice.signature_pair()
    return (
        int(lattice.module_rank()),
        int(signature.first()),
        abs(int(lattice.determinant())),
        _discriminant_prime_powers(lattice),
    )


def _printed_summary(lattice) -> tuple[int, tuple[int, int], int, tuple[int, ...]]:
    """`(rank, signature, |q|, group of q)` as Table 10.3 states them for a printed Gram tensor."""
    signature = lattice.signature_pair()
    return (
        int(lattice.module_rank()),
        (int(signature.first()), int(signature.second())),
        abs(int(lattice.determinant())),
        _discriminant_prime_powers(lattice),
    )


def basis_gives_isometry(source, target, basis_rows) -> bool:
    """Whether the printed change of basis `P` is an isometry from `source` onto `target`.

    The columns of `P` are the images of the generators of `source` in the
    coordinates of `target`.  The module map they define is an isometry when it
    preserves the forms and is bijective.
    """
    images = tuple(target(column) for column in zip(*basis_rows, strict=True))
    module_map = source.module_category().Mor(source, target)(images)
    return (
        source.Mor(target).preserves_forms(module_map)
        and module_map.is_injective()
        and module_map.is_surjective()
    )


def _primitive_orthogonal_pair(ambient, first, second) -> bool:
    """Whether the column spans of two stored embedding matrices are complementary in `ambient`.

    The two spans must be orthogonal, of ranks summing to the rank of `ambient`,
    each spanned freely by its columns, and each primitive.
    """
    first_columns = tuple(zip(*first, strict=True))
    second_columns = tuple(zip(*second, strict=True))
    if len(first_columns) + len(second_columns) != int(ambient.module_rank()):
        return False
    orthogonal = all(
        ambient(left).is_orthogonal_to(ambient(right))
        for left in first_columns
        for right in second_columns
    )
    if not orthogonal:
        return False
    module = ambient.unformed_module()
    for columns in (first_columns, second_columns):
        span = module.subobject_on(tuple(module(column) for column in columns))
        if int(span.module_rank()) != len(columns) or not span.is_primitive():
            return False
    return True


def complements(
    invariant: tuple[Tag, int],
    coinvariant: tuple[Tag, int],
    k3: Lattice,
    morphisms: corpus.Held,
) -> bool:
    """Whether stored source morphisms contain primitive orthogonal complements in the K3 lattice.

    Each stored morphism is `(matrix rows, scale)`; only the morphisms whose scale
    is the stated twist are candidates.
    """
    ambient = Lattices(ZZ)(k3.gram_tensor)
    first_candidates = tuple(
        rows
        for rows, scale in morphisms.get((invariant[0], K3_RECORD), ())
        if int(scale) == invariant[1]
    )
    second_candidates = tuple(
        rows
        for rows, scale in morphisms.get((coinvariant[0], K3_RECORD), ())
        if int(scale) == coinvariant[1]
    )
    return any(
        _primitive_orthogonal_pair(ambient, first, second)
        for first in first_candidates
        for second in second_candidates
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
        computed = _coinvariant_summary(owned)
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
            computed_invariants = _printed_summary(source)
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
