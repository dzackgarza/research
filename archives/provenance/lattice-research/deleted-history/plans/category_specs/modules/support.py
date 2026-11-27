r"""Support categories shared by the module category spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.objects import Objects
from sage.categories.sets_cat import Sets

if TYPE_CHECKING:
    from sage.structure.parent import Parent

    Ring = Parent


FinSet = Sets().Finite()


class Categories(Category_singleton):
    r"""A shim to define an infty-category of Sage categories."""

    def super_categories(self):
        return [Objects()]

    def __contains__(self, C: Any) -> bool:
        return isinstance(C, Category)

    @classmethod
    def is_over_a_ring(cls, C: Category) -> bool:
        assert C in Categories(), f"Object is not a category: {C}"
        return any(hasattr(D, "base_ring") for D in C.super_categories())

    @classmethod
    def base_ring(cls, C: Category) -> Ring:
        base_ring_cat = next(
            (D for D in C.super_categories() if hasattr(D, "base_ring")),
            None,
        )
        assert base_ring_cat is not None, f"No super category of {C} is a category over a base ring."
        return base_ring_cat.base_ring()
