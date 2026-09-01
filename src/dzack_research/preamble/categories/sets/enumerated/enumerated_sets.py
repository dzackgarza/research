"""Owned enumerated-set spine over Sage's enumerated-set categories."""

from sage.categories.category import Category
from sage.categories.enumerated_sets import EnumeratedSets as SageEnumeratedSets
from sage.categories.infinite_enumerated_sets import (
    InfiniteEnumeratedSets as SageInfiniteEnumeratedSets,
)


class EnumeratedSets(Category):
    r"""Sets equipped with a ranking, as Sage's :class:`EnumeratedSets`."""

    def super_categories(self):
        return [SageEnumeratedSets()]


class InfiniteEnumeratedSets(Category):
    r"""Countably infinite enumerated sets."""

    def super_categories(self):
        return [SageInfiniteEnumeratedSets(), EnumeratedSets()]
