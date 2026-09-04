"""Owned indexed families of mathematical values."""

from sage.structure.sage_object import SageObject


class IndexedFamily(SageObject):
    r"""A family ``(x_i)_{i in I}`` retaining its indexing set.

    A family is not the set of its values: different indices may have equal
    values.  It therefore has no inverse ``rank(value)`` operation in general.
    Consumers iterate values lazily or address them through ``value(index)``.
    """

    def __init__(self, index_set, value, *, name=None) -> None:
        if not callable(value):
            raise TypeError("an indexed family requires a value map")
        self._index_set = index_set
        self._value_function = value
        self._value_cache = {}
        self._name = name

    def index_set(self):
        return self._index_set

    def cardinality(self):
        return self.index_set().cardinality()

    def value(self, index):
        normalized = self.index_set()(index)
        try:
            return self._value_cache[normalized]
        except (KeyError, TypeError):
            value = self._value_function(normalized)
            try:
                self._value_cache[normalized] = value
            except TypeError:
                pass
            return value

    __call__ = value

    def __getitem__(self, index):
        try:
            normalized = self.index_set()(index)
        except (TypeError, ValueError):
            return self.unrank(index)
        return self.value(normalized)

    def items(self):
        return ((index, self.value(index)) for index in self.index_set())

    def __iter__(self):
        return (self.value(index) for index in self.index_set())

    def unrank(self, position):
        try:
            index = self.index_set().unrank(int(position))
        except AttributeError:
            try:
                index = next(
                    index
                    for offset, index in enumerate(self.index_set())
                    if offset == int(position)
                )
            except StopIteration as error:
                raise IndexError(position) from error
        return self.value(index)

    def map(self, function, *, name=None):
        if not callable(function):
            raise TypeError("a family map must be callable")
        return IndexedFamily(
            self.index_set(),
            lambda index: function(self.value(index)),
            name=name,
        )

    def _repr_(self):
        return self._name or f"Family indexed by {self.index_set()}"


def indexed_family(index_set, value, *, name=None):
    r"""Return the family ``index |-> value(index)`` over ``index_set``."""
    return IndexedFamily(index_set, value, name=name)


finite_indexed_family = indexed_family


def finite_framing(module):
    r"""Return a selected module framing after asserting that it is finite."""
    from dzack_research.preamble.categories.sets.cardinals import cardinal

    labels = module.module_generating_set()
    if not cardinal(labels.cardinality()).is_finite():
        raise TypeError("a coordinate presentation requires a finite module framing")
    return labels


def coordinate_index_set(left_labels, right_labels):
    r"""Return the dependent two-factor index set for a rectangular family."""
    from dzack_research.preamble.categories.sets.set_categories import (
        CartesianProductOfFamily,
        Sets,
    )

    return CartesianProductOfFamily(
        Sets.Δ[1],
        lambda index: left_labels if int(index) == 0 else right_labels,
    )


def coerce_family_value(value_module, value):
    return (
        value
        if getattr(value, "parent", lambda: None)() is value_module
        else value_module(value)
    )


def coordinate_family(left_labels, right_labels, value_module, datum, *, name):
    r"""Parse finite rectangular data as a family indexed by ``left × right``."""
    indices = coordinate_index_set(left_labels, right_labels)
    if isinstance(datum, IndexedFamily):
        source_indices = datum.index_set()

        def transported(pair):
            source_pair = source_indices(lambda index: pair.component(index))
            return coerce_family_value(value_module, datum[source_pair])

        return indexed_family(indices, transported, name=name)

    left_size = int(left_labels.cardinality())
    right_size = int(right_labels.cardinality())
    rows = iter(datum.rows() if hasattr(datum, "rows") else datum)
    entries = {}
    for left_position in range(left_size):
        try:
            row = iter(next(rows))
        except StopIteration as error:
            raise ValueError(
                f"the coordinate presentation must have shape {left_size} x {right_size}"
            ) from error
        for right_position in range(right_size):
            try:
                entry = next(row)
            except StopIteration as error:
                raise ValueError(
                    f"the coordinate presentation must have shape {left_size} x {right_size}"
                ) from error
            entries[left_position, right_position] = coerce_family_value(
                value_module, entry
            )
        try:
            next(row)
        except StopIteration:
            pass
        else:
            raise ValueError(
                f"the coordinate presentation must have shape {left_size} x {right_size}"
            )
    try:
        next(rows)
    except StopIteration:
        pass
    else:
        raise ValueError(
            f"the coordinate presentation must have shape {left_size} x {right_size}"
        )

    return indexed_family(
        indices,
        lambda pair: entries[
            int(left_labels.rank(pair.component(0))),
            int(right_labels.rank(pair.component(1))),
        ],
        name=name,
    )


def coordinate_pair(values, left_label, right_label):
    indices = values.index_set()
    return values[
        indices(lambda index: left_label if int(index) == 0 else right_label)
    ]


def coordinate_family_from_function(
    left_labels,
    right_labels,
    value_module,
    function,
    *,
    name,
):
    indices = coordinate_index_set(left_labels, right_labels)
    return indexed_family(
        indices,
        lambda pair: coerce_family_value(
            value_module,
            function(pair.component(0), pair.component(1)),
        ),
        name=name,
    )


__all__ = [
    "IndexedFamily",
    "coerce_family_value",
    "coordinate_family",
    "coordinate_family_from_function",
    "coordinate_index_set",
    "coordinate_pair",
    "finite_framing",
    "finite_indexed_family",
    "indexed_family",
]
