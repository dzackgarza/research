# Repo-scoped stubs; see lexicon/README.md.
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.rings import Rings
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement, covariant=True)

class Category_over_base_ring(Category, Generic[_Scalar]):
    def __init__(self, base: Rings.ParentMethods[_Scalar], name: str | None = ...) -> None: ...
    # A category over a base ring always has one (Modules(ZZ).base_ring() is
    # ZZ) — unlike a bare Parent, whose base_ring may be None.
    def base_ring(self) -> Rings.ParentMethods[_Scalar]: ...

class Category_module(Category_over_base_ring[_Scalar], Generic[_Scalar]): ...
