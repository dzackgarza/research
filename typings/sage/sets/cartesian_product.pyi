# Sage reference implementation: sage/sets/cartesian_product.py.
from sage.categories.sets_cat import Sets
from sage.structure.parent import ElementConstructorInput

class CartesianProduct_iters(
    Sets.ParentMethods[tuple[ElementConstructorInput, ...]],
):
    def cartesian_factors(
        self,
    ) -> tuple[Sets.ParentMethods[ElementConstructorInput], ...]: ...
