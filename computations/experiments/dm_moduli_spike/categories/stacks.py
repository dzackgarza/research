r"""Stack categories over a moduli base."""

from __future__ import annotations

from sage.categories.category import Category

from .base import ModuliBase, default_base
from .foundation import ModuliCategory
from .schemes import Schemes


class Stacks(ModuliCategory):
    r"""Stacks over a base :class:`ModuliBase`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.moduli_base())]


class AlgebraicStacks(Stacks):
    r"""Algebraic stacks over the base."""

    def super_categories(self) -> list[Category]:
        return [Stacks(self.moduli_base())]


class DeligneMumfordStacks(AlgebraicStacks):
    r"""Deligne--Mumford stacks over the base."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicStacks(self.moduli_base())]
