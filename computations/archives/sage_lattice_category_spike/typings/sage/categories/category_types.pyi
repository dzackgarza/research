# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.categories.category import Category

class Category_over_base_ring(Category):
    def __init__(self, base: Any = ..., name: Any = ...) -> None: ...
    def base_ring(self) -> Any: ...
