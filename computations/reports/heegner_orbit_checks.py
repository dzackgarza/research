"""The post-stabilizer consumer path, shared by the real run and by the small driver.

Every acceptance predicate of the Heegner decomposition lives here exactly once, so that the small
example exercises the same code the full computation runs -- not a sketch of it.  The earlier small probe
checked that the restricted action *constructs* and then missed the failure one step later, in the Orbit
accessor; that is what this module exists to prevent.
"""


def restrict(G, subgroup, points):
    """The subgroup's action on ``points``, restricted from the ambient action through H -> G.

    Returns one frozen set of points per orbit.  ``orbits()`` yields Orbit objects, which are not
    iterable; ``points()`` is the accessor.
    """
    from sage_extensions.categories.group.g_sets import FiniteGSets

    elements = G.element_action()
    inclusion = subgroup.inclusion()
    restricted_action = elements.restrict_action(inclusion)
    h_set = FiniteGSets(subgroup)(points, lambda h, x: restricted_action.act(h, x))
    return [frozenset(orbit.points()) for orbit in h_set.orbits()]


def check_partition(partition, isotropic_set, zero_element, expected_sizes):
    """Disjointness, coverage, q = 0 throughout, the singleton being the zero class, and the sizes."""
    for orbit in partition:
        assert set(orbit) <= isotropic_set, 'an orbit leaves the isotropic classes'
    covered = set().union(*[set(orbit) for orbit in partition]) if partition else set()
    assert covered == isotropic_set, 'the orbits do not cover the isotropic classes'
    total = sum(len(orbit) for orbit in partition)
    assert total == len(isotropic_set), 'the orbits are not disjoint'
    assert sum(len(orbit) for orbit in partition) == total
    singletons = [orbit for orbit in partition if len(orbit) == 1]
    assert len(singletons) == 1, 'there is not exactly one singleton orbit'
    assert set(singletons[0]) == {zero_element}, 'the singleton orbit is not the zero class'
    sizes = sorted(len(orbit) for orbit in partition)
    assert sizes == sorted(expected_sizes), (sizes, expected_sizes)
    return sizes


def check_generators(generators, polarization, points, q):
    """Every generator fixes the chosen class and preserves q on the tested domain."""
    assert generators, 'no generators'
    for generator in generators:
        assert generator(polarization) == polarization, 'a generator moves the chosen class'
    for generator in generators:
        for point in points:
            assert q(generator(point)) == q(point), 'a generator does not preserve q'
    return len(generators)


def check_values(q, points, value_module_zero):
    """Every point tested has q = 0 (the isotropic domain is the q = 0 fiber)."""
    bad = [point for point in points if q(point) != value_module_zero]
    assert not bad, 'a tested point is not isotropic'
    return len(points)
