r"""Finite-dimensional algebras with basis."""

from __future__ import annotations

from typing import final, override

from sage.categories.finite_dimensional_algebras_with_basis import (
    FiniteDimensionalAlgebrasWithBasis as SageFiniteDimensionalAlgebrasWithBasis,
)

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras
from .with_basis import _AlgebrasWithBasis


class _FiniteDimensionalAlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    r"""Finite-dimensional algebras with a distinguished basis.

    Canonical chain: ``Algebras(R).WithBasis().FiniteDimensional()``.
    """

    _base_category_class_and_axiom = (_AlgebrasWithBasis, "FiniteDimensional")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return finite-dimensional, with-basis, and Sage supercategories."""
        R = self.base_ring()
        return [
            Algebras(R).FiniteDimensional(),
            Algebras(R).WithBasis(),
            SageFiniteDimensionalAlgebrasWithBasis(R),
        ]

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
