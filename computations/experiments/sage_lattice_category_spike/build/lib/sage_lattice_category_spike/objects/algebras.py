r"""The standard algebra joins, as synthetic nodes.

An ``R``-algebra combines compatible module and multiplicative structure:
``MagmaticAlgebras(R)`` is the general (not-necessarily-associative,
not-necessarily-unital) node — an ``R``-module with a bilinear
multiplication — and ``Algebras(R)`` is the associative unital
refinement, which is in particular a ring. Both are synthetic: correct
joins, inherited obligations, and immediate functors, with no concrete
parent invented merely to look exercised. Based and finite-dimensional
refinements are reached through Sage's standard axioms at request time.

Nothing here declares set behavior: the module and multiplicative legs
both roll up through the operation roots' underlying-set route.
"""

from __future__ import annotations

from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras

from .functors import CatObject
from .magmas import Magmas
from .modules import Modules
from .scalars import Rings


class MagmaticAlgebras(CatObject, Category_over_base_ring):
    r"""``R``-modules with a bilinear multiplication: the general algebra
    node, before associativity or a unit is assumed."""

    def super_categories(self) -> list[Category]:
        return [SageMagmaticAlgebras(self.base_ring()), Modules(self.base_ring()), Magmas()]


class Algebras(CatObject, Category_over_base_ring):
    r"""Associative unital ``R``-algebras: in particular rings."""

    def super_categories(self) -> list[Category]:
        return [SageAlgebras(self.base_ring()), MagmaticAlgebras(self.base_ring()), Rings()]
