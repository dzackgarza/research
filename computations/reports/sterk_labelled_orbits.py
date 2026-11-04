"""Orbits of the maximal parabolic subdiagrams under the labelled symmetries (Type II only).

SUPERSEDED for the elliptic side: the elliptic enumeration here was a local checker that
maximalized within a rank cap, which made two "independent" readings identical by construction
and tested nothing, and its cap was wrong besides (a Type III ray in rank 10 needs elliptic rank
9, not 8).  Use computations/reports/sterk_owner_subdiagrams.py, which takes the subdiagrams from
CoxeterDiagrams().maximal_elliptic_subdiagrams(connected=False).  The parabolic/Type II part here
stands: its orbits were verified against the manuscript and are reproduced there.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_labelled_orbits.py

The action is the labelled one on the original vertices: the graph keeps every source root
(G.add_vertices(range(n)) before the edges, so an isolated root is a vertex and not just a member
of a partition class), vertices carry their norm through the partition, edges carry their labels,
and the backend is named explicitly -- algorithm="sage", Sage's own partition refinement -- because
this image's default (Bliss, chosen when algorithm is None) segfaults on the smallest input.  No
edge-gadget transform is used.
"""
import sys
from sage.all import Graph

load('/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage')


def labelled_graph(M):
    n = M.nrows()
    G = Graph(loops=False, multiedges=False)
    G.add_vertices(range(n))                       # every source root is a vertex
    for i in range(n):
        for j in range(i + 1, n):
            if M[i, j]:
                G.add_edge(i, j, edge_label(M, i, j))
    classes = {}
    for i in range(n):
        classes.setdefault(M[i, i], []).append(i)
    partition = list(classes.values())
    assert sorted(v for c in partition for v in c) == list(range(n)), "partition misses a root"
    assert all(v in G for v in range(n)), "a source root is missing from the graph"
    return G, partition


def orbits(group, sets):
    remaining = list(sets)
    reps = []
    while remaining:
        S = remaining[0]
        reps.append(S)
        orb = set(frozenset(g(v) for v in S) for g in group)
        remaining = [T for T in remaining if T not in orb]
    return reps


def _retired_elliptic_of_rank(M, rank):
    """Subsets of exactly `rank` vertices whose restriction is negative definite."""
    n = M.nrows()
    good = []
    for mask in range(1, 1 << n):
        S = tuple(i for i in range(n) if mask >> i & 1)
        if len(S) != rank:
            continue
        if (-M.matrix_from_rows_and_columns(S, S)).is_positive_definite():
            good.append(frozenset(S))
    return good


def _retired_maximal_elliptic(M, rank):
    """Inclusion-maximal subsets whose restriction is negative definite, of size <= rank."""
    n = M.nrows()
    good = []
    for mask in range(1, 1 << n):
        S = tuple(i for i in range(n) if mask >> i & 1)
        if len(S) > rank:
            continue
        if (-M.matrix_from_rows_and_columns(S, S)).is_positive_definite():
            good.append(frozenset(S))
    return [S for S in good if not any(S < T for T in good)]


MANUSCRIPT = {"3.3.7": (4, 4), "3.3.9": (2, 8), "3.3.10": (3, 15), "3.3.11": (4, 12),
              "3.3.12": (5, 17)}

for name, build in CUSPS:
    M = gram_of(build())
    G, partition = labelled_graph(M)
    aut = G.automorphism_group(partition=partition, edge_labels=True, algorithm="sage")
    maxp = [frozenset(i for c in comps for i in c) for S, comps in
            maximal_parabolic_subdiagrams(M, rank=8)]
    maxe = _retired_maximal_elliptic(M, rank=8)
    key = name.split()[0]
    print("%-30s roots %2d  norm classes %s  |Aut| %d" %
          (name, M.nrows(), [len(c) for c in partition], aut.order()))
    print("   parabolic subdiagrams %2d -> orbits %2d   (manuscript Type II  %d)"
          % (len(maxp), len(orbits(aut, maxp)), MANUSCRIPT[key][0]))
    e8 = _retired_elliptic_of_rank(M, 8)
    print("   elliptic of rank 8: %4d -> orbits %3d   | inclusion-maximal elliptic: %3d -> "
          "orbits %2d   (manuscript Type III %d)"
          % (len(e8), len(orbits(aut, e8)), len(maxe), len(orbits(aut, maxe)),
             MANUSCRIPT[key][1]))
    sys.stdout.flush()
