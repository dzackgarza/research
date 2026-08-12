# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable

from sage.categories.category import Category
from sage.structure.element import Element
from sage.categories.category_with_axiom import CategoryWithAxiom

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
    def __init__(self) -> None: ...

    # Axiom categories are generated at runtime by the axiom machinery;
    # the stub names the ones this tree asks for.
    def FinitelyGenerated(self) -> CategoryWithAxiom: ...
