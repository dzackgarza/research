"""#760 (stage 3): the face of the restricted Enriques semifan cut by an admissible Coble root.

The question
------------
research#760 asks, at a marked 0-cusp [I] of F_En,2 with boundary lattice K_I = eta_I^perp / Z eta_I
and restricted Enriques semifan F_I: for two admissible roots r_1, r_2 of K_I that are inequivalent
under Gamma_Co,2, do the hyperplanes r_1^perp and r_2^perp cut different faces of F_I?

The object
----------
For a root r of K_I, the face of F_I cut by r^perp is the unique cone of F_I whose relative interior
contains the relative interior of r^perp intersect C, the chamber C = the fundamental chamber of the
reflection group W(K_I).  It is well defined: relint(r^perp intersect C) is a connected relatively
open subset of r^perp, so it lies in the relative interior of one cone and, being relatively open and
connected, of only that one.  Its two values are read off Definition 5.4 (def:generalized-coxeter-
semifan) with no further computation:

  * r relevant: r^perp intersect cl(C) is a face of the chamber and a cone of F_I, so the face is
    that wall, of dimension one less than the chamber;
  * r irrelevant: s_r lies in W^irr, so the chamber s_r(C) is glued to C across the wall r^perp, and
    relint(r^perp intersect C) lies in the interior of the maximal cone M = union over h in W^irr of
    h(C).  No other cone of F_I meets it, so the face is M itself -- the same cone for every
    irrelevant root of the diagram, since M depends on the chamber and on Phi^irrel only.

So the map from roots to faces is injective on the relevant roots and constant on the irrelevant
ones.  This record decides, exactly, which of the admissible T_Co-roots fall in which class, and
hence whether F_I separates two inequivalent marked roots.

The data
--------
T_En = U + U(2) + E8(2) with basis (e, f, e', f', a_1..a_8): e.f = 1, e'.f' = 2, and the a_i have Gram
matrix -2 cartan(E8).  The Coble root is delta = e - f (lem:coble-heegner-vector), delta^2 = -2, and
T_Co = delta^perp.  The five representatives eta_1..eta_5 and the printed root sets R_1..R_5 are
Sterk's, transcribed verbatim from computations/reports/coble_sterk-reflection-subgroups.py, whose
provenance is coble_sterk-root-lifts-run.txt; the same transcription is used by the accepted records
coble_cusp-admissibility.py and coble_coble-root-orbits.py.

The relevant/irrelevant split is Definition 5.4 read through AEGS25 Figure 5: a folded root is
irrelevant exactly when every constituent of the folding is an interior node of the K3 diagram --
interior meaning off the boundary of the square, respectively the triangle.  The fold table FOLD and
the interior sets INTERIOR below are the transcription of computations/reports/
sterk_figure5_adjacency.py, whose record asserts every fold sum against the library's own root
vectors; this record re-asserts the same sums, so a mis-transcription fails here rather than passing.

The three tests, each exact
---------------------------
(1) The printed order against the library's vertex order.  Sterk numbers the vertices of his printed
    diagrams, and the library names them r_0, ..., r_{n-1} in its own construction order; the two
    agree only if they agree.  The record compares the labelled Gram matrix of the transcribed
    printed roots with that of Sterk.cusp_roots_in_TEn, and where they differ it enumerates every
    permutation of the library order that carries one Gram matrix to the other, pruning by the row
    signature (the square of a root and the multiset of its pairings).  A printed label is declared
    irrelevant only when every such permutation gives the same verdict for it.

(2) The classes in K_I.  Two roots of eta^perp have the same class in K_I exactly when their
    difference is a rational multiple of eta: the difference lies in eta^perp, and Z eta is the whole
    of Q eta intersect eta^perp because eta is primitive and isotropic.  So the test is the exact
    rank over QQ of the pair (eta, r_a - r_b).  Distinct classes give distinct Gamma_Co,2-orbits,
    because every element of Gamma_Co,2 that carries one marked pair at [I] to another preserves
    [I] and therefore acts on K_I.

(3) The face.  By the two-valued description above it is decided by the verdict of (1); the record
    prints it as a named cone of F_I for each admissible root.

Run
---
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
      -b <repo>:/repo -w /repo /bin/sh -c \\
      'PATH=/sage/.venv/bin:$PATH PYTHONPATH=/repo/.scratch/sage-extensions/src \\
       python /repo/computations/reports/coble_irrelevant-marking-face.py'

Transcript: coble_irrelevant-marking-face-run.txt.  Sage 11.0.beta5 in the shared runtime, with the
library sage-extensions at .scratch/sage-extensions, commit LIBRARY_COMMIT below; no GAP, no pari
interface and no provider call is made, only integer and rational linear algebra over ZZ and QQ.
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
from sage.version import version as SAGE_VERSION

LIBRARY_COMMIT = "1488acf"
t0 = time.time()

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))])
        for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f

# ---- Sterk's data, verbatim from computations/reports/coble_sterk-reflection-subgroups.py
a9, a10 = f - e, 2 * fp + abar[7]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))])
         for i in range(8)]
STERK_ETA = {3: ep + fp + abar[7], 4: 2 * ep + fp + abar[0], 5: 2 * e + 2 * f + abar[0]}
ROOTS = {}
ROOTS[3] = (alpha[0:7] + [a9, a10, (e + f) - a9 - a10, 2 * e + (abar[0] - abar[7]),
                          (e + f) + (alpha[7] - fp)])
ROOTS[4] = (alpha[1:8] + [f - e, abar[7] + 2 * ep, e + f + alpha[0] - ep,
                          2 * e - 2 * ep + abar[7] - abar[0]])
ROOTS[5] = ([at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
             2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
             et + ft + (abart[5] - abart[2]), et + ft + (abart[0] + abart[7] - abart[2]),
             et + ft + at[2]])

# ---- AEGS25 Figure 5 and the fold, transcribed in computations/reports/sterk_figure5_adjacency.py
INTERIOR = {"square": set(range(16, 22)), "triangle": {1, 19}}
FOLD = {
    3: [["v13"], ["v14", "v12"], ["v15", "v11"], ["v16", "v10"], ["v1", "v9"], ["v2", "v8"],
        ["v3", "v7"], ["v4", "v6"], ["v5"], ["v17", "v19"], ["v22", "v20", "v20"],
        ["v22", "v18", "v18"]],
    4: [["v15"], ["v16", "v14"], ["v1", "v13"], ["v2", "v12"], ["v3", "v11"], ["v4", "v10"],
        ["v5", "v9"], ["v6", "v8"], ["v7"], ["v17", "v20"], ["v18", "v19"]],
    5: [["v16", "v1", "v1", "v2"], ["v2", "v3", "v3", "v4"], ["v4", "v5", "v5", "v6"],
        ["v6", "v7", "v7", "v8"], ["v8", "v9", "v9", "v10"], ["v10", "v11", "v11", "v12"],
        ["v12", "v13", "v13", "v14"], ["v14", "v15", "v15", "v16"],
        ["v17"], ["v18"], ["v19"], ["v20"], ["v21"], ["v22"]],
}
SIDE = {3: "square", 4: "square", 5: "square"}

from sage_extensions.all import Sterk  # noqa: E402

basis_of = dict(Sterk.roots_18_2_0(), **Sterk.roots_18_0_0())


def printed_label(name):
    """The printed Figure 5 number of a K3 root, from the transports of sterk_figure5_adjacency."""
    if name.startswith("v"):
        return int(name[1:]) - 1
    return 1 if name == "w18" else (19 if name == "w19" else int(name[1:]) - 1)


print("the face of the restricted Enriques semifan cut by an admissible Coble root")
print("Sage %s; exact ZZ/QQ linear algebra; library sage-extensions at commit %s"
      % (SAGE_VERSION, LIBRARY_COMMIT))
print("T_En Gram determinant %d; delta = e - f, delta^2 = %d; T_Co = delta^perp"
      % (G.det(), ip(delta, delta)))
print()

library_roots = {j: [vector(ZZ, x) for x in Sterk.cusp_roots_in_TEn("Sterk_%d" % j)] for j in (3, 4, 5)}

print("=== (1) the printed order against the library's vertex order r_0, ..., r_{n-1}")
printed_irrelevant = {}
for j in (3, 4, 5):
    hand = ROOTS[j]
    lib = library_roots[j]
    n = len(hand)
    hg = matrix(ZZ, n, n, lambda a, b: ip(hand[a], hand[b]))
    lg = matrix(ZZ, n, n, lambda a, b: ip(lib[a], lib[b]))
    # the irrelevant vertices, in the library's own order, from Definition 5.4 through the fold
    configuration = Sterk.sterk_roots()["Sterk_%d" % j]
    assert len(configuration) == n == len(FOLD[j]), (j, len(configuration), n, len(FOLD[j]))
    lib_irrelevant = set()
    folds = []
    for index, (root, fold) in enumerate(zip(configuration, FOLD[j])):
        rebuilt = None
        for name in fold:
            term = basis_of[name]
            rebuilt = term if rebuilt is None else rebuilt + term
        assert rebuilt == root, ("cusp %d: r_%d is not the transcribed sum of %s" % (j, index, fold))
        nodes = [printed_label(name) for name in fold]
        folds.append(nodes)
        if all(node in INTERIOR[SIDE[j]] for node in nodes):
            lib_irrelevant.add(index)
    print("cusp %d: %2d printed roots; Gram of the printed order = Gram of the library order: %s"
          % (j, n, hg == lg))
    if hg == lg:
        matches = [list(range(n))]
    else:
        def signature(M, i):
            return (int(M[i, i]), tuple(sorted(int(M[i, k]) for k in range(n) if k != i)))
        hand_sig = [signature(hg, i) for i in range(n)]
        lib_sig = [signature(lg, i) for i in range(n)]
        cand = {i: [k for k in range(n) if lib_sig[k] == hand_sig[i]] for i in range(n)}
        matches = []

        def walk(assign, used):
            i = len(assign)
            if i == n:
                matches.append(list(assign))
                return
            for k in cand[i]:
                if k in used:
                    continue
                if all(int(hg[i, b]) == int(lg[k, assign[b]]) for b in range(i)):
                    assign.append(k)
                    used.add(k)
                    walk(assign, used)
                    used.discard(k)
                    assign.pop()
        walk([], set())
        print("        the orders differ; permutations of the library order carrying one labelled Gram "
              "to the other: %d" % len(matches))
    verdicts = set()
    for match in matches:
        verdicts.add(tuple(sorted(i + 1 for i in range(n) if match[i] in lib_irrelevant)))
    assert len(verdicts) == 1, (j, verdicts)
    printed_irrelevant[j] = sorted(verdicts.pop())
    print("        irrelevant vertices in the library order: r%s"
          % ",".join(str(i) for i in sorted(lib_irrelevant)))
    print("        the printed labels of those vertices, under every matching: %s"
          % printed_irrelevant[j])
    match = matches[0]
    for label in printed_irrelevant[j]:
        index = match[label - 1]
        print("        label %2d = r%d = the sum of the printed Figure 5 nodes %s"
              % (label, index, folds[index]))
print()

print("=== (2) the admissible T_Co-roots, their classes in K_I, and their faces")
for j in (3, 4, 5):
    eta = STERK_ETA[j]
    assert ip(eta, eta) == 0
    R = ROOTS[j]
    inside = [i + 1 for i, r in enumerate(R) if ip(r, delta) == 0]
    admissible = [label for label in inside if ip(R[label - 1], R[label - 1]) == -2]
    print("cusp %d: eta_j . delta = %d; walls in T_Co at printed labels %s; admissible roots %s"
          % (j, ip(eta, delta), inside, admissible))
    for label in admissible:
        r = R[label - 1]
        print("        label %2d: r^2 = %d, (r, delta) = %d, (r, eta_j) = %d; in the irrelevant set: %s"
              % (label, ip(r, r), ip(r, delta), ip(eta, r), label in printed_irrelevant[j]))
    classes = {}
    for a, label in enumerate(admissible):
        for other in admissible[a + 1:]:
            diff = vector(ZZ, R[label - 1] - R[other - 1])
            same = matrix(QQ, [vector(QQ, eta), vector(QQ, diff)]).rank() < 2
            classes.setdefault(label, set()).add((other, same))
            print("        labels %2d and %2d: same class in K_I: %s   (rank of (eta, difference) = %d)"
                  % (label, other, same, matrix(QQ, [vector(QQ, eta), vector(QQ, diff)]).rank()))
    assert all(not same for pairs in classes.values() for _, same in pairs), j
    if len(admissible) < 2:
        print("        one admissible root: no pair exists, so the map is injective here and carries "
              "no information about the marking")
    else:
        print("        %d admissible roots, pairwise distinct classes in K_I, so pairwise "
              "inequivalent under Gamma_Co,2" % len(admissible))
    faces = "{" + ", ".join("label %d: %s" % (label, "the maximal cone M" if label in printed_irrelevant[j]
                                                else "the wall r^perp") for label in admissible) + "}"
    print("        the face of F_%d cut by r^perp: %s" % (j, faces))
    print()

print("=== (3) the verdict of #760 at each marked cusp")
for j in (3, 4, 5):
    eta = STERK_ETA[j]
    R = ROOTS[j]
    admissible = [i + 1 for i, r in enumerate(R) if ip(r, delta) == 0 and ip(r, r) == -2]
    irrelevant = [label for label in admissible if label in printed_irrelevant[j]]
    print("cusp %d: %d admissible T_Co-roots, %d of them irrelevant (%s)"
          % (j, len(admissible), len(irrelevant), irrelevant))
print()
print("at cusp 5 the three admissible T_Co-roots are pairwise inequivalent under Gamma_Co,2 and each")
print("cuts the maximal cone M = union over h in W^irr of h(C) of F_5, one and the same cone: the map")
print("from Gamma_Co,2-orbits of admissible roots to faces of F_5 is not injective, and the statement")
print("of #760 fails there.")
print("elapsed %d s" % round(time.time() - t0))
print("PYEXIT=0")
