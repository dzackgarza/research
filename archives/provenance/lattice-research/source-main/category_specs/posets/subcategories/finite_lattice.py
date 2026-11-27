r"""Finite order-theoretic lattice poset subcategory."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Any, Literal, cast, final, override

from sage.categories.finite_lattice_posets import (
    FiniteLatticePosets as SageFiniteLatticePosets,
)
from sage.combinat.posets.lattices import FiniteLatticePoset as SageFiniteLatticePoset

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .finite_join_semilattice import _FiniteJoinSemilatticePosets
from .finite_meet_semilattice import _FiniteMeetSemilatticePosets
from .lattice import _LatticePosets

if TYPE_CHECKING:
    from ...types import (
        EquivalenceRelation,
        FiniteLatticePoset,
        LatticePoset,
        Poset,
        PosetElement,
    )


class _FiniteLatticePosets(CategoryWithAxiom):
    r"""Finite lattice posets.

    Canonical chain: ``Posets().Lattice().Finite()``.
    """

    _base_category_class_and_axiom = (_LatticePosets, "Finite")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return lattice, semilattice, and Sage finite-lattice supercategories."""
        return [
            _LatticePosets(),
            _FiniteMeetSemilatticePosets(),
            _FiniteJoinSemilatticePosets(),
            SageFiniteLatticePosets(),
        ]

    class ParentMethods:
        @abstractmethod
        def complements(
            self,
            element: PosetElement | None = None,
        ) -> list[PosetElement] | dict[PosetElement, list[PosetElement]]:
            r"""Return complements of ``element``, or all complements by element."""
            ...

        @abstractmethod
        def is_atomic(self) -> bool:
            r"""Return whether every element is a join of atoms."""
            ...

        @final
        def atomic_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return atomicity and a non-atomic join-irreducible if false."""
            return cast(
                "tuple[bool, PosetElement | None]",
                SageFiniteLatticePoset.is_atomic(cast(Any, self), certificate=True),
            )

        @abstractmethod
        def is_coatomic(self) -> bool:
            r"""Return whether every element is a meet of coatoms."""
            ...

        @final
        def coatomic_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return coatomicity and a non-coatomic meet-irreducible if false."""
            return cast(
                "tuple[bool, PosetElement | None]",
                SageFiniteLatticePoset.is_coatomic(cast(Any, self), certificate=True),
            )

        @abstractmethod
        def is_complemented(self) -> bool:
            r"""Return whether every element has a complement."""
            ...

        @final
        def complemented_certificate(self) -> tuple[bool, PosetElement | None]:
            r"""Return complementedness and an uncomplemented element if false."""
            return cast(
                "tuple[bool, PosetElement | None]",
                SageFiniteLatticePoset.is_complemented(
                    cast(Any, self), certificate=True
                ),
            )

        @abstractmethod
        def is_distributive(self) -> bool:
            r"""Return whether finite meets distribute over finite joins."""
            ...

        @final
        def distributive_certificate(
            self,
        ) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return distributivity status with a violating triple when false."""
            return cast(
                "tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]",
                SageFiniteLatticePoset.is_distributive(
                    cast(Any, self), certificate=True
                ),
            )

        @abstractmethod
        def is_modular(self) -> bool:
            r"""Return whether the lattice is modular."""
            ...

        @final
        def are_modular_elements(self, elements: Iterable[PosetElement]) -> bool:
            r"""Return whether every element in ``elements`` is modular."""
            return cast(
                bool,
                SageFiniteLatticePoset.is_modular(cast(Any, self), list(elements)),
            )

        @final
        def modular_certificate(
            self,
        ) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return modularity status with a violating triple when false."""
            return cast(
                "tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]",
                SageFiniteLatticePoset.is_modular(
                    cast(Any, self), certificate=True
                ),
            )

        @final
        def modular_elements_certificate(
            self,
            elements: Iterable[PosetElement],
        ) -> tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]:
            r"""Return modularity for ``elements`` and a violating triple if false."""
            return cast(
                "tuple[bool, tuple[PosetElement, PosetElement, PosetElement] | None]",
                SageFiniteLatticePoset.is_modular(
                    cast(Any, self), list(elements), certificate=True
                ),
            )

        @abstractmethod
        def is_semidistributive(self) -> bool:
            r"""Return whether the lattice is join- and meet-semidistributive."""
            ...

        @final
        def join_irreducibles(self) -> list[PosetElement]:
            r"""Return the join-irreducible elements."""
            return cast(
                "list[PosetElement]",
                SageFiniteLatticePosets.ParentMethods.join_irreducibles(self),
            )

        @final
        def join_irreducibles_poset(self) -> Poset:
            r"""Return the poset of join-irreducible elements."""
            return cast(
                "Poset",
                SageFiniteLatticePosets.ParentMethods.join_irreducibles_poset(self),
            )

        @final
        def meet_irreducibles(self) -> list[PosetElement]:
            r"""Return the meet-irreducible elements."""
            return cast(
                "list[PosetElement]",
                SageFiniteLatticePosets.ParentMethods.meet_irreducibles(self),
            )

        @final
        def meet_irreducibles_poset(self) -> Poset:
            r"""Return the poset of meet-irreducible elements."""
            return cast(
                "Poset",
                SageFiniteLatticePosets.ParentMethods.meet_irreducibles_poset(self),
            )

        @final
        def irreducibles_poset(self) -> Poset:
            r"""Return the poset of meet- and join-irreducible elements."""
            return cast(
                "Poset", SageFiniteLatticePosets.ParentMethods.irreducibles_poset(self)
            )

        @final
        def is_lattice_morphism(
            self, f: Callable[[PosetElement], PosetElement], codomain: LatticePoset
        ) -> bool:
            r"""Return whether ``f`` preserves finite meets and joins."""
            return cast(
                bool,
                SageFiniteLatticePosets.ParentMethods.is_lattice_morphism(
                    self, f, codomain
                ),
            )

        @abstractmethod
        def sublattice(self, elements: list[PosetElement]) -> LatticePoset:
            r"""Return the sublattice generated by ``elements``."""
            ...

        @abstractmethod
        def sublattices_lattice(self) -> LatticePoset:
            r"""Return the lattice of sublattices ordered by inclusion."""
            ...

        @abstractmethod
        def congruence(
            self, blocks: Iterable[Iterable[PosetElement]]
        ) -> EquivalenceRelation:
            r"""Return the congruence generated by ``blocks``."""
            ...

        @final
        def congruence_generated_by(
            self, blocks: Iterable[Iterable[PosetElement]]
        ) -> EquivalenceRelation:
            r"""Return the least congruence containing each block in ``blocks``."""
            return self.congruence(blocks)

        @abstractmethod
        def quotient(
            self,
            congruence: EquivalenceRelation,
            labels: Literal["tuple", "lattice", "integer"] = "tuple",
        ) -> FiniteLatticePoset:
            r"""Return the quotient lattice by ``congruence``."""
            ...

        @abstractmethod
        def congruences_lattice(
            self,
            labels: Literal["congruence", "integer"] = "congruence",
        ) -> FiniteLatticePoset:
            r"""Return the lattice of congruences ordered by refinement."""
            ...

        @final
        def congruence_lattice(
            self,
            labels: Literal["congruence", "integer"] = "congruence",
        ) -> FiniteLatticePoset:
            r"""Return the lattice of congruences ordered by refinement."""
            return self.congruences_lattice(labels=labels)

    class ElementMethods: ...
