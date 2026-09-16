r"""Covering families of represented locally ringed spaces.

This layer does not assign a coordinate ring to a non-affine chart or overlap.
It retains the spaces and the two embeddings of every overlap.  Affine
refinements of an overlap are separate objects whose charts map back to that
overlap, hence to both original covering charts.
"""

from collections.abc import Mapping

from sage.categories.morphism import Morphism
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasRefinement,
    _FiniteSchemeGluingDatum,
)
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)


def _family(values, *, index_set=None, name):
    if isinstance(values, IndexedFamily):
        if values.cardinality().is_finite() is not True:
            raise TypeError(f"{name} is a finite family")
        if index_set is None:
            return values
        entries = {index: values[index] for index in index_set}
    elif isinstance(values, Mapping):
        if index_set is None:
            index_set = finite_ordered_set(tuple(values))
        if set(values) != set(index_set):
            raise ValueError(f"{name} has exactly the covering-family index set")
        entries = dict(values)
    else:
        sequence = tuple(values)
        if index_set is None:
            index_set = finite_ordered_set(range(len(sequence)))
        if len(sequence) != int(index_set.cardinality().finite_value()):
            raise ValueError(f"{name} has the wrong number of entries")
        entries = {
            index: sequence[position]
            for position, index in enumerate(index_set)
        }
    return finite_indexed_family(
        index_set,
        lambda index: entries[index],
        name=name,
    )


class RingedCoveringOverlap(SageObject):
    r"""One represented overlap with its two embeddings into covering charts."""

    def __init__(self, family, left_index, right_index, space, left_map, right_map) -> None:
        self._family = family
        self._left_index = family.normalize_index(left_index)
        self._right_index = family.normalize_index(right_index)
        if self._left_index == self._right_index:
            raise ValueError("a covering overlap joins two distinct chart labels")
        self._space = space
        self._left_map = left_map
        self._right_map = right_map
        if not isinstance(left_map, Morphism) or not isinstance(right_map, Morphism):
            raise TypeError("represented ringed overlaps use actual morphisms")
        if left_map.domain() is not space or right_map.domain() is not space:
            raise ValueError("both overlap embeddings have the overlap as domain")
        if left_map.codomain() is not family.chart(self._left_index):
            raise ValueError("the left overlap embedding lands in the left chart")
        if right_map.codomain() is not family.chart(self._right_index):
            raise ValueError("the right overlap embedding lands in the right chart")
        left_to_ambient = family.embedding(self._left_index) * left_map
        right_to_ambient = family.embedding(self._right_index) * right_map
        if left_to_ambient != right_to_ambient:
            raise ValueError("the two overlap embeddings define different maps to the ambient space")

    def family(self):
        return self._family

    def ambient_space(self):
        return self.family().ambient_space()

    def left_index(self):
        return self._left_index

    def right_index(self):
        return self._right_index

    def space(self):
        return self._space

    def left_embedding(self):
        return self._left_map

    def right_embedding(self):
        return self._right_map

    def is_affine(self) -> bool:
        base = getattr(self.space(), "scheme_base_ring", lambda: None)()
        if base is None:
            return False
        return self.space() in Schemes(base).Affine()

    def affine_refinement(self):
        r"""Use the overlap's represented affine gluing as an affine refinement.

        A non-affine overlap such as the punctured plane may itself be a glued
        scheme.  Its gluing datum is the affine refinement; its comparison to
        the overlap is the identity because that datum owns this very scheme.
        """
        datum = getattr(self.space(), "gluing_datum", lambda: None)()
        if not isinstance(datum, _FiniteSchemeGluingDatum):
            raise TypeError(
                "this represented overlap has no finite affine gluing from which to build a refinement"
            )
        return AffineOverlapRefinement(
            self,
            datum,
            self.space().categorical_identity_morphism(),
        )

    def _repr_(self):
        return (
            f"Overlap of charts {self.left_index()} and {self.right_index()} "
            f"in {self.ambient_space()}"
        )


class RingedCoveringFamily(SageObject):
    r"""A finite represented covering family of one locally ringed space.

    The first supported cover-verification regime is deliberately exact: one
    selected chart is the ambient space itself and its embedding is the
    identity.  Thus the family covers without invoking point enumeration or a
    global coordinate ring.  Other coverage proofs belong to later topology
    owners rather than being accepted as booleans here.
    """

    def __init__(
        self,
        ambient_space,
        charts,
        embeddings,
        overlaps,
        *,
        ambient_chart_index,
    ) -> None:
        self._ambient_space = ambient_space
        self._charts = _family(charts, name="Charts of a ringed covering family")
        self._embeddings = _family(
            embeddings,
            index_set=self._charts.index_set(),
            name="Chart embeddings of a ringed covering family",
        )
        self._ambient_chart_index = self.normalize_index(ambient_chart_index)
        for index in self.index_set():
            embedding = self._embeddings[index]
            if not isinstance(embedding, Morphism):
                raise TypeError("a represented ringed covering chart uses an actual morphism")
            if embedding.domain() is not self.chart(index):
                raise ValueError("a covering chart embedding has the wrong domain")
            if embedding.codomain() is not ambient_space:
                raise ValueError("every covering chart embeds in the ambient space")
        ambient_chart = self.chart(self._ambient_chart_index)
        ambient_embedding = self.embedding(self._ambient_chart_index)
        if ambient_chart is not ambient_space:
            raise ValueError("the currently verified covering regime contains the ambient space as a chart")
        if ambient_embedding != ambient_space.categorical_identity_morphism():
            raise ValueError("the ambient chart is embedded by the identity morphism")

        self._overlaps = {}
        supplied = dict(overlaps)
        expected = {
            self._ordered_pair(left, right)
            for left_position, left in enumerate(tuple(self.index_set()))
            for right in tuple(self.index_set())[left_position + 1 :]
        }
        normalized = {}
        for pair, value in supplied.items():
            left, right = pair
            ordered = self._ordered_pair(left, right)
            if ordered == (self.normalize_index(left), self.normalize_index(right)):
                normalized[ordered] = value
            else:
                if not isinstance(value, (tuple, list)) or len(value) != 3:
                    raise TypeError(
                        "an overlap is supplied as (space, left embedding, right embedding)"
                    )
                normalized[ordered] = (value[0], value[2], value[1])
        if set(normalized) != expected:
            raise ValueError("a covering family retains one represented overlap for every chart pair")
        for pair, datum in normalized.items():
            if not isinstance(datum, (tuple, list)) or len(datum) != 3:
                raise TypeError("an overlap is supplied as (space, left embedding, right embedding)")
            self._overlaps[pair] = RingedCoveringOverlap(
                self,
                pair[0],
                pair[1],
                datum[0],
                datum[1],
                datum[2],
            )

    def ambient_space(self):
        return self._ambient_space

    def index_set(self):
        return self._charts.index_set()

    def normalize_index(self, index):
        return self.index_set()(index)

    def chart(self, index):
        return self._charts[self.normalize_index(index)]

    def embedding(self, index):
        return self._embeddings[self.normalize_index(index)]

    def ambient_chart_index(self):
        return self._ambient_chart_index

    def _ordered_pair(self, left_index, right_index):
        left = self.normalize_index(left_index)
        right = self.normalize_index(right_index)
        if left == right:
            raise ValueError("a covering overlap uses two distinct chart labels")
        ranking = self.index_set().ranking_map()
        if ranking(left) < ranking(right):
            return left, right
        return right, left

    def overlap(self, left_index, right_index):
        pair = self._ordered_pair(left_index, right_index)
        return self._overlaps[pair]

    def _repr_(self):
        return (
            f"Covering family of {self.ambient_space()} by "
            f"{self.index_set().cardinality()} represented charts"
        )


class AffineOverlapRefinement(SageObject):
    r"""An affine atlas refining one represented, possibly non-affine overlap."""

    def __init__(
        self,
        overlap,
        atlas_datum,
        comparison_to_overlap,
        *,
        coarse_refinement=None,
        atlas_refinement=None,
    ) -> None:
        if not isinstance(overlap, RingedCoveringOverlap):
            raise TypeError("an affine overlap refinement refines one represented covering overlap")
        if not isinstance(atlas_datum, _FiniteSchemeGluingDatum):
            raise TypeError("an affine overlap refinement is a finite affine gluing")
        if comparison_to_overlap.domain() is not atlas_datum.scheme():
            raise ValueError("the refinement comparison starts at the affine atlas scheme")
        if comparison_to_overlap.codomain() is not overlap.space():
            raise ValueError("the refinement comparison lands in the represented overlap")
        self._overlap = overlap
        self._atlas_datum = atlas_datum
        self._comparison_to_overlap = comparison_to_overlap
        self._coarse_refinement = coarse_refinement
        self._atlas_refinement = atlas_refinement

    def overlap(self):
        return self._overlap

    def atlas_datum(self):
        return self._atlas_datum

    def comparison_to_overlap(self):
        return self._comparison_to_overlap

    def chart_indices(self):
        return self.atlas_datum().chart_indices()

    def chart(self, index):
        return self.atlas_datum().chart(index)

    def chart_map_to_overlap(self, index):
        return self.comparison_to_overlap() * self.atlas_datum().chart_embedding(index)

    def left_embedding(self, index):
        return self.overlap().left_embedding() * self.chart_map_to_overlap(index)

    def right_embedding(self, index):
        return self.overlap().right_embedding() * self.chart_map_to_overlap(index)

    def refined_by(self, atlas_refinement):
        r"""Refine this affine atlas and retain the actual comparison morphism."""
        if not isinstance(atlas_refinement, FiniteAtlasRefinement):
            raise TypeError("an overlap atlas is refined by a finite-atlas refinement")
        if atlas_refinement.coarse_datum() is not self.atlas_datum():
            raise ValueError("the finite-atlas refinement starts at this overlap refinement")
        comparison = self.comparison_to_overlap() * atlas_refinement.comparison_morphism()
        return AffineOverlapRefinement(
            self.overlap(),
            atlas_refinement.fine_datum(),
            comparison,
            coarse_refinement=self,
            atlas_refinement=atlas_refinement,
        )

    def coarse_refinement(self):
        if self._coarse_refinement is None:
            raise TypeError("this is the initial affine refinement of the overlap")
        return self._coarse_refinement

    def atlas_refinement(self):
        if self._atlas_refinement is None:
            raise TypeError("this affine refinement was not obtained from a coarser one")
        return self._atlas_refinement

    def _repr_(self):
        return (
            f"Affine refinement of {self.overlap()} by "
            f"{self.atlas_datum().number_of_charts()} charts"
        )


__all__ = [
    "AffineOverlapRefinement",
    "RingedCoveringFamily",
    "RingedCoveringOverlap",
]
