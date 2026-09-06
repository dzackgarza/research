r"""Vinberg invariants of mirrors, and the two hyperbolic families they decide.

The invariant of a pair of mirrors is the projective point
\([4b(r,s)^2 : q(r)q(s)]\), dehomogenized \(t = 4\cos^2(\pi/m)\).  These tests
state what the invariant knows that the Coxeter matrix does not, and check the
Lannér and quasi-Lannér conditions on the rank-three triangles where the
literature names the answer.

Sources: Vinberg, *Hyperbolic reflection groups*, Russian Math. Surveys 40
(1985), sections 1 and 4; Lannér, *On complexes with transitive groups of
automorphisms* (1950); Bourbaki, *Groupes et algèbres de Lie* VI.1.1 for the
crystallographic restriction.
"""

from sage.all import AA, CoxeterMatrix, Infinity, sqrt

from dzack_research.preamble.all import (
    CoxeterDiagrams,
    Lattices,
    VinbergInvariantMatrices,
    ZZ,
    reflection_cosines,
)


def rooted_diagram(gram_rows):
    r"""Return the rooted diagram of the rank-two lattice with this Gram."""
    return CoxeterDiagrams().from_roots(Lattices(ZZ)(gram_rows).module_generators())


def test_membership_in_the_reflection_cosines_is_decided_exactly() -> None:
    r"""\(\cos(\pi/n)\) is recognised in \(\overline{\mathbb Q}\), never by rounding.

    \(1/2 = \cos(\pi/3)\) and \((1+\sqrt5)/4 = \cos(\pi/5)\) are reflection
    cosines; \(1/3\) is not, and the test that says so is the multiplicative
    order of \(x + i\sqrt{1-x^2}\), which is infinite there.
    """
    cosines = reflection_cosines()

    assert AA(1) / 2 in cosines
    assert AA((1 + sqrt(5)) / 4) in cosines
    assert AA(1) / 3 not in cosines
    assert AA(0) in cosines, "cos(pi/2) = 0"

    # Position k of the enumeration carries n = k + 1.
    assert cosines.unrank(2) == AA(1) / 2
    assert cosines.unrank(4) == AA((1 + sqrt(5)) / 4)
    assert cosines.rank(AA(1) / 2) == 2
    assert cosines.rank(AA(0)) == 1


def test_the_invariant_of_a_root_pair_gives_back_the_coxeter_bond() -> None:
    r"""\(t = 0, 1, 2, 3\) are the bonds \(2, 3, 4, 6\).

    Read off actual root pairings: two roots of square \(-2\) pairing to
    \(1\) give \([4:4]\) and the bond \(3\); a root of square \(-2\) and one of
    square \(-4\) pairing to \(2\) give \([16:8]\) and the bond \(4\); squares
    \(-2\) and \(-6\) pairing to \(3\) give \([36:12]\) and the bond \(6\).
    """
    single = rooted_diagram([[-2, 1], [1, -2]]).vinberg_invariant_matrix()
    double = rooted_diagram([[-2, 2], [2, -4]]).vinberg_invariant_matrix()
    triple = rooted_diagram([[-2, 3], [3, -6]]).vinberg_invariant_matrix()

    assert single.vinberg_ratio(0, 1) == 1
    assert single.coxeter_entry(0, 1) == 3
    assert double.vinberg_ratio(0, 1) == 2
    assert double.coxeter_entry(0, 1) == 4
    assert triple.vinberg_ratio(0, 1) == 3
    assert triple.coxeter_entry(0, 1) == 6


def test_the_invariant_separates_parallel_mirrors_from_divergent_ones() -> None:
    r"""Both bonds are \(\infty\); the invariants are \(4\) and \(9\).

    The Coxeter matrix cannot tell the two configurations apart, because it
    records only that the mirrors fail to meet.  The invariant records how they
    fail: exactly \(4\) when they meet at a point of the boundary, and more
    when they have a common perpendicular instead.
    """
    parallel = rooted_diagram([[-2, 2], [2, -2]]).vinberg_invariant_matrix()
    divergent = rooted_diagram([[-2, 3], [3, -2]]).vinberg_invariant_matrix()

    assert parallel.coxeter_entry(0, 1) is Infinity
    assert divergent.coxeter_entry(0, 1) is Infinity
    assert parallel.coxeter_matrix() == divergent.coxeter_matrix()

    assert parallel.vinberg_ratio(0, 1) == 4
    assert divergent.vinberg_ratio(0, 1) == 9
    assert parallel.vinberg_invariant(0, 1) != divergent.vinberg_invariant(0, 1)


def test_the_invariant_does_not_move_when_the_mirrors_normals_are_rescaled() -> None:
    r"""The invariant is projective, so scaling the lattice does not change it.

    \(A_2\) and \(A_2(4)\) have the same mirrors and different normals: the
    numerator is multiplied by \(16\) and the denominator by \(16\).  Over
    \(\mathbb Z\) the two matrices agree as points of \(\mathbb P^1\), which no
    matrix of ring elements could record, the ratio \(4b^2/q q'\) being no
    integer in general.
    """
    plain = rooted_diagram([[-2, 1], [1, -2]]).vinberg_invariant_matrix()
    scaled = rooted_diagram([[-8, 4], [4, -8]]).vinberg_invariant_matrix()

    assert plain.vinberg_invariant(0, 1) == scaled.vinberg_invariant(0, 1)
    assert plain.coxeter_entry(0, 1) == scaled.coxeter_entry(0, 1) == 3


def test_the_crystallographic_and_simply_laced_conditions_read_the_bonds() -> None:
    r"""Crystallographic is \(m\in\{2,3,4,6,\infty\}\); simply laced is \(m\in\{2,3\}\).

    \(A_2\) is both.  \(B_2\), whose bond is \(4\), is crystallographic and not
    simply laced.  \(H_3\), whose bond is \(5\), is neither: \(4\cos^2(\pi/5)\)
    is irrational, so no lattice is preserved.
    """
    a2 = CoxeterDiagrams().from_cartan_type(["A", 2]).vinberg_invariant_matrix()
    b2 = CoxeterDiagrams().from_cartan_type(["B", 2]).vinberg_invariant_matrix()
    h3 = CoxeterDiagrams().from_cartan_type(["H", 3]).vinberg_invariant_matrix()

    assert a2.is_crystallographic()
    assert a2.is_simply_laced()

    assert b2.is_crystallographic()
    assert not b2.is_simply_laced()

    assert not h3.is_crystallographic()
    assert not h3.is_simply_laced()


def test_the_two_three_seven_triangle_is_a_lanner_diagram() -> None:
    r"""\(\Delta(2,3,7)\) is compact hyperbolic and not paracompact.

    Lannér's condition: the diagram is hyperbolic and every proper subdiagram
    is elliptic.  Deleting each of the three mirrors in turn leaves the bonds
    \(3\), \(2\) and \(7\), so the three vertex-deleted subdiagrams are
    \(A_2\), \(A_1\times A_1\) and \(I_2(7)\), all finite.  The simplex is
    therefore compact and the reflection group is cocompact.
    """
    diagram = CoxeterDiagrams().from_coxeter_matrix(
        CoxeterMatrix([[1, 7, 2], [7, 1, 3], [2, 3, 1]])
    )
    invariants = diagram.vinberg_invariant_matrix()

    assert diagram.is_hyperbolic()
    assert invariants.is_hyperbolic()
    assert invariants.is_compact_hyperbolic()
    assert not invariants.is_paracompact_hyperbolic()


def test_the_two_three_infinity_triangle_is_a_quasi_lanner_diagram() -> None:
    r"""\(\Delta(2,3,\infty)\) is paracompact hyperbolic and not compact.

    Vinberg's condition: hyperbolic, with every proper subdiagram positive
    semidefinite and at least one degenerate.  Deleting the mirrors leaves the
    bonds \(\infty\), \(2\) and \(3\); the first is the affine diagram
    \(\tilde A_1\), whose Schlaefli form has a radical, so the simplex has an
    ideal vertex.  It has finite volume and is not compact.
    """
    diagram = CoxeterDiagrams().from_coxeter_matrix(
        CoxeterMatrix([[1, 3, 2], [3, 1, -1], [2, -1, 1]])
    )
    invariants = diagram.vinberg_invariant_matrix()

    assert diagram.is_hyperbolic()
    assert invariants.coxeter_entry(1, 2) is Infinity
    assert invariants.vinberg_ratio(1, 2) == 4
    assert invariants.is_paracompact_hyperbolic()
    assert not invariants.is_compact_hyperbolic()


def test_the_invariant_matrix_restricts_and_draws_its_weighted_graph() -> None:
    r"""A submatrix is the invariant matrix of the selected mirrors.

    The weighted graph joins the pairs that are not orthogonal and labels each
    edge with the projective invariant of the pair, so an orthogonal pair is a
    missing edge and not an edge of weight zero.
    """
    diagram = CoxeterDiagrams().from_coxeter_matrix(
        CoxeterMatrix([[1, 7, 2], [7, 1, 3], [2, 3, 1]])
    )
    invariants = diagram.vinberg_invariant_matrix()

    assert invariants.cardinality() == 3
    assert invariants.weighted_graph().num_edges() == 2, "one pair is orthogonal"

    edge = invariants.submatrix((1, 2))
    assert edge.cardinality() == 2
    assert edge.coxeter_entry(1, 2) == 3
    assert edge.is_elliptic()


def test_the_invariant_matrix_can_be_stated_without_any_mirrors() -> None:
    r"""The combinatorial presentation states the invariants directly.

    A Vinberg invariant matrix is a matrix of angles, and a caller may write
    those angles down with no lattice behind them.  Here \(t=1\) throughout
    off the diagonal, so every bond is \(3\) and the diagram is the affine
    triangle \(\tilde A_2\).
    """
    invariants = VinbergInvariantMatrices().from_invariants(
        ZZ, [[4, 1, 1], [1, 4, 1], [1, 1, 4]]
    )

    assert invariants.cardinality() == 3
    assert invariants.coxeter_entry(0, 1) == 3
    assert invariants.is_crystallographic()
    assert invariants.is_simply_laced()
    assert invariants.is_parabolic()
    assert not invariants.is_hyperbolic()
    assert invariants.coxeter_diagram().schlaflian() == 0
