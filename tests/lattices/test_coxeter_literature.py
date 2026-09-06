r"""Literature values for Coxeter diagrams, their groups and their Schlaeflians.

Every row cites the source that states it.  The sources are the captures kept
with the archived specification corpus
(``archives/preamble/tests/coxeter_tdd_specs/literature/``), which record the
article and revision they were taken from:

* ``wikipedia/finite_coxeter_group_invariants.md`` -- rank, Coxeter number,
  reflection count, order and bracket symbol of every finite irreducible
  Coxeter group.  It carries the correction that \(|W(A_n)| = (n+1)!\) under
  the indexing used throughout, not \(n!\).
* ``wikipedia/schlaefli_determinants_by_family.md`` -- the Schlaeflian by
  family and rank, and the affine transition at which it vanishes.
* ``wikipedia/affine_coxeter_groups_witt_symbols.md`` -- the roster of the
  irreducible affine diagrams.
* Humphreys, *Reflection Groups and Coxeter Groups* (1990), Theorem 6.4:
  a Coxeter group is finite exactly when its Schlaefli form is positive
  definite.

Two corrections the archived specification recorded, and this file keeps:

* the automorphism group of the \(A_4\) diagram is \(\mathbb Z/2\) and not
  trivial, because reversing a path is an automorphism for every \(n\geq 2\);
* \([4,3]\) and \([3,4]\) are \(B_3\) and \(C_3\), two labellings of one
  Coxeter graph, so they present one group of order \(48\).

Group orders are asserted only where the owned surface answers them by
counting a small group.  \(|W(E_8)| = 696729600\) is in the invariant table
and is not enumerated here.
"""

import pytest
from sage.all import CoxeterMatrix, SymmetricGroup, factorial

from dzack_research.preamble.all import CoxeterDiagrams


def bracket_diagram(*bonds: int):
    r"""Return the diagram of the bracket symbol \([p_1,\dots,p_k]\).

    Bracket notation names a path: the diagram on \(k+1\) nodes whose
    consecutive bonds are \(p_1,\dots,p_k\) and whose remaining bonds are
    \(2\).
    """
    rank = len(bonds) + 1
    entries = [
        [
            1 if i == j else (bonds[min(i, j)] if abs(i - j) == 1 else 2)
            for j in range(rank)
        ]
        for i in range(rank)
    ]
    return CoxeterDiagrams().from_coxeter_matrix(CoxeterMatrix(entries))


# Bracket symbol -> the name the literature gives it and the order of its group.
BRACKET_ORDERS = {
    (3,): ("A_2", 6),
    (4,): ("B_2 = I_2(4)", 8),
    (5,): ("H_2 = I_2(5)", 10),
    (6,): ("G_2 = I_2(6)", 12),
    (3, 3): ("A_3", 24),
    (4, 3): ("B_3", 48),
    (3, 4): ("C_3", 48),
    (5, 3): ("H_3", 120),
}

# Schlaeflian by family: det C for C_vv = 2, C_vw = -2 cos(pi/m_vw).
FAMILY_SCHLAEFLIAN = {
    "A": lambda rank: rank + 1,
    "B": lambda rank: 2,
    "C": lambda rank: 2,
    "D": lambda rank: 4,
    "E": lambda rank: 9 - rank,
    "F": lambda rank: 5 - rank,
    "G": lambda rank: 3 - rank,
}

CLASSICAL_TYPES = (
    [(["A", rank], rank) for rank in range(1, 7)]
    + [(["B", rank], rank) for rank in range(2, 7)]
    + [(["C", rank], rank) for rank in range(3, 7)]
    + [(["D", rank], rank) for rank in range(4, 7)]
)

EXCEPTIONAL_TYPES = (("E", 6), ("E", 7), ("E", 8), ("F", 4), ("G", 2), ("H", 3), ("H", 4))

EXCEPTIONAL_ORDERS = {("F", 4): 1152, ("G", 2): 12, ("H", 3): 120}

DIAGRAM_INVARIANTS = {
    ("A", 4): (4, 3, 2),
    ("D", 4): (4, 3, 6),
    ("E", 8): (8, 7, 1),
}

AFFINE_TYPES = (
    ["A", 2, 1],
    ["B", 3, 1],
    ["C", 3, 1],
    ["D", 4, 1],
    ["E", 6, 1],
    ["E", 7, 1],
    ["E", 8, 1],
    ["F", 4, 1],
    ["G", 2, 1],
)


@pytest.mark.parametrize("bonds", sorted(BRACKET_ORDERS))
def test_a_bracket_symbol_names_an_elliptic_diagram_of_the_tabulated_order(bonds) -> None:
    r"""Each bracket symbol denotes an elliptic diagram whose group has the tabulated order."""
    name, order = BRACKET_ORDERS[bonds]
    diagram = bracket_diagram(*bonds)

    assert diagram.cardinality() == len(bonds) + 1
    assert diagram.is_connected()
    assert diagram.is_elliptic(), f"{name} is a finite Coxeter group"
    assert diagram.coxeter_group().order() == order


def test_the_two_orderings_of_the_rank_three_double_bond_present_one_group() -> None:
    r"""\([4,3]\) and \([3,4]\) are \(B_3\) and \(C_3\): two labellings, one group.

    The directed Dynkin diagrams differ while the undirected Coxeter graphs
    agree, so the two bracket symbols name the same Coxeter group.
    """
    b3 = bracket_diagram(4, 3)
    c3 = bracket_diagram(3, 4)

    assert b3.coxeter_matrix() != c3.coxeter_matrix(), "the labellings differ"
    assert b3.coxeter_group().order() == 48
    assert c3.coxeter_group().order() == 48
    assert b3.coxeter_group().is_isomorphic_to(c3.coxeter_group())
    assert b3.schlaflian() == c3.schlaflian() == 2


@pytest.mark.parametrize("cartan_type", [("A", 2), ("B", 2), ("G", 2), ("H", 3)])
def test_the_coxeter_presentation_presents_the_coxeter_group(cartan_type) -> None:
    r"""\(\langle s_v \mid s_v^2,\ (s_v s_w)^{m_{vw}}\rangle\) presents \(W\).

    The presented group and the reflection representation are one owned group,
    so the claim is that the chosen presentation it carries has one generator
    per mirror and the relations of the definition.
    """
    letter, rank = cartan_type
    orders = {("A", 2): 6, ("B", 2): 8, ("G", 2): 12, ("H", 3): 120}
    group = CoxeterDiagrams().from_cartan_type([letter, rank]).coxeter_group()

    assert group.group_generators().cardinality() == rank, "one generator per mirror"
    assert group.order() == orders[cartan_type]
    # One squaring relation per mirror, one braid relation per unordered pair.
    assert group.defining_relations().cardinality() == rank + rank * (rank - 1) // 2


@pytest.mark.parametrize("rank", [1, 2, 3, 4])
def test_the_coxeter_group_of_type_a_is_the_symmetric_group(rank) -> None:
    r"""\(W(A_n)\cong S_{n+1}\), of order \((n+1)!\)."""
    group = CoxeterDiagrams().from_cartan_type(["A", rank]).coxeter_group()

    assert group.order() == factorial(rank + 1)
    assert group.is_isomorphic_to(SymmetricGroup(rank + 1))


@pytest.mark.parametrize("rank", [2, 3, 4])
def test_the_coxeter_groups_of_types_b_and_c_coincide(rank) -> None:
    r"""\(W(B_n)\cong W(C_n)\), of order \(2^n\,n!\).

    That is the order of the hyperoctahedral group \(C_2\wr S_n\), which is the
    structure the invariant table records.  The wreath product itself has no
    constructor on the owned surface, so the identification is asserted through
    the order and the isomorphism of the two Coxeter groups.
    """
    b_group = CoxeterDiagrams().from_cartan_type(["B", rank]).coxeter_group()
    c_group = CoxeterDiagrams().from_cartan_type(["C", rank]).coxeter_group()

    assert b_group.order() == 2**rank * factorial(rank)
    assert c_group.order() == b_group.order()
    assert b_group.is_isomorphic_to(c_group)


@pytest.mark.parametrize("cartan_type,rank", CLASSICAL_TYPES)
def test_a_classical_finite_type_is_elliptic_of_the_tabulated_schlaeflian(
    cartan_type, rank
) -> None:
    r"""Elliptic type is positive definiteness of the Schlaefli form (Humphreys 6.4).

    The determinant is the family formula, and no finite member reaches the
    zero at which the family becomes affine.
    """
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)

    assert diagram.cardinality() == rank
    assert diagram.is_elliptic()
    assert diagram.negative_inertia_index() == 0
    assert diagram.zero_inertia_index() == 0
    assert diagram.schlaflian() == FAMILY_SCHLAEFLIAN[cartan_type[0]](rank)


@pytest.mark.parametrize("cartan_type", EXCEPTIONAL_TYPES)
def test_an_exceptional_finite_type_is_elliptic_of_the_tabulated_rank(cartan_type) -> None:
    r"""The exceptional finite Coxeter diagrams, against the invariant table.

    \(H_3\) and \(H_4\) are not crystallographic, so their Schlaefli entries
    involve the golden ratio; the arithmetic stays exact because the entries
    are algebraic numbers and not floating cosines.  The determinant table does
    not cover \(H\), so no Schlaeflian is asserted there.
    """
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.cardinality() == rank
    assert diagram.is_elliptic()
    if letter in FAMILY_SCHLAEFLIAN:
        assert diagram.schlaflian() == FAMILY_SCHLAEFLIAN[letter](rank)


@pytest.mark.parametrize("cartan_type", sorted(EXCEPTIONAL_ORDERS))
def test_an_exceptional_finite_group_has_the_tabulated_order(cartan_type) -> None:
    r"""\(|W(F_4)| = 1152\), \(|W(G_2)| = 12\), \(|W(H_3)| = 120\)."""
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.coxeter_group().order() == EXCEPTIONAL_ORDERS[cartan_type]


@pytest.mark.parametrize("cartan_type", sorted(DIAGRAM_INVARIANTS))
def test_diagram_invariants_match_the_literature(cartan_type) -> None:
    r"""Node count, edge count and \(|\operatorname{Aut}|\) of the diagram.

    The correction the archived specification recorded: \(\operatorname{Aut}\)
    of the \(A_4\) diagram is \(\mathbb Z/2\), generated by reversing the path,
    and not the trivial group.  \(D_4\) has the symmetric group on its three
    outer nodes, which is triality; \(E_8\) has no nontrivial automorphism.
    """
    letter, rank = cartan_type
    vertices, edges, automorphisms = DIAGRAM_INVARIANTS[cartan_type]
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.cardinality() == vertices
    assert diagram.graph().num_edges() == edges
    assert diagram.Aut().order() == automorphisms


@pytest.mark.parametrize("cartan_type", AFFINE_TYPES)
def test_an_extended_diagram_is_parabolic_with_vanishing_schlaeflian(cartan_type) -> None:
    r"""Each extended diagram is parabolic, connected, and has \(\det C = 0\).

    Adjoining the highest root to an irreducible diagram of rank \(r\) gives an
    affine Coxeter group on \(r+1\) nodes.  Affine is the owned parabolicity: a
    positive semidefinite Schlaefli form whose radical is one dimensional, so
    the Schlaeflian vanishes and the zero index of inertia is exactly one.
    """
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)

    assert diagram.cardinality() == cartan_type[1] + 1, "one node is adjoined"
    assert diagram.is_connected()
    assert diagram.is_parabolic()
    assert not diagram.is_elliptic()
    assert diagram.schlaflian() == 0
    assert diagram.zero_inertia_index() == 1
    assert diagram.negative_inertia_index() == 0
