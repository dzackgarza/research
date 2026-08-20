r"""The Coxeter matrix and the root Gram matrix determine each other.

A Coxeter diagram's root Gram matrix is $B_{ij} = 2\cos(\pi/m_{ij})$ for the
Coxeter exponent $m_{ij}$: $-2$ on the diagonal ($m=1$), $0$ on a commuting
pair ($m=2$), $1$ on a single bond ($m=3$), and $2$ where the mirrors are
parallel ($m=\infty$).  That is this repository's sign.  The literature's
Schläfli matrix is $C_{ij} = -2\cos(\pi/m_{ij}) = -B$, and
``CoxeterDiagrams.ParentMethods.schlafli_matrix`` is the one place it is spelled.

Oracles for the fixture values below:

  - ``literature/PROJECT_CONVENTIONS.md`` in this corpus: $B_{ij} =
    2\cos(\pi/M_{ij})$, with $A_2$ giving $[[-2,1],[1,-2]]$.
  - ``literature/wikiwand/coxeter_schlaefli_matrices.md``: the literature
    Schläfli matrix $C_{ij} = -2\cos(\pi/M_{ij})$.

The owned surface is ``CoxeterDiagrams`` and ``CoxeterDiagrams`` in
``preamble/categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage``.
"""

from sage.all import AA, CoxeterMatrix, cos, matrix, pi, ZZ

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


def test_a2_root_gram_matrix_is_two_cosine_of_the_coxeter_angles() -> None:
    r"""$A_2$ realizes $B_{ij} = 2\cos(\pi/m_{ij})$ as $[[-2,1],[1,-2]]$.

    Two owned constructions of the same lattice are compared: the rooted
    diagram of the Cartan type at scale $1$, and the catalogue name ``A2``.
    They are built from different data -- the symmetrized Cartan matrix and
    the ambient inner products of the simple roots -- so their agreement is a
    statement, not a restatement.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2], scale=1)

    assert diagram.root_intersection_matrix() == matrix(ZZ, [[-2, 1], [1, -2]])
    assert diagram.root_intersection_matrix() == IntegralLattice("A2").gram_matrix()
    assert diagram.coxeter_matrix() == CoxeterMatrix([[1, 3], [3, 1]], index_set=(0, 1))

    exponents = ((1, 3), (3, 1))
    assert diagram.root_intersection_matrix() == matrix(
        ZZ, [[AA(2 * cos(pi / m)) for m in row] for row in exponents]
    )


def test_root_gram_matrix_is_the_negated_schlafli_matrix() -> None:
    r"""$B = -C$: the repository's Gram matrix negates the literature's.

    Determinants therefore agree only in even rank, $\det B = (-1)^n\det C$.
    Both parities are exercised: $A_2$ agrees at $3$, $A_1$ does not.
    """
    a2 = CoxeterDiagrams().from_cartan_type(["A", 2], scale=1)
    a1 = CoxeterDiagrams().from_cartan_type(["A", 1], scale=1)

    assert a2.root_intersection_matrix() == -a2.schlafli_matrix()
    assert a1.root_intersection_matrix() == -a1.schlafli_matrix()

    assert a2.schlafli_matrix() == matrix(AA, [[2, -1], [-1, 2]])
    assert a2.root_intersection_matrix().det() == a2.schlafli_matrix().det() == 3
    assert a1.root_intersection_matrix().det() == -2
    assert a1.schlafli_matrix().det() == 2


def test_commuting_roots_give_a_zero_entry_and_two_components() -> None:
    r"""$m=2$ gives $B_{ij} = 2\cos(\pi/2) = 0$, and the diagram splits.

    The specimen is the orthogonal edge of
    ``CoxeterDiagrams.minimal_edge_lattices``, which is $A_1\oplus A_1$: two
    commuting reflections, so the Gram matrix is the block sum of two copies
    of $\langle -2\rangle$ and the Coxeter graph has two components.
    """
    lattice = CoxeterDiagrams.minimal_edge_lattices()["orthogonal"]
    diagram = CoxeterDiagrams().from_roots(lattice.module_generators())

    assert diagram.root_intersection_matrix() == matrix(ZZ, [[-2, 0], [0, -2]])
    assert diagram.root_intersection_matrix()[0, 1] == AA(2 * cos(pi / 2)) == 0
    assert diagram.coxeter_matrix() == CoxeterMatrix([[1, 2], [2, 1]], index_set=(0, 1))
    assert len(diagram.connected_components()) == 2
    assert all(
        component.root_intersection_matrix() == matrix(ZZ, [[-2]])
        for component in diagram.connected_components()
    )
    assert diagram.is_elliptic()


def test_parallel_mirrors_give_the_entry_two_and_a_degenerate_form() -> None:
    r"""$m=\infty$ gives $B_{ij} = 2\cos 0 = 2$, and the form acquires a radical.

    The red-phase specification skipped this requirement for want of a
    representation of infinite order.  The owned surface has one: the
    ``parallel`` edge of ``CoxeterDiagrams.minimal_edge_lattices``, whose
    mirrors meet at infinity.  Its Schläfli entry is $-2$, its root Gram
    entry $+2$, and the form is degenerate -- which is the affine boundary,
    not a defect: this diagram is $\tilde A_1$.
    """
    lattice = CoxeterDiagrams.minimal_edge_lattices()["parallel"]
    diagram = CoxeterDiagrams().from_roots(lattice.module_generators())

    assert diagram.root_intersection_matrix() == matrix(ZZ, [[-2, 2], [2, -2]])
    assert diagram.root_intersection_matrix()[0, 1] == 2
    assert diagram.schlafli_matrix()[0, 1] == -2
    assert diagram.root_intersection_matrix().det() == 0
    assert not diagram.root_lattice().is_nondegenerate()
    assert diagram.is_parabolic()
    assert not diagram.is_elliptic()


def test_a1_is_the_rank_one_diagram() -> None:
    r"""$A_1$ is $\langle -2\rangle$, of determinant $-2$ and not $+2$.

    The sign is the whole content: the literature's rank-one Schläfli matrix
    is $[[2]]$, and odd rank is exactly where $\det B = -\det C$ bites.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 1], scale=1)

    assert diagram.root_intersection_matrix() == matrix(ZZ, [[-2]])
    assert diagram.root_lattice().rank() == 1
    assert diagram.cardinality() == 1
    assert diagram.root_intersection_matrix().det() == -2
    assert diagram.is_elliptic()


def test_b3_root_gram_matrix_is_symmetric_with_one_double_bond() -> None:
    r"""$B_3$ is connected, symmetric, and carries the exponents $3,4$.

    The red-phase specification checked symmetry entrywise to a floating
    tolerance of $10^{-9}$.  Symmetry of a Gram matrix is exact over
    $\mathbb Z$ and is asked of the matrix.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["B", 3], scale=1)
    gram = diagram.root_intersection_matrix()

    assert gram.is_symmetric()
    assert diagram.root_lattice().rank() == 3
    assert diagram.is_connected()
    assert diagram.is_elliptic()
    assert sorted(
        label for _left, _right, label in diagram.graph().edges(sort=True)
    ) == [3, 4]


def test_diagram_roots_have_negative_square() -> None:
    r"""Every root of a Coxeter diagram has negative square, here $-2$ or $-4$.

    This is the surviving content of the specification's "negative diagonal"
    requirement, which asked the constructor to *reject* a positive diagonal.
    That rejection would be false of this repository, which owns positive
    definite and indefinite lattices alike -- $\langle 2\rangle$ and $U$ are
    ordinary objects.  What the convention actually fixes is the sign of a
    *root*: mirrors of a reflection group, so $B_{ii} = 2\cos\pi = -2$, and
    ``minimal_edge_lattices`` records $-2$ and $-4$ as the only root squares
    that occur.
    """
    for cartan_type in (["A", 2], ["B", 3], ["D", 4], ["E", 8]):
        gram = CoxeterDiagrams().from_cartan_type(
            cartan_type, scale=1
        ).root_intersection_matrix()
        assert all(gram[i, i] < 0 for i in range(gram.nrows())), cartan_type

    squares = {
        edge.gram_matrix()[i, i]
        for edge in CoxeterDiagrams.minimal_edge_lattices().values()
        for i in (0, 1)
    }
    assert squares == {-2, -4}
