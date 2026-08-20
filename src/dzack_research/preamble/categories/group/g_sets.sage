r"""\(G\)-sets and the owned torsor refinement.

``GSets(G)`` is the owned category of sets with a \(G\)-action.  The
defining datum is the action, and an action is a group morphism the caller
constructs — \(\rho:G\to\operatorname{Aut}(U(X))\) — so the category
requires it the way the owned module category requires its ring morphism
(``modules/pure/modules.sage``), and everything else is read off it: the
acting group is \(\rho\)'s domain, and ``act`` is evaluation.  No parent
here accepts a group plus raw images and assembles a morphism itself.

``Torsors(G)`` refines by the free transitive action.  A nonempty torsor
is identified with \(G\) only through a CHOSEN point (``an_element`` — a
choice, never canonical data).  From that choice the contract derives
enumeration (acting \(G\) through the chosen point is exhaustive by
transitivity and duplicate-free by freeness) and exact cardinality
(\(|T| = |G|\), since the trivialization is a bijection).
"""

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.g_sets import GSets as SageGSets
from sage.misc.abstract_method import abstract_method
from sage.misc.unknown import Unknown

if TYPE_CHECKING:
    from collections.abc import Iterator

    from sage.categories.groups import Group
    from sage.categories.morphism import Morphism
    from sage.structure.element import Element
    from dzack_research.preamble.categories.sets.cardinals import Cardinal


class GSets(Category):
    r"""The owned category of \(G\)-sets: sets with a \(G\)-action."""

    def __init__(self, group: "Group") -> None:
        self._group = group
        Category.__init__(self)

    def _repr_object_names(self) -> str:
        return f"{self._group} sets"

    def super_categories(self) -> list[Category]:
        return [SageGSets(self._group)]

    def acting_group(self) -> "Group":
        return self._group

    class ParentMethods:
        @abstract_method
        def action(self) -> "Morphism":
            r"""Return \(\rho:G\to\operatorname{Aut}(U(X))\), which is the action.

            The defining datum, constructed by the caller as a group
            morphism; a parent placed here without one has not been given
            a \(G\)-set structure, whatever category it sits in.
            """
            ...

        def acting_group(self) -> "Group":
            r"""The acting group: the domain of the action morphism."""
            return self.action().domain()

        def act(self, group_element: "Element", element: "Element") -> "Element":
            r"""Return \(g\cdot x\), which is \(\rho(g)(x)\) and nothing else."""
            return self.action()(group_element)(element)


class Torsors(Category):
    r"""\(G\)-torsors: free transitive \(G\)-sets."""

    def __init__(self, group: "Group") -> None:
        self._group = group
        Category.__init__(self)

    def _repr_object_names(self) -> str:
        return f"{self._group} torsors"

    def super_categories(self) -> list[Category]:
        return [GSets(self._group)]

    def acting_group(self) -> "Group":
        return self._group

    class ParentMethods:
        @abstract_method
        def an_element(self) -> "Element":
            r"""A CHOSEN point of the torsor — the trivializing choice.

            A torsor has no canonical point; this is extra data the
            concrete parent carries, and every derived operation below
            states which theorem lets it consume the choice.
            """
            ...

        def __iter__(self) -> "Iterator[Element]":
            r"""Enumeration through the trivializing choice.

            Acting the group through one chosen point is exhaustive by
            transitivity and duplicate-free by freeness.  Termination
            follows the acting group's own placement, not the torsor's:
            the iteration is the group's, transported by the bijection.
            """
            chosen = self.an_element()
            return (self.act(group_element, chosen) for group_element in self.acting_group())

        def cardinality(self) -> "Cardinal":
            r"""\(|T| = |G|\): the trivialization is a bijection."""
            from dzack_research.preamble.categories.sets.cardinals import cardinal

            return cardinal(self.acting_group().cardinality())

        def transporter(self, source: "Element", target: "Element") -> "Element | Unknown":
            r"""The unique \(g\) with \(g\cdot\text{source} = \text{target}\).

            Existence by transitivity, uniqueness by freeness.  No uniform
            algorithm lives on this node: computing \(g\) means inverting
            the trivialization, which is data of the concrete parent (a
            scan over \(G\) is the enumeration tell and does not land).
            Concrete torsor parents whose acting group placement supports
            a transporter computation override; here the answer is the
            stated unknown.
            """
            return Unknown
