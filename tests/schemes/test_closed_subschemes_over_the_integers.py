r"""Cutting a hypersurface out of the affine plane over a base that is not a field.

A closed subobject of ``Spec A`` is ``Spec(A/I)`` presented by the equations
that cut it out, and building it needs the quotient, not a module
presentation of ``I``.  The parabola below is cut out over the integers,
where the presentation of the ideal as a module has no backend; that
presentation is a separate question, asked only when the owned ideal is.
"""

from dzack_research.preamble.all import (
    AffineSpace,
    ClosedEmbeddings,
    QQ,
    ZZ,
)


def _parabola_in_the_plane_over(ring):
    plane = AffineSpace(2, ring, names=("x", "y"))
    algebra = plane.coordinate_ring()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")
    equation = y - x**2
    return plane, equation, plane.closed_subscheme(equation)


def test_the_parabola_is_cut_out_of_the_affine_plane_over_the_integers() -> None:
    plane, equation, parabola = _parabola_in_the_plane_over(ZZ)

    assert parabola in ClosedEmbeddings(plane)
    assert parabola.inclusion().codomain() is plane
    assert parabola.defining_equations().cardinality() == 1
    # The equation vanishes on the subscheme: that is what cutting it out means.
    assert parabola.inclusion().coordinate_algebra_morphism()(equation).is_zero()


def test_the_defining_ideal_is_derived_from_the_equations_when_it_is_asked_for() -> None:
    r"""A hypersurface in the plane has codimension one, read off that ideal."""
    _plane, _equation, parabola = _parabola_in_the_plane_over(QQ)

    assert parabola.codimension() == 1
