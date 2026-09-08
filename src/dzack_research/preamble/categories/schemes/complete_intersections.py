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
            return True


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
