r"""Stack and moduli categories over a base scheme.

Hierarchy (contract §2):

.. code-block:: text

    Stacks(S)
      └── AlgebraicStacks(S)
            └── DeligneMumfordStacks(S)
                  └── AlgebraicSpaces(S)
                        └── Schemes(S)
                              └── Varieties(k)
"""

from __future__ import annotations

from sage.categories.category import Category

from .axioms import _AxiomMixin
from .foundation import ModuliCategory


class Stacks(ModuliCategory, _AxiomMixin):
    r"""Stacks over a base scheme `S`."""

    def super_categories(self) -> list[Category]:
        from sage.categories.sets_cat import Sets

        return [Sets()]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return Stacks(self.base_scheme())


class AlgebraicStacks(Stacks):
    r"""Algebraic stacks over `S`."""

    def super_categories(self) -> list[Category]:
        return [Stacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return AlgebraicStacks(self.base_scheme())


class DeligneMumfordStacks(AlgebraicStacks):
    r"""Deligne--Mumford stacks over `S`."""

    def super_categories(self) -> list[Category]:
        return [AlgebraicStacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return DeligneMumfordStacks(self.base_scheme())


class ModuliStacks(DeligneMumfordStacks):
    r"""Moduli stacks over `S` (stacks equipped with a moduli problem)."""

    def super_categories(self) -> list[Category]:
        return [DeligneMumfordStacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return ModuliStacks(self.base_scheme())
