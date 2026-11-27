r"""Finite-rank free formed-module axiom chain.

This file owns the formed-module part of the lattice chain.  The lattice subtree
starts only at the named `Lattice` endpoint.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..modules.subcategories.free import _FreeFiniteRank

if TYPE_CHECKING:
    from ..types import DiscriminantGroup, Lattice, OrthogonalGroup, RModuleElement, RModuleMorphism, SubModule


class FiniteRankFreeFormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms()``.
    """

    _base_category_class_and_axiom = (_FreeFiniteRank, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @final
        def has_form(self) -> bool:
            return True

        @abstract_method
        def is_bilinear(self) -> bool: ...

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def form(self) -> RModuleMorphism: ...

        @final
        def orthogonal_group(self) -> OrthogonalGroup:
            r"""Return the automorphism group preserving the form on this module.

            For ``M`` in a formed-module category ``C``, this is
            ``Aut_C(M) = {g in Aut_R(M) : form(gv, gw) = form(v, w)}``.
            """
            return self.category().AutCategory().Of(self)

    class ElementMethods: ...
    class MorphismMethods: ...

    Bilinear = LazyImport(__name__, "FiniteRankFreeBilinearModulesCategory")


class FiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a bilinear form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms().Bilinear()``.
    """

    _base_category_class_and_axiom = (FiniteRankFreeFormedModulesCategory, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class ParentMethods:
        @final
        def is_bilinear(self) -> bool:
            return True

        @abstract_method
        def is_symmetric(self) -> bool: ...

        @abstract_method
        def is_alternating(self) -> bool: ...

        @abstract_method
        def is_nondegenerate(self) -> bool: ...

        @abstract_method
        def is_integral(self) -> bool: ...

        @abstract_method
        def is_rational(self) -> bool: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)

    class ElementMethods: ...
    class MorphismMethods: ...

    Symmetric = LazyImport(__name__, "SymmetricFiniteRankFreeBilinearModulesCategory")


class SymmetricFiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a symmetric bilinear form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric()``.
    """

    _base_category_class_and_axiom = (FiniteRankFreeBilinearModulesCategory, "Symmetric")
    _defining_predicates = ("is_symmetric",)

    class ParentMethods:
        @final
        def is_symmetric(self) -> bool:
            return True

        @abstract_method
        def is_definite(self) -> bool: ...

        @abstract_method
        def is_indefinite(self) -> bool: ...

        @abstract_method
        def is_positive_definite(self) -> bool: ...

        @abstract_method
        def is_negative_definite(self) -> bool: ...

        @abstract_method
        def orthogonal_submodule_to(self, S: SubModule) -> SubModule: ...

    class ElementMethods: ...
    class MorphismMethods: ...

    Nondegenerate = LazyImport(__name__, "NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory")


class NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules with a nondegenerate symmetric bilinear form.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate()``.
    """

    _base_category_class_and_axiom = (SymmetricFiniteRankFreeBilinearModulesCategory, "Nondegenerate")
    _defining_predicates = ("is_nondegenerate",)

    class ParentMethods:
        @final
        def is_nondegenerate(self) -> bool:
            return True

        @abstract_method
        def radical(self) -> SubModule: ...

    class ElementMethods:
        @abstract_method
        def is_anisotropic(self) -> bool: ...

    class MorphismMethods: ...

    Integral = LazyImport(__name__, "IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory")


class IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Integral nondegenerate symmetric bilinear forms on finite-rank free modules.

    Canonical chain: ``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()``.
    """

    _base_category_class_and_axiom = (NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory, "Integral")
    _defining_predicates = ("is_integral",)

    class ParentMethods:
        @final
        def is_integral(self) -> bool:
            return True

        @final
        def is_rational(self) -> bool:
            return True

        @abstract_method
        def dual_lattice(self) -> Lattice: ...

        @abstract_method
        def inclusion_morphism(self) -> RModuleMorphism: ...

        @abstract_method
        def discriminant_group(self) -> DiscriminantGroup: ...

        @final
        def is_unimodular(self) -> bool:
            return self.discriminant_group().is_trivial()

        @abstract_method
        def is_even(self) -> bool: ...

    class ElementMethods: ...

    class MorphismMethods: ...

    class SubcategoryMethods:
        @cached_method
        @final
        def Lattice(self) -> Category:
            return self._with_axiom("Lattice")

    Lattice = LazyImport("category_specs.lattices.chain", "LatticesCategory")


FiniteRankFreeFormedModulesObject = FiniteRankFreeFormedModulesCategory.ParentMethods
FiniteRankFreeFormedModulesElement = FiniteRankFreeFormedModulesCategory.ElementMethods
FiniteRankFreeFormedModulesMorphism = FiniteRankFreeFormedModulesCategory.MorphismMethods

FiniteRankFreeBilinearModulesObject = FiniteRankFreeBilinearModulesCategory.ParentMethods
FiniteRankFreeBilinearModulesElement = FiniteRankFreeBilinearModulesCategory.ElementMethods
FiniteRankFreeBilinearModulesMorphism = FiniteRankFreeBilinearModulesCategory.MorphismMethods

SymmetricFiniteRankFreeBilinearModulesObject = SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
SymmetricFiniteRankFreeBilinearModulesElement = SymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
SymmetricFiniteRankFreeBilinearModulesMorphism = SymmetricFiniteRankFreeBilinearModulesCategory.MorphismMethods

NondegenerateSymmetricFiniteRankFreeBilinearModulesObject = NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
NondegenerateSymmetricFiniteRankFreeBilinearModulesElement = NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.MorphismMethods

IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.MorphismMethods
)
