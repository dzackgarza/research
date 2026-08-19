r"""Invariants of a Coxeter diagram's root Gram matrix, and what they classify.

The determinant, rank, signature and spectrum of $B$ are what Coxeter's
classification reads: elliptic (finite) diagrams are negative definite here,
parabolic (euclidean) ones are negative semidefinite with a one-dimensional
radical, and the rest are indefinite.  The signs are inverted relative to the
literature because $B = -C$ for the Schläfli matrix $C$; see the module
docstring of ``test_matrix_construction.sage``.

Oracles for the fixture values below:

  - ``literature/PROJECT_CONVENTIONS.md``: $A_2$ has $B = [[-2,1],[1,-2]]$
    with eigenvalues $-3, -1$, against the literature's $+3, +1$.
  - ``literature/wikiwand/coxeter_schlaefli_matrices.md``: the triangle group
    $(3,3,3)$ is $A_2$; the square is the dihedral group of order $8$.
  - ``literature/wikipedia/finite_coxeter_group_invariants.md``: the order
    table for the finite Coxeter groups.

Definiteness is asked of ``signature_pair()``, which is Sylvester's law over
$\mathbb Q$, and not of eigenvalue signs; the eigenvalues appear only where
the literature quotes them as values.
"""

import pytest

from sage.all import AA, CoxeterMatrix, QQ, matrix, ZZ

from dzack_research.preamble.install import install_preamble

install_preamble(globals())


def test_a2_determinant_signature_and_discriminant() -> None:
    r"""$A_2$: $\det B = 3$, signature $(0,2)$, discriminant $-3$.

    The determinant and the discriminant differ in sign, and that is the
    point of the discriminant: $d_\pm = (-1)^{n(n-1)/2}\det G$ is the Witt
    invariant, so $A_2$ has discriminant $-3$ while its Gram determinant is
    $3$.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2], scale=1)
    lattice = diagram.root_lattice()

    assert lattice.gram_matrix().det() == 3
    assert lattice.signature_pair() == (0, 2)
    assert lattice.discriminant() == -3
    assert lattice.is_elliptic()
    assert diagram.is_elliptic()


def test_a2_eigenvalues_are_the_negatives_of_the_schlafli_eigenvalues() -> None:
    r"""$B$ has spectrum $\{-1,-3\}$ where the Schläfli matrix has $\{1,3\}$.

    Both are quoted in ``PROJECT_CONVENTIONS.md``; asserting them together is
    what makes the sign relation falsifiable rather than restated.  The
    Schläfli matrix is read over $\mathbb Z$: its entries are algebraic in
    general, but on a simply-laced diagram they are integers, and that is
    itself part of the claim.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2], scale=1)

    assert sorted(diagram.root_intersection_matrix().eigenvalues()) == [-3, -1]
    assert sorted(diagram.schlafli_matrix().change_ring(ZZ).eigenvalues()) == [1, 3]


def test_a_series_ranks_and_determinants() -> None:
    r"""$A_n$ has rank $n$ and $\det B = (-1)^n(n+1)$.

    The unsigned value $n+1$ is the order of the discriminant group of
    $A_n$; the sign is the parity carried in from $B = -C$.
    """
    for rank, determinant in ((1, -2), (2, 3), (3, -4), (4, 5)):
        lattice = CoxeterDiagrams().from_cartan_type(
            ["A", rank], scale=1
        ).root_lattice()

        assert lattice.rank() == rank, rank
        assert lattice.gram_matrix().det() == determinant, rank


def test_elliptic_diagrams_are_negative_definite() -> None:
    r"""A diagram is elliptic exactly when its root lattice is negative definite.

    Two independent routes to the same classification: the diagram asks
    Sage's Coxeter classification whether the group is finite, the lattice
    asks whether $-G$ is positive definite.  They are computed from different
    data and must agree.
    """
    for cartan_type in (["A", 2], ["B", 3], ["D", 4], ["F", 4], ["G", 2]):
        diagram = CoxeterDiagrams().from_cartan_type(cartan_type, scale=1)
        lattice = diagram.root_lattice()

        assert diagram.is_elliptic(), cartan_type
        assert lattice.is_elliptic(), cartan_type
        assert lattice.signature_pair() == (0, lattice.rank()), cartan_type


def test_affine_a2_root_gram_matrix_is_singular_and_the_diagram_is_parabolic() -> None:
    r"""$\tilde A_2$ has $\det B = 0$ and is parabolic, not elliptic.

    The red-phase specification tested singularity as
    ``abs(determinant()) < 1e-10``.  The determinant of an integral Gram
    matrix is an integer and is zero exactly, so the tolerance is dropped.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["A", 2, 1], scale=1)
    lattice = diagram.root_lattice()

    assert lattice.gram_matrix() == matrix(
        ZZ, [[-2, 1, 1], [1, -2, 1], [1, 1, -2]]
    )
    assert lattice.gram_matrix().det() == 0
    assert not lattice.is_nondegenerate()
    assert diagram.is_parabolic()
    assert not diagram.is_elliptic()


@pytest.mark.xfail(
    strict=True,
    reason=(
        "a degenerate lattice is not refined into IntegralLattices "
        "(refine_one_lattice in integral_lattices.sage stops at "
        "Lattices(ZZ).Integral()), so signature_pair() -- an "
        "IntegralLattices.ParentMethods method -- does not resolve on a "
        "parabolic root lattice; the missing degenerate/parabolic category "
        "is recorded in notes/category-design/lattice-categories-roster.md"
    ),
)
def test_affine_a2_root_lattice_has_signature_zero_two_one() -> None:
    r"""$\tilde A_2$ is negative semidefinite with a one-dimensional radical.

    Signature $(p,q,r) = (0,2,1)$: two negative directions and the radical
    that makes the diagram parabolic rather than elliptic.  ``signature_pair``
    returns $(p,q)$ and the radical dimension is $n - p - q$.
    """
    lattice = CoxeterDiagrams().from_cartan_type(
        ["A", 2, 1], scale=1
    ).root_lattice()

    positive, negative = lattice.signature_pair()

    assert (positive, negative, lattice.rank() - positive - negative) == (0, 2, 1)


def test_a_hyperbolic_edge_has_negative_determinant_and_mixed_signature() -> None:
    r"""Ultraparallel mirrors give an indefinite rank-two lattice.

    The red-phase specification left the hyperbolic case an empty skip for
    want of an example.  The owned surface names one: the ``ultraparallel``
    edge of ``CoxeterDiagrams.minimal_edge_lattices``, where the two mirrors
    diverge.  Its form is nondegenerate and indefinite -- signature $(1,1)$,
    determinant $4 - 9 = -5$ -- so the diagram is neither elliptic nor
    parabolic.
    """
    lattice = CoxeterDiagrams.minimal_edge_lattices()["ultraparallel"]
    diagram = FiniteCoxeterDiagram.from_roots(lattice.module_generators())

    assert lattice.gram_matrix() == matrix(ZZ, [[-2, 3], [3, -2]])
    assert lattice.gram_matrix().det() == -5
    assert lattice.is_nondegenerate()
    assert lattice.signature_pair() == (1, 1)
    assert not diagram.is_elliptic()
    assert not diagram.is_parabolic()


def test_triangle_group_333_is_the_a2_schlafli_matrix() -> None:
    r"""The $(3,3,3)$ triangle is $A_2$, with Schläfli matrix $[[2,-1],[-1,2]]$.

    The Wikiwand example, read on the owned surface: a triangle with angles
    $\pi/3$ has Coxeter matrix $[[1,3],[3,1]]$, Schläfli matrix
    $[[2,-1],[-1,2]]$ of determinant $3$, and this repository's $B$ is its
    negative.  Determinants agree here only because the rank is even.
    """
    diagram = FiniteCoxeterDiagram(CoxeterMatrix([[1, 3], [3, 1]]))

    assert diagram.schlafli_matrix() == matrix(AA, [[2, -1], [-1, 2]])
    assert diagram.schlafli_matrix().det() == 3
    assert diagram.is_elliptic()
    assert diagram.coxeter_group().order() == 6


def test_square_group_is_the_dihedral_group_of_order_eight() -> None:
    r"""The square is $I_2(4)$, elliptic of order $8$.

    The Wikiwand square example.  Its Coxeter matrix $[[1,4],[4,1]]$ is
    written directly rather than through a Cartan-type name, because $I_2(4)$
    and $B_2$ name the same Coxeter system and the claim here is about the
    system, not about which spelling Sage prefers.
    """
    diagram = FiniteCoxeterDiagram(CoxeterMatrix([[1, 4], [4, 1]]))

    assert diagram.is_elliptic()
    assert diagram.coxeter_group().order() == 8
    assert diagram.schlafli_matrix() == matrix(
        AA, [[2, -AA(2).sqrt()], [-AA(2).sqrt(), 2]]
    )


def test_a_gram_matrix_must_be_symmetric() -> None:
    r"""A bilinear form on a lattice is symmetric, so a non-symmetric Gram is refused.

    The specimen corrupts the canonical $A_2$ matrix in one entry, so the
    only thing that changed is the symmetry.
    """
    with pytest.raises(AssertionError, match="symmetric"):
        IntegralLattice(matrix(ZZ, [[-2, 1], [2, -2]]))


def test_an_integral_lattice_must_have_integral_gram_entries() -> None:
    r"""Halving the $A_2$ Gram matrix leaves no integral lattice.

    $\frac12 B$ is a perfectly good rational form; what it is not is a form
    with values in $\mathbb Z$, and ``IntegralLattice`` is the $\mathbb Z$-valued
    one.
    """
    with pytest.raises(TypeError):
        IntegralLattice(matrix(QQ, [[-1, QQ(1) / 2], [QQ(1) / 2, -1]]))
