r"""Subdiagram posets, automorphism orbits, and the root data behind a diagram.

The affine \(A_2\) diagram is the working specimen: a triangle with every bond
\(3\), whose automorphism group is the symmetric group on its three vertices.
Its subdiagram lattice is small enough to name in full, and the counts
distinguish the elliptic subdiagrams from the parabolic one.
"""

from sage.all import Infinity

from dzack_research.preamble.all import CoxeterDiagrams, Lattices, ZZ


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


def test_the_empty_subdiagram_is_elliptic_and_is_the_least_subdiagram() -> None:
    r"""The subdiagram on no vertices is elliptic and has no connected component.

    Its Schlaefli form is the form on the zero space: no negative and no zero
    index of inertia, so it is elliptic by the definition.  It is not
    connected, because connectedness is having exactly one component and it has
    none, so the connected enumeration drops it.
    """
    diagram = affine_a2()
    empty = diagram.induced_subdiagram(())

    assert empty.cardinality() == 0
    assert empty.is_elliptic()
    assert not empty.is_connected()
    assert empty.connected_components().cardinality() == 0
    assert diagram.elliptic_subdiagrams(connected=True).cardinality() == 6

    poset = diagram.subdiagram_poset()
    least = poset.minimal_elements()
    greatest = poset.maximal_elements()
    assert len(least) == 1
    assert len(greatest) == 1
    assert least[0].cardinality() == 0
    assert greatest[0].cardinality() == 3


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
    orbits = {frozenset(member.index_set()): member for member in poset}

    assert set(orbits) == {
        frozenset(),
        frozenset({1}),
        frozenset({2}),
        frozenset({1, 2}),
        frozenset({1, 3}),
        frozenset({1, 2, 3}),
        frozenset({1, 3, 4}),
        frozenset({1, 2, 3, 4}),
    }

    centre = orbits[frozenset({2})]
    outer_node = orbits[frozenset({1})]
    outer_pair = orbits[frozenset({1, 3})]
    centre_and_outer = orbits[frozenset({1, 2})]
    three_outer = orbits[frozenset({1, 3, 4})]

    assert not poset.is_lequal(centre, three_outer)
    assert not poset.is_lequal(centre_and_outer, three_outer)
    assert poset.is_lequal(outer_node, three_outer)
    assert poset.is_lequal(outer_pair, three_outer)
    assert poset.is_lequal(outer_pair, orbits[frozenset({1, 2, 3})])

    assert poset.bottom() is orbits[frozenset()]
    assert poset.top() is orbits[frozenset({1, 2, 3, 4})]


def test_the_triangle_is_its_own_only_parabolic_subdiagram_orbit() -> None:
    r"""The parabolic orbit poset of affine \(A_2\) is a single point.

    The triangle is parabolic and no proper subdiagram of it is: its proper
    subdiagrams are the empty one, the vertices and the edges, all elliptic.
    So there is one parabolic orbit, and the order on it is trivial.
    """
    poset = affine_a2().parabolic_subdiagram_orbit_poset()

    assert poset.cardinality() == 1
    assert poset.top() is poset.bottom()
    assert frozenset(poset.top().index_set()) == frozenset({0, 1, 2})


def test_a_disconnected_diagram_splits_into_its_components() -> None:
    r"""Two orthogonal mirrors give two components, each a single vertex."""
    diagram = CoxeterDiagrams().from_coxeter_matrix([[1, 2], [2, 1]])
    components = diagram.connected_components()

    assert not diagram.is_connected()
    assert components.cardinality() == 2
    for component in components:
        assert component.cardinality() == 1
        assert component.is_connected()


def test_the_root_morphism_carries_the_abstract_root_lattice_into_the_realization() -> None:
    r"""A rooted diagram realizes its abstract root lattice through a morphism.

    The domain is the lattice presented by the root Gram, the codomain is the
    lattice the roots live in, and the arrow sends the \(v\)-th module
    generator to the \(v\)-th root.  What makes it a lattice morphism is that
    the Gram of the domain is the Gram of the roots, so it preserves the form;
    that is the claim asserted here, generator pair by generator pair.
    """
    realization = Lattices(ZZ)([[-2, 1], [1, -2]])
    diagram = CoxeterDiagrams().from_roots(realization.module_generators())
    morphism = diagram.root_morphism()
    abstract = diagram.root_lattice()

    assert morphism.domain() is abstract
    assert morphism.codomain() is realization
    assert abstract.rank() == 2
    generators = tuple(abstract.module_generators())
    roots = tuple(diagram.roots())
    for left_index, left in enumerate(generators):
        assert morphism(left) == roots[left_index]
        for right_index, right in enumerate(generators):
            assert morphism(left).b(morphism(right)) == left.b(right)


def test_the_root_intersection_graph_records_squares_as_loops_and_pairings_as_edges() -> None:
    r"""The exact integral datum the Coxeter matrix summarizes.

    On the \(A_2\) realization the two roots have square \(-2\) and pair to
    \(1\), so the graph has one loop of label \(-2\) at each vertex and one
    edge of label \(1\).  The Coxeter bond \(3\) is recovered from those
    numbers as \(4\cdot 1^2/((-2)(-2)) = 1 = 4\cos^2(\pi/3)\).
    """
    realization = Lattices(ZZ)([[-2, 1], [1, -2]])
    diagram = CoxeterDiagrams().from_roots(realization.module_generators())
    graph = diagram.root_intersection_graph()
    vertices = tuple(diagram.index_set())

    assert graph.num_verts() == 2
    assert graph.edge_label(vertices[0], vertices[0]) == -2
    assert graph.edge_label(vertices[1], vertices[1]) == -2
    assert graph.edge_label(vertices[0], vertices[1]) == 1
    assert diagram.coxeter_entry(vertices[0], vertices[1]) == 3


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
