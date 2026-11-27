r"""Subobject construction category for categories."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from ... import (
    CategoryWithAxiom,
    CategoryWithAxiom_over_base_ring,
    CategoryWithAxiom_singleton,
    SubobjectsCategory,
)

if TYPE_CHECKING:
    from ....types import Category, CategoryObject


class Subcategories(SubobjectsCategory):
    r"""Subcategories viewed as subobjects in ``Cat()``.

    Canonical chain: ``Cat().Subobjects()``.
    """

    @override
    @final
    def __contains__(self, candidate: Any) -> bool:
        r"""Return whether ``candidate`` is registered as a subcategory object."""
        from ... import Cat

        if candidate not in Cat():
            return False
        if not isinstance(
            candidate,
            (
                CategoryWithAxiom,
                CategoryWithAxiom_singleton,
                CategoryWithAxiom_over_base_ring,
            ),
        ):
            return False
        ambient = candidate.ambient_category()
        predicates = candidate.defining_predicates()
        return (
            ambient in Cat() and candidate.is_subcategory(ambient) and bool(predicates)
        )

    class ParentMethods:
        @abstractmethod
        def ambient_category(self) -> Category:
            r"""Return the category in which this subcategory is defined."""
            ...

        @abstractmethod
        def defining_predicates(self) -> tuple[str, ...]:
            r"""Return the object predicates defining this full subcategory."""
            ...

        @abstractmethod
        def defining_predicate(self, candidate: CategoryObject) -> bool:
            r"""Return whether ``candidate`` satisfies all defining predicates."""
            ...

    class ElementMethods: ...
