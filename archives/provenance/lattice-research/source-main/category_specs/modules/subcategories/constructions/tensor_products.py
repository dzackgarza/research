r"""Tensor products of modules."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, TypeVar, cast, final, override

from sage.categories.tensor import TensorProductFunctor
from sage.misc.lazy_import import LazyImport

from ....cat import Category, TensorProductsCategory

if TYPE_CHECKING:
    from ....types import RMod, RModule, RModuleElement

_TensorAlgebraComponents = LazyImport(
    "category_specs.tensor_algebra_components", "TensorAlgebraComponents"
)

_F = TypeVar("_F", bound=Callable[..., object])


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules.

    Canonical chain: ``Modules(R).TensorProducts()``.
    """
    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Declare that M tensor_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        @final
        def construction(self) -> tuple[TensorProductFunctor, list[RModule]]:
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstractmethod
        def tensor_factors(self) -> list[RModule]: ...

        @abstractmethod
        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""Lift a product element to the tensor product."""
            ...

    class SubcategoryMethods:
        @abstractmethod
        def base_category(self) -> RMod: ...
        @final
        def TensorAlgebraComponents(self) -> Category:
            r"""Return the category of graded pieces ``T_R(M)[p,q]``."""
            return cast(
                Category, _TensorAlgebraComponents(self.base_category().base_ring())
            )

    class ElementMethods: ...
