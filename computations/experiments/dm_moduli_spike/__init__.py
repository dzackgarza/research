r"""Deligne--Mumford moduli spike: theorem-backed geometric ontology + combinatorial Γ.

Mathematical contract
=====================

**Implements**

1. Sage categories ``Stacks → AlgebraicStacks → DeligneMumfordStacks → AlgebraicSpaces →
   Schemes → Varieties`` with geometric axiom refinements (``.Proper()``, ``.Smooth()``, …).
2. Theorem-backed geometric parents: stacks, Hom-sets, immersions, compactifications,
   boundaries, stratifications, product/quotient stacks, moduli stacks ``M_gI`` / ``Mbar_gI``.
3. Curve/family types with Sage ``Curve_generic`` models for the smooth proving set.
4. The finite combinatorial category ``Γ_{g,n}`` and ``StableGraphs(g,I)`` as the indexing
   layer for dual-graph stratifications.
5. Symmetric Δ-complex of ``Γ_{g,n}`` (DM boundary identification only for ``g=0``).

**Does not claim**

* Computational étale atlases or equation-level properness tests for arbitrary stacks.
* A universal family computed as a scheme over ``M_{g,n}``.
* Geometric nodal gluing beyond theorem-backed dual graphs (smooth fibers are Sage curves).

Formal morphisms (atlases, diagonals, clutching) have correct domain/codomain and Hom
membership; properties of ``Mbar_{g,n}`` are theorem-backed at construction.
"""

from __future__ import annotations

import sage.all  # noqa: F401

from .categories.base import AffineScheme, complex_numbers_ring, spec, spec_complex
from .categories.curves import (
    CurveFamilies,
    PointedCurveFamilies,
    StablePointedCurveFamilies,
    StablePointedCurves,
)
from .categories.schemes import AlgebraicSpaces, Schemes, Varieties
from .categories.stacks import (
    AlgebraicStacks,
    DeligneMumfordStacks,
    ModuliStacks,
    Stacks,
)
from .categories.stratified import StratifiedSpaces, StratifiedStacks
from .geometry import (
    Boundary,
    ClosedSubstack,
    ClutchingMorphism,
    Compactification,
    Compactifications,
    LocallyClosedSubspace,
    LocallyClosedSubstack,
    LocallyClosedSubstacks,
    OpenSubstack,
    ProductStack,
    QuotientStack,
    StableDualGraph,
    Stack,
    StackMorphism,
    Stratification,
    Stratifications,
    Stratum,
    Variety,
    scheme_open_immersion_compactification,
)
from .moduli import M_gI, M_gn, Mbar_gI, Mbar_gn, ModuliStack
from .objects.delta_complex import SymmetricDeltaComplex, symmetric_delta_complex
from .objects.gamma import (
    Gamma_gn,
    StableGraphCategory,
    StableGraphHomset,
    StableGraphMorphism,
)
from .objects.stable_graphs import StableGraph, StableGraphs

__all__ = [
    "AffineScheme",
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "Boundary",
    "ClosedSubstack",
    "ClutchingMorphism",
    "Compactification",
    "Compactifications",
    "CurveFamilies",
    "DeligneMumfordStacks",
    "Gamma_gn",
    "LocallyClosedSubspace",
    "LocallyClosedSubstack",
    "LocallyClosedSubstacks",
    "M_gI",
    "M_gn",
    "Mbar_gI",
    "Mbar_gn",
    "ModuliStack",
    "ModuliStacks",
    "OpenSubstack",
    "PointedCurveFamilies",
    "ProductStack",
    "QuotientStack",
    "Schemes",
    "Stack",
    "StackMorphism",
    "Stacks",
    "StableDualGraph",
    "StableGraph",
    "StableGraphCategory",
    "StableGraphHomset",
    "StableGraphMorphism",
    "StableGraphs",
    "StablePointedCurveFamilies",
    "StablePointedCurves",
    "Stratification",
    "Stratifications",
    "StratifiedSpaces",
    "StratifiedStacks",
    "Stratum",
    "SymmetricDeltaComplex",
    "Varieties",
    "Variety",
    "complex_numbers_ring",
    "scheme_open_immersion_compactification",
    "spec",
    "spec_complex",
    "symmetric_delta_complex",
]
