r"""Affine semigroup algebras from finite lattice-generator presentations."""

from sage.matrix.constructor import matrix as _engine_matrix
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.toric.ideal import ToricIdeal as _SageToricIdeal

from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    Algebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
)


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

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Algebras(self.base_ring()).Associative().Unital().Commutative()
            and candidate in AlgebrasWithChosenFinitePresentation(self.base_ring())
            and hasattr(candidate, "_preamble_affine_semigroup_generator_coordinates")
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
            presentation._from_engine_element(engine_presentation(relation))
            for relation in engine_ideal.gens()
        )
        construction_data = (
            ("_preamble_affine_semigroup_generator_coordinates", coordinates),
            *tuple(extra_construction_data),
        )
        return (presentation).quotient_by_relations(relations,
            _extra_categories=tuple(extra_categories),
            _extra_construction_data=construction_data,
        )


__all__ = ["AffineSemigroupAlgebras"]
