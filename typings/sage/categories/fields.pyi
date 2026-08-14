# Category-first typing; see categories/rings.pyi for the pattern.

from sage.categories.category import Category
from sage.categories.rings import Rings

class Fields(Category):
    def __init__(self) -> None: ...

    class ParentMethods(Rings.ParentMethods):
        # The fraction field of a field is a field (verified:
        # QQ.fraction_field() is a RationalField), and of a domain a field.
        def fraction_field(self) -> Fields.ParentMethods: ...

    class ElementMethods: ...
