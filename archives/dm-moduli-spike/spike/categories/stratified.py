r"""Stratified space and stack categories (equipped objects).

A stratification is additional structure. Categories of stratified objects
forget to the underlying geometric category; they do **not** inherit across
the stack / algebraic-space divide.
"""

from __future__ import annotations

from sage.categories.category import Category

from .axioms import _AxiomMixin
from .foundation import ModuliCategory
from .schemes import AlgebraicSpaces, schemes_over
from .stacks import DeligneMumfordStacks, Stacks


class StratifiedSpaces(ModuliCategory, _AxiomMixin):
    r"""Stratified algebraic spaces over `S` (equipped ``AlgebraicSpaces``)."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedSpaces(self.base_scheme())


class StratifiedStacks(ModuliCategory, _AxiomMixin):
    r"""Stratified stacks over `S` (equipped stacks; typically DM when ambient is DM).

    Supercategories are stack categories only — **not** ``StratifiedSpaces``.
    """

    def super_categories(self) -> list[Category]:
        return [DeligneMumfordStacks(self.base_scheme()), Stacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedStacks(self.base_scheme())


class StratifiedSchemes(ModuliCategory, _AxiomMixin):
    r"""Stratified schemes over `S`."""

    def super_categories(self) -> list[Category]:
        return [schemes_over(self.base_scheme()), StratifiedSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedSchemes(self.base_scheme())


class StratifiedAlgebraicSpaces(ModuliCategory, _AxiomMixin):
    r"""Stratified algebraic spaces over `S` (alias path under AlgebraicSpaces)."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme()), StratifiedSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedAlgebraicSpaces(self.base_scheme())
