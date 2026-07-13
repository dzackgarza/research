r"""Stratified spaces and stacks."""

from __future__ import annotations

from sage.categories.category import Category

from .base import ModuliBase, default_base
from .foundation import ModuliCategory
from .schemes import Schemes
from .stacks import Stacks


class StratifiedSpaces(ModuliCategory):
    r"""Spaces equipped with a stratification over the base."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.moduli_base())]


class StratifiedStacks(ModuliCategory):
    r"""Stacks equipped with a stratification over the base."""

    def super_categories(self) -> list[Category]:
        return [Stacks(self.moduli_base()), StratifiedSpaces(self.moduli_base())]
