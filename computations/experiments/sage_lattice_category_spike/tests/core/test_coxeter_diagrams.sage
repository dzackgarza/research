r"""Coxeter diagrams as finite Sage parents."""

import pytest

from sage.all import CoxeterMatrix, TestSuite

from sage_lattice_category_spike import CoxeterDiagrams, FiniteCoxeterDiagram, Lattice


def test_root_generated_lattice_constructs_its_diagram_as_a_sage_parent():
    r"""The $A_4$ lattice constructs its Coxeter diagram as a Sage parent."""
    lattice = Lattice("A4")
    diagram = lattice.coxeter_diagram()

    assert diagram.category().is_subcategory(CoxeterDiagrams())
    assert diagram.coxeter_matrix() == CoxeterMatrix(["A", 4])
    assert list(diagram.graph().edges(sort=True)) == [
        (1, 2, 3),
        (2, 3, 3),
        (3, 4, 3),
    ]
    TestSuite(diagram).run(raise_on_failure=True)


def test_induced_subdiagram_recovers_the_standard_a3_diagram():
    r"""The first three simple roots of $A_4$ induce the $A_3$ diagram."""
    diagram = Lattice("A4").coxeter_diagram()

    subdiagram = diagram.subdiagram([diagram.vertex(i) for i in range(3)])

    assert subdiagram.coxeter_matrix() == CoxeterMatrix(["A", 3])


def test_parent_constructs_a_diagram_from_its_coxeter_matrix():
    r"""The parent constructor preserves the standard $B_3$ exponents."""
    matrix = CoxeterMatrix(["B", 3])

    diagram = FiniteCoxeterDiagram(matrix)

    assert diagram.coxeter_matrix() == matrix
    assert list(diagram.graph().edges(sort=True)) == [(1, 2, 3), (2, 3, 4)]


def test_morphisms_preserve_the_full_coxeter_matrix_and_compose():
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
