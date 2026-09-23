from sage.all import Infinity

from dzack_research.preamble.all import ZZ, CoxeterDiagrams, Lattices
from dzack_research.preamble.categories.graph_categories import LabelledGraphs

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/test_coxeter_diagrams.sage",
        "live_owner": "tests/lattices/test_coxeter.py",
        "owner_overrides": {
            "test_rooted_diagram_records_roots_intersections_layout_and_tikz": "tests/lattices/test_coxeter_subdiagrams.py",
        },
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage",
        "live_owner": "src/dzack_research/preamble/categories/coxeter_diagrams.py",
        "owner_overrides": {
            "CoxeterDiagrams.ParentMethods.vertex_weight": "src/dzack_research/preamble/categories/vinberg_invariants.py",
            "CoxeterDiagrams.ParentMethods.edge_weight": "src/dzack_research/preamble/categories/vinberg_invariants.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def test_a2_root_realization_gives_single_bond_and_elliptic_diagram() -> None:
    lattice = Lattices(ZZ)("A2")
    diagram = CoxeterDiagrams().from_roots(lattice.module_generators())
    vertices = diagram.index_set()

    assert diagram in LabelledGraphs()
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










def test_minimal_edge_lattices_retain_parallel_and_ultraparallel_geometry() -> None:
    edges = CoxeterDiagrams().minimal_edge_lattices()
    parallel = CoxeterDiagrams().from_roots(edges["parallel"].module_generators())
    divergent = CoxeterDiagrams().from_roots(edges["ultraparallel"].module_generators())

    assert parallel.coxeter_entry(0, 1) == Infinity
    assert parallel.mirrors_are_parallel(0, 1)
    assert divergent.coxeter_entry(0, 1) == Infinity
    assert divergent.mirrors_are_divergent(0, 1)
    assert parallel.coxeter_matrix() == divergent.coxeter_matrix()


