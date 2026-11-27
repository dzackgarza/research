r"""Slice construction category of topological spaces under a fixed space."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory
from ....cat.subcategories.constructions.objects_over import (
    structure_codomain,
    structure_domain,
)

if TYPE_CHECKING:
    from ....types import Morphism, TopologicalSpace


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Spaces ``Y`` equipped with a continuous map ``X -> Y``.

    Canonical chain: ``TopologicalSpaces().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"topological spaces under {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_space(self) -> TopologicalSpace:
            r"""Return the base topological space of this object-under structure."""
            ...

        @abstractmethod
        def structure_map(self) -> Morphism:
            r"""Return the structure map from the base topological space."""
            ...

        @final
        def structure_morphism(self) -> Morphism:
            r"""Return the structure map as the universal structure morphism."""
            return self.structure_map()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...
