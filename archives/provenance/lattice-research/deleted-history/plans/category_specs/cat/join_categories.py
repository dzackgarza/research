r"""Join-category predicate surface for ``Cat()``."""

from __future__ import annotations

from typing import Any, final, override

from sage.categories.category import JoinCategory as SageJoinCategory

from .base_category_types import Category, Category_singleton


@final
def is_join_category(candidate: Any) -> bool:
    r"""Return whether ``candidate`` is Sage's category-lattice join object."""
    return isinstance(candidate, SageJoinCategory)


class JoinCategories(Category_singleton):
    r"""Subcategory of ``Cat()`` whose objects are Sage join categories.

    Canonical chain: ``Cat().JoinCategories()``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "join categories"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return ``Cat()`` as the ambient category of join objects."""
        from . import Cat

        return [Cat()]

    @override
    @final
    def additional_structure(self):
        r"""Return Sage's additional-structure marker for join categories."""
        return None

    @override
    @final
    def __contains__(self, candidate: Any) -> bool:
        r"""Return whether ``candidate`` is a Sage join category object."""
        return is_join_category(candidate)
