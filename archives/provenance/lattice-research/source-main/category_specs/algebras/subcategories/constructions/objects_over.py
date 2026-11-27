r"""Slice construction category of algebras over a fixed algebra."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraMorphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Algebras ``B`` equipped with an algebra morphism ``B -> A``.

    Canonical chain: ``Algebras(R).ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"algebras over {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_algebra(self) -> Algebra:
            r"""Return the target algebra of this object-over structure."""
            ...

        @abstractmethod
        def structure_map(self) -> AlgebraMorphism:
            r"""Return the algebra morphism from this algebra to the target."""
            ...

        @final
        def structure_morphism(self) -> AlgebraMorphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
