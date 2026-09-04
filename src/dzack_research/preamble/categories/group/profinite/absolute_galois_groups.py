r"""Owned categories for absolute Galois groups."""

from sage.categories.category_singleton import Category_singleton
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.group.groups import OwnedAbelianGroups
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.sets.cardinals import continuum


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
        def is_finite(self) -> bool:
            return False

        def order(self):
            from sage.rings.infinity import Infinity

            return Infinity

        def cardinality(self):
            return continuum

        def is_abelian(self) -> bool:
            return True

        def is_finitely_generated(self) -> bool:
            return False

        def topological_group_generators(self):
            return (self.frobenius(),)


class OpenAbsoluteGaloisSubgroups(Category_singleton):
    r"""Open subgroups (G_E\subseteq G_K) carrying the embedding (E\to\bar K)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "open subgroups of absolute Galois groups"

    def super_categories(self):
        return [AbsoluteGaloisGroups()]

    class ParentMethods:
        def ambient(self):
            return self._ambient

        def supergroup(self):
            return self._ambient

        def fixed_field(self):
            return self._fixed_extension.field()

        def fixed_extension(self):
            return self._fixed_extension

        def embedding(self):
            return self._fixed_extension.embedding()

        def index(self):
            return self._fixed_extension.degree()

        def inclusion(self):
            return self._inclusion


def absolute_galois_group_category(field):
    from sage.categories.finite_fields import FiniteFields

    return (
        AbsoluteGaloisGroupsOfFiniteFields()
        if _engine_ring(field) in FiniteFields()
        else AbsoluteGaloisGroups()
    )


__all__ = [
    "AbsoluteGaloisGroups",
    "AbsoluteGaloisGroupsOfFiniteFields",
    "OpenAbsoluteGaloisSubgroups",
    "absolute_galois_group_category",
]
