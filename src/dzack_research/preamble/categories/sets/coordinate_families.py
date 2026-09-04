"""Finite coordinate presentations built from owned indexed families."""

from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import (
    CartesianProductOfFamily,
    Sets,
)


def finite_framing(module):
    r"""Return a selected module framing after asserting that it is finite."""

    labels = module.module_generating_set()
    if not cardinal(labels.cardinality()).is_finite():
        raise TypeError("a coordinate presentation requires a finite module framing")
    return labels


def coordinate_index_set(left_labels, right_labels):
    r"""Return the dependent two-factor index set for a rectangular family."""

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
    "coerce_family_value",
    "coordinate_family",
    "coordinate_family_from_function",
    "coordinate_index_set",
    "coordinate_pair",
    "finite_framing",
]
