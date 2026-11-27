r"""Finite poset subcategory."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, final, override

from sage.categories.finite_posets import FinitePosets as SageFinitePosets
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import FiniteLatticePoset, Integer, Poset, PosetElement, PosetMorphism, PosetSubset

from .. import Posets


class _FinitePosets(CategoryWithAxiom):
    r"""Finite partially ordered sets.

    Canonical chain: ``Posets().Finite()``.
    """

    _base_category_class_and_axiom = (Posets, "Finite")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return posets and Sage finite posets as supercategories."""
        return [Posets(), SageFinitePosets()]

    class ParentMethods:
        @abstract_method
        def list(self) -> list[PosetElement]:
            r"""Return the elements in the distinguished linear extension order."""
            ...

        @abstract_method
        def bottom(self) -> PosetElement:
            r"""Return the bottom element."""
            ...

        @abstract_method
        def top(self) -> PosetElement:
            r"""Return the top element."""
            ...

        @abstract_method
        def has_bottom(self) -> bool:
            r"""Return whether the poset has a bottom element."""
            ...

        @abstract_method
        def has_top(self) -> bool:
            r"""Return whether the poset has a top element."""
            ...

        @abstract_method
        def is_bounded(self) -> bool:
            r"""Return whether the poset has both top and bottom elements."""
            ...

        @abstract_method
        def minimal_elements(self) -> list[PosetElement]:
            r"""Return the minimal elements."""
            ...

        @abstract_method
        def maximal_elements(self) -> list[PosetElement]:
            r"""Return the maximal elements."""
            ...

        @abstract_method
        def cover_relations(self) -> list[tuple[PosetElement, PosetElement]]:
            r"""Return the cover relations."""
            ...

        @abstract_method
        def cover_relations_iterator(self) -> Iterable[tuple[PosetElement, PosetElement]]:
            r"""Return an iterator over the cover relations."""
            ...

        @abstract_method
        def covers(self, x: PosetElement, y: PosetElement) -> bool:
            r"""Return whether ``y`` covers ``x``."""
            ...

        @abstract_method
        def closed_interval(self, x: PosetElement, y: PosetElement) -> list[PosetElement]:
            r"""Return the closed interval ``[x, y]``."""
            ...

        @abstract_method
        def open_interval(self, x: PosetElement, y: PosetElement) -> list[PosetElement]:
            r"""Return the open interval ``(x, y)``."""
            ...

        @abstract_method
        def interval(self, x: PosetElement, y: PosetElement) -> list[PosetElement]:
            r"""Return the closed interval ``[x, y]``."""
            ...

        @abstract_method
        def dual(self) -> Poset:
            r"""Return the dual poset."""
            ...

        @abstract_method
        def subposet(self, elements: Iterable[PosetElement]) -> Poset:
            r"""Return the induced subposet on ``elements``."""
            ...

        @abstract_method
        def height(self) -> Integer:
            r"""Return the height of the poset."""
            ...

        @abstract_method
        def height_certificate(self) -> tuple[Integer, list[PosetElement]]:
            r"""Return the height with a maximum-cardinality chain."""
            ...

        @abstract_method
        def width(self) -> Integer:
            r"""Return the width of the poset."""
            ...

        @abstract_method
        def width_certificate(self) -> tuple[Integer, list[PosetElement]]:
            r"""Return the width with a maximum-cardinality antichain."""
            ...

        @abstract_method
        def is_ranked(self) -> bool:
            r"""Return whether every maximal chain has the same length."""
            ...

        @abstract_method
        def rank(self, element: PosetElement | None = None) -> Integer:
            r"""Return the rank of ``element`` or the rank of the poset."""
            ...

        @abstract_method
        def is_poset_morphism(self, f: PosetMorphism, codomain: Poset) -> bool:
            r"""Return whether ``f`` is order-preserving into ``codomain``."""
            ...

        @abstract_method
        def order_ideals_lattice(self, facade: bool = True) -> FiniteLatticePoset:
            r"""Return the finite distributive lattice of order ideals."""
            ...

        @abstract_method
        def is_meet_semilattice(self) -> bool:
            r"""Return whether every pair has a meet."""
            ...

        @abstract_method
        def meet_semilattice_certificate(self) -> tuple[bool, tuple[PosetElement, PosetElement] | None]:
            r"""Return semilattice status with a pair lacking a meet when false."""
            ...

        @abstract_method
        def is_join_semilattice(self) -> bool:
            r"""Return whether every pair has a join."""
            ...

        @abstract_method
        def join_semilattice_certificate(self) -> tuple[bool, tuple[PosetElement, PosetElement] | None]:
            r"""Return semilattice status with a pair lacking a join when false."""
            ...

        @abstract_method
        def chains(self) -> Iterable[PosetSubset]:
            r"""Return the chains of this finite poset."""
            ...

        @abstract_method
        def antichains(self) -> Iterable[PosetSubset]:
            r"""Return the antichains of this finite poset."""
            ...

        @abstract_method
        def linear_extensions(self) -> Iterable[list[PosetElement]]:
            r"""Return the linear extensions of this finite poset."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
