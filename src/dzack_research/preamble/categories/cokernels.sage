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
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class CokernelElement(Element):
    r"""A class $\bar x\in\operatorname{coker} f$, held by a canonical lift."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        Element.__init__(self, parent)
        self._coordinates = parent.reduce(coordinates)

    def lift(self) -> FreeModuleElement:
        r"""Return the canonical representative in $B$."""
        return self._coordinates

    def _repr_(self) -> str:
        return repr(self._coordinates)

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates, other._coordinates, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates))

    def _add_(self, other: Any) -> "CokernelElement":
        return self.parent()(self._coordinates + other._coordinates)

    def _sub_(self, other: Any) -> "CokernelElement":
        return self.parent()(self._coordinates - other._coordinates)

    def _neg_(self) -> "CokernelElement":
        return self.parent()(-self._coordinates)

    def _lmul_(self, factor: Any) -> "CokernelElement":
        return self.parent()(factor * self._coordinates)

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
        self._hermite = relations.hermite_form(include_zero_rows=False)

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
        coordinates = vector(ZZ, coordinates)
        for row in self._hermite.rows():
            pivot = next(i for i, entry in enumerate(row) if entry != 0)
            coordinates -= (coordinates[pivot] // row[pivot]) * row
        return coordinates

    def _element_constructor_(self, x: Any) -> CokernelElement:
        if isinstance(x, CokernelElement):
            x = x.lift()
        return self.element_class(self, x)

    def gens(self) -> tuple[CokernelElement, ...]:
        r"""Return the images of $B$'s generators."""
        size = self._relations.ncols()
        return tuple(
            self(vector(ZZ, [ZZ(i == j) for j in range(size)])) for i in range(size)
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
            yield self(vector(ZZ, point))

    def _repr_(self) -> str:
        return f"Cokernel of {self._relations.nrows()} relations, order {self.cardinality()}"
