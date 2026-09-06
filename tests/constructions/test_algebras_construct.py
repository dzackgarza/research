r"""Algebra constructions a mathematician expects, over every named ring.

Polynomial, free, symmetric, exterior and tensor algebras, matrix algebras as
Lie algebras, presented algebras, Kähler differentials and the de Rham
complex: each asked over every ring in the catalogue for which the mathematics
defines it, with the values the definitions determine.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Free, symmetric, exterior and tensor algebras.
# ---------------------------------------------------------------------------


def test_free_algebra_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    free = FreeAlgebraOn(ring, ("a", "b"))
    a = free.algebra_generator("a")
    b = free.algebra_generator("b")

    assert free in Algebras(ring)
    assert free in FreeAlgebras(ring)
    assert free not in CommutativeAlgebras(ring)
    assert free not in CommutativeRings()
    assert a * b != b * a
    assert (a + b) * (a + b) == a * a + a * b + b * a + b * b
    assert free.algebra_generators().cardinality() == 2


def test_symmetric_algebra_is_the_polynomial_algebra(commutative_ring) -> None:
    ring = commutative_ring
    symmetric = SymmetricAlgebraOn(ring, ("x", "y"))
    x = symmetric.algebra_generator("x")
    y = symmetric.algebra_generator("y")

    assert symmetric in CommutativeAlgebras(ring)
    assert symmetric in SymmetricAlgebras(ring)
    assert symmetric in GradedAlgebras(ring)
    assert x * y == y * x
    assert (x + y) ** 2 == x**2 + 2 * x * y + y**2
    assert symmetric.graded_piece(2).module_rank() == 3
    assert symmetric.graded_piece(0).module_rank() == 1


def test_symmetric_algebra_of_a_free_module(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 3)
    symmetric = SymmetricAlgebraOf(module)
    assert symmetric in CommutativeAlgebras(ring)
    assert symmetric.free_source_module() is module
    assert symmetric.graded_piece(1).module_rank() == 3
    assert symmetric.graded_piece(2).module_rank() == 6


def test_exterior_algebra_of_a_free_module(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 3)
    exterior = AlternatingAlgebraOf(module)
    e0 = exterior.algebra_generator(0)
    e1 = exterior.algebra_generator(1)
    e2 = exterior.algebra_generator(2)

    assert exterior in AlternatingAlgebras(ring)
    assert exterior in StrictlyGradedCommutativeAlgebras(ring)
    assert exterior in GradedAlgebras(ring)
    assert e0 * e0 == exterior.zero()
    assert e0 * e1 == -(e1 * e0)
    assert e0 * e1 * e2 != exterior.zero()
    assert exterior.graded_piece(0).module_rank() == 1
    assert exterior.graded_piece(1).module_rank() == 3
    assert exterior.graded_piece(2).module_rank() == 3
    assert exterior.graded_piece(3).module_rank() == 1
    assert exterior.graded_piece(4).module_rank() == 0


def test_tensor_algebra_of_a_free_module(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    tensor = TensorAlgebraOf(module)
    a = tensor.algebra_generator(0)
    b = tensor.algebra_generator(1)

    assert tensor in TensorAlgebras(ring)
    assert tensor in Algebras(ring)
    assert tensor not in CommutativeAlgebras(ring)
    assert a * b != b * a
    assert tensor.graded_piece(2).module_rank() == 4
    assert tensor.graded_piece(3).module_rank() == 8


def test_polynomial_ring_is_a_commutative_algebra(commutative_ring) -> None:
    ring = commutative_ring
    polynomials = PolynomialRing(ring, ("x", "y"))
    assert polynomials in CommutativeAlgebras(ring)
    assert polynomials in Algebras(ring)
    assert polynomials.algebra_base_ring() is ring
    assert polynomials.algebra_structure_morphism()(ring.one()) == polynomials.one()


# ---------------------------------------------------------------------------
# Matrix algebras and Lie algebras.
# ---------------------------------------------------------------------------


def test_matrix_algebra_is_a_lie_algebra_under_the_commutator(commutative_ring) -> None:
    ring = commutative_ring
    matrices = MatrixSpace(ring, 2)
    e01 = matrices.matrix_unit(0, 1)
    e10 = matrices.matrix_unit(1, 0)

    assert matrices in CommutatorLieAlgebras(ring)
    assert matrices in LieAlgebras(ring)
    assert matrices.bracket(e01, e10) == e01 * e10 - e10 * e01
    assert matrices.bracket(e01, e01) == matrices.zero()
    h = matrices.bracket(e01, e10)
    assert matrices.bracket(h, e01) == 2 * e01
    assert matrices.bracket(h, e10) == -2 * e10


# ---------------------------------------------------------------------------
# Presented algebras.
# ---------------------------------------------------------------------------


def test_coordinate_axes_as_a_presented_algebra(field) -> None:
    plane = PolynomialRing(field, ("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = FinitelyPresentedAlgebra(plane, [x * y])
    xbar = axes.algebra_generator("x")
    ybar = axes.algebra_generator("y")

    assert axes in CommutativeAlgebras(field)
    assert axes in FinitelyPresentedAlgebras(field)
    assert xbar * ybar == axes.zero()
    assert xbar != axes.zero()
    assert xbar**2 != axes.zero()
    assert axes.krull_dimension() == 1
    assert axes.presentation_ring() is plane


# ---------------------------------------------------------------------------
# Kähler differentials.
# ---------------------------------------------------------------------------


def test_kahler_differentials_of_a_ring_over_itself_vanish(commutative_ring) -> None:
    r"""$\Omega_{R/R} = 0$."""
    omega = KahlerDifferentials(commutative_ring)
    assert omega in Modules(commutative_ring)
    assert omega.cardinality() == 1


def test_kahler_differentials_of_the_polynomial_algebra(commutative_ring) -> None:
    r"""$\Omega_{R[x,y]/R} = R[x,y]\,dx \oplus R[x,y]\,dy$ with $d(xy) = y\,dx + x\,dy$."""
    ring = commutative_ring
    polynomials = PolynomialRing(ring, ("x", "y"))
    x = polynomials.algebra_generator("x")
    y = polynomials.algebra_generator("y")
    omega = KahlerDifferentials(polynomials)
    d = omega.universal_derivation()
    dx = omega.differential_generator("x")
    dy = omega.differential_generator("y")

    assert omega in KahlerDifferentialModules(polynomials)
    assert omega in Modules(polynomials)
    assert omega.module_rank() == 2
    assert d(x) == dx
    assert d(x * y) == omega.scalar_multiple(y, dx) + omega.scalar_multiple(x, dy)
    assert d(x**3) == omega.scalar_multiple(3 * x**2, dx)
    assert d(polynomials(ring.one())) == omega.zero()


def test_kahler_differentials_of_a_separable_extension_vanish(build) -> None:
    for name, base in (("QQ(i)", QQ), ("QQ(cbrt2)", QQ), ("GF(4)", GF(2))):
        omega = KahlerDifferentials(build(name).as_algebra_over(base))
        assert omega.cardinality() == 1


@pytest.mark.parametrize(
    "name, discriminant",
    [("ZZ[i]", 4), ("ZZ[sqrt-5]", 20), ("ZZ[phi]", 5), ("ZZ[zeta5]", 125), ("ZZ[cbrt2]", 108)],
)
def test_kahler_differentials_of_a_ring_of_integers_have_the_order_of_the_discriminant(
    build, name, discriminant
) -> None:
    r"""$|\Omega_{\mathcal O_K/\mathbb Z}| = |d_K|$."""
    omega = KahlerDifferentials(build(name).as_algebra_over(ZZ))
    assert omega.cardinality() == discriminant


def test_kahler_differentials_of_a_rational_function_field(build) -> None:
    omega = KahlerDifferentials(build("QQ(x)").as_algebra_over(QQ))
    assert omega.module_rank() == 1
    assert omega.cardinality() == aleph0


def test_kahler_differentials_of_the_coordinate_axes(field) -> None:
    plane = PolynomialRing(field, ("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    axes = FinitelyPresentedAlgebra(plane, [x * y])
    xbar = axes.algebra_generator("x")
    ybar = axes.algebra_generator("y")
    omega = KahlerDifferentials(axes)
    dx = omega.differential_generator("x")
    dy = omega.differential_generator("y")

    assert omega.scalar_multiple(ybar, dx) + omega.scalar_multiple(xbar, dy) == omega.zero()
    assert omega.universal_derivation()(xbar * ybar) == omega.zero()
    assert dx != omega.zero()


# ---------------------------------------------------------------------------
# The de Rham complex.
# ---------------------------------------------------------------------------


def test_de_rham_complex_of_the_affine_line(field) -> None:
    polynomials = PolynomialRing(field, "x")
    x = polynomials.algebra_generator("x")
    de_rham = DeRhamAlgebra(polynomials)
    d = de_rham.differential()

    assert de_rham in StrictlyCommutativeDifferentialGradedAlgebras(field)
    assert de_rham.de_rham_source_algebra() is polynomials
    assert de_rham.kahler_differentials().module_rank() == 1
    assert d(d(de_rham(x))) == de_rham.zero()
    assert d(de_rham(x**2)) == 2 * de_rham(x) * d(de_rham(x))
    assert de_rham.graded_piece(2).module_rank() == 0


@pytest.mark.parametrize("name", ["QQ", "QQ(i)", "RR", "AA"])
def test_poincare_lemma_in_characteristic_zero(build, name) -> None:
    r"""$H^1_{dR}(\mathbb A^1_K) = 0$ and $H^0 = K$ when $\operatorname{char} K = 0$."""
    field = build(name)
    de_rham = DeRhamAlgebra(PolynomialRing(field, "x"))
    assert de_rham.cohomology(1).cardinality() == 1
    assert de_rham.cohomology(0).module_rank() == 1


@pytest.mark.parametrize("name", ["GF(5)", "GF(4)"])
def test_de_rham_cohomology_of_the_line_is_nonzero_in_positive_characteristic(build, name) -> None:
    r"""$x^{p-1}\,dx$ is closed and not exact over $\mathbb F_q$."""
    field = build(name)
    de_rham = DeRhamAlgebra(PolynomialRing(field, "x"))
    assert de_rham.cohomology(1).cardinality() != 1
    assert de_rham.cohomology(1).module_rank() >= 1


def test_de_rham_cohomology_of_the_integer_line_has_torsion() -> None:
    r"""$x\,dx$ is closed over $\mathbb Z$ and $2\,x\,dx = d(x^2)$, so $H^1$ has $2$-torsion."""
    de_rham = DeRhamAlgebra(PolynomialRing(ZZ, "x"))
    assert de_rham.cohomology(1).cardinality() != 1
    assert de_rham.cohomology(0).module_rank() == 1
