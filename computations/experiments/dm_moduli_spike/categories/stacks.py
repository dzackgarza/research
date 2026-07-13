r"""Stack categories over a base scheme."""

from __future__ import annotations

from sage.categories.category import Category

from .foundation import ModuliCategory
from .schemes import Schemes


class Stacks(ModuliCategory):
    r"""Stacks over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme())]


class AlgebraicStacks(Stacks):
    r"""Algebraic stacks over `S`."""

    def super_categories(self) -> list[Category]:
        return [Stacks(self.base_scheme())]


class DeligneMumfordStacks(AlgebraicStacks):
    r"""Deligne--Mumford stacks over `S` (e.g. `\mathcal M_{g,n} \to \mathrm{Spec}(\mathbb Z)`)."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicStacks(self.base_scheme())]
