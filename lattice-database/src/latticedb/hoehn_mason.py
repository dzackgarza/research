"""The Magma file `lattices.txt` of G. Höhn and G. Mason, "The 290 fixed-point sublattices of the Leech lattice", arXiv:1505.06420, and the records it identifies.

The file gives `leech[1]`, the Leech lattice $\\Lambda$ as the span of 24 rows in $\\mathbb{Q}^{24}$ with an
inner product matrix, and for each fixed-point lattice $B$ of rank $i$, number $j$ of their Table 1, the
entry `lattices[i,j]` $= [A, B, C]$: the coinvariant lattice $A = B^\\perp$ and $B$ as rows in the same
$\\mathbb{Q}^{24}$ with the same inner product, and the pointwise stabilizer $C \\subset \\mathrm{Co}_0$ of
$B$ as $24 \\times 24$ integer matrices that act on row vectors of coordinates in the basis of `leech[1]`.

`sources/hoehn_mason/leech.json` stores `leech[1]` as printed, the record of the Leech lattice, and the
matrix whose column $j$ holds the coordinates in the basis of `leech[1]` of the $j$-th basis vector of
the record. `sources/hoehn_mason/lattices_<i>_<j>.json` stores, for each entry whose coinvariant lattice
is $\\Lambda_G(-1)$ for a row of Table 10.2 of Hashimoto (`latticedb.hashimoto`), the bases of $A$ and
$B$ and the generators of $C$ as printed, the row, the record $R$, the twist $t$ with $A = R(t)$, and the
matrix $P$ whose column $j$ holds the coordinates in the basis of $A$ of the $j$-th basis vector of $R$.

`embedding` and `automorphisms` compute from these the morphism $R(t) \\to \\Lambda$ and the action of $C$
on $R$; `check` asserts every equation that the files state and that the source lattice cards hold these maps.
"""

from collections.abc import Mapping
from fractions import Fraction
from pathlib import Path

from flint import fmpq, fmpq_mat, fmpz_mat
from pydantic import BaseModel, ConfigDict, TypeAdapter

from latticedb import corpus, hashimoto
from latticedb.corpus import Matrix
from latticedb.model import Lattice, Tag

LEECH_RANK = 24


class Leech(BaseModel):
    """`leech[1]` as printed, and the basis of its record."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    basis: Matrix
    inner_product: tuple[tuple[str, ...], ...]
    record: Tag
    record_basis: Matrix


class Entry(BaseModel):
    """`lattices[i,j]` as printed, the row of Table 10.2 of Hashimoto, and the basis of the record of its coinvariant lattice."""

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
    """`leech[1]` and the entries from `directory`."""
    leech = Leech.model_validate_json((directory / "leech.json").read_text())
    entries = tuple(TypeAdapter(Entry).validate_json(path.read_text()) for path in sorted(directory.glob("lattices_*.json")))
    return leech, entries


def _rational(rows: Matrix) -> fmpq_mat:
    return fmpq_mat([list(row) for row in rows])


def _integral(matrix: fmpq_mat) -> fmpz_mat | None:
    entries = matrix.entries()
    if any(x.q != 1 for x in entries):
        return None
    return fmpz_mat(matrix.nrows(), matrix.ncols(), [int(x.p) for x in entries])


def _rows(matrix: fmpz_mat) -> Matrix:
    return tuple(tuple(int(matrix[r, c]) for c in range(matrix.ncols())) for r in range(matrix.nrows()))


def _gram(lattice: Lattice) -> fmpq_mat:
    return fmpq_mat([[fmpq(x.numerator, x.denominator) for x in row] for row in lattice.gram_tensor])


def leech_gram(leech: Leech) -> fmpq_mat:
    """The Gram matrix of `leech[1]` in its printed basis."""
    inner_product = fmpq_mat([[fmpq(Fraction(x).numerator, Fraction(x).denominator) for x in row] for row in leech.inner_product])
    basis = _rational(leech.basis)
    return basis * inner_product * basis.transpose()


def coordinates(leech: Leech, rows: Matrix) -> fmpq_mat:
    """The rows of `rows`, vectors of $\\mathbb{Q}^{24}$, in coordinates of the basis of `leech[1]`."""
    return _rational(rows) * _rational(leech.basis).inv()


def action(leech: Leech, entry: Entry) -> list[fmpq_mat]:
    """For each generator $g$ of $C$, the matrix $X$ with $a g = X a$ for the coordinates $a$ of the basis of $A$."""
    a = coordinates(leech, entry.coinvariant_basis)
    inverse = (a * a.transpose()).inv()
    return [a * _rational(g) * a.transpose() * inverse for g in entry.stabilizer_generators]


def embedding(leech: Leech, entry: Entry) -> Matrix:
    """The matrix of the inclusion $R(t) = A \\to \\Lambda$ in the bases of the records: column $j$ is the image of the $j$-th basis vector of $R$."""
    a = coordinates(leech, entry.coinvariant_basis)
    image = _rational(leech.record_basis).inv() * a.transpose() * _rational(entry.record_basis)
    integral = _integral(image)
    assert integral is not None, f"lattices[{entry.i},{entry.j}]: the basis of the record is not in the Leech lattice"
    return _rows(integral)


def automorphisms(leech: Leech, entry: Entry) -> list[Matrix]:
    """The matrices of the generators of $C$ on the record $R$: column $j$ is the image of the $j$-th basis vector of $R$."""
    p = _rational(entry.record_basis)
    found = []
    for x in action(leech, entry):
        integral = _integral(p.inv() * x.transpose() * p)
        assert integral is not None, f"lattices[{entry.i},{entry.j}]: a generator does not map the record to itself"
        found.append(_rows(integral))
    return found


def group_order(generators: list[Matrix]) -> int:
    """The order of the finite group that the integer matrices `generators` generate, by closure under multiplication."""
    matrices = [fmpz_mat([list(row) for row in g]) for g in generators]
    identity = fmpz_mat([[int(r == c) for c in range(len(generators[0]))] for r in range(len(generators[0]))])
    seen = {_rows(identity)}
    frontier = [identity]
    while frontier:
        products = [h * g for h in frontier for g in matrices]
        frontier = [h for h in products if _rows(h) not in seen]
        seen.update(_rows(h) for h in frontier)
    return len(seen)


def check(leech: Leech, entries: tuple[Entry, ...], groups: tuple[hashimoto.GroupRow, ...], lattices: Mapping[str, Lattice], morphisms: corpus.Held) -> list[str]:
    """The equations of the stored file that the records, Table 10.2 of Hashimoto and the stored card morphisms do not satisfy."""
    found: list[str] = []
    gram = leech_gram(leech)
    basis = _rational(leech.record_basis)
    leech_basis = _integral(basis)
    if _integral(gram) is None or leech_basis is None or abs(leech_basis.det()) != 1 or basis.transpose() * gram * basis != _gram(lattices[leech.record]):
        found.append(f"leech[1]: the stored basis is not an isometry from {leech.record} to leech[1]")
    by_n = {row.n: row for row in groups}
    rows = sorted(entry.row for entry in entries)
    owners = sorted(row.n for row in groups if row.shares is None)
    if rows != owners:
        found.append(f"lattices.txt: the entries name the rows {rows} of Table 10.2, the rows without a sharp sign are {owners}")
    for entry in entries:
        name = f"lattices[{entry.i},{entry.j}]"
        a = coordinates(leech, entry.coinvariant_basis)
        b = coordinates(leech, entry.fixed_basis)
        if _integral(a) is None or _integral(b) is None or a.rank() + b.rank() != LEECH_RANK or a * gram * b.transpose() != fmpq_mat(a.nrows(), b.nrows()):
            found.append(f"{name}: A and B are not orthogonal sublattices of leech[1] of complementary rank")
            continue
        generators = [_rational(g) for g in entry.stabilizer_generators]
        if any(g * gram * g.transpose() != gram or b * g != b for g in generators):
            found.append(f"{name}: a generator of C is not an isometry of leech[1] that fixes B")
            continue
        if any(_integral(x) is None for x in action(leech, entry)):
            found.append(f"{name}: a generator of C does not map A to itself")
            continue
        p = _rational(entry.record_basis)
        lattice = lattices[entry.record]
        if _integral(p) is None or abs(p.det()) != 1 or p.transpose() * (a * gram * a.transpose()) * p != entry.twist * _gram(lattice):
            found.append(f"{name}: the stored basis is not an isometry from {entry.record}({entry.twist}) to A")
            continue
        row = by_n[entry.row]
        stated = (row.coinvariant.record, -row.coinvariant.twist) if row.coinvariant else None
        if stated != (entry.record, entry.twist):
            found.append(f"{name}: Table 10.2 row {entry.row} gives Lambda_G(-1) = {stated}, the entry gives {(entry.record, entry.twist)}")
        generated = automorphisms(leech, entry)
        order = group_order(generated)
        if order != row.order:
            found.append(f"{name}: C acts on A with a group of order {order}, Table 10.2 row {entry.row} states |G| = {row.order}")
        if (embedding(leech, entry), entry.twist) not in morphisms.get((entry.record, leech.record), ()):
            found.append(f"lattice card {entry.record} does not hold the inclusion of {name} into {leech.record}")
        held = morphisms.get((entry.record, entry.record), ())
        if any((g, 1) not in held for g in generated):
            found.append(f"lattice card {entry.record} does not hold the self-isometry generators of C of {name}")
    return found


def stored_problems(root: Path, loaded: corpus.Corpus) -> list[str]:
    """`check` on the files under `root/sources/hoehn_mason`, against the lattice records and their stored morphisms."""
    groups, _ = hashimoto.stored(root / "sources" / "hashimoto")
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    return check(*stored(root / "sources" / "hoehn_mason"), groups, lattices, corpus.held(loaded))
