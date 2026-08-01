r"""Cokernels of morphisms of free modules.

The quotient layer, owned.  Sage's finitely generated quotients are a pair
$(V, W)$ -- a cover and a submodule of it -- so they carry spans, basis
matrices, and ambient coordinates.  A cokernel needs none of that: a morphism
$f: A\to B$ of free modules already says everything, with $B$'s generating set
becoming the quotient's and $f$'s matrix rows becoming the relations.

An element is a coordinate vector in $B$'s generators, taken modulo the lattice
those rows span.  Two are equal when their difference lies in it, which is
decided by reducing against the Hermite form -- the same reduction that gives
each class a canonical representative to print and hash.
"""

from typing import Any

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.structure.element import Element, Vector
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class CokernelElement(Element):
    r"""A class $\bar x\in\operatorname{coker} f$, held by a canonical lift."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        Element.__init__(self, parent)
        self._coordinates = parent.reduce(coordinates)

    def _lift(self) -> FreeModuleElement:
        r"""Return the canonical representative of this class.  Private: see
        :meth:`FormModuleElement._coordinates`."""
        return self._coordinates

    def _repr_(self) -> str:
        return repr(self._coordinates)

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates, other._coordinates, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates))

    def _add_(self, other: Any) -> "CokernelElement":
        return self.parent()._from_coordinates(self._coordinates + other._coordinates)

    def _sub_(self, other: Any) -> "CokernelElement":
        return self.parent()._from_coordinates(self._coordinates - other._coordinates)

    def _neg_(self) -> "CokernelElement":
        return self.parent()._from_coordinates(-self._coordinates)

    def _lmul_(self, factor: Any) -> "CokernelElement":
        return self.parent()._from_coordinates(factor * self._coordinates)

    _rmul_ = _lmul_

    def order(self) -> Any:
        r"""Return the least $k\ge 1$ with $k\bar x = 0$."""
        parent = self.parent()
        if self._coordinates.is_zero():
            return ZZ.one()
        for k in ZZ(parent.exponent()).divisors():
            if parent.reduce(k * self._coordinates).is_zero():
                return k
        assert False, "an element of a finite cokernel must have finite order"


class Cokernel(Parent):
    r"""$\operatorname{coker} f$ for $f: A\to B$ a morphism of free modules.

    Presented by the morphism itself: the generating set is $B$'s and the
    relations are $f$'s rows.  Nothing here is a submodule of anything.
    """

    Element = CokernelElement

    def __init__(self, morphism: FreeModuleMorphism) -> None:
        relations = matrix(ZZ, morphism.matrix())
        assert relations.det() != 0, (
            "f must be injective, or the cokernel is not finite"
        )
        Parent.__init__(self, base=ZZ)
        self._morphism = morphism
        self._relations = relations
        self._hermite = relations.hermite_form()

    def morphism(self) -> FreeModuleMorphism:
        r"""Return the $f$ this is the cokernel of."""
        return self._morphism

    def relation_matrix(self) -> Matrix:
        r"""Return the relations among :meth:`gens`, one per row."""
        return self._relations

    def reduce(self, coordinates: Any) -> FreeModuleElement:
        r"""Return the canonical representative of this class in $B$.

        Reduction against the Hermite form: each pivot in turn, subtracting the
        multiple of its row that brings that coordinate into range.  The result
        depends only on the class, which is what makes equality and hashing
        decidable rather than a search.
        """
        # Taken as coordinates, not as an element: what arrives may belong to a
        # module carrying a form or an inner product, and the reduction below
        # subtracts plain rows of the Hermite form.
        coordinates = vector(ZZ, list(coordinates))
        for row in self._hermite.rows():
            pivot = next(i for i, entry in enumerate(row) if entry != 0)
            coordinates -= (coordinates[pivot] // row[pivot]) * row
        return coordinates

    def _element_constructor_(self, x: Any) -> CokernelElement:
        r"""Return ``x``, which has to be an element of this quotient already.

        A coordinate vector is not an element of anything: it becomes one only
        against a stated generating set, and stating one is what
        :meth:`linear_combination` is for.
        """
        assert isinstance(x, CokernelElement) and x.parent() is self, (
            f"{x} is not an element of {self}; a class here is built from this "
            "quotient's own generators, with linear_combination or by adding "
            "and scaling them"
        )
        return x

    def __contains__(self, x: Any) -> bool:
        r"""Return whether ``x`` is a class in this quotient, which is parenthood."""
        return isinstance(x, CokernelElement) and x.parent() is self

    def _from_coordinates(self, coordinates: Any) -> CokernelElement:
        r"""Return the class of ``coordinates``, read in this quotient's generators.

        Private, and the only route from a bare vector to an element: the
        object's own construction of its generators and their arithmetic goes
        through here, and everything else states what it means through
        :meth:`linear_combination`.
        """
        return self.element_class(self, coordinates)

    def zero(self) -> CokernelElement:
        return self._from_coordinates([ZZ.zero()] * self.ngens())

    def linear_combination(self, coefficients: Any) -> CokernelElement:
        r"""Return $\sum_i a_i g_i$ for ``coefficients`` $=(a_i)$."""
        coefficients = tuple(coefficients)
        generators = self.gens()
        assert len(coefficients) == len(generators), (
            f"this quotient has {len(generators)} generators, got "
            f"{len(coefficients)} coefficients"
        )
        total = self.zero()
        for coefficient, generator in zip(coefficients, generators):
            # Cast rather than coerce: a coefficient outside the base ring is
            # not a scalar here, and saying so loudly beats a silent product.
            total += ZZ(coefficient) * generator
        return total

    def gens(self) -> tuple[CokernelElement, ...]:
        r"""Return the images of $B$'s generators."""
        size = self._relations.ncols()
        return tuple(
            self._from_coordinates([ZZ(i == j) for j in range(size)])
            for i in range(size)
        )

    def invariants(self) -> tuple:
        r"""Return the invariant factors, from the Smith form of the relations."""
        smith = self._relations.smith_form()[0]
        return tuple(
            entry for entry in smith.diagonal() if entry not in (ZZ.one(), ZZ.zero())
        )

    def exponent(self) -> Any:
        r"""Return the exponent: the largest invariant factor, or 1."""
        invariants = self.invariants()
        return invariants[-1] if invariants else ZZ.one()

    def cardinality(self) -> Any:
        r"""Return $|\operatorname{coker} f| = |\det f|$."""
        return abs(self._relations.det())

    def __iter__(self):
        from sage.misc.mrange import cartesian_product_iterator

        size = self._relations.ncols()
        bounds = [self._hermite[i, i] for i in range(size)]
        for point in cartesian_product_iterator([range(b) for b in bounds]):
            yield self._from_coordinates(point)

    def annihilator(self) -> Any:
        r"""Return the ideal killing every element: $(\text{exponent})$."""
        return ZZ.ideal(self.exponent())

    def smith_form_gens(self) -> tuple[CokernelElement, ...]:
        r"""Return generators realizing the invariant factor decomposition.

        With $D=UMV$ the Smith form of the relations, $x\mapsto xV$ carries
        $\operatorname{coker} M$ onto $\mathbb Z^m/\operatorname{row} D$, whose
        standard generators pull back to the rows of $V^{-1}$.  Those with
        $d_i=1$ die, so they are dropped.
        """
        smith, _, right = self._relations.smith_form()
        inverse = right.inverse().change_ring(ZZ)
        return tuple(
            self._from_coordinates(inverse.row(i))
            for i, entry in enumerate(smith.diagonal())
            if entry != ZZ.one()
        )

    def rank(self) -> Any:
        r"""Return 0: a cokernel of an injective map of free modules is torsion."""
        return ZZ.zero()

    def ngens(self) -> int:
        return self._relations.ncols()

    def _repr_(self) -> str:
        return f"Cokernel of {self._relations.nrows()} relations, order {self.cardinality()}"
