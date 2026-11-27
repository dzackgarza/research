r"""Facade set subcategory."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method

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
        @abstract_method
        def _element_constructor_(self, element: SetElement) -> SetElement:
            r"""Coerce ``element`` from any facade parent."""
            ...

        @abstract_method
        def facade_for(self) -> tuple[Set, ...]:
            r"""Return the tuple of parents this set is a facade for."""
            ...

        @override
        @abstract_method
        def is_parent_of(self, element: SetElement) -> bool: ...

        @override
        @abstract_method
        def __contains__(self, element: Any) -> bool: ...

        @override
        @abstract_method
        def _an_element_(self) -> SetElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
