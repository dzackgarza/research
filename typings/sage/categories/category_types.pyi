# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.categories.category import Category
from sage.categories.rings import Rings

class Category_over_base_ring(Category):
    def __init__(self, base: Any = ..., name: Any = ...) -> None: ...
    # A category over a base ring always has one (Modules(ZZ).base_ring() is
    # ZZ) — unlike a bare Parent, whose base_ring may be None.
    def base_ring(self) -> Rings.ParentMethods: ...

class Category_module(Category_over_base_ring): ...
