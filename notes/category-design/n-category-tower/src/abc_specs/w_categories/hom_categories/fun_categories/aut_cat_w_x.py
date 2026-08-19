# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/hom_categories/fun_categories/aut_cat_w_x.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
AutoFun_x ABC: AutFun(C) = Aut_{Cat_w}(C), the autoequivalence category on C.

Architecture:
- AutFun(C) is an object (0-cell) in AutFun
- Objects of AutFun(C) = autoequivalences F: C → C (invertible endofunctors)
- 1-cells of AutFun(C) = natural isomorphisms between those autoequivalences
- 2-cells of AutFun(C) = modifications between natural isomorphisms
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs


# =============================================================================
# 0-cells (objects in AutFun(C) = autoequivalences F: C → C)
# =============================================================================


@dataclass
class _AutFun_x_0Cell_ABC(CategoryABCs.AutoFunctor, ABC):
    """
    0-cells in AutFun(C): autoequivalences F: C → C.

    These are the objects of AutFun(C).
    """


# =============================================================================
# 1-cells (natural isomorphisms η: F ⇒ G)
# =============================================================================


@dataclass
class _AutFun_x_1Cell_ABC(CategoryABCs.AutoNaturalTransformation, ABC):
    """
    1-cells in AutFun(C): natural isomorphisms η: F ⇒ G.
    """


@dataclass
class _AutFun_x_Endo1Cell_ABC(_AutFun_x_1Cell_ABC, ABC):
    """
    Endo-1-cells in AutFun(C): endo-natural isomorphisms η: F ⇒ F.
    """


@dataclass
class _AutFun_x_Auto1Cell_ABC(_AutFun_x_Endo1Cell_ABC, ABC):
    """
    Auto-1-cells in AutFun(C): invertible endo-natural isomorphisms.
    """


# =============================================================================
# 2-cells (modifications between natural isomorphisms)
# =============================================================================


@dataclass
class _AutFun_x_2Cell_ABC(ABC):
    """
    2-cells in AutFun(C): modifications between natural isomorphisms.
    """


@dataclass
class _AutFun_x_Endo2Cell_ABC(_AutFun_x_2Cell_ABC, ABC):
    """
    Endo-2-cells in AutFun(C).
    """


@dataclass
class _AutFun_x_Auto2Cell_ABC(_AutFun_x_Endo2Cell_ABC, ABC):
    """
    Auto-2-cells in AutFun(C).
    """


# =============================================================================
# AutFun(C) itself
# =============================================================================


@dataclass
class _AutFun_x_ABC(CategoryABCs.AutC_x, ABC):
    """
    AutFun(C) = Aut_{Cat_w}(C): The category of autoequivalences on C.

    This is an object in AutFun. Its structure:
    - Domain == Codomain: category C
    - Objects (0-cells): autoequivalences F: C → C (invertible endofunctors)
    - Morphisms (1-cells): natural isomorphisms η: F ⇒ G

    Invariant: is_groupoid() == True
    """

    @abstractmethod
    @override
    def domain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The category C."""
        ...

    @abstractmethod
    @override
    def codomain(self) -> CategoryABCs.Nontrivial_TwoCategory:
        """The category C (domain == codomain)."""
        ...

    @final
    @abstractmethod
    @override
    def objects(self) -> Sequence[_AutFun_x_0Cell_ABC]:
        """All autoequivalences F: C → C."""
        ...

    @final
    @abstractmethod
    def morphisms(self) -> Sequence[_AutFun_x_1Cell_ABC]:
        """All natural isomorphisms between autoequivalences."""
        ...

    @final
    @abstractmethod
    @override
    def amb(self) -> CategoryABCs.AutoFun:
        """Return AutFun, the ambient category."""
        ...


# Semantic exports

# This category:
CategoryDefinition = _AutFun_x_ABC

# Cells
## Objects
ZeroCell = _AutFun_x_0Cell_ABC
## 1-Morphisms
OneCell = _AutFun_x_1Cell_ABC
EndoOneCell = _AutFun_x_Endo1Cell_ABC
AutoOneCell = _AutFun_x_Auto1Cell_ABC
## 2-Morphisms
TwoCell = _AutFun_x_2Cell_ABC
EndoTwoCell = _AutFun_x_Endo2Cell_ABC
AutoTwoCell = _AutFun_x_Auto2Cell_ABC

# Misc Extra
# ...
