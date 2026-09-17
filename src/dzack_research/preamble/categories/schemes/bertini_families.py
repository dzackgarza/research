r"""A Bertini application with an actual smooth locus and exceptional member.

The Hesse pencil on ``P^2`` is spanned by

``x^3+y^3+z^3`` and ``xyz``.

On the affine parameter chart used here the family is
``x^3+y^3+z^3-3txyz=0``.  In characteristic zero the Jacobian equations have a
projective solution exactly when ``t^3=1``.  Thus the theorem's conclusion is
the represented open ``D(t^3-1)`` in the parameter scheme, not a claim that
every member is smooth.  The fibre ``t=0`` is the Fermat cubic and is smooth;
``t=1`` is an explicit singular member of the same family.

The pencil has base points.  One rational base point ``[1:-1:0]`` is retained
with its actual value and first-jet evaluation maps, so the application keeps
the base-locus hypothesis visible rather than silently treating the pencil as
basepoint free.
"""

from sage.misc.cachefunc import cached_method
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.complete_intersections import (
    ProjectiveCompleteIntersections,
)
from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces


class HesseBertiniFamily(SageObject):
    r"""The Hesse cubic pencil with its exact good and exceptional parameter loci."""

    def __init__(self) -> None:
        base = _own_ring(SageQQ)
        parameter = base.polynomial_ring("t")
        t = parameter.algebra_generator("t")
        plane = ProjectiveSpaces(parameter)(2, names=("x", "y", "z"))
        relative_sections = plane.O(3).global_sections()
        relative_ring = relative_sections.homogeneous_coordinate_ring()
        x = relative_ring.algebra_generator("x")
        y = relative_ring.algebra_generator("y")
        z = relative_ring.algebra_generator("z")
        scalar = relative_ring.algebra_structure_morphism()
        equation = x**3 + y**3 + z**3 - scalar(parameter(3) * t) * x * y * z
        family = ProjectiveCompleteIntersections(plane.scheme_base_ring())(plane, equation)

        reference_plane = ProjectiveSpaces(base)(2, names=("x", "y", "z"))
        bundle = reference_plane.O(3)
        sections = bundle.global_sections()
        ring = sections.homogeneous_coordinate_ring()
        rx = ring.algebra_generator("x")
        ry = ring.algebra_generator("y")
        rz = ring.algebra_generator("z")
        fermat = sections.section_from_homogeneous_polynomial(rx**3 + ry**3 + rz**3)
        product = sections.section_from_homogeneous_polynomial(rx * ry * rz)
        linear_system = bundle.linear_system((fermat, product))
        basepoint = reference_plane.point_morphism((base.one(), -base.one(), base.zero()))
        base_locus_point = linear_system.base_locus().corestriction(basepoint)
        value_evaluation = bundle.jet_evaluation(basepoint, 1)
        first_jet_evaluation = bundle.jet_evaluation(basepoint, 2)
        if any(
            value_evaluation(section) != value_evaluation.codomain().zero()
            for section in (fermat, product)
        ):
            raise ArithmeticError("the selected Hesse point is not a base point of the pencil")

        discriminant = t**3 - parameter.one()
        parameter_scheme = family.base_scheme()
        good_locus = parameter_scheme.distinguished_open(discriminant)
        exceptional_locus = parameter_scheme.closed_subscheme(discriminant)

        self._base_ring = base
        self._parameter_ring = parameter
        self._parameter = t
        self._family = family
        self._reference_plane = reference_plane
        self._line_bundle = bundle
        self._linear_system = linear_system
        self._fermat_section = fermat
        self._product_section = product
        self._basepoint = basepoint
        self._base_locus_point = base_locus_point
        self._value_evaluation = value_evaluation
        self._first_jet_evaluation = first_jet_evaluation
        self._discriminant = discriminant
        self._good_locus = good_locus
        self._exceptional_locus = exceptional_locus

    def base_ring(self):
        return self._base_ring

    def parameter_ring(self):
        return self._parameter_ring

    def parameter(self):
        return self._parameter

    def parameter_scheme(self):
        return self.family().base_scheme()

    def family(self):
        return self._family

    def family_morphism(self):
        return self.family().family_morphism()

    def linear_system(self):
        return self._linear_system

    def base_locus(self):
        return self.linear_system().base_locus()

    def basepoint(self):
        return self._basepoint

    def base_locus_point(self):
        return self._base_locus_point

    def basepoint_value_evaluation(self):
        return self._value_evaluation

    def basepoint_first_jet_evaluation(self):
        return self._first_jet_evaluation

    def discriminant(self):
        return self._discriminant

    def good_parameter_locus(self):
        r"""Return ``D(t^3-1)``, exactly the smooth-fibre locus on this chart."""
        return self._good_locus

    def exceptional_parameter_locus(self):
        r"""Return ``V(t^3-1)``, the singular-fibre locus on this chart."""
        return self._exceptional_locus

    def parameter_is_good(self, value) -> bool:
        value = self.base_ring()(value)
        return value**3 != self.base_ring().one()

    def fiber(self, value):
        value = self.base_ring()(value)
        specialization = self.parameter_ring().Mor(self.base_ring())(
            {"t": value}
        )
        return self.family().base_change(specialization)

    @cached_method
    def general_member(self):
        return self.fiber(self.base_ring().zero())

    @cached_method
    def exceptional_member(self):
        return self.fiber(self.base_ring().one())

    @cached_method
    def restriction_to_good_locus(self):
        ring_map = self.good_parameter_locus().inclusion().coordinate_algebra_morphism()
        return self.family().base_change(ring_map)

    def good_locus_restriction_map(self):
        return self.restriction_to_good_locus().base_change_projection()

    def theorem_hypotheses(self) -> bool:
        r"""The selected Hesse/Bertini calculation uses characteristic zero."""
        return int(self.base_ring().characteristic()) == 0

    def theorem_conclusion_is_exact(self) -> bool:
        r"""Record the computed conclusion without upgrading it to every fibre."""
        return (
            self.theorem_hypotheses()
            and self.parameter_is_good(self.base_ring().zero())
            and not self.parameter_is_good(self.base_ring().one())
        )

    def _repr_(self) -> str:
        return f"Hesse-Bertini family over {self.parameter_ring()} with good locus {self.good_parameter_locus()}"



def hesse_bertini_family():
    return HesseBertiniFamily()


__all__ = ["HesseBertiniFamily", "hesse_bertini_family"]
