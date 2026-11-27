r"""TopologicalRings ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override

from sage.categories.rings import Rings as SageRings
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...topological_spaces import TopologicalSpaces
from ...utils import with_axiom
from .. import Rings

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    pass


class _TopologicalRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Topological()``."""

    _base_category_class_and_axiom = (Rings, "Topological")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "topological rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageRings().Topological(), TopologicalSpaces(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageRings().Topological() or (
            R in self.base_category() and R.is_topological_ring()
        )

    Complete = LazyImport(
        "category_specs.rings.subcategories.complete", "_CompleteRings"
    )

    class SubcategoryMethods:
        @final
        def Complete(self) -> Category:
            return cast(Category, with_axiom(self, "Complete"))

    class ParentMethods:
        @override
        @final
        def is_topological_ring(self) -> bool:
            return True

    class ElementMethods: ...
