r"""Finite order-theoretic lattice poset subcategory."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Literal, final, override

from sage.categories.finite_lattice_posets import FiniteLatticePosets as SageFiniteLatticePosets
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .finite_join_semilattice import _FiniteJoinSemilatticePosets
from .finite_meet_semilattice import _FiniteMeetSemilatticePosets
from .lattice import _LatticePosets

if TYPE_CHECKING:
    from ...types import EquivalenceRelation, FiniteLatticePoset, LatticePoset, PosetElement


class _FiniteLatticePosets(CategoryWithAxiom):
    r"""Finite lattice posets.

    Canonical chain: ``Posets().Lattice().Finite()``.
    """

    _base_category_class_and_axiom = (_LatticePosets, "Finite")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return lattice, finite semilattice, and Sage finite-lattice supercategories."""
        return [
            _LatticePosets(),
            _FiniteMeetSemilatticePosets(),
            _FiniteJoinSemilatticePosets(),
            SageFiniteLatticePosets(),
        ]

    class ParentMethods:
        @abstract_method
        def complements(
            self,
            element: PosetElement | None = None,
        ) -> list[PosetElement] | dict[PosetElement, list[PosetElement]]:
            r"""Return complements of ``element``, or all complements by element."""
            ...

        @abstract_method
        def is_atomic(self) -> bool:
            r"""Return whether every element is a join of atoms."""
            ...

        @abstract_method
        def atomic_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return atomicity status with a non-atomic join-irreducible when false."""
            ...

        @abstract_method
        def is_coatomic(self) -> bool:
            r"""Return whether every element is a meet of coatoms."""
            ...

        @abstract_method
        def coatomic_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return coatomicity status with a non-coatomic meet-irreducible when false."""
            ...

        @abstract_method
        def is_complemented(self) -> bool:
            r"""Return whether every element has a complement."""
            ...

        @abstract_method
        def complemented_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return complementedness status with an uncomplemented element when false."""
            ...

        @abstract_method
        def is_distributive(self) -> bool:
            r"""Return whether finite meets distribute over finite joins."""
            ...

        @abstract_method
        def distributive_certificate(
            self,
        ) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return distributivity status with a violating triple when false."""
            ...

        @abstract_method
        def is_modular(self) -> bool:
            r"""Return whether the lattice is modular."""
            ...

        @abstract_method
        def are_modular_elements(self, elements: Iterable[PosetElement]) -> bool:
            r"""Return whether every element in ``elements`` is modular."""
            ...

        @abstract_method
        def modular_certificate(self) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return modularity status with a violating triple when false."""
            ...

        @abstract_method
        def modular_elements_certificate(
            self,
            elements: Iterable[PosetElement],
        ) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return modularity status for ``elements`` with a violating triple when false."""
            ...

        @abstract_method
        def is_semidistributive(self) -> bool:
            r"""Return whether the lattice is join- and meet-semidistributive."""
            ...

        @abstract_method
        def join_irreducibles(self) -> list[PosetElement]:
            r"""Return the join-irreducible elements."""
            ...

        @abstract_method
        def join_irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of join-irreducible elements."""
            ...

        @abstract_method
        def meet_irreducibles(self) -> list[PosetElement]:
            r"""Return the meet-irreducible elements."""
            ...

        @abstract_method
        def meet_irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of meet-irreducible elements."""
            ...

        @abstract_method
        def irreducibles_poset(self) -> FiniteLatticePoset:
            r"""Return the poset of meet- and join-irreducible elements."""
            ...

        @abstract_method
        def is_lattice_morphism(self, f: Callable[[PosetElement], PosetElement], codomain: LatticePoset) -> bool:
            r"""Return whether ``f`` preserves finite meets and joins."""
            ...

        @abstract_method
        def sublattice(self, elements: list[PosetElement]) -> LatticePoset:
            r"""Return the sublattice generated by ``elements``."""
            ...

        @abstract_method
        def sublattices_lattice(self) -> LatticePoset:
            r"""Return the lattice of sublattices ordered by inclusion."""
            ...

        @abstract_method
        def congruence_generated_by(self, blocks: Iterable[Iterable[PosetElement]]) -> EquivalenceRelation:
            r"""Return the least congruence containing each block in ``blocks``."""
            ...

        @abstract_method
        def quotient(
            self,
            congruence: EquivalenceRelation,
            labels: Literal["tuple", "lattice", "integer"] = "tuple",
        ) -> FiniteLatticePoset:
            r"""Return the quotient lattice by ``congruence``."""
            ...

        @abstract_method
        def congruence_lattice(
            self,
            labels: Literal["congruence", "integer"] = "congruence",
        ) -> FiniteLatticePoset:
            r"""Return the lattice of congruences ordered by refinement."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...
