r"""Finite-rank free formed-module axiom chain.

This file owns the formed-module part of the lattice chain.  The lattice subtree
starts only at the named `Lattice` endpoint.
"""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, TypeVar, final, TypeAlias

from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..modules.subcategories.free import _FreeFiniteRank
from .subcategories.free_bilinear import FreeBilinearModulesMorphism
from .subcategories.integral import IntegralBilinearModulesCategory
from .subcategories.with_forms import FormedModulesMorphism

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ..types import (
        Category as CategoryType,
    )
    from ..types import (
        OrthogonalGroup,
        RModuleElement,
        RModuleMorphism,
        SubModule,
    )


class _BilinearForm(Protocol):
    def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement: ...


class FiniteRankFreeFormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms()``.
    """

    _base_category_class_and_axiom = (_FreeFiniteRank, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @abstractmethod
        def category(self) -> CategoryType: ...

        @final
        def has_form(self) -> bool:
            return True

        @abstractmethod
        def is_bilinear(self) -> bool: ...

        @abstractmethod
        def is_quadratic(self) -> bool: ...

        @abstractmethod
        def form(self) -> RModuleMorphism: ...

        @final
        def orthogonal_group(self) -> OrthogonalGroup:
            r"""Return the automorphism group preserving the form on this module.

            For ``M`` in a formed-module category ``C``, this is
            ``Aut_C(M) = {g in Aut_R(M) : form(gv, gw) = form(v, w)}``.
            """
            return self.category().AutCategory().Of(self)

    class ElementMethods: ...


    Bilinear = LazyImport(__name__, "FiniteRankFreeBilinearModulesCategory")


class FiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a bilinear form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms().Bilinear()``.
    """

    _base_category_class_and_axiom = (FiniteRankFreeFormedModulesCategory, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class ParentMethods:
        @abstractmethod
        def form(self) -> _BilinearForm: ...

        @final
        def is_bilinear(self) -> bool:
            return True

        @abstractmethod
        def is_symmetric(self) -> bool: ...

        @abstractmethod
        def is_alternating(self) -> bool: ...

        @abstractmethod
        def is_nondegenerate(self) -> bool: ...

        @abstractmethod
        def is_integral(self) -> bool: ...

        @abstractmethod
        def is_rational(self) -> bool: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)

    class ElementMethods: ...


    Symmetric = LazyImport(__name__, "SymmetricFiniteRankFreeBilinearModulesCategory")


class SymmetricFiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a symmetric bilinear form.

    Canonical chain::

        Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric()
    """

    _base_category_class_and_axiom = (
        FiniteRankFreeBilinearModulesCategory,
        "Symmetric",
    )
    _defining_predicates = ("is_symmetric",)

    class ParentMethods:
        @final
        def is_symmetric(self) -> bool:
            return True

        @abstractmethod
        def is_definite(self) -> bool: ...

        @abstractmethod
        def is_indefinite(self) -> bool: ...

        @abstractmethod
        def is_positive_definite(self) -> bool: ...

        @abstractmethod
        def is_negative_definite(self) -> bool: ...

        @abstractmethod
        def orthogonal_submodule_to(self, S: SubModule) -> SubModule: ...

    class ElementMethods: ...


    Nondegenerate = LazyImport(
        __name__, "NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory"
    )


class NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory(
    CategoryWithAxiom_over_base_ring
):
    r"""Finite-rank free modules with a nondegenerate symmetric bilinear form.

    Canonical chain::

        Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate()
    """

    _base_category_class_and_axiom = (
        SymmetricFiniteRankFreeBilinearModulesCategory,
        "Nondegenerate",
    )
    _defining_predicates = ("is_nondegenerate",)

    class ParentMethods:
        @final
        def is_nondegenerate(self) -> bool:
            return True

        @abstractmethod
        def radical(self) -> SubModule: ...

    class ElementMethods:
        @abstractmethod
        def is_anisotropic(self) -> bool: ...


    Integral = LazyImport(
        __name__, "IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory"
    )


class IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory(
    CategoryWithAxiom_over_base_ring
):
    r"""Integral nondegenerate symmetric bilinear forms on finite-rank free modules.

    Canonical chain::

        Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
    """

    _base_category_class_and_axiom = (
        NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
        "Integral",
    )
    _defining_predicates = ("is_integral",)

    class ParentMethods(IntegralBilinearModulesCategory.ParentMethods):
        @final
        def is_integral(self) -> bool:
            return True

        @final
        def is_rational(self) -> bool:
            return True

        @abstractmethod
        def is_even(self) -> bool: ...

    class ElementMethods: ...


    class SubcategoryMethods:
        @final
        def Lattice(self) -> Category:
            return self._with_axiom("Lattice")

    Lattice = LazyImport("category_specs.lattices.chain", "LatticesCategory")


FiniteRankFreeFormedModulesObject : TypeAlias = FiniteRankFreeFormedModulesCategory.ParentMethods
FiniteRankFreeFormedModulesElement : TypeAlias = FiniteRankFreeFormedModulesCategory.ElementMethods
FiniteRankFreeFormedModulesMorphism : TypeAlias = FormedModulesMorphism

FiniteRankFreeBilinearModulesObject = (
    FiniteRankFreeBilinearModulesCategory.ParentMethods
)
FiniteRankFreeBilinearModulesElement = (
    FiniteRankFreeBilinearModulesCategory.ElementMethods
)
FiniteRankFreeBilinearModulesMorphism : TypeAlias = FreeBilinearModulesMorphism

SymmetricFiniteRankFreeBilinearModulesObject = (
    SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
)
SymmetricFiniteRankFreeBilinearModulesElement = (
    SymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
)
SymmetricFiniteRankFreeBilinearModulesMorphism : TypeAlias = FreeBilinearModulesMorphism

NondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
)
NondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
)
NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    FreeBilinearModulesMorphism
)

IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    FreeBilinearModulesMorphism
)
