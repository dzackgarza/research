# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/end_c.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
EndC ABC: The category of endomorphism categories.

Architecture:
- EndC is a subcategory of HomC
- Objects of EndC = End_C(X) categories for all X in base category C
- 1-cells of EndC = functors between End_C(X) categories
- 2-cells of EndC = natural transformations between those functors
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs
from .hom_c import (
    Hom_C_Category,
    Hom_C_Category_Functors,
    Hom_C_Category_EndoFunctors,
    Hom_C_Category_AutoFunctors,
    Hom_C_Category_NaturalTransformations,
    Hom_C_Category_EndoNaturalTransformations,
    Hom_C_Category_AutoNaturalTransformations,
)


# =============================================================================
# 0-cells (objects in EndC = End_C(X) categories)
# =============================================================================


@dataclass
class _EndC_0Cell_ABC(Hom_C_Category, ABC):
    """
    0-cells in EndC: the endomorphism categories End_C(X).

    These are the objects of EndC.
    """


# =============================================================================
# 1-cells (functors between End_C(X) categories)
# =============================================================================


@dataclass
class _EndC_1Cell_ABC(Hom_C_Category_Functors, ABC):
    """
    1-cells in EndC: functors F: End_C(X) → End_C(X').
    """


@dataclass
class _EndC_Endo1Cell_ABC(_EndC_1Cell_ABC, Hom_C_Category_EndoFunctors, ABC):
    """
    Endo-1-cells in EndC: endofunctors on a single End_C(X).
    """


@dataclass
class _EndC_Auto1Cell_ABC(_EndC_Endo1Cell_ABC, Hom_C_Category_AutoFunctors, ABC):
    """
    Auto-1-cells in EndC: autoequivalences on a single End_C(X).
    """


# =============================================================================
# 2-cells (natural transformations between functors)
# =============================================================================


@dataclass
class _EndC_2Cell_ABC(Hom_C_Category_NaturalTransformations, ABC):
    """
    2-cells in EndC: natural transformations η: F ⇒ G.
    """


@dataclass
class _EndC_Endo2Cell_ABC(_EndC_2Cell_ABC, Hom_C_Category_EndoNaturalTransformations, ABC):
    """
    Endo-2-cells in EndC: endo-natural transformations.
    """


@dataclass
class _EndC_Auto2Cell_ABC(_EndC_Endo2Cell_ABC, Hom_C_Category_AutoNaturalTransformations, ABC):
    """
    Auto-2-cells in EndC: natural isomorphisms.
    """


# =============================================================================
# EndC itself
# =============================================================================


@dataclass
class _EndC_ABC(CategoryABCs.HomC, ABC):
    """
    End_C: The category whose objects are all endomorphism categories End_C(X).

    This is a subcategory of HomC. Its structure:
    - Base: a category C
    - Objects (0-cells): End_C(X) for each object X in C
    - Morphisms (1-cells): functors F: End_C(X) → End_C(X')
    """

    @abstractmethod
    @override
    def objects(self) -> Sequence[_EndC_0Cell_ABC]:
        """All End_C(X) categories for objects X in base category."""
        ...

    @abstractmethod
    def object_from_domain(self, x: Annotated[Any, "Object x in the base category C."]) -> _EndC_0Cell_ABC:
        """Construct End_C(X) for specific X."""
        ...

    @abstractmethod
    def autc_subcategory(self) -> CategoryABCs.AutC:
        """Return the Aut_C subcategory."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _EndC_ABC

# Cells
## Objects
ZeroCell = _EndC_0Cell_ABC
## 1-Morphisms
OneCell = _EndC_1Cell_ABC
EndoOneCell = _EndC_Endo1Cell_ABC
AutoOneCell = _EndC_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _EndC_2Cell_ABC
EndoTwoCell = _EndC_Endo2Cell_ABC
AutoTwoCell = _EndC_Auto2Cell_ABC

# For use in AutC
End_C_Category = ZeroCell
End_C_Category_Functors = OneCell
End_C_Category_EndoFunctors = EndoOneCell
End_C_Category_AutoFunctors = AutoOneCell
End_C_Category_NaturalTransformations = TwoCell
End_C_Category_EndoNaturalTransformations = EndoTwoCell
End_C_Category_AutoNaturalTransformations = AutoTwoCell