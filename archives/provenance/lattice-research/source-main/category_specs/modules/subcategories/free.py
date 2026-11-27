r"""Free modules."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override

from sage.categories.category import Category
from sage.misc.lazy_import import LazyImport
from sage.modules.free_module import FreeModule as SageFreeModule
from sage.modules.free_module import FreeModule_generic as SageFreeModuleGeneric
from sage.tensor.modules.finite_rank_free_module import (
    FiniteRankFreeModule as SageFiniteRankFreeModule,
)

from ...cat import CategoryWithAxiom_over_base_ring
from ...utils import with_axiom
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        Algebra,
        Cardinality,
        DualModule,
        Integer,
        ModuleBasis,
        RingMorphism,
        RModMorphism,
        RModule,
    )

_F = TypeVar("_F", bound=Callable[..., object])


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free modules over the base ring.

    Canonical chain: ``Modules(R).Free()``.
    """

    _base_category_class_and_axiom = (Modules, "Free")
    FiniteRank = LazyImport(__name__, "_FreeFiniteRank")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().Projective()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @final
        def FiniteRank(self) -> Category:
            return with_axiom(self, "FiniteRank")

    class ParentMethods:
        @override
        @final
        def is_free(self) -> bool:
            return True

        @abstractmethod
        def rank(self) -> Cardinality:
            r"""Return the cardinality of a basis."""
            ...

    class ElementMethods: ...



class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules.

    Canonical chain: ``Modules(R).Free().FiniteRank()``.
    """

    _base_category_class_and_axiom = (_Free, "FiniteRank")
    WithForms = LazyImport(
        "category_specs.forms.chain", "FiniteRankFreeFormedModulesCategory"
    )

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @override
        @abstractmethod
        def rank(self) -> Integer:
            r"""Return the finite rank of this free module."""
            ...

        @abstractmethod
        def basis(self) -> ModuleBasis: ...

        @override
        @final
        def bases(self) -> list[ModuleBasis]:
            if isinstance(self, SageFiniteRankFreeModule):
                return cast(list[ModuleBasis], SageFiniteRankFreeModule.bases(self))
            assert isinstance(self, SageFreeModuleGeneric)
            return [self.basis()]

        @override
        @final
        def default_basis(self) -> ModuleBasis:
            if isinstance(self, SageFiniteRankFreeModule):
                return SageFiniteRankFreeModule.default_basis(self)
            assert isinstance(self, SageFreeModuleGeneric)
            return self.basis()

        @override
        @final
        def set_default_basis(self, basis: ModuleBasis) -> None:
            if isinstance(self, SageFiniteRankFreeModule):
                SageFiniteRankFreeModule.set_default_basis(self, basis)
                return None
            assert isinstance(self, SageFreeModuleGeneric)
            if basis != self.basis():
                raise NotImplementedError(
                    "ambient Sage free modules have a fixed canonical basis"
                )
            return None

        @override
        @final
        def dimension(self) -> Cardinality:
            return self.rank()

        @final
        def degree(self) -> Cardinality:
            return self.dimension()

        @override
        @final
        def symmetric_algebra(self) -> Algebra:
            from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

            return cast(
                "Algebra",
                PolynomialRing(
                    self.base_ring(),
                    names=tuple(f"x{i}" for i in range(int(self.rank()))),
                ),
            )

        @override
        @final
        def alternating_algebra(self) -> Algebra:
            from sage.algebras.clifford_algebra import ExteriorAlgebra

            return cast(
                "Algebra",
                ExteriorAlgebra(
                    self, names=tuple(f"e{i}" for i in range(int(self.rank())))
                ),
            )

        @override
        @final
        def determinant_module(self) -> RModule:
            return self.exterior_power(self.rank())

        @override
        @final
        def dual(self) -> DualModule:
            if isinstance(self, SageFiniteRankFreeModule):
                return cast("DualModule", SageFiniteRankFreeModule.dual(self))

            assert isinstance(self, SageFreeModuleGeneric)
            return cast("DualModule", self.Hom(SageFreeModule(self.base_ring(), 1)))

        @override
        @final
        def is_isomorphic_to(self, other: RModule) -> bool:
            if isinstance(other, (SageFiniteRankFreeModule, SageFreeModuleGeneric)):
                return bool(
                    self.base_ring() == other.base_ring()
                    and self.rank() == other.rank()
                )
            return False

        @override
        @abstractmethod
        def tensor_module(
            self,
            k: Integer,
            ell: Integer,
            *,
            sym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
            antisym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
        ) -> RModule:
            ...

        @override
        @final
        def exterior_power(self, p: Integer) -> RModule:
            if isinstance(self, SageFiniteRankFreeModule):
                return cast("RModule", SageFiniteRankFreeModule.exterior_power(self, p))

            from sage.algebras.clifford_algebra import ExteriorAlgebra

            assert isinstance(self, SageFreeModuleGeneric)
            exterior_algebra = ExteriorAlgebra(
                self, names=tuple(f"e{i}" for i in range(int(self.rank())))
            )
            return cast("RModule", exterior_algebra.homogeneous_component(p))

        @override
        @final
        def alternating_form(
            self,
            degree: Integer,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> RModMorphism:
            return cast(
                "RModMorphism",
                SageFiniteRankFreeModule.alternating_form(
                    self, degree, name=name, latex_name=latex_name
                ),
            )

        @override
        @final
        def base_change(self, morphism: RingMorphism) -> RModule:
            assert morphism.domain() == self.base_ring()
            return cast("RModule", self.change_ring(morphism.codomain()))

    class ElementMethods: ...
