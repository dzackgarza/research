"""Finite-group actions and isotypic decomposition of section spaces."""

from sage.all import QQ, CyclicPermutationGroup, ProjectiveSpace


def test_isotypic_decomposition_of_quadratic_involution_action():
    """The involution on `(4,4)` has 13+12 dimensional decomposition."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    involution = X.hom([x0, -x1, y0, -y1], X)
    action = X.Aut().action(CyclicPermutationGroup(2), [involution])
    sections = X.O(4, 4)
    linearized = sections.linearize(action)
    representation = linearized.H_representation(0)
    decomposition = representation.isotypic_decomposition()

    assert len(decomposition) == 2
    assert decomposition.dimension() == 25
    assert decomposition.trivial_component().dimension() == 13
    assert len(decomposition.nontrivial_components()) == 1
    assert decomposition.nontrivial_components()[0].dimension() == 12

    g = CyclicPermutationGroup(2).gen(0)
    for basis_section in decomposition.trivial_component().basis():
        assert linearized.act_on_section(g, basis_section) == basis_section
