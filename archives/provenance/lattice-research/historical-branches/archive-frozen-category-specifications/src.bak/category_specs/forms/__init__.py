r"""Formed-module category surface.

``FormedModules(R)`` is the category of ``R``-modules equipped with a form.
It is the forms-subtree owner for the existing Sage-compatible spelling
``Modules(R).WithForms()``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, TypeAlias

from ..cat import Category
from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory
from . import chain as _chain
from .chain import (
    FiniteRankFreeBilinearModulesCategory as FiniteRankFreeBilinearModulesCategory,
)
from .chain import (
    FiniteRankFreeBilinearModulesElement as FiniteRankFreeBilinearModulesElement,
)
from .chain import (
    FiniteRankFreeBilinearModulesMorphism as FiniteRankFreeBilinearModulesMorphism,
)
from .chain import (
    FiniteRankFreeBilinearModulesObject as FiniteRankFreeBilinearModulesObject,
)
from .chain import (
    FiniteRankFreeFormedModulesCategory as FiniteRankFreeFormedModulesCategory,
)
from .chain import (
    FiniteRankFreeFormedModulesElement as FiniteRankFreeFormedModulesElement,
)
from .chain import (
    FiniteRankFreeFormedModulesMorphism as FiniteRankFreeFormedModulesMorphism,
)
from .chain import (
    FiniteRankFreeFormedModulesObject as FiniteRankFreeFormedModulesObject,
)
from .subcategories.bilinear import (
    BilinearModulesCategory as BilinearModulesCategory,
)
from .subcategories.bilinear import (
    BilinearModulesElement as BilinearModulesElement,
)
from .subcategories.bilinear import (
    BilinearModulesMorphism as BilinearModulesMorphism,
)
from .subcategories.bilinear import (
    BilinearModulesObject as BilinearModulesObject,
)
from .subcategories.quadratic import (
    QuadraticModulesCategory as QuadraticModulesCategory,
)
from .subcategories.quadratic import (
    QuadraticModulesElement as QuadraticModulesElement,
)
from .subcategories.quadratic import (
    QuadraticModulesMorphism as QuadraticModulesMorphism,
)
from .subcategories.quadratic import (
    QuadraticModulesObject as QuadraticModulesObject,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as TorsionQuadraticModulesCategory,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesElement as TorsionQuadraticModulesElement,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesMorphism as TorsionQuadraticModulesMorphism,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesObject as TorsionQuadraticModulesObject,
)
from .subcategories.with_forms import (
    FormedModulesCategory as FormedModulesCategory,
)
from .subcategories.with_forms import (
    FormedModulesElement as FormedModulesElement,
)
from .subcategories.with_forms import (
    FormedModulesMorphism as FormedModulesMorphism,
)
from .subcategories.with_forms import (
    FormedModulesObject as FormedModulesObject,
)

NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory
)
NondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesElement
)
NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism
)
NondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesObject
)
SymmetricFiniteRankFreeBilinearModulesCategory = (
    _chain.SymmetricFiniteRankFreeBilinearModulesCategory
)
SymmetricFiniteRankFreeBilinearModulesElement = (
    _chain.SymmetricFiniteRankFreeBilinearModulesElement
)
SymmetricFiniteRankFreeBilinearModulesMorphism = (
    _chain.SymmetricFiniteRankFreeBilinearModulesMorphism
)
SymmetricFiniteRankFreeBilinearModulesObject = (
    _chain.SymmetricFiniteRankFreeBilinearModulesObject
)

_IntegralNondegenerateSymmetricCategory = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory
)
_IntegralNondegenerateSymmetricElement = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement
)
_IntegralNondegenerateSymmetricMorphism = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism
)
_IntegralNondegenerateSymmetricObject = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject
)

IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _IntegralNondegenerateSymmetricCategory
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _IntegralNondegenerateSymmetricElement
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _IntegralNondegenerateSymmetricMorphism
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    _IntegralNondegenerateSymmetricObject
)

if TYPE_CHECKING:
    from ..types import Ring


def FormedModules(base_ring: Ring) -> Category:
    r"""Return the category of ``R``-modules equipped with a form."""
    from ..modules import Modules

    return cast(Category, Modules(base_ring, dispatch=False).WithForms())


FormedModulesHomCategory : TypeAlias = RModuleHomCategory
FormedModulesEndCategory : TypeAlias = RModuleEndCategory
FormedModulesAutCategory : TypeAlias = RModuleAutCategory
FormedModulesHom : TypeAlias = RModuleHomCategory.ParentMethods
FormedModulesEnd : TypeAlias = RModuleEndCategory.ParentMethods
FormedModulesAut : TypeAlias = RModuleAutCategory.ParentMethods
FormedModulesEndomorphism : TypeAlias = RModuleEndCategory.ElementMethods
FormedModulesAutomorphism : TypeAlias = RModuleAutCategory.ElementMethods

BilinearModulesHomCategory : TypeAlias = RModuleHomCategory
BilinearModulesEndCategory : TypeAlias = RModuleEndCategory
BilinearModulesAutCategory : TypeAlias = RModuleAutCategory
BilinearModulesHom : TypeAlias = RModuleHomCategory.ParentMethods
BilinearModulesEnd : TypeAlias = RModuleEndCategory.ParentMethods
BilinearModulesAut : TypeAlias = RModuleAutCategory.ParentMethods
BilinearModulesEndomorphism : TypeAlias = RModuleEndCategory.ElementMethods
BilinearModulesAutomorphism : TypeAlias = RModuleAutCategory.ElementMethods

QuadraticModulesHomCategory : TypeAlias = RModuleHomCategory
QuadraticModulesEndCategory : TypeAlias = RModuleEndCategory
QuadraticModulesAutCategory : TypeAlias = RModuleAutCategory
QuadraticModulesHom : TypeAlias = RModuleHomCategory.ParentMethods
QuadraticModulesEnd : TypeAlias = RModuleEndCategory.ParentMethods
QuadraticModulesAut : TypeAlias = RModuleAutCategory.ParentMethods
QuadraticModulesEndomorphism : TypeAlias = RModuleEndCategory.ElementMethods
QuadraticModulesAutomorphism : TypeAlias = RModuleAutCategory.ElementMethods

TorsionQuadraticModulesHomCategory : TypeAlias = RModuleHomCategory
TorsionQuadraticModulesEndCategory : TypeAlias = RModuleEndCategory
TorsionQuadraticModulesAutCategory : TypeAlias = RModuleAutCategory
TorsionQuadraticModulesHom : TypeAlias = RModuleHomCategory.ParentMethods
TorsionQuadraticModulesEnd : TypeAlias = RModuleEndCategory.ParentMethods
TorsionQuadraticModulesAut : TypeAlias = RModuleAutCategory.ParentMethods
TorsionQuadraticModulesEndomorphism : TypeAlias = RModuleEndCategory.ElementMethods
TorsionQuadraticModulesAutomorphism : TypeAlias = RModuleAutCategory.ElementMethods
