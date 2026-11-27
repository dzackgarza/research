r"""Modules with a specified basis."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        CategoryElement,
        Integer,
        Matrix,
        ModuleBasis,
        Ring,
        RingElement,
        RModule,
        RModuleElement,
        RModuleMorphism,
    )


class _WithBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified basis.

    Canonical chain: ``Modules(R).WithBasis()``.
    """

    _base_category_class_and_axiom = (Modules, "WithBasis")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().Free()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_basis()

    class SubcategoryMethods:
        @final
        def WithOrderedBasis(self):
            return self.base_category().WithOrderedBasis()

    class ParentMethods:
        @override
        @final
        def has_basis(self) -> bool:
            return True

        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @final
        def basis_index_set(self):
            return self.basis().keys()

        @abstract_method
        def monomial(self, index: CategoryElement) -> RModuleElement:
            r"""Return the basis element indexed by ``index``."""
            ...

        @abstract_method
        def term(self, index: CategoryElement, coeff: RingElement | None = None) -> RModuleElement:
            r"""Return ``coeff`` times the basis element indexed by ``index``."""
            ...

        @abstract_method
        def linear_combination_of_basis(
            self,
            terms: dict[CategoryElement, RingElement] | Sequence[tuple[CategoryElement, RingElement]],
        ) -> RModuleElement:
            r"""Return the finite linear combination of basis terms."""
            ...

        @abstract_method
        def echelon_form(
            self,
            elements: Sequence[RModuleElement],
            row_reduced: bool = False,
            order: Sequence[CategoryElement] | Callable[[CategoryElement], Integer | str] | None = None,
        ) -> list[RModuleElement]: ...

        @abstract_method
        def reduce(self, x: RModuleElement) -> RModuleElement: ...

    class ElementMethods:
        @abstract_method
        def monomial_coefficients(self, copy: bool = True) -> dict[CategoryElement, RingElement]:
            r"""Return the finite coefficient map in the parent's basis."""
            ...

        @abstract_method
        def coefficient(self, index: CategoryElement) -> RingElement:
            r"""Return the coefficient of the basis element indexed by ``index``."""
            ...

        @abstract_method
        def support(self) -> list[CategoryElement]:
            r"""Return the finite basis support of this element."""
            ...

        @abstract_method
        def monomials(self) -> list[RModuleElement]:
            r"""Return the basis monomials appearing with nonzero coefficient."""
            ...

        @abstract_method
        def terms(self) -> list[RModuleElement]:
            r"""Return the nonzero scalar basis terms of this element."""
            ...

        @abstract_method
        def coefficients(self) -> list[RingElement]:
            r"""Return the nonzero coefficients in the basis expansion."""
            ...

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstract_method
            def from_basis_map(self, f: Callable[[CategoryElement], RModuleElement]) -> RModuleMorphism:
                r"""Return the module morphism determined by a map on basis indices."""
                ...

        class ElementMethods:
            @abstract_method
            def on_basis(self) -> Callable[[CategoryElement], RModuleElement]:
                r"""Return the basis-index map determining this morphism."""
                ...

        class MorphismMethods: ...

    class MorphismMethods: ...


class _WithOrderedBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified ordered basis.

    Canonical chain: ``Modules(R).WithOrderedBasis()``.
    """

    _base_category_class_and_axiom = (Modules, "WithOrderedBasis")

    @override
    @final
    def extra_super_categories(self):
        return [
            self.base_category().WithBasis(),
            self.base_category().WithOrderedGeneratingSet(),
        ]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_basis()

    class ParentMethods:
        @override
        @final
        def has_ordered_basis(self) -> bool:
            return True

        @final
        def basis_order(self) -> tuple[CategoryElement, ...]:
            return tuple(self.basis().keys())

        @final
        def user_basis(self) -> ModuleBasis:
            return self.basis()

        @abstract_method
        def basis_matrix(self, ring: Ring | None = None) -> Matrix: ...

        @abstract_method
        def echelonized_basis(self) -> ModuleBasis: ...

        @abstract_method
        def echelonized_basis_matrix(self) -> Matrix: ...

        @abstract_method
        def coordinate_vector(
            self,
            v: RModuleElement | Sequence[RingElement],
            check: bool = True,
        ) -> RModuleElement | Sequence[RingElement]: ...

        @abstract_method
        def coordinates(self, v: RModuleElement | Sequence[RingElement]) -> RModuleElement | Sequence[RingElement]: ...

        @abstract_method
        def from_vector(
            self,
            vector: RModuleElement | Sequence[RingElement],
            order: Sequence[CategoryElement] | None = None,
            coerce: bool = True,
        ) -> RModuleElement: ...

        @abstract_method
        def coordinate_module(self, V: RModule) -> RModule: ...

        @abstract_method
        def matrix(self) -> Matrix: ...

    class ElementMethods:
        @abstract_method
        def list(self) -> list[RingElement]: ...

        @abstract_method
        def vector(self) -> RModuleElement | Sequence[RingElement]: ...

        @abstract_method
        def degree(self) -> Integer: ...

    class MorphismMethods: ...
