r"""Sage categories for schemes, stacks, curves, and stratified objects."""

from __future__ import annotations

from .base import AffineScheme, complex_numbers_ring, spec, spec_complex
from .curves import Curves, PointedCurves, SmoothCurves, StablePointedCurves
from .membership import (
    coarse_in_category,
    pointed_curve_in_category,
    stack_in_category,
    stratified_stack_in_category,
)
from .schemes import AlgebraicSpaces, Schemes, Varieties
from .stacks import AlgebraicStacks, DeligneMumfordStacks, Stacks
from .stratified import StratifiedSpaces, StratifiedStacks

__all__ = [
    "AffineScheme",
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "Curves",
    "DeligneMumfordStacks",
    "PointedCurves",
    "Schemes",
    "SmoothCurves",
    "Stacks",
    "StablePointedCurves",
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
