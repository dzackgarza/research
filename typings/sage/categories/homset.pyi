from sage.categories.category import Category
from sage.structure.parent import Parent

class Homset(Parent):
    def __init__(
        self,
        domain: Parent,
        codomain: Parent,
        category: Category | None = ...,
        base: object = ...,
        check: bool = ...,
    ) -> None: ...

    def domain(self) -> Parent: ...
    def codomain(self) -> Parent: ...

# The homset constructor: Hom(X, Y) in the given category (the meet of the
# parents' categories when none is named).
def Hom(
    X: Parent,
    Y: Parent,
    category: Category | None = ...,
    check: bool = ...,
) -> Homset: ...
