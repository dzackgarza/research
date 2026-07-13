r"""Stratified space and stack categories."""

from __future__ import annotations

from sage.categories.category import Category

from .axioms import _AxiomMixin
from .foundation import ModuliCategory
from .schemes import AlgebraicSpaces, Schemes
from .stacks import DeligneMumfordStacks, Stacks


class StratifiedSpaces(ModuliCategory, _AxiomMixin):
    r"""Stratified geometric spaces over `S`."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedSpaces(self.base_scheme())


class StratifiedStacks(ModuliCategory, _AxiomMixin):
    r"""Stratified Deligne--Mumford stacks over `S`."""

    def super_categories(self) -> list[Category]:
        return [DeligneMumfordStacks(self.base_scheme()), StratifiedSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedStacks(self.base_scheme())


class StratifiedSchemes(ModuliCategory, _AxiomMixin):
    r"""Stratified schemes over `S`."""

    def super_categories(self) -> list[Category]:
        return [Schemes(self.base_scheme()), StratifiedSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedSchemes(self.base_scheme())


class StratifiedAlgebraicSpaces(ModuliCategory, _AxiomMixin):
    r"""Stratified algebraic spaces over `S`."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicSpaces(self.base_scheme()), StratifiedSpaces(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return StratifiedAlgebraicSpaces(self.base_scheme())
