# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/hom_cat_w.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Fun ABC: Fun = Hom_{Cat_w}, the category of functor categories.

Architecture:
- Fun is a hom-category over Cat_w (base = Cat_w)
- Objects = Fun(C, D) for all categories C, D
- 1-cells = functors between functor categories
- 2-cells = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in Fun = Fun(C, D) functor categories)
# =============================================================================


@dataclass
class _Fun_0Cell_ABC(CategoryABCs.Fun_xy, ABC):
    """
    0-cells in Fun: the functor categories Fun(C, D).

    These are the objects of Fun.
    """


# =============================================================================
# 1-cells (functors between Fun(C, D) categories)
# =============================================================================


@dataclass
class _Fun_1Cell_ABC(CategoryABCs.Functor, ABC):
    """
    1-cells in Fun: functors F: Fun(C, D) → Fun(C', D').
    """


@dataclass
class _Fun_Endo1Cell_ABC(_Fun_1Cell_ABC, CategoryABCs.EndoFunctor, ABC):
    """
    Endo-1-cells in Fun: endofunctors on a single Fun(C, D).
    """


@dataclass
class _Fun_Auto1Cell_ABC(_Fun_Endo1Cell_ABC, CategoryABCs.AutoFunctor, ABC):
    """
    Auto-1-cells in Fun: autoequivalences on a single Fun(C, D).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _Fun_2Cell_ABC(CategoryABCs.NaturalTransformation, ABC):
    """
    2-cells in Fun: natural transformations η: F ⇒ G.
    """


@dataclass
class _Fun_Endo2Cell_ABC(_Fun_2Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-2-cells in Fun: endo-natural transformations.
    """


@dataclass
class _Fun_Auto2Cell_ABC(_Fun_Endo2Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-2-cells in Fun: natural isomorphisms.
    """


# =============================================================================
# Fun itself
# =============================================================================


@dataclass
class _Fun_ABC(CategoryABCs.HomC, ABC):
    """
    Fun = Hom_{Cat_w}: The category whose objects are functor categories.

    This is a hom-category with base = Cat_w. Its structure:
    - Base: Cat_w (the ω-category of categories)
    - Objects (0-cells): Fun(C, D) = Hom_{Cat_w}(C, D) for any C, D
    - Morphisms (1-cells): functors between functor categories
    """

    @final
    @abstractmethod
    @override
    def objects(self) -> Sequence[_Fun_0Cell_ABC]:
        """All functor categories Fun(C, D)."""
        ...

    @final
    @abstractmethod
    def fun_xy(
        self, x: CategoryABCs.Nontrivial_TwoCategory, y: CategoryABCs.Nontrivial_TwoCategory
    ) -> _Fun_0Cell_ABC:
        """Construct Fun(x, y) for specific x and y."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _Fun_ABC

# Cells
## Objects
ZeroCell = _Fun_0Cell_ABC
## 1-Morphisms
OneCell = _Fun_1Cell_ABC
EndoOneCell = _Fun_Endo1Cell_ABC
AutoOneCell = _Fun_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _Fun_2Cell_ABC
EndoTwoCell = _Fun_Endo2Cell_ABC
AutoTwoCell = _Fun_Auto2Cell_ABC

# Misc Extra
# ...