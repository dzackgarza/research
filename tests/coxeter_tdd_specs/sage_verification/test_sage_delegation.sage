r"""The Coxeter classification seams where the preamble delegates to Sage.

``FiniteCoxeterDiagram`` answers four questions by handing them to Sage:
``is_elliptic``/``is_parabolic`` to ``CoxeterMatrix``'s classification,
``coxeter_group`` to ``CoxeterGroup`` on that same matrix, the rooted
realization of a Cartan type to the symmetrized Cartan matrix, and
``schlafli_matrix`` to exact algebraic arithmetic in ``AA``.  A break at one
of those seams is a preamble bug or a change of convention, and either one
must be visible.  So every assertion below states the *literature* value and
asks the owned surface for it; Sage is the compute engine, never the oracle.

Sources (each transcribed in this corpus, revision-pinned):

  - ``literature/wikipedia/finite_coxeter_group_invariants.md``
    (`wikipedia_coxeter_groups_2025`, oldid 1300325012).  The invariant table
    of the finite irreducible Coxeter groups: order, Coxeter number $h$, and
    the number of reflections $m = nh/2$, which is also the number of
    positive roots.  It also records the exceptional isomorphisms
    $I_2(3)\cong A_2$, $I_2(4)\cong B_2$, $I_2(6)\cong G_2$.
  - ``literature/wikipedia/schlaefli_determinants_by_family.md``
    (`wikipedia_coxeter_dynkin_2025`, oldid 1290398091).  The Schläflian
    $\det C$ as a function of rank, per family, in the literature convention
    $C_{ij} = -2\cos(\pi/m_{ij})$.
  - ``literature/PROJECT_CONVENTIONS.md``.  This repository's Gram matrix is
    $B = -C$: roots have negative square, elliptic reads as negative
    definite, and $\det B = (-1)^n \det C$.
  - J. E. Humphreys, *Reflection Groups and Coxeter Groups* (1990), Hum90:
    the longest element of a finite Coxeter group has length $|\Phi^+|$, and
    $|W|$ is the product of the degrees of the basic invariants.

Rewritten 2026-08-20 from the red-phase file ``test_sage_cross_validation.py``,
which asserted a never-built ``coxeter_matrices.GramMatrix`` against Sage
recomputed inside the test.  The requirements are the same ones; the oracle is
now the literature and the surface under test is the preamble.
"""

import pytest

from sage.all import AA, CoxeterMatrix, matrix, prod, ZZ

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


# The invariant table, transcribed from
# ``literature/wikipedia/finite_coxeter_group_invariants.md``:
# Coxeter type -> (order |W|, Coxeter number h, reflections m = nh/2).
FINITE_INVARIANTS = {
    ("A", 1): (2, 2, 1),
    ("A", 2): (6, 3, 3),
    ("A", 3): (24, 4, 6),
    ("A", 4): (120, 5, 10),
    ("A", 5): (720, 6, 15),
    ("B", 2): (8, 4, 4),
    ("B", 3): (48, 6, 9),
    ("B", 4): (384, 8, 16),
    ("D", 4): (192, 6, 12),
    ("D", 5): (1920, 8, 20),
    ("E", 6): (51840, 12, 36),
    ("E", 7): (2903040, 18, 63),
    ("E", 8): (696729600, 30, 120),
    ("F", 4): (1152, 12, 24),
    ("G", 2): (12, 6, 6),
    ("H", 3): (120, 10, 15),
    ("H", 4): (14400, 30, 60),
    ("I", 5): (10, 5, 5),
    ("I", 7): (14, 7, 7),
}

# Enumerating $W$ is enumerating its elements: ``CoxeterMatrixGroup.order``
# counts them one by one.  These are the types whose enumeration is over in a
# moment; the rest are asserted through their degrees, below.
ENUMERABLE_TYPES = (
    ("A", 1), ("A", 2), ("A", 3), ("A", 4),
    ("B", 2), ("B", 3), ("B", 4),
    ("D", 4),
    ("G", 2),
    ("H", 3),
    ("I", 5), ("I", 7),
)


def test_the_schlafli_matrix_is_the_literature_sign_and_the_root_gram_its_negative() -> None:
    r"""$C_{ij}=-2\cos(\pi/m_{ij})$ and $B=-C$ on a simply laced diagram.

    ``PROJECT_CONVENTIONS.md`` writes both matrices out for $A_2$: the
    literature's $C=[[2,-1],[-1,2]]$ and this repository's
    $B=[[-2,1],[1,-2]]$.  On a simply laced diagram every root has the same
    square, so the two differ by the global sign and nothing else -- which is
    what makes the determinant rows below transferable.
    """
    a2 = CoxeterDiagrams().from_cartan_type(["A", 2])

    assert a2.schlafli_matrix() == matrix(AA, [[2, -1], [-1, 2]])

    for cartan_type in (["A", 2], ["A", 4], ["D", 4], ["E", 6]):
        rooted = FiniteCoxeterDiagram.from_cartan_type(cartan_type, scale=1)
        gram = rooted.root_intersection_matrix()
        assert gram.change_ring(AA) == -rooted.schlafli_matrix(), (
            f"{cartan_type}: the root Gram matrix is not -C"
        )
        assert all(gram[i, i] == -2 for i in range(gram.nrows())), (
            f"{cartan_type}: simply laced roots have square -2 in this convention"
        )

    assert FiniteCoxeterDiagram.from_cartan_type(
        ["A", 2], scale=1
    ).root_intersection_matrix() == matrix(ZZ, [[-2, 1], [1, -2]])


def test_the_schlaflian_of_each_finite_family_matches_the_published_table() -> None:
    r"""$\det C$ by family: $A_n\mapsto n+1$, $B_n\mapsto 2$, $D_n\mapsto 4$,
    $E_n\mapsto 9-n$, $F_n\mapsto 5-n$, $G_n\mapsto 3-n$.

    The rows of ``schlaefli_determinants_by_family.md``, asked of
    :meth:`schlafli_matrix`.  $B_n$, $F_4$ and $G_2$ are the interesting ones:
    their Schläfli matrices leave $\mathbb Q$ -- $-\sqrt2$ and $-\sqrt3$
    appear -- so a determinant of exactly $2$ or $1$ is also the statement
    that the entries were built exactly and no cosine was floated.
    """
    schlaflians = {
        ("A", 1): 2, ("A", 2): 3, ("A", 3): 4, ("A", 4): 5, ("A", 5): 6,
        ("B", 2): 2, ("B", 3): 2, ("B", 4): 2, ("B", 5): 2,
        ("D", 4): 4, ("D", 5): 4, ("D", 6): 4,
        ("E", 6): 3, ("E", 7): 2, ("E", 8): 1,
        ("F", 4): 1,
        ("G", 2): 1,
    }

    for cartan_type, schlaflian in schlaflians.items():
        diagram = CoxeterDiagrams().from_cartan_type(list(cartan_type))
        assert diagram.schlafli_matrix().determinant() == schlaflian, (
            f"{cartan_type}: Schläflian is not {schlaflian}"
        )


def test_the_dihedral_schlaflian_is_four_sine_squared_and_stays_algebraic() -> None:
    r"""$\det C = 4\sin^2(\pi/p)$ for the rank-two diagram $[p]$.

    The table's rank-two row, including the two irrational cases it prints:
    $p=5$ gives $(5-\sqrt5)/2$ and $p=4$ gives $2$.  Asserted in $AA$ against
    the closed form, which is exactly the requirement the red-phase file
    called "numerical precision": there is no tolerance here because there is
    no floating point.
    """
    for bond, schlaflian in (
        (2, AA(4)),
        (3, AA(3)),
        (4, AA(2)),
        (5, (5 - AA(5).sqrt()) / 2),
        (6, AA(1)),
    ):
        diagram = CoxeterDiagrams().from_coxeter_matrix(
            CoxeterMatrix([[1, bond], [bond, 1]])
        )
        assert diagram.schlafli_matrix().determinant() == schlaflian, (
            f"I_2({bond}): Schläflian is not {schlaflian}"
        )


@pytest.mark.xfail(
    strict=True,
    reason=(
        "defect on the owned surface: FiniteCoxeterDiagram.schlafli_matrix "
        "documents the entry -2 at an infinite bond, but reads the exponent "
        "through CoxeterMatrix.__getitem__, which returns Sage's internal -1 "
        "rather than +Infinity (only coxeter_graph() converts).  So "
        "_schlafli_entry receives -1 and its bond assertion fires."
    ),
)
def test_a_parallel_pair_has_the_schlafli_entry_minus_two() -> None:
    r"""$C = [[2,-2],[-2,2]]$, $\det C = 0$, for $I_2(\infty)$.

    The last row of the rank-two table: $m=\infty$ means the mirrors are
    parallel, $\cos 0 = 1$, and the Schläflian vanishes -- the rank-two case
    where a zero determinant is exactly the affine boundary.  This is the
    only bond the corpus asks for that the diagram cannot yet answer.
    """
    parallel = CoxeterDiagrams().from_coxeter_matrix(
        CoxeterMatrix([[1, -1], [-1, 1]])
    )

    assert parallel.schlafli_matrix() == matrix(AA, [[2, -2], [-2, 2]])
    assert parallel.schlafli_matrix().determinant() == 0
    assert parallel.is_elliptic() is False


def test_the_root_lattice_determinant_carries_the_convention_sign() -> None:
    r"""$\det B = (-1)^n\det C$ on the named root lattices.

    The catalogue's $A_n$, $D_n$, $E_n$ are negative definite, so the
    published Schläflians reach them through the sign rule stated in
    ``schlaefli_determinants_by_family.md``.  $E_8$ landing on $+1$ is the
    unimodularity of $E_8$; $E_{10}=U\oplus E_8$ landing on $-1$ is the
    family formula $9-n$ continued past the affine member $E_9$, and it is
    asserted here of a lattice the catalogue builds by an entirely different
    route.
    """
    for name, rank, schlaflian in (
        ("A1", 1, 2), ("A2", 2, 3), ("A3", 3, 4), ("A4", 4, 5),
        ("D4", 4, 4), ("D5", 5, 4),
        ("E6", 6, 3), ("E7", 7, 2), ("E8", 8, 1),
    ):
        lattice = getattr(Lattices, name)
        assert lattice.gram_matrix().determinant() == (-1) ** rank * schlaflian, (
            f"{name}: determinant does not carry the convention sign"
        )

    assert Lattices.E10.gram_matrix().determinant() == -1


def test_the_schlaflian_of_a_family_as_a_function_of_rank() -> None:
    r"""$\det C$ stays $n+1$ for $A_n$ and $4$ for $D_n$ out to rank 20.

    The published rows are claims about the whole family, not about the small
    members, so they are asked at ranks the small tables never reach.  (This
    is what survives of the red-phase "large rank stress test": the claim it
    could actually falsify was the family determinant, and everything else it
    measured was elapsed time.)
    """
    for rank in range(10, 21):
        assert getattr(Lattices, f"A{rank}").gram_matrix().determinant() == (
            (-1) ** rank * (rank + 1)
        ), f"A{rank}: Schläflian is not {rank + 1}"
        assert getattr(Lattices, f"D{rank}").gram_matrix().determinant() == (
            (-1) ** rank * 4
        ), f"D{rank}: Schläflian is not 4"


def test_the_finite_coxeter_groups_have_their_published_orders() -> None:
    r"""$|W|$ from the invariant table, through ``coxeter_group()``.

    The seam: ``coxeter_group()`` hands this diagram's own Coxeter matrix to
    Sage's ``CoxeterGroup``, so the order is a statement about the matrix the
    preamble built, not about the Cartan type it was named by.
    """
    for cartan_type in ENUMERABLE_TYPES:
        order, _h, _reflections = FINITE_INVARIANTS[cartan_type]
        diagram = CoxeterDiagrams().from_cartan_type(list(cartan_type))
        assert diagram.coxeter_group().order() == order, (
            f"{cartan_type}: |W| is not {order}"
        )


def test_the_large_exceptional_orders_come_from_the_degrees() -> None:
    r"""$|W| = \prod_i d_i$ for $E_6$, $E_7$, $E_8$, $F_4$, $H_4$ [Hum90].

    $|W(E_8)| = 696729600$ is a published number that no enumeration will
    ever confirm: ``CoxeterMatrixGroup.order`` counts elements one at a time.
    The invariant-theoretic identity gives the same claim from the degrees of
    the basic invariants, which are read off one Coxeter element's
    characteristic polynomial.  The largest degree is the Coxeter number, so
    the table's $h$ column is asserted here too.
    """
    for cartan_type in (("E", 6), ("E", 7), ("E", 8), ("F", 4), ("H", 4)):
        order, coxeter_number, _reflections = FINITE_INVARIANTS[cartan_type]
        degrees = CoxeterDiagrams().from_cartan_type(
            list(cartan_type)
        ).coxeter_group().degrees()
        assert prod(degrees) == order, f"{cartan_type}: |W| is not {order}"
        assert max(degrees) == coxeter_number, (
            f"{cartan_type}: h is not {coxeter_number}"
        )

    assert CoxeterDiagrams().from_cartan_type(
        ["E", 8]
    ).coxeter_group().degrees() == (2, 8, 12, 14, 18, 20, 24, 30)


def test_the_longest_element_has_one_reflection_per_positive_root() -> None:
    r"""$\ell(w_0) = |\Phi^+| = nh/2$ [Hum90], against the table's $m$ column.

    The red-phase file compared its own longest element with Sage's; the
    claim underneath was that the length is the published reflection count,
    which is what is asserted here.
    """
    for cartan_type in (("A", 3), ("B", 3), ("D", 4), ("G", 2), ("H", 3), ("I", 5)):
        _order, _h, reflections = FINITE_INVARIANTS[cartan_type]
        weyl_group = CoxeterDiagrams().from_cartan_type(
            list(cartan_type)
        ).coxeter_group()
        assert weyl_group.long_element().length() == reflections, (
            f"{cartan_type}: l(w_0) is not {reflections}"
        )


def test_a_root_lattice_knows_its_roots_its_positive_roots_and_its_height() -> None:
    r"""$|\Phi| = 2m$, $|\Phi^+| = m$, and $\operatorname{ht}(\theta) = h-1$.

    The root lattice answers with vectors, not with a comparison against
    another root system: the roots are the vectors of the simple roots'
    square, positivity is the sign of the coordinates over the simple system,
    and the highest root's height is one less than the Coxeter number
    (Hum90; the $m$ and $h$ columns of the invariant table).
    """
    for name, cartan_type in (("A3", ("A", 3)), ("D4", ("D", 4)), ("E6", ("E", 6))):
        _order, coxeter_number, reflections = FINITE_INVARIANTS[cartan_type]
        lattice = getattr(Lattices, name)

        roots = lattice.roots()
        assert roots.cardinality() == 2 * reflections, (
            f"{name}: the root system does not have {2 * reflections} roots"
        )
        positive = [root for root in roots if root.is_positive_root()]
        assert len(positive) == reflections, (
            f"{name}: there are not {reflections} positive roots"
        )
        assert lattice.coxeter_number() == coxeter_number
        assert lattice.highest_root().height() == coxeter_number - 1
        assert lattice.highest_root().is_positive_root() is True


def test_every_finite_type_is_elliptic_and_its_affine_extension_parabolic() -> None:
    r"""Coxeter's classification, over the whole finite irreducible list.

    ``is_elliptic`` is $W$ finite and ``is_parabolic`` is every component
    affine; both are delegated to ``CoxeterMatrix``.  The affine extension of
    a finite type has Schläflian $0$ -- one eigenvalue leaves -- which is the
    table's transition row, so the two answers are checked against each other
    and against the determinant.
    """
    for cartan_type in FINITE_INVARIANTS:
        diagram = CoxeterDiagrams().from_cartan_type(list(cartan_type))
        assert diagram.is_elliptic() is True, f"{cartan_type} is not elliptic"
        assert diagram.is_parabolic() is False
        assert diagram.schlafli_matrix().determinant() > 0

    for cartan_type in (["A", 2, 1], ["B", 3, 1], ["D", 4, 1], ["E", 8, 1], ["G", 2, 1]):
        affine = CoxeterDiagrams().from_cartan_type(cartan_type)
        assert affine.is_parabolic() is True, f"{cartan_type} is not parabolic"
        assert affine.is_elliptic() is False
        assert affine.schlafli_matrix().determinant() == 0


def test_the_exceptional_dihedral_isomorphisms_are_visible_in_the_bonds() -> None:
    r"""$I_2(3)\cong A_2$, $I_2(4)\cong B_2$, $I_2(6)\cong G_2$.

    Built from bare Coxeter matrices, so nothing here is Sage's normalization
    of the Cartan type ``['I', 6]`` into ``['G', 2]``: the claim is that the
    rank-two diagram with bond $p$ carries the same bond as the named
    crystallographic diagram, and presents a group of order $2p$.
    """
    for bond, cartan_type in ((3, ["A", 2]), (4, ["B", 2]), (6, ["G", 2])):
        dihedral = CoxeterDiagrams().from_coxeter_matrix(
            CoxeterMatrix([[1, bond], [bond, 1]])
        )
        named = CoxeterDiagrams().from_cartan_type(cartan_type)

        assert [
            label for _left, _right, label in dihedral.graph().edges(sort=True)
        ] == [label for _left, _right, label in named.graph().edges(sort=True)]
        assert dihedral.coxeter_group().order() == 2 * bond
        assert named.coxeter_group().order() == 2 * bond


@pytest.mark.xfail(
    strict=True,
    reason=(
        "gap on the owned surface: Lattices.root_lattice admits only the "
        "simply laced families A, D, E, so F_4 and G_2 -- root lattices over "
        "ZZ like the others -- have no named specimen.  Their Gram data is "
        "reachable only through FiniteCoxeterDiagram.from_cartan_type(..., "
        "scale=1).root_intersection_matrix()."
    ),
)
def test_the_non_simply_laced_root_lattices_are_named_specimens() -> None:
    r"""$Q(F_4)$ and $Q(G_2)$ as lattices, not as diagram data.

    $Q(F_4)$ is the $D_4$ lattice and $Q(G_2)$ is $A_2$ rescaled; both are
    ordinary integral lattices, and the corpus asked for them alongside the
    $E$-series.  Until the catalogue admits them the requirement stands here,
    failing.
    """
    assert Lattices.root_lattice("F", 4).gram_matrix().determinant() == 4
    assert Lattices.root_lattice("G", 2).gram_matrix().determinant() == 3


@pytest.mark.xfail(
    strict=True,
    reason=(
        "gap on the owned surface: the non-crystallographic root systems H_3 "
        "and H_4 need a form module over ZZ[phi], and every owned lattice is "
        "over ZZ.  Their Schläfli matrices exist in AA (asserted above), but "
        "a matrix is not a form module: it has no Aut, no discriminant "
        "group, and no roots."
    ),
)
def test_the_icosahedral_root_systems_are_form_modules_over_the_golden_ring() -> None:
    r"""$H_3$ over $\mathbb Z[\varphi]$, with its $30$ roots.

    The invariant table gives $m = 15$, so $|\Phi| = 30$ -- the icosahedral
    root system.  The requirement is the object, not the matrix.
    """
    icosahedral = Lattices.root_lattice("H", 3)

    assert icosahedral.roots().cardinality() == 30
    assert icosahedral.coxeter_number() == 10
