# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/end_cat_w_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
EndoFun_x ABC: EndFun(C) = End_{Cat_w}(C), the endofunctor category on C.

Architecture:
- EndFun(C) is an object (0-cell) in EndFun
- Objects of EndFun(C) = endofunctors F: C → C
- 1-cells of EndFun(C) = natural transformations between those endofunctors
- 2-cells of EndFun(C) = modifications between natural transformations
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in EndFun(C) = endofunctors F: C → C)
# =============================================================================


@dataclass
class _EndoFun_x_0Cell_ABC(CategoryABCs.EndoFunctor, ABC):
    """
    0-cells in EndFun(C): endofunctors F: C → C.

    These are the objects of EndFun(C).
    """


# =============================================================================
# 1-cells (natural transformations η: F ⇒ G)
# =============================================================================


@dataclass
class _EndoFun_x_1Cell_ABC(CategoryABCs.NaturalTransformation, ABC):
    """
    1-cells in EndFun(C): natural transformations η: F ⇒ G.
    """


@dataclass
class _EndoFun_x_Endo1Cell_ABC(_EndoFun_x_1Cell_ABC, CategoryABCs.EndoNaturalTransformation, ABC):
    """
    Endo-1-cells in EndFun(C): endo-natural transformations η: F ⇒ F.
    """


@dataclass
class _EndoFun_x_Auto1Cell_ABC(_EndoFun_x_Endo1Cell_ABC, CategoryABCs.AutoNaturalTransformation, ABC):
    """
    Auto-1-cells in EndFun(C): natural isomorphisms.
    """


# =============================================================================
# 2-cells (modifications between natural transformations)
# =============================================================================


@dataclass
class _EndoFun_x_2Cell_ABC(ABC):
    """
    2-cells in EndFun(C): modifications between natural transformations.
    """


@dataclass
class _EndoFun_x_Endo2Cell_ABC(_EndoFun_x_2Cell_ABC, ABC):
    """
    Endo-2-cells in EndFun(C).
    """


@dataclass
class _EndoFun_x_Auto2Cell_ABC(_EndoFun_x_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in EndFun(C).
    """


# =============================================================================
# EndFun(C) itself
# =============================================================================


@dataclass
class _EndoFun_x_ABC(CategoryABCs.EndC_x, ABC):
    """
    EndFun(C) = End_{Cat_w}(C): The category of endofunctors on C.

    This is an object in EndFun. Its structure:
    - Domain == Codomain: category C
    - Objects (0-cells): endofunctors F: C → C
    - Morphisms (1-cells): natural transformations η: F ⇒ G
    """

    @final
    @abstractmethod
    @override
    def domain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The category C."""
        ...

    @final
    @abstractmethod
    @override
    def codomain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The category C (domain == codomain)."""
        ...

    @final
    @abstractmethod
    @override
    def objects(self) -> Sequence[_EndoFun_x_0Cell_ABC]:
        """All endofunctors F: C → C."""
        ...

    @final
    @abstractmethod
    def morphisms(self) -> Sequence[_EndoFun_x_1Cell_ABC]:
        """All natural transformations between endofunctors."""
        ...

    @final
    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.EndoFun:
        """Return EndFun, the ambient category."""
        ...

    @final
    @abstractmethod
    @override
    def object_from_callable(self, f: Any) -> _EndoFun_x_0Cell_ABC:
        """Construct an endofunctor from callable."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _EndoFun_x_ABC

# Cells
## Objects
ZeroCell = _EndoFun_x_0Cell_ABC
## 1-Morphisms
OneCell = _EndoFun_x_1Cell_ABC
EndoOneCell = _EndoFun_x_Endo1Cell_ABC
AutoOneCell = _EndoFun_x_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _EndoFun_x_2Cell_ABC
EndoTwoCell = _EndoFun_x_Endo2Cell_ABC
AutoTwoCell = _EndoFun_x_Auto2Cell_ABC

# Misc Extra
# ...
