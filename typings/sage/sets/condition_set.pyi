# Repo-scoped stubs; see lexicon/README.md.
#
# The subset of a universe cut out by predicates. Its universe argument is a
# set, so the parameter is typed with the lexicon noun's realization
# (Sets.ParentMethods); the result is itself a set and declares that edge.
from collections.abc import Callable, Sequence
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.structure.parent import MembershipInput, Parent

_E = TypeVar("_E")

class ConditionSet(Sets.ParentMethods[_E], Generic[_E]):
    def __init__(
        self,
        universe: Parent[_E],
        *predicates: Callable[[_E], bool],
        names: Sequence[str] | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def __contains__(self, x: MembershipInput) -> bool: ...
