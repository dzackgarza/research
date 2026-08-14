# Category-first typing; see categories/rings.pyi for the pattern.
# Sets.ParentMethods is the static type of "a mathematical set" -- the lexicon
# noun ``Set`` (INVENTORY.md II.1). It is generic in the element type, because
# a set is known by what its members are; the stub tree declares the
# mathematically true MRO edge on each set implementation it stubs
# (TotallyOrderedFiniteSet, ImageSubobject, ...), so those satisfy the noun
# without a migration.
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.parent import Parent

_E = TypeVar("_E", bound=Element, default=Element, covariant=True)

class Sets(Category):
    def __init__(self) -> None: ...

    # A set IS a Sage Parent: the holder class declares the edge the runtime
    # realizes by copying ParentMethods into each parent's dynamic class.
    # NOTE: ``cardinality`` is deliberately NOT declared here -- Sage places it
    # on EnumeratedSets and on Sets().Infinite(), and a bare set carries no
    # counting operation. A site that counts is typed by the set kind that
    # can count (INVENTORY.md II.1).
    class ParentMethods(Parent[_E], Generic[_E]):
        def __contains__(self, x: object) -> bool: ...
        def is_parent_of(self, element: object) -> bool: ...
        def an_element(self) -> _E: ...
        def some_elements(self) -> list[_E]: ...

    class ElementMethods: ...

# Canonical short name for "a mathematical set" (a Sage object, so it
# belongs with the Sage typing, not with preamble vocabulary). Type-only:
# Sage's runtime sage.categories.sets_cat exports ``Sets``, not ``Set`` —
# code that imports this name does so under TYPE_CHECKING.
Set = Sets.ParentMethods
