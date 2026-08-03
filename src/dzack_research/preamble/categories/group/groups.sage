r"""Owned categories of groups."""

from typing import Any

from sage.categories.category import Category
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.cpython.type import can_assign_class
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.abelian_gps.abelian_group_element import AbelianGroupElement
from sage.misc.latex import latex


class OwnedAbelianGroupElement(AbelianGroupElement):
    r"""An element of an abelian group owned by the preamble."""


class OwnedAbelianGroup(AbelianGroup_class):
    r"""An abelian group in :class:`OwnedGroups`.

    The owned parent type for the abelian groups this preamble reports -- the
    invariant-factor form of a torsion module's underlying group.  It adds
    nothing to Sage's class; the behaviour is the category's.  The subcategories
    of groups inherit it rather than falling back to a bare Sage group.
    """

    Element = OwnedAbelianGroupElement


def own_group_types(group: Any) -> Any:
    r"""Claim the owned parent and element types before refine reads them."""
    if isinstance(group, OwnedAbelianGroup) or not isinstance(group, AbelianGroup_class):
        return group
    assert can_assign_class(group), f"cannot own the type of {type(group).__name__}"
    group.__class__ = OwnedAbelianGroup
    group.Element = OwnedAbelianGroupElement
    # Sage caches ``element_class`` on the instance at construction; refine only
    # rebuilds it for categories that carry ``ElementMethods``, and this one has
    # none, so the cache is dropped here and Sage rebuilds it from ``Element``.
    group.__dict__.pop("element_class", None)
    group.__dict__.pop("_abstract_element_class", None)
    return group


class OwnedGroups(Category):
    r"""Groups whose notebook-facing methods are owned by the preamble."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "groups"

    def super_categories(self) -> list:
        return [SageGroups()]

    class ParentMethods:
        def group_generators(self) -> tuple[Any, ...]:
            """Return the generating set as `group_generators`."""
            return tuple(SageGroups().ParentMethods.group_generators(self))

        def _latex_(self: Any) -> str:
            r"""Return the group displayed by its distinguished group_generators."""
            group_generators = self.group_generators()
            if not group_generators:
                return r"\{1\}"
            entries = ", ".join(str(latex(generator)) for generator in group_generators)
            return rf"\left\langle {entries} \right\rangle"


class OwnedFiniteGroups(Category):
    r"""Finite groups whose notebook-facing methods are owned by the preamble."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finite groups"

    def super_categories(self) -> list:
        return [OwnedGroups(), SageFiniteGroups()]
