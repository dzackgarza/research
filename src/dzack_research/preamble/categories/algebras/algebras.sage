r"""Framed algebras over a base ring R.

A framed R-algebra is equipped with a chosen surjection from a free R-algebra on
a set S, exactly as a framed R-module is equipped with a surjection from a free
R-module on S.
"""

from sage.categories.category_types import Category_over_base_ring
from sage.categories.algebras import Algebras as SageAlgebras
from sage.misc.abstract_method import abstract_method


class Algebras(Category_over_base_ring):
    r"""Associative unital algebras over a base ring (R)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "algebras"

    def super_categories(self) -> list:
        return [SageAlgebras(self.base_ring())]

    class SubcategoryMethods:
        def Free(self):
            r"""Return the free-algebra subcategory over this base ring."""
            return FreeAlgebras(self.base_ring())

    class ParentMethods:
        def is_algebra(self) -> bool:
            r"""Return whether this parent is declared to be an (R)-algebra."""
            return True


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
            r"""Return the product of generators labelled by s and t in S."""


def install_algebras() -> None:
    r"""Register post-init hooks and installation for algebras."""
    pass
