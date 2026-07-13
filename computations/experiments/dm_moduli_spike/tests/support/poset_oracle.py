"""Oracle posets and combinatorial fixtures for specialization-order tests."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from itertools import combinations
from typing import TYPE_CHECKING, Protocol, cast

from sage.all import Graph, Poset

if TYPE_CHECKING:
    from sage.combinat.posets.posets import FinitePoset


class _FaceComplex(Protocol):
    def face_iterator(self) -> Iterator[object]: ...


def stable_splits(n: int) -> tuple[frozenset[int], tuple[frozenset[int], ...]]:
    """Canonical representatives of stable splits of {1, ..., n}."""
    if n < 3:
        raise ValueError("Mbar_{0,n} is stable only for n >= 3")

    ground = frozenset(range(1, n + 1))
    splits = tuple(frozenset((1, *tail)) for size in range(2, n - 1) for tail in combinations(range(2, n + 1), size - 1))
    return ground, splits


def compatible_splits(left: frozenset[int], right: frozenset[int], ground: frozenset[int]) -> bool:
    """Whether two stable splits are pairwise compatible."""
    left_complement = ground - left
    right_complement = ground - right
    return any(
        len(intersection) == 0
        for intersection in (
            left & right,
            left & right_complement,
            left_complement & right,
            left_complement & right_complement,
        )
    )


def augmented_face_poset(simplicial_complex: _FaceComplex) -> Poset:
    """Face poset including the empty face."""
    faces = tuple(frozenset(cast(Iterable[int], simplex)) for simplex in simplicial_complex.face_iterator())
    return Poset((faces, lambda left, right: left.issubset(right)), facade=True)


def expected_M0n_specialization_poset(n: int) -> Poset:
    """Expected specialization poset for Mbar(0, n) via compatible split systems."""
    ground, splits = stable_splits(n)

    compatibility_graph = Graph()
    compatibility_graph.add_vertices(splits)
    compatibility_graph.add_edges((left, right) for left, right in combinations(splits, 2) if compatible_splits(left, right, ground))

    return augmented_face_poset(compatibility_graph.clique_complex())


def specialization_poset(g: int, n: int) -> FinitePoset:
    """Convenience wrapper used throughout the regression suite."""
    from dm_moduli_spike.objects.model import DMCompactificationModel

    return DMCompactificationModel(g, n).stratification(backend="pure-sage").specialization_poset()
