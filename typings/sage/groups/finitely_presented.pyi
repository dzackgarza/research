# Repo-scoped stubs; see lexicon/README.md.
#
# A finitely presented group F/N: consumed for its presentation data —
# the relators and the free group they normally generate.
from sage.categories.groups import Groups
from sage.structure.element import Element, MultiplicativeGroupElement

class FinitelyPresentedGroupElement(MultiplicativeGroupElement):
    def parent(self) -> FinitelyPresentedGroup: ...

class FinitelyPresentedGroup(Groups.ParentMethods[FinitelyPresentedGroupElement]):
    def relations(self) -> tuple[Element, ...]: ...
    def free_group(self) -> Parent: ...
