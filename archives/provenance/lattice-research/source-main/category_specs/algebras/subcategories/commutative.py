r"""Commutative algebras."""

from __future__ import annotations

from typing import Any, final, override

from sage.categories.commutative_algebras import (
    CommutativeAlgebras as SageCommutativeAlgebras,
)

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras


class _CommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras whose multiplication is commutative.

    Canonical chain: ``Algebras(R).Commutative()``.
    """

    _base_category_class_and_axiom = (Algebras, "Commutative")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return algebra and Sage commutative-algebra supercategories."""
        R = self.base_ring()
        return [Algebras(R), SageCommutativeAlgebras(R)]

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is an algebra satisfying Sage commutativity."""
        return A in self.base_category() and A in SageCommutativeAlgebras(
            self.base_ring()
        )

    class ParentMethods:
        @final
        def is_commutative(self) -> bool:
            r"""Return ``True`` for objects in the commutative algebra category."""
            return True

    class ElementMethods: ...
