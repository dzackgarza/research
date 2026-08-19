r"""Classification of Coxeter diagrams: elliptic, parabolic, and the two
hyperbolic families.

Migrated from the red-phase spec ``system/test_classification_examples.py``,
which asked a planned ``CoxeterSystem`` class for eigenvalues and a type string.
The requirements survive; they are now asked of the owned surface:

* :meth:`FiniteCoxeterDiagram.is_elliptic` and :meth:`is_parabolic`
  (``preamble/.../integrallattice/coxeter_diagrams.sage``) are Coxeter's own
  words for what the spec called finite and affine type;
* :meth:`FiniteCoxeterDiagram.schlafli_matrix` is the literature matrix
  $C_{ij} = -2\cos(\pi/m_{ij})$, exact over $\overline{\mathbb Q}\cap\mathbb R$
  -- no floating cosine and no numerical tolerance, so the spec's ``1e-9``
  guards are gone rather than loosened;
* the hyperbolic families are decided on Vinberg invariants
  $t_{ij} = 4\cos^2(\pi/m_{ij})$ through
  ``CombinatorialVinbergInvariantMatrix`` (``vinberg_invariants.sage``), whose
  ``is_compact_hyperbolic`` is the Lannér condition and whose
  ``is_paracompact_hyperbolic`` reports the affine minor of a quasi-Lannér
  diagram.

**Convention, kept from the earlier correction on this file.** The literature
Schläfli matrix is $C_{ij} = -2\cos(\pi/m_{ij})$; this repository's Gram matrix
is $B_{ij} = +2\cos(\pi/m_{ij})$, so $B = -C$ -- the negative of $C$, not $C$
itself.  Elliptic therefore reads as positive definite on $C$ and as *negative*
definite on $B$, and $\det B = (-1)^n\det C$, so a determinant sign is a type
test only in even rank.  Sources: ``literature/PROJECT_CONVENTIONS.md``,
``literature/wikiwand/coxeter_schlaefli_matrices.md``,
``literature/wikipedia/schlaefli_determinants_by_family.md``.

The spec's Bogachev--Kolpakov rows are not reproduced here: those lattices are
catalogue specimens (``Lattices.BogachevKolpakovNonReflective`` and
``...WithoutRoots``) and their non-reflectivity, root lengths, and printed
Vinberg roots are asserted against the paper in
``tests/test_known_mathematics.sage``.  One fact per owner.
"""

import itertools

import pytest

from sage.all import AA, CoxeterMatrix, cos, infinity, matrix, pi

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


# The canonical finite types the spec parametrized over, with their ranks.
# ``H_2`` is not a Sage Cartan type; it is the dihedral $I_2(5)$ and appears
# below as an explicit Coxeter matrix instead.
CLASSICAL_TYPES = (
    [(["A", rank], rank) for rank in range(1, 8)]
    + [(["B", rank], rank) for rank in range(2, 8)]
    + [(["C", rank], rank) for rank in range(3, 8)]
    + [(["D", rank], rank) for rank in range(4, 8)]
)

# ``literature/wikipedia/schlaefli_determinants_by_family.md``: the Schläflian
# by family and rank.  $n+1$ for $A_n$, $2$ for $B_n$ and $C_n$, $4$ for $D_n$,
# $9-n$ for $E_n$, $5-n$ for $F_n$, $3-n$ for $G_n$.  $H_3$ and $H_4$ are not in
# the table and are not asserted.
FAMILY_SCHLAEFLIAN = {
    "A": lambda rank: rank + 1,
    "B": lambda rank: 2,
    "C": lambda rank: 2,
    "D": lambda rank: 4,
    "E": lambda rank: 9 - rank,
    "F": lambda rank: 5 - rank,
    "G": lambda rank: 3 - rank,
}

# Wikipedia, *Coxeter group*, oldid 1300325012, section "Properties": the
# exceptional finite irreducible Coxeter groups, by type and rank.
EXCEPTIONAL_TYPES = (
    ("E", 6),
    ("E", 7),
    ("E", 8),
    ("F", 4),
    ("G", 2),
    ("H", 3),
    ("H", 4),
)

# The subset whose order the owned surface can answer: ``coxeter_group()`` is
# Sage's ``CoxeterMatrixGroup``, whose ``order`` counts elements, so a group of
# 51840 elements upward is not asked for it here.  $|W(E_6)| = 51840$,
# $|W(E_7)| = 2903040$, $|W(E_8)| = 696729600$ and $|W(H_4)| = 14400$ are the
# tabulated values; the first three are asserted of Sage's ``WeylGroup``
# against Humphreys section 2.11 in ``tests/test_known_mathematics.sage``.
EXCEPTIONAL_ORDERS = {
    ("F", 4): 1152,
    ("G", 2): 12,
    ("H", 3): 120,
}


def _vinberg_invariant(bond: "Integer | PlusInfinity") -> "Element":
    r"""Return $t = 4\cos^2(\pi/m)$, the Vinberg invariant of a Coxeter bond.

    At $m = \infty$ the mirrors are parallel, $\cos 0 = 1$, and $t = 4$: the
    boundary value at which ``coxeter_order`` reads the bond back as infinite.
    """
    if bond is infinity:
        return AA(4)
    return AA(4 * cos(pi / bond) ** 2)


def _coxeter_triangle(
    first: "Integer | PlusInfinity",
    second: "Integer | PlusInfinity",
    third: "Integer | PlusInfinity",
) -> "Parent":
    r"""Return the rank-three Vinberg invariant matrix of the triangle whose
    bonds are $m_{01} = $ ``first``, $m_{12} = $ ``second``, $m_{02} = $
    ``third``.
    """
    t01, t12, t02 = (
        _vinberg_invariant(bond) for bond in (first, second, third)
    )
    return combinatorial_vinberg_invariant_matrix(
        AA,
        [[4, t01, t02], [t01, 4, t12], [t02, t12, 4]],
    )


def _proper_subsets(rank: int) -> "tuple[tuple[int, ...], ...]":
    r"""Return the nonempty proper index subsets of a rank-``rank`` diagram."""
    return tuple(
        subset
        for size in range(1, rank)
        for subset in itertools.combinations(range(rank), size)
    )


@pytest.mark.parametrize("cartan_type,rank", CLASSICAL_TYPES)
def test_classical_finite_types_are_elliptic_of_the_tabulated_schlaeflian(
    cartan_type: list, rank: int
) -> None:
    r"""Elliptic type is positive definiteness of $C$, at the family's
    determinant.

    Humphreys, *Reflection Groups and Coxeter Groups* (1990), Theorem 2.7.1: the
    Coxeter group is finite exactly when the standard Gram matrix of the
    reflection normals is positive definite.  The determinant is the per-family
    literature formula and separates the ranks: it is where the family's affine
    transition would be read off, and no finite member reaches it.
    """
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)
    schlafli = diagram.schlafli_matrix()

    assert diagram.cardinality() == rank
    assert diagram.is_elliptic()
    assert schlafli.is_positive_definite()
    assert schlafli.det() == FAMILY_SCHLAEFLIAN[cartan_type[0]](rank)


@pytest.mark.parametrize("cartan_type", EXCEPTIONAL_TYPES)
def test_exceptional_finite_types_are_elliptic_of_the_tabulated_rank(
    cartan_type: tuple,
) -> None:
    r"""The exceptional finite Coxeter diagrams, against the literature table.

    $H_3$ and $H_4$ are not crystallographic, so their Schläfli entries involve
    the golden ratio; the arithmetic stays exact because ``schlafli_matrix``
    builds $2\cos(\pi/m)$ as $\zeta + \zeta^{-1}$ in $\overline{\mathbb Q}$.
    The Schläflian is asserted for the families the determinant table covers.
    """
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])
    schlafli = diagram.schlafli_matrix()

    assert diagram.cardinality() == rank
    assert diagram.is_elliptic()
    assert schlafli.is_positive_definite()
    if letter in FAMILY_SCHLAEFLIAN:
        assert schlafli.det() == FAMILY_SCHLAEFLIAN[letter](rank)


@pytest.mark.parametrize("cartan_type", sorted(EXCEPTIONAL_ORDERS))
def test_exceptional_finite_groups_have_the_tabulated_order(
    cartan_type: tuple,
) -> None:
    r"""$|W(F_4)| = 1152$, $|W(G_2)| = 12$, $|W(H_3)| = 120$."""
    letter, rank = cartan_type
    diagram = CoxeterDiagrams().from_cartan_type([letter, rank])

    assert diagram.coxeter_group().order() == EXCEPTIONAL_ORDERS[cartan_type]


@pytest.mark.parametrize(
    "cartan_type", [["A", 1, 1], ["A", 2, 1], ["B", 3, 1], ["D", 4, 1]]
)
def test_affine_types_are_parabolic_with_a_vanishing_schlaeflian(
    cartan_type: list,
) -> None:
    r"""Parabolic type is positive semidefiniteness of $C$ of corank one.

    Humphreys (1990) Theorem 4.3.1 and Davis, *The Geometry and Topology of
    Coxeter Groups* (2008), Theorem 6.3.1.  Corank one is the whole condition:
    semidefiniteness alone is implied by definiteness, and without the corank
    clause every elliptic diagram would answer parabolic too.

    **Correction to the spec.** The spec excluded $\tilde A_1$ from this row as
    "reducible".  It is not: its diagram is two nodes joined by an edge labelled
    $\infty$, which is connected, and its Gram matrix $[[-2,2],[2,-2]]$ is
    indecomposable.  $\tilde A_1 = I_2(\infty)$ is the rank-two euclidean
    diagram and belongs in the affine roster
    (``literature/wikipedia/affine_coxeter_groups_witt_symbols.md``).  It is
    asserted here with the rest.
    """
    diagram = CoxeterDiagrams().from_cartan_type(cartan_type)
    schlafli = diagram.schlafli_matrix()

    assert diagram.is_parabolic()
    assert not diagram.is_elliptic(), "parabolic and elliptic are exclusive"
    assert diagram.is_connected(), "each of these affine diagrams is irreducible"
    assert schlafli.is_positive_semidefinite()
    assert schlafli.rank() == schlafli.nrows() - 1
    assert schlafli.det() == 0


def test_the_a2_schlaefli_matrix_is_the_negative_of_this_repositorys_gram_matrix() -> None:
    r"""$A_2$: $C = [[2,-1],[-1,2]]$ with eigenvalues $1, 3$; $B = -C$.

    The wikiwand capture's worked example, with the correction it records
    applied: the literature Schläfli matrix is $C_{ij} = -2\cos(\pi/M_{ij})$,
    giving $[[2,-1],[-1,2]]$, spectrum $\{1,3\}$, determinant $3$.  This
    repository's Gram matrix is the *negative* of that, $[[-2,1],[1,-2]]$, with
    spectrum $\{-1,-3\}$ and the same determinant $3$ (rank two is even).
    Finite type is positive definiteness of $C$ and negative definiteness of
    $B$; reading the negated spectrum through the un-negated rule is the error
    the capture corrects.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2])
    schlafli = diagram.schlafli_matrix()
    gram = Lattices.A2.gram_matrix()

    variable = schlafli.charpoly().parent().gen()

    assert schlafli == matrix(AA, [[2, -1], [-1, 2]])
    assert schlafli.charpoly() == (variable - 1) * (variable - 3), (
        "the literature spectrum {1, 3}, stated as the polynomial that has it"
    )
    assert schlafli.det() == 3

    assert gram == matrix([[-2, 1], [1, -2]])
    assert gram == -schlafli
    assert matrix(AA, gram).charpoly() == (variable + 1) * (variable + 3), (
        "the negated spectrum {-1, -3}"
    )
    assert gram.det() == 3

    assert schlafli.is_positive_definite()
    assert matrix(AA, gram).is_negative_definite()


@pytest.mark.parametrize(
    "bond,schlaeflian",
    [
        (2, AA(4)),
        (3, AA(3)),
        (4, AA(2)),
        (5, (5 - AA(5).sqrt()) / 2),
        (6, AA(1)),
    ],
)
def test_the_rank_two_schlaeflian_is_four_sine_squared(
    bond: int, schlaeflian: "Element"
) -> None:
    r"""$\det C = 4 - 4\cos^2(\pi/p) = 4\sin^2(\pi/p)$ for the diagram $[p]$.

    The rank-two table of
    ``literature/wikipedia/schlaefli_determinants_by_family.md``: $4$ for
    $I_2(2) = A_1\times A_1$, $3$ for $A_2$, $2$ for $B_2$, $(5-\sqrt5)/2$ for
    $H_2 = I_2(5)$, $1$ for $G_2$.  In rank two, and only there, the sign of the
    Schläflian settles the type outright, the determinant being the product of
    the two eigenvalues.
    """
    diagram = FiniteCoxeterDiagram(CoxeterMatrix([[1, bond], [bond, 1]]))
    schlafli = diagram.schlafli_matrix()

    assert schlafli.det() == schlaeflian
    assert diagram.is_elliptic()
    assert diagram.coxeter_group().order() == 2 * bond


def test_the_two_three_seven_triangle_is_a_lanner_simplex() -> None:
    r"""$[3,7]$ is compact hyperbolic: hyperbolic with every proper subdiagram
    elliptic.

    The reflection group of the hyperbolic triangle with angles $\pi/2$,
    $\pi/3$, $\pi/7$.  A connected diagram is hyperbolic when it is neither
    elliptic nor parabolic while every proper connected subdiagram is elliptic
    or parabolic, and **compact (Lannér)** when every proper subdiagram is
    elliptic (``literature/wikipedia/schlaefli_determinants_by_family.md``,
    "Hyperbolic subdivision").

    **Correction to the spec.** The spec named this group and then wrote its
    Coxeter matrix as the rank-two, non-symmetric ``[[1,3],[7,1]]``.  A
    hyperbolic triangle group has rank three -- one mirror per side -- and its
    Coxeter matrix is symmetric; in bracket notation $[3,7]$ is the path
    $m_{01}=3$, $m_{12}=7$, $m_{02}=2$.  The rank-two matrix $[[1,7],[7,1]]$
    would be the *finite* dihedral group $I_2(7)$.

    $m = 7$ is not crystallographic, so this diagram has no integral root
    realization; it is built from its Vinberg invariants
    $t_{ij} = 4\cos^2(\pi/m_{ij})$, exactly, over the real algebraic numbers.
    """
    lanner = _coxeter_triangle(3, 7, 2)

    assert lanner.is_coxeter()
    assert lanner.coxeter_order(0, 1) == 3
    assert lanner.coxeter_order(1, 2) == 7
    assert lanner.coxeter_order(0, 2) == 2
    assert not lanner.is_crystallographic(), "the bond 7 is not crystallographic"

    assert lanner.is_hyperbolic()
    assert not lanner.is_elliptic()
    assert not lanner.is_parabolic()
    assert lanner.is_compact_hyperbolic()
    assert not lanner.is_paracompact_hyperbolic(), (
        "a Lannér simplex is cocompact: it has no ideal vertex, "
        "so no proper subdiagram is parabolic"
    )

    for subset in _proper_subsets(3):
        assert lanner.is_elliptic(indices=subset), (
            f"every proper subdiagram of a Lannér simplex is elliptic; {subset}"
        )


def test_the_three_infinity_triangle_is_quasi_lanner() -> None:
    r"""$[3,\infty]$ is paracompact hyperbolic: hyperbolic, with one parabolic
    proper subdiagram and no non-elliptic others.

    The **quasi-Lannér** (Koszul) condition: hyperbolic with every proper
    subdiagram elliptic or parabolic, and at least one parabolic -- the ideal
    vertex that makes the simplex non-compact but still of finite volume
    (``literature/wikipedia/schlaefli_determinants_by_family.md``, "Hyperbolic
    subdivision").

    The parabolic subdiagram is the bond $m_{12} = \infty$, which is
    $\tilde A_1 = I_2(\infty)$ -- the same rank-two euclidean diagram the affine
    row above asserts.  ``is_paracompact_hyperbolic`` on the owned surface
    reports only that such a parabolic minor exists; the second half of the
    definition, that no proper subdiagram is worse than parabolic, is asserted
    here directly.
    """
    quasi = _coxeter_triangle(3, infinity, 2)

    assert quasi.is_coxeter()
    assert quasi.coxeter_order(0, 1) == 3
    assert quasi.coxeter_order(1, 2) == infinity
    assert quasi.coxeter_order(0, 2) == 2

    assert quasi.is_hyperbolic()
    assert quasi.is_paracompact_hyperbolic()
    assert not quasi.is_compact_hyperbolic()

    assert quasi.is_parabolic(indices=(1, 2)), "the ideal vertex"
    for subset in _proper_subsets(3):
        assert quasi.is_elliptic(indices=subset) or quasi.is_parabolic(
            indices=subset
        ), f"no proper subdiagram of a quasi-Lannér simplex is hyperbolic; {subset}"
