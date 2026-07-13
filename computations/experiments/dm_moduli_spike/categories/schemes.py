r"""Scheme, variety, and algebraic-space categories over a base scheme.

Algebraic spaces embed as Deligne--Mumford stacks (Stacks Project).  Spike
``Schemes(S)`` sits under ``AlgebraicSpaces(S)`` in the contract hierarchy.
"""

from __future__ import annotations

from sage.categories.category import Category

from .axioms import _AxiomMixin
from .foundation import ModuliCategory


class Schemes(ModuliCategory, _AxiomMixin):
    r"""Schemes over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return Schemes(self.base_scheme())


class AlgebraicSpaces(ModuliCategory, _AxiomMixin):
    r"""Algebraic spaces over `S`; embed into Deligne--Mumford stacks."""

    def super_categories(self) -> list[Category]:
        from .stacks import DeligneMumfordStacks

        return [DeligneMumfordStacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return AlgebraicSpaces(self.base_scheme())


class Varieties(AlgebraicSpaces, _AxiomMixin):
    r"""Varieties over a field-like base (integral, separated, finite type)."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme()), Schemes(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return Varieties(self.base_scheme())
