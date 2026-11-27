r"""Finite poset subcategory."""

from __future__ import annotations

import builtins
from abc import abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING, final, override

from sage.categories.finite_posets import FinitePosets as SageFinitePosets
from sage.combinat.posets.posets import FinitePoset as SageFinitePoset

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import (
        FiniteLatticePoset,
        Integer,
        Poset,
        PosetElement,
        PosetMorphism,
        PosetSubset,
    )

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
        from ...sets import Sets

        return [Posets(), Sets().Finite(), SageFinitePosets()]

    class ParentMethods:
        @abstractmethod
        def list(self) -> builtins.list[PosetElement]:
            r"""Return the elements in the distinguished linear extension order."""
            ...

        @abstractmethod
        def bottom(self) -> PosetElement:
            r"""Return the bottom element."""
            ...

        @abstractmethod
        def top(self) -> PosetElement:
            r"""Return the top element."""
            ...

        @abstractmethod
        def has_bottom(self) -> bool:
            r"""Return whether the poset has a bottom element."""
            ...

        @abstractmethod
        def has_top(self) -> bool:
            r"""Return whether the poset has a top element."""
            ...

        @abstractmethod
        def is_bounded(self) -> bool:
            r"""Return whether the poset has both top and bottom elements."""
            ...

        @abstractmethod
        def minimal_elements(self) -> builtins.list[PosetElement]:
            r"""Return the minimal elements."""
            ...

        @abstractmethod
        def maximal_elements(self) -> builtins.list[PosetElement]:
            r"""Return the maximal elements."""
            ...

        @abstractmethod
        def cover_relations(
            self,
        ) -> builtins.list[tuple[PosetElement, PosetElement]]:
            r"""Return the cover relations."""
            ...

        @abstractmethod
        def cover_relations_iterator(
            self,
        ) -> Iterable[tuple[PosetElement, PosetElement]]:
            r"""Return an iterator over the cover relations."""
            ...

        @abstractmethod
        def covers(self, x: PosetElement, y: PosetElement) -> bool:
            r"""Return whether ``y`` covers ``x``."""
            ...

        @abstractmethod
        def closed_interval(
            self, x: PosetElement, y: PosetElement
        ) -> builtins.list[PosetElement]:
            r"""Return the closed interval ``[x, y]``."""
            ...

        @abstractmethod
        def open_interval(
            self, x: PosetElement, y: PosetElement
        ) -> builtins.list[PosetElement]:
            r"""Return the open interval ``(x, y)``."""
            ...

        @abstractmethod
        def interval(
            self, x: PosetElement, y: PosetElement
        ) -> builtins.list[PosetElement]:
            r"""Return the closed interval ``[x, y]``."""
            ...

        @abstractmethod
        def dual(self) -> Poset:
            r"""Return the dual poset."""
            ...

        @abstractmethod
        def subposet(self, elements: Iterable[PosetElement]) -> Poset:
            r"""Return the induced subposet on ``elements``."""
            ...

        @abstractmethod
        def height(self) -> Integer:
            r"""Return the height of the poset."""
            ...

        @final
        def height_certificate(self) -> tuple[Integer, builtins.list[PosetElement]]:
            r"""Return the height with a maximum-cardinality chain."""
            return SageFinitePoset.height(self, certificate=True)

        @abstractmethod
        def width(self) -> Integer:
            r"""Return the width of the poset."""
            ...

        @final
        def width_certificate(self) -> tuple[Integer, builtins.list[PosetElement]]:
            r"""Return the width with a maximum-cardinality antichain."""
            return SageFinitePoset.width(self, certificate=True)

        @abstractmethod
        def is_ranked(self) -> bool:
            r"""Return whether every maximal chain has the same length."""
            ...

        @abstractmethod
        def rank(self, element: PosetElement | None = None) -> Integer:
            r"""Return the rank of ``element`` or the rank of the poset."""
            ...

        @final
        def is_poset_morphism(self, f: PosetMorphism, codomain: Poset) -> bool:
            r"""Return whether ``f`` is order-preserving into ``codomain``."""
            return SageFinitePosets.ParentMethods.is_poset_morphism(self, f, codomain)

        @final
        def order_ideals_lattice(self, facade: bool = True) -> FiniteLatticePoset:
            r"""Return the finite distributive lattice of order ideals."""
            return SageFinitePosets.ParentMethods.order_ideals_lattice(
                self, as_ideals=True, facade=facade
            )

        @abstractmethod
        def is_meet_semilattice(self) -> bool:
            r"""Return whether every pair has a meet."""
            ...

        @final
        def meet_semilattice_certificate(
            self,
        ) -> tuple[bool, tuple[PosetElement, PosetElement] | None]:
            r"""Return semilattice status with a pair lacking a meet when false."""
            return SageFinitePoset.is_meet_semilattice(self, certificate=True)

        @abstractmethod
        def is_join_semilattice(self) -> bool:
            r"""Return whether every pair has a join."""
            ...

        @final
        def join_semilattice_certificate(
            self,
        ) -> tuple[bool, tuple[PosetElement, PosetElement] | None]:
            r"""Return semilattice status with a pair lacking a join when false."""
            return SageFinitePoset.is_join_semilattice(self, certificate=True)

        @abstractmethod
        def chains(self) -> Iterable[PosetSubset]:
            r"""Return the chains of this finite poset."""
            ...

        @abstractmethod
        def antichains(self) -> Iterable[PosetSubset]:
            r"""Return the antichains of this finite poset."""
            ...

        @abstractmethod
        def linear_extensions(self) -> Iterable[builtins.list[PosetElement]]:
            r"""Return the linear extensions of this finite poset."""
            ...

    class ElementMethods: ...
