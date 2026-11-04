"""Maximal elliptic subdiagrams from the maintained owner API, then orbits under the labelled action.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_owner_subdiagrams.py

The subdiagrams are the owner's: CoxeterDiagrams().from_roots(family) then
maximal_elliptic_subdiagrams(connected=False), so no subset ellipticity test is written here.
The action is the verified one on the full Gram labelling -- Sage graph automorphisms with
edge_labels=True and the norm partition, algorithm="sage" -- applied to the owner-returned vertex
sets, not the coarser Coxeter-order group of the owner's own orbit methods.
"""
import sys
from sage.all import Graph, ZZ

from sage_extensions.all import CoxeterDiagrams, Lattices

load('/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage')


def labelled_graph(M):
    n = M.nrows()
    G = Graph(loops=False, multiedges=False)
    G.add_vertices(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if M[i, j]:
                G.add_edge(i, j, edge_label(M, i, j))
    classes = {}
    for i in range(n):
        classes.setdefault(M[i, i], []).append(i)
    partition = list(classes.values())
    assert sorted(v for c in partition for v in c) == list(range(n))
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


for name, build in CUSPS:
    M = gram_of(build())
    n = M.nrows()
    try:
        L = Lattices(ZZ)([list(r) for r in M.rows()])
        is_nondegenerate = True
    except Exception as error:
        print("%-30s lattice from Gram refused: %s" % (name, str(error)[:90]))
        continue
    roots = {("a%d" % (i + 1)): L.basis_vector(i) for i in range(n)}
    D = CoxeterDiagrams().from_roots(roots)
    subs = list(D.maximal_elliptic_subdiagrams(connected=False))
    sets = [frozenset(int(d.index_set().__getitem__(k).lstrip("a")) - 1
                      for k in range(len(d.index_set()))) for d in subs]
    G, partition = labelled_graph(M)
    aut = G.automorphism_group(partition=partition, edge_labels=True, algorithm="sage")
    print("%-30s maximal elliptic (owner): %3d   orbits under labelled Aut: %2d"
          % (name, len(sets), len(orbits(aut, sets))))
    for S in orbits(aut, sets)[:12]:
        print("      representative: %s" % [i + 1 for i in sorted(S)])
    sys.stdout.flush()
