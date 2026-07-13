r"""Deligne--Mumford moduli landscape: stacks, compactifications, stratifications.

Public API semantics:

* `\mathcal M_{g,n}` and `\overline{\mathcal M}_{g,n}` are Deligne--Mumford stacks
  over `\mathrm{Spec}(\mathbb Z)` (see :func:`~dm_moduli_spike.moduli.instances.M_gn`).
* :func:`~dm_moduli_spike.categories.base.spec` is the `\mathrm{Spec}` functor from
  rings to affine schemes; objects of `\mathrm{Sch}/B` are :class:`~dm_moduli_spike.categories.base.SchemeOver`.
* Base change along `S \to \mathrm{Spec}(\mathbb Z)` is ``stack.base_change(S)``;
  `S`-points are the same data as ``stack.s_points(S)``.
* Symbolic `\mathbb C` is :func:`~dm_moduli_spike.categories.base.complex_numbers_ring`
  (`\mathbb R[x]/(x^2+1)`), with :func:`~dm_moduli_spike.categories.base.spec_complex`.
"""

from __future__ import annotations

import sage.all  # noqa: F401

from .categories import (
    AffineScheme,
    AlgebraicSpaces,
    AlgebraicStacks,
    DeligneMumfordStacks,
    SchemeOver,
    Schemes,
    Stacks,
    StratifiedSpaces,
    StratifiedStacks,
    Varieties,
    complex_numbers_ring,
    coarse_in_category,
    scheme_over,
    spec,
    spec_complex,
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
from .moduli.coarse import CoarseModuliScheme, CoarseModuliSchemeOver, CoarseModuliSpace
from .moduli.instances import M_gn_base_change, Mbar_gn, Mbar_gn_base_change
from .moduli.stack import DeligneMumfordModuliStackOver
from .stratification import BoundaryStack, DualGraphType, StratifiedStack, StratifiedVariety

from .objects.graph_types import StableGraphType, StableGraphTypes
from .objects.model import DMCompactificationModel
from .objects.records import StableGraph
from .objects.strata import DMStratum, ModuliFactor

__all__ = [
    "AffineScheme",
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "BoundaryStack",
    "CoarseModuliMap",
    "CoarseModuliScheme",
    "CoarseModuliSchemeOver",
    "CoarseModuliSpace",
    "Compactification",
    "DMCompactificationModel",
    "DMStratum",
    "DeligneMumfordModuliStack",
    "DeligneMumfordModuliStackOver",
    "DeligneMumfordStacks",
    "DualGraphType",
    "FamiliesOver",
    "M_gn",
    "M_gn_base_change",
    "Mbar_gn",
    "Mbar_gn_base_change",
    "ModuliFactor",
    "ModuliProblem",
    "OpenImmersion",
    "SchemeOver",
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
    "complex_numbers_ring",
    "coarse_in_category",
    "scheme_over",
    "spec",
    "spec_complex",
    "stack_in_category",
    "stratified_stack_in_category",
]
