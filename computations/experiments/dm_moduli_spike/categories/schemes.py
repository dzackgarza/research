r"""Scheme, variety, and algebraic-space categories over a base scheme."""

from __future__ import annotations

from sage.categories.category import Category

from .foundation import ModuliCategory


class Schemes(ModuliCategory):
    r"""Schemes over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        from sage.categories.sets_cat import Sets

        return [Sets()]


class AlgebraicSpaces(Schemes):
    r"""Algebraic spaces over `S`; coarse moduli maps land here in general."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme())]


class Varieties(AlgebraicSpaces):
    r"""Varieties over `S` (e.g. `\overline M_{g,n}` over `\mathrm{Spec}(\mathbb C)`)."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme())]
