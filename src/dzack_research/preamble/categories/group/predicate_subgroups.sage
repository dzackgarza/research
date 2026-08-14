r"""Subgroups cut out of an ambient group by a membership predicate.

A subgroup of \(O(L)\) cannot be built from generators: computing even a
generating set of \(O(L)\) for a common indefinite lattice runs for days.
What is always available is *containment* -- deciding \(f\in H\) -- so a
subgroup is specified by the predicate that decides it, together with the
inclusion recording it as a subobject of the ambient group.

Nothing is enumerated and nothing is closed.  Cardinality, finiteness,
finite generation and a generating set are questions such a subgroup is
entitled not to know: each is a theorem or an expensive computation, and an
operation needing one asks for it at the point of use rather than having the
constructor presume it.

The centralizer \(Z_G(f)=\{g\in G:[f,g]=1\}\) is the shape of all of them,
as are normalizers, stabilizers of a sublattice, and the kernel of
\(O(L)\to O(A_L)\).
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput
if TYPE_CHECKING:
    from typing import Callable

if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from sage.categories.groups import Group

from sage.categories.groups import Groups
from sage.categories.category import Category
from sage.structure.parent import Parent


class PredicateSubgroup(Parent):
    r"""The subgroup \(\{g\in G: P(g)\}\) of an ambient group \(G\)."""

    def __init__(
        self,
        containing_group: "Group",
        predicate: "Callable",
        description: str,
    ) -> None:
        assert containing_group in Groups(), (
            f"{containing_group} is not a group, so it has no subgroups"
        )
        # Stored before ``Parent.__init__`` so identity is answerable while
        # Sage's caches hash this object during construction.
        self._containing_group = containing_group
        self._predicate = predicate
        self._description = description
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        Parent.__init__(
            self,
            category=Category.join([OwnedGroups(), Groups().Subobjects()]),
        )

    def supergroup(self) -> "Group":
        r"""Return \(G\), the group this is a subgroup of."""
        return self._containing_group

    def defining_predicate(self) -> "Callable":
        r"""Return \(P\), the predicate deciding membership."""
        return self._predicate

    def __contains__(self, element: "Element") -> bool:
        r"""Return whether \(g\in G\) and \(P(g)\) -- the one always-available operation."""
        return element in self._containing_group and bool(self._predicate(element))

    def _element_constructor_(self, element: "Element") -> "Element":
        assert element in self, f"{element} does not satisfy {self._description}"
        return element

    def one(self) -> "Element":
        identity = self._containing_group.one()
        assert identity in self, (
            f"{self._description} does not contain the identity, so it is "
            "not a subgroup"
        )
        return identity

    def __hash__(self) -> int:
        return hash((type(self), self._containing_group, self._description))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._containing_group == other._containing_group
            and self._description == other._description
        )

    def _repr_(self) -> str:
        return f"{{g in {self._containing_group} : {self._description}}}"


def centralizer(containing_group: "Group", element: "Element") -> PredicateSubgroup:
    r"""Return \(Z_G(f)=\{g\in G:[f,g]=1\}\)."""
    assert element in containing_group, f"{element} is not in {containing_group}"
    return PredicateSubgroup(
        containing_group,
        lambda candidate: element * candidate == candidate * element,
        f"g commutes with {element}",
    )
