r"""Modules over Ore-polynomial quotient data."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category

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
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Modules(R).Free().FiniteRank()]

    class ParentMethods:
        @override
        @final
        def is_ore_module(self) -> bool:
            return True

        @abstractmethod
        def ore_polynomial_ring(self) -> Ring: ...

        @abstractmethod
        def pseudomorphism(self) -> RModMorphism: ...

        @abstractmethod
        def companion_matrix(self) -> Matrix: ...

        @abstractmethod
        def characteristic_polynomial(self) -> Polynomial: ...

        @abstractmethod
        def cyclic_vector(self) -> RModuleElement: ...

    class ElementMethods: ...
