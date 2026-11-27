r"""Slice construction category for categories over a fixed category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.functor import Functor

from ... import Category, Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import CategoryObject


def structure_domain(self: CategoryObject) -> CategoryObject:
    r"""Return the domain of the structure morphism."""
    return self.structure_morphism().domain()


def structure_codomain(self: CategoryObject) -> CategoryObject:
    r"""Return the codomain of the structure morphism."""
    return self.structure_morphism().codomain()


class SliceCategories(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``D -> C``.

    Canonical chain: ``Cat().ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"categories over {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_category(self) -> Category:
            r"""Return the base category ``C`` of this slice object."""
            ...

        @abstractmethod
        def structure_functor(self) -> Functor:
            r"""Return the structure functor from this category to ``C``."""
            ...

        @final
        def structure_morphism(self) -> Functor:
            r"""Return the structure functor as the structure morphism in ``Cat()``."""
            return self.structure_functor()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...



_ObjectsOver = SliceCategories
