r"""Integral lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category

from ...cat import Cat, Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Matrix


class _IntegerLattices(Category_over_base_ring):
    r"""Finite-rank integral bilinear modules with lattice algorithms.

    Constructor target: ``Modules(ZZ).Constructors().IntegerLattice(...)``
    refines here as the legacy module-side route toward ``Lattices(ZZ)``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Cat().join(
                [
                    Modules(R).Subobjects(),
                    Modules(R).WithOrderedGeneratingSet(),
                    Modules(R).OverPID(),
                    Modules(R).WithForms().Bilinear(),
                ]
            )
        ]

    class ParentMethods:
        @override
        @final
        def is_lattice(self) -> bool:
            return True

        @abstractmethod
        def gram_matrix(self) -> Matrix: ...

    class ElementMethods: ...
