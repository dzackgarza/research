# Repo-scoped stubs; see lexicon/README.md.
#
# A finitely presented group F/N: consumed for its presentation data —
# the relators and the free group they normally generate.
from sage.structure.element import Element
from sage.structure.parent import Parent

class FinitelyPresentedGroup(Parent):
    def relations(self) -> tuple[Element, ...]: ...
    def free_group(self) -> Parent: ...
