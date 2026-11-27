r"""Algebras equipped with a distinguished basis."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.algebras_with_basis import AlgebrasWithBasis as SageAlgebrasWithBasis
from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras

if TYPE_CHECKING:
    from ...types import (
        AlgebraBasis,
        AlgebraElement,
        HochschildChainComplex,
        RModule,
        SetFamily,
    )


class _AlgebrasWithBasis(CategoryWithAxiom_over_base_ring):
    r"""Algebras with a distinguished basis.

    Canonical chain: ``Algebras(R).WithBasis()``.
    """

    _base_category_class_and_axiom = (Algebras, "WithBasis")
    FiniteDimensional = LazyImport(
        "category_specs.algebras.subcategories.finite_dimensional_with_basis",
        "_FiniteDimensionalAlgebrasWithBasis",
    )

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return algebra and Sage with-basis supercategories."""
        R = self.base_ring()
        return [Algebras(R), SageAlgebrasWithBasis(R)]

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is an algebra with a Sage-recognized basis."""
        return A in self.base_category() and A in SageAlgebrasWithBasis(self.base_ring())

    class ParentMethods:
        @abstract_method
        def basis(self) -> AlgebraBasis:
            r"""Return the distinguished basis of this algebra."""
            ...

        @override
        @abstract_method
        def algebra_generators(self) -> SetFamily:
            r"""Return algebra generators expressed in the distinguished basis."""
            ...

        @override
        @abstract_method
        def hochschild_complex(self, coefficients: RModule) -> HochschildChainComplex:
            r"""Return the Hochschild complex computed from this basis presentation."""
            ...

    class ElementMethods:
        @abstract_method
        def __invert__(self) -> AlgebraElement:
            r"""Return the multiplicative inverse of this algebra element."""
            ...

    class MorphismMethods: ...
