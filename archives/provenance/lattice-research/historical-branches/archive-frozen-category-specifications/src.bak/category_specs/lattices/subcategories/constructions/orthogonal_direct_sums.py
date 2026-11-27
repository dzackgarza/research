r"""Orthogonal direct-sum construction category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, TypeAlias

from ....cat import Category_module
from ...homsets import LatticeHomCategory

if TYPE_CHECKING:
    from ....cat import Category
    from ....types import Lattice, SetFamily


class OrthogonalDirectSumsCategory(Category_module):
    r"""Orthogonal direct sums of lattices.

    Canonical chain: ``Lattices(R).OrthogonalDirectSums()``.
    """

    @final
    def _repr_object_names(self) -> str:
        return f"orthogonal direct sums of lattices over {self.base_ring()}"

    @final
    def super_categories(self) -> list[Category]:
        from ... import Lattices

        return [Lattices(self.base_ring()).CartesianProducts()]

    class ParentMethods:
        @abstractmethod
        def summands(self) -> SetFamily: ...

        @abstractmethod
        def summand(self, i: int) -> Lattice: ...

    class ElementMethods: ...



OrthogonalDirectSumsObject : TypeAlias = OrthogonalDirectSumsCategory.ParentMethods
OrthogonalDirectSumsElement : TypeAlias = OrthogonalDirectSumsCategory.ElementMethods
OrthogonalDirectSumsMorphism : TypeAlias = LatticeHomCategory.ElementMethods
