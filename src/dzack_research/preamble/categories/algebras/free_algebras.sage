r"""Free algebras over a base ring, without a chosen generating set."""

from sage.categories.category_types import Category_over_base_ring


class FreeAlgebras(Category_over_base_ring):
    r"""Category of free commutative algebras over a base ring, without a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free algebras"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring())]

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this algebra is free."""
            return True
