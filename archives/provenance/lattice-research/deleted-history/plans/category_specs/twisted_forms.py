"""Spec class for the TwistedForms category."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Self, final

import sage.categories.category_with_axiom as _cwa
from sage.categories.category import Category
from sage.categories.category_over_base_ring import Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.rings.integer import Integer
from sage.structure.element import Matrix

from .types import (
    BilinearForm,
    BilinearFormSpace,
    QuadraticForm,
    QuadraticFormSpace,
    RingMorphism,
    RModule,
    TensorProductRModule,
    TwistedForm,
)

_cwa.all_axioms += ("Bilinear", "Quadratic", "Linear")


class TwistedForms(Category_over_base_ring):
    r"""
    The category of twisted form spaces over a base ring R.

    Objects in this category are Hom-spaces Hom_R(T_R(M)[p,q], S)^\sigma. Here:
    - T_R(M) := \bioplus_{n} \bigoplus_{p+q=n} M^{\otimes_R p} \otimes_R (M^*)^{\otimes_R q}
      is the full bigraded tensor algebra of M
    - T_R(M)[p,q] := M \otimes_R ... \otimes_R M \otimes_R M^* \otimes_R ... \otimes_R M^*
      is the (p,q)-th graded piece with p factors of M and q factors of M^*
    - S is any R-module, typically R or K/R (not necessarily finitely generated)
    - \sigma is a ring endomorphism of R

    These forms satisfy the semilinearity condition:
    f(r.m) = \sigma(r).f(m)

    These can equivalently be regarded as standard R-module morphisms
    in Hom_R(T_R(M)[p,q], S^\sigma) where S^\sigma has a twisted R-module
    structure r.s := \sigma(r).s where the RHS action is the original
    R-module structure on S.
    """

    @final
    def super_categories(self) -> list[Category]:
        from .modules import Modules
        return [Modules(self.base_ring()).TensorProducts().Homsets()]

    @final
    def _repr_object_names(self) -> str:
        return "twisted form spaces"

    def _latex_(self) -> str:
        ...

    class SubcategoryMethods:
        @final
        def Bilinear(self):
            return self._with_axiom("Bilinear")

        @final
        def Quadratic(self):
            return self._with_axiom("Quadratic")

        @final
        def Linear(self):
            return self._with_axiom("Linear")

    class ParentMethods(ABC):
        @abstractmethod
        def base_module(self) -> RModule | TensorProductRModule:
            r"""The underlying module M."""
            ...

        @abstractmethod
        def tensor_degree(self) -> tuple[Integer, Integer]:
            r"""Tensor degree as a pair (p, q)."""
            ...

        @abstractmethod
        def twist_endomorphism(self) -> RingMorphism:
            r"""The twist automorphism \sigma in Aut(R)."""
            ...

    class ElementMethods(ABC):
        @final
        def tensor_degree(self) -> tuple[Integer, Integer]:
            return self.parent().tensor_degree()

        @final
        def twist_endomorphism(self) -> RingMorphism:
            return self.parent().twist_endomorphism()

        @final
        def base_module(self) -> RModule | TensorProductRModule:
            return self.parent().base_module()

    class MorphismMethods(ABC):
        ...

    class Linear(DualObjectsCategory, CategoryWithAxiom_over_base_ring):
        r"""
        Linear form spaces.

        Degree (1,0) with \sigma = id_R. Inherits from DualObjectsCategory
        to provide the M^* = Hom_R(M, R) construction logic.
        """
        _functor_category = "DualObjects"

        def __init__(self, base_category):
            super().__init__(base_category, base_category.base_ring())

        def _repr_object_names(self) -> str:
            return f"linear forms on {self.base_category()._repr_object_names()}"

        def extra_super_categories(self) -> list[Category]:
            from .modules import Modules
            R = self.base_ring()
            return [Modules(R), TwistedForms(R)]

        class ParentMethods(ABC):

            @classmethod
            @abstractmethod
            def from_module(cls, M) -> Self:
                r"""
                Must define how to construct M^* from M, regarding
                the generators of M^* as e_i^* such that e_i^*(e_j) = \delta_{ij}
                """
                ...

            @final
            def tensor_degree(self) -> tuple[Integer, Integer]:
                return (Integer(1), Integer(0))

            @final
            def dual_of(self) -> RModule | TensorProductRModule:
                r"""The module M such that this space is M^* = Hom_R(M, R)."""
                return self.base_module()

            @abstractmethod
            def natural_pairing(self) -> TwistedForm:
                r"""The (1,1) form b in Hom_R(M \otimes_R M^*, R)
                defined by b(v, w^*) := w^*(v) in R.
                """
                ...

        class ElementMethods(ABC):
            r"""Linear functionals"""
            ...

    class Bilinear(CategoryWithAxiom_over_base_ring):
        r"""
        Symmetric bilinear form spaces.

        Degree (2,0) with \sigma = id_R.
        """
        @final
        def _repr_object_names(self) -> str:
            return "bilinear twisted form spaces"

        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @final
            def tensor_degree(self) -> tuple[Integer, Integer]:
                return (Integer(2), Integer(0))

            @abstractmethod
            def associated_quadratic_form_space(self) -> QuadraticFormSpace:
                ...

        class ElementMethods(ABC):
            r"""Bilinear forms"""
            @abstractmethod
            def gram_matrix(self) -> Matrix:
                ...

            @abstractmethod
            def associated_quadratic_form(self) -> QuadraticForm:
                ...

    class Quadratic(CategoryWithAxiom_over_base_ring):
        r"""
        Quadratic form spaces.

        Degree (1,0) with semilinearity twist \sigma(r) = r^2.
        """
        @final
        def _repr_object_names(self) -> str:
            return "quadratic twisted form spaces"

        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @final
            def tensor_degree(self) -> tuple[Integer, Integer]:
                return (Integer(1), Integer(0))

            @abstractmethod
            def associated_bilinear_form_space(self) -> BilinearFormSpace:
                ...

        class ElementMethods(ABC):
            r"""Quadratic forms"""

            @abstractmethod
            def gram_matrix(self) -> Matrix:
                r"""
                A canonical choice of a matrix such that f(x) = x^tMx
                """
                ...

            @abstractmethod
            def associated_bilinear_form(self) -> BilinearForm:
                ...
