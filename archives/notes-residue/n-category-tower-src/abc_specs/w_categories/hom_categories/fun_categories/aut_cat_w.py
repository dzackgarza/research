# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/aut_cat_w.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
AutFun ABC: AutFun = Aut_{Cat_w}, the category of autoequivalence categories.

Architecture:
- AutFun is an automorphism category over Cat_w (base = Cat_w)
- Objects = AutFun(C) = Aut_{Cat_w}(C) for all categories C
- 1-cells = functors between autoequivalence categories
- 2-cells = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in AutFun = AutFun(C) autoequivalence categories)
# =============================================================================


@dataclass
class _AutoFun_0Cell_ABC(CategoryABCs.AutFun_x, ABC):
    """
    0-cells in AutFun: the autoequivalence categories AutFun(C).

    These are the objects of AutFun.
    """


# =============================================================================
# 1-cells (functors between AutFun(C) categories)
# =============================================================================


@dataclass
class _AutoFun_1Cell_ABC(CategoryABCs.Functor, ABC):
    """
    1-cells in AutFun: functors F: AutFun(C) → AutFun(C').
    """


@dataclass
class _AutoFun_Endo1Cell_ABC(_AutoFun_1Cell_ABC, CategoryABCs.EndoFunctor, ABC):
    """
    Endo-1-cells in AutFun: endofunctors on a single AutFun(C).
    """


@dataclass
class _AutoFun_Auto1Cell_ABC(_AutoFun_Endo1Cell_ABC, CategoryABCs.AutoFunctor, ABC):
    """
    Auto-1-cells in AutFun: autoequivalences on a single AutFun(C).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _AutoFun_2Cell_ABC(CategoryABCs.NaturalTransformation, ABC):
    """
    2-cells in AutFun: natural transformations η: F ⇒ G.
    """


@dataclass
class _AutoFun_Endo2Cell_ABC(_AutoFun_2Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-2-cells in AutFun: endo-natural transformations.
    """


@dataclass
class _AutoFun_Auto2Cell_ABC(_AutoFun_Endo2Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-2-cells in AutFun: natural isomorphisms.
    """


# =============================================================================
# AutFun itself
# =============================================================================


@dataclass
class _AutoFun_ABC(CategoryABCs.AutC, ABC):
    """
    AutFun = Aut_{Cat_w}: The category whose objects are autoequivalence categories Aut(C) for categories C and whose morphisms are functors Aut(C) -> Aut(D).

    This is an automorphism category with base = Cat_w. Its structure:
    - Base: Cat_w (the ω-category of categories)
    - Objects (0-cells): AutFun(C) = Aut_{Cat_w}(C) for any category C
    - Morphisms (1-cells): functors between autoequivalence categories
    """

    @abstractmethod
    @override
    def objects(self) -> Sequence[_AutoFun_0Cell_ABC]:
        """All autoequivalence categories Aut(C)."""
        ...

    @abstractmethod
    @override
    def morphisms(self) -> Sequence[_AutoFun_1Cell_ABC]:
        """All functors between autoequivalence categories."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _AutoFun_ABC

# Cells
## Objects
ZeroCell = _AutoFun_0Cell_ABC
## 1-Morphisms
OneCell = _AutoFun_1Cell_ABC
EndoOneCell = _AutoFun_Endo1Cell_ABC
AutoOneCell = _AutoFun_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _AutoFun_2Cell_ABC
EndoTwoCell = _AutoFun_Endo2Cell_ABC
AutoTwoCell = _AutoFun_Auto2Cell_ABC

# Misc Extra
# ...
