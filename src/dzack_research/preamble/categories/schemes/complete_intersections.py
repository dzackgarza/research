r"""Projective complete intersections with their selected defining multidegree."""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    _engine_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ClosedSubschemes,
    ProjectiveSchemes,
    ProjectiveSpaces,
    _categorical_scheme_morphism,
    _refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family


def _complete_intersection_base_supported(base) -> bool:
    r"""Return whether the selected regular base regime justifies the CI criterion."""
    if base in OwnedFields():
        return True
    if base in LocalizationRings():
        return _complete_intersection_base_supported(base.localization_source())
    try:
        coefficient_base = base.algebra_base_ring()
    except AttributeError:
        return False
    return (
        coefficient_base in OwnedFields()
        and base in SymmetricAlgebras(coefficient_base)
    )


class _CompleteIntersectionBaseChange(SageObject):
    r"""The selected source and scalar map defining one scalar base change."""

    def __init__(self, source, ring_map) -> None:
        self._source = source
        self._ring_map = ring_map
        if ring_map.domain() is not source.scheme_base_ring():
            raise ValueError(
                "a complete-intersection base-change datum starts at the source scalar base"
            )

    def source(self):
        return self._source

    def ring_map(self):
        return self._ring_map

    def projection(self, changed):
        r"""Return the projection from the selected base change to its source."""
        if changed.scheme_base_ring() is not self.ring_map().codomain():
            raise ValueError(
                "the changed complete intersection has the wrong scalar base for this datum"
            )
        changed_ambient = changed.complete_intersection_ambient()
        ambient_projection = changed_ambient.left_projection()
        into_source_ambient = ambient_projection * changed.inclusion()
        return _categorical_scheme_morphism(
            into_source_ambient.native_morphism(),
            domain=changed,
            codomain=self.source(),
        )


class _CompleteIntersectionAdjunctionComparison(SageObject):
    r"""The adjunction comparison ``omega_X ~= (omega_P tensor det N)_X``.

    Every line bundle in the comparison is an actual pullback ``O_X(d)``.
    The determinant of the normal bundle is ``O_X(sum d_i)`` for the selected
    regular sequence, while ``omega_P=O_P(-n-1)``.
    """

    def __init__(self, complete_intersection) -> None:
        self._scheme = complete_intersection
        ambient = complete_intersection.complete_intersection_ambient()
        normal_degree = sum(int(value) for value in complete_intersection.defining_degrees())
        canonical = complete_intersection.O(
            complete_intersection.adjunction_twist_degree()
        )
        ambient_canonical = ambient.canonical_line_bundle().restrict_to(
            complete_intersection
        )
        normal_determinant = complete_intersection.O(normal_degree)
        adjunction_target = ambient_canonical.tensor_product(normal_determinant)
        self._canonical = canonical
        self._ambient_canonical = ambient_canonical
        self._normal_determinant = normal_determinant
        self._target = adjunction_target
        self._isomorphism = canonical.canonical_isomorphism_to(adjunction_target)

    def scheme(self):
        return self._scheme

    def canonical_line_bundle(self):
        return self._canonical

    def restricted_ambient_canonical_bundle(self):
        return self._ambient_canonical

    def normal_determinant_line_bundle(self):
        return self._normal_determinant

    def adjunction_target(self):
        return self._target

    def isomorphism(self):
        return self._isomorphism

    def _repr_(self) -> str:
        return f"Adjunction comparison for {self.scheme()}: {self.canonical_line_bundle()} ~= {self.adjunction_target()}"



class ProjectiveCompleteIntersections(OwnedCategoryOverBaseRing):
    r"""Closed complete intersections over a field or polynomial parameter base.

    The selected homogeneous equations are part of the construction.  Over a
    field, and over a polynomial parameter algebra over a field, the homogeneous
    coordinate ring is regular.  There a family of
    ``r`` generators whose ideal has height ``r`` is a regular sequence, hence
    cuts out a complete intersection.  The represented criterion is therefore
    exactly ``number of selected equations == codimension``.
    """

    def an_object(self):
        plane = ProjectiveSpaces(self.base_ring())(2)
        x, y, z = plane.homogeneous_coordinate_generators()
        return self(plane.closed_subscheme(x * z - y**2))

    def _call_(self, subscheme, *, base_change_datum=None):
        r"""Place a projective closed subscheme with its selected regular sequence."""
        base = subscheme.scheme_base_ring()
        if base is not self.base_ring():
            raise ValueError("a complete intersection is placed over this category's base ring")
        if not _complete_intersection_base_supported(base):
            raise TypeError(
                "the represented complete-intersection criterion requires a field or a polynomial parameter algebra over a field"
            )
        if subscheme not in ClosedSubschemes(base):
            raise TypeError(
                "a projective complete intersection starts from a represented closed subscheme"
            )
        ambient = subscheme.inclusion().codomain()
        if ambient not in ProjectiveSpaces(base):
            raise TypeError(
                "the represented complete-intersection criterion requires projective-space ambient"
            )
        equations = tuple(subscheme.defining_equations())
        if not equations:
            raise ValueError(
                "select at least one homogeneous equation for this complete-intersection construction"
            )
        codimension = int(subscheme.codimension())
        if codimension != len(equations):
            raise ValueError(
                f"the selected {len(equations)} equations have codimension {codimension}, so they are not a regular sequence"
            )
        subscheme._preamble_complete_intersection_ambient = ambient
        subscheme._preamble_complete_intersection_degrees = tuple(
            int(equation.degree()) for equation in equations
        )
        if (
            base_change_datum is not None
            and base_change_datum.ring_map().codomain() is not base
        ):
            raise ValueError(
                "the complete-intersection base-change datum has the wrong target scalar base"
            )
        subscheme._complete_intersection_base_change_datum = base_change_datum
        return _refine_scheme(subscheme, base, [self])

    def _repr_object_names(self):
        return f"projective complete intersections over {self.base_ring()}"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring()), ClosedSubschemes(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        base = self.base_ring()
        return (
            candidate in ClosedSubschemes(base)
            and getattr(candidate, "_preamble_complete_intersection_ambient", None)
            in ProjectiveSpaces(base)
        )

    class ParentMethods:
        def is_complete_intersection(self) -> bool:
            return True

        def complete_intersection_ambient(self):
            return self._preamble_complete_intersection_ambient

        def defining_degrees(self):
            return finite_family(
                self._preamble_complete_intersection_degrees,
                name="Complete-intersection defining degrees",
            )

        def complete_intersection_codimension(self):
            return len(self._preamble_complete_intersection_degrees)

        def expected_dimension(self):
            return int(self.complete_intersection_ambient().relative_dimension()) - self.complete_intersection_codimension()

        def family_base_scheme(self):
            return self.base_scheme()

        def family_morphism(self):
            r"""Return the relative projective complete-intersection morphism to its base."""
            return self.structure_morphism()

        def base_change_datum(self):
            datum = self._complete_intersection_base_change_datum
            if datum is None:
                raise ValueError("this complete intersection was not selected as a scalar base change")
            return datum

        def base_change_source_complete_intersection(self):
            return self.base_change_datum().source()

        def base_change_projection(self):
            return self.base_change_datum().projection(self)

        def base_change(self, ring_map):
            r"""Base-change this complete-intersection family through its defining sections."""
            base = self.scheme_base_ring()
            if ring_map.domain() is not base:
                raise ValueError("a complete-intersection base change starts at its scalar base")
            ambient = self.complete_intersection_ambient()
            changed_ambient = ambient.base_change(ring_map)
            changed_equations = []
            defining_equations = tuple(self.defining_equations())
            for equation_position, equation in enumerate(defining_equations):
                degree = int(equation.degree())
                source_bundle = ambient.O(degree)
                source_sections = source_bundle.global_sections()
                source_ring = source_sections.homogeneous_coordinate_ring()
                raised = tuple(
                    self.homogeneous_defining_equations(source_ring)
                )[equation_position]
                source_section = source_sections.section_from_homogeneous_polynomial(raised)
                changed_bundle = source_bundle.base_change(ring_map)
                comparison = changed_bundle.section_base_change_comparison()
                changed_source = comparison.domain()
                target_ring = changed_source.base_ring()
                changed_source_section = changed_source.linear_combination(
                    {
                        label: target_ring(ring_map(coefficient))
                        for label, coefficient in source_sections.framing_coefficients(source_section).items()
                    }
                )
                target_section = comparison(changed_source_section)
                changed_equations.append(
                    changed_bundle.global_sections().homogeneous_polynomial(target_section)
                )

            datum = _CompleteIntersectionBaseChange(self, ring_map)
            return ProjectiveCompleteIntersections(ring_map.codomain())(
                changed_ambient.closed_subscheme(tuple(changed_equations)),
                base_change_datum=datum,
            )

        def adjunction_twist_degree(self):
            r"""Return ``sum(d_i) - n - 1`` in ``K_X = O_X(sum d_i-n-1)``.

            This is the integer in the projective complete-intersection
            adjunction formula.  The actual canonical bundle and comparison
            map are returned separately by :meth:`canonical_line_bundle` and
            :meth:`adjunction_isomorphism`.
            """
            ambient_dimension = int(self.complete_intersection_ambient().relative_dimension())
            return sum(self._preamble_complete_intersection_degrees) - ambient_dimension - 1

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
            singular_cone_dimension = int(self.Jacobian().dimension())
            return singular_cone_dimension <= dimension - 1

        def projective_degree(self):
            r"""Return the complete-intersection degree ``prod d_i``."""
            degree = 1
            for value in self._preamble_complete_intersection_degrees:
                degree *= int(value)
            return degree

        def anticanonical_twist_degree(self):
            r"""Return ``n + 1 - sum(d_i)`` for ``-K_X``."""
            return -self.adjunction_twist_degree()

        @cached_method
        def adjunction_comparison(self):
            return _CompleteIntersectionAdjunctionComparison(self)

        def adjunction_isomorphism(self):
            return self.adjunction_comparison().isomorphism()

        @cached_method
        def canonical_line_bundle(self):
            return self.adjunction_comparison().canonical_line_bundle()

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
            if self.scheme_base_ring() not in OwnedFields():
                raise TypeError("the del Pezzo predicate is a fibrewise projective-surface question over a field")
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
            r"""Return ``(-K_X)^2`` for a represented del Pezzo complete intersection."""
            if not self.is_del_pezzo():
                raise ValueError("the represented complete intersection is not a del Pezzo surface")
            coefficient = self.anticanonical_twist_degree()
            return coefficient**2 * self.projective_degree()


__all__ = [
    "ProjectiveCompleteIntersections",
]
