# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/end_c_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
EndC_x ABC: The endomorphism category End_C(X) for a specific object X.

Architecture:
- End_C(X) is an object (0-cell) in EndC
- Objects of End_C(X) = endomorphisms f: X → X in base category C
- 1-cells of End_C(X) = 2-cells between those endomorphisms
- 2-cells of End_C(X) = 3-cells (modifications) between 2-cells
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs
from .hom_c_xy import *

# =============================================================================
# 0-cells (objects in End_C(X) = endomorphisms f: X → X)
# =============================================================================


@dataclass
class _EndC_x_0Cell_ABC(EndoZeroCell, ABC):
    """
    0-cells in End_C(X): endomorphisms f: X → X in the base category C.

    These are the objects of End_C(X).
    """


# =============================================================================
# 1-cells (2-morphisms in the base category)
# =============================================================================


@dataclass
class _EndC_x_1Cell_ABC(CategoryABCs.PlainTwoMorphism, ABC):
    """
    1-cells in End_C(X): 2-cells α: f ⇒ g between endomorphisms.
    """


@dataclass
class _EndC_x_Endo1Cell_ABC(_EndC_x_1Cell_ABC, CategoryABCs.EndoTwoMorphism, ABC):
    """
    Endo-1-cells in End_C(X): endo-2-cells α: f ⇒ f.
    """


@dataclass
class _EndC_x_Auto1Cell_ABC(_EndC_x_Endo1Cell_ABC, CategoryABCs.AutoTwoMorphism, ABC):
    """
    Auto-1-cells in End_C(X): invertible 2-cells.
    """


# =============================================================================
# 2-cells (3-morphisms / modifications)
# =============================================================================


@dataclass
class _EndC_x_2Cell_ABC(ABC):
    """
    2-cells in End_C(X): modifications between 2-cells.
    """


@dataclass
class _EndC_x_Endo2Cell_ABC(_EndC_x_2Cell_ABC, ABC):
    """
    Endo-2-cells in End_C(X).
    """


@dataclass
class _EndC_x_Auto2Cell_ABC(_EndC_x_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in End_C(X).
    """


# =============================================================================
# End_C(X) itself
# =============================================================================


@dataclass
class _EndC_x_ABC(CategoryABCs.HomC_xy, ABC):
    """
    End_C(X): The category of endomorphisms on X.

    This is an object (0-cell) in EndC. Its structure:
    - Domain == Codomain: object X in base category C
    - Objects (0-cells): endomorphisms f: X → X in C
    - Morphisms (1-cells): 2-cells between those endomorphisms

    Invariant: domain() == codomain()
    """

    @abstractmethod
    @override
    def objects(self) -> Sequence[_EndC_x_0Cell_ABC]:
        """All endomorphisms f: X → X in C."""
        ...

    @abstractmethod
    def identity_automorphism(self) -> CategoryABCs.AutoOneMorphism:
        """id_X: the identity endomorphism on X."""
        ...

    @final
    @abstractmethod
    def autc_x_subcategory(self) -> CategoryABCs.AutC_x:
        """Return the Aut_C(X) subcategory."""
        ...

    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.EndC:
        """Return EndC, the ambient category this End_C(X) lives in."""
        ...

    @abstractmethod
    @override
    def object_from_callable(self, f: Callable[[Any], Any]) -> _EndC_x_0Cell_ABC:
        """Construct an endomorphism X → X from callable."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _EndC_x_ABC

# Cells
## Objects
ZeroCell = _EndC_x_0Cell_ABC
## 1-Morphisms
OneCell = _EndC_x_1Cell_ABC
EndoOneCell = _EndC_x_Endo1Cell_ABC
AutoOneCell = _EndC_x_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _EndC_x_2Cell_ABC
EndoTwoCell = _EndC_x_Endo2Cell_ABC
AutoTwoCell = _EndC_x_Auto2Cell_ABC

# Misc Extra
# ...
