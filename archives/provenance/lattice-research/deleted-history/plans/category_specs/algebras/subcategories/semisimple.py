r"""Semisimple algebras."""

from __future__ import annotations

from typing import Any, final, override

from sage.categories.semisimple_algebras import SemisimpleAlgebras as SageSemisimpleAlgebras

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras


class _SemisimpleAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras whose Jacobson radical is zero.

    Canonical chain: ``Algebras(R).Semisimple()``.
    """

    _base_category_class_and_axiom = (Algebras, "Semisimple")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return algebra and Sage semisimple-algebra supercategories."""
        R = self.base_ring()
        return [Algebras(R), SageSemisimpleAlgebras(R)]

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is an algebra satisfying Sage semisimplicity."""
        return A in self.base_category() and A in SageSemisimpleAlgebras(self.base_ring())

    class ParentMethods:
        @final
        def is_semisimple(self) -> bool:
            r"""Return ``True`` for objects in the semisimple algebra category."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
