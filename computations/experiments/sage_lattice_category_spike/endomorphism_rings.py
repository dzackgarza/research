r"""End(L) — the endomorphism ring (V0d ratification 2026-07-03; owned substrate).

End(L) is the ring of MODULE endomorphisms of the underlying based module,
carrying the lattice's form as context. It is a genuine ring — sums,
differences, nilpotents exist — which is exactly why its elements are NOT the
form-preserving LatticeMorphism type: a nilpotent endomorphism never preserves
a nondegenerate form. The ring's full unit group is GL(L); the lattice's
automorphism group O(L) = Aut(L) is canonically the subgroup of units that
preserve the form, and ``unit_group()`` returns that O(L) object (the
lattice-categorical units, per the ratification).
"""

from __future__ import annotations

from sage.categories.rings import Rings
from sage.matrix.constructor import identity_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element
from sage.structure.parent import Parent

from .domain_algebra import EndomorphismRing as EndomorphismRingCarrier


class ModuleEndomorphism(Element):
    r"""An R-module endomorphism of a synthetic lattice's underlying module.

    Ring element algebra (the ratified philosophy): ``f * g`` is composition,
    ``f + g``/``f - g`` pointwise, powers, unit inverses, ``order()``,
    ``is_nilpotent()``, ``is_unipotent()``. ``preserves_form()`` asks whether
    the endomorphism lies over an isometry-shaped matrix.
    """

    def __init__(self, parent, matrix_data):
        Element.__init__(self, parent)
        lattice = parent.lattice()
        A = matrix(lattice.base_ring(), matrix_data)
        assert A.is_square() and A.nrows() == lattice.rank(), (
            "endomorphism matrix must be square of lattice rank; "
            f"rank={lattice.rank()}, matrix={A}"
        )
        A.set_immutable()
        self._matrix = A

    def _repr_(self):
        return f"Module endomorphism of {self.parent().lattice()._label} represented by\n{self._matrix}"

    def matrix(self):
        return self._matrix

    def __call__(self, element):
        lattice = self.parent().lattice()
        element = lattice(element) if element.parent() is not lattice else element
        image = self._matrix * matrix(lattice.base_ring(), lattice.rank(), 1, list(element.coefficient_vector()))
        return lattice([image[i, 0] for i in range(lattice.rank())])

    def _mul_(self, other):
        r"""Ring multiplication IS composition: ``(f * g)(x) = f(g(x))``."""
        return self.parent()(self._matrix * other.matrix())

    def _add_(self, other):
        return self.parent()(self._matrix + other.matrix())

    def _sub_(self, other):
        return self.parent()(self._matrix - other.matrix())

    def _neg_(self):
        return self.parent()(-self._matrix)

    def __pow__(self, n):
        n = int(n)
        if n < 0:
            return self.inverse() ** (-n)
        if n == 0:
            return self.parent().one()
        return self.parent()(self._matrix ** n)

    def is_unit(self):
        determinant = self._matrix.det()
        if self.parent().lattice().base_ring() is ZZ:
            return determinant in (1, -1)
        return determinant != 0

    def inverse(self):
        if not self.is_unit():
            raise ValueError(
                "only units of End(L) are invertible; "
                f"det={self._matrix.det()} is not a unit of {self.parent().lattice().base_ring()}"
            )
        return self.parent()(self._matrix.inverse())

    def order(self):
        r"""Multiplicative order (units only); ``+Infinity`` when infinite."""
        if not self.is_unit():
            raise ValueError(
                "multiplicative order is defined for units of End(L); "
                f"det={self._matrix.det()}"
            )
        return self._matrix.multiplicative_order()

    def is_identity(self):
        return self._matrix.is_one()

    def is_nilpotent(self):
        return (self._matrix ** self.parent().lattice().rank()).is_zero()

    def is_unipotent(self):
        rank = self.parent().lattice().rank()
        return ((self._matrix - identity_matrix(self._matrix.base_ring(), rank)) ** rank).is_zero()

    def preserves_form(self):
        gram = self.parent().lattice().gram_matrix()
        A = matrix(QQ, self._matrix)
        return A.transpose() * gram * A == gram

    def __eq__(self, other):
        return (
            isinstance(other, ModuleEndomorphism)
            and self.parent() == other.parent()
            and self._matrix == other.matrix()
        )

    def __hash__(self):
        return hash((self.parent().lattice(), self._matrix))


class SyntheticEndomorphismRing(EndomorphismRingCarrier, Parent):
    r"""The ring End(L); unique per lattice (identity: the lattice)."""

    Element = ModuleEndomorphism

    def __init__(self, lattice):
        self._lattice = lattice
        Parent.__init__(self, category=Rings())

    def _repr_(self):
        return f"Endomorphism ring End({self._lattice._label})"

    def _element_constructor_(self, matrix_data):
        from .homsets import LatticeMorphism

        if isinstance(matrix_data, LatticeMorphism):
            assert matrix_data.domain() == self._lattice and matrix_data.codomain() == self._lattice, (
                "only endomorphisms of this ring's lattice embed into End(L); "
                f"domain={matrix_data.domain()}, codomain={matrix_data.codomain()}, lattice={self._lattice}"
            )
            matrix_data = matrix_data.matrix()
        return self.element_class(self, matrix_data)

    def lattice(self):
        return self._lattice

    def from_matrix(self, matrix_data):
        return self(matrix_data)

    def one(self):
        return self(identity_matrix(self._lattice.base_ring(), self._lattice.rank()))

    def zero(self):
        rank = self._lattice.rank()
        return self(matrix(self._lattice.base_ring(), rank, rank))

    def unit_group(self):
        r"""The lattice-categorical unit group Aut(L) = O(L) — the
        form-preserving units. (The ring's FULL unit group is GL(L); the
        ratified reading distinguishes the lattice's automorphisms.)"""
        return self._lattice.isometry_group()

    def __eq__(self, other):
        return isinstance(other, SyntheticEndomorphismRing) and self._lattice == other._lattice

    def __hash__(self):
        return hash(("End", self._lattice))
