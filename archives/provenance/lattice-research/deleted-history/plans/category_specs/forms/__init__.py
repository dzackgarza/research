r"""Formed-module category surface.

``FormedModules(R)`` is the category of ``R``-modules equipped with a form.
It is the forms-subtree owner for the existing Sage-compatible spelling
``Modules(R).WithForms()``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory
from .chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement,
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism,
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject,
    NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
    NondegenerateSymmetricFiniteRankFreeBilinearModulesElement,
    NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism,
    NondegenerateSymmetricFiniteRankFreeBilinearModulesObject,
    SymmetricFiniteRankFreeBilinearModulesCategory,
    SymmetricFiniteRankFreeBilinearModulesElement,
    SymmetricFiniteRankFreeBilinearModulesMorphism,
    SymmetricFiniteRankFreeBilinearModulesObject,
    FiniteRankFreeBilinearModulesCategory,
    FiniteRankFreeBilinearModulesElement,
    FiniteRankFreeBilinearModulesMorphism,
    FiniteRankFreeBilinearModulesObject,
    FiniteRankFreeFormedModulesCategory,
    FiniteRankFreeFormedModulesElement,
    FiniteRankFreeFormedModulesMorphism,
    FiniteRankFreeFormedModulesObject,
)
from .subcategories.bilinear import (
    BilinearModulesCategory,
    BilinearModulesElement,
    BilinearModulesMorphism,
    BilinearModulesObject,
)
from .subcategories.quadratic import (
    QuadraticModulesCategory,
    QuadraticModulesElement,
    QuadraticModulesMorphism,
    QuadraticModulesObject,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory,
    TorsionQuadraticModulesElement,
    TorsionQuadraticModulesMorphism,
    TorsionQuadraticModulesObject,
)
from .subcategories.with_forms import (
    FormedModulesCategory,
    FormedModulesElement,
    FormedModulesMorphism,
    FormedModulesObject,
)

if TYPE_CHECKING:
    from ..cat import Category
    from ..types import Ring


@final
def FormedModules(base_ring: Ring) -> Category:
    r"""Return the category of ``R``-modules equipped with a form."""
    from ..modules import Modules

    return Modules(base_ring, dispatch=False).WithForms()

FormedModulesHomCategory = RModuleHomCategory
FormedModulesEndCategory = RModuleEndCategory
FormedModulesAutCategory = RModuleAutCategory
FormedModulesHom = RModuleHomCategory.ParentMethods
FormedModulesEnd = RModuleEndCategory.ParentMethods
FormedModulesAut = RModuleAutCategory.ParentMethods
FormedModulesEndomorphism = RModuleEndCategory.ElementMethods
FormedModulesAutomorphism = RModuleAutCategory.ElementMethods

BilinearModulesHomCategory = RModuleHomCategory
BilinearModulesEndCategory = RModuleEndCategory
BilinearModulesAutCategory = RModuleAutCategory
BilinearModulesHom = RModuleHomCategory.ParentMethods
BilinearModulesEnd = RModuleEndCategory.ParentMethods
BilinearModulesAut = RModuleAutCategory.ParentMethods
BilinearModulesEndomorphism = RModuleEndCategory.ElementMethods
BilinearModulesAutomorphism = RModuleAutCategory.ElementMethods

QuadraticModulesHomCategory = RModuleHomCategory
QuadraticModulesEndCategory = RModuleEndCategory
QuadraticModulesAutCategory = RModuleAutCategory
QuadraticModulesHom = RModuleHomCategory.ParentMethods
QuadraticModulesEnd = RModuleEndCategory.ParentMethods
QuadraticModulesAut = RModuleAutCategory.ParentMethods
QuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
QuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods

TorsionQuadraticModulesHomCategory = RModuleHomCategory
TorsionQuadraticModulesEndCategory = RModuleEndCategory
TorsionQuadraticModulesAutCategory = RModuleAutCategory
TorsionQuadraticModulesHom = RModuleHomCategory.ParentMethods
TorsionQuadraticModulesEnd = RModuleEndCategory.ParentMethods
TorsionQuadraticModulesAut = RModuleAutCategory.ParentMethods
TorsionQuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
TorsionQuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods
