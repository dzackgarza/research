r"""Projective complete intersections with their selected regular sequence.

A complete intersection ``X = V_+(f_1, ..., f_r) <= P^n_R`` is a closed
subscheme of projective space together with the homogeneous equations cutting
it out, where ``f_1, ..., f_r`` is a regular sequence.  It is constructed by
the closed-subscheme construction of ``P^n_R`` with the placement
``ProjectiveCompleteIntersections(R)``; the category adds no datum of its own:
its codimension, multidegree and ambient are read off the equations and the
inclusion.

The base change ``X_{R'} = X x_{Spec R} Spec R'`` along ``g: R -> R'`` is the
closed subscheme of ``P^n_{R'}`` cut out by the base-changed equations, and it
is constructed as an object of ``FiberProductSchemes(R')``: its left projection
is ``X_{R'} -> X`` and its right projection is the structure morphism.
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    _engine_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ClosedSubschemes,
    FiberProductSchemes,
    ProjectiveSpaces,
    SchemeFiberProductConstruction,
    SchemeMorphism,
    Schemes,
    _engine_projective_subscheme,
    _projective_closed_subscheme,
    _projective_equation_family,
    _engine_scheme,
    _equation_family,
    _native_scheme_homset,
    _scheme_mor_category,
    _structure_morphism_rule,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family


def _complete_intersection_base_supported(base) -> bool:
    r"""Whether the base is a field, a localization of one, or a polynomial algebra over one.

    Over these bases the homogeneous coordinate ring is regular, so ``r``
    homogeneous equations whose ideal has height ``r`` form a regular sequence.
    """
    match base:
        case _ if base in OwnedFields():
            return True
        case _ if base in LocalizationRings():
            return _complete_intersection_base_supported(base.localization_source())
        case _ if base.base_ring() in OwnedFields():
            return base in SymmetricAlgebras(base.base_ring())
        case _:
            return False


def _projective_complete_intersection(ambient, equations, placements=(), **level_data):
    r"""``V_+(f_1, ..., f_r) <= P^n_R`` as a complete intersection.

    The equations are the selected regular sequence.  The closed subscheme is
    constructed once, with its complete-intersection placement and any further
    placement a construction states (the fibre-product placement of a base
    change); the regular-sequence criterion is checked on the native ideal
    before the object is constructed.
    """
    base = ambient.scheme_base_ring()
    assert ambient in ProjectiveSpaces(base), (
        "the represented complete-intersection criterion requires a projective-space ambient"
    )
    assert _complete_intersection_base_supported(base), (
        "the represented complete-intersection criterion requires a field, a localization of a "
        "represented base, or a polynomial parameter algebra over a field"
    )
    family = _projective_equation_family(_equation_family(equations))
    assert family.cardinality() > 0, "a selected regular sequence is nonempty"
    engine = _engine_projective_subscheme(_engine_scheme(ambient), family)
    assert _regular_sequence_codimension(engine) == int(family.cardinality()), (
        "the selected homogeneous equations do not have the height of a regular sequence"
    )
    return _projective_closed_subscheme(
        ambient, family, placements=(ProjectiveCompleteIntersections(base), *placements),
        _engine=engine, **level_data,
    )


def _regular_sequence_codimension(engine):
    r"""Height of the homogeneous defining ideal, before scheme placement.

    Engine adapter for the complete-intersection entry: in the regular
    polynomial rings it admits, height equal to the number of generators
    is the regular-sequence criterion (Stacks, 00NQ and 02JN).  The computation is
    the native ideal's dimension computation, not a second scheme object.
    """
    ring = engine.ambient_space().coordinate_ring()
    return int(ring.krull_dimension() - engine.defining_ideal().dimension())


class ProjectiveCompleteIntersections(OwnedCategoryOverBaseRing):
    r"""Closed complete intersections in projective space over a regular base.

    Over a field, a localization, and a polynomial parameter algebra over a
    field, the homogeneous coordinate ring is regular.  There ``r`` homogeneous
    equations whose ideal has height ``r`` form a regular sequence, hence cut
    out a complete intersection; the represented criterion is exactly
    ``number of selected equations == codimension``.
    """

    def an_object(self):
        plane = ProjectiveSpaces(self.base_ring())(2)
        x, y, z = plane.homogeneous_coordinate_generators()
        return self(plane, x * z - y**2)

    def _call_(self, ambient, *equations):
        r"""``V_+(f_1, ..., f_r) <= P^n_R`` for a regular sequence of homogeneous equations.

        The equations are given one by one or as one finite family.
        """
        assert ambient.scheme_base_ring() is self.base_ring(), (
            "a complete intersection is constructed in a projective space over this category's base ring"
        )
        return _projective_complete_intersection(ambient, equations)

    def _repr_object_names(self):
        return f"projective complete intersections over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Projective(), ClosedSubschemes(self.base_ring())]

    class ParentMethods:
        def is_complete_intersection(self) -> bool:
            return True

        def complete_intersection_ambient(self):
            r"""The projective space ``P^n_R`` this complete intersection is cut out of."""
            return self.inclusion().codomain()

        def defining_degrees(self):
            r"""The degrees ``d_1, ..., d_r`` of the selected regular sequence."""
            return finite_family(
                tuple(int(equation.degree()) for equation in self.defining_equations()),
                name="Complete-intersection defining degrees",
            )

        def complete_intersection_codimension(self):
            return self.defining_equations().cardinality()

        def expected_dimension(self):
            return int(self.complete_intersection_ambient().relative_dimension()) - int(
                self.complete_intersection_codimension()
            )

        def family_base_scheme(self):
            return self.base_scheme()

        def family_morphism(self):
            r"""Return the relative projective complete-intersection morphism to its base."""
            return self.structure_morphism()

        def base_change_source_complete_intersection(self):
            r"""``X`` for ``X_{R'} = X x_{Spec R} Spec R'``: the domain of the left cospan leg."""
            assert self in FiberProductSchemes(self.scheme_base_ring()), (
                "this complete intersection was not constructed as a scalar base change"
            )
            return self.fiber_product_cospan()[0].domain()

        def base_change_projection(self):
            r"""The projection ``X_{R'} -> X`` of the scalar base-change pullback."""
            assert self in FiberProductSchemes(self.scheme_base_ring()), (
                "this complete intersection was not constructed as a scalar base change"
            )
            return self.left_projection()

        def base_change(self, ring_map):
            r"""Base change through the scheme owner; the new equations decide regularity.

            A regular sequence need not stay regular under nonflat base
            change.  The scheme owner always constructs the base-changed
            closed subscheme, and keeps complete-intersection placement only
            when the new homogeneous ideal satisfies the criterion.
            """
            return self.scheme_category().base_change_functor(ring_map)(self)

        def adjunction_twist_degree(self):
            r"""Return ``sum(d_i) - n - 1`` in ``K_X = O_X(sum d_i-n-1)``.

            This is the integer in the projective complete-intersection
            adjunction formula.  The canonical bundle and the adjunction
            isomorphism are returned by :meth:`canonical_line_bundle` and
            :meth:`adjunction_isomorphism`.
            """
            ambient_dimension = int(self.complete_intersection_ambient().relative_dimension())
            return sum(self.defining_degrees()) - ambient_dimension - 1

        def is_gorenstein(self) -> bool:
            r"""Return ``True``: a quotient of a regular ring by a regular sequence is Gorenstein."""
            return True

        def is_normal(self) -> bool:
            r"""Decide normality by Serre's criterion in characteristic zero.

            A complete intersection is Cohen--Macaulay, hence satisfies ``S_2``.
            Thus normality is equivalent to ``R_1``.  Sage's projective
            Jacobian ideal is computed on the affine cone: if ``X`` has
            dimension ``d >= 1``, ``R_1`` says its projective singular locus
            has dimension at most ``d-2``, equivalently the affine-cone
            Jacobian locus has dimension at most ``d-1``.  In dimension zero,
            characteristic zero makes normality equivalent to smoothness.
            """
            base = self.scheme_base_ring()
            assert base in OwnedFields(), (
                "the represented complete-intersection normality criterion applies to a selected field fibre, "
                "not a relative family inferred only from its equations"
            )
            assert int(_engine_ring(base).characteristic()) == 0, (
                "the represented complete-intersection normality criterion requires characteristic zero"
            )
            dimension = int(self.expected_dimension())
            if dimension == 0:
                return bool(self.is_smooth())
            singular_cone_dimension = int(_engine_scheme(self).Jacobian().dimension())
            return singular_cone_dimension <= dimension - 1

        def projective_degree(self):
            r"""Return the complete-intersection degree ``prod d_i``."""
            degree = 1
            for value in self.defining_degrees():
                degree *= int(value)
            return degree

        def anticanonical_twist_degree(self):
            r"""Return ``n + 1 - sum(d_i)`` for ``-K_X``."""
            return -self.adjunction_twist_degree()

        @cached_method
        def restricted_ambient_canonical_bundle(self):
            r"""``omega_P|_X = O_X(-n-1)``, the restricted canonical bundle of the ambient."""
            return self.complete_intersection_ambient().canonical_line_bundle().restrict_to(self)

        @cached_method
        def normal_determinant_line_bundle(self):
            r"""``det N_{X/P} = O_X(sum d_i)`` for the selected regular sequence."""
            return self.O(sum(self.defining_degrees()))

        @cached_method
        def adjunction_isomorphism(self):
            r"""The adjunction isomorphism ``omega_X ~= omega_P|_X tensor det N_{X/P}``.

            Its domain is the canonical bundle ``O_X(sum d_i - n - 1)`` and its
            codomain is the tensor product of the restricted ambient canonical
            bundle with the determinant of the normal bundle.
            """
            canonical = self.O(self.adjunction_twist_degree())
            target = self.restricted_ambient_canonical_bundle().tensor_product(
                self.normal_determinant_line_bundle()
            )
            return canonical.canonical_isomorphism_to(target)

        def adjunction_target(self):
            r"""``omega_P|_X tensor det N_{X/P}``, the codomain of the adjunction isomorphism."""
            return self.adjunction_isomorphism().codomain()

        def canonical_line_bundle(self):
            return self.adjunction_isomorphism().domain()

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            return self.canonical_line_bundle().dual_sheaf()

        anticanonical_bundle = anticanonical_line_bundle

        def is_del_pezzo(self) -> bool:
            r"""Decide the del Pezzo condition for a smooth complete-intersection surface.

            In this represented regime adjunction constructs ``-K_X`` as an
            actual restricted projective line bundle.  Smoothness is decided
            by Sage's exact projective-subscheme Jacobian calculation and the
            ampleness question is delegated to that line-bundle object.
            """
            assert self.scheme_base_ring() in OwnedFields(), (
                "the del Pezzo predicate is a fibrewise projective-surface question over a field"
            )
            if int(self.expected_dimension()) != 2:
                return False
            if not bool(self.is_smooth()):
                return False
            return bool(self.anticanonical_line_bundle().is_ample())

        @cached_method
        def integral_topology(self):
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _QuarticK3IntegralTopology,
            )

            return _QuarticK3IntegralTopology(self)

        def integral_singular_cohomology(self, degree):
            return self.integral_topology().integral_cohomology(degree)

        @cached_method
        def hodge_structure(self):
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _QuarticK3HodgeData,
            )

            return _QuarticK3HodgeData(self)

        def del_pezzo_degree(self):
            r"""Return ``(-K_X)^2 = (n + 1 - sum d_i)^2 prod d_i`` for a del Pezzo complete intersection."""
            assert self.is_del_pezzo(), "the represented complete intersection is not a del Pezzo surface"
            coefficient = self.anticanonical_twist_degree()
            return coefficient**2 * self.projective_degree()


__all__ = [
    "ProjectiveCompleteIntersections",
]
