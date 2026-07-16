r"""Stack and moduli categories over a base scheme.

Hierarchy (contract §2):

.. code-block:: text

    Stacks(S)
      └── AlgebraicStacks(S)
            └── DeligneMumfordStacks(S)
                  └── AlgebraicSpaces(S)
                        └── (Sage) Schemes(S)
                              └── Varieties(k)

``ModuliStacks(S)`` is an *equipped* category over ``Stacks(S)`` — not a
subcategory of ``DeligneMumfordStacks(S)``. Concrete ``M_{g,I}`` may inhabit both.
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


class ModuliStacks(ModuliCategory, _AxiomMixin):
    r"""Moduli stacks over `S`: stacks equipped with a moduli problem.

    Forgetful to ``Stacks(S)``. Not a subcategory of Deligne--Mumford stacks:
    a moduli stack need not be DM (e.g. many moduli of sheaves are Artin).
    """

    def super_categories(self) -> list[Category]:
        return [Stacks(self.base_scheme())]

    def _base_category_for_axioms(self) -> ModuliCategory:
        return ModuliStacks(self.base_scheme())
