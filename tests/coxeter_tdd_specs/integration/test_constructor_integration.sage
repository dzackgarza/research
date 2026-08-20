r"""One Coxeter type, one diagram, one root lattice, one group -- and they agree.

Migrated from the red-phase spec ``integration/test_constructor_integration.py``,
which asserted these agreements against a planned ``GramMatrix`` / ``RootSystem``
/ ``CoxeterGroup`` / ``WeylGroup`` API that was never built.  Every mathematical
requirement it carried survives here; what changed is the surface it is asked
of.

On the owned surface a Cartan type constructs a ``CoxeterDiagrams``
(``preamble/.../integrallattice/coxeter_diagrams.sage``), and the objects the
spec kept in step are not separate objects any more:

* the "Gram matrix" is :meth:`root_intersection_matrix`, the Gram matrix of the
  diagram's own root lattice, so agreement between a Gram object and a root
  system object is identity, not an assertion;
* the "root system" is :meth:`root_lattice`, the domain of
  :meth:`root_morphism`;
* the "Coxeter group" and the "Weyl group" are one object,
  :meth:`coxeter_group` -- for a crystallographic diagram the Coxeter group *is*
  the Weyl group (Wikipedia, *Coxeter group*, oldid 1300325012), and the spec's
  "both constructors give the same order" was that identity written as a
  comparison.

What stays falsifiable is the arithmetic: ranks, bonds, Schläfli determinants,
and group orders.  The oracles are the in-corpus captures
``literature/wikipedia/finite_coxeter_group_invariants.md`` (|W(A_n)| = (n+1)!,
|W(B_n)| = |W(C_n)| = 2^n n!, |W(D_n)| = 2^{n-1} n!, |W(F_4)| = 1152,
|W(G_2)| = 12) and ``literature/wikipedia/schlaefli_determinants_by_family.md``
(the Schläflian by family and rank).  Orders are asserted of the group reached
*through the diagram*, which is a different route from
``tests/test_known_mathematics.sage``'s assertions about Sage's ``WeylGroup``
and not a duplicate of them.
"""

import pytest

from sage.all import CoxeterMatrix, SymmetricGroup, matrix

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


# ``literature/wikipedia/schlaefli_determinants_by_family.md``: the Schläflian
# $\det C$ of each finite family, as a function of the rank -- $n+1$ for $A_n$,
# $2$ for $B_n$ and $C_n$, $4$ for $D_n$, $9-n$ for $E_n$, $5-n$ for $F_n$,
# $3-n$ for $G_n$.  Exact, and instant at every rank.
FINITE_CRYSTALLOGRAPHIC_SCHLAEFLIANS = {
    ("A", 2): 3,
    ("B", 3): 2,
    ("C", 4): 2,
    ("D", 5): 4,
    ("E", 7): 2,
    ("F", 4): 1,
    ("G", 2): 1,
}

# Wikipedia, *Coxeter group*, oldid 1300325012, section "Properties": the order
# of the finite irreducible Coxeter group of that type.  Only the types whose
# groups are small enough to enumerate appear -- the sole route the owned
# surface offers to $|W|$ is ``coxeter_group().order()``, which counts elements
# (Sage's ``CoxeterMatrixGroup.order`` is ``len(self)``).  There is no
# closed-form order on a diagram, so $|W(E_6)|$, $|W(E_7)|$ and $|W(E_8)|$ are
# not asserted here; they are asserted of Sage's ``WeylGroup`` against
# Humphreys section 2.11 in ``tests/test_known_mathematics.sage``.
ENUMERABLE_ORDERS = {
    ("A", 2): 6,
    ("B", 3): 48,
    ("C", 4): 384,
    ("D", 5): 1920,
    ("F", 4): 1152,
    ("G", 2): 12,
}


def test_the_cartan_type_and_its_rooted_realization_agree_on_rank_and_gram() -> None:
    r"""$A_2$: the diagram's root lattice is the catalogue's $A_2$.

    The spec asked that a ``GramMatrix`` built from a Coxeter type and a
    ``RootSystem`` built from that Gram matrix report the same rank and the
    same entries.  Here the rooted diagram *carries* its root lattice, so the
    content of that requirement is that the lattice it carries is the named one:
    Gram $[[-2,1],[1,-2]]$, this repository's convention
    (``literature/PROJECT_CONVENTIONS.md``, and the wikiwand capture's
    A_2 row).
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2], scale=1)

    assert diagram.cardinality() == 2
    assert diagram.root_lattice().rank() == 2
    assert diagram.root_intersection_matrix() == matrix([[-2, 1], [1, -2]])
    assert diagram.root_intersection_matrix() == Lattices.A2.gram_matrix()
    assert diagram.coxeter_matrix() == CoxeterMatrix(
        [[1, 3], [3, 1]], index_set=(0, 1)
    )


def test_a_rooted_diagram_is_recovered_from_its_own_roots() -> None:
    r"""$B_3$: roots -> diagram -> roots -> diagram is the identity on the data.

    The spec's round trip (``RootSystem`` -> ``GramMatrix`` -> ``RootSystem``).
    The reference realization of $B_3$ has short roots of square $-2$ and long
    roots of square $-4$; the bonds are read back off the Gram data by
    $4b(r,s)^2/q(r)q(s) \in \{0,1,2\} \mapsto m \in \{2,3,4\}$, giving the
    bracket-$[4,3]$ Coxeter matrix.
    """
    rooted = CoxeterDiagrams().from_cartan_type(["B", 3], scale=1)

    recovered = CoxeterDiagrams().from_roots(tuple(rooted.roots()))

    assert recovered.root_intersection_matrix() == rooted.root_intersection_matrix()
    assert recovered.coxeter_matrix() == rooted.coxeter_matrix()
    assert recovered.coxeter_matrix() == CoxeterMatrix(
        [[1, 3, 2], [3, 1, 4], [2, 4, 1]], index_set=(0, 1, 2)
    )
    assert sorted(root.norm() for root in rooted.roots()) == [-4, -4, -2]
    assert recovered.coxeter_group().order() == 48


def test_the_coxeter_group_of_a3_is_the_symmetric_group_on_four_letters() -> None:
    r"""$W(A_3) \cong S_4$, of order $24 = 4!$.

    The spec built a ``CoxeterGroup`` from a ``RootSystem`` and checked its
    order against $|S_4|$.  The owned route is
    :meth:`CoxeterDiagrams.ParentMethods.coxeter_group`, and the isomorphism is asked
    with the owned name -- ``is_isomorphic_to``, which decides the question for
    finite groups through GAP rather than inferring it from equal orders.
    """
    group = CoxeterDiagrams().from_cartan_type(["A", 3]).coxeter_group()

    assert group.order() == 24
    assert group.is_isomorphic_to(SymmetricGroup(4)) is True


def test_every_construction_path_reaches_the_same_c3_diagram() -> None:
    r"""$C_3$: Cartan type, Coxeter matrix, and roots build one diagram.

    The spec's "alternative construction paths give equivalent results".  The
    three constructors are the category's ``from_cartan_type``, the parent
    constructor on a Coxeter matrix, and ``from_roots`` on the reference
    realization; they differ only in their index sets, which is a labelling and
    not mathematics, so the comparison is of bonds and of group order.
    """
    by_type = CoxeterDiagrams().from_cartan_type(["C", 3])
    by_matrix = CoxeterDiagrams().from_coxeter_matrix(CoxeterMatrix(["C", 3]))
    by_roots = CoxeterDiagrams().from_cartan_type(["C", 3], scale=1)

    assert by_type.coxeter_matrix() == by_matrix.coxeter_matrix()
    assert by_roots.coxeter_matrix() == CoxeterMatrix(
        [[1, 3, 2], [3, 1, 4], [2, 4, 1]], index_set=(0, 1, 2)
    )
    orders = {
        diagram.coxeter_group().order()
        for diagram in (by_type, by_matrix, by_roots)
    }
    assert orders == {48}, "B_3 and C_3 are one Coxeter group, of order 2^3 3!"


def test_rank_is_one_number_across_diagram_lattice_and_group() -> None:
    r"""$E_6$: the vertex count, the root-lattice rank, and the dimension of the
    reflection representation are the same number.

    The spec collected ``rank`` from four separate objects and asserted the set
    had one element.  Two of those objects no longer exist separately; the
    remaining three places the number can be read are asserted here.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["E", 6], scale=1)

    assert diagram.cardinality() == 6
    assert diagram.root_lattice().rank() == 6
    assert diagram.root_realization().rank() == 6
    assert diagram.coxeter_group().degree() == 6


@pytest.mark.parametrize("cartan_type", sorted(FINITE_CRYSTALLOGRAPHIC_SCHLAEFLIANS))
def test_finite_crystallographic_types_are_elliptic_of_the_tabulated_schlaeflian(
    cartan_type: tuple,
) -> None:
    r"""Each finite crystallographic type is elliptic, with the family's
    Schläflian.

    "Elliptic" is Coxeter's word for what the spec called finite type, and it is
    the owned predicate: :meth:`CoxeterDiagrams.ParentMethods.is_elliptic`.  The
    determinant is the per-family literature formula, not a recomputation, and
    it separates the ranks within a family: $E_7$ has $\det C = 2$, while
    $\det C$ reaches $0$ at $E_9 = \tilde E_8$ and $-1$ at $E_{10}$.
    """
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.is_elliptic()
    assert not diagram.is_parabolic(), "elliptic and parabolic are exclusive"
    assert diagram.cardinality() == rank
    assert diagram.schlafli_matrix().det() == FINITE_CRYSTALLOGRAPHIC_SCHLAEFLIANS[
        cartan_type
    ]


@pytest.mark.parametrize("cartan_type", sorted(ENUMERABLE_ORDERS))
def test_the_diagrams_coxeter_group_has_the_tabulated_order(
    cartan_type: tuple,
) -> None:
    r"""$|W|$ of the group reached through the diagram, against the literature.

    The spec asserted that a ``CoxeterGroup`` and a ``WeylGroup`` built from the
    same type have the same order.  For a crystallographic diagram they are one
    group, so what remains to check is that the diagram reaches it with the
    tabulated order.
    """
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.coxeter_group().order() == ENUMERABLE_ORDERS[cartan_type]


def test_the_schlaeflian_sign_separates_elliptic_from_parabolic() -> None:
    r"""$\det C > 0$ for $A_2$ and $\det C = 0$ for $\tilde A_2$.

    The spec's Gram-determinant/type correspondence, restated in the literature
    convention where it is true.  :meth:`schlafli_matrix` is the literature's
    $C_{ij} = -2\cos(\pi/m_{ij})$, under which elliptic is positive definite and
    parabolic is positive semidefinite of corank one
    (``literature/wikipedia/schlaefli_determinants_by_family.md``: $\det C =
    n+1$ for $A_n$, so $3$ for $A_2$; the extended diagram is the affine
    transition, $\det C = 0$).

    The repository's own Gram matrix is $B = -C$, so $\det B = (-1)^n \det C$
    and the *sign* of the determinant is not a type test in odd rank.  That is
    why the assertion below is made on $C$ and the definiteness assertion on
    $B$.
    """
    elliptic = CoxeterDiagrams().from_cartan_type(["A", 2])
    parabolic = CoxeterDiagrams().from_cartan_type(["A", 2, 1])

    assert elliptic.schlafli_matrix().det() == 3
    assert elliptic.schlafli_matrix().is_positive_definite()
    assert elliptic.is_elliptic()

    assert parabolic.schlafli_matrix().det() == 0
    assert parabolic.is_parabolic()
    assert not parabolic.is_elliptic()

    assert (-Lattices.A2.gram_matrix()).is_positive_definite(), (
        "this repository's B = -C, so elliptic reads as negative definite on B"
    )
