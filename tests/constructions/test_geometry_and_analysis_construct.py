r"""Polytopes, Coxeter diagrams and root systems, function spaces, tensors, divisors, real numbers.

The remaining corners of the session a mathematician would reach for, each
asked for the values its definition determines.
"""

import pytest
from sage.all import Infinity

from dzack_research.preamble.all import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Polytopes.
# ---------------------------------------------------------------------------


def test_the_standard_simplex_and_the_square() -> None:
    simplex = LatticePolygon([[0, 0], [1, 0], [0, 1]])
    square = LatticePolygon([[-1, -1], [1, -1], [1, 1], [-1, 1]])

    assert simplex in ConvexPolygons()
    assert simplex in ConvexPolytopes()
    assert simplex in LatticePolytopes()
    assert simplex.dimension() == 2
    assert simplex.n_vertices() == 3
    assert simplex.volume() == QQ(1) / 2
    assert simplex.normalized_volume() == 1
    assert simplex.n_integral_points() == 3
    assert simplex.n_interior_points() == 0
    assert simplex.n_boundary_points() == 3
    assert simplex.is_lattice_polytope()
    assert simplex.is_compact()
    assert not simplex.is_reflexive()
    assert simplex.facets().cardinality() == 3
    assert square.volume() == 4
    assert square.n_interior_points() == 1
    assert square.n_boundary_points() == 8
    assert square.is_reflexive()
    assert square.polar_dual().n_vertices() == 4
    assert square.polar_dual().volume() == 2
    assert square.polar_dual().is_reflexive()
    assert square.contains_point((0, 0))
    assert not square.contains_point((2, 0))
    assert square.interior_contains_point((0, 0))
    assert not square.interior_contains_point((1, 0))


def test_ehrhart_polynomial_of_the_square() -> None:
    square = LatticePolygon([[0, 0], [1, 0], [1, 1], [0, 1]])
    ehrhart = square.ehrhart_polynomial()
    t = ehrhart.parent().algebra_generator("t")
    assert ehrhart == (t + 1) ** 2
    assert ehrhart(2) == 9
    assert square.h_star_vector().cardinality() == 3


def test_a_three_dimensional_polytope() -> None:
    cube = LatticePolytope([[a, b, c] for a in (0, 1) for b in (0, 1) for c in (0, 1)])
    tetrahedron = ConvexPolytope([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert cube.dimension() == 3
    assert cube.n_vertices() == 8
    assert cube.facets().cardinality() == 6
    assert cube.volume() == 1
    assert cube.n_integral_points() == 8
    assert cube.is_smooth()
    assert tetrahedron.volume() == QQ(1) / 6
    assert tetrahedron.normalized_volume() == 1
    assert tetrahedron.n_integral_points() == 4
    assert ConvexPolygon([[0, 0], [QQ(1) / 2, 0], [0, QQ(1) / 2]]).is_lattice_polytope() is False


# ---------------------------------------------------------------------------
# Coxeter diagrams, Coxeter groups, root lattices.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "cartan_type, order, rank, coxeter_number, root_count",
    [(["A", 2], 6, 2, 3, 6), (["A", 3], 24, 3, 4, 12), (["D", 4], 192, 4, 6, 24), (["E", 6], 51840, 6, 12, 72)],
)
def test_finite_coxeter_diagrams_groups_and_root_lattices(cartan_type, order, rank, coxeter_number, root_count) -> None:
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)
    group = Groups.Coxeter(cartan_type)
    root_lattice = Lattices(ZZ)(cartan_type[0] + str(cartan_type[1]))

    assert diagram.cardinality() == rank
    assert diagram.is_elliptic()
    assert not diagram.is_parabolic()
    assert not diagram.is_hyperbolic()
    assert diagram.is_connected()
    assert diagram.coxeter_entry(0, 1) == 3
    assert diagram.coxeter_entry(0, 0) == 1
    assert group in FiniteGroups()
    assert group.order() == order
    assert Groups.Coxeter(diagram.coxeter_matrix()).order() == order
    assert root_lattice in RootLattices()
    assert root_lattice.rank() == rank
    assert root_lattice.roots().cardinality() == root_count
    assert root_lattice.simple_roots().cardinality() == rank
    assert root_lattice.coxeter_number() == coxeter_number
    assert root_lattice.fundamental_weights().cardinality() == rank
    assert root_lattice.simple_reflections().cardinality() == rank
    assert root_lattice.highest_root().is_root()
    assert root_lattice.highest_root().height() == coxeter_number - 1
    assert root_lattice.O().order() % order == 0
    assert root_lattice.cartan_type().rank() == rank


def test_affine_and_hyperbolic_coxeter_diagrams() -> None:
    affine = CoxeterDiagrams().from_cartan_type(["A", 2, 1])
    hyperbolic = CoxeterDiagrams().from_coxeter_matrix([[1, 3, 3], [3, 1, 4], [3, 4, 1]])
    assert affine.is_parabolic()
    assert not affine.is_elliptic()
    assert affine.zero_inertia_index() == 1
    assert hyperbolic.is_hyperbolic()
    assert hyperbolic.negative_inertia_index() == 1
    assert hyperbolic.positive_inertia_index() == 2
    assert hyperbolic.elliptic_subdiagrams().cardinality() >= 3
    assert Groups.Coxeter(hyperbolic.coxeter_matrix()) not in FiniteGroups()
    assert Groups.Coxeter(["A", 2, 1]) not in FiniteGroups()
    assert hyperbolic.induced_subdiagram([0, 1]).is_elliptic()
    assert affine.coxeter_entry(0, 1) == 3


def test_a_rooted_diagram_from_a_root_lattice() -> None:
    a2 = Lattices(ZZ)("A2")
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2], rooted=True)
    assert diagram.is_rooted()
    assert diagram.roots().cardinality() == 2
    assert diagram.root_gram_tensor() == a2.gram_tensor()
    reflection = a2.reflection(a2.simple_roots()[0])
    assert reflection * reflection == a2.O().one()
    assert reflection in a2.O()


# ---------------------------------------------------------------------------
# Function spaces and sequence spaces.
# ---------------------------------------------------------------------------


def test_smooth_functions_on_the_real_line() -> None:
    smooth = C(Infinity, RR)
    x = smooth.coordinate()
    f = x**2 + 1
    assert smooth in Algebras(RR)
    assert smooth in Modules(RR)
    assert f.evaluate_at(RR(2)) == RR(5)
    assert f.derivative() == 2 * x
    assert f.derivative().derivative() == smooth(2)
    assert smooth.integral(f, RR(0)) == x**3 / 3 + x
    assert f.compose(x + 1) == (x + 1) ** 2 + 1
    assert f.maclaurin_series().coefficient(2) == 1
    assert smooth.cardinality() > aleph0
    assert smooth.one() * f == f


def test_lebesgue_and_sequence_spaces() -> None:
    square_integrable = Lp(2)
    cubic = Lp(3)
    sequences = ell(2)
    assert square_integrable in Modules(RR)
    assert square_integrable.conjugate_lebesgue_space() is square_integrable
    assert cubic.conjugate_lebesgue_space().integrability_exponent() == QQ(3) / 2
    assert square_integrable.integrability_exponent() == 2
    assert sequences.conjugate_sequence_space() is sequences
    assert ell(1).conjugate_sequence_space().integrability_exponent() == Infinity


def test_indexed_families_of_special_functions() -> None:
    characters = FourierCharacters()
    hermite = HermitePolynomials()
    assert characters.cardinality() == aleph0
    assert hermite.cardinality() == aleph0
    assert characters.ranking_map()(characters[3]) == 3
    assert hermite.ranking_map()(hermite[4]) == 4
    assert hermite[2] != hermite[3]


# ---------------------------------------------------------------------------
# Tensors.
# ---------------------------------------------------------------------------


def test_a_gram_tensor_and_its_pullback() -> None:
    gram = tensor(ZZ, (), (1, 1), [[2, 1], [1, 2]])
    doubled = tensor(ZZ, (), (1, 1), [[8, 4], [4, 8]])
    assert gram.tensor_order() == 2
    assert gram.is_symmetric()
    assert not tensor(ZZ, (), (1, 1), [[0, 1], [-1, 0]]).is_symmetric()
    assert gram.tensor_space() in Modules(ZZ)
    assert gram.tensor_space().rank() == 4
    assert gram.change_ring(QQ).tensor_space() in Modules(QQ)
    module = Lattices(ZZ)([[2, 1], [1, 2]]).unformed_module()
    scaling = module.Mor(module)({0: 2 * module.module_generator(0), 1: 2 * module.module_generator(1)})
    assert gram.pullback(scaling) == doubled
    assert gram == Lattices(ZZ)([[2, 1], [1, 2]]).gram_tensor()
    vector = tensor(ZZ, (1,), (), [1, 1])
    assert gram.contract(vector, vector) == 6


# ---------------------------------------------------------------------------
# Divisors.
# ---------------------------------------------------------------------------


def test_divisor_groups_on_a_finite_set_of_points() -> None:
    points = Set(("p", "q", "r"))
    free = FreeModuleOn(ZZ, points)
    divisors = DivisorGroup(free)
    picard = PicardGroup(free)
    classes = ClassGroup(free)
    assert divisors in DivisorGroups()
    assert picard in PicardGroups()
    assert classes in ClassGroups()
    assert divisors.rank() == 3
    formal = FormalDivisor(ZZ, {"p": 2, "q": -1})
    assert formal.parent() in FormalDivisorGroups(ZZ)
    assert formal.parent().terms(formal).cardinality() == 2
    assert formal + formal == FormalDivisor(ZZ, {"p": 4, "q": -2})


# ---------------------------------------------------------------------------
# Real, algebraic and complex numbers.
# ---------------------------------------------------------------------------


def test_exact_real_numbers_and_algebraic_numbers() -> None:
    root_two = RR(2).sqrt()
    assert root_two * root_two == RR(2)
    assert root_two > RR(1)
    assert root_two < RR(2)
    assert RR(4).sqrt() == RR(2)
    assert RR(1) / 2 in UnitInterval
    assert RR(2) not in UnitInterval
    assert RR(3) in NonNegativeReals
    assert -RR(1) not in NonNegativeReals
    approximation = RealApproximation(1.5)
    assert approximation in RR
    assert approximation < RR(2)
    algebraic = AA(2).sqrt()
    assert algebraic.minpoly().degree() == 2
    assert algebraic**2 == AA(2)
    assert AA(4).sqrt().minpoly().degree() == 1
    imaginary = QQbar(-1).sqrt()
    assert imaginary**2 == QQbar(-1)
    assert imaginary.minpoly().degree() == 2
    assert imaginary not in AA
