# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/hom_c.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
HomC ABC: The category of hom-categories.

Architecture:
- HomC is a category (0-cell in Cat)
- Objects of HomC = Hom_C(X,Y) categories for all X,Y in base category C
- 1-cells of HomC = functors between Hom_C(X,Y) categories
- 2-cells of HomC = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in HomC = Hom_C(X,Y) categories)
# =============================================================================


@dataclass
class _HomC_0Cell_ABC(CategoryABCs.HomC_xy, ABC):
    """
    0-cells in HomC: the hom-categories Hom_C(X,Y).

    These are the objects of HomC.
    """


# =============================================================================
# 1-cells (functors between Hom_C(X,Y) categories)
# =============================================================================


@dataclass
class _HomC_1Cell_ABC(CategoryABCs.Functor, ABC):
    """
    1-cells in HomC: functors F: Hom_C(X,Y) → Hom_C(X',Y').
    """


@dataclass
class _HomC_Endo1Cell_ABC(_HomC_1Cell_ABC, CategoryABCs.EndoFunctor, ABC):
    """
    Endo-1-cells in HomC: endofunctors on a single Hom_C(X,Y).
    """


@dataclass
class _HomC_Auto1Cell_ABC(_HomC_Endo1Cell_ABC, CategoryABCs.AutoFunctor, ABC):
    """
    Auto-1-cells in HomC: autoequivalences on a single Hom_C(X,Y).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _HomC_2Cell_ABC(CategoryABCs.NaturalTransformation, ABC):
    """
    2-cells in HomC: natural transformations η: F ⇒ G.
    """


@dataclass
class _HomC_Endo2Cell_ABC(_HomC_2Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-2-cells in HomC: endo-natural transformations.
    """


@dataclass
class _HomC_Auto2Cell_ABC(_HomC_Endo2Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-2-cells in HomC: natural isomorphisms.
    """


# =============================================================================
# HomC itself
# =============================================================================


@dataclass
class _HomC_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    Hom_C: The category whose objects are all hom-categories Hom_C(X,Y).

    This is a 0-cell in Cat. Its structure:
    - Base: a category C
    - Objects (0-cells): Hom_C(X,Y) for each pair (X,Y) of objects in C
    - Morphisms (1-cells): functors F: Hom_C(X,Y) → Hom_C(X',Y')
    """

    base_category: CategoryABCs.Nontrivial_TwoCategory

    @abstractmethod
    def objects(self) -> Sequence[_HomC_0Cell_ABC]:
        """All Hom_C(X,Y) categories for pairs X,Y in base category."""
        ...

    @final
    @abstractmethod
    def object_from_domain_and_codomain(
        self,
        domain: CategoryABCs.Object,
        codomain: CategoryABCs.Object
    ) -> _HomC_0Cell_ABC:
        """Construct Hom_C(X, Y) for specific X and Y."""
        ...

    @final
    @abstractmethod
    def amb(self) -> CategoryABCs.Cat_w:
        """Every Hom_C is an object in Cat_w"""
        ...


# Semantic exports

# This category:
CategoryDefinition = _HomC_ABC

# Cells
## Objects
ZeroCell = _HomC_0Cell_ABC
## 1-Morphisms
OneCell = _HomC_1Cell_ABC
EndoOneCell = _HomC_Endo1Cell_ABC
AutoOneCell = _HomC_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _HomC_2Cell_ABC
EndoTwoCell = _HomC_Endo2Cell_ABC
AutoTwoCell = _HomC_Auto2Cell_ABC

# Misc Extra
Hom_C_Category = ZeroCell
Hom_C_Category_Functors = OneCell
Hom_C_Category_EndoFunctors = EndoOneCell
Hom_C_Category_AutoFunctors = AutoOneCell
Hom_C_Category_NaturalTransformations = TwoCell
Hom_C_Category_EndoNaturalTransformations = EndoTwoCell
Hom_C_Category_AutoNaturalTransformations = AutoTwoCell
