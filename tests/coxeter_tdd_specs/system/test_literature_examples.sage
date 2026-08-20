r"""Literature examples, end to end: bracket notation, presentations, Weyl-group
identifications, and the extended diagrams.

Migrated from the red-phase spec ``system/test_literature_examples.py``, which
drove a planned ``CoxeterGroup`` / ``WeylGroup`` / ``DynkinDiagram`` /
``RegularPolytope`` API through mock workflow, validator, and timing fixtures.
The fixtures carried no requirement and are gone; every table of literature
values they surrounded is asserted here against the owned surface.

Oracles, all in-corpus captures:

* ``literature/wikipedia/finite_coxeter_group_invariants.md`` -- rank, Coxeter
  number, reflection count, order and structure of every finite irreducible
  Coxeter group, with bracket notation.  It carries the correction that
  $|W(A_n)| = (n+1)!$, not $n!$, under the indexing used throughout.
* ``literature/wikipedia/schlaefli_determinants_by_family.md`` -- the Schläflian
  by family and rank, and the affine transition where it vanishes.
* ``literature/wikipedia/affine_coxeter_groups_witt_symbols.md`` -- the roster of
  irreducible affine diagrams.

$|W|$ is asserted only where the owned surface can answer it without
enumeration cost: ``coxeter_group()`` is Sage's ``CoxeterMatrixGroup``, whose
``order`` counts elements.  $|W(E_8)| = 696729600$ is in the table above and is
asserted of Sage's ``WeylGroup`` in ``tests/test_known_mathematics.sage``.
"""

import pytest

from sage.all import CoxeterMatrix, SymmetricGroup, factorial

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


def _bracket_diagram(*bonds: int) -> "Parent":
    r"""Return the diagram of the bracket symbol $[p_1,\dots,p_{k}]$.

    Bracket notation names the *path*: the diagram on $k+1$ nodes whose
    consecutive bonds are $p_1,\dots,p_k$ and whose non-consecutive bonds are
    $2$.  There is no bracket constructor on the owned surface, so the path is
    written out as the Coxeter matrix it denotes.
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


# Wikipedia, *Coxeter group*, oldid 1300325012: bracket symbol -> named type and
# order.  ``[4,3]`` is $B_3$ and ``[3,4]`` is $C_3$; both have order 48, because
# the directed Dynkin diagrams differ while the undirected Coxeter graphs agree,
# so $B_n$ and $C_n$ are one Coxeter group.
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


@pytest.mark.parametrize("bonds", sorted(BRACKET_ORDERS))
def test_bracket_notation_names_a_finite_group_of_the_tabulated_order(
    bonds: tuple,
) -> None:
    r"""Each bracket symbol denotes an elliptic diagram of the tabulated order."""
    name, order = BRACKET_ORDERS[bonds]
    diagram = _bracket_diagram(*bonds)

    assert diagram.cardinality() == len(bonds) + 1
    assert diagram.is_connected()
    assert diagram.is_elliptic(), f"{name} is a finite Coxeter group"
    assert diagram.coxeter_group().order() == order


def test_the_two_orderings_of_the_rank_three_double_bond_are_one_group() -> None:
    r"""$[4,3]$ and $[3,4]$ are $B_3$ and $C_3$, and they are the same group.

    Reversing a path is a diagram isomorphism, so the two bracket symbols name
    the same Coxeter diagram up to relabelling; the Coxeter matrices differ only
    by that relabelling, and the groups are isomorphic.
    """
    b3 = _bracket_diagram(4, 3)
    c3 = _bracket_diagram(3, 4)

    assert b3.coxeter_matrix() != c3.coxeter_matrix(), "the labellings differ"
    assert b3.coxeter_group().order() == c3.coxeter_group().order() == 48
    assert b3.coxeter_group().is_isomorphic_to(c3.coxeter_group()) is True
    assert c3.coxeter_matrix() == CoxeterMatrix(
        [[1, 3, 2], [3, 1, 4], [2, 4, 1]], index_set=(0, 1, 2)
    ), "the [3,4] labelling is the one Sage's B_3 and C_3 Coxeter graphs carry"


@pytest.mark.xfail(
    strict=True,
    reason=(
        "no constructor from a Schläfli symbol on the owned surface: "
        "ConvexPolytopes (preamble/categories/schemes/polytopes.sage) builds a "
        "polytope from its vertices, nothing reaches a regular polytope from "
        "its symbol {p, q}, and no polytope exposes a symmetry group as a "
        "Coxeter diagram"
    ),
)
def test_a_schlafli_symbol_names_a_polytope_whose_symmetry_group_is_its_coxeter_group() -> None:
    r"""$\{5,3\}$ is the dodecahedron, with symmetry group $H_3$ of order $120$.

    The Schläfli symbol of a regular polytope is the bracket symbol of its
    symmetry group: $\{3\}$ the triangle and $A_2$, $\{4\}$ the square and
    $B_2$, $\{3,3\}$ the tetrahedron and $A_3$, $\{4,3\}$ the cube and $B_3$,
    $\{3,4\}$ the octahedron and $C_3$, $\{5,3\}$ the dodecahedron and $\{3,5\}$
    the icosahedron, both $H_3$.  The group half of every one of those rows is
    asserted above under its bracket symbol; what is missing is the polytope and
    the map from it to its group.
    """
    polytope = RegularPolytope.from_schlafli_symbol("{5,3}")  # noqa: F821

    assert polytope.symmetry_group().coxeter_matrix() == CoxeterMatrix(["H", 3])
    assert polytope.symmetry_group().order() == 120


# Wikipedia, *Coxeter group*, oldid 1300325012: the Coxeter presentation is
# $\langle s_i \mid (s_i s_j)^{m_{ij}} = 1\rangle$ with $m_{ii} = 1$ -- the
# capture's correction to a garbled ``(sts...)^{m_ij}``.  A presentation is
# right when it presents the right group, so the row asserts the order of the
# presented group and its isomorphism with the represented one.
PRESENTED_ORDERS = {("A", 2): 6, ("B", 2): 8, ("G", 2): 12, ("H", 3): 120}


@pytest.mark.parametrize("cartan_type", sorted(PRESENTED_ORDERS))
def test_the_coxeter_presentation_presents_the_coxeter_group(
    cartan_type: tuple,
) -> None:
    r"""$\langle s_v \mid s_v^2, (s_v s_w)^{m_{vw}}\rangle$ presents $W$.

    The spec compared a rendered presentation string against a string from
    Wikipedia.  A string comparison is not a mathematical claim: the content is
    that the chosen presentation and the reflection representation are the same
    group, which is what ``finitely_presented_coxeter_group`` and
    ``coxeter_group`` are the two names for.
    """
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    presented = diagram.finitely_presented_coxeter_group()
    represented = diagram.coxeter_group()

    assert presented.group_generators().cardinality() == rank, (
        "one generator per mirror"
    )
    assert presented.order() == PRESENTED_ORDERS[cartan_type]
    assert presented.is_isomorphic_to(represented) is True


@pytest.mark.parametrize("rank", [1, 2, 3, 4])
def test_the_weyl_group_of_type_a_is_the_symmetric_group(rank: int) -> None:
    r"""$W(A_n) \cong S_{n+1}$, of order $(n+1)!$.

    The capture's correction: the article gave the order of the $A$ series as
    $n!$; with the $A_n$ indexing used throughout, $W(A_n) \cong S_{n+1}$ and
    the order is $(n+1)!$.
    """
    group = CoxeterDiagrams().from_cartan_type(["A", rank]).coxeter_group()

    assert group.order() == factorial(rank + 1)
    assert group.is_isomorphic_to(SymmetricGroup(rank + 1)) is True


@pytest.mark.parametrize("rank", [2, 3, 4])
def test_the_weyl_groups_of_types_b_and_c_coincide(rank: int) -> None:
    r"""$W(B_n) \cong W(C_n)$, of order $2^n\,n!$.

    That order is the order of the hyperoctahedral group $C_2 \wr S_n$, which is
    the structure the literature table records for this row.  The wreath product
    itself is not built here: the owned surface has no wreath-product
    constructor, so the identification with $C_2 \wr S_n$ is asserted through its
    order and not through an isomorphism.
    """
    b_group = CoxeterDiagrams().from_cartan_type(["B", rank]).coxeter_group()
    c_group = CoxeterDiagrams().from_cartan_type(["C", rank]).coxeter_group()

    assert b_group.order() == 2**rank * factorial(rank)
    assert c_group.order() == b_group.order()
    assert b_group.is_isomorphic_to(c_group) is True


# Wikipedia, *Coxeter group* and *Coxeter-Dynkin diagram*: node count, edge
# count, and the order of the diagram automorphism group.
#
# **Correction to the spec.** The spec recorded the automorphism group of the
# $A_4$ diagram as trivial.  It is not: the $A_n$ diagram is a path, and
# reversing it is a nontrivial automorphism for every $n \geq 2$, so the group
# is $\mathbb Z/2$ of order $2$.  The $D_4$ row ($S_3$, order $6$, triality) and
# the $E_8$ row (trivial) are correct as the spec had them.
DIAGRAM_INVARIANTS = {
    ("A", 4): {"vertices": 4, "edges": 3, "automorphisms": 2},
    ("D", 4): {"vertices": 4, "edges": 3, "automorphisms": 6},
    ("E", 8): {"vertices": 8, "edges": 7, "automorphisms": 1},
}


@pytest.mark.parametrize("cartan_type", sorted(DIAGRAM_INVARIANTS))
def test_diagram_invariants_match_the_literature(cartan_type: tuple) -> None:
    r"""Node count, edge count, and $|\operatorname{Aut}|$ of the diagram.

    :meth:`CoxeterDiagrams.ParentMethods.Aut` on an unrooted diagram is the
    bond-preserving group -- the automorphism group of the Coxeter graph with
    its edge labels -- which is the group the literature tabulates for a Dynkin
    diagram.
    """
    letter, rank = cartan_type
    expected = DIAGRAM_INVARIANTS[cartan_type]
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.cardinality() == expected["vertices"]
    assert len(diagram.graph().edges(sort=False)) == expected["edges"]
    assert diagram.Aut().order() == expected["automorphisms"]


def test_the_weyl_orders_of_the_small_diagram_invariant_rows() -> None:
    r"""$|W(A_4)| = 120$ and $|W(D_4)| = 192$.

    The third row of the invariant table, $E_8$, has $|W| = 696729600$; it is
    asserted of Sage's ``WeylGroup`` in ``tests/test_known_mathematics.sage``
    rather than by enumerating the group here.
    """
    assert CoxeterDiagrams().from_cartan_type(["A", 4]).coxeter_group().order() == 120
    assert CoxeterDiagrams().from_cartan_type(["D", 4]).coxeter_group().order() == 192


@pytest.mark.parametrize(
    "cartan_type",
    [
        ["A", 2, 1],
        ["B", 3, 1],
        ["C", 3, 1],
        ["D", 4, 1],
        ["E", 6, 1],
        ["E", 7, 1],
        ["E", 8, 1],
        ["F", 4, 1],
        ["G", 2, 1],
    ],
)
def test_the_extended_diagrams_are_the_affine_roster(cartan_type: list) -> None:
    r"""Each extended diagram is parabolic, connected, and has $\det C = 0$.

    The extended diagram of an irreducible root system of rank $r$ adjoins the
    highest root as an $(r+1)$-st node, and the resulting Coxeter group is
    affine (``literature/wikipedia/affine_coxeter_groups_witt_symbols.md``).
    Affine is the owned :meth:`is_parabolic`; the vanishing Schläflian is the
    corank-one radical that makes it so.
    """
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)
    schlafli = diagram.schlafli_matrix()

    assert diagram.cardinality() == cartan_type[1] + 1, "one node is adjoined"
    assert diagram.is_connected()
    assert diagram.is_parabolic()
    assert not diagram.is_elliptic()
    assert schlafli.det() == 0
    assert schlafli.rank() == schlafli.nrows() - 1
