r"""Deligne--Mumford moduli landscape: stacks, compactifications, stratifications.

The public API is organized from general geometric objects downward:

1. Sage categories (`Stacks`, `Varieties`, `StratifiedStacks`, ...)
2. moduli stacks and coarse moduli spaces (`M_gn`, `DeligneMumfordModuliStack`)
3. compactifications as open immersions with boundary
4. stratifications indexed by dual graphs
5. combinatorial stable-graph kernel (`objects/`, private indexing backend)

Stable graphs are **not** the ambient ontology. They index one boundary
stratification of the Deligne--Mumford compactification of `\mathcal M_{g,n}`.
"""

from __future__ import annotations

import sage.all  # noqa: F401

from .categories import (
    AlgebraicSpaces,
    AlgebraicStacks,
    DeligneMumfordStacks,
    ModuliBase,
    Schemes,
    Stacks,
    StratifiedSpaces,
    StratifiedStacks,
    Varieties,
    ComplexNumbers,
    default_base,
    coarse_in_category,
    stack_in_category,
    stratified_stack_in_category,
)
from .curves import SmoothPointedCurve, StablePointedCurve
from .geometry import CoarseModuliMap, Compactification, OpenImmersion
from .moduli import (
    DeligneMumfordModuliStack,
    FamiliesOver,
    M_gn,
    ModuliProblem,
    SmoothPointedCurves,
    StablePointedCurves,
)
from .moduli.coarse import CoarseModuliSpace
from .moduli.instances import Mbar_gn
from .stratification import BoundaryStack, DualGraphType, StratifiedStack, StratifiedVariety

# Combinatorial backend (stable graphs, oracles, enumeration).
from .objects.graph_types import StableGraphType, StableGraphTypes
from .objects.model import DMCompactificationModel
from .objects.records import StableGraph
from .objects.strata import DMStratum, ModuliFactor

__all__ = [
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "BoundaryStack",
    "CoarseModuliMap",
    "CoarseModuliSpace",
    "Compactification",
    "ComplexNumbers",
    "DMCompactificationModel",
    "ModuliFactor",
    "DeligneMumfordModuliStack",
    "DeligneMumfordStacks",
    "DualGraphType",
    "FamiliesOver",
    "M_gn",
    "Mbar_gn",
    "ModuliBase",
    "ModuliProblem",
    "OpenImmersion",
    "Schemes",
    "SmoothPointedCurve",
    "SmoothPointedCurves",
    "StableGraph",
    "StableGraphType",
    "StableGraphTypes",
    "StablePointedCurve",
    "StablePointedCurves",
    "Stacks",
    "StratifiedSpaces",
    "StratifiedStack",
    "StratifiedStacks",
    "StratifiedVariety",
    "Varieties",
    "coarse_in_category",
    "stack_in_category",
    "stratified_stack_in_category",
    "default_base",
]
