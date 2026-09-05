r"""Cochain complexes, connections and Cartan calculus a mathematician expects.

The Koszul complex of $(x, y)$ over every field, cycles, boundaries and
cohomology as functors, connections on a free module and their curvature,
vector fields, interior products, Lie derivatives and the Cartan formula,
derivations, and de Rham cohomology of the punctured line.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


def _koszul_complex(ring):
    r"""$0 \to A \xrightarrow{(x,y)} A^2 \xrightarrow{(-y, x)} A \to 0$ for $A = R[x, y]$."""
    plane = PolynomialRing(ring, ("x", "y"))
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")
    first = FreeModule(plane, 1)
    middle = FreeModule(plane, 2)
    last = FreeModule(plane, 1)
    d0 = first.Mor(middle)({0: x * middle.module_generator(0) + y * middle.module_generator(1)})
    d1 = middle.Mor(last)({0: -y * last.module_generator(0), 1: x * last.module_generator(0)})
    return plane, CochainComplexes(plane)({0: first, 1: middle, 2: last}, {0: d0, 1: d1})


def test_the_koszul_complex_of_a_regular_sequence(field) -> None:
    plane, koszul = _koszul_complex(field)
    assert koszul in CochainComplexes(plane)
    assert koszul in GradedModules(plane)
    assert koszul.differential().degree_shift() == 1
    assert koszul.cohomology(0).cardinality() == 1
    assert koszul.cohomology(1).cardinality() == 1
    assert koszul.cohomology(2).cardinality() == field.cardinality()
    assert koszul.cycles(1).rank() == 1
    assert koszul.boundaries(1).rank() == 1
    assert koszul.cycles(1) == koszul.boundaries(1)
    assert cohomology_functor(plane, 2)(koszul) == koszul.cohomology(2)
    assert CochainComplexes(plane).underlying_graded_module()(koszul) in GradedModules(plane)


def test_the_koszul_complex_over_the_integers() -> None:
    plane, koszul = _koszul_complex(ZZ)
    assert koszul.cohomology(1).cardinality() == 1
    assert koszul.cohomology(2).rank() == 1
    assert koszul.cohomology(2).annihilator() == plane.ideal(plane.algebra_generator("x"), plane.algebra_generator("y"))


def test_cochain_morphisms_and_the_identity() -> None:
    _, koszul = _koszul_complex(QQ)
    homset = cochain_homset(koszul, koszul)
    identity = homset.identity()
    assert identity * identity == identity
    assert identity.domain() is koszul
    assert koszul.Mor(koszul).identity() == identity


def test_a_complex_with_nonzero_d_squared_is_refused() -> None:
    line = FreeModule(ZZ, 1)
    doubling = line.Mor(line)({0: 2 * line.module_generator(0)})
    with pytest.raises((ValueError, AssertionError)):
        CochainComplexes(ZZ)({0: line, 1: line, 2: line}, {0: doubling, 1: doubling})


def test_a_cochain_complex_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    line = FreeModule(ring, 1)
    doubling = line.Mor(line)({0: 2 * line.module_generator(0)})
    complex_ = CochainComplexes(ring)({0: line, 1: line}, {0: doubling})
    assert complex_ in CochainComplexes(ring)
    assert complex_.cohomology(1).cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality()
    assert complex_.cohomology(0).rank() == (1 if ring(2) == ring.zero() else 0)


# ---------------------------------------------------------------------------
# Connections.
# ---------------------------------------------------------------------------


def test_connections_on_a_free_module_over_the_affine_line(field) -> None:
    line = PolynomialRing(field, "x")
    module = FreeModule(line, 1)
    connections = Connections(module)
    omega = KahlerDifferentials(line)
    target = connections.target_module()
    dx = omega.differential_generator("x")
    e = module.module_generator(0)

    trivial = connections(lambda label: target.zero())
    twisted = connections(lambda label: target.pure_tensor(e, dx))
    assert trivial.is_flat()
    assert twisted.is_flat()
    assert trivial.module() is module
    assert trivial.algebra() is line
    with_connection = ModuleWithConnection(twisted)
    assert with_connection in ModulesWithConnection(line)
    assert with_connection in ModulesWithFlatConnection(line)
    assert with_connection.connection() is twisted
    assert with_connection.is_flat_connection()


def test_curvature_of_a_connection_on_the_plane(field) -> None:
    r"""$\nabla = d + x\,dy$ on the trivial line bundle has curvature $dx \wedge dy \ne 0$."""
    plane = PolynomialRing(field, ("x", "y"))
    x = plane.algebra_generator("x")
    module = FreeModule(plane, 1)
    connections = Connections(module)
    omega = KahlerDifferentials(plane)
    target = connections.target_module()
    dy = omega.differential_generator("y")
    e = module.module_generator(0)

    curved = connections(lambda label: target.pure_tensor(e, omega.scalar_multiple(x, dy)))
    flat = connections(lambda label: target.pure_tensor(e, dy))
    assert not curved.is_flat()
    assert flat.is_flat()
    assert curved.curvature_on_generator(0) != curved.curvature_target().zero()
    assert flat.curvature_on_generator(0) == flat.curvature_target().zero()
    assert ModuleWithConnection(curved) in ModulesWithConnection(plane)
    assert ModuleWithConnection(curved) not in ModulesWithFlatConnection(plane)


# ---------------------------------------------------------------------------
# Cartan calculus.
# ---------------------------------------------------------------------------


def _plane_calculus(field):
    plane = PolynomialRing(field, ("x", "y"))
    values = plane.regular_module()
    fields_ = VectorFields(plane)
    x = plane.algebra_generator("x")
    y = plane.algebra_generator("y")

    def field_of(a, b):
        return fields_({"x": values.scalar_multiple(a, values.module_generator(0)), "y": values.scalar_multiple(b, values.module_generator(0))})

    return plane, x, y, field_of


def test_vector_fields_and_lie_brackets(field) -> None:
    plane, x, y, field_of = _plane_calculus(field)
    d_dx = field_of(plane.one(), plane.zero())
    d_dy = field_of(plane.zero(), plane.one())
    x_d_dy = field_of(plane.zero(), x)
    y_d_dx = field_of(y, plane.zero())

    assert d_dx(x) == plane.one()
    assert d_dx(y) == plane.zero()
    assert d_dx(x * y) == y
    assert LieBracket(d_dx, d_dy)(x * y) == plane.zero()
    assert LieBracket(d_dx, x_d_dy)(y) == plane.one()
    assert LieBracket(d_dx, x_d_dy)(x) == plane.zero()
    euler = LieBracket(y_d_dx, x_d_dy)
    assert euler(x) == -x
    assert euler(y) == y
    assert Derivations(plane, plane.regular_module()).rank() == 2
    assert d_dx in Derivations(plane, plane.regular_module())


def test_interior_products_lie_derivatives_and_the_cartan_formula(field) -> None:
    plane, x, y, field_of = _plane_calculus(field)
    de_rham = DeRhamAlgebra(plane)
    d = de_rham.differential()
    dx = de_rham(KahlerDifferentials(plane).differential_generator("x"))
    dy = de_rham(KahlerDifferentials(plane).differential_generator("y"))
    d_dx = field_of(plane.one(), plane.zero())
    x_d_dy = field_of(plane.zero(), x)

    assert InteriorProduct(d_dx)(dx) == de_rham.one()
    assert InteriorProduct(d_dx)(dy) == de_rham.zero()
    assert InteriorProduct(d_dx)(dx * dy) == dy
    assert InteriorProduct(x_d_dy)(dy) == de_rham(x)
    assert LieDerivative(d_dx)(de_rham(x)) == de_rham.one()
    assert LieDerivative(d_dx)(dx) == de_rham.zero()
    assert LieDerivative(x_d_dy)(dy) == dx
    form = de_rham(y) * dx
    assert LieDerivative(d_dx)(form) == d(InteriorProduct(d_dx)(form)) + InteriorProduct(d_dx)(d(form))
    assert LieDerivative(x_d_dy)(form) == d(InteriorProduct(x_d_dy)(form)) + InteriorProduct(x_d_dy)(d(form))
    assert d(d(form)) == de_rham.zero()
    assert dx * dy == -(dy * dx)


def test_de_rham_cohomology_of_the_punctured_line(field) -> None:
    r"""$H^1_{dR}(\mathbb G_m) $ is spanned by $dx/x$ in characteristic zero."""
    laurent = LaurentPolynomialRing(field, "x")
    de_rham = DeRhamAlgebra(laurent)
    cohomology = CohomologyAlgebra(de_rham)
    assert cohomology in CohomologyAlgebras(field)
    assert de_rham.cohomology(0).rank() == 1
    if field.characteristic() == 0:
        assert de_rham.cohomology(1).rank() == 1
        assert de_rham.cohomology(2).cardinality() == 1
    else:
        assert de_rham.cohomology(1).rank() >= 1


def test_the_regular_dg_module_of_a_dga(field) -> None:
    de_rham = DeRhamAlgebra(PolynomialRing(field, "x"))
    regular = regular_dg_module(de_rham)
    assert regular in DifferentialGradedModules(de_rham)
    assert regular.dga() is de_rham
    assert regular.is_differential_graded_module()
