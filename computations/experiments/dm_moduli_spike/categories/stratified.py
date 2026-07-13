r"""Stratified spaces and stacks over a base scheme."""

from __future__ import annotations

from sage.categories.category import Category

from .foundation import ModuliCategory
from .schemes import Schemes
from .stacks import Stacks


class StratifiedSpaces(ModuliCategory):
    r"""Schemes with a stratification over base `S`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme())]


class StratifiedStacks(ModuliCategory):
    r"""Stacks with a stratification over base `S`."""

    def super_categories(self) -> list[Category]:
        return [Stacks(self.base_scheme()), StratifiedSpaces(self.base_scheme())]
