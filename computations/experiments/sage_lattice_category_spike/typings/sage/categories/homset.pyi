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
