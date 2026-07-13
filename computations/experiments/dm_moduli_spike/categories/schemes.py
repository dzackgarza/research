r"""Scheme, variety, and algebraic-space categories over a moduli base."""

from __future__ import annotations

from sage.categories.category import Category

from .base import ModuliBase, default_base
from .foundation import ModuliCategory


class Schemes(ModuliCategory):
    r"""Schemes over a base :class:`ModuliBase`."""

    def super_categories(self) -> list[Category]:
        from sage.categories.sets_cat import Sets

        return [Sets()]


class AlgebraicSpaces(Schemes):
    r"""Algebraic spaces over the base; coarse moduli maps land here generically."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.moduli_base())]


class Varieties(AlgebraicSpaces):
    r"""Varieties over the base; stronger than algebraic spaces."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.moduli_base())]
