r"""Scheme, variety, and algebraic-space categories over a base scheme.

Sage's :class:`~sage.categories.schemes.Schemes` is the scheme category.
This module does **not** define a second class named ``Schemes``.

Algebraic spaces embed as Deligne--Mumford stacks (Stacks Project).
"""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.schemes import Schemes

from .axioms import _AxiomMixin
from .foundation import ModuliCategory


def schemes_over(base: object) -> Category:
    r"""Sage ``Schemes`` over the underlying scheme of an :class:`AffineScheme` base."""
    from .base import AffineScheme

    if isinstance(base, AffineScheme):
        result = Schemes(base.sage_scheme())
    else:
        result = Schemes(base)
    assert isinstance(result, Category), f"Schemes(...) must return a Category; found {type(result)!r}"
    return result


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
        return [AlgebraicSpaces(self.base_scheme()), schemes_over(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return Varieties(self.base_scheme())


__all__ = ["AlgebraicSpaces", "Schemes", "Varieties", "schemes_over"]
