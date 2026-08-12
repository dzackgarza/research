# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring


class CategoryWithAxiom(Category):
    _base_category_class_and_axiom: tuple[type, str]
    def base_category(self) -> Category: ...


class CategoryWithAxiom_over_base_ring(Category_over_base_ring):
    _base_category_class_and_axiom: tuple[type, str]

class _AxiomSet:
    def __contains__(self, name: str) -> bool: ...
    def add(self, name: str) -> None: ...

all_axioms: _AxiomSet

def axiom(name: str) -> Any: ...
