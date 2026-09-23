r"""Subdiagram posets, automorphism orbits, and the root data behind a diagram.

The affine \(A_2\) diagram is the working specimen: a triangle with every bond
\(3\), whose automorphism group is the symmetric group on its three vertices.
Its subdiagram lattice is small enough to name in full, and the counts
distinguish the elliptic subdiagrams from the parabolic one.
"""

from sage.all import Infinity

from dzack_research.preamble.all import ZZ, CoxeterDiagrams, Lattices, finite_ordered_set


def affine_a2():
    r"""Return the affine \(A_2\) diagram: the triangle with every bond three."""
    return CoxeterDiagrams().from_cartan_type(["A", 2, 1])


def test_the_affine_triangle_has_seven_elliptic_and_one_parabolic_subdiagram() -> None:
    r"""The subdiagrams of the affine \(A_2\) triangle, counted by type.

    The eight induced subdiagrams are the empty one, three vertices, three
    edges and the triangle.  The first seven are elliptic: each is a diagram of
    type \(A_0\), \(A_1\) or \(A_2\).  The triangle alone is parabolic, being
    the affine diagram itself.
    """
    diagram = affine_a2()

    assert diagram.cardinality() == 3
    assert diagram.subdiagram_poset().cardinality() == 8
    assert diagram.elliptic_subdiagrams().cardinality() == 7
    assert diagram.parabolic_subdiagrams().cardinality() == 1
    assert diagram.is_parabolic()




def test_the_maximal_elliptic_subdiagrams_of_the_affine_triangle_are_its_edges() -> None:
    r"""Each edge of the triangle is a maximal elliptic subdiagram.

    An edge is of type \(A_2\); the only subdiagram strictly above it is the
    triangle, which is parabolic.  A vertex is not maximal, being below an
    edge, and neither is the empty subdiagram.
    """
    diagram = affine_a2()
    maximal = diagram.maximal_elliptic_subdiagrams()

    assert maximal.cardinality() == 3
    for edge in maximal:
        assert edge.cardinality() == 2
        assert edge.is_elliptic()
        assert edge.is_connected()


def test_the_symmetric_group_on_the_triangle_fuses_the_subdiagrams_into_three_orbits() -> None:
    r"""\(\operatorname{Aut}\) of the affine \(A_2\) diagram is \(S_3\).

    Every permutation of the three vertices preserves every bond, so the
    automorphism group has order six and acts transitively on the vertices and
    on the edges.  The elliptic subdiagrams therefore fall into three orbits:
    the empty one, the three vertices, and the three edges.
    """
    diagram = affine_a2()

    assert diagram.Aut().order() == 6
    assert diagram.elliptic_subdiagram_orbits().cardinality() == 3
    assert diagram.parabolic_subdiagram_orbits().cardinality() == 1
    assert diagram.subdiagram_orbits().cardinality() == 4
    assert diagram.maximal_parabolic_subdiagrams().cardinality() == 1


def test_triality_orders_the_subdiagram_orbits_of_d4_by_the_orbit_relation() -> None:
    r"""The orbit order on the elliptic subdiagrams of \(D_4\).

    \(D_4\) is a star: the centre \(2\) joined to the three outer nodes
    \(1,3,4\), every bond three, so \(\operatorname{Aut}\) is the symmetric
    group on the outer nodes, of order six.  Every induced subdiagram of a
    finite-type diagram is finite type, hence elliptic, so all sixteen vertex
    subsets appear and an orbit is fixed by whether it holds the centre and by
    how many outer nodes it holds: eight orbits.

    The order is on orbits, not on representatives: \([H]\leq[K]\) when some
    member of \([H]\) is an induced subdiagram of some member of \([K]\).  The
    claims below are what that order says about the star.  The centre is in no
    subdiagram spanned by outer nodes, so its orbit is not below the orbit of
    the three outer nodes even though it is smaller; an outer node and a pair
    of outer nodes are.
    """
    diagram = CoxeterDiagrams().from_cartan_type(["D", 4])

    assert diagram.Aut().order() == 6
    assert diagram.elliptic_subdiagrams().cardinality() == 16

    poset = diagram.elliptic_subdiagram_orbit_poset()
    expected_indices = finite_ordered_set(
        (
            finite_ordered_set(()),
            finite_ordered_set((1,)),
            finite_ordered_set((2,)),
            finite_ordered_set((1, 2)),
            finite_ordered_set((1, 3)),
            finite_ordered_set((1, 2, 3)),
            finite_ordered_set((1, 3, 4)),
            finite_ordered_set((1, 2, 3, 4)),
        )
    )
    assert poset.cardinality() == expected_indices.cardinality()
    assert all(
        any(member.index_set() == expected for member in poset)
        for expected in expected_indices
    )

    def member_on(indices):
        expected = finite_ordered_set(indices)
        return next(member for member in poset if member.index_set() == expected)

    centre = member_on((2,))
    outer_node = member_on((1,))
    outer_pair = member_on((1, 3))
    centre_and_outer = member_on((1, 2))
    three_outer = member_on((1, 3, 4))

    assert not poset.is_lequal(centre, three_outer)
    assert not poset.is_lequal(centre_and_outer, three_outer)
    assert poset.is_lequal(outer_node, three_outer)
    assert poset.is_lequal(outer_pair, three_outer)
    assert poset.is_lequal(outer_pair, member_on((1, 2, 3)))

    assert poset.bottom() is member_on(())
    assert poset.top() is member_on((1, 2, 3, 4))










def test_the_root_data_separates_parallel_mirrors_from_divergent_ones() -> None:
    r"""One Coxeter bond, two geometries, told apart by the roots.

    Both realizations below have Coxeter bond \(\infty\), so their Coxeter
    matrices are equal and the diagram of one cannot be told from the diagram
    of the other by its matrix.  The roots decide: the discriminant
    \(b(r,s)^2-q(r)q(s)\) vanishes when the mirrors meet at a boundary point
    and is positive when they have a common perpendicular instead.
    """
    parallel = CoxeterDiagrams().from_roots(
        Lattices(ZZ)([[-2, 2], [2, -2]]).module_generators()
    )
    divergent = CoxeterDiagrams().from_roots(
        Lattices(ZZ)([[-2, 3], [3, -2]]).module_generators()
    )
    meeting = CoxeterDiagrams().from_roots(
        Lattices(ZZ)([[-2, 1], [1, -2]]).module_generators()
    )

    assert parallel.coxeter_matrix() == divergent.coxeter_matrix()
    assert parallel.coxeter_entry(0, 1) == Infinity
    assert divergent.coxeter_entry(0, 1) == Infinity

    assert parallel.mirrors_are_parallel(0, 1)
    assert not parallel.mirrors_are_divergent(0, 1)

    assert divergent.mirrors_are_divergent(0, 1)
    assert not divergent.mirrors_are_parallel(0, 1)

    assert meeting.coxeter_entry(0, 1) == 3
    assert not meeting.mirrors_are_parallel(0, 1)
    assert not meeting.mirrors_are_divergent(0, 1)


