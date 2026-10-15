r"""A Bertini application with an actual smooth locus and exceptional member.

The Hesse pencil on ``P^2`` is spanned by

``x^3+y^3+z^3`` and ``xyz``.

On the affine parameter chart used here the family is
``x^3+y^3+z^3-3txyz=0``.  In characteristic zero the Jacobian equations have a
projective solution exactly when ``t^3=1``.  Thus the theorem's conclusion is
the represented open ``D(t^3-1)`` in the parameter scheme, not a claim that
every member is smooth.  The fibre ``t=0`` is the Fermat cubic and is smooth;
``t=1`` is an explicit singular member of the same family.

The family is an object of the slice ``Sch_T/Spec T`` over the parameter
ring ``T = QQ[t]``: the cubic ``X`` with its structure morphism
``X -> Spec T``.

The pencil has base points.  One rational base point ``[1:-1:0]`` is retained
with its actual value and first-jet evaluation maps, so the application keeps
the base-locus hypothesis visible rather than silently treating the pencil as
basepoint free.
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.rings.ring_foundation import _owned_rationals
from dzack_research.preamble.categories.schemes.complete_intersections import (
    ProjectiveCompleteIntersections,
)
from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces
from dzack_research.preamble.validation import validator


class _HessePencil:
    r"""Private realization of the Hesse family as an object of ``Sch_T/Spec T``.

    The slice object itself retains the family ``X -> Spec T``.  This engine
    adds the pencil on the reference plane ``P^2_QQ`` that the family
    specializes, with its selected base point.
    """

    def __init__(
        self,
        *,
        base_field,
        parameter,
        line_bundle,
        linear_system,
        fermat_section,
        product_section,
        basepoint,
        **rest,
    ) -> None:
        self._base_field = base_field
        self._parameter = parameter
        self._line_bundle = line_bundle
        self._linear_system = linear_system
        self._fermat_section = fermat_section
        self._product_section = product_section
        self._basepoint = basepoint
        super().__init__(**rest)

    def base_field(self):
        return self._base_field

    def parameter_ring(self):
        return self.parameter_scheme().coordinate_algebra()

    def parameter(self):
        return self._parameter

    def parameter_scheme(self):
        return self.arrow().codomain()

    def family(self):
        return self.arrow().domain()

    def linear_system(self):
        return self._linear_system

    def base_locus(self):
        return self.linear_system().base_locus()

    def basepoint(self):
        return self._basepoint

    @cached_method
    def base_locus_point(self):
        return self.base_locus().corestriction(self.basepoint())

    @cached_method
    def basepoint_value_evaluation(self):
        return self._line_bundle.jet_evaluation(self.basepoint(), 1)

    @cached_method
    def basepoint_first_jet_evaluation(self):
        return self._line_bundle.jet_evaluation(self.basepoint(), 2)

    @validator
    def validate_basepoint(self) -> None:
        r"""Check that ``[1:-1:0]`` is a base point: both spanning sections vanish there."""
        evaluation = self.basepoint_value_evaluation()
        for section in (self._fermat_section, self._product_section):
            if evaluation(section) != evaluation.codomain().zero():
                raise ValueError(
                    f"the point {self.basepoint()} of {self.basepoint().codomain()} is not a base "
                    f"point of the Hesse pencil: the section {section} does not vanish there"
                )

    def discriminant(self):
        t = self.parameter()
        return t**3 - self.parameter_ring().one()

    @cached_method
    def good_parameter_locus(self):
        r"""Return ``D(t^3-1)``, exactly the smooth-fibre locus on this chart."""
        return self.parameter_scheme().distinguished_open(self.discriminant())

    @cached_method
    def exceptional_parameter_locus(self):
        r"""Return ``V(t^3-1)``, the singular-fibre locus on this chart."""
        return self.parameter_scheme().closed_subscheme(self.discriminant())

    def parameter_is_good(self, value) -> bool:
        value = self.base_field()(value)
        return value**3 != self.base_field().one()

    def member(self, value):
        r"""The member over the rational point ``t = value``: the base change of ``X`` along ``T -> QQ``, ``t |-> value``."""
        value = self.base_field()(value)
        specialization = self.parameter_ring().Mor(self.base_field())(
            {"t": value}
        )
        return self.family().base_change(specialization)

    @cached_method
    def general_member(self):
        return self.member(self.base_field().zero())

    @cached_method
    def exceptional_member(self):
        return self.member(self.base_field().one())

    @cached_method
    def restriction_to_good_locus(self):
        ring_map = self.good_parameter_locus().inclusion().coordinate_algebra_morphism()
        return self.family().base_change(ring_map)

    def good_locus_restriction_map(self):
        return self.restriction_to_good_locus().base_change_projection()

    def theorem_hypotheses(self) -> bool:
        r"""The selected Hesse/Bertini calculation uses characteristic zero."""
        return int(self.base_field().characteristic()) == 0

    def theorem_conclusion_is_exact(self) -> bool:
        r"""Record the computed conclusion without upgrading it to every fibre."""
        return (
            self.theorem_hypotheses()
            and self.parameter_is_good(self.base_field().zero())
            and not self.parameter_is_good(self.base_field().one())
        )

    def _repr_(self) -> str:
        return f"Hesse-Bertini family over {self.parameter_ring()} with good locus {self.good_parameter_locus()}"


def HesseBertiniFamily(check=False):
    r"""Return the Hesse cubic pencil as an object of ``Sch_T/Spec T`` for ``T = QQ[t]``.

    The object is the cubic ``X = V(x^3+y^3+z^3-3txyz) <= P^2_T`` with its
    structure morphism ``X -> Spec T``, together with the pencil
    ``<x^3+y^3+z^3, xyz> <= H^0(P^2_QQ, O(3))`` and its base point
    ``[1:-1:0]``.
    """
    base = _owned_rationals()
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

    pencil = family.scheme_category().slice_category().object(
        family.structure_morphism(),
        _engine=_HessePencil,
        construction_data={
            "base_field": base,
            "parameter": t,
            "line_bundle": bundle,
            "linear_system": bundle.linear_system((fermat, product)),
            "fermat_section": fermat,
            "product_section": product,
            "basepoint": reference_plane.point_morphism((base.one(), -base.one(), base.zero())),
        },
    )
    pencil.validate_basepoint(check=check)
    return pencil


__all__ = ["HesseBertiniFamily"]
