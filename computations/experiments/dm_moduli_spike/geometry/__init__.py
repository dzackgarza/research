r"""Theorem-backed geometric ontology and combinatorial Γ for DM moduli."""

from __future__ import annotations

from .compactification import scheme_open_immersion_compactification
from .stacks import (
    AlgebraicSpace,
    AlgebraicStack,
    Boundary,
    ClosedImmersion,
    CoarseModuliMorphism,
    Compactification,
    Compactifications,
    DeligneMumfordStack,
    LocallyClosedImmersion,
    OpenImmersion,
    ProductStack,
    QuotientStack,
    Stack,
    StackFiber,
    StackHomset,
    StackMorphism,
    Variety,
)
from .stratification import (
    ClutchingMorphism,
    StableDualGraph,
    Stratification,
    Stratifications,
    StratifiedSpace,
    Stratum,
)

__all__ = [
    "AlgebraicSpace",
    "AlgebraicStack",
    "Boundary",
    "ClosedImmersion",
    "ClutchingMorphism",
    "CoarseModuliMorphism",
    "Compactification",
    "Compactifications",
    "DeligneMumfordStack",
    "LocallyClosedImmersion",
    "OpenImmersion",
    "ProductStack",
    "QuotientStack",
    "StableDualGraph",
    "Stack",
    "StackFiber",
    "StackHomset",
    "StackMorphism",
    "Stratification",
    "Stratifications",
    "StratifiedSpace",
    "Stratum",
    "Variety",
    "scheme_open_immersion_compactification",
]
