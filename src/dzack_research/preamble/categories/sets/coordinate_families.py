"""Finite coordinate presentations built from owned indexed families."""

from collections.abc import Callable, Iterable

from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _finite_framing(module: Parent) -> Parent:
    r"""Return a selected module framing after asserting that it is finite."""

    labels = module.module_generating_set()
    if not cardinal(labels.cardinality()).is_finite():
        raise TypeError("a coordinate presentation requires a finite module framing")
    return labels


def _coordinate_index_set(left_labels: Parent, right_labels: Parent) -> Parent:
    r"""Return the dependent two-factor index set for a rectangular family."""

    return Sets().product(indexed_family(Sets.Δ[1], lambda index: left_labels if int(index) == 0 else right_labels))


def _coerce_family_value[CoordinateValueInputT](
    value_module: Parent,
    value: CoordinateValueInputT,
) -> Element:
    return (
        value
        if getattr(value, "parent", lambda: None)() is value_module
        else value_module(value)
    )


def _coordinate_family[CoordinateValueInputT](
    left_labels: Parent,
    right_labels: Parent,
    value_module: Parent,
    datum: IndexedFamily | Iterable[Iterable[CoordinateValueInputT]],
    *,
    name: str,
) -> IndexedFamily:
    r"""Parse finite rectangular data as a family indexed by ``left × right``."""
    indices = _coordinate_index_set(left_labels, right_labels)
    if isinstance(datum, IndexedFamily):
        source_indices = datum.index_set()

        def transported(pair: Element) -> Element:
            source_pair = source_indices(lambda index: pair.component(index))
            return _coerce_family_value(value_module, datum[source_pair])

        return indexed_family(indices, transported, name=name)

    left_size = int(left_labels.cardinality())
    right_size = int(right_labels.cardinality())
    rows = iter(datum)
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
            entries[left_position, right_position] = _coerce_family_value(
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
            int(left_labels.ranking_map()(pair.component(0))),
            int(right_labels.ranking_map()(pair.component(1))),
        ],
        name=name,
    )


def _coordinate_pair[LeftLabelT, RightLabelT](
    values: IndexedFamily,
    left_label: LeftLabelT,
    right_label: RightLabelT,
) -> Element:
    indices = values.index_set()
    return values[
        indices(lambda index: left_label if int(index) == 0 else right_label)
    ]


def _coordinate_family_from_function[LeftLabelT, RightLabelT, CoordinateValueInputT](
    left_labels: Parent,
    right_labels: Parent,
    value_module: Parent,
    function: Callable[[LeftLabelT, RightLabelT], CoordinateValueInputT],
    *,
    name: str,
) -> IndexedFamily:
    indices = _coordinate_index_set(left_labels, right_labels)
    return indexed_family(
        indices,
        lambda pair: _coerce_family_value(
            value_module,
            function(pair.component(0), pair.component(1)),
        ),
        name=name,
    )
