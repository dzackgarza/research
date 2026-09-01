r"""Owned categories for absolute Galois groups."""

from sage.categories.category_singleton import Category_singleton
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.group.groups import OwnedAbelianGroups
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)


class AbsoluteGaloisGroups(Category_singleton):
    r"""Groups (G_K=\operatorname{Aut}_K(\bar K)) with a chosen base point."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "absolute Galois groups"

    def super_categories(self):
        return [ProfiniteGroups()]

    class ParentMethods:
        def characteristic(self):
            return self.base_field().characteristic()

        def is_profinite(self) -> bool:
            return True

        def is_abelian(self):
            return Unknown


class AbsoluteGaloisGroupsOfFiniteFields(Category_singleton):
    r"""The procyclic absolute Galois groups of finite fields."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "absolute Galois groups of finite fields"

    def super_categories(self):
        return [AbsoluteGaloisGroups(), OwnedAbelianGroups()]

    class ParentMethods:
        def is_abelian(self) -> bool:
            return True

        def is_finitely_generated(self) -> bool:
            return False

        def topological_group_generators(self):
            return (self.frobenius(),)


def absolute_galois_group_category(field):
    from sage.categories.finite_fields import FiniteFields
    from dzack_research.preamble.categories.rings.rings import engine_ring

    return (
        AbsoluteGaloisGroupsOfFiniteFields()
        if engine_ring(field) in FiniteFields()
        else AbsoluteGaloisGroups()
    )


def AbsoluteGaloisGroup(field, **kwargs):
    r"""Construct (\operatorname{Aut}_K(\bar K)) with exact realization data."""
    from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
        AbsoluteGaloisGroup as _AbsoluteGaloisGroup,
    )

    return _AbsoluteGaloisGroup(field, **kwargs)


absolute_galois_group = AbsoluteGaloisGroup


__all__ = [
    "AbsoluteGaloisGroup",
    "AbsoluteGaloisGroups",
    "AbsoluteGaloisGroupsOfFiniteFields",
    "absolute_galois_group",
    "absolute_galois_group_category",
]
