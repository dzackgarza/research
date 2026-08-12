# Category-first typing; see categories/rings.pyi for the pattern.
from typing import Any

from sage.categories.category import Category
from sage.categories.rings import Rings

class Fields(Category):
    def __init__(self) -> None: ...

    class ParentMethods(Rings.ParentMethods):
        def fraction_field(self) -> Any: ...

    class ElementMethods: ...
