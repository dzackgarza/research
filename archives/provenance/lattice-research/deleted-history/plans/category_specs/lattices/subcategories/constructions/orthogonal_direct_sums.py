r"""Orthogonal direct-sum construction category."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import Category_module

if TYPE_CHECKING:
    from ....types import Lattice, SetFamily


class OrthogonalDirectSumsCategory(Category_module):
    r"""Orthogonal direct sums of lattices.

    Canonical chain: ``Lattices(R).OrthogonalDirectSums()``.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"orthogonal direct sums of lattices over {self.base_ring()}"

    @final
    def super_categories(self):
        from ... import Lattices

        return [Lattices(self.base_ring()).CartesianProducts()]

    class ParentMethods:
        @abstract_method
        def summands(self) -> SetFamily: ...

        @abstract_method
        def summand(self, i) -> Lattice: ...

    class ElementMethods: ...
    class MorphismMethods: ...


OrthogonalDirectSumsObject = OrthogonalDirectSumsCategory.ParentMethods
OrthogonalDirectSumsElement = OrthogonalDirectSumsCategory.ElementMethods
OrthogonalDirectSumsMorphism = OrthogonalDirectSumsCategory.MorphismMethods
