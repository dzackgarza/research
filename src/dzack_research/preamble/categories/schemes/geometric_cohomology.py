r"""Geometric cochain complexes and comparison-owned cohomology constructions."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplex,
    CochainComplexes,
    Cohomology,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.schemes.toric.fans import (
    _engine_vector,
    _owned_vector,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.refine import refine


class ToricWeightCohomologyComplexes(OwnedCategoryOverBaseRing):
    r"""Shifted reduced simplicial complexes computing one toric sheaf-cohomology weight."""

    @classmethod
    def _repr_object_names(cls):
        return "toric weight cohomology complexes"

    def super_categories(self):
        return [CochainComplexes(self.base_ring())]

    class ParentMethods:
        def cohomology_scheme(self):
            return self._preamble_geometric_cohomology_scheme

        def cohomology_divisor(self):
            return self._preamble_geometric_cohomology_divisor

        def cohomology_weight(self):
            return self._preamble_geometric_cohomology_weight

        def comparison_description(self):
            return (
                "H^i(X,O_X(D))_m is identified with shifted reduced simplicial "
                "cohomology H~^(i-1)(V_{D,m})"
            )


class ToricGeometricLineBundleCohomologySpaces(OwnedCategoryOverBaseRing):
    r"""Total toric line-bundle cohomology assembled from its live weight complexes."""

    @classmethod
    def _repr_object_names(cls):
        return "geometric toric line-bundle cohomology spaces"

    def super_categories(self):
        from dzack_research.preamble.categories.divisors.cohomology import (
            LineBundleCohomologySpaces,
        )

        return [LineBundleCohomologySpaces(self.base_ring())]

    class ParentMethods:
        def cohomology_weight_support(self):
            return self._preamble_cohomology_weight_support

        def cohomology_weight_piece(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            return self._preamble_cohomology_weight_pieces[weight]

        def cohomology_weight_inclusion(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            if weight not in self.cohomology_weight_support():
                raise ValueError("this weight has zero cohomology in the selected degree")
            return self.injection(weight)


def _matrix_morphism(base, source, target, matrix):
    r"""Cross one engine incidence matrix into an owned module morphism."""
    source_labels = tuple(source.module_generating_set())
    target_labels = tuple(target.module_generating_set())
    if matrix.ncols() != len(source_labels) or matrix.nrows() != len(target_labels):
        raise ArithmeticError("the simplicial differential matrix has inconsistent endpoint ranks")

    def image(source_label):
        column = source_labels.index(source_label)
        return target.linear_combination(
            {
                target_label: base(int(matrix[row, column]))
                for row, target_label in enumerate(target_labels)
                if matrix[row, column]
            }
        )

    return module_homset(source, target)(image)


def ToricWeightCohomologyComplex(scheme, divisor, weight):
    r"""Return the finite complex computing ``H^*(X,O_X(D))_weight``.

    Sage's toric-divisor engine selects the simplicial complex ``V_{D,m}`` of
    negative cones.  We retain only that finite combinatorial output and cross
    its augmented cochain incidence matrices into owned free modules.  The
    grading is shifted by one so degree ``i`` computes
    ``H~^(i-1)(V_{D,m})``, the toric line-bundle weight cohomology.
    """
    base = scheme.scheme_base_ring()
    divisor = scheme.weil_divisor_group()(divisor)
    if not scheme.is_cartier(divisor):
        raise ValueError("the represented toric weight complex requires a Cartier divisor")
    weight = scheme.character_lattice()(weight)
    engine_divisor = scheme._engine_toric_divisor(divisor)
    simplicial = engine_divisor._sheaf_complex(
        _engine_vector(scheme.character_lattice(), weight)
    )

    if int(simplicial.dimension()) == -1:
        degree_zero = BasedFreeModule(base, 1)
        degree_one = BasedFreeModule(base, 0)
        complex_ = CochainComplex(
            base,
            {0: degree_zero, 1: degree_one},
            {0: module_homset(degree_zero, degree_one)({0: degree_one.zero()})},
            name="Toric weight cohomology complex",
        )
    else:
        engine = simplicial.chain_complex(
            augmented=True,
            base_ring=SageZZ,
            cochain=True,
        )
        top = int(simplicial.dimension())
        matrices = {q: engine.differential(q) for q in range(-1, top + 1)}
        pieces = {
            q + 1: BasedFreeModule(base, matrix.ncols())
            for q, matrix in matrices.items()
        }
        pieces[top + 2] = BasedFreeModule(base, 0)
        differentials = {
            q + 1: _matrix_morphism(base, pieces[q + 1], pieces[q + 2], matrix)
            for q, matrix in matrices.items()
        }
        complex_ = CochainComplex(
            base,
            pieces,
            differentials,
            name="Toric weight cohomology complex",
        )

    complex_._preamble_geometric_cohomology_scheme = scheme
    complex_._preamble_geometric_cohomology_divisor = divisor
    complex_._preamble_geometric_cohomology_weight = weight
    return refine(complex_, ToricWeightCohomologyComplexes(base))


def ToricWeightCohomology(scheme, divisor, weight, degree):
    r"""Return the owned weight piece ``H^degree(X,O_X(D))_weight`` from its complex."""
    return Cohomology(
        ToricWeightCohomologyComplex(scheme, divisor, weight),
        int(degree),
    )


def ToricLineBundleCohomology(scheme, divisor, degree):
    r"""Assemble ``H^degree(X,O_X(D))`` as the direct sum of its weight cohomologies."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    degree = int(degree)
    if degree < 0 or degree > int(scheme.dimension()):
        raise ValueError("cohomological degree lies outside the scheme dimension")
    if not scheme.fan().is_complete():
        raise ValueError("finite-dimensional toric line-bundle cohomology requires a complete fan")
    divisor = scheme.weil_divisor_group()(divisor)
    if not scheme.is_cartier(divisor):
        raise ValueError("the represented geometric cohomology requires a Cartier divisor")

    engine_divisor = scheme._engine_toric_divisor(divisor)
    support_hull = engine_divisor._sheaf_cohomology_support()
    characters = scheme.character_lattice()
    candidate_weights = tuple(
        _owned_vector(characters, point)
        for point in support_hull.integral_points()
    )
    pieces = {
        weight: ToricWeightCohomology(scheme, divisor, weight, degree)
        for weight in candidate_weights
    }
    pieces = {
        weight: piece
        for weight, piece in pieces.items()
        if int(piece.dimension()) != 0
    }
    weights = finite_ordered_set(tuple(pieces))
    base = scheme.scheme_base_ring()
    if weights.cardinality() == 0:
        total = BasedFreeModule(base, 0)
    else:
        total = Modules(base).biproduct(
            finite_indexed_family(
                weights,
                lambda weight: pieces[weight],
                name="Nonzero toric cohomology weight pieces",
            )
        )
    total._preamble_cohomology_scheme = scheme
    total._preamble_cohomology_divisor = divisor
    total._preamble_cohomological_degree = degree
    total._preamble_cohomology_weight_support = weights
    total._preamble_cohomology_weight_pieces = pieces
    return refine(total, ToricGeometricLineBundleCohomologySpaces(base))


__all__ = [
    "ToricGeometricLineBundleCohomologySpaces",
    "ToricLineBundleCohomology",
    "ToricWeightCohomology",
    "ToricWeightCohomologyComplex",
    "ToricWeightCohomologyComplexes",
]
