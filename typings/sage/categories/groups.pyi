# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.structure.element import MultiplicativeGroupElement
from sage.structure.parent import Parent

_E = TypeVar(
    "_E",
    bound=MultiplicativeGroupElement,
    default=MultiplicativeGroupElement,
    covariant=True,
)

class Groups(Category):
    def Commutative(self) -> Category: ...
    # Registered by the TopologicalSpaces functorial construction.
    def Topological(self) -> Category: ...

    class ParentMethods(Parent[_E], Generic[_E]):
        # sage/categories/groups.py supplies these methods to each group
        # parent through Sage's dynamic category classes.
        def group_generators(self) -> Iterable[_E]: ...
        def one(self) -> _E: ...

    # The element-side surface (lexicon ``GroupElement``); element classes
    # declare their own arithmetic, so the category marker stays empty like
    # Rings.ElementMethods.
    class ElementMethods: ...

    def __init__(self) -> None: ...

    # Axiom categories are generated at runtime by the axiom machinery;
    # the stub names the ones this tree asks for.
    def FinitelyGenerated(self) -> CategoryWithAxiom: ...

# Canonical short names for "a group parent" and "a group element" (Sage
# objects, so they belong with the Sage typing, not with preamble
# vocabulary). Type-only: Sage's runtime sage.categories.groups exports
# ``Groups``, not ``Group``/``GroupElement`` — code that imports these names
# does so under TYPE_CHECKING.
Group = Groups.ParentMethods
GroupElement = Groups.ElementMethods
