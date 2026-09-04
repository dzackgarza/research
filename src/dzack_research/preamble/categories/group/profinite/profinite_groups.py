"""Profinite groups."""

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

from dzack_research.preamble.categories.group.groups import TopologicalGroups


class ProfiniteGroups(Category_singleton):
    def super_categories(self):
        return [TopologicalGroups()]

    class ParentMethods:
        def is_profinite(self):
            return True

        @abstract_method(optional=True)
        def topological_group_generators(self):
            pass
