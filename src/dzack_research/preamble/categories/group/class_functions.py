r"""Class functions on finite owned groups."""

from sage.categories.morphism import SetMorphism

from dzack_research.preamble.categories.group.groups import _conjugacy_class_elements
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class FiniteGroupClassFunction(SetMorphism):
    r"""A class function ``G -> A`` stored on chosen conjugacy representatives.

    A class function is constant on conjugacy classes, so it is determined by
    its values on one representative of each class; the table on all of
    ``G`` is expanded once, class by class.
    """

    def __init__(self, group, codomain, representatives, values) -> None:
        self._representatives = representatives
        supplied = tuple(values)
        if len(supplied) != int(representatives.cardinality()):
            raise ValueError(
                "a finite-group class function needs one value per conjugacy representative"
            )
        values_by_position = {
            position: codomain(value) for position, value in enumerate(supplied)
        }
        self._values = finite_indexed_family(
            representatives,
            lambda representative: values_by_position[
                representatives.ranking_map()(representative)
            ],
            name="Class-function values",
        )
        self._value_table = {
            element: self._values[representative]
            for representative in representatives
            for element in _conjugacy_class_elements(group, representative)
        }
        SetMorphism.__init__(
            self,
            Sets().Mor(group, codomain),
            self._value_at,
        )

    def _value_at(self, element):
        group = self.domain()
        element = element if element in group else group(element)
        if element not in self._value_table:
            raise ValueError(
                f"{element} lies outside the conjugacy classes on which this class function is defined"
            )
        return self._value_table[element]

    def conjugacy_class_representatives(self):
        return self._representatives

    def degree(self):
        r"""The value at the identity: for a character, the dimension of its representation."""
        return self(self.domain().one())

    def values(self):
        return self._values

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return int(self._values.cardinality())

    def __getitem__(self, index):
        return self._values[index]

    def _repr_(self):
        return f"Class function {self.domain()} -> {self.codomain()}"


def _finite_group_class_function(group, codomain, values, *, representatives=None):
    r"""The class function on ``group`` with ``values`` on the chosen representatives.

    Representatives default to the group's own; a literal family of them is
    read as a finite ordered set.
    """
    if representatives is None:
        representatives = group.conjugacy_classes_representatives()
    if representatives not in FiniteOrderedSets():
        representatives = finite_ordered_set(tuple(representatives))
    return FiniteGroupClassFunction(group, codomain, representatives, values)


__all__ = ["FiniteGroupClassFunction"]
