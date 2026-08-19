# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/aut_c_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
AutC_x ABC: The automorphism category Aut_C(X) for a specific object X.

Architecture:
- Aut_C(X) is an object (0-cell) in AutC
- Objects of Aut_C(X) = automorphisms f: X → X in base category C (invertible endomorphisms)
- 1-cells of Aut_C(X) = 2-cells between those automorphisms
- 2-cells of Aut_C(X) = 3-cells (modifications) between 2-cells
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs
from .end_c_x import ZeroCell as EndC_x_ZeroCell


# =============================================================================
# 0-cells (objects in Aut_C(X) = automorphisms f: X → X)
# =============================================================================


@dataclass
class _AutC_x_0Cell_ABC(EndC_x_ZeroCell, ABC):
    """
    0-cells in Aut_C(X): automorphisms f: X → X in the base category C.

    These are the objects of Aut_C(X).
    """


# =============================================================================
# 1-cells (2-morphisms in the base category)
# =============================================================================


@dataclass
class _AutC_x_1Cell_ABC(CategoryABCs.PlainTwoMorphism, ABC):
    """
    1-cells in Aut_C(X): 2-cells α: f ⇒ g between automorphisms.
    """


@dataclass
class _AutC_x_Endo1Cell_ABC(_AutC_x_1Cell_ABC, CategoryABCs.EndoTwoMorphism, ABC):
    """
    Endo-1-cells in Aut_C(X): endo-2-cells α: f ⇒ f.
    """


@dataclass
class _AutC_x_Auto1Cell_ABC(_AutC_x_Endo1Cell_ABC, CategoryABCs.AutoTwoMorphism, ABC):
    """
    Auto-1-cells in Aut_C(X): invertible 2-cells.
    """


# =============================================================================
# 2-cells (3-morphisms / modifications)
# =============================================================================


@dataclass
class _AutC_x_2Cell_ABC(ABC):
    """
    2-cells in Aut_C(X): modifications between 2-cells.
    """


@dataclass
class _AutC_x_Endo2Cell_ABC(_AutC_x_2Cell_ABC, ABC):
    """
    Endo-2-cells in Aut_C(X).
    """


@dataclass
class _AutC_x_Auto2Cell_ABC(_AutC_x_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in Aut_C(X).
    """


# =============================================================================
# Aut_C(X) itself
# =============================================================================


@dataclass
class _AutC_x_ABC(CategoryABCs.EndC_x, ABC):
    """
    Aut_C(X): The category of automorphisms on X.

    This is an object (0-cell) in AutC. Its structure:
    - Domain == Codomain: object X in base category C
    - Objects (0-cells): automorphisms f: X → X in C (invertible endomorphisms)
    - Morphisms (1-cells): 2-cells between those automorphisms

    Invariant: is_groupoid() == True (all morphisms are invertible)
    """

    @abstractmethod
    @override
    def objects(self) -> Sequence[_AutC_x_0Cell_ABC]:
        """All automorphisms f: X → X in C."""
        ...

    @final
    @abstractmethod
    def endc_x_supercategory(self) -> CategoryABCs.EndC_x:
        """Return the End_C(X) supercategory."""
        ...

    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.AutC:
        """Return AutC, the ambient category this Aut_C(X) lives in."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _AutC_x_ABC

# Cells
## Objects
ZeroCell = _AutC_x_0Cell_ABC
## 1-Morphisms
OneCell = _AutC_x_1Cell_ABC
EndoOneCell = _AutC_x_Endo1Cell_ABC
AutoOneCell = _AutC_x_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _AutC_x_2Cell_ABC
EndoTwoCell = _AutC_x_Endo2Cell_ABC
AutoTwoCell = _AutC_x_Auto2Cell_ABC

# Misc Extra
# ...
