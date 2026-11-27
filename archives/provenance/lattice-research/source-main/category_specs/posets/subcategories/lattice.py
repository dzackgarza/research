r"""Order-theoretic lattice poset subcategory."""

from __future__ import annotations

from typing import cast, final, override

from sage.categories.lattice_posets import LatticePosets as SageLatticePosets
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...utils import with_axiom
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
        @final
        def Finite(self) -> Category:
            r"""Return the finite lattice-poset subcategory."""
            return cast(Category, with_axiom(self, "Finite"))

    Finite = LazyImport(
        "category_specs.posets.subcategories.finite_lattice", "_FiniteLatticePosets"
    )

    class ParentMethods: ...

    class ElementMethods: ...
