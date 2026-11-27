"""Spec for ModulesWithForms(R)."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

import sage.categories.category_with_axiom as _cwa
from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.tensor import TensorProductsCategory
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.structure.parent import Parent

from .homsets import ModulesWithFormsHomsets
from .modules import Modules

if TYPE_CHECKING:
    from .types import (
        BilinearForm,
        BilinearFormSpace,
        QuadraticForm,
        QuadraticFormSpace,
        Ring,
        RingElement,
        RingMorphism,
        RModAutset,
        RModHomsetElement,
        RModule,
        RModuleElement,
        RModuleWithForm,
        TwistedForm,
    )

_cwa.all_axioms += ("NonDegenerate", "Integral", "Rational", "Bilinear", "Quadratic")


class ModulesWithForms(CategoryWithAxiom_over_base_ring):
    r"""
    Category of modules with forms.

    A subcategory of Modules(R) equipped with an extra structure:
    an object from the TwistedForms category.
    """

    Homsets = LazyImport("category_specs.homsets", "ModulesWithFormsHomsets")

    @staticmethod
    def BilinearForms(base_ring: Ring) -> BilinearFormSpace:
        from .twisted_forms import TwistedForms
        return TwistedForms(base_ring).Bilinear()

    @staticmethod
    def QuadraticForms(base_ring: Ring) -> QuadraticFormSpace:
        from .twisted_forms import TwistedForms
        return TwistedForms(base_ring).Quadratic()

    @final
    def super_categories(self) -> list[Category]:
        return [Modules(self.base_ring())]

    @final
    def additional_structure(self):
        from .twisted_forms import TwistedForms
        return TwistedForms(self.base_ring())

    @final
    def _repr_object_names(self) -> str:
        return f"modules with forms over {self.base_ring()}"

    def _latex_(self) -> str:
        ...

    class SubcategoryMethods:
        @final
        @cached_method
        def base_ring(self) -> Ring:
            return self.base_category().base_ring()

        @final
        @cached_method
        def Bilinear(self) -> Category:
            return self._with_axiom("Bilinear")

        @final
        @cached_method
        def Quadratic(self) -> Category:
            return self._with_axiom("Quadratic")

        @final
        @cached_method
        def NonDegenerate(self) -> Category:
            return self._with_axiom("NonDegenerate")

        @final
        @cached_method
        def Integral(self) -> Category:
            return self._with_axiom("Integral")

        @final
        @cached_method
        def Rational(self) -> Category:
            return self._with_axiom("Rational")

        @final
        @cached_method
        def BilinearForms(self) -> BilinearFormSpace:
            return ModulesWithForms.BilinearForms(self.base_ring())

        @final
        @cached_method
        def QuadraticForms(self) -> QuadraticFormSpace:
            return ModulesWithForms.QuadraticForms(self.base_ring())

        @abstractmethod
        def zero_module(self) -> Parent:
            ...

    class TensorProducts(TensorProductsCategory):
        @final
        def extra_super_categories(self):
            return [self.base_category()]

        class Homsets(ModulesWithFormsHomsets):
            ...

    class CartesianProducts(CartesianProductsCategory):
        @final
        def extra_super_categories(self):
            return [self.base_category()]

        class Homsets(ModulesWithFormsHomsets):
            ...

    class Bilinear(CategoryWithAxiom_over_base_ring):
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        @final
        def additional_structure(self):
            return self.base_ring().BilinearForms()

        class ParentMethods(ABC):
            @abstractmethod
            def form(self) -> BilinearForm:
                ...

            @abstractmethod
            def associated_quadratic_module(self) -> RModuleWithForm:
                ...

            @final
            def b(self, left: RModuleElement, right: RModuleElement) -> RingElement:
                return self.form().evaluate(left, right)

    class Quadratic(CategoryWithAxiom_over_base_ring):
        @final
        def super_categories(self):
            return [ModulesWithForms(self.base_ring())]

        @final
        def additional_structure(self):
            return self.base_ring().QuadraticForms()

        class ParentMethods(ABC):
            @abstractmethod
            def form(self) -> QuadraticForm:
                ...

            @abstractmethod
            def associated_bilinear_module(self) -> RModuleWithForm:
                ...

            @final
            def q(self, value: RModuleElement) -> RingElement:
                return self.form().evaluate(value)

    class ParentMethods(Modules.ParentMethods, ABC):
        @abstractmethod
        def underlying_module(self) -> RModule:
            ...

        @abstractmethod
        def form(self) -> TwistedForm:
            ...

        @final
        def twist_endomorphism(self) -> RingMorphism:
            return self.form().twist_endomorphism()

        @abstractmethod
        def determinant(self) -> RingElement:
            ...

        @abstractmethod
        def discriminant(self) -> RingElement:
            ...

        @abstractmethod
        def orthogonal_group(self) -> RModAutset:
            ...

        @final
        def O(self) -> RModAutset:
            return self.orthogonal_group()

    class ElementMethods(Modules.ElementMethods, ABC):
        @final
        def form(self) -> TwistedForm:
            return self.parent().form()

    class MorphismMethods(Modules.MorphismMethods, ABC):
        @abstractmethod
        def adjoint(self) -> RModHomsetElement:
            ...
