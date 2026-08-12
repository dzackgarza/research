# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.categories.category_types import Category_over_base_ring

from sage.categories.category import Category

class Modules(Category_over_base_ring):
    def __init__(self, base_ring: Any = ...) -> None: ...
    def FiniteDimensional(self) -> Category: ...
    def WithBasis(self) -> Category: ...
