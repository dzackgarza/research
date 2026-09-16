r"""Projective curve normalizations and residue-weighted genus defects.

For a reduced integral projective curve ``C`` with finite normalization
``nu:C^nu -> C``, the normalization sequence

``0 -> O_C -> nu_* O_Cnu -> Q -> 0``

has ``Q`` supported at the nonnormal closed points.  Stacks Project, Tag
``0C1R``, identifies the stalk length with the local delta invariant.  Taking
Euler characteristics gives

``p_a(C) = g(C^nu) + sum_p delta_p [kappa(p):k]``

for the represented geometrically integral curves below.  The residue degree is
part of each contribution, so a nonrational closed point is not split into
geometric points and then counted as if each were rational.

The two supplied plane quintics have explicit normalization maps from ``P^1``.
Their local delta invariants are computed independently by Singular
``normal.lib::deltaLoc`` through :class:`IsolatedHypersurfaceSingularity`; the
global genus relation only checks that these local contributions exhaust the
normalization defect.
"""

from sage.misc.cachefunc import cached_method
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.schemes import (
    ProjectiveSpaces,
    Schemes,
)
from dzack_research.preamble.categories.schemes.singularities import (
    IsolatedHypersurfaceSingularity,
)
from dzack_research.preamble.categories.schemes.varieties import Curves
from dzack_research.preamble.categories.sets.finite_families import finite_family

_RATIONALS = _own_ring(SageQQ)


class CurveLocalDeltaContribution(SageObject):
    r"""One closed singular point with its local delta and residue degree."""

    def __init__(self, singularity, point, *, projective_support=None) -> None:
        if point.parent().ring() is not singularity.polynomial_ring():
            raise ValueError("a curve delta contribution uses a point of its local plane")
        self._singularity = singularity
        self._point = point
        self._projective_support = projective_support

    def singularity(self):
        return self._singularity

    def local_point(self):
        return self._point

    def projective_support(self):
        return self._projective_support

    @cached_method
    def delta_invariant(self):
        return self.singularity().delta_invariant_at(self.local_point())

    @cached_method
    def residue_degree(self):
        return self.local_point().residue_degree()

    @cached_method
    def weighted_contribution(self):
        return self.singularity().delta_contribution_over_base(self.local_point())

    def _repr_(self):
        return (
            f"delta={self.delta_invariant()} at {self.projective_support()!r} "
            f"with residue degree {self.residue_degree()}"
        )


class _CurveGenusComparison(SageObject):
    r"""The normalization-sequence equality between arithmetic and geometric genus."""

    def __init__(self, normalization_data) -> None:
        self._normalization_data = normalization_data
        if self.arithmetic_genus() != self.geometric_genus() + self.total_delta_contribution():
            raise ArithmeticError(
                "the selected local delta contributions do not exhaust the normalization genus defect"
            )

    def normalization_data(self):
        return self._normalization_data

    def arithmetic_genus(self):
        return self.normalization_data().curve().arithmetic_genus()

    def geometric_genus(self):
        return self.normalization_data().geometric_genus()

    def total_delta_contribution(self):
        return self.normalization_data().total_delta_contribution()

    def holds(self) -> bool:
        return True

    def _repr_(self) -> str:
        return f"Genus comparison: p_a={self.arithmetic_genus()}, g={self.geometric_genus()}, delta={self.total_delta_contribution()}"



class ProjectiveCurveNormalizationData(SageObject):
    r"""A selected projective normalization map and all of its local defects."""

    def __init__(
        self,
        curve,
        normalization_morphism,
        local_contributions,
    ) -> None:
        base = curve.scheme_base_ring()
        if curve not in Curves(base) or curve not in Schemes(base).Projective():
            raise TypeError("curve normalization data require a projective integral curve")
        if normalization_morphism.codomain() is not curve:
            raise ValueError("the normalization morphism must land in the selected curve")
        normalization = normalization_morphism.domain()
        if normalization not in Curves(base) or normalization not in Schemes(base).Projective():
            raise TypeError("the represented normalization must itself be a projective curve")
        contributions = tuple(local_contributions)
        if not contributions:
            raise ValueError("a singular curve normalization records its nonzero local defects")
        if normalization not in ProjectiveSpaces(base) or int(normalization.relative_dimension()) != 1:
            raise NotImplementedError(
                "the selected genus comparison currently certifies geometric integrality through an actual P^1 normalization"
            )
        self._curve = curve
        self._normalization_morphism = normalization_morphism
        self._local_contributions = contributions
        self._geometrically_integral = True
        self._connected_normalization = True
        curve._preamble_curve_normalization_data = self
        self.genus_comparison()

    def curve(self):
        return self._curve

    def normalization_morphism(self):
        return self._normalization_morphism

    def normalization_curve(self):
        return self.normalization_morphism().domain()

    def is_geometrically_integral(self) -> bool:
        return self._geometrically_integral

    def normalization_is_connected(self) -> bool:
        return self._connected_normalization

    def local_contributions(self):
        return finite_family(
            self._local_contributions,
            name="Local delta contributions of the projective curve normalization",
        )

    def total_delta_contribution(self):
        return sum(
            (int(contribution.weighted_contribution()) for contribution in self._local_contributions),
            0,
        )

    def geometric_genus(self):
        return self.normalization_curve().arithmetic_genus()

    @cached_method
    def genus_comparison(self):
        return _CurveGenusComparison(self)

    def _repr_(self) -> str:
        return f"Normalization data for {self.curve()} via {self.normalization_morphism()}"



def _projective_quintic_normalization(curve, coordinate_formula):
    r"""Corestrict one basepoint-free degree-five map ``P1 -> P2`` to ``curve``."""
    base = curve.scheme_base_ring()
    normalization = ProjectiveSpaces(base)(1, names=("s", "t"))
    ring = normalization.O(5).global_sections().homogeneous_coordinate_ring()
    s = ring.algebra_generator("s")
    t = ring.algebra_generator("t")
    ambient = curve.inclusion().codomain()
    coordinates = coordinate_formula(s, t)
    ambient_map = normalization.projective_morphism_from_coordinates(
        ambient,
        coordinates,
    )
    return curve.corestriction(ambient_map)


def _origin_contribution(equation, *, projective_support):
    plane = equation.parent()
    singularity = IsolatedHypersurfaceSingularity(plane, equation)
    point = plane.spectrum()(plane.ideal(*tuple(plane.algebra_generators())))
    return CurveLocalDeltaContribution(
        singularity,
        point,
        projective_support=projective_support,
    )


def rational_quintic_with_two_nodes_normalization():
    r"""Return a rational quintic with two affine nodes and one point at infinity.

    ``C: Y^2 Z^3 = X(X-Z)^2(X-4Z)^2`` has the normalization

    ``[s:t] |-> [s^2 t^3 : s(s^2-t^2)(s^2-4t^2) : t^5]``.
    """
    plane = ProjectiveSpaces(_RATIONALS)(2, names=("X", "Y", "Z"))
    ring = plane.O(5).global_sections().homogeneous_coordinate_ring()
    X = ring.algebra_generator("X")
    Y = ring.algebra_generator("Y")
    Z = ring.algebra_generator("Z")
    curve = Curves(_RATIONALS).from_equation(
        Y**2 * Z**3 - X * (X - Z) ** 2 * (X - 4 * Z) ** 2,
        plane,
    )
    normalization = _projective_quintic_normalization(
        curve,
        lambda s, t: (
            s**2 * t**3,
            s * (s**2 - t**2) * (s**2 - 4 * t**2),
            t**5,
        ),
    )

    local = _RATIONALS.polynomial_ring(("u", "v"))
    u, v = tuple(local.algebra_generators())
    first = _origin_contribution(
        v**2 - (u + 1) * u**2 * (u - 3) ** 2,
        projective_support=(1, 0, 1),
    )
    second = _origin_contribution(
        v**2 - (u + 4) * (u + 3) ** 2 * u**2,
        projective_support=(4, 0, 1),
    )
    infinity = _origin_contribution(
        v**3 - u * (u - v) ** 2 * (u - 4 * v) ** 2,
        projective_support=(0, 1, 0),
    )
    return ProjectiveCurveNormalizationData(
        curve,
        normalization,
        (first, second, infinity),
    )


def rational_quintic_with_nonrational_node_normalization():
    r"""Return a rational quintic with one degree-two singular closed point.

    ``C: Y^2 Z^3 = X(X^2+Z^2)^2`` is normalized by

    ``[s:t] |-> [s^2 t^3 : s(s^4+t^4) : t^5]``.

    On ``Z=1`` the singular prime ``(x^2+1,y)`` has residue degree two.  Its
    local delta is one at each conjugate geometric point, so the one closed
    point contributes ``2`` over ``QQ``; it is never expanded into two entries.
    """
    plane = ProjectiveSpaces(_RATIONALS)(2, names=("X", "Y", "Z"))
    ring = plane.O(5).global_sections().homogeneous_coordinate_ring()
    X = ring.algebra_generator("X")
    Y = ring.algebra_generator("Y")
    Z = ring.algebra_generator("Z")
    curve = Curves(_RATIONALS).from_equation(
        Y**2 * Z**3 - X * (X**2 + Z**2) ** 2,
        plane,
    )
    normalization = _projective_quintic_normalization(
        curve,
        lambda s, t: (
            s**2 * t**3,
            s * (s**4 + t**4),
            t**5,
        ),
    )

    affine = _RATIONALS.polynomial_ring(("x", "y"))
    x, y = tuple(affine.algebra_generators())
    affine_singularity = IsolatedHypersurfaceSingularity(
        affine,
        y**2 - x * (x**2 + 1) ** 2,
    )
    nonrational_point = affine.spectrum()(affine.ideal(x**2 + 1, y))
    nonrational = CurveLocalDeltaContribution(
        affine_singularity,
        nonrational_point,
        projective_support="V(X^2+Z^2,Y) on Z != 0",
    )

    infinity_ring = _RATIONALS.polynomial_ring(("x", "z"))
    x_inf, z_inf = tuple(infinity_ring.algebra_generators())
    infinity = _origin_contribution(
        z_inf**3 - x_inf * (x_inf**2 + z_inf**2) ** 2,
        projective_support=(0, 1, 0),
    )
    return ProjectiveCurveNormalizationData(
        curve,
        normalization,
        (nonrational, infinity),
    )


__all__ = [
    "CurveLocalDeltaContribution",
    "ProjectiveCurveNormalizationData",
    "rational_quintic_with_nonrational_node_normalization",
    "rational_quintic_with_two_nodes_normalization",
]
