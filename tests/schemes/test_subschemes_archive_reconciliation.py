r"""Archive reconciliation for equation-defined closed subschemes.

The archived ``EquationDefinedClosedSubscheme(X, equations)`` was a parallel
wrapper around the mathematical datum of a closed immersion cut out by chosen
equations.  The live owner is instead the subobject construction
``X.closed_subscheme(*equations)``: the returned scheme itself retains its
closed immersion, the selected equation family and the corresponding ideal.
These specimens retain the archive mathematics without reviving that wrapper.
"""

from dzack_research.preamble.all import (
    QQ,
    AffineSpace,
    ClosedEmbeddings,
    ClosedSubschemes,
    ProjectiveSpace,
    Schemes,
)


def test_affine_equation_defined_subscheme_is_the_live_closed_subobject() -> None:
    plane = AffineSpace(2, QQ, names=("x", "y"))
    x, y = plane.coordinate_ring().algebra_generators()
    parabola = plane.closed_subscheme(y - x**2)

    assert parabola in Schemes(QQ)
    assert parabola in ClosedSubschemes(QQ)
    assert parabola in ClosedEmbeddings(plane)
    assert parabola.inclusion().domain() is parabola
    assert parabola.inclusion().codomain() is plane
    equations = parabola.defining_equations()
    assert equations.cardinality() == 1
    assert equations[0] == y - x**2
    assert parabola.defining_ideal_owned().contains(y - x**2)
    assert parabola.codimension() == 1


def test_projective_hypersurface_retains_its_homogeneous_equation_and_embedding() -> None:
    projective_plane = ProjectiveSpace(2, QQ, names=("x", "y", "z"))
    x, y, z = projective_plane.coordinate_ring().algebra_generators()
    conic = projective_plane.closed_subscheme(x * z - y**2)

    assert conic in ClosedSubschemes(QQ)
    assert conic in ClosedEmbeddings(projective_plane)
    assert conic.inclusion().codomain() is projective_plane
    equations = conic.defining_equations()
    assert equations.cardinality() == 1
    assert equations[0] == x * z - y**2
    assert conic.codimension() == 1


def test_scheme_theoretic_intersection_is_cut_out_by_the_sum_of_equation_ideals() -> None:
    affine = AffineSpace(2, QQ, names=("x", "y"))
    x, y = affine.coordinate_ring().algebra_generators()
    horizontal = affine.closed_subscheme(y)
    vertical = affine.closed_subscheme(x)

    origin = horizontal.intersection(vertical)

    assert origin in ClosedEmbeddings(affine)
    assert origin.inclusion().codomain() is affine
    assert tuple(origin.defining_equations()) == (y, x)
    ideal = origin.defining_ideal_owned()
    assert ideal.contains(x)
    assert ideal.contains(y)
    assert origin.codimension() == 2
