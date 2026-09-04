from sage.all import Infinity

from dzack_research.preamble.all import CoxeterDiagrams, Lattices, ZZ


def test_a2_root_realization_gives_single_bond_and_elliptic_diagram() -> None:
    lattice = Lattices(ZZ)("A2")
    diagram = CoxeterDiagrams().from_roots(lattice.module_generators())
    vertices = diagram.index_set()

    assert diagram.is_rooted()
    assert diagram.coxeter_matrix()[vertices[0], vertices[1]] == 3
    assert diagram.graph().num_edges() == 1
    assert diagram.is_elliptic()


def test_double_and_parallel_bonds_are_read_from_actual_root_pairings() -> None:
    double_lattice = Lattices(ZZ)([[-2, 2], [2, -4]])
    double = CoxeterDiagrams().from_roots(double_lattice.module_generators())
    assert double.coxeter_matrix()[0, 1] == 4

    parallel_lattice = Lattices(ZZ)([[-2, 2], [2, -2]])
    parallel = CoxeterDiagrams().from_roots(parallel_lattice.module_generators())
    assert parallel.coxeter_entry(0, 1) == Infinity
    assert parallel.is_parabolic()


def test_generic_g2_coxeter_matrix_can_have_m6_even_though_minus_two_minus_four_roots_cannot() -> None:
    generic = CoxeterDiagrams().from_coxeter_matrix([[1, 6], [6, 1]])
    assert generic.coxeter_entry(0, 1) == 6
    assert generic.is_elliptic()

    rooted = Lattices(ZZ)([[-2, 3], [3, -6]])
    diagram = CoxeterDiagrams().from_roots(rooted.module_generators())
    assert diagram.coxeter_matrix()[0, 1] == 6


def test_induced_subdiagrams_preserve_selected_roots() -> None:
    lattice = Lattices(ZZ)("A3")
    diagram = CoxeterDiagrams().from_roots(lattice.module_generators())
    subdiagram = diagram.induced_subdiagram((0, 1))
    assert subdiagram.is_rooted()
    _shape = subdiagram.root_gram_tensor().tensor_shape()
    assert _shape.cardinality() == 2
    assert _shape[0] == 2
    assert _shape[1] == 2
    assert subdiagram.coxeter_matrix()[0, 1] == 3
