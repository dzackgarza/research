# Repo-scoped stubs; see lexicon/README.md.
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom

class Groups(Category):
    def __init__(self) -> None: ...

    # Axiom categories are generated at runtime by the axiom machinery;
    # the stub names the ones this tree asks for.
    def FinitelyGenerated(self) -> CategoryWithAxiom: ...
