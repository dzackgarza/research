r"""Modules equipped with bilinear forms."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol, final, override, TypeAlias

from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import (
    FormedModulesCategory,
    FormedModulesMorphism,
    OverPIDFormedModulesCategory,
    OverPIDFormedModulesMorphism,
)

if TYPE_CHECKING:
    from ...types import Category, Matrix, RingElement, RModuleElement


class BilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, b)`` with ``b`` bilinear on ``M``.

    Canonical chain: ``Modules(R).WithForms().Bilinear()``.
    """

    _base_category_class_and_axiom = (FormedModulesCategory, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class _BilinearForm(Protocol):
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement: ...

    class ParentMethods:
        @abstractmethod
        def form(self) -> BilinearModulesCategory._BilinearForm: ...

        @override
        @final
        def is_bilinear(self) -> bool:
            return True

        @abstractmethod
        def is_symmetric(self) -> bool:
            r"""Introduced here: decide whether the bilinear form is symmetric."""
            ...

        @abstractmethod
        def is_alternating(self) -> bool:
            r"""Introduced here: decide whether the bilinear form is alternating."""
            ...

        @abstractmethod
        def is_nondegenerate(self) -> bool:
            r"""Introduced here: decide whether the bilinear form has zero radical."""
            ...

        @abstractmethod
        def is_integral(self) -> bool:
            r"""Introduced here: decide whether values lie in the base ring."""
            ...

        @abstractmethod
        def is_rational(self) -> bool:
            r"""Introduced here: decide whether values lie in the fraction field."""
            ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            r"""Introduced here: evaluate the form on two module elements."""
            return self.form().b(v, w)

        @abstractmethod
        def inner_product_matrix(self) -> Matrix:
            r"""Introduced here: return the ambient inner-product matrix."""
            ...

        @abstractmethod
        def gram_matrix(self) -> Matrix:
            r"""Introduced here: return the generator Gram matrix."""
            ...

        @abstractmethod
        def uses_ambient_inner_product(self) -> bool:
            r"""Introduced here: decide whether the form is ambient-inherited."""
            ...

    class ElementMethods:
        @abstractmethod
        def inner_product(self, other: RModuleElement) -> RingElement:
            r"""Introduced here: pair by the parent bilinear form."""
            ...

        @abstractmethod
        def dot_product(self, other: RModuleElement) -> RingElement:
            r"""Introduced here: expose Sage's formed-element dot product."""
            ...


    Symmetric = LazyImport(
        "category_specs.forms.subcategories.symmetric",
        "SymmetricBilinearModulesCategory",
    )
    Alternating = LazyImport(
        "category_specs.forms.subcategories.alternating",
        "AlternatingBilinearModulesCategory",
    )
    Nondegenerate = LazyImport(
        "category_specs.forms.subcategories.nondegenerate",
        "NondegenerateBilinearModulesCategory",
    )
    Integral = LazyImport(
        "category_specs.forms.subcategories.integral", "IntegralBilinearModulesCategory"
    )
    Rational = LazyImport(
        "category_specs.forms.subcategories.rational", "RationalBilinearModulesCategory"
    )


class OverPIDBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Bilinear formed modules over a PID.

    Canonical chain: ``Modules(R).OverPID().WithForms().Bilinear()``.
    """

    _base_category_class_and_axiom = (OverPIDFormedModulesCategory, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    ParentMethods : TypeAlias = BilinearModulesCategory.ParentMethods

    class SubcategoryMethods:
        @final
        def Symmetric(self) -> Category:
            from .symmetric import OverPIDSymmetricBilinearModulesCategory

            return OverPIDSymmetricBilinearModulesCategory(self)
        @final
        def Alternating(self) -> Category:
            from .alternating import OverPIDAlternatingBilinearModulesCategory

            return OverPIDAlternatingBilinearModulesCategory(self)
        @final
        def Nondegenerate(self) -> Category:
            from .nondegenerate import OverPIDNondegenerateBilinearModulesCategory

            return OverPIDNondegenerateBilinearModulesCategory(self)
        @final
        def Integral(self) -> Category:
            from .integral import OverPIDIntegralBilinearModulesCategory

            return OverPIDIntegralBilinearModulesCategory(self)
        @final
        def Rational(self) -> Category:
            from .rational import OverPIDRationalBilinearModulesCategory

            return OverPIDRationalBilinearModulesCategory(self)

    ElementMethods : TypeAlias = BilinearModulesCategory.ElementMethods

    Symmetric = LazyImport(
        "category_specs.forms.subcategories.symmetric",
        "OverPIDSymmetricBilinearModulesCategory",
    )
    Alternating = LazyImport(
        "category_specs.forms.subcategories.alternating",
        "OverPIDAlternatingBilinearModulesCategory",
    )
    Nondegenerate = LazyImport(
        "category_specs.forms.subcategories.nondegenerate",
        "OverPIDNondegenerateBilinearModulesCategory",
    )
    Integral = LazyImport(
        "category_specs.forms.subcategories.integral",
        "OverPIDIntegralBilinearModulesCategory",
    )
    Rational = LazyImport(
        "category_specs.forms.subcategories.rational",
        "OverPIDRationalBilinearModulesCategory",
    )


BilinearModulesObject : TypeAlias = BilinearModulesCategory.ParentMethods
BilinearModulesElement : TypeAlias = BilinearModulesCategory.ElementMethods
BilinearModulesMorphism : TypeAlias = FormedModulesMorphism
OverPIDBilinearModulesObject : TypeAlias = OverPIDBilinearModulesCategory.ParentMethods
OverPIDBilinearModulesElement : TypeAlias = OverPIDBilinearModulesCategory.ElementMethods
OverPIDBilinearModulesMorphism : TypeAlias = OverPIDFormedModulesMorphism
