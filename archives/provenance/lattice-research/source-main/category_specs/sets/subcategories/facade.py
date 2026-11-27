r"""Facade set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast, final, override

from sage.categories.facade_sets import FacadeSets as SageFacadeSets
from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Set, SetElement

from .. import Sets


class _FacadeSets(CategoryWithAxiom):
    r"""Canonical chain: ``Sets().Facade()``."""

    _base_category_class_and_axiom = (Sets, "Facade")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "facade sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageSets().Facade(), Sets()]

    class ParentMethods:
        @override
        @final
        def is_facade(self) -> bool:
            return True

        @override
        @final
        def _element_constructor_(self, element: SetElement) -> SetElement:
            r"""Coerce ``element`` from any facade parent."""
            return cast(
                "SetElement",
                SageFacadeSets.ParentMethods._element_constructor_(self, element),
            )

        @override
        @final
        def facade_for(self) -> tuple[Set, ...] | bool:
            r"""Return the tuple of parents this set is a facade for."""
            return cast(
                "tuple[Set, ...] | bool", SageFacadeSets.ParentMethods.facade_for(self)
            )

        @override
        @final
        def is_parent_of(self, element: Any) -> bool:
            return cast(bool, SageFacadeSets.ParentMethods.is_parent_of(self, element))

        @override
        @final
        def __contains__(self, element: Any) -> bool:
            return cast(bool, SageFacadeSets.ParentMethods.__contains__(self, element))

        @override
        @final
        def _an_element_(self) -> SetElement:
            return cast("SetElement", SageFacadeSets.ParentMethods._an_element_(self))

    class ElementMethods: ...
