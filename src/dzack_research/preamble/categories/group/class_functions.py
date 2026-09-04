r"""Class functions on finite owned groups."""

from sage.categories.morphism import SetMorphism

from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


class FiniteGroupClassFunction(SetMorphism):
    r"""A class function ``G -> A`` stored on chosen conjugacy representatives."""

    def __init__(self, group, codomain, representatives, values) -> None:
        self._representatives = (
            finite_ordered_set(representatives)
            if isinstance(representatives, (tuple, list, range))
            else representatives
        )
        count = int(self._representatives.cardinality())
        value_iterator = iter(values)
        values_by_position = {}
        for position in range(count):
            try:
                values_by_position[position] = codomain(next(value_iterator))
            except StopIteration as error:
                raise ValueError(
                    "a finite-group class function needs one value per conjugacy representative"
                ) from error
        try:
            next(value_iterator)
        except StopIteration:
            pass
        else:
            raise ValueError(
                "a finite-group class function needs one value per conjugacy representative"
            )
        self._values = finite_indexed_family(
            self._representatives,
            lambda representative: values_by_position[
                self._representatives.rank(representative)
            ],
            name="Class-function values",
        )
        self._value_table = self._expand_conjugacy_table(group)
        SetMorphism.__init__(
            self,
            Sets().mor(group, codomain),
            self._value_at,
        )

    def _expand_conjugacy_table(self, group):
        from dzack_research.preamble.categories.group.groups import _engine_group

        engine = _engine_group(group)
        table = {}
        for representative in self._representatives:
            value = self._values[representative]
            backend_representative = group._to_engine(representative)
            for backend_element in engine.conjugacy_class(backend_representative):
                table[group._from_engine(backend_element)] = value
        return table

    def _value_at(self, element):
        group = self.domain()
        if element not in group:
            element = group(element)
        try:
            return self._value_table[element]
        except KeyError as error:
            raise ValueError(
                f"{element} lies outside the conjugacy classes on which this class function is defined"
            ) from error

    def conjugacy_class_representatives(self):
        return self._representatives

    def values(self):
        return self._values

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return int(self._values.cardinality())

    def __getitem__(self, index):
        return self._values.unrank(index)

    def _repr_(self):
        return f"Class function {self.domain()} -> {self.codomain()}"


def finite_group_class_function(group, codomain, values, *, representatives=None):
    if representatives is None:
        representatives = group.conjugacy_classes_representatives()
    return FiniteGroupClassFunction(group, codomain, representatives, values)


__all__ = ["FiniteGroupClassFunction", "finite_group_class_function"]
