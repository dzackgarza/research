r"""Tensor products of modules."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, final, override

from sage.categories.tensor import TensorProductFunctor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ....cat import Category, TensorProductsCategory

if TYPE_CHECKING:
    from ....types import RModule, RModuleElement

_TensorAlgebraComponents = LazyImport("category_specs.tensor_algebra_components", "TensorAlgebraComponents")


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules.

    Canonical chain: ``Modules(R).TensorProducts()``.
    """

    @cached_method
    @override
    @final
    def extra_super_categories(self):
        r"""Declare that M tensor_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        @final
        def construction(self) -> tuple[TensorProductFunctor, list[RModule]]:
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        @abstract_method
        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""Lift a product element to the tensor product."""
            ...

    class SubcategoryMethods:
        @cached_method
        @final
        def TensorAlgebraComponents(self) -> Category:
            r"""Return the category of graded pieces ``T_R(M)[p,q]``."""
            return _TensorAlgebraComponents(self.base_category().base_ring())

    class ElementMethods: ...
    class MorphismMethods: ...
