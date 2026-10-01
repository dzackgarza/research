"""Tables 10.2 and 10.3 of K. Hashimoto, "Finite symplectic actions on the K3 lattice", arXiv:1012.2682, and the records they identify.

Let $\\Lambda = \\mathrm{II}_{3,19}$ be the K3 lattice. Table 10.2 lists the 81 finite groups
$\\mathfrak{G}_n \\subset O(\\Lambda)$ of symplectic isometries, up to conjugacy: the order, the
SmallGroup number $i$, the group, the order $|q_n|$ and the genus symbol $q_n$ of the discriminant
form, and the rank $c(\\mathfrak{G}_n)$ of the coinvariant lattice $\\Lambda_G = (\\Lambda^G)^\\perp$.
A row printed with $\\sharp m$ in place of $q_n$ has the same invariant lattice as row $m$.
Table 10.3 gives a Gram tensor of $\\Lambda^G$ for each row $m$ that no other row points to,
two Gram tensors where the genus of $\\Lambda^G$ has two classes.

`sources/hashimoto/table_10_2.json` stores Table 10.2 as printed, with `shares` for $\\sharp m$ and,
on each other row, the record $R$ and the twist $t$ with $\\Lambda_G = R(t)$.
`sources/hashimoto/table_10_3.json` stores each printed Gram tensor $T$ with the record $R$, the
twist $t$, and the matrix $P$ whose column $j$ holds the coordinates in the basis of $R$ of the
$j$-th basis vector of $T$, so that $P^{\\top} (t \\, G_R) P = T$.
`check` asserts every equation that these files state.
"""

import re
from fractions import Fraction
from collections.abc import Mapping
from pathlib import Path

from flint import fmpz, fmpz_mat
from pydantic import BaseModel, ConfigDict, TypeAdapter

from latticedb import arithmetic
from latticedb.model import Lattice, Tag

K3_RANK = 22
_SYMBOL = re.compile(r"(\d+)(?:_(?:II|\d))?\^\{([+-])(\d+)\}")


class Twist(BaseModel):
    """A record $R$ and a nonzero integer $t$: the lattice is $R(t)$."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    record: Tag
    twist: int


class GroupRow(BaseModel):
    """A row of Table 10.2."""

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
    """A Gram tensor of Table 10.3, the record $R$ and twist $t$ of the lattice, and the matrix $P$ with $P^{\\top} (t \\, G_R) P = T$."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    gram_tensor: tuple[tuple[int, ...], ...]
    record: Tag
    twist: int
    basis: tuple[tuple[int, ...], ...]


class InvariantRow(BaseModel):
    """A row of Table 10.3."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    n: int
    lattices: tuple[InvariantLattice, ...]


def stored(directory: Path) -> tuple[tuple[GroupRow, ...], tuple[InvariantRow, ...]]:
    """Tables 10.2 and 10.3 from `directory`."""
    groups = TypeAdapter(tuple[GroupRow, ...]).validate_json((directory / "table_10_2.json").read_text())
    invariants = TypeAdapter(tuple[InvariantRow, ...]).validate_json((directory / "table_10_3.json").read_text())
    return groups, invariants


def symbol_group(symbol: str) -> list[int]:
    """The orders of the cyclic factors of prime-power order of the discriminant group of a genus symbol such as `2_II^{-2}, 8_1^{+1}, 3^{-1}`."""
    terms = [term.strip() for term in symbol.split(",")]
    found = [_SYMBOL.fullmatch(term) for term in terms]
    assert all(found), f"{symbol} is not a genus symbol"
    return sorted(int(match[1]) for match in found if match for _ in range(int(match[3])))


def prime_powers(gram_tensor: arithmetic.GramTensor) -> list[int]:
    """The orders of the cyclic factors of prime-power order of the discriminant group."""
    return sorted(int(p) ** int(e) for factor in arithmetic.discriminant_invariants(gram_tensor) for p, e in fmpz(factor).factor())


def twisted(lattice: Lattice, twist: int) -> arithmetic.GramTensor:
    return arithmetic.scaled(lattice.gram_tensor, twist)


def _tensor(rows: tuple[tuple[int, ...], ...]) -> arithmetic.GramTensor:
    return tuple(tuple(map(Fraction, row)) for row in rows)


def check(groups: tuple[GroupRow, ...], invariants: tuple[InvariantRow, ...], lattices: Mapping[str, Lattice]) -> list[str]:
    """The equations of Tables 10.2 and 10.3 that the records do not satisfy."""
    found: list[str] = []
    by_n = {row.n: row for row in groups}
    assert sorted(by_n) == list(range(1, 82)), "Table 10.2 has the rows 1 to 81"
    owners = {row.n for row in groups if row.shares is None}
    if owners != {row.n for row in invariants}:
        found.append(f"Table 10.3 has the rows {sorted(row.n for row in invariants)}, the rows of Table 10.2 without a sharp sign are {sorted(owners)}")
    for row in groups:
        if row.shares is not None:
            owner = by_n[row.shares]
            if owner.shares is not None or (owner.discriminant_order, owner.rank) != (row.discriminant_order, row.rank):
                found.append(f"Table 10.2 row {row.n}: row {row.shares} is not a row with the same |q| and c")
            continue
        assert row.coinvariant is not None and row.discriminant_form is not None, f"Table 10.2 row {row.n} names no record"
        lattice = lattices[row.coinvariant.record]
        coinvariant = twisted(lattice, row.coinvariant.twist)
        computed = (lattice.rank, arithmetic.inertia(coinvariant)[0], abs(arithmetic.determinant(coinvariant)), prime_powers(coinvariant))
        stated = (row.rank, 0, row.discriminant_order, symbol_group(row.discriminant_form))
        if computed != stated:
            found.append(f"Table 10.2 row {row.n}: (c, n_+, |q|, group of q) is {stated}, {row.coinvariant.record}({row.coinvariant.twist}) gives {computed}")
    for invariant in invariants:
        row = by_n[invariant.n]
        for printed in invariant.lattices:
            lattice = lattices[printed.record]
            basis = fmpz_mat([list(r) for r in printed.basis])
            images = tuple(tuple(int(basis[i, j]) for i in range(basis.nrows())) for j in range(basis.ncols()))
            tensor = _tensor(printed.gram_tensor)
            if abs(basis.det()) != 1 or arithmetic.restriction(twisted(lattice, printed.twist), images) != tensor:
                found.append(f"Table 10.3 row {invariant.n}: P is not an isometry from the printed Gram tensor to {printed.record}({printed.twist})")
            assert row.discriminant_form is not None
            rank = K3_RANK - row.rank
            computed = (len(tensor), arithmetic.inertia(tensor)[:2], abs(arithmetic.determinant(tensor)), prime_powers(tensor))
            stated = (rank, (3, rank - 3), row.discriminant_order, symbol_group(row.discriminant_form))
            if computed != stated:
                found.append(f"Table 10.3 row {invariant.n}: (rank, signature, |q|, group of q) is {stated}, the printed Gram tensor gives {computed}")
    return found


def stored_problems(root: Path, lattices: Mapping[str, Lattice]) -> list[str]:
    """`check` on the files under `root/sources/hashimoto`."""
    return check(*stored(root / "sources" / "hashimoto"), lattices)


