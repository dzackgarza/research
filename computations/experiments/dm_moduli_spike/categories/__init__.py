r"""Sage categories for schemes, stacks, and stratified objects."""

from __future__ import annotations

from .base import ModuliBase, ComplexNumbers, default_base
from .membership import coarse_in_category, stack_in_category, stratified_stack_in_category
from .schemes import AlgebraicSpaces, Schemes, Varieties
from .stacks import AlgebraicStacks, DeligneMumfordStacks, Stacks
from .stratified import StratifiedSpaces, StratifiedStacks

__all__ = [
    "AlgebraicSpaces",
    "AlgebraicStacks",
    "DeligneMumfordStacks",
    "ModuliBase",
    "ComplexNumbers",
    "Schemes",
    "Stacks",
    "StratifiedSpaces",
    "StratifiedStacks",
    "Varieties",
    "default_base",
    "coarse_in_category",
    "stack_in_category",
    "stratified_stack_in_category",
]
