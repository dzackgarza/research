# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/terminal_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Terminal Category: the terminal category as an object in wCat.

The terminal category 𝟙 has:
- Exactly one 0-cell (one object, typically denoted pt or *)
- Exactly one 1-cell (the identity morphism id_pt : pt → pt)
- All 2-cells are identities

As an object in wCat, the terminal category inherits from _wCat_Nontrivial0Cell_ABC.
The terminal category is the terminal object in wCat: for any category C,
there exists a unique functor C → 𝟙.

Internal structure:
- 1-cells in 𝟙 are morphisms pt → pt (just id_pt)
- 2-cells in 𝟙 are transformations between morphisms (trivial)
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs

# =============================================================================
# 0-cells: Terminal Category (as object in wCat)
# =============================================================================


@dataclass
class _TerminalCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    The terminal category 𝟙 as a 0-cell in wCat.

    Has exactly one object pt and one morphism id_pt.
    """

    pass


# =============================================================================
# 1-cells: Morphisms pt → pt in 𝟙
# =============================================================================


@dataclass
class _Terminal1Cell_ABC(CategoryABCs.OneMorphism_In_A_1_Cat, ABC):
    """
    1-cell (morphism) in the terminal category 𝟙.

    There is exactly one: id_pt : pt → pt.
    """

    pass


@dataclass
class _TerminalEndo1Cell_ABC(_Terminal1Cell_ABC, CategoryABCs.EndoOneMorphism, ABC):
    """
    Endo-1-cell in 𝟙. Since 𝟙 has one object, all morphisms are endomorphisms.
    """

    pass


@dataclass
class _TerminalAuto1Cell_ABC(_TerminalEndo1Cell_ABC, CategoryABCs.AutoMorphism, ABC):
    """
    Auto-1-cell in 𝟙. The unique morphism id_pt is trivially invertible.
    """

    pass


# =============================================================================
# 2-cells: Transformations between morphisms in 𝟙
# =============================================================================


@dataclass
class _Terminal2Cell_ABC(CategoryABCs.PlainTwoMorphism, ABC):
    """
    2-cell in the terminal category 𝟙.

    There is exactly one: the identity transformation on id_pt.
    """

    pass


@dataclass
class _TerminalEndo2Cell_ABC(_Terminal2Cell_ABC, CategoryABCs.EndoTwoMorphism, ABC):
    """
    Endo-2-cell in 𝟙.
    """

    pass


@dataclass
class _TerminalAuto2Cell_ABC(_TerminalEndo2Cell_ABC, CategoryABCs.AutoTwoMorphism, ABC):
    """
    Auto-2-cell in 𝟙.
    """

    pass


# Re-exports
_ = _TerminalCategory_ABC
_ = _Terminal1Cell_ABC
_ = _TerminalEndo1Cell_ABC
_ = _TerminalAuto1Cell_ABC
_ = _Terminal2Cell_ABC
_ = _TerminalEndo2Cell_ABC
_ = _TerminalAuto2Cell_ABC
