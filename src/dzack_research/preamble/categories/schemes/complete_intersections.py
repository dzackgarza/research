r"""Projective complete intersections with their selected defining multidegree."""

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ClosedSubschemes,
    ProjectiveSchemes,
    ProjectiveSpaces,
    ProjectiveSpace,
    refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family


class ProjectiveCompleteIntersections(OwnedCategoryOverBaseRing):
    r"""Closed complete intersections in projective space over a field.

    The selected homogeneous equations are part of the construction.  In the
    regular homogeneous coordinate ring of projective space, a family of
    ``r`` generators whose ideal has height ``r`` is a regular sequence, hence
    cuts out a complete intersection.  The represented criterion is therefore
    exactly ``number of selected equations == codimension``.
    """

    def an_object(self):
        plane = ProjectiveSpace(2, self.base_ring())
        x, y, z = plane.gens()
        return ProjectiveCompleteIntersection(plane.closed_subscheme(x * z - y**2))

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

        def adjunction_twist_degree(self):
            r"""Return ``sum(d_i) - n - 1`` in ``K_X = O_X(sum d_i-n-1)``.

            This is the integer in the projective complete-intersection
            adjunction formula.  It is deliberately kept distinct from an
            actual line bundle until arbitrary projective closed subschemes
            support restriction of ``O(d)``.
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
            if int(_engine_ring(base).characteristic()) != 0:
                raise NotImplementedError(
                    "the represented complete-intersection normality criterion currently requires characteristic zero"
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

        def is_del_pezzo(self) -> bool:
            r"""Decide the del Pezzo condition for a smooth complete-intersection surface.

            In this represented regime ``-K_X = O_X(c)`` with
            ``c = n+1-sum(d_i)``.  The restriction of ``O(1)`` is ample, so
            ``-K_X`` is ample exactly when ``c > 0``.  Smoothness is decided
            by Sage's exact projective-subscheme Jacobian calculation.
            """
            if int(self.expected_dimension()) != 2:
                return False
            if not bool(self.is_smooth()):
                return False
            return self.anticanonical_twist_degree() > 0

        def del_pezzo_degree(self):
            r"""Return ``(-K_X)^2`` for a represented del Pezzo complete intersection."""
            if not self.is_del_pezzo():
                raise ValueError("the represented complete intersection is not a del Pezzo surface")
            coefficient = self.anticanonical_twist_degree()
            return coefficient**2 * self.projective_degree()


def ProjectiveCompleteIntersection(subscheme):
    r"""Place a projective closed subscheme at its selected complete-intersection owner."""
    base = subscheme.scheme_base_ring()
    if not bool(_engine_ring(base).is_field()):
        raise TypeError("the represented projective complete-intersection criterion currently requires a field base")
    if subscheme not in ClosedSubschemes(base):
        raise TypeError("a projective complete intersection starts from a represented closed subscheme")
    ambient = subscheme.inclusion().codomain()
    if ambient not in ProjectiveSpaces(base):
        raise TypeError("the represented complete-intersection criterion requires projective-space ambient")
    equations = tuple(subscheme.defining_equations())
    if not equations:
        raise ValueError("select at least one homogeneous equation for this complete-intersection construction")
    codimension = int(subscheme.codimension())
    if codimension != len(equations):
        raise ValueError(
            f"the selected {len(equations)} equations have codimension {codimension}, so they are not a regular sequence"
        )
    subscheme._preamble_complete_intersection_ambient = ambient
    subscheme._preamble_complete_intersection_degrees = tuple(int(equation.degree()) for equation in equations)
    return refine_scheme(subscheme, base, [ProjectiveCompleteIntersections(base)])


__all__ = ["ProjectiveCompleteIntersection", "ProjectiveCompleteIntersections"]
