# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/aut_c.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
AutC ABC: The category of automorphism categories.

Architecture:
- AutC is a subcategory of EndC
- Objects of AutC = Aut_C(X) categories for all X in base category C
- 1-cells of AutC = functors between Aut_C(X) categories
- 2-cells of AutC = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs
from .end_c import (
    End_C_Category,
    End_C_Category_Functors,
    End_C_Category_EndoFunctors,
    End_C_Category_AutoFunctors,
    End_C_Category_NaturalTransformations,
    End_C_Category_EndoNaturalTransformations,
    End_C_Category_AutoNaturalTransformations,
)


# =============================================================================
# 0-cells (objects in AutC = Aut_C(X) categories)
# =============================================================================


@dataclass
class _AutC_0Cell_ABC(End_C_Category, ABC):
    """
    0-cells in AutC: the automorphism categories Aut_C(X).

    These are the objects of AutC.
    """


# =============================================================================
# 1-cells (functors between Aut_C(X) categories)
# =============================================================================


@dataclass
class _AutC_1Cell_ABC(End_C_Category_Functors, ABC):
    """
    1-cells in AutC: functors F: Aut_C(X) → Aut_C(X').
    """


@dataclass
class _AutC_Endo1Cell_ABC(_AutC_1Cell_ABC, End_C_Category_EndoFunctors, ABC):
    """
    Endo-1-cells in AutC: endofunctors on a single Aut_C(X).
    """


@dataclass
class _AutC_Auto1Cell_ABC(_AutC_Endo1Cell_ABC, End_C_Category_AutoFunctors, ABC):
    """
    Auto-1-cells in AutC: autoequivalences on a single Aut_C(X).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _AutC_2Cell_ABC(End_C_Category_NaturalTransformations, ABC):
    """
    2-cells in AutC: natural transformations η: F ⇒ G.
    """


@dataclass
class _AutC_Endo2Cell_ABC(_AutC_2Cell_ABC, End_C_Category_EndoNaturalTransformations, ABC):
    """
    Endo-2-cells in AutC: endo-natural transformations.
    """


@dataclass
class _AutC_Auto2Cell_ABC(_AutC_Endo2Cell_ABC, End_C_Category_AutoNaturalTransformations, ABC):
    """
    Auto-2-cells in AutC: natural isomorphisms.
    """


# =============================================================================
# AutC itself
# =============================================================================


@dataclass
class _AutC_ABC(CategoryABCs.EndC, ABC):
    """
    Aut_C: The category whose objects are all automorphism categories Aut_C(X).

    This is a subcategory of EndC. Its structure:
    - Base: a category C
    - Objects (0-cells): Aut_C(X) for each object X in C
    - Morphisms (1-cells): functors F: Aut_C(X) → Aut_C(X')
    """

    @abstractmethod
    @override
    def objects(self) -> Sequence[_AutC_0Cell_ABC]:
        """All Aut_C(X) categories for objects X in base category."""
        ...

    @final
    @abstractmethod
    def endc_supercategory(self) -> CategoryABCs.EndC:
        """Return the End_C supercategory."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _AutC_ABC

# Cells
## Objects
ZeroCell = _AutC_0Cell_ABC
## 1-Morphisms
OneCell = _AutC_1Cell_ABC
EndoOneCell = _AutC_Endo1Cell_ABC
AutoOneCell = _AutC_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _AutC_2Cell_ABC
EndoTwoCell = _AutC_Endo2Cell_ABC
AutoTwoCell = _AutC_Auto2Cell_ABC

# Semantic aliases for external use
Aut_C_Category = ZeroCell
Aut_C_Category_Functors = OneCell
Aut_C_Category_EndoFunctors = EndoOneCell
Aut_C_Category_AutoFunctors = AutoOneCell
Aut_C_Category_NaturalTransformations = TwoCell
Aut_C_Category_EndoNaturalTransformations = EndoTwoCell
Aut_C_Category_AutoNaturalTransformations = AutoTwoCell
