from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.parent import Parent

# A homset is a parent whose elements are its morphisms
# (Homset._element_constructor_, homset.py:806); subclasses bind the
# parameter to their morphism class instead of re-declaring __call__.
_M = TypeVar("_M", bound=Element, default=Element, covariant=True)
# The two ends. Unbounded (default Parent) so a subclass may bind them to the
# structural protocol naming what its objects offer.
_D = TypeVar("_D", default=Parent, covariant=True)
_C = TypeVar("_C", default=Parent, covariant=True)

class Homset(Parent[_M], Generic[_M, _D, _C]):
    def __init__(
        self,
        domain: Parent,
        codomain: Parent,
        category: Category | None = ...,
        base: object = ...,
        check: bool = ...,
    ) -> None: ...

    def domain(self) -> _D: ...
    def codomain(self) -> _C: ...

# The homset constructor: Hom(X, Y) in the given category (the meet of the
# parents' categories when none is named).
def Hom(
    X: Parent,
    Y: Parent,
    category: Category | None = ...,
    check: bool = ...,
) -> Homset: ...
