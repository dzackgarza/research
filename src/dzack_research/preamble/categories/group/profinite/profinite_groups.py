"""Profinite groups."""

from sage.misc.abstract_method import abstract_method

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.groups import TopologicalGroups


class ProfiniteGroups(OwnedCategory):
    def an_object(self):
        r"""The procyclic absolute Galois group of ``GF(2)``."""
        from sage.rings.finite_rings.finite_field_constructor import GF as SageGF

        from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
            AbsoluteGaloisGroup,
        )
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return AbsoluteGaloisGroup(_own_ring(SageGF(2)))

    @classmethod
    def _repr_object_names(cls):
        return "profinite groups"

    def super_categories(self):
        return [TopologicalGroups()]

    class ParentMethods:
        def is_profinite(self):
            return True

        @abstract_method(optional=True)
        def topological_group_generators(self):
            pass
