"""Type III rays of the five Enriques semifans, counted on the maintained owner API.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/sterk_type_iii_subdiagrams.py

Why rank 9.  For each of Sterk's five isotropic representatives the roots of
v^perp/Zv are computed in sterk_cusp_diagrams.sage; their Gram has rank 10 with
Schlaefli signature (9,1), i.e. the ambient is hyperbolic of rank 10.  A Type III
cone of dimension k has elliptic rank 10 - k (AET Thm 4.3), so a Type III *ray*
needs an elliptic subdiagram of rank 9.  Rank 9 is also the largest possible
elliptic rank there, so every rank-9 elliptic subdiagram is maximal in the
lattice and no maximality test has to be written here.

The subdiagram and its ellipticity are the owner's (CoxeterDiagrams().from_roots,
induced_subdiagram, is_elliptic).  The action is the verified one on the full Gram
labelling -- Sage graph automorphisms with edge_labels=True and the norm
partition, algorithm="sage" -- applied to the returned vertex sets.

Superseded, and kept for provenance.  This run enumerates the 9-vertex subsets and asks
the owner's predicate of each of them; it was written before the owner's enumeration decided
inertia and maximality on vertex sets.  The acceptance run is
computations/reports/sterk_type_iii_rays.py, which takes maximal_elliptic_subdiagrams(connected=False)
from the owner and selects rank 9 among the results, on the maintained rooted diagrams.  The two
agree on all five counts (4, 8, 15, 12, 17); this file is where they were first computed.
"""
import os
import sys
from itertools import combinations

from sage.all import Graph, ZZ

from sage_extensions.all import CoxeterDiagrams, Lattices

SOURCE = '/repo/computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage'


def load_definitions(path):
    """Execute the reconstruction with its module-level reports disabled.

    Its four report functions take minutes (exact eigenvalues of every vertex
    subset) and their output is kept in computations/reports/sterk-cusp-diagrams-run.txt;
    only the grammar of the cusp diagrams is wanted here, and it is unchanged.
    """
    text = open(path).read()
    for call in ('report', 'primitivity_report', 'qrank_report', 'rank_condition_report'):
        target = '\n%s()\n' % call
        assert text.count(target) == 1, (call, text.count(target))
        text = text.replace(target, '\npass  # %s() disabled: its output is in the -run.txt\n' % call)
    namespace = {'__name__': 'sterk_cusp_diagrams'}
    exec('from sage.all import *', namespace)   # what sage's loader seeds for a .sage file
    exec(compile(text, path, 'exec'), namespace)
    return namespace


DEFINITIONS = load_definitions(SOURCE)
CUSPS = DEFINITIONS['CUSPS']
gram_of = DEFINITIONS['gram_of']
edge_label = DEFINITIONS['edge_label']

MANUSCRIPT = [4, 8, 15, 12, 17]   # 900-five-cusps.md, Type III in the Coxeter compactification


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


k = 0
for name, build in CUSPS:
    k += 1
    M = gram_of(build())
    n = M.nrows()
    ambient = M.rank()
    top = ambient - 1
    L = Lattices(ZZ)([list(r) for r in M.rows()])
    roots = {i: L.basis_vector(i) for i in range(n)}
    D = CoxeterDiagrams().from_roots(roots)
    found = []
    for S in combinations(range(n), top):
        if D.induced_subdiagram(S).is_elliptic():
            found.append(frozenset(S))
    G, partition = labelled_graph(M)
    aut = G.automorphism_group(partition=partition, edge_labels=True, algorithm="sage")
    reps = orbits(aut, found)
    # two rank-9 elliptic subdiagrams with equal image span in v^perp/Zv would give
    # one ray, not two: rank of the union's Gram is then 9, not more.
    coincident = []
    for a in range(len(reps)):
        for b in range(a + 1, len(reps)):
            S = sorted(reps[a] | reps[b])
            if M[S, S].rank() == top:
                coincident.append((reps[a], reps[b]))
    print("%-30s n=%2d  rank(v^perp/Zv)=%2d  elliptic rank %d: %3d subdiagrams  "
          "|Aut|=%2d  orbits %2d   manuscript %2d%s"
          % (name, n, ambient, top, len(found), aut.order(), len(reps), MANUSCRIPT[k - 1],
             "" if len(reps) == MANUSCRIPT[k - 1] else "   *** MISMATCH"))
    for rep in reps:
        print("      %s" % [i + 1 for i in sorted(rep)])
    if coincident:
        print("      coincident spans among representatives: %d pairs" % len(coincident))
    sys.stdout.flush()
