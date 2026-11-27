r"""Modules over Ore-polynomial quotient data."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Matrix, Polynomial, Ring, RModMorphism, RModuleElement



class _OreModules(Category_over_base_ring):
    r"""Finite free modules over an Ore polynomial ring quotient.

    Constructor target: ``Modules(R).Constructors().OreQuotientModule(...)``
    refines Sage Ore quotient modules here.
    """

    @override
    @final
    def super_categories(self):
        R = self.base_ring()
        return [Modules(R).Free().FiniteRank()]

    class ParentMethods:
        @override
        @final
        def is_ore_module(self) -> bool:
            return True

        @abstract_method
        def ore_polynomial_ring(self) -> Ring: ...

        @abstract_method
        def pseudomorphism(self) -> RModMorphism: ...

        @abstract_method
        def companion_matrix(self) -> Matrix: ...

        @abstract_method
        def characteristic_polynomial(self) -> Polynomial: ...

        @abstract_method
        def cyclic_vector(self) -> RModuleElement: ...

    class ElementMethods: ...
    class MorphismMethods: ...
