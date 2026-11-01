"""Orbits of the maximal parabolic subdiagrams under the labelled diagram's symmetries.

Edge labels are encoded as intermediate vertices, so the automorphism group is the plain one
on a partitioned graph -- no edge_labels path -- and the partition keeps norms distinguishable.
"""
from sage.all import Graph
load('/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage')

def encoded(M):
    n = M.nrows()
    H = Graph(loops=False)
    norm_classes = {}
    for i in range(n):
        norm_classes.setdefault(("v", M[i, i]), []).append(i)
    label_classes = {}
    for i in range(n):
        for j in range(i + 1, n):
            if M[i, j]:
                lab = ("e", edge_label(M, i, j))
                e = ("edge", i, j)
                H.add_edge(i, e); H.add_edge(e, j)
                label_classes.setdefault(lab, []).append(e)
    partition = list(norm_classes.values()) + list(label_classes.values())
    return H, partition

def orbits(group, sets):
    remaining = list(sets); reps = []
    while remaining:
        S = remaining[0]; reps.append(S)
        orb = set(frozenset(g(v) for v in S) for g in group)
        remaining = [T for T in remaining if T not in orb]
    return reps

for name, build in CUSPS:
    M = gram_of(build())
    H, partition = encoded(M)
    aut = H.automorphism_group(partition=partition)
    maxl = maximal_parabolic_subdiagrams(M, rank=8)
    sets = [frozenset(i for c in comps for i in c) for S, comps in maxl]
    orb = orbits(aut, sets)
    print("%-32s |Aut| = %-4d  parabolic subdiagrams %2d  orbits %2d  representatives %s"
          % (name, aut.order(), len(maxl), len(orb), [sorted(r) for r in orb]))
