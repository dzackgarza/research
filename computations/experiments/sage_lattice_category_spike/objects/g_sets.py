r"""G-sets and the owned torsor refinement.

The owned ``GSets(G)`` integrates Sage's standard node and is a
structured forwarding root exactly like the operation roots: generic set
behavior routes through the underlying-set functor, and nothing below
repeats it.

``Torsors(G)`` is the project-owned refinement by the standard free
transitive action. The refinement is executable: a nonempty torsor is
identified with ``G`` only through a CHOSEN element (``an_element`` — a
choice, never canonical data), and from that choice the contract
constructs enumeration (acting the group through the chosen element is
exhaustive and duplicate-free by freeness and transitivity), exact
cardinality (``|T| = |G|``), and the unique transporter between any two
points. ``Aut`` obligations stay abstract here: no uniform automorphism
algorithm is invented merely because the category exists.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, cast

from sage.categories.category import Category
from sage.categories.g_sets import GSets as SageGSets

from ..lexicon import SageParent
from .cardinals import Cardinal, cardinal
from .functors import CatObject
from .underlying_sets import ViaUnderlyingSet

if TYPE_CHECKING:
    # Sage's abstract_method ships untyped; for type-checking use
    # abc.abstractmethod. Runtime uses Sage's.
    from abc import abstractmethod as abstract_method
else:
    from sage.misc.abstract_method import abstract_method


class GSets(CatObject, Category):
    r"""The owned category of ``G``-sets: sets with a ``G``-action, the
    structured forwarding root on the action side."""

    def __init__(self, group: SageParent) -> None:
        self._group = group
        Category.__init__(self)

    def _repr_object_names(self) -> str:
        return f"{self._group} sets"

    def super_categories(self) -> list[Category]:
        return [SageGSets(self._group)]

    def acting_group(self) -> SageParent:
        return self._group

    ParentMethods = ViaUnderlyingSet


def torsor_enumeration(torsor: Any) -> Iterator[object]:
    r"""Enumeration through the trivializing choice: acting the group
    through one chosen point is exhaustive (transitivity) and
    duplicate-free (freeness). The typed operation both the ``Torsors``
    node and torsor-structured specialized parents route through."""
    chosen = torsor.an_element()
    return (torsor.act(group_element, chosen) for group_element in torsor.acting_group())


def torsor_cardinality(torsor: Any) -> Cardinal:
    r"""``|T| = |G|``: the trivialization is a bijection."""
    return cardinal(torsor.acting_group().order())


def torsor_transporter(torsor: Any, source: object, target: object) -> object:
    r"""The unique ``g`` with ``g . source == target`` — existence by
    transitivity, uniqueness by freeness. Terminates for finite acting
    groups; no termination promise otherwise."""
    for group_element in torsor.acting_group():
        if torsor.act(group_element, source) == target:
            return group_element
    assert False, f"no group element moves {source} to {target}: the action is not transitive, so this parent is not a torsor"


class Torsors(CatObject, Category):
    r"""``G``-torsors: free transitive ``G``-sets."""

    def __init__(self, group: SageParent) -> None:
        self._group = group
        Category.__init__(self)

    def _repr_object_names(self) -> str:
        return f"{self._group} torsors"

    def super_categories(self) -> list[Category]:
        return [GSets(self._group)]

    def acting_group(self) -> SageParent:
        return self._group

    class ParentMethods:
        @abstract_method
        def an_element(self) -> object:
            r"""A CHOSEN point of the torsor — the trivializing choice; a
            torsor has no canonical one."""

        @abstract_method
        def act(self, group_element: object, element: object) -> object:
            r"""The action of ``g`` on a point."""

        def acting_group(self) -> Any:
            r"""The acting group, read off the torsor's category node."""
            parent = cast("SageParent", self)
            for node in parent.category().all_super_categories():
                if isinstance(node, Torsors):
                    return node.acting_group()
            assert False, f"{parent} is not in any Torsors(G) category"

        def __iter__(self) -> Iterator[object]:
            return torsor_enumeration(self)

        def cardinality(self) -> Cardinal:
            return torsor_cardinality(self)

        def transporter(self, source: object, target: object) -> object:
            r"""The unique ``g`` with ``g . source == target``."""
            return torsor_transporter(self, source, target)
