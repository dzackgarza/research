r"""Functorial construction categories for ``Modules(R)``."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.dual import DualObjectsCategory
from sage.categories.quotients import QuotientsCategory
from sage.categories.subobjects import SubobjectsCategory
from sage.categories.tensor import TensorProductFunctor, TensorProductsCategory
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    Cardinality = Integer | InfinityElement
    QuotientModule = Parent
    RingElement = Element
    RModule = Parent
    RModuleElement = Element
    SubModule = Parent


class _DualObjects(DualObjectsCategory):
    r"""Dual modules M^* := Hom_R(M, R) viewed as integral linear forms."""

    def extra_super_categories(self):
        r"""The dual M^* of an R-module is an integral linear form, i.e. an
        object of ``Modules(R).Homsets().Forms().Linear().Integral()``.
        """
        return [self.base_category().Homsets().Forms().Linear().Integral()]


class _Subobjects(SubobjectsCategory):
    r"""Submodule category.

    Extends ``RegressiveCovariantConstructionCategory`` so ``C.Subobjects()``
    is always a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's SubobjectsCategory.
    """

    @abstract_method
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @abstract_method
        def inclusion(self): ...

        @abstract_method
        def intersect(self, N: SubModule) -> SubModule: ...

        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        def index(self) -> Cardinality:
            return self.inclusion().index()

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        @abstract_method
        def saturation(self) -> SubModule: ...

        @abstract_method
        def __le__(self, other: RModule) -> bool: ...

        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()


class _Quotients(QuotientsCategory):
    r"""Quotient module category.

    Extends ``RegressiveCovariantConstructionCategory`` so ``C.Quotients()``
    is always a subcategory of ``C``.

    TODO: enumerate methods already provided by Sage's QuotientsCategory.
    """

    class ParentMethods:
        @abstract_method
        def projection(self): ...

    class ElementMethods:
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products of R-modules.

    TODO: verify
    r * (m_1 \otimes ... \otimes m_n)
        = (r * m_1) \otimes ... \otimes m_n
        = m_1 \otimes ... \otimes (r * m_n)
    holds at the level of the spec.
    """

    @cached_method
    def extra_super_categories(self):
        r"""Declare that M \otimes_R N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def construction(self):
            factors = self.tensor_factors()
            return (TensorProductFunctor(), factors)

        @abstract_method
        def tensor_factors(self) -> list[RModule]: ...

        @abstract_method
        def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
            r"""Given an ordered set {m_1, ..., m_n} with m_i in M_i, where
            this module is M = M_1 \otimes_R ... \otimes_R M_n, lift the
            product element (m_1, ..., m_n) to m_1 \otimes ... \otimes m_n.
            """
            ...


class _CartesianProducts(CartesianProductsCategory):
    def extra_super_categories(self):
        r"""Declare that M x N is again an R-module."""
        return [self.base_category()]

    class ParentMethods:
        def __init_extra__(self):
            factors = self._sets
            assert len(factors) > 0, f"No factors found in {self}: {factors}"
            R = factors[0].base_ring()
            assert all(Mi.base_ring() is R for Mi in factors)
            self._base = R

    class ElementMethods:
        def _lmul_(self, x: RingElement):
            return self.parent()._cartesian_product_of_elements(x * y for y in self.cartesian_factors())
