r"""Quotient construction category for lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import LatticeElement, LatticeMorphism


class _Quotients(QuotientsCategory):
    r"""Lattice quotients for quotient objects that remain in the lattice category.

    Canonical chain: ``Lattices(R).Quotients()``.
    """

    class ParentMethods:
        @abstract_method
        def projection(self) -> LatticeMorphism: ...

    class ElementMethods:
        @final
        def lift(self) -> LatticeElement:
            return self.parent().projection().lift(self)

    class MorphismMethods: ...
