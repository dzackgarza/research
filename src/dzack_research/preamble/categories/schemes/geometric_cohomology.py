r"""Geometric cochain complexes and comparison-owned cohomology constructions."""

from sage.categories.category import Category
from sage.groups.free_group import FreeGroup
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups, _own_group
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplex,
    CochainComplexes,
    Cohomology,
    cochain_homset,
)
from dzack_research.preamble.categories.functors.cohomology import cohomology_functor
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearForm,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _own_ring,
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

        def cohomology_weight_projection(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            if weight not in self.cohomology_weight_support():
                raise ValueError("this weight has zero cohomology in the selected degree")
            return self.projection(weight)


class ToricIntegralSingularCohomologyGroups(OwnedCategoryOverBaseRing):
    r"""Integral singular cohomology of a specified smooth complete toric complex realization."""

    @classmethod
    def _repr_object_names(cls):
        return "integral singular cohomology groups of smooth complete toric varieties"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyPresentedModules,
        )

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def topological_scheme(self):
            return self._preamble_topological_scheme

        def cohomological_degree(self):
            return self._preamble_topological_cohomological_degree

        def cohomology_coefficients(self):
            return self.base_ring()

        def cohomology_topology(self):
            return "singular cohomology of the complex analytic realization"


class ToricFundamentalGroups(Category):
    r"""Pointed fundamental groups of supported toric complex realizations."""

    @classmethod
    def _repr_object_names(cls):
        return "fundamental groups of supported toric complex realizations"

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def topological_scheme(self):
            return self._preamble_topological_scheme

        def base_point_cone(self):
            r"""Return the maximal cone indexing the selected torus-fixed basepoint."""
            return self._preamble_topological_base_point_cone

        def realization_description(self):
            return "complex analytic realization under the selected QQ-to-CC embedding"


class ToricHodgeData(SageObject):
    r"""Pure Hodge numbers tied to the live integral cohomology of one toric realization."""

    def __init__(self, scheme) -> None:
        _require_smooth_complete_rational_toric_realization(scheme)
        self._scheme = scheme

    def scheme(self):
        return self._scheme

    def is_pure(self) -> bool:
        return True

    def integral_cohomology(self, degree):
        return self.scheme().integral_singular_cohomology(degree)

    def hodge_number(self, p, q):
        p = int(p)
        q = int(q)
        dimension = int(self.scheme().dimension())
        if p < 0 or q < 0 or p > dimension or q > dimension:
            return 0
        if p != q:
            return 0
        return int(self.integral_cohomology(2 * p).module_rank())

    def degree_hodge_numbers(self, degree):
        degree = int(degree)
        if degree < 0 or degree > 2 * int(self.scheme().dimension()):
            raise ValueError("Hodge degree lies between zero and twice the complex dimension")
        return tuple(
            (p, degree - p, self.hodge_number(p, degree - p))
            for p in range(degree + 1)
            if 0 <= degree - p <= int(self.scheme().dimension())
        )

    def _repr_(self):
        return f"Pure toric Hodge data of {self.scheme()}"


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


def _toric_weight_simplicial_complex(scheme, divisor, weight):
    r"""Private Sage adapter for the simplicial support ``V_{D,m}``.

    Sage's maintained toric-divisor implementation owns the combinatorial
    selection of the negative-cone subcomplex.  The private helper is confined
    here because the public cohomology operation returns only the resulting
    vector space and does not expose the augmented incidence maps needed by the
    owned cochain complex.
    """
    engine_divisor = scheme._engine_toric_divisor(divisor)
    return engine_divisor._sheaf_complex(
        _engine_vector(scheme.character_lattice(), weight)
    )


def _toric_weight_support_hull(scheme, divisor):
    r"""Private Sage adapter for the finite weight-support hull of ``O_X(D)``."""
    return scheme._engine_toric_divisor(divisor)._sheaf_cohomology_support()


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
    simplicial = _toric_weight_simplicial_complex(scheme, divisor, weight)

    if int(simplicial.dimension()) == -1:
        degree_zero = BasedFreeModule(base, 1)
        degree_one = BasedFreeModule(base, 0)
        complex_ = CochainComplex(
            base,
            {0: degree_zero, 1: degree_one},
            {0: module_homset(degree_zero, degree_one)({0: degree_one.zero()})},
            name="Toric weight cohomology complex",
            extra_categories=(ToricWeightCohomologyComplexes(base),),
            extra_construction_data={
                "geometric_cohomology_scheme": scheme,
                "geometric_cohomology_divisor": divisor,
                "geometric_cohomology_weight": weight,
            },
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
            extra_categories=(ToricWeightCohomologyComplexes(base),),
            extra_construction_data={
                "geometric_cohomology_scheme": scheme,
                "geometric_cohomology_divisor": divisor,
                "geometric_cohomology_weight": weight,
            },
        )
    return complex_


def ToricWeightCohomology(scheme, divisor, weight, degree):
    r"""Return the owned weight piece ``H^degree(X,O_X(D))_weight`` from its complex."""
    return Cohomology(
        ToricWeightCohomologyComplex(scheme, divisor, weight),
        int(degree),
    )


def ToricWeightScalarCochainMap(scheme, divisor, weight, scalar):
    r"""Return multiplication by ``scalar`` on the selected toric weight complex.

    This is the cochain map induced by the scalar endomorphism of the line
    bundle ``O_X(D)``.  It is represented on the actual complex computing the
    chosen character weight, so the induced cohomology map is obtained by the
    shared cohomology functor rather than by scalar multiplication on a
    separately recomputed vector space.
    """
    complex_ = ToricWeightCohomologyComplex(scheme, divisor, weight)
    scalar = complex_.base_ring()(scalar)
    return scalar * cochain_homset(complex_, complex_).identity()


def ToricWeightScalarCohomologyMap(scheme, divisor, weight, degree, scalar):
    r"""Return the map on one weight cohomology induced by scalar multiplication."""
    cochain_map = ToricWeightScalarCochainMap(
        scheme,
        divisor,
        weight,
        scalar,
    )
    return cohomology_functor(scheme.scheme_base_ring(), int(degree))(cochain_map)


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

    support_hull = _toric_weight_support_hull(scheme, divisor)
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
    construction_data = {
        "cohomology_scheme": scheme,
        "cohomology_divisor": divisor,
        "cohomological_degree": degree,
        "cohomology_weight_support": weights,
        "cohomology_weight_pieces": pieces,
    }
    if weights.cardinality() == 0:
        total = FreshFreeModuleOn(
            base,
            finite_ordered_set(()),
            _extra_categories=(ToricGeometricLineBundleCohomologySpaces(base),),
            _extra_construction_data=construction_data,
        )
    else:
        total = Modules(base).biproduct(
            finite_indexed_family(
                weights,
                lambda weight: pieces[weight],
                name="Nonzero toric cohomology weight pieces",
            ),
            extra_categories=(ToricGeometricLineBundleCohomologySpaces(base),),
            extra_construction_data=construction_data,
        )
    return total


def _require_smooth_complete_rational_toric_realization(scheme):
    if _engine_ring(scheme.scheme_base_ring()) is not SageQQ:
        raise NotImplementedError(
            "the selected integral singular-cohomology comparison currently uses the specified QQ-to-CC realization"
        )
    if not scheme.fan().is_smooth() or not scheme.fan().is_complete():
        raise ValueError(
            "the Jurkiewicz-Danilov integral comparison requires a smooth complete toric variety"
        )


def ToricIntegralSingularCohomology(scheme, degree):
    r"""Return ``H^degree(X(CC),ZZ)`` through the integral toric cycle comparison.

    For a smooth complete complex toric variety, Danilov--Jurkiewicz identifies
    the integral Chow ring with integral singular cohomology, with invariant
    divisor classes in Chow codimension ``k`` mapping to degree ``2k``.
    Odd cohomology vanishes and the even groups are torsion-free.
    """
    _require_smooth_complete_rational_toric_realization(scheme)
    degree = int(degree)
    dimension = int(scheme.dimension())
    if degree < 0 or degree > 2 * dimension:
        raise ValueError("singular cohomological degree lies between zero and twice the complex dimension")
    integers = _own_ring(SageZZ)
    construction_data = (
        ("_preamble_topological_scheme", scheme),
        ("_preamble_topological_cohomological_degree", degree),
    )
    if degree % 2:
        return FreshFreeModuleOn(
            integers,
            finite_ordered_set(()),
            _extra_categories=(ToricIntegralSingularCohomologyGroups(integers),),
            _extra_construction_data=construction_data,
        )

    codimension = degree // 2
    chow = scheme.chow_group(dimension - codimension)
    return chow._same_presentation_module(
        chow.module_generating_set(),
        _extra_categories=(ToricIntegralSingularCohomologyGroups(integers),),
        _extra_construction_data=construction_data,
    )


def ToricCycleClassIsomorphism(scheme, codimension):
    r"""Return ``CH^k(X) -> H^(2k)(X(CC),ZZ)`` for smooth complete toric ``X/QQ``."""
    _require_smooth_complete_rational_toric_realization(scheme)
    codimension = int(codimension)
    dimension = int(scheme.dimension())
    if codimension < 0 or codimension > dimension:
        raise ValueError("cycle codimension lies between zero and the scheme dimension")
    chow = scheme.chow_group(dimension - codimension)
    cohomology = scheme.integral_singular_cohomology(2 * codimension)
    forward = module_homset(chow, cohomology)(
        {
            label: cohomology.module_generator(label)
            for label in chow.module_generating_set()
        }
    )
    inverse = module_homset(cohomology, chow)(
        {
            label: chow.module_generator(label)
            for label in cohomology.module_generating_set()
        }
    )
    return Isomorphism(forward, inverse)


def ToricPicardToChowIsomorphism(scheme):
    r"""Return ``Pic(X) -> CH^1(X)`` for a smooth complete toric surface."""
    _require_smooth_complete_rational_toric_realization(scheme)
    if int(scheme.dimension()) != 2:
        raise ValueError("the represented Picard-to-Chow comparison is currently used on surfaces")
    picard = scheme.picard_group()
    chow = scheme.chow_group(1)
    cycles = scheme.torus_invariant_cycle_group(1)
    cycle_projection = scheme.torus_invariant_cycle_class_map(1)
    forward = module_homset(picard, chow)(
        {
            label: cycle_projection(cycles.module_generator(label))
            for label in picard.module_generating_set()
        }
    )
    return Isomorphism(forward, forward.inverse())


def ToricMiddleCohomologyForm(scheme):
    r"""Return ``H^2(X(CC),ZZ)`` with its cup-product intersection form."""
    _require_smooth_complete_rational_toric_realization(scheme)
    if int(scheme.dimension()) != 2:
        raise ValueError("the represented middle-cohomology form is for surfaces")
    cohomology = scheme.integral_singular_cohomology(2)
    cycle_class = scheme.cycle_class_isomorphism(1)
    picard_to_chow = ToricPicardToChowIsomorphism(scheme)
    cohomology_to_picard = picard_to_chow.inverse() * cycle_class.inverse()
    intersection = scheme.picard_intersection_pairing()
    integers = _own_ring(SageZZ)
    return BilinearForm(
        cohomology,
        integers,
        lambda left, right: intersection(
            cohomology_to_picard(left),
            cohomology_to_picard(right),
        ),
    )


def ToricFundamentalGroup(scheme, base_point_cone=None):
    r"""Return the pointed ``pi_1`` of a smooth complete toric complex realization.

    For a normal toric variety ``X_Sigma``, the fundamental group is the
    quotient of ``N`` by the sublattice generated by ``|Sigma| cap N``.  A
    complete fan has full support, hence that quotient is trivial.  A maximal
    cone is retained as the selected torus-fixed basepoint.
    """
    _require_smooth_complete_rational_toric_realization(scheme)
    maximal = scheme.fan().maximal_cones()
    if base_point_cone is None:
        base_point_cone = next(iter(maximal))
    if base_point_cone not in maximal:
        raise ValueError("the selected torus-fixed basepoint is indexed by a maximal cone")
    group = _own_group(FreeGroup(0))
    group._preamble_topological_scheme = scheme
    group._preamble_topological_base_point_cone = base_point_cone
    return refine(group, ToricFundamentalGroups())


def ToricHodgeStructure(scheme):
    r"""Return the pure diagonal Hodge data of a smooth complete toric complex realization."""
    return ToricHodgeData(scheme)


__all__ = [
    "ToricCycleClassIsomorphism",
    "ToricGeometricLineBundleCohomologySpaces",
    "ToricIntegralSingularCohomology",
    "ToricIntegralSingularCohomologyGroups",
    "ToricLineBundleCohomology",
    "ToricMiddleCohomologyForm",
    "ToricPicardToChowIsomorphism",
    "ToricFundamentalGroup",
    "ToricFundamentalGroups",
    "ToricHodgeData",
    "ToricHodgeStructure",
    "ToricWeightCohomology",
    "ToricWeightCohomologyComplex",
    "ToricWeightCohomologyComplexes",
    "ToricWeightScalarCochainMap",
    "ToricWeightScalarCohomologyMap",
]
