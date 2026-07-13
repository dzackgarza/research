r"""Sage categories for schemes, stacks, and stratified objects."""

from __future__ import annotations

from .base import AffineScheme, SchemeOver, complex_numbers_ring, scheme_over, spec, spec_complex
from .membership import coarse_in_category, stack_in_category, stratified_stack_in_category
from .schemes import AlgebraicSpaces, Schemes, Varieties
from .stacks import AlgebraicStacks, DeligneMumfordStacks, Stacks
from .stratified import StratifiedSpaces, StratifiedStacks

__all__ = [
    "AffineScheme",
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "DeligneMumfordStacks",
    "Schemes",
    "SchemeOver",
    "Stacks",
    "StratifiedSpaces",
    "StratifiedStacks",
    "Varieties",
    "complex_numbers_ring",
    "coarse_in_category",
    "scheme_over",
    "spec",
    "spec_complex",
    "stack_in_category",
    "stratified_stack_in_category",
]
