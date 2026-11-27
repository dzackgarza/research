r"""NoetherianRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.noetherian_rings import NoetherianRings as SageNoetherianRings

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .commutative import _CommutativeRings as _CommutativeRings

if TYPE_CHECKING:
    pass


class _NoetherianRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Noetherian()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "Noetherian")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "noetherian rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageNoetherianRings(), _CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageNoetherianRings() or (
            R in self.base_category() and R.is_noetherian()
        )

    class ParentMethods: ...

    class ElementMethods: ...
