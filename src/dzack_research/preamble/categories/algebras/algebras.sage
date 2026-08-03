r"""Framed algebras over a base ring R.

A framed R-algebra is equipped with a chosen surjection from a free R-algebra on
a set S, exactly as a framed R-module is equipped with a surjection from a free
R-module on S.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.algebras import Algebras as SageAlgebras
from sage.misc.abstract_method import abstract_method
from sage.structure.parent import Parent


class Algebras(Category_over_base_ring):
    r"""Associative unital algebras over a base ring (R)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "algebras"

    def __contains__(self, algebra: Any) -> bool:
        """Return whether ``algebra`` is an explicit ``R``-algebra witness."""
        if SageAlgebras.__contains__(self, algebra):
            return True

        if not isinstance(algebra, Parent):
            return False

        return bool(algebra.coerce_map_from(self.base_ring()))

    def super_categories(self) -> list:
        return [SageAlgebras(self.base_ring())]

    class ParentMethods:
        def algebra_structure_map(self) -> Any:
            """Return the explicit structure map from the base ring."""
            witness = self.coerce_map_from(self.base_ring())
            if not witness:
                raise ValueError(f"{self} has no structure map from {self.base_ring()}")
            return witness

        def base_change(self, ring_hom: Any) -> Any:
            r"""Base change this algebra along a ring morphism."""
            assert hasattr(ring_hom, "domain") and hasattr(
                ring_hom, "codomain"
            ), "base_change requires a ring morphism"
            assert ring_hom.domain() == self.base_ring(), (
                "the map must have this algebra's base ring as domain"
            )
            if ring_hom.codomain() == self.base_ring():
                return self
            return self.change_ring(ring_hom.codomain())

        def is_algebra(self) -> bool:
            r"""Return whether this parent is declared to be an (R)-algebra."""
            return True

    class SubcategoryMethods:
        def Free(self):
            r"""Return the free-algebra subcategory over this base ring."""
            return FreeAlgebras(self.base_ring())

        def FinitelyPresented(self):
            from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
                FinitelyPresentedAlgebras,
            )
            return FinitelyPresentedAlgebras(self.base_ring())

class FramedAlgebras(Category_over_base_ring):
    r"""R-algebras carrying a specified surjection \(\operatorname{FreeAlg}_R(S) \to A\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed algebras"

    def super_categories(self) -> list:
        return [Algebras(self.base_ring()), FramedModules(self.base_ring())]

    class ParentMethods:

        @abstract_method
        def product_on_generators(self, s, t) -> object:
            r"""Return the product of algebra_generators labelled by s and t in S."""


_ALGEBRAS_INSTALLED = False


def install_algebras() -> None:
    r"""Register post-init hooks and installation for algebras."""
    global _ALGEBRAS_INSTALLED

    if _ALGEBRAS_INSTALLED:
        return

    _ALGEBRAS_INSTALLED = True
