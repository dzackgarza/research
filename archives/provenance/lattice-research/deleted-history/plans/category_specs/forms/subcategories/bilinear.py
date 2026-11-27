r"""Modules equipped with bilinear forms."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import FormedModulesCategory

if TYPE_CHECKING:
    from ...types import Matrix, RingElement, RModuleElement


class BilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, b)`` with ``b`` bilinear on ``M``.

    Canonical chain: ``Modules(R).WithForms().Bilinear()``.
    """

    _base_category_class_and_axiom = (FormedModulesCategory, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class ParentMethods:
        @override
        @final
        def is_bilinear(self) -> bool:
            return True

        @abstract_method
        def is_symmetric(self) -> bool:
            r"""Introduced here: decide whether the bilinear form is symmetric."""
            ...

        @abstract_method
        def is_alternating(self) -> bool:
            r"""Introduced here: decide whether the bilinear form is alternating."""
            ...

        @abstract_method
        def is_nondegenerate(self) -> bool:
            r"""Introduced here: decide whether the bilinear form has zero radical."""
            ...

        @abstract_method
        def is_integral(self) -> bool:
            r"""Introduced here: decide whether the form takes values in the base ring."""
            ...

        @abstract_method
        def is_rational(self) -> bool:
            r"""Introduced here: decide whether the form takes values in the fraction field."""
            ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            r"""Introduced here: evaluate the bilinear form on two module elements."""
            return self.form().b(v, w)

        @abstract_method
        def inner_product_matrix(self) -> Matrix:
            r"""Introduced here: return the matrix encoding the ambient inner product."""
            ...

        @abstract_method
        def gram_matrix(self) -> Matrix:
            r"""Introduced here: return the matrix of the bilinear form on generators."""
            ...

        @abstract_method
        def uses_ambient_inner_product(self) -> bool:
            r"""Introduced here: decide whether the form is inherited from an ambient module."""
            ...

    class ElementMethods:
        @abstract_method
        def inner_product(self, other: RModuleElement) -> RingElement:
            r"""Introduced here: pair this element with another by the parent bilinear form."""
            ...

        @abstract_method
        def dot_product(self, other: RModuleElement) -> RingElement:
            r"""Introduced here: expose Sage's dot-product convention for formed elements."""
            ...

    class MorphismMethods: ...

    Symmetric = LazyImport("category_specs.forms.subcategories.symmetric", "SymmetricBilinearModulesCategory")
    Alternating = LazyImport("category_specs.forms.subcategories.alternating", "AlternatingBilinearModulesCategory")
    Nondegenerate = LazyImport("category_specs.forms.subcategories.nondegenerate", "NondegenerateBilinearModulesCategory")
    Integral = LazyImport("category_specs.forms.subcategories.integral", "IntegralBilinearModulesCategory")
    Rational = LazyImport("category_specs.forms.subcategories.rational", "RationalBilinearModulesCategory")


BilinearModulesObject = BilinearModulesCategory.ParentMethods
BilinearModulesElement = BilinearModulesCategory.ElementMethods
BilinearModulesMorphism = BilinearModulesCategory.MorphismMethods
