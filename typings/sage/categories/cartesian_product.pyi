# Sage reference implementation: sage/categories/cartesian_product.py.
from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.structure.parent import ElementConstructorInput

class CartesianProductsCategory(Category):
    class ParentMethods(
        Sets.ParentMethods[tuple[ElementConstructorInput, ...]],
    ):
        def cartesian_factors(
            self,
        ) -> tuple[Sets.ParentMethods[ElementConstructorInput], ...]: ...
