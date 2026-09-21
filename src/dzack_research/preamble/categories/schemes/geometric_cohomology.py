r"""Geometric cochain complexes and comparison-owned cohomology constructions."""

from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
)
from dzack_research.preamble.categories.group.cyclic_subgroups import (
    CyclicGroups,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplexes,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.toric.fans import (
    _engine_vector,
    _owned_vector,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    Sets,
)


class _ToricWeightCohomologyConstruction:
    r"""The toric scheme, divisor, and character defining one weight complex."""

    def __init__(self, scheme, divisor, weight) -> None:
        self._scheme = scheme
        self._divisor = divisor
        self._weight = weight

    def scheme(self):
        return self._scheme

    def divisor(self):
        return self._divisor

    def weight(self):
        return self._weight


class ToricWeightCohomologyComplexes(OwnedCategoryOverBaseRing):
    r"""Shifted reduced simplicial complexes computing one toric sheaf-cohomology weight."""

    @classmethod
    def _repr_object_names(cls):
        return "toric weight cohomology complexes"

    def super_categories(self):
        return [CochainComplexes(self.base_ring())]

    class ParentMethods:
        def __init__(self, toric_weight_cohomology_construction, **rest) -> None:
            self._toric_weight_cohomology_construction = toric_weight_cohomology_construction
            super().__init__(**rest)

        def toric_weight_cohomology_construction(self):
            return self._toric_weight_cohomology_construction

        def cohomology_scheme(self):
            return self.toric_weight_cohomology_construction().scheme()

        def cohomology_divisor(self):
            return self.toric_weight_cohomology_construction().divisor()

        def cohomology_weight(self):
            return self.toric_weight_cohomology_construction().weight()

        def comparison_description(self):
            return "H^i(X,O_X(D))_m is identified with shifted reduced simplicial cohomology H~^(i-1)(V_{D,m})"


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
        def __init__(
            self,
            cohomology_weight_support,
            cohomology_weight_pieces,
            **rest,
        ) -> None:
            self._cohomology_weight_support = cohomology_weight_support
            self._cohomology_weight_pieces = cohomology_weight_pieces
            super().__init__(**rest)

        def cohomology_weight_support(self):
            return self._cohomology_weight_support

        def cohomology_weight_piece(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            return self._cohomology_weight_pieces[weight]

        def cohomology_weight_inclusion(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            assert weight in self.cohomology_weight_support(), "this weight has zero cohomology in the selected degree"
            return self.injection(weight)

        def cohomology_weight_projection(self, weight):
            weight = self.cohomology_scheme().character_lattice()(weight)
            assert weight in self.cohomology_weight_support(), "this weight has zero cohomology in the selected degree"
            return self.projection(weight)


class AffineGeometricCohomologyComplexes(OwnedCategoryOverBaseRing):
    r"""The affine-acyclic complex computing a represented quasi-coherent sheaf."""

    @classmethod
    def _repr_object_names(cls):
        return "affine geometric cohomology complexes"

    def super_categories(self):
        return [CochainComplexes(self.base_ring())]

    class ParentMethods:
        def __init__(self, geometric_sheaf, geometric_cover=None, **rest) -> None:
            self._geometric_sheaf = geometric_sheaf
            self._geometric_cover = geometric_cover
            super().__init__(**rest)

        def geometric_sheaf(self):
            return self._geometric_sheaf

        def geometric_scheme(self):
            return self.geometric_sheaf().scheme()

        def geometric_cover(self):
            r"""The distinguished unit cover the complex was stated on, or ``None`` for the one-chart cover."""
            return self._geometric_cover

        def acyclicity_reason(self):
            return "quasi-coherent sheaves on an affine scheme have no higher cohomology; this is the one-chart affine Cech resolution"

        def augmentation(self):
            r"""Return the identification of degree zero with global sections."""
            source = self.graded_piece(0)
            target = self.geometric_sheaf().global_sections()
            return source.module_category().Mor(source, target).identity()


def _affine_geometric_cohomology_complex(sheaf, cover=None):
    r"""Return the one-chart affine complex computing ``H^*(X,sheaf)``.

    The sheaf is a quasi-coherent sheaf ``M~`` on an affine scheme ``X``.  The
    cover consists of the single affine chart ``X`` itself, whose finite
    intersections are affine; quasi-coherent affine acyclicity therefore
    identifies the Cech complex with ``M`` in degree zero and zero elsewhere.
    """
    from dzack_research.preamble.categories.schemes.ringed_spaces import (
        QuasiCoherentSheaves,
    )
    from dzack_research.preamble.categories.schemes.schemes import Schemes

    scheme = sheaf.scheme()
    assert scheme in Schemes(scheme.scheme_base_ring()).Affine() and sheaf in QuasiCoherentSheaves(scheme), (
        "affine geometric cohomology is taken of a quasi-coherent sheaf on an affine scheme"
    )
    match cover:
        case None:
            pass
        case _:
            assert cover.ambient_scheme() is scheme, "the selected affine cover belongs to a different scheme"
            one = scheme.coordinate_algebra().one()
            assert all(cover.defining_element(index) == one for index in cover.atlas()), (
                "the represented contracted Cech comparison requires the selected unit charts D(1)"
            )
    module = sheaf.global_sections()
    base = module.base_ring()
    zero = base._fresh_free_module_on(finite_ordered_set(()))
    return CochainComplexes(base)(
        {0: module, 1: zero},
        {0: module.module_category().Mor(module, zero).zero()},
        name=f"Affine Cech complex of {sheaf}",
        extra_categories=(AffineGeometricCohomologyComplexes(base),),
        extra_construction_data={"geometric_sheaf": sheaf, "geometric_cover": cover},
    )


def _affine_geometric_scalar_cohomology_map(sheaf, degree, scalar, *, cover=None):
    r"""Return the cohomology map induced by scalar multiplication on ``sheaf``."""
    complex_ = _affine_geometric_cohomology_complex(sheaf, cover=cover)
    scalar = complex_.base_ring()(scalar)
    cochain_map = scalar * CochainComplexes(complex_.base_ring()).Mor(complex_, complex_).identity()
    return CochainComplexes(complex_.base_ring()).cohomology(int(degree))(cochain_map)


def _affine_cover_refinement_cochain_map(refinement, sheaf):
    r"""Return the cochain map ``C(U; F) -> C(V; F)`` induced by a unit-cover refinement ``V`` of ``U``.

    Both complexes are the contracted affine Čech complexes of ``F``, which
    are ``F(X)`` in degree zero, so the comparison is the identity there.
    Its cohomology image in degree ``d`` is
    ``CochainComplexes(R).cohomology(d)`` applied to this map.
    """
    assert refinement.ambient_scheme() is sheaf.scheme(), "the cover refinement belongs to a different affine scheme"
    source = _affine_geometric_cohomology_complex(sheaf, cover=refinement.coarse_cover())
    target = _affine_geometric_cohomology_complex(sheaf, cover=refinement.fine_cover())
    source_degree_zero = source.graded_piece(0)
    degree_zero = source_degree_zero.module_category().Mor(source_degree_zero, target.graded_piece(0)).identity()
    return CochainComplexes(source.base_ring()).Mor(source, target)({0: degree_zero})


def _affine_cover_refinement_cohomology_map(refinement, sheaf, degree):
    r"""Return ``H^degree`` of the refinement cochain map, the comparison on sheaf cohomology."""
    cochain_map = _affine_cover_refinement_cochain_map(refinement, sheaf)
    return CochainComplexes(cochain_map.domain().base_ring()).cohomology(int(degree))(cochain_map)



class _IntegralTopologicalCohomologyConstruction:
    r"""The selected realization and degree defining one integral cohomology group."""

    def __init__(self, scheme, degree, theory, realization) -> None:
        self._scheme = scheme
        self._degree = int(degree)
        self._theory = theory
        self._realization = realization

    def scheme(self):
        return self._scheme

    def degree(self):
        return self._degree

    def theory(self):
        return self._theory

    def realization_description(self):
        return self._realization


class IntegralTopologicalCohomologyGroups(OwnedCategoryOverBaseRing):
    r"""Integral cohomology groups of a specified topological realization/theory."""

    @classmethod
    def _repr_object_names(cls):
        return "integral cohomology groups of specified topological realizations"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyPresentedModules,
        )

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def __init__(self, integral_topological_cohomology_construction, **rest) -> None:
            self._integral_topological_cohomology_construction = integral_topological_cohomology_construction
            super().__init__(**rest)

        def integral_topological_cohomology_construction(self):
            return self._integral_topological_cohomology_construction

        def topological_scheme(self):
            return self.integral_topological_cohomology_construction().scheme()

        def cohomological_degree(self):
            return self.integral_topological_cohomology_construction().degree()

        def cohomology_coefficients(self):
            return self.base_ring()

        def cohomology_topology(self):
            return self.integral_topological_cohomology_construction().theory()

        def realization_description(self):
            return (
                self.integral_topological_cohomology_construction()
                .realization_description()
            )


class IntegralSingularCohomologyGroups(OwnedCategoryOverBaseRing):
    r"""Ordinary integral singular cohomology of specified complex realizations."""

    @classmethod
    def _repr_object_names(cls):
        return "ordinary integral singular cohomology groups"

    def super_categories(self):
        return [IntegralTopologicalCohomologyGroups(self.base_ring())]


class ResolutionIntegralCohomologyGroups(OwnedCategoryOverBaseRing):
    r"""Integral cohomology computed on a specified resolution/normalization."""

    @classmethod
    def _repr_object_names(cls):
        return "integral resolution cohomology groups"

    def super_categories(self):
        return [IntegralTopologicalCohomologyGroups(self.base_ring())]


class ToricIntegralSingularCohomologyGroups(OwnedCategoryOverBaseRing):
    r"""Integral singular cohomology of a specified smooth complete toric complex realization."""

    @classmethod
    def _repr_object_names(cls):
        return "integral singular cohomology groups of smooth complete toric varieties"

    def super_categories(self):
        return [IntegralSingularCohomologyGroups(self.base_ring())]


class _GeometricFundamentalGroupConstruction:
    r"""The pointed realization defining one represented fundamental group."""

    def __init__(self, scheme, base_point, realization) -> None:
        self._scheme = scheme
        self._base_point = base_point
        self._realization = realization

    def scheme(self):
        return self._scheme

    def base_point(self):
        return self._base_point

    def realization_description(self):
        return self._realization


class _ToricFundamentalGroupConstruction:
    r"""The toric realization and fixed-point cone defining one fundamental group."""

    def __init__(self, scheme, base_point_cone) -> None:
        self._scheme = scheme
        self._base_point_cone = base_point_cone

    def scheme(self):
        return self._scheme

    def base_point_cone(self):
        return self._base_point_cone


class GeometricFundamentalGroups(OwnedCategory):
    r"""Groups built as ``pi_1(X(CC), x)`` of a specified pointed complex realization.

    An object is a group together with the pointed realization it is the
    fundamental group of; forgetting that datum leaves the group.
    """

    @classmethod
    def _repr_object_names(cls):
        return "fundamental groups of specified pointed geometric realizations"

    def super_categories(self):
        return [OwnedGroups()]

    def an_object(self):
        r"""The infinite cyclic ``pi_1`` of the rational nodal cubic."""
        return _nodal_cubic_fundamental_group()

    class ParentMethods:
        def __init__(self, geometric_fundamental_group_construction, **rest) -> None:
            self._geometric_fundamental_group_construction = geometric_fundamental_group_construction
            super().__init__(**rest)

        def geometric_fundamental_group_construction(self):
            return self._geometric_fundamental_group_construction

        def topological_scheme(self):
            return self.geometric_fundamental_group_construction().scheme()

        def base_point(self):
            return self.geometric_fundamental_group_construction().base_point()

        def realization_description(self):
            return (
                self.geometric_fundamental_group_construction()
                .realization_description()
            )


def _geometric_fundamental_group(generator, scheme, base_point, realization):
    r"""``pi_1(X(CC), x)``, built as the cyclic group of ``generator`` placed with its pointed realization."""
    assert base_point.codomain() is scheme, "a pointed fundamental group requires a point of its scheme"
    return CyclicGroups()(
        generator,
        placements=(GeometricFundamentalGroups(),),
        geometric_fundamental_group_construction=_GeometricFundamentalGroupConstruction(
            scheme, base_point, realization
        ),
    )


class ToricFundamentalGroups(OwnedCategory):
    r"""Groups built as ``pi_1`` of a supported toric complex realization at a torus-fixed point."""

    @classmethod
    def _repr_object_names(cls):
        return "fundamental groups of supported toric complex realizations"

    def super_categories(self):
        return [OwnedGroups()]

    def an_object(self):
        r"""The trivial ``pi_1`` of the projective plane."""
        from dzack_research.preamble.categories.schemes.toric.fans import (
            RationalPolyhedralFans,
        )

        cocharacters = _own_ring(SageZZ).free_module(2)
        plane = RationalPolyhedralFans(cocharacters).projective_space_fan().toric_variety(_own_ring(SageQQ))
        return plane.fundamental_group()

    class ParentMethods:
        def __init__(self, toric_fundamental_group_construction, **rest) -> None:
            self._toric_fundamental_group_construction = toric_fundamental_group_construction
            super().__init__(**rest)

        def toric_fundamental_group_construction(self):
            return self._toric_fundamental_group_construction

        def topological_scheme(self):
            return self.toric_fundamental_group_construction().scheme()

        def base_point_cone(self):
            r"""Return the maximal cone indexing the selected torus-fixed basepoint."""
            return self.toric_fundamental_group_construction().base_point_cone()

        def realization_description(self):
            return "complex analytic realization under the selected QQ-to-CC embedding"


def _degree_hodge_number_family(hodge_data, degree, p_values, q_bound):
    r"""Return ``(h^{p,q})_{p+q=degree}`` as an owned indexed family.

    The index is a finite owned subset of ``NN x NN`` and every value is a
    point of ``NN``.  Thus the grading pair and the Hodge number both remain
    mathematical set elements rather than Python tuple/integer payloads.
    """
    bidegrees = Sets().product((NN, NN))
    labels = finite_ordered_set(tuple(bidegrees((NN(p), NN(degree - p))) for p in p_values if 0 <= degree - p <= q_bound))
    return finite_indexed_family(
        labels,
        lambda bidegree: NN(hodge_data.hodge_number(int(bidegree[0]), int(bidegree[1]))),
        name=f"Hodge numbers in degree {degree}",
    )


class _ToricHodgeData(SageObject):
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
        if p < 0 or q < 0 or p > dimension or q > dimension or p != q:
            return NN(0)
        return NN(self.integral_cohomology(2 * p).module_rank())

    def degree_hodge_numbers(self, degree):
        degree = int(degree)
        dimension = int(self.scheme().dimension())
        assert 0 <= degree <= 2 * dimension, "Hodge degree lies between zero and twice the complex dimension"
        return _degree_hodge_number_family(self, degree, range(degree + 1), dimension)

    def _repr_(self):
        return f"Pure toric Hodge data of {self.scheme()}"


def _matrix_morphism(base, source, target, matrix):
    r"""Cross one engine incidence matrix into an owned module morphism."""
    source_labels = tuple(source.module_generating_set())
    target_labels = tuple(target.module_generating_set())
    assert matrix.ncols() == len(source_labels) and matrix.nrows() == len(target_labels), "the simplicial differential matrix has inconsistent endpoint ranks"

    def image(source_label):
        column = source_labels.index(source_label)
        return target.linear_combination({target_label: base(int(matrix[row, column])) for row, target_label in enumerate(target_labels) if matrix[row, column]})

    return source.module_category().Mor(source, target)(image)


def _toric_weight_simplicial_complex(scheme, divisor, weight):
    r"""Private Sage adapter for the simplicial support ``V_{D,m}``.

    Sage's maintained toric-divisor implementation owns the combinatorial
    selection of the negative-cone subcomplex.  The private helper is confined
    here because the public cohomology operation returns only the resulting
    vector space and does not expose the augmented incidence maps needed by the
    owned cochain complex.
    """
    engine_divisor = scheme._engine_toric_divisor(divisor)
    return engine_divisor._sheaf_complex(_engine_vector(scheme.character_lattice(), weight))


def _toric_weight_support_hull(scheme, divisor):
    r"""Private Sage adapter for the finite weight-support hull of ``O_X(D)``."""
    return scheme._engine_toric_divisor(divisor)._sheaf_cohomology_support()


def _toric_weight_cohomology_complex(scheme, divisor, weight):
    r"""Return the finite complex computing ``H^*(X,O_X(D))_weight``.

    Sage's toric-divisor engine selects the simplicial complex ``V_{D,m}`` of
    negative cones.  We retain only that finite combinatorial output and cross
    its augmented cochain incidence matrices into owned free modules.  The
    grading is shifted by one so degree ``i`` computes
    ``H~^(i-1)(V_{D,m})``, the toric line-bundle weight cohomology.
    """
    base = scheme.scheme_base_ring()
    divisor = scheme.weil_divisor_group()(divisor)
    assert scheme.is_cartier(divisor), "the represented toric weight complex requires a Cartier divisor"
    weight = scheme.character_lattice()(weight)
    simplicial = _toric_weight_simplicial_complex(scheme, divisor, weight)

    if int(simplicial.dimension()) == -1:
        degree_zero = base.free_module(1)
        degree_one = base.free_module(0)
        complex_ = CochainComplexes(base)(
            {0: degree_zero, 1: degree_one},
            {0: degree_zero.module_category().Mor(degree_zero, degree_one)({0: degree_one.zero()})},
            name="Toric weight cohomology complex",
            extra_categories=(ToricWeightCohomologyComplexes(base),),
            extra_construction_data={
                "toric_weight_cohomology_construction": _ToricWeightCohomologyConstruction(
                    scheme, divisor, weight
                ),
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
        pieces = {q + 1: base.free_module(matrix.ncols()) for q, matrix in matrices.items()}
        pieces[top + 2] = base.free_module(0)
        differentials = {q + 1: _matrix_morphism(base, pieces[q + 1], pieces[q + 2], matrix) for q, matrix in matrices.items()}
        complex_ = CochainComplexes(base)(
            pieces,
            differentials,
            name="Toric weight cohomology complex",
            extra_categories=(ToricWeightCohomologyComplexes(base),),
            extra_construction_data={
                "toric_weight_cohomology_construction": _ToricWeightCohomologyConstruction(
                    scheme, divisor, weight
                ),
            },
        )
    return complex_


def _toric_weight_cohomology(scheme, divisor, weight, degree):
    r"""Return the owned weight piece ``H^degree(X,O_X(D))_weight`` from its complex."""
    return scheme.weight_cohomology_complex(divisor, weight).cohomology(int(degree))


def _toric_weight_scalar_cochain_map(scheme, divisor, weight, scalar):
    r"""Return multiplication by ``scalar`` on the selected toric weight complex.

    This is the cochain map induced by the scalar endomorphism of the line
    bundle ``O_X(D)``.  It is represented on the actual complex computing the
    chosen character weight, so the induced cohomology map is obtained by the
    shared cohomology functor rather than by scalar multiplication on a
    separately recomputed vector space.
    """
    complex_ = scheme.weight_cohomology_complex(divisor, weight)
    scalar = complex_.base_ring()(scalar)
    return scalar * CochainComplexes(complex_.base_ring()).Mor(complex_, complex_).identity()


def _toric_weight_scalar_cohomology_map(scheme, divisor, weight, degree, scalar):
    r"""Return the map on one weight cohomology induced by scalar multiplication."""
    cochain_map = scheme.weight_scalar_cochain_map(divisor, weight, scalar)
    return CochainComplexes(scheme.scheme_base_ring()).cohomology(int(degree))(cochain_map)


def _toric_line_bundle_cohomology(scheme, divisor, degree):
    r"""Assemble ``H^degree(X,O_X(D))`` as the direct sum of its weight cohomologies."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    degree = int(degree)
    assert 0 <= degree <= int(scheme.dimension()), "cohomological degree lies outside the scheme dimension"
    assert scheme.fan().is_complete(), "finite-dimensional toric line-bundle cohomology requires a complete fan"
    divisor = scheme.weil_divisor_group()(divisor)
    assert scheme.is_cartier(divisor), "the represented geometric cohomology requires a Cartier divisor"

    support_hull = _toric_weight_support_hull(scheme, divisor)
    characters = scheme.character_lattice()
    candidate_weights = tuple(_owned_vector(characters, point) for point in support_hull.integral_points())
    pieces = {
        weight: scheme.weight_cohomology(divisor, weight, degree)
        for weight in candidate_weights
    }
    pieces = {weight: piece for weight, piece in pieces.items() if int(piece.dimension()) != 0}
    weights = finite_ordered_set(tuple(pieces))
    base = scheme.scheme_base_ring()
    weight_pieces = finite_indexed_family(
        weights,
        lambda weight: pieces[weight],
        name="Nonzero toric cohomology weight pieces",
    )
    construction_data = {
        "cohomology_scheme": scheme,
        "cohomology_divisor": divisor,
        "cohomological_degree": degree,
        "cohomology_weight_support": weights,
        "cohomology_weight_pieces": weight_pieces,
    }
    if weights.cardinality() == 0:
        total = base._fresh_free_module_on(
            finite_ordered_set(()),
            _extra_categories=(ToricGeometricLineBundleCohomologySpaces(base),),
            _extra_construction_data=construction_data,
        )
    else:
        total = Modules(base).biproduct(
            weight_pieces,
            extra_categories=(ToricGeometricLineBundleCohomologySpaces(base),),
            extra_construction_data=construction_data,
        )
    return total


def _require_smooth_quartic_k3_complex_realization(scheme):
    r"""Require the represented smooth quartic K3 regime over ``QQ``."""
    from dzack_research.preamble.categories.schemes.complete_intersections import (
        ProjectiveCompleteIntersections,
    )

    base = scheme.scheme_base_ring()
    assert _engine_ring(base) is SageQQ, (
        "the selected quartic K3 integral realization uses the specified QQ-to-CC embedding"
    )
    assert scheme in ProjectiveCompleteIntersections(base), "the represented quartic K3 topology requires a projective complete intersection"
    assert int(scheme.expected_dimension()) == 2 and tuple(scheme.defining_degrees()) == (4,), "the represented K3 topology here is for a quartic surface in P^3"
    assert bool(scheme.is_smooth()), "the quartic K3 integral realization requires a smooth surface"


class _QuarticK3IntegralTopology(SageObject):
    r"""Integral singular cohomology of a smooth quartic K3 with one marking.

    Under the selected complex realization, a smooth quartic surface is a K3
    surface.  Its middle integral cohomology with cup product is the even
    unimodular K3 lattice ``3U + 2E8(-1)``.  A *marking* is additional data;
    this object selects the catalogue marking in which the hyperplane class is
    ``e1 + 2 f1``, a primitive vector of square ``4``.  No toric Chow
    comparison is used.
    """

    def __init__(self, scheme) -> None:
        _require_smooth_quartic_k3_complex_realization(scheme)
        self._scheme = scheme

    def scheme(self):
        return self._scheme

    def realization_description(self):
        return "ordinary singular cohomology of the complex analytic quartic under the selected QQ-to-CC embedding"

    @cached_method
    def middle_cohomology_lattice(self):
        from dzack_research.preamble.catalogue import NamedLattices

        return NamedLattices.LK3

    @cached_method
    def integral_cohomology(self, degree):
        degree = int(degree)
        assert degree >= 0, "a singular-cohomology degree is nonnegative"
        integers = _own_ring(SageZZ)
        if degree == 2:
            return self.middle_cohomology_lattice()
        if degree in (0, 4):
            return integers._fresh_free_module_on(
                finite_ordered_set((f"H{degree}",)),
            )
        return integers._fresh_free_module_on(finite_ordered_set(()))

    @cached_method
    def cup_product(self, left_degree, right_degree):
        r"""Return the graded cup product in the selected K3 marking."""
        left_degree = int(left_degree)
        right_degree = int(right_degree)
        assert left_degree >= 0 and right_degree >= 0, "cup-product degrees are nonnegative"
        left = self.integral_cohomology(left_degree)
        right = self.integral_cohomology(right_degree)
        target = self.integral_cohomology(left_degree + right_degree)
        if left_degree == 0:
            return BilinearMap(
                left,
                right,
                target,
                lambda _unit_label, right_label: target.module_generator(right_label),
            )
        if right_degree == 0:
            return BilinearMap(
                left,
                right,
                target,
                lambda left_label, _unit_label: target.module_generator(left_label),
            )
        if left_degree == right_degree == 2:
            top_label = next(iter(target.module_generating_set()))
            middle = self.middle_cohomology_lattice()
            return BilinearMap(
                left,
                right,
                target,
                lambda left_label, right_label: target.scalar_multiple(
                    middle.b(
                        middle.module_generator(left_label),
                        middle.module_generator(right_label),
                    ),
                    target.module_generator(top_label),
                ),
            )
        return BilinearMap(
            left,
            right,
            target,
            lambda _left_label, _right_label: target.zero(),
        )

    @cached_method
    def cup_product_pairing(self):
        middle = self.middle_cohomology_lattice()
        values = _own_ring(SageZZ).regular_module()
        return BilinearMap(
            middle,
            middle,
            values,
            lambda left, right: middle.b(
                middle.module_generator(left),
                middle.module_generator(right),
            ),
        )

    @cached_method
    def hyperplane_first_chern_class(self):
        middle = self.middle_cohomology_lattice()
        e1, f1 = tuple(middle.module_generators())[:2]
        hyperplane = e1 + 2 * f1
        assert middle.q(hyperplane) == _own_ring(SageZZ)(4), "the selected K3 marking does not give the quartic hyperplane square four"
        assert hyperplane.is_primitive(), "the selected quartic hyperplane class is not primitive"
        return hyperplane

    @cached_method
    def hyperplane_c1_embedding(self):
        from dzack_research.preamble.catalogue import NamedLattices

        source = NamedLattices.Z.twist(4)
        target = self.middle_cohomology_lattice()
        hyperplane = self.hyperplane_first_chern_class()
        return source.Emb(target)(lambda _label: hyperplane)

    def first_chern_class(self, line_bundle):
        r"""``c_1(O_X(d)) = d h`` for a restricted projective line bundle ``O_X(d)``.

        The represented line bundles on the quartic are the restrictions
        ``O_X(d)``; other classes of ``Pic(X)`` are not constructed.
        """
        assert line_bundle.scheme() is self.scheme(), "the first Chern class belongs to a line bundle on this K3 surface"
        return int(line_bundle.degree()) * self.hyperplane_first_chern_class()

    @cached_method
    def hodge_structure(self):
        return _QuarticK3HodgeData(self.scheme())

    def middle_cohomology_torsion_free_quotient(self):
        r"""K3 middle cohomology is already torsion-free."""
        return self.middle_cohomology_lattice()

    def _repr_(self) -> str:
        return f"Integral topology of {self.scheme()} ({self.realization_description()})"



class _QuarticK3HodgeData(SageObject):
    r"""Pure Hodge data of the selected smooth quartic K3 realization.

    Adjunction gives ``K_X = O_X``.  The represented restriction of the unique
    constant section computes ``h^(2,0)=h^0(K_X)``.  Hodge symmetry gives
    ``h^(0,2)``, and the integral K3 lattice supplies ``b_2=22``, so the
    remaining middle dimension is ``h^(1,1)``.  Thus the off-diagonal terms are
    attached to the live canonical bundle and integral cohomology rather than a
    toric diagonal template.
    """

    def __init__(self, scheme) -> None:
        _require_smooth_quartic_k3_complex_realization(scheme)
        self._scheme = scheme

    def scheme(self):
        return self._scheme

    def is_pure(self) -> bool:
        return True

    def integral_topology(self):
        return self.scheme().integral_topology()

    def integral_cohomology(self, degree):
        return self.integral_topology().integral_cohomology(degree)

    @cached_method
    def holomorphic_two_form_space(self):
        canonical = self.scheme().canonical_line_bundle()
        return canonical.represented_global_section_image()

    def hodge_number(self, p, q):
        p = int(p)
        q = int(q)
        if p < 0 or q < 0 or p > 2 or q > 2:
            return NN(0)
        if (p, q) == (0, 0) or (p, q) == (2, 2):
            return NN(1)
        if p + q != 2:
            return NN(0)
        holomorphic = int(self.holomorphic_two_form_space().dimension())
        if (p, q) in ((2, 0), (0, 2)):
            return NN(holomorphic)
        middle_rank = int(self.integral_cohomology(2).module_rank())
        return NN(middle_rank - 2 * holomorphic)

    def degree_hodge_numbers(self, degree):
        degree = int(degree)
        assert 0 <= degree <= 4, "a K3 surface has Hodge degrees zero through four"
        return _degree_hodge_number_family(self, degree, range(3), 2)

    def middle_betti_number(self):
        return int(self.integral_cohomology(2).module_rank())

    def polarization_class(self):
        return self.integral_topology().hyperplane_first_chern_class()

    def _repr_(self) -> str:
        return f"Hodge data of {self.scheme()}"



def _integral_topology_construction_data(
    scheme,
    degree,
    realization,
    theory="ordinary singular cohomology",
):
    return {
        "integral_topological_cohomology_construction": (
            _IntegralTopologicalCohomologyConstruction(
                scheme,
                degree,
                theory,
                realization,
            )
        ),
    }


def _free_integral_topology_group(
    scheme,
    degree,
    rank,
    realization,
    *,
    category=None,
    theory="ordinary singular cohomology",
):
    integers = _own_ring(SageZZ)
    category = IntegralSingularCohomologyGroups(integers) if category is None else category
    return integers._fresh_free_module_on(
        finite_ordered_set(tuple(f"H{degree}_{index}" for index in range(rank))),
        _extra_categories=(category,),
        _extra_construction_data=_integral_topology_construction_data(scheme, degree, realization, theory),
    )


def _zmod2_integral_topology_group(scheme, degree, realization):
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presented_module_from_morphism,
    )

    integers = _own_ring(SageZZ)
    source = integers.free_module(1)
    target = integers.free_module(1)
    presentation = source.module_category().Mor(source, target)({0: integers(2) * target.module_generator(0)})
    return _presented_module_from_morphism(
        presentation,
        _extra_categories=(IntegralSingularCohomologyGroups(integers),),
        _extra_construction_data=_integral_topology_construction_data(scheme, degree, realization),
    )


@cached_function
def NodalCubic():
    r"""Return the rational nodal cubic ``y^2 z = x^2(x+z)`` in ``P^2``."""
    from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

    base = _own_ring(SageQQ)
    plane = ProjectiveSpaces(base)(2, names=("x", "y", "z"))
    ring = plane.O(3).global_sections().homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    z = ring.algebra_generator("z")
    return plane.closed_subscheme(y**2 * z - x**2 * (x + z))


@cached_function
def NodalCubicNormalization():
    r"""Return the explicit normalization ``P^1 -> C`` of :func:`NodalCubic`."""
    from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

    curve = NodalCubic()
    plane = curve.inclusion().codomain()
    line = ProjectiveSpaces(curve.scheme_base_ring())(1, names=("s", "t"))
    ring = line.O(3).global_sections().homogeneous_coordinate_ring()
    s = ring.algebra_generator("s")
    t = ring.algebra_generator("t")
    ambient = line.projective_morphism_from_coordinates(
        plane,
        ((s**2 - t**2) * t, s * (s**2 - t**2), t**3),
    )
    normalization = curve.corestriction(ambient)
    return normalization


def _nodal_cubic_fundamental_group(scheme=None, base_point=None):
    r"""Return the pointed ``pi_1`` of the rational nodal cubic, an infinite cyclic group."""
    selected = NodalCubic() if scheme is None else scheme
    assert selected is NodalCubic(), "this fundamental-group model is attached to the represented nodal cubic"
    point = selected.point_morphism((0, 1, 0)) if base_point is None else base_point
    generator = next(iter(OwnedGroups().Free(1).group_generators()))
    return _geometric_fundamental_group(
        generator,
        selected,
        point,
        "nodal cubic complex realization S^2 wedge S^1",
    )


def _projective_line_fundamental_group(line, base_point):
    r"""Return the trivial pointed fundamental group of one represented projective line."""
    return _geometric_fundamental_group(
        OwnedGroups().C(1).one(),
        line,
        base_point,
        "complex projective line, homeomorphic to S^2",
    )


class NodalCubicIntegralTopology(SageObject):
    r"""Ordinary and normalization-resolution cohomology of the rational nodal cubic.

    Analytically, identifying the two preimages of the node in ``P^1`` gives
    ``C(C) ~= S^2 vee S^1``.  Thus ordinary cohomology has ``H^1=Z``, while
    resolution cohomology means the ordinary cohomology of the normalization
    ``P^1`` and has ``H^1=0``.  The normalization morphism supplies the actual
    contravariant comparison map between the two selected theories.
    """

    _ordinary_realization = "ordinary singular cohomology of the complex nodal cubic, topologically S^2 wedge S^1"
    _resolution_realization = "resolution cohomology via the explicit normalization P^1 -> nodal cubic"

    def __init__(self, scheme=None) -> None:
        selected = NodalCubic() if scheme is None else scheme
        assert selected is NodalCubic(), "this topology comparison is attached to the represented nodal cubic"
        self._scheme = selected

    def scheme(self):
        return self._scheme

    @cached_method
    def normalization_morphism(self):
        return NodalCubicNormalization()

    def normalization_scheme(self):
        return self.normalization_morphism().domain()

    @cached_method
    def base_point(self):
        return self.scheme().point_morphism((0, 1, 0))

    @cached_method
    def normalization_base_point(self):
        point = self.normalization_scheme().point_morphism((1, 0))
        image = self.normalization_morphism().image_of_point(point)
        assert tuple(image.point_coordinates()) == tuple(self.base_point().point_coordinates()), "the selected normalization basepoint does not map to the selected nodal basepoint"
        return point

    @cached_method
    def fundamental_group(self):
        return _nodal_cubic_fundamental_group(self.scheme(), self.base_point())

    @cached_method
    def normalization_fundamental_group(self):
        return _projective_line_fundamental_group(
            self.normalization_scheme(),
            self.normalization_base_point(),
        )

    @cached_method
    def normalization_fundamental_group_map(self):
        r"""Return the induced map ``pi_1(P^1)->pi_1(C)`` of the pointed normalization."""
        source = self.normalization_fundamental_group()
        target = self.fundamental_group()
        induced = source.Mor(target)(())
        return induced

    @cached_method
    def ordinary_cohomology(self, degree):
        degree = int(degree)
        assert degree >= 0, "a cohomological degree is nonnegative"
        rank = 1 if degree in (0, 1, 2) else 0
        return _free_integral_topology_group(
            self.scheme(),
            degree,
            rank,
            self._ordinary_realization,
            category=IntegralSingularCohomologyGroups(_own_ring(SageZZ)),
            theory="ordinary singular cohomology",
        )

    @cached_method
    def resolution_cohomology(self, degree):
        degree = int(degree)
        assert degree >= 0, "a cohomological degree is nonnegative"
        rank = 1 if degree in (0, 2) else 0
        return _free_integral_topology_group(
            self.scheme(),
            degree,
            rank,
            self._resolution_realization,
            category=ResolutionIntegralCohomologyGroups(_own_ring(SageZZ)),
            theory="resolution cohomology via normalization",
        )

    @cached_method
    def normalization_pullback(self, degree):
        r"""Return ``nu^*:H^degree(C,Z)->H^degree(P^1,Z)`` for the normalization."""
        source = self.ordinary_cohomology(degree)
        target = self.resolution_cohomology(degree)
        source_labels = tuple(source.module_generating_set())
        target_labels = tuple(target.module_generating_set())
        if len(source_labels) == len(target_labels) == 1:
            return source.module_category().Mor(source, target)({source_labels[0]: target.module_generator(target_labels[0])})
        return source.module_category().Mor(source, target)({label: target.zero() for label in source_labels})

    def _repr_(self) -> str:
        return f"Integral topology of {self.scheme()} with normalization {self.normalization_scheme()}"



@cached_function
def ProjectiveGeneralLinearGroup2():
    r"""Return ``PGL_2`` over ``QQ`` as ``P^3 - V(ad-bc)``."""
    from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

    base = _own_ring(SageQQ)
    projective = ProjectiveSpaces(base)(3, names=("a", "b", "c", "d"))
    sections = projective.O(2).global_sections()
    ring = sections.homogeneous_coordinate_ring()
    a = ring.algebra_generator("a")
    b = ring.algebra_generator("b")
    c = ring.algebra_generator("c")
    d = ring.algebra_generator("d")
    return projective.closed_subscheme(a * d - b * c).open_complement()


def _pgl2_fundamental_group(scheme=None, base_point=None):
    r"""Return the pointed ``pi_1(PGL_2(C)) ~= C_2``."""
    selected = ProjectiveGeneralLinearGroup2() if scheme is None else scheme
    assert selected is ProjectiveGeneralLinearGroup2(), "this fundamental-group model is attached to represented PGL_2"
    point = selected.point_morphism((1, 0, 0, 1)) if base_point is None else base_point
    generator = next(iter(OwnedGroups().C(2).group_generators()))
    return _geometric_fundamental_group(
        generator,
        selected,
        point,
        "PGL_2(C) deformation retracted to PU(2) ~= SO(3)",
    )


class PGL2IntegralTopology(SageObject):
    r"""Ordinary integral cohomology of ``PGL_2(C)`` via its ``SO(3)`` retract.

    Polar decomposition retracts ``PGL_2(C)`` onto ``PU(2) ~= SO(3) ~= RP^3``.
    Hence the integral cohomology has ``Z`` in degrees 0 and 3, ``Z/2`` in
    degree 2, and zero otherwise.  This torsion is deliberately retained and
    disappears after rational coefficient change.
    """

    _realization = "PGL_2(C)=P^3(C)-V(ad-bc), deformation retracted by polar decomposition to PU(2) ~= SO(3) ~= RP^3"

    def __init__(self, scheme=None) -> None:
        selected = ProjectiveGeneralLinearGroup2() if scheme is None else scheme
        assert selected is ProjectiveGeneralLinearGroup2(), "the selected ordinary-topology model is the represented PGL_2 scheme"
        self._scheme = selected

    def scheme(self):
        return self._scheme

    def realization_description(self):
        return self._realization

    @cached_method
    def base_point(self):
        return self.scheme().point_morphism((1, 0, 0, 1))

    @cached_method
    def fundamental_group(self):
        return _pgl2_fundamental_group(self.scheme(), self.base_point())

    @cached_method
    def integral_cohomology(self, degree):
        degree = int(degree)
        assert 0 <= degree <= 6, "PGL_2 has complex dimension three, so singular cohomology lies in degrees zero through six"
        if degree == 2:
            return _zmod2_integral_topology_group(self.scheme(), degree, self.realization_description())
        if degree in (0, 3):
            return _free_integral_topology_group(self.scheme(), degree, 1, self.realization_description())
        return _free_integral_topology_group(self.scheme(), degree, 0, self.realization_description())

    @cached_method
    def rational_cohomology(self, degree):
        integers = _own_ring(SageZZ)
        extension = integers.fraction_field_map()
        return self.integral_cohomology(degree).base_change(extension)

    @cached_method
    def coefficient_change_to_rationals(self, degree):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        integers = _own_ring(SageZZ)
        extension = integers.fraction_field_map()
        return Modules(integers).base_change_adjunction(extension).unit(self.integral_cohomology(degree))

    def _repr_(self) -> str:
        return f"Integral topology of {self.scheme()} ({self.realization_description()})"



def _require_smooth_complete_rational_toric_realization(scheme):
    assert _engine_ring(scheme.scheme_base_ring()) is SageQQ, (
        "the selected integral singular-cohomology comparison uses the specified QQ-to-CC realization"
    )
    assert scheme.fan().is_smooth() and scheme.fan().is_complete(), "the Jurkiewicz-Danilov integral comparison requires a smooth complete toric variety"


def _toric_integral_singular_cohomology(scheme, degree):
    r"""Return ``H^degree(X(CC),ZZ)`` through the integral toric cycle comparison.

    For a smooth complete complex toric variety, Danilov--Jurkiewicz identifies
    the integral Chow ring with integral singular cohomology, with invariant
    divisor classes in Chow codimension ``k`` mapping to degree ``2k``.
    Odd cohomology vanishes and the even groups are torsion-free.
    """
    _require_smooth_complete_rational_toric_realization(scheme)
    degree = int(degree)
    dimension = int(scheme.dimension())
    assert 0 <= degree <= 2 * dimension, "singular cohomological degree lies between zero and twice the complex dimension"
    integers = _own_ring(SageZZ)
    construction_data = _integral_topology_construction_data(
        scheme,
        degree,
        "complex analytic realization under the selected QQ-to-CC embedding",
        "singular cohomology of the complex analytic realization",
    )
    if degree % 2:
        return integers._fresh_free_module_on(
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


def _toric_cycle_class_isomorphism(scheme, codimension):
    r"""Return ``CH^k(X) -> H^(2k)(X(CC),ZZ)`` for smooth complete toric ``X/QQ``."""
    _require_smooth_complete_rational_toric_realization(scheme)
    codimension = int(codimension)
    dimension = int(scheme.dimension())
    assert 0 <= codimension <= dimension, "cycle codimension lies between zero and the scheme dimension"
    chow = scheme.chow_group(dimension - codimension)
    cohomology = scheme.integral_singular_cohomology(2 * codimension)
    forward = chow.module_category().Mor(chow, cohomology)({label: cohomology.module_generator(label) for label in chow.module_generating_set()})
    inverse = cohomology.module_category().Mor(cohomology, chow)({label: chow.module_generator(label) for label in cohomology.module_generating_set()})
    return chow.module_category().Core().Mor(chow, cohomology)(forward, inverse)


def _toric_picard_to_chow_isomorphism(scheme):
    r"""Return ``Pic(X) -> CH^1(X)`` for a smooth complete toric surface."""
    _require_smooth_complete_rational_toric_realization(scheme)
    assert int(scheme.dimension()) == 2, "the represented Picard-to-Chow comparison is currently used on surfaces"
    picard = scheme.picard_group()
    chow = scheme.chow_group(1)
    cycles = scheme.torus_invariant_cycle_group(1)
    cycle_projection = scheme.torus_invariant_cycle_class_map(1)
    forward = picard.module_category().Mor(picard, chow)({label: cycle_projection(cycles.module_generator(label)) for label in picard.module_generating_set()})
    return picard.module_category().Core().Mor(picard, chow)(forward, forward.inverse())


def _toric_middle_cohomology_form(scheme):
    r"""Return ``H^2(X(CC),ZZ)`` with its cup-product intersection form."""
    _require_smooth_complete_rational_toric_realization(scheme)
    assert int(scheme.dimension()) == 2, "the represented middle-cohomology form is for surfaces"
    cohomology = scheme.integral_singular_cohomology(2)
    cycle_class = scheme.cycle_class_isomorphism(1)
    picard_to_chow = scheme.picard_to_chow_isomorphism()
    cohomology_to_picard = picard_to_chow.inverse() * cycle_class.inverse()
    intersection = scheme.picard_intersection_pairing()
    integers = _own_ring(SageZZ)
    return cohomology.equip_bilinear_form(integers, lambda left, right: intersection(
            cohomology_to_picard(left),
            cohomology_to_picard(right),
        ))


def _toric_fundamental_group(scheme, base_point_cone=None):
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
    assert base_point_cone in maximal, "the selected torus-fixed basepoint is indexed by a maximal cone"
    return CyclicGroups()(
        OwnedGroups().C(1).one(),
        placements=(ToricFundamentalGroups(),),
        toric_fundamental_group_construction=_ToricFundamentalGroupConstruction(scheme, base_point_cone),
    )


def _toric_hodge_structure(scheme):
    r"""Return the pure diagonal Hodge data of a smooth complete toric complex realization."""
    return _ToricHodgeData(scheme)


__all__ = [
    "GeometricFundamentalGroups",
    "NodalCubicIntegralTopology",
    "NodalCubicNormalization",
    "NodalCubic",
    "ResolutionIntegralCohomologyGroups",
    "IntegralTopologicalCohomologyGroups",
    "ProjectiveGeneralLinearGroup2",
    "PGL2IntegralTopology",
    "IntegralSingularCohomologyGroups",
    "AffineGeometricCohomologyComplexes",
    "ToricGeometricLineBundleCohomologySpaces",
    "ToricIntegralSingularCohomologyGroups",
    "ToricFundamentalGroups",
    "ToricWeightCohomologyComplexes",
]
