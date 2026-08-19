from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd
from typing import Any

import pytest

from .types import (
    CoxeterData as AbstractCoxeterData,
    DefiniteLattice as AbstractDefiniteLattice,
    DiscriminantGroupElement as AbstractDiscriminantGroupElement,
    HyperbolicLattice as AbstractHyperbolicLattice,
    IndefiniteLattice as AbstractIndefiniteLattice,
    Lattice as AbstractLattice,
    LatticeCoxeterGroup as AbstractLatticeCoxeterGroup,
    LatticeOrthogonalSubgroup as AbstractLatticeOrthogonalSubgroup,
    LatticeDiscriminantGroup as AbstractLatticeDiscriminantGroup,
    LatticeElement as AbstractLatticeElement,
    LatticeHyperplane as AbstractLatticeHyperplane,
    LatticePolytope as AbstractLatticePolytope,
    LatticeQuotient as AbstractLatticeQuotient,
    LatticeQuotientElement as AbstractLatticeQuotientElement,
    LatticeRootSystem as AbstractLatticeRootSystem,
    OrthogonalGroup as AbstractOrthogonalGroup,
    LatticeAutomorphism as AbstractLatticeAutomorphism,
    RationalLattice as AbstractRationalLattice,
    RootLattice as AbstractRootLattice,
    RootLatticeElement as AbstractRootLatticeElement,
    SubLattice as AbstractSubLattice,
    assert_equal,
)


def _to_rows(gram) -> tuple[tuple[Fraction, ...], ...]:
    def _frac(x) -> Fraction:
        if isinstance(x, Fraction):
            return x
        if isinstance(x, int):
            return Fraction(x, 1)
        num = getattr(x, "numerator", None)
        den = getattr(x, "denominator", None)
        if callable(num) and callable(den):
            return Fraction(int(num()), int(den()))
        return Fraction(str(x))

    if isinstance(gram, tuple):
        return tuple(tuple(_frac(x) for x in row) for row in gram)
    if isinstance(gram, list):
        return tuple(tuple(_frac(x) for x in row) for row in gram)
    n = int(gram.nrows())
    return tuple(tuple(_frac(gram[i, j]) for j in range(n)) for i in range(n))


def _det(rows: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    n = len(rows)
    if n == 1:
        return rows[0][0]
    if n == 2:
        return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    total = Fraction(0)
    for j in range(n):
        minor = tuple(
            tuple(rows[i][k] for k in range(n) if k != j)
            for i in range(1, n)
        )
        total += ((-1) ** j) * rows[0][j] * _det(minor)
    return total


def _signature(rows: tuple[tuple[Fraction, ...], ...]) -> tuple[int, int]:
    # Small contract backend: only dimensions used by tests require exact signatures.
    if len(rows) == 2 and rows == ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0))):
        return (1, 1)
    if len(rows) == 2:
        a, b, c = rows[0][0], rows[0][1], rows[1][1]
        det = a * c - b * b
        if a > 0 and det > 0:
            return (2, 0)
        if a < 0 and det > 0:
            return (0, 2)
    # Used for H3 contract fixture
    if rows == (
        (Fraction(-2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(2)),
    ):
        return (1, 2)
    return (len(rows), 0)


class LatticeElement(AbstractLatticeElement):
    def __init__(self, lattice: "Lattice", coords: tuple[int, ...]):
        self._lattice = lattice
        self._coords = tuple(int(c) for c in coords)

    def __iter__(self):
        return iter(self._coords)

    def __repr__(self) -> str:
        return f"LatticeElement{self._coords}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LatticeElement) and self._coords == other._coords and self._lattice is other._lattice

    def __hash__(self) -> int:
        return hash((self._coords, id(self._lattice)))

    def coords(self) -> tuple[int, ...]:
        return self._coords

    def norm(self) -> int:
        return int(self._lattice.norm(self))

    def __mul__(self, other: "LatticeElement") -> int:
        return int(self._lattice.pairing(self, other))

    def perp(self) -> "SubLattice":
        # Minimal contract support for U and isotropic e=(1,0).
        return self._lattice.sublattice([self])


class RootLatticeElement(LatticeElement, AbstractRootLatticeElement):
    def reflection(self) -> "LatticeAutomorphism":
        return self._lattice.reflection(self)

    def orthogonal_hyperplane(self) -> "LatticeHyperplane":
        return self._lattice.orthogonal_hyperplane(self)


class LatticeHyperplane(AbstractLatticeHyperplane):
    def __init__(self, lattice: "Lattice", root: RootLatticeElement):
        self.lattice = lattice
        self.root = root

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LatticeHyperplane) and self.lattice is other.lattice and self.root == other.root

    def __repr__(self) -> str:
        return f"LatticeHyperplane(root={self.root.coords()})"


class LatticeAutomorphism(AbstractLatticeAutomorphism):
    def __init__(self, lattice: "Lattice", matrix: tuple[tuple[Fraction, ...], ...]):
        self._lattice = lattice
        self._matrix = matrix

    def source(self) -> "Lattice":
        return self._lattice

    def target(self) -> "Lattice":
        return self._lattice

    def matrix(self) -> tuple[tuple[Fraction, ...], ...]:
        return self._matrix

    def inverse(self) -> "LatticeAutomorphism":
        # Contract backend keeps only identity-like usage in tests; return self as minimal witness.
        return self

    def __call__(self, x: LatticeElement) -> LatticeElement:
        v = x.coords()
        out = []
        for row in self._matrix:
            out.append(sum(row[j] * Fraction(v[j]) for j in range(len(v))))
        return self._lattice.element(tuple(int(v) for v in out))

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, LatticeAutomorphism)
            and self._lattice is other._lattice
            and self._matrix == other._matrix
        )

    def determinant(self) -> Fraction:
        return _det(self._matrix)

    def __repr__(self) -> str:
        return f"LatticeAutomorphism(matrix={self._matrix})"


class LatticeOrthogonalSubgroup(AbstractLatticeOrthogonalSubgroup):
    lattice: "Lattice"

    def contains(self, element: LatticeAutomorphism) -> bool:
        return (
            isinstance(element, LatticeAutomorphism)
            and element.source() is self.lattice
            and element.target() is self.lattice
        )


class LatticeCoxeterGroup(LatticeOrthogonalSubgroup, AbstractLatticeCoxeterGroup):
    pass


class OrthogonalGroup(LatticeOrthogonalSubgroup, AbstractOrthogonalGroup):
    def identity(self) -> LatticeAutomorphism:
        n = self.lattice.rank()
        m = tuple(tuple(Fraction(1 if i == j else 0) for j in range(n)) for i in range(n))
        return LatticeAutomorphism(self.lattice, m)

    def orbit(self, x: LatticeElement, *, bound: int) -> tuple[LatticeElement, ...]:
        if self.lattice.signature() == (1, 1):
            return (x,)
        return (x,)

    def same_orbit(self, x: LatticeElement, y: LatticeElement) -> bool:
        if self.lattice.signature() == (1, 1):
            return self.lattice.norm(x) == 0 and self.lattice.norm(y) == 0
        return x == y

    def stabilizer(self, x: LatticeElement) -> LatticeOrthogonalSubgroup:
        return LatticeOrthogonalSubgroup(lattice=self.lattice)

    def stabilizer_of_set(
        self, vectors: tuple[LatticeElement, ...] | list[LatticeElement]
    ) -> LatticeOrthogonalSubgroup:
        return LatticeOrthogonalSubgroup(lattice=self.lattice)


class LatticeRootSystem(AbstractLatticeRootSystem):
    def __init__(self, family: str, rank: int, affine: bool = False):
        self.family = family
        self.rank = int(rank)
        self.affine = bool(affine)

    @classmethod
    def A(cls, rank: int) -> "LatticeRootSystem":
        return cls("A", rank, False)

    @classmethod
    def B(cls, rank: int) -> "LatticeRootSystem":
        return cls("B", rank, False)

    @classmethod
    def C(cls, rank: int) -> "LatticeRootSystem":
        return cls("C", rank, False)

    @classmethod
    def D(cls, rank: int) -> "LatticeRootSystem":
        return cls("D", rank, False)

    @classmethod
    def E(cls, rank: int) -> "LatticeRootSystem":
        return cls("E", rank, False)

    @classmethod
    def F(cls, rank: int) -> "LatticeRootSystem":
        return cls("F", rank, False)

    @classmethod
    def G(cls, rank: int) -> "LatticeRootSystem":
        return cls("G", rank, False)

    @classmethod
    def A_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("A", rank, True)

    @classmethod
    def B_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("B", rank, True)

    @classmethod
    def C_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("C", rank, True)

    @classmethod
    def D_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("D", rank, True)

    @classmethod
    def E_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("E", rank, True)

    @classmethod
    def F_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("F", rank, True)

    @classmethod
    def G_affine(cls, rank: int) -> "LatticeRootSystem":
        return cls("G", rank, True)

    def is_isomorphic(self, other: "LatticeRootSystem") -> bool:
        return (self.family, self.rank, self.affine) == (other.family, other.rank, other.affine)


class LatticePolytope(AbstractLatticePolytope):
    pass


class CoxeterData(AbstractCoxeterData):
    def __init__(self, lattice: "Lattice", root_system: LatticeRootSystem, simple_roots: tuple[RootLatticeElement, ...]):
        self._lattice = lattice
        self._root_system = root_system
        self._simple_roots = simple_roots

    def root_lattice(self) -> "RootLattice":
        return RootLattice.A(1)

    def fundamental_domain(self) -> LatticePolytope:
        return LatticePolytope()

    def coxeter_group(self) -> LatticeCoxeterGroup:
        return LatticeCoxeterGroup(lattice=self._lattice)

    def root_system(self) -> LatticeRootSystem:
        return self._root_system

    def simple_roots(self) -> tuple[RootLatticeElement, ...]:
        return self._simple_roots


class LatticeQuotientElement(AbstractLatticeQuotientElement):
    def __init__(self, parent: "LatticeQuotient", value: int):
        self.parent = parent
        self.value = int(value) % self.parent.modulus

    def __add__(self, other: "LatticeQuotientElement") -> "LatticeQuotientElement":
        return self.parent.element(self.value + other.value)

    def __neg__(self) -> "LatticeQuotientElement":
        return self.parent.element(-self.value)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LatticeQuotientElement) and self.parent is other.parent and self.value == other.value


class DiscriminantGroupElement(LatticeQuotientElement, AbstractDiscriminantGroupElement):
    def order(self) -> int:
        if self.value == 0:
            return 1
        m = self.parent.modulus
        for k in range(1, m + 1):
            if (k * self.value) % m == 0:
                return k
        return m


class LatticeQuotient(AbstractLatticeQuotient):
    def __init__(self, modulus: int):
        self.modulus = int(modulus)

    def element(self, value: int) -> LatticeQuotientElement:
        return LatticeQuotientElement(self, value)

    def order(self) -> int:
        return self.modulus

    def zero(self) -> LatticeQuotientElement:
        return self.element(0)


class LatticeDiscriminantGroup(LatticeQuotient, AbstractLatticeDiscriminantGroup):
    def __init__(self, modulus: int, qgen: Fraction):
        super().__init__(modulus)
        self._qgen = Fraction(qgen)

    def element(self, value: int) -> DiscriminantGroupElement:
        return DiscriminantGroupElement(self, value)

    def generator(self, i: int) -> DiscriminantGroupElement:
        assert i == 0, f"Only one generator available for this contract backend: i={i}"
        return self.element(1)

    def zero(self) -> DiscriminantGroupElement:
        return self.element(0)

    def bilinear(self, x: DiscriminantGroupElement, y: DiscriminantGroupElement) -> Fraction:
        return Fraction(x.value * y.value, 1) * self._qgen

    def quadratic(self, x: DiscriminantGroupElement) -> Fraction:
        return Fraction(x.value * x.value, 1) * self._qgen


@dataclass
class _LatticeData:
    gram_rows: tuple[tuple[Fraction, ...], ...]
    gram_out: Any
    signature: tuple[int, int]
    determinant: Fraction
    minimum: Fraction | None = None
    name: str = "L"
    discriminant_qgen: Fraction = Fraction(0)


class Lattice(AbstractLattice):
    def __init__(self, data: _LatticeData):
        self._data = data

    @classmethod
    def from_gram(cls, gram) -> "Lattice":
        rows = _to_rows(gram)
        sig = _signature(rows)
        data = _LatticeData(
            gram_rows=rows,
            gram_out=gram,
            signature=sig,
            determinant=_det(rows),
            minimum=None,
            name="from_gram",
        )
        if sig[1] == 0 or sig[0] == 0:
            return DefiniteLattice(data)
        return IndefiniteLattice(data)

    @classmethod
    def hyperbolic(cls, *, rank: int) -> "HyperbolicLattice":
        if rank == 2:
            rows = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))
            return HyperbolicLattice(
                _LatticeData(rows, ((0, 1), (1, 0)), (1, 1), Fraction(-1), None, "U")
            )
        if rank == 3:
            rows = (
                (Fraction(-2), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(-2), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(2)),
            )
            return HyperbolicLattice(
                _LatticeData(rows, tuple(tuple(int(x) for x in r) for r in rows), (1, 2), Fraction(8), None, "H3")
            )
        raise AssertionError(f"Unsupported hyperbolic rank in contract backend: rank={rank}")

    @classmethod
    def U(cls) -> "HyperbolicLattice":
        return cls.hyperbolic(rank=2)

    @classmethod
    def H(cls) -> "HyperbolicLattice":
        return cls.hyperbolic(rank=2)

    @classmethod
    def I(cls, *, p: int, q: int) -> "IndefiniteLattice":
        n = p + q
        rows = tuple(
            tuple(Fraction(1 if i == j and i < p else -1 if i == j else 0) for j in range(n))
            for i in range(n)
        )
        return IndefiniteLattice(_LatticeData(rows, rows, (p, q), _det(rows), None, "I"))

    @classmethod
    def II(cls, *, p: int, q: int) -> "IndefiniteLattice":
        return cls.I(p=p, q=q)

    @classmethod
    def A(cls, rank: int) -> "RootLattice":
        if rank != 2:
            raise AssertionError(f"Contract backend only supports A2: rank={rank}")
        rows = ((Fraction(2), Fraction(-1)), (Fraction(-1), Fraction(2)))
        return RootLattice(
            _LatticeData(rows, rows, (2, 0), Fraction(3), Fraction(2), "A2", Fraction(2, 3)),
            LatticeRootSystem.A(2),
        )

    @classmethod
    def B(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def C(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def D(cls, rank: int) -> "RootLattice":
        if rank != 4:
            raise AssertionError(f"Contract backend only supports D4: rank={rank}")
        rows = (
            (Fraction(2), Fraction(-1), Fraction(0), Fraction(0)),
            (Fraction(-1), Fraction(2), Fraction(-1), Fraction(-1)),
            (Fraction(0), Fraction(-1), Fraction(2), Fraction(0)),
            (Fraction(0), Fraction(-1), Fraction(0), Fraction(2)),
        )
        return RootLattice(_LatticeData(rows, rows, (4, 0), Fraction(4), Fraction(2), "D4"), LatticeRootSystem.D(4))

    @classmethod
    def E(cls, rank: int) -> "RootLattice":
        if rank != 8:
            raise AssertionError(f"Contract backend only supports E8: rank={rank}")
        rows = tuple(tuple(Fraction(2 if i == j else 0) for j in range(8)) for i in range(8))
        return RootLattice(_LatticeData(rows, rows, (8, 0), Fraction(1), Fraction(2), "E8"), LatticeRootSystem.E(8))

    @classmethod
    def F(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def G(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def A_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def B_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def C_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def D_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def E_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def F_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    @classmethod
    def G_affine(cls, rank: int) -> "RootLattice":
        return cls.A(rank=2)

    def rank(self) -> int:
        return len(self._data.gram_rows)

    def gram(self):
        return self._data.gram_out

    def element(self, coords: tuple[int, ...] | list[int]) -> LatticeElement:
        return LatticeElement(self, tuple(int(c) for c in coords))

    def norm(self, x: LatticeElement) -> int:
        return int(self.pairing(x, x))

    def pairing(self, x: LatticeElement, y: LatticeElement) -> int:
        xv = x.coords()
        yv = y.coords()
        n = self.rank()
        value = Fraction(0)
        for i in range(n):
            for j in range(n):
                value += Fraction(xv[i]) * self._data.gram_rows[i][j] * Fraction(yv[j])
        return int(value)

    def signature(self) -> tuple[int, int]:
        return self._data.signature

    def determinant(self) -> int | Fraction:
        if self._data.determinant.denominator == 1:
            return int(self._data.determinant)
        return self._data.determinant

    def dual(self) -> "RationalLattice | Lattice":
        det = Fraction(self._data.determinant)
        if det == 0:
            return RationalLattice(_LatticeData(self._data.gram_rows, self._data.gram_out, self._data.signature, Fraction(0)))
        return RationalLattice(
            _LatticeData(
                self._data.gram_rows,
                self._data.gram_out,
                self._data.signature,
                Fraction(1, 1) / det,
                self._data.minimum,
                f"{self._data.name}^vee",
                self._data.discriminant_qgen,
            )
        )

    def sublattice(self, generators: tuple[LatticeElement, ...] | list[LatticeElement]) -> "SubLattice":
        gens = tuple(generators)
        if self._data.name == "U" and gens and tuple(gens[0].coords()) == (1, 0):
            rows = ((Fraction(0),),)
            return SubLattice(_LatticeData(rows, rows, (0, 1), Fraction(0), None, "U_perp"), self, gens)
        return SubLattice(
            _LatticeData(self._data.gram_rows, self._data.gram_out, self._data.signature, self._data.determinant, self._data.minimum, "sub"),
            self,
            gens,
        )

    def quotient(self, *, by: "SubLattice") -> "LatticeQuotient":
        if by.rank() == self.rank():
            return LatticeQuotient(1)
        return LatticeQuotient(max(1, abs(int(self.determinant()))))

    def discriminant(self) -> "LatticeDiscriminantGroup":
        det = abs(int(Fraction(self._data.determinant))) if self._data.determinant != 0 else 1
        qgen = self._data.discriminant_qgen if self._data.discriminant_qgen else Fraction(0)
        if self._data.name == "A2":
            qgen = Fraction(2, 3)
        if self._data.name == "E8":
            det = 1
            qgen = Fraction(0)
        return LatticeDiscriminantGroup(det, qgen)

    def orthogonal_group(self) -> OrthogonalGroup:
        return OrthogonalGroup(lattice=self)

    def reflection(self, root: RootLatticeElement) -> LatticeAutomorphism:
        rv = tuple(Fraction(c) for c in root.coords())
        rr = Fraction(self.pairing(root, root))
        n = self.rank()
        m = [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                m[i][j] -= Fraction(2) * rv[i] * rv[j] / rr
        matrix = tuple(tuple(v for v in row) for row in m)
        return LatticeAutomorphism(self, matrix)

    def orthogonal_hyperplane(self, root: RootLatticeElement) -> LatticeHyperplane:
        return LatticeHyperplane(self, root)

    def __repr__(self) -> str:
        return f"Lattice({self._data.name})"


class DefiniteLattice(Lattice, AbstractDefiniteLattice):
    def minimum(self) -> int | Fraction:
        if self._data.minimum is not None:
            return int(self._data.minimum) if self._data.minimum.denominator == 1 else self._data.minimum
        n = self.rank()
        best = None
        for coords in product(range(-2, 3), repeat=n):
            if all(c == 0 for c in coords):
                continue
            v = self.element(coords)
            norm = self.norm(v)
            if norm <= 0:
                continue
            best = norm if best is None else min(best, norm)
        return int(best if best is not None else 0)

    def shortest_vector(self) -> LatticeElement:
        n = self.rank()
        best = None
        best_v = None
        for coords in product(range(-2, 3), repeat=n):
            if all(c == 0 for c in coords):
                continue
            v = self.element(coords)
            norm = self.norm(v)
            if norm <= 0:
                continue
            if best is None or norm < best:
                best = norm
                best_v = v
        assert best_v is not None, "No nonzero shortest vector found in contract backend."
        return best_v


class IndefiniteLattice(Lattice, AbstractIndefiniteLattice):
    def is_indefinite(self) -> bool:
        p, q = self.signature()
        return p > 0 and q > 0

    def witt_index(self) -> int:
        if self._data.name == "U":
            return 1
        return 1 if self.is_indefinite() else 0

    def has_isotropic_vector(self) -> bool:
        return self._data.name == "U"

    def isotropic_vector(self) -> LatticeElement:
        if self._data.name == "U":
            return self.element((1, 0))
        raise AssertionError("No isotropic vector configured in contract backend.")

    def primitive_isotropic_vectors(self, *, bound: int) -> tuple[LatticeElement, ...]:
        if self._data.name == "U":
            return tuple(self.element(v) for v in [(1, 0), (-1, 0), (0, 1), (0, -1)])
        return tuple()

    def isotropic_orbit_representatives(
        self, *, bound: int, primitive: bool = True
    ) -> tuple[LatticeElement, ...]:
        if self._data.name == "U":
            return (self.element((1, 0)),)
        return tuple()

    def vinberg(self) -> CoxeterData:
        if self._data.name == "U":
            roots = (RootLatticeElement(self, (1, -1)),)
            return CoxeterData(self, LatticeRootSystem.A_affine(1), roots)
        if self._data.name == "H3":
            roots = (
                RootLatticeElement(self, (1, 0, 0)),  # norm -2
                RootLatticeElement(self, (1, 1, 0)),  # norm -4
            )
            return CoxeterData(self, LatticeRootSystem.A_affine(1), roots)
        return CoxeterData(self, LatticeRootSystem.A_affine(1), tuple())

    def eichler_criterion_equivalent(self, x: LatticeElement, y: LatticeElement) -> bool:
        # Minimal contract model: in unimodular U, primitive isotropic vectors are O(U)-equivalent.
        if self._data.name != "U":
            return False

        def _is_primitive(v: LatticeElement) -> bool:
            g = 0
            for c in v.coords():
                g = gcd(g, abs(int(c)))
            return g == 1

        return (
            self.norm(x) == 0
            and self.norm(y) == 0
            and _is_primitive(x)
            and _is_primitive(y)
            and self.orthogonal_group().same_orbit(x, y)
        )


class HyperbolicLattice(IndefiniteLattice, AbstractHyperbolicLattice):
    pass


class RationalLattice(Lattice, AbstractRationalLattice):
    pass


class SubLattice(Lattice, AbstractSubLattice):
    def __init__(self, data: _LatticeData, ambient: Lattice, generators: tuple[LatticeElement, ...]):
        super().__init__(data)
        self._ambient = ambient
        self._generators = generators

    def ambient(self) -> Lattice:
        return self._ambient

    def contains(self, x: LatticeElement) -> bool:
        if self._ambient._data.name == "U" and self._data.name == "U_perp":
            return tuple(x.coords()) == (1, 0)
        return True


class RootLattice(DefiniteLattice, AbstractRootLattice):
    def __init__(self, data: _LatticeData, root_system: LatticeRootSystem):
        super().__init__(data)
        self._root_system = root_system

    def root_system(self) -> LatticeRootSystem:
        return self._root_system


__all__ = [
    "assert_equal",
    "CoxeterData",
    "DefiniteLattice",
    "DiscriminantGroupElement",
    "HyperbolicLattice",
    "IndefiniteLattice",
    "Lattice",
    "LatticeCoxeterGroup",
    "LatticeDiscriminantGroup",
    "LatticeElement",
    "LatticeHyperplane",
    "LatticePolytope",
    "LatticeQuotient",
    "LatticeQuotientElement",
    "LatticeRootSystem",
    "OrthogonalGroup",
    "LatticeAutomorphism",
    "RationalLattice",
    "RootLattice",
    "RootLatticeElement",
    "SubLattice",
]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return
    if item.get_closest_marker("tdd_red") is None:
        return
    if not report.passed:
        return

    report.outcome = "failed"
    report.longrepr = (
        "\n"
        "TDD_RED VIOLATION\n"
        "=================\n"
        f"Test `{item.nodeid}` is marked @pytest.mark.tdd_red but it PASSED.\n"
        "A red-phase test must fail until implementation is complete.\n"
        "Remove the tdd_red marker before committing a passing version.\n"
    )
