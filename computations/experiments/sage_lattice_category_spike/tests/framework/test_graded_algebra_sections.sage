"""Cox ring and graded section-space contracts for products."""

from sage.all import Algebras, QQ, ProjectiveSpace


def test_cox_ring_structure_and_section_space_roundtrip():
    """Cox ring grading and section ring conversion are internally consistent."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y

    cox = X.cox_ring()
    L = X.O(4, 4)
    sections = L.H(0)
    section_ring = L.section_ring()
    gens = cox.gens()

    assert len(gens) == 4
    assert cox.category().is_subcategory(Algebras(QQ).Commutative().WithBasis())
    assert section_ring.graded_piece(1) is sections
    assert section_ring.graded_piece(2).dimension() == 81
    assert len(section_ring.gens()) == 25

    monomial = sections.basis()[0].to_polynomial()
    assert sections.from_polynomial(monomial) == sections.basis()[0]
    assert cox.homogeneous_degree(gens[0] * gens[-1]) == X.O(1, 1)
