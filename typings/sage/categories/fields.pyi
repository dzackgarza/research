# Category-first typing; see categories/rings.pyi for the pattern.

from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.rings import Rings
from sage.structure.element import FieldElement

_CategoryElement = TypeVar(
    "_CategoryElement",
    bound=FieldElement,
    default=FieldElement,
    covariant=True,
)
_ParentElement = TypeVar(
    "_ParentElement",
    bound=FieldElement,
    default=FieldElement,
    covariant=True,
)

class Fields(Category, Generic[_CategoryElement]):
    def __init__(self) -> None: ...

    class ParentMethods(Rings.ParentMethods[_ParentElement], Generic[_ParentElement]):
        # The fraction field of a field is a field (verified:
        # QQ.fraction_field() is a RationalField), and of a domain a field.
        def fraction_field(self) -> Fields.ParentMethods[_ParentElement]: ...

    class ElementMethods: ...
