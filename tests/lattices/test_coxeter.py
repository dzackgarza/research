from sage.all import Infinity

from dzack_research.preamble.all import ZZ, CoxeterDiagrams, Lattices, finite_ordered_set
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


def test_coxeter_tikz_is_a_view_of_the_live_bond_data() -> None:
    diagram = CoxeterDiagrams().from_coxeter_matrix(
        [[1, 3, 4], [3, 1, -1], [4, -1, 1]],
        names=("a", "b", "c"),
    )
    tikz = diagram.tikz_picture()

    assert tikz.startswith(r"\begin{tikzpicture}")
    assert tikz.endswith(r"\end{tikzpicture}")
    assert "$ 4 $" in tikz
    assert r"$ \infty $" in tikz
    assert "$ 3 $" not in tikz
    assert "$ a $" in tikz


def test_coxeter_diagram_morphisms_preserve_all_bonds_and_compose() -> None:
    a2 = CoxeterDiagrams().from_cartan_type(["A", 2])
    a3 = CoxeterDiagrams().from_cartan_type(["A", 3])
    a4 = CoxeterDiagrams().from_cartan_type(["A", 4])
    a2_vertices = a2.index_set()
    a3_vertices = a3.index_set()
    a4_vertices = a4.index_set()

    first = CoxeterDiagrams().Mor(a2, a3)(
        finite_ordered_set((a3_vertices[1], a3_vertices[2]))
    )
    second = CoxeterDiagrams().Mor(a3, a4)(
        finite_ordered_set((a4_vertices[1], a4_vertices[2], a4_vertices[3]))
    )
    composite = second * first

    assert composite.images() == finite_ordered_set((a4_vertices[2], a4_vertices[3]))
    assert composite.domain() is a2
    assert composite.codomain() is a4
    assert CoxeterDiagrams().Mor(a2, a2).identity().is_identity()

    import pytest

    with pytest.raises(ValueError, match="preserve every Coxeter matrix entry"):
        CoxeterDiagrams().Mor(a2, a3)((a3_vertices[0], a3_vertices[2]))


def test_scaled_cartan_recognition_and_reference_scaling_use_the_same_root_data() -> None:
    b3 = CoxeterDiagrams().from_cartan_type(["B", 3], scale=2)
    cartan, scale = b3.scaled_cartan_type()

    assert cartan.type() == "B"
    assert cartan.rank() == 3
    assert scale == ZZ(2)
    assert b3.node_color(b3.vertex(0)) in {"#F8F9FE", "#BFC9CA"}
    assert b3.root(b3.vertex(0)).parent() is b3.root_realization()


def test_minimal_edge_lattices_retain_parallel_and_ultraparallel_geometry() -> None:
    edges = CoxeterDiagrams().minimal_edge_lattices()
    parallel = CoxeterDiagrams().from_roots(edges["parallel"].module_generators())
    divergent = CoxeterDiagrams().from_roots(edges["ultraparallel"].module_generators())

    assert parallel.coxeter_entry(0, 1) == Infinity
    assert parallel.mirrors_are_parallel(0, 1)
    assert divergent.coxeter_entry(0, 1) == Infinity
    assert divergent.mirrors_are_divergent(0, 1)
    assert parallel.coxeter_matrix() == divergent.coxeter_matrix()


def test_archived_diagram_session_vocabulary_uses_the_live_owned_objects() -> None:
    diagram = CoxeterDiagrams().from_cartan_type(["A", 3], rooted=True)

    assert diagram.vertices() is diagram.index_set()
    assert diagram.num_vertices() == 3
    assert diagram.finitely_presented_coxeter_group() is diagram.coxeter_group()
    assert diagram.subdiagram((diagram.vertex(0), diagram.vertex(1))).cardinality() == 2
    assert diagram.drawing_conventions()["ordinary Coxeter bond"]
    assert diagram.tikz().startswith(r"\begin{tikzpicture}")
