"""Spec class for homsets in ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, final

if TYPE_CHECKING:
    from .types import (
        RModAutset,
        RModAutsetElement,
        RModEndset,
        RModEndsetElement,
    )

import sage.categories.category_with_axiom as _cwa
from sage.categories.category_with_axiom import CategoryWithAxiom, CategoryWithAxiom_over_base_ring
from sage.categories.groups import Groups
from sage.categories.homsets import HomsetsCategory
from sage.categories.magmatic_algebras import MagmaticAlgebras
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix
from sage.structure.parent import Parent

_cwa.all_axioms += ("Autset",)


class RModAutsetElement(ABC):
    r"""
    An automorphism of a finitely presented ``R``-module.

    Elements are units in ``End_R(M)`` and act as ``R``-linear morphisms
    ``M -> M``.
    """

    @abstractmethod
    def parent(self) -> RModAutset: ...

    @abstractmethod
    def domain(self) -> Parent: ...

    @final
    def codomain(self) -> Parent:
        return self.domain()

    @abstractmethod
    def __call__(self, value: Element) -> Element: ...

    @abstractmethod
    def endomorphism(self) -> RModEndsetElement: ...

    @abstractmethod
    def as_unit(self) -> RModEndsetElement: ...

    @abstractmethod
    def inverse(self) -> RModAutsetElement: ...

    @final
    def __invert__(self) -> RModAutsetElement:
        return self.inverse()

    @abstractmethod
    def to_matrix(self) -> Matrix: ...

    @abstractmethod
    def __mul__(self, other: RModAutsetElement) -> RModAutsetElement: ...


class RModAutset(ABC):
    r"""
    The group ``Aut_R(M)`` of units of ``End_R(M)``.

    The parent is a group object.  It carries its ambient endomorphism algebra
    and matrix realization; the free rank-``n`` specialization is ``GL_n(R)``.
    """

    @abstractmethod
    def module(self) -> Parent: ...

    @abstractmethod
    def endomorphism_algebra(self) -> RModEndset: ...

    @final
    def unit_group_of(self) -> RModEndset:
        return self.endomorphism_algebra()

    @abstractmethod
    def ambient_general_linear_group(self) -> Parent:
        r"""Ambient ``GL_n(R)`` for the chosen free presentation."""
        ...

    @abstractmethod
    def inclusion(self) -> Morphism:
        r"""Canonical map ``Aut_R(M) -> End_R(M)``."""
        ...

    @abstractmethod
    def identity(self) -> RModAutsetElement: ...

    @final
    def one(self) -> RModAutsetElement:
        return self.identity()

    @abstractmethod
    def from_endomorphism(self, value: RModEndsetElement) -> RModAutsetElement:
        r"""Coerce an invertible endomorphism into ``Aut_R(M)``."""
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[RModAutsetElement]: ...

    @abstractmethod
    def order(self) -> Any: ...

    @abstractmethod
    def __contains__(self, value: Any) -> bool: ...


class ModuleHomsets(HomsetsCategory):
    r"""Homsets of finitely presented ``R``-modules."""

    @final
    def extra_super_categories(self):
        from sage.categories.modules import Modules

        return [Modules(self.base_category().base_ring())]

    @final
    def base_ring(self) -> Ring:
        return self.base_category().base_ring()

    @final
    def _repr_object_names(self) -> str:
        return "homsets of modules"

    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        @abstractmethod
        def domain(self) -> Parent:
            ...

        @abstractmethod
        def codomain(self) -> Parent:
            ...

        @final
        @cached_method
        def base_ring(self) -> Ring:
            return self.domain().base_ring()

        @abstractmethod
        def matrix_space(self) -> Parent:
            r"""
            Matrix-space realization of ``Hom_R(M, N)``.

            For free modules this is the rectangular matrix space
            ``Mat_{rank(N) x rank(M)}(R)``.  For finite presentations, it is
            the subquotient of matrices between the chosen free presentations
            satisfying the descent conditions.
            """
            ...

        @abstractmethod
        def presentation_matrix_space(self) -> Parent:
            r"""
            Ambient free-presentation matrix space.

            If ``M`` and ``N`` are represented by presentations
            ``W_M -> V_M -> M`` and ``W_N -> V_N -> N``, a morphism is
            represented by a matrix in ``Hom_R(V_M, V_N)`` whose image of
            ``W_M`` lands in ``W_N``; two such matrices define the same map
            exactly when they differ by a map factoring through ``W_N``.
            """
            ...

        @abstractmethod
        def from_dict(self, mapping: Mapping[Element, Element]) -> Morphism:
            ...

        @abstractmethod
        def from_images(self, images: Sequence[Element]) -> Morphism:
            ...

        @abstractmethod
        def from_matrix(self, matrix_data: Matrix) -> Morphism:
            ...

        @abstractmethod
        def __call__(self, data: object) -> Morphism:
            ...

        @abstractmethod
        def __contains__(self, value: object) -> bool:
            ...

        @abstractmethod
        def zero(self) -> Morphism:
            ...

        @abstractmethod
        def _repr_(self) -> str:
            ...

        @abstractmethod
        def _latex_(self) -> str:
            ...

    class ElementMethods(ABC):
        ...

    class MorphismMethods(ABC):
        ...

    class Endset(CategoryWithAxiom_over_base_ring):
        r"""
        Endomorphism algebras ``End_R(M)``.

        Sage's category join makes ``Modules(R).Homsets().Endset()`` an
        associative unital algebra: homsets supply the ``R``-module,
        generic endsets supply the composition monoid, and magmatic algebras
        supply bilinearity.  Objects of this category must expose that
        algebra structure, not only the underlying homset.
        """

        @final
        def extra_super_categories(self):
            return [MagmaticAlgebras(self.base_category().base_ring())]

        @final
        def _repr_object_names(self) -> str:
            return "endomorphism algebras of modules"

        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            @final
            def module(self) -> Parent:
                return self.domain()

            @abstractmethod
            def identity(self) -> Morphism:
                ...

            @final
            def id(self) -> Morphism:
                return self.identity()

            @final
            def one(self) -> Morphism:
                return self.identity()

            @abstractmethod
            def zero(self) -> Morphism:
                ...

            @abstractmethod
            def square_matrix_space(self) -> Parent:
                r"""Ambient square matrix space for the free presentation."""
                ...

            @abstractmethod
            def matrix_algebra_quotient(self) -> Parent:
                r"""
                Matrix-algebra presentation of ``End_R(M)``.

                For a free rank-``n`` module this is ``Mat_n(R)``.  For a
                finitely presented module, it is the algebra of matrices in
                the free-presentation space that preserve the relations,
                modulo matrices inducing the zero map on the quotient.
                """
                ...

            @abstractmethod
            def from_matrix(self, matrix_data: Matrix) -> RModEndsetElement:
                ...

            @abstractmethod
            def Aut(self) -> RModAutset:
                ...

            @final
            def unit_group(self) -> RModAutset:
                return self.Aut()

        class ElementMethods(ABC):
            @abstractmethod
            def parent(self) -> RModEndset:
                ...

            @abstractmethod
            def is_unit(self) -> bool:
                ...

            @abstractmethod
            def inverse(self) -> RModEndsetElement:
                ...

            @final
            def __invert__(self) -> RModEndsetElement:
                return self.inverse()

            @abstractmethod
            def as_automorphism(self) -> RModAutsetElement:
                ...

        class MorphismMethods(ABC):
            ...

        class SubcategoryMethods:
            def Autset(self):
                """Return the subcategory of automorphism sets."""
                return self._with_axiom("Autset")

        class Autset(CategoryWithAxiom):
            r"""
            Automorphism groups of finitely presented ``R``-modules.

            ``Aut_R(M)`` is the group of units of ``End_R(M)``.  Reached via
            ``Endset()._with_axiom("Autset")``.
            """

            def extra_super_categories(self):
                return [Groups()]

            @final
            def _repr_object_names(self) -> str:
                return "automorphism groups of modules"

            def _latex_(self) -> str: ...

            class ParentMethods(RModAutset):
                @final
                def object(self) -> Parent:
                    return self.module()

                @final
                def endomorphism_set(self) -> RModEndset:
                    return self.endomorphism_algebra()

                @abstractmethod
                def matrix_group(self) -> Parent:
                    r"""
                    Matrix subgroup representing ``Aut_R(M)``.

                    For free ``M = R^n`` this is exactly ``GL_n(R)``.  For a
                    general finite presentation it is the subgroup of the
                    ambient ``GL(V)`` whose matrices preserve the presentation
                    and descend to automorphisms of the quotient module.
                    """
                    ...

            class ElementMethods(RModAutsetElement):
                ...


class ModulesWithFormsHomsets(ModuleHomsets):
    r"""Homset category for modules with forms."""

    # @override HomsetsCategory.extra_super_categories
    @final
    def extra_super_categories(self):
        return []

    # @override HomsetsCategory.base_ring
    @final
    def base_ring(self) -> Ring:
        return self.base_category().base_ring()

    # @override HomsetsCategory._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "homsets of modules with forms"

    # @override HomsetsCategory._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        ...

    class ElementMethods(ABC):
        ...

    class MorphismMethods(ABC):
        ...

    class Endset(CategoryWithAxiom_over_base_ring):
        # @override CategoryWithAxiom_over_base_ring._repr_object_names
        @final
        def _repr_object_names(self) -> str:
            return "endomorphism sets of modules with forms"

        # @override CategoryWithAxiom_over_base_ring._latex_
        def _latex_(self) -> str:
            ...

        class ParentMethods(ABC):
            ...

        class ElementMethods(ABC):
            ...

        class MorphismMethods(ABC):
            ...
