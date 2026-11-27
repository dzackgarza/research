r"""Order-theoretic lattice poset subcategory."""

from __future__ import annotations

from typing import final, override

from sage.categories.lattice_posets import LatticePosets as SageLatticePosets
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from .join_semilattice import _JoinSemilatticePosets
from .meet_semilattice import _MeetSemilatticePosets


class _LatticePosets(Category):
    r"""Posets in which every pair has a meet and join.

    Canonical chain: ``Posets().Lattice()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return meet, join, and Sage lattice-poset supercategories."""
        return [_MeetSemilatticePosets(), _JoinSemilatticePosets(), SageLatticePosets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            r"""Return the finite lattice-poset subcategory."""
            return self._with_axiom("Finite")

    Finite = LazyImport("category_specs.posets.subcategories.finite_lattice", "_FiniteLatticePosets")

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
