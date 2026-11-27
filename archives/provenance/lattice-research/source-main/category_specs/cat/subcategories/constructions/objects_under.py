r"""Coslice construction category for categories under a fixed category."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.functor import Functor

from ... import Category, Category_over_base, RegressiveCovariantConstructionCategory
from .objects_over import structure_codomain, structure_domain

if TYPE_CHECKING:
    pass


class CosliceCategories(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Categories ``D`` equipped with a functor ``C -> D``.

    Canonical chain: ``Cat().ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"categories under {self.base()}"

    class ParentMethods:
        @abstractmethod
        def structure_category(self) -> Category:
            r"""Return the base category ``C`` of this coslice object."""
            ...

        @abstractmethod
        def structure_functor(self) -> Functor:
            r"""Return the structure functor from ``C`` to this category."""
            ...

        @final
        def structure_morphism(self) -> Functor:
            r"""Return the structure functor as the structure morphism in ``Cat()``."""
            return self.structure_functor()

        structure_domain = structure_domain
        structure_codomain = structure_codomain

    class ElementMethods: ...



_ObjectsUnder = CosliceCategories
