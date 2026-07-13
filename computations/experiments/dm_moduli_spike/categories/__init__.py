r"""Sage categories for the geometric ontology."""

from __future__ import annotations

from .axioms import AxiomRefinement
from .base import AffineScheme, complex_numbers_ring, spec, spec_complex
from .curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves
from .foundation import ModuliCategory
from .membership import (
    coarse_in_category,
    pointed_curve_in_category,
    stack_in_category,
    stratified_stack_in_category,
)
from .schemes import AlgebraicSpaces, Schemes, Varieties
from .stacks import AlgebraicStacks, DeligneMumfordStacks, ModuliStacks, Stacks
from .stratified import (
    StratifiedAlgebraicSpaces,
    StratifiedSchemes,
    StratifiedSpaces,
    StratifiedStacks,
)

__all__ = [
    "AffineScheme",
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "AxiomRefinement",
    "Curves",
    "DeligneMumfordStacks",
    "ModuliCategory",
    "ModuliStacks",
    "PointedCurves",
    "Schemes",
    "SmoothCurves",
    "Stacks",
    "StablePointedCurves",
    "StratifiedAlgebraicSpaces",
    "StratifiedSchemes",
    "StratifiedSpaces",
    "StratifiedStacks",
    "Varieties",
    "complex_numbers_ring",
    "coarse_in_category",
    "pointed_curve_in_category",
    "spec",
    "spec_complex",
    "stack_in_category",
    "stratified_stack_in_category",
]
