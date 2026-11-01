"""Orbits of the maximal parabolic subdiagrams under the labelled diagrams' symmetries.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_labelled_orbits.py

The action is the labelled one: `automorphism_group(edge_labels=True, partition=...)`, so norms
(the partition) and edge labels are preserved and the group is not the unlabelled graph
automorphism group.  The backend is named explicitly -- `algorithm="sage"` -- because this image's
default Bliss backend segfaults on the smallest possible input (see GAPS); the call is the
maintained API's, not an encoding of my own.
"""
import sys
from sage.all import Graph

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
    return G, list(classes.values())


def orbit_representatives(group, sets):
    remaining = list(sets)
    reps = []
    while remaining:
        S = remaining[0]
        reps.append(S)
        orbit = set(frozenset(g(v) for v in S) for g in group)
        remaining = [T for T in remaining if T not in orbit]
    return reps


MANUSCRIPT = {"3.3.7": (4, 4), "3.3.9": (2, 8), "3.3.10": (3, 15), "3.3.11": (4, 12),
              "3.3.12": (5, 17)}

for name, build in CUSPS:
    M = gram_of(build())
    G, partition = labelled_graph(M)
    aut = G.automorphism_group(edge_labels=True, partition=partition, algorithm="sage")
    maxl = maximal_parabolic_subdiagrams(M, rank=8)
    sets = [frozenset(i for c in comps for i in c) for S, comps in maxl]
    reps = orbit_representatives(aut, sets)
    key = name.split()[0]
    print("%-30s |Aut| = %-3d  parabolic subdiagrams %2d -> orbits %2d   (manuscript Type III: %d)"
          % (name, aut.order(), len(maxl), len(reps), MANUSCRIPT[key][1]))
    for r in reps:
        print("      representative: %s" % [i + 1 for i in sorted(r)])
    sys.stdout.flush()
