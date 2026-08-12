# Repo-scoped stubs; see lexicon/README.md.
#
# The subset of a universe cut out by predicates. Its universe argument is a
# set, so the parameter is typed with the lexicon noun's realization
# (Sets.ParentMethods); the result is itself a set and declares that edge.
from collections.abc import Sequence

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.structure.element import Element
from sage.structure.parent import Parent

class ConditionSet(Sets.ParentMethods[Element], Parent[Element]):
    def __init__(
        self,
        universe: Sets.ParentMethods[Element],
        *predicates: Element,
        names: Sequence[str] | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
