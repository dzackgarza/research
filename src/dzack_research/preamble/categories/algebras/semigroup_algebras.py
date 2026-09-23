r"""Affine semigroup algebras from finite lattice-generator presentations."""

from sage.matrix.constructor import matrix as _engine_matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.toric.ideal import ToricIdeal as _SageToricIdeal

from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    Algebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets


class _AffineSemigroupPresentation:
    r"""The selected lattice-generator presentation defining an affine semigroup algebra."""

    def __init__(self, generator_coordinates) -> None:
        self._generator_coordinates = generator_coordinates

    def _raw_generator_coordinates(self):
        return self._generator_coordinates


class AffineSemigroupAlgebras(OwnedCategoryOverBaseRing):
    r"""Affine semigroup algebras with one selected finite lattice presentation."""

    def an_object(self):
        r"""The polynomial algebra ``R[t] = R[NN]``."""
        return self(((1,),), names=("t",))

    def super_categories(self):
        return [AlgebrasWithChosenFinitePresentation(self.base_ring()).Commutative()]

    @classmethod
    def _repr_object_names(cls):
        return "affine semigroup algebras"

    class ParentMethods:
        def affine_semigroup_generator_coordinates(self):
            r"""Return the selected lattice-generator coordinates as an owned family."""
            raw = self._affine_semigroup_presentation._raw_generator_coordinates()
            labels = self.algebra_generating_set()
            coordinate_indices = Sets.Δ[len(raw[0]) - 1]
            integers = _own_ring(SageZZ)
            return finite_indexed_family(
                labels,
                lambda label: finite_indexed_family(
                    coordinate_indices,
                    lambda coordinate: integers(
                        raw[int(labels.ranking_map()(label))][int(coordinate)]
                    ),
                    name=f"Coordinates of affine semigroup generator {label}",
                ),
                name="Affine semigroup generator coordinates",
            )

    def _call_(
        self,
        generator_coordinates,
        *,
        names=None,
        extra_categories=(),
        extra_construction_data=(),
    ):
        coordinates = tuple(
            tuple(int(entry) for entry in row)
            for row in generator_coordinates
        )
        if not coordinates:
            raise ValueError("an affine semigroup presentation requires at least one generator")
        ambient_rank = len(coordinates[0])
        if any(len(row) != ambient_rank for row in coordinates):
            raise ValueError("affine semigroup generators must lie in one lattice")
        if names is None:
            names = tuple(f"s{position}" for position in range(len(coordinates)))
        else:
            names = tuple(names)
        if len(names) != len(coordinates):
            raise ValueError("an affine semigroup presentation needs one variable per generator")

        base = self.base_ring()
        presentation = base.polynomial_ring(names)
        engine_presentation = _engine_ring(presentation)
        columns = _engine_matrix(SageZZ, coordinates).transpose()
        engine_ideal = _SageToricIdeal(
            columns,
            names=names,
            base_ring=_engine_ring(base),
        )
        relations = tuple(
            _owned_engine_element(presentation, engine_presentation(relation))
            for relation in engine_ideal.gens()
        )
        construction_data = (
            ("_affine_semigroup_presentation", _AffineSemigroupPresentation(coordinates)),
            *tuple(extra_construction_data),
        )
        return (presentation).quotient_by_relations(relations,
            _extra_categories=(self, *tuple(extra_categories)),
            _extra_construction_data=construction_data,
        )


__all__ = ["AffineSemigroupAlgebras"]
