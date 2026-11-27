r"""Free modules."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, ModuleBasis, RModMorphism, RModule


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free modules over the base ring.

    Canonical chain: ``Modules(R).Free()``.
    """

    _base_category_class_and_axiom = (Modules, "Free")
    FiniteRank = LazyImport(__name__, "_FreeFiniteRank")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().Projective()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        @final
        def FiniteRank(self) -> Category:
            return self._with_axiom("FiniteRank")

    class ParentMethods:
        @override
        @final
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Return the cardinality of a basis."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules.

    Canonical chain: ``Modules(R).Free().FiniteRank()``.
    """

    _base_category_class_and_axiom = (_Free, "FiniteRank")
    WithForms = LazyImport("category_specs.forms.chain", "FiniteRankFreeFormedModulesCategory")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @abstract_method
        def bases(self) -> list[ModuleBasis]: ...

        @abstract_method
        def default_basis(self) -> ModuleBasis: ...

        @abstract_method
        def set_default_basis(self, basis: ModuleBasis) -> None: ...

        @abstract_method
        def dimension(self) -> Cardinality: ...

        @final
        def degree(self) -> Cardinality:
            return self.dimension()

        @override
        @abstract_method
        def tensor_module(
            self,
            k: Integer,
            l: Integer,
            *,
            sym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
            antisym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
        ) -> RModule: ...

        @abstract_method
        def exterior_power(self, p: Integer) -> RModule: ...

        @abstract_method
        def alternating_form(
            self,
            degree: Integer,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> RModMorphism: ...

    class ElementMethods: ...

    class MorphismMethods: ...
