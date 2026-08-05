r"""Coxeter diagrams as finite Sage parents."""

import pytest

from sage.all import CoxeterMatrix, TestSuite, matrix, ZZ

from pathlib import Path
import dzack_research

_p = Path(dzack_research.__file__).resolve().parent / "preamble"
load(str(_p / "install.sage"))


def test_cartan_type_constructs_its_diagram_as_a_sage_parent() -> None:
    r"""The Cartan type $A_4$ constructs its Coxeter diagram as a Sage parent."""
    diagram = CoxeterDiagrams().from_cartan_type(["A", 4])

    assert diagram.category().is_subcategory(CoxeterDiagrams())
    assert diagram.coxeter_matrix() == CoxeterMatrix(["A", 4])
    assert list(diagram.graph().edges(sort=True)) == [
        (1, 2, 3),
        (2, 3, 3),
        (3, 4, 3),
    ]
    TestSuite(diagram).run(raise_on_failure=True)


def test_induced_subdiagram_recovers_the_standard_a3_diagram() -> None:
    r"""The first three simple roots of $A_4$ induce the $A_3$ diagram."""
    diagram = CoxeterDiagrams().from_cartan_type(["A", 4])

    subdiagram = diagram.subdiagram([diagram.vertex(i) for i in range(3)])

    assert subdiagram.coxeter_matrix() == CoxeterMatrix(["A", 3])


def test_parent_constructs_a_diagram_from_its_coxeter_matrix() -> None:
    r"""The parent constructor preserves the standard $B_3$ exponents."""
    matrix = CoxeterMatrix(["B", 3])

    diagram = FiniteCoxeterDiagram(matrix)

    assert diagram.coxeter_matrix() == matrix
    assert list(diagram.graph().edges(sort=True)) == [(1, 2, 3), (2, 3, 4)]


def test_rooted_diagram_records_roots_intersections_layout_and_tikz() -> None:
    r"""A rooted diagram stores the lattice roots behind a non-simply-laced edge."""
    lattice = IntegralLattice(matrix(ZZ, [[-4, 2], [2, -2]]), names=("r", "s"))
    r, s = lattice.gens()

    diagram = FiniteCoxeterDiagram.from_roots(
        (r, s),
        names=("r", "s"),
        positions={0: (0, 0), 1: (2, 0)},
    )

    assert diagram.embedding_codomain() is lattice
    assert diagram.root_lattice().gram_matrix() == lattice.gram_matrix()
    assert diagram.root_embedding()(diagram.root_lattice().module_generators()[0]) == r
    assert diagram.roots() == (r, s)
    assert diagram.root_intersection_matrix() == matrix(ZZ, [[-4, 2], [2, -2]])
    assert diagram.coxeter_matrix() == CoxeterMatrix([[1, 4], [4, 1]], index_set=(0, 1))
    assert list(diagram.root_intersection_graph().edges(sort=True)) == [
        (0, 0, -4),
        (0, 1, 2),
        (1, 1, -2),
    ]
    assert diagram.preferred_positions() == {0: (0, 0), 1: (2, 0)}
    assert diagram.node_color(0) == "#F8F9FE"
    assert diagram.node_color(1) == "#BFC9CA"
    assert diagram.drawing_conventions()["root squares"] == (
        "stored as self-loops in root_intersection_graph(), omitted from TikZ"
    )

    tikz = diagram.tikz()
    assert "coxeter double" in tikz
    assert "coxeterNegativeFour" in tikz
    assert "coxeterNegativeTwo" in tikz
    assert "(v0) -- (v1)" in tikz
    assert "(v0) -- (v0)" not in tikz
    assert "(v1) -- (v1)" not in tikz

    subdiagram = diagram.subdiagram([diagram.vertex(1)])
    assert subdiagram.embedding_codomain() is lattice
    assert subdiagram.roots() == (s,)
    assert subdiagram.root_intersection_matrix() == matrix(ZZ, [[-2]])
    assert subdiagram.preferred_positions() == {1: (2, 0)}


def test_morphisms_preserve_the_full_coxeter_matrix_and_compose() -> None:
    r"""Diagram morphisms preserve every exponent, including nonedges."""
    a2 = FiniteCoxeterDiagram.from_cartan_type(["A", 2])
    a3 = FiniteCoxeterDiagram.from_cartan_type(["A", 3])
    a4 = FiniteCoxeterDiagram.from_cartan_type(["A", 4])

    inclusion_23 = a2.hom([2, 3], codomain=a3)
    inclusion_234 = a3.hom([2, 3, 4], codomain=a4)
    composite = inclusion_234 * inclusion_23

    assert tuple(vertex.value for vertex in composite.images()) == (3, 4)
    assert composite.domain() == a2
    assert composite.codomain() == a4
    assert composite.parent().category().is_subcategory(CoxeterDiagrams().Homsets())
    assert all(
        a2.coxeter_matrix()[left, right]
        == a4.coxeter_matrix()[composite(a2(left)).value, composite(a2(right)).value]
        for left in a2.index_set()
        for right in a2.index_set()
    )
    identity = a2.hom(a2.index_set(), codomain=a2)
    assert tuple(vertex.value for vertex in (inclusion_23 * identity).images()) == (
        2,
        3,
    )

    with pytest.raises(
        AssertionError,
        match="must preserve every Coxeter exponent",
    ):
        a2.hom([1, 3], codomain=a3)
