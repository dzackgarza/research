# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.structure.element import Element

class Groups(Category):
    def Commutative(self) -> Category: ...
    # Registered by the TopologicalSpaces functorial construction.
    def Topological(self) -> Category: ...

    class ParentMethods:
        # sage/categories/groups.py — the default implementations the owned
        # category calls explicitly before refining placement. The explicit
        # ``self: object`` admits unbound calls on any refined parent, which
        # is how dynamic_class applies these mixins.
        def group_generators(self: object) -> Iterable[Element]: ...
        def one(self: object) -> Element: ...

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
