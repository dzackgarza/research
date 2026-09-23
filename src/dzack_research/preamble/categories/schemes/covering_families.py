r"""Scheme-facing ingress for finite covering families of locally ringed spaces.

The mathematical object is owned by :class:`CoveringFamilies`.  This module
only translates the convenient chart/embedding/overlap input used by locally
ringed spaces into arrows of the slice over the covered space.  It deliberately
defines no second covering-family, overlap, or refinement record.
"""

from collections.abc import Mapping
from itertools import combinations

from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.presheaves import (
    CoveringFamilies,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)


def _family(values, *, index_set=None, name):
    r"""Read finite chart data without changing its supplied labels."""

    match values:
        case IndexedFamily():
            if values.cardinality().is_finite() is not True:
                raise TypeError(f"{name} is a finite family")
            match index_set:
                case None:
                    return values
                case _:
                    entries = {index: values[index] for index in index_set}
        case Mapping():
            match index_set:
                case None:
                    index_set = finite_ordered_set(tuple(values))
                case _:
                    pass
            if set(values) != set(index_set):
                raise ValueError(f"{name} has exactly the covering-family index set")
            entries = dict(values)
        case _:
            sequence = tuple(values)
            match index_set:
                case None:
                    index_set = finite_ordered_set(range(len(sequence)))
                case _:
                    pass
            if len(sequence) != int(index_set.cardinality().finite_value()):
                raise ValueError(f"{name} has the wrong number of entries")
            entries = {
                index: sequence[position]
                for position, index in enumerate(index_set)
            }
    return finite_indexed_family(index_set, entries.__getitem__, name=name)


def _ringed_covering_family(
    ambient_space,
    site_category,
    charts,
    embeddings,
    overlaps,
    *,
    ambient_chart_index,
):
    r"""Build a certified cover as a covering family in ``LRS/X``.

    The presently represented certificate is the deliberately small exact one
    already used by the public ingress: one selected chart is literally ``X``
    and its embedding is ``id_X``.  Every chart and overlap is then placed in
    the slice before the family is built by :class:`CoveringFamilies`.
    """

    if site_category.base_object() is not ambient_space:
        raise ValueError("a ringed covering family is built in the slice over its ambient space")
    chart_family = _family(charts, name="Charts of a ringed covering family")
    embedding_family = _family(
        embeddings,
        index_set=chart_family.index_set(),
        name="Chart embeddings of a ringed covering family",
    )
    ambient_index = chart_family.index_set()(ambient_chart_index)
    for index in chart_family.index_set():
        embedding = embedding_family[index]
        if not isinstance(embedding, Morphism):
            raise TypeError("a represented ringed covering chart uses an actual morphism")
        if embedding.domain() is not chart_family[index] or embedding.codomain() is not ambient_space:
            raise ValueError("a covering chart embedding has the wrong endpoints")
    if chart_family[ambient_index] is not ambient_space:
        raise ValueError("the certified covering regime contains the ambient space as a chart")
    if embedding_family[ambient_index] != ambient_space.categorical_identity_morphism():
        raise ValueError("the ambient chart is embedded by the identity morphism")

    target = site_category.an_object()
    chart_objects = finite_indexed_family(
        chart_family.index_set(),
        lambda index: site_category.object(embedding_family[index]),
        name="Covering charts in the ambient slice",
    )
    members = finite_indexed_family(
        chart_family.index_set(),
        lambda index: site_category.Mor(chart_objects[index], target)(embedding_family[index]),
        name="Cover arrows in the ambient slice",
    )

    ranking = chart_family.index_set().ranking_map()
    expected_pairs = tuple(combinations(tuple(chart_family.index_set()), 2))
    normalized = {}
    for raw_pair, datum in dict(overlaps).items():
        left, right = raw_pair
        left = chart_family.index_set()(left)
        right = chart_family.index_set()(right)
        match ranking(left) < ranking(right):
            case True:
                normalized[left, right] = datum
            case False:
                normalized[right, left] = (datum[0], datum[2], datum[1])
    if set(normalized) != set(expected_pairs):
        raise ValueError("a covering family retains one represented overlap for every chart pair")

    overlap_data = {}
    for left, right in expected_pairs:
        overlap_space, left_map, right_map = normalized[left, right]
        if not isinstance(left_map, Morphism) or not isinstance(right_map, Morphism):
            raise TypeError("represented ringed overlaps use actual morphisms")
        if left_map.domain() is not overlap_space or right_map.domain() is not overlap_space:
            raise ValueError("both overlap embeddings have the overlap as domain")
        if left_map.codomain() is not chart_family[left] or right_map.codomain() is not chart_family[right]:
            raise ValueError("an overlap embedding lands in the wrong covering chart")
        left_to_ambient = embedding_family[left] * left_map
        right_to_ambient = embedding_family[right] * right_map
        if left_to_ambient != right_to_ambient:
            raise ValueError("the two overlap embeddings define different maps to the ambient space")
        overlap_object = site_category.object(left_to_ambient)
        overlap_data[left, right] = (
            overlap_object,
            site_category.Mor(overlap_object, chart_objects[left])(left_map),
            site_category.Mor(overlap_object, chart_objects[right])(right_map),
        )

    return CoveringFamilies(site_category).family(target, members, overlap_data)


__all__ = []
