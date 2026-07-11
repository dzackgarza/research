r"""Family-level oracle for the specialization posets of Mbar(0, n)."""

from __future__ import annotations

import pytest

from itertools import combinations

from dm_moduli_spike.objects.splits import canonicalize_split
from sage.all import Graph, SymmetricGroup, factorial, graphs
from sage.rings.rational_field import QQ
from tests.support.poset_oracle import (
    augmented_face_poset,
    compatible_splits,
    expected_M0n_specialization_poset,
    specialization_poset,
    stable_splits,
)


@pytest.mark.parametrize("n", range(3, 7))
def test_full_M0n_poset_is_compatible_split_poset(n):
    actual = specialization_poset(0, n)
    expected = expected_M0n_specialization_poset(n)
    assert actual.is_isomorphic(expected)


@pytest.mark.slow
def test_full_M07_poset_is_compatible_split_poset():
    actual = specialization_poset(0, 7)
    expected = expected_M0n_specialization_poset(7)
    assert actual.is_isomorphic(expected)


@pytest.mark.parametrize("n", range(3, 7))
def test_dual_tree_to_split_system_is_the_poset_isomorphism(n):
    poset = specialization_poset(0, n)
    expected = expected_M0n_specialization_poset(n)

    phi = {
        stratum: stratum.curve_type().split_system(anchor_marking=1)
        for stratum in poset
    }

    assert set(phi.values()) == set(expected)
    assert len(set(phi.values())) == poset.cardinality()

    for left in poset:
        for right in poset:
            assert poset.is_lequal(left, right) == phi[left].issubset(phi[right])

    for stratum in poset:
        assert poset.rank(stratum) == len(phi[stratum])


def test_M04_is_three_armed_poset():
    actual = specialization_poset(0, 4)
    expected = expected_M0n_specialization_poset(4)
    sage_expected = expected

    assert actual.is_isomorphic(sage_expected)
    assert len(sage_expected.minimal_elements()) == 1
    assert len(sage_expected.maximal_elements()) == 3


def test_M05_is_augmented_face_poset_of_petersen_graph():
    actual = specialization_poset(0, 5)
    expected = augmented_face_poset(graphs.PetersenGraph().clique_complex())
    assert actual.is_isomorphic(expected)


def test_M05_split_compatibility_graph_is_petersen():
    ground, splits = stable_splits(5)

    graph = Graph()
    graph.add_vertices(splits)
    graph.add_edges(
        (left, right)
        for left, right in combinations(splits, 2)
        if compatible_splits(left, right, ground)
    )

    assert graph.is_isomorphic(graphs.PetersenGraph())


@pytest.mark.parametrize("n", [4, 5, 6])
def test_M0n_marking_relabeling_is_poset_equivariant(n):
    poset = specialization_poset(0, n)

    for sigma in SymmetricGroup(n).gens():
        relabel = {stratum: stratum.relabel_markings(sigma) for stratum in poset}

        assert set(relabel.values()) == set(poset)

        for left in poset:
            for right in poset:
                assert poset.is_lequal(left, right) == poset.is_lequal(relabel[left], relabel[right])

        for stratum in poset:
            source_splits = stratum.curve_type().split_system()
            target_splits = relabel[stratum].curve_type().split_system()
            expected_target = {
                canonicalize_split({sigma(label) for label in side}, n=n, anchor_marking=1)
                for side in source_splits
            }
            assert target_splits == expected_target


@pytest.mark.parametrize("n", [4, 5, 6])
def test_M0n_boundary_order_complex_homology(n):
    poset = specialization_poset(0, n)

    minimum, = poset.minimal_elements()
    boundary_poset = poset.subposet([element for element in poset if element != minimum])
    order_complex = boundary_poset.order_complex()

    homology = order_complex.homology(base_ring=QQ)
    nonzero_betti_numbers = {
        degree: group.dimension()
        for degree, group in homology.items()
        if group.dimension() != 0
    }

    assert nonzero_betti_numbers == {n - 4: factorial(n - 2)}
