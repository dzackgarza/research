# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/end_cat_w.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
EndFun ABC: EndFun = End_{Cat_w}, the category of endofunctor categories.

Architecture:
- EndFun is an endomorphism category over Cat_w (base = Cat_w)
- Objects = EndFun(C) = End_{Cat_w}(C) for all categories C
- 1-cells = functors between endofunctor categories
- 2-cells = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in EndFun = EndFun(C) endofunctor categories)
# =============================================================================


@dataclass
class _EndoFun_0Cell_ABC(CategoryABCs.EndoFun_x, ABC):
    """
    0-cells in EndFun: the endofunctor categories EndFun(C).

    These are the objects of EndFun.
    """


# =============================================================================
# 1-cells (functors between EndFun(C) categories)
# =============================================================================


@dataclass
class _EndoFun_1Cell_ABC(CategoryABCs.Functor, ABC):
    """
    1-cells in EndFun: functors F: EndFun(C) → EndFun(C').
    """


@dataclass
class _EndoFun_Endo1Cell_ABC(_EndoFun_1Cell_ABC, CategoryABCs.EndoFunctor, ABC):
    """
    Endo-1-cells in EndFun: endofunctors on a single EndFun(C).
    """


@dataclass
class _EndoFun_Auto1Cell_ABC(_EndoFun_Endo1Cell_ABC, CategoryABCs.AutoFunctor, ABC):
    """
    Auto-1-cells in EndFun: autoequivalences on a single EndFun(C).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _EndoFun_2Cell_ABC(CategoryABCs.NaturalTransformation, ABC):
    """
    2-cells in EndFun: natural transformations η: F ⇒ G.
    """


@dataclass
class _EndoFun_Endo2Cell_ABC(_EndoFun_2Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-2-cells in EndFun: endo-natural transformations.
    """


@dataclass
class _EndoFun_Auto2Cell_ABC(_EndoFun_Endo2Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-2-cells in EndFun: natural isomorphisms.
    """


# =============================================================================
# EndFun itself
# =============================================================================


@dataclass
class _EndoFun_ABC(CategoryABCs.EndC, ABC):
    """
    EndFun = End_{Cat_w}: The category whose objects are endofunctor categories.

    This is an endomorphism category with base = Cat_w. Its structure:
    - Base: Cat_w (the ω-category of categories)
    - Objects (0-cells): EndFun(C) = End_{Cat_w}(C) for any category C
    - Morphisms (1-cells): functors between endofunctor categories
    """

    @final
    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.Cat_w:
        """Return Cat_w, the ambient category."""
        ...

    @final
    @abstractmethod
    @override
    def objects(self) -> Sequence[_EndoFun_0Cell_ABC]:
        """All endofunctor categories EndFun(C)."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _EndoFun_ABC

# Cells
## Objects
ZeroCell = _EndoFun_0Cell_ABC
## 1-Morphisms
OneCell = _EndoFun_1Cell_ABC
EndoOneCell = _EndoFun_Endo1Cell_ABC
AutoOneCell = _EndoFun_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _EndoFun_2Cell_ABC
EndoTwoCell = _EndoFun_Endo2Cell_ABC
AutoTwoCell = _EndoFun_Auto2Cell_ABC

# Misc Extra
# ...
