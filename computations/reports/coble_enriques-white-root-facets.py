"""White roots of AEGS Figures 7--8: wall Gram matrices, induced facet angles,
and the discriminant form of the perpendicular in T_En.

Header: the objects and the owner calls, fixed before the run
-----------------------------------------------------------
The lattice is T_En = U + U(2) + E8(2), with basis (e,f,e',f',a_1,...,a_8),
so e.f = 1, e'.f' = 2, and the a_i have Gram matrix -2 times the E_8 Cartan
matrix.  The five vectors eta_j and the printed roots are transcribed verbatim
from the accepted #654 records coble_sterk-root-lifts.py and
coble_sterk-reflection-subgroups.py; their sources are Sterk (1991), 4.2.3 and
4.3.5--4.3.9.  AEGS (Nagoya Math. J. 259 (2025)), section 3.4, printed p. 591,
sets g_ij = (a_i.a_j)/sqrt(a_i^2 a_j^2) and uses a single, double, thick,
dotted bond for g_ij = 1/2, sqrt(2)/2, 1, >1 respectively (their m-tuple
convention has g = cos(pi/(m+2))).  The same paragraph assigns square -2 to
white nodes and square -4 to black nodes.  Figures 7 and 8, printed pp. 594--595,
are the coloured graphs FIGURES below, read from those pages and from the
vector-PDF figures in the authors' arXiv tarball (2312.03638).

For a white node delta, every other wall j meets delta^perp: here g_delta,j is
0 or sqrt(2)/2.  The full induced angle table uses, without discarding walls
orthogonal to delta,

  cos(phi_ij) = (g_ij + g_delta,i g_delta,j) /
                 sqrt((1-g_delta,i^2)(1-g_delta,j^2)).

This is the mirror-facet formula in the manuscript.  Tables include every pair
i<j, not only neighbours of delta.  Values 0, 1/2, sqrt(2)/2 are pi/2, pi/3,
pi/4; value 1 means parallel walls; values >1 mean no intersection.

For the discriminant computation, exact integer linear algebra is the owner:
  H_delta = B G B^T, where the rows of B are a ZZ-basis of delta^perp in T_En;
  IntegralLattice(H_delta).discriminant_group().normal_form()
is compared entrywise (invariants, quadratic matrix, bilinear matrix) with the
same owner call on H_Co = <2> + U(2) + E8(2).  The TorsionQuadraticModule
documentation states that these data determine the finite quadratic module.
No provider call, group algorithm, Vinberg search, or numerical approximation
is made.

Lift independence is checked constructively.  For each white delta the script
checks gcd(delta.e^perp) = 1 and produces a in e^perp with (a,delta) = 1.  The
Eichler isometry E_{e,a}(x) = x+(x,e)a-(x,a)e-(a^2/2)(x,e)e then sends delta to
delta-e and fixes e.  Its k-th power sends delta to delta-ke for every k in ZZ,
acts trivially on e^perp/e, and hence identifies all the perpendiculars.
Explicit isometry checks are printed for k=-2,...,2.

Run in the maintained Sage runtime:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs \
    -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo /bin/sh -c \
    'PATH=/sage/.venv/bin:$PATH python \
     /repo/computations/reports/coble_enriques-white-root-facets.py'
Transcript: coble_enriques-white-root-facets-run.txt.
"""
from collections import Counter
from itertools import combinations
from math import gcd
import sys

sys.stdout.reconfigure(line_buffering=True)
import networkx as nx
from sage.all import (ZZ, QQ, QuadraticField, matrix, vector, block_diagonal_matrix,
                      CartanMatrix, xgcd)
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.version import version as SAGE_VERSION

K2 = QuadraticField(2, "s")
s = K2.gen()
HALF = K2(QQ(1) / 2)
SQRT2_HALF = s / 2

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = (BAS[i] for i in range(4))
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))) for i in range(8)]
ETA = {1: e, 2: ep, 3: ep + fp + abar[7], 4: 2 * ep + fp + abar[0],
       5: 2 * e + 2 * f + abar[0]}
a9, a10 = f - e, 2 * fp + abar[7]
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: at[i].dot_product(G * at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))])
         for i in range(8)]
ROOTS = {1: list(alpha) + [fp - ep, abar[7] + 2 * ep,
                           2 * ep + 2 * fp + abar[0] + abar[7], 5 * ep + 3 * fp + 2 * abar[1]],
         2: list(alpha) + [abar[7] + 2 * f, e - f],
         3: alpha[0:7] + [a9, a10, (e + f) - a9 - a10, 2 * e + (abar[0] - abar[7]),
                           (e + f) + (alpha[7] - fp)],
         4: alpha[1:8] + [f - e, abar[7] + 2 * ep, e + f + alpha[0] - ep,
                           2 * e - 2 * ep + abar[7] - abar[0]],
         5: [at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
             2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
             et + ft + (abart[5] - abart[2]),
             et + ft + (abart[0] + abart[7] - abart[2]), et + ft + at[2]]}

# Figure inputs: (square, bonds), with bonds i, j, type; type 3=single, 4=double,
# inf=thick.  Unlisted pairs are orthogonal.  Nodes are numbered in the order
# described in the run output; root-representative matching is computed, not assumed.
FIGURES = {
    1: ({i: -4 for i in range(1, 13)},
        [(1,2,3),(2,3,3),(3,4,3),(4,5,3),(5,6,3),(6,7,3),(7,8,3),(8,1,3),
         (7,9,3),(9,10,"inf"),(10,11,"inf"),(11,12,"inf"),(12,3,3)]),
    2: ({**{i: -4 for i in range(1, 10)}, 10: -2},
        [(1,2,3),(2,3,3),(1,4,3),(1,5,3),(5,6,3),(6,7,3),(7,8,3),(8,9,3),(9,10,4)]),
    3: ({**{i: -4 for i in range(1, 13)}, 5: -2, 9: -2},
        [(1,2,3),(2,3,3),(3,4,3),(1,6,3),(6,7,3),(7,8,3),(1,12,3),
         (4,5,4),(5,11,4),(11,10,"inf"),(10,9,4),(9,8,4)]),
    4: ({**{i: -4 for i in range(1, 12)}, 7: -2, 9: -2},
        [(1,2,3),(2,3,3),(3,4,3),(4,5,3),(1,6,3),(5,8,3),(1,10,3),(5,11,3),
         (6,7,4),(8,9,4)]),
    5: ({**{i: -4 for i in range(1, 15)}, 9: -2, 10: -2, 11: -2, 12: -2},
        [(1,2,3),(2,3,3),(3,4,3),(4,5,3),(5,6,3),(6,7,3),(7,8,3),(8,1,3),
         (1,9,4),(9,14,4),(14,12,4),(12,5,4),(7,10,4),(10,13,4),(13,11,4),(11,3,4),
         (13,14,"inf")])}
FIGURE_ORDER = {
    1: "outer square 1..8, then the four diagonal nodes 9..12 from corner 7 to corner 3",
    2: "the ten-node bond list already used in the manuscript; only node 10 is white",
    3: "top row 1..5, left side 6,7,8 then white 9, diagonal 10,11, spur 12",
    4: "top row 1..5, left side 6, white 7, right side 8, white 9, spurs 10,11",
    5: "outer square 1..8; white diagonal nodes 9,10 left and 11,12 right; central black nodes 13,14"}


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


def sat_kernel_rows(rowvec):
    n = len(rowvec)
    g = gcd(*[abs(int(x)) for x in rowvec])
    S, U_, V = matrix(ZZ, [[int(x) // g for x in rowvec]]).smith_form()
    assert S[0, 0] == 1
    return matrix(ZZ, n - 1, n, [[V[i, j] for i in range(n)] for j in range(1, n)])


def unimodular_completion(c):
    n = len(c)
    assert gcd(*[abs(int(x)) for x in c]) == 1
    S, U_, V = matrix(ZZ, [list(c)]).smith_form()
    Q = V.inverse()
    Q = matrix(ZZ, [[int(Q[i, j]) for j in range(n)] for i in range(n)])
    if list(Q.row(0)) != list(c):
        Q = -Q
    assert list(Q.row(0)) == list(c) and abs(Q.det()) == 1
    return Q


def cusp_frame(v):
    Wm = sat_kernel_rows([ip(BAS[i], v) for i in range(N)])
    sol = Wm.change_ring(QQ).transpose().solve_right(vector(QQ, v))
    assert all(x in ZZ for x in sol)
    Wp = unimodular_completion([int(x) for x in sol]) * Wm
    assert vector(ZZ, list(Wp.row(0))) == v
    return Wp


def normalized_entry(ri, rj):
    bij = ip(ri, rj)
    d = ip(ri, ri) * ip(rj, rj)
    if d == 4:
        den = K2(2)
    elif d == 8:
        den = 2 * s
    elif d == 16:
        den = K2(4)
    else:
        raise AssertionError(d)
    ans = K2(bij) / den
    assert ans >= 0, (bij, ri, rj)
    return ans


def bond(g):
    if g == 0:
        return 2
    if g == HALF:
        return 3
    if g == SQRT2_HALF:
        return 4
    if g == 1:
        return "inf"
    if g > 1:
        return "dotted"
    raise AssertionError("unrecognised cosine %s" % g)


def graph_of(squares, bonds):
    gr = nx.Graph()
    gr.add_nodes_from((i, {"square": q}) for i, q in squares.items())
    gr.add_edges_from((i, j, {"bond": b}) for i, j, b in bonds if b != 2)
    return gr


def normal_form(H):
    D = IntegralLattice(H).discriminant_group().normal_form()
    return D, (D._modulus, tuple(D.invariants()), D.gram_matrix_quadratic(), D.gram_matrix_bilinear())


def complement(delta):
    pairing_row = matrix(ZZ, 1, N, list(vector(ZZ, delta) * G))
    B = pairing_row.right_kernel().basis_matrix()
    assert B.nrows() == 11 and B * G * vector(ZZ, delta) == vector(ZZ, [0] * 11)
    return B, B * G * B.transpose()


def bezout(values):
    g, coeffs = 0, []
    for value in values:
        d, a, b = xgcd(g, int(value))
        coeffs = [a * c for c in coeffs] + [b]
        g = d
    assert g == 1 and sum(c * int(v) for c, v in zip(coeffs, values)) == 1
    return coeffs


def eichler(eta, a, x):
    ae = ip(a, eta)
    assert ae == 0 and ip(a, a) % 2 == 0
    return x + ip(x, eta) * a - ip(x, a) * eta - (ip(a, a) // 2) * ip(x, eta) * eta


def eichler_matrix(eta, a):
    return matrix(ZZ, N, N, [list(eichler(eta, a, b)) for b in BAS])


def facet_cosines(order, gmat, delta_index):
    out = {}
    for i, j in combinations([t for t in range(len(order)) if t != delta_index], 2):
        a, b = gmat[delta_index, i], gmat[delta_index, j]
        cos = (gmat[i, j] + a * b) / ((1 - a * a) * (1 - b * b)).sqrt()
        out[i, j] = cos
    return out


def show_matrix(M):
    return "[%s]" % "\n ".join("[" + " ".join("%3s" % M[i, j] for j in range(M.ncols())) + "]"
                                  for i in range(M.nrows()))


def cosine_name(c):
    if c == 0:
        return "pi/2"
    if c == HALF:
        return "pi/3"
    if c == SQRT2_HALF:
        return "pi/4"
    if c == 1:
        return "parallel"
    if c > 1:
        return "no-intersection"
    return "NON-COXETER"


print("AEGS white roots: wall Gram matrices, complete induced facet angle tables, and complements")
print("Sage %s; exact ZZ/QQ/quadratic-field arithmetic; networkx %s only for coloured graph matching"
      % (SAGE_VERSION, nx.__version__))
print("T_En Gram determinant %d; target T_Co = <2> + U(2) + E8(2)" % G.det())
HCO = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, -2 * C)
DCO, NCO = normal_form(HCO)
print("T_Co: rank %d, det %d, discriminant normal form\n%s" % (HCO.nrows(), HCO.det(), DCO))
print("")

COBLE_BONDS = {(1,2): 3, (2,3): 3, (1,4): 3, (1,5): 3,
               (5,6): 3, (6,7): 3, (7,8): 3, (8,9): 4}
coblet_matches = []
discriminant_matches = []
for cusp in range(1, 6):
    eta = ETA[cusp]
    roots = ROOTS[cusp]
    squares_fig, bonds_fig = FIGURES[cusp]
    assert len(roots) == len(squares_fig)
    gmat = matrix(K2, len(roots), len(roots),
                  lambda i, j: K2(1) if i == j else normalized_entry(roots[i], roots[j]))
    derived_bonds = [(i + 1, j + 1, bond(gmat[i, j]))
                     for i, j in combinations(range(len(roots)), 2)
                     if bond(gmat[i, j]) != 2]
    derived_squares = {i + 1: ip(roots[i], roots[i]) for i in range(len(roots))}
    target_graph = graph_of(squares_fig, bonds_fig)
    derived_graph = graph_of(derived_squares, derived_bonds)
    matcher = nx.algorithms.isomorphism.GraphMatcher(
        target_graph, derived_graph,
        node_match=lambda a, b: a["square"] == b["square"],
        edge_match=lambda a, b: a["bond"] == b["bond"])
    assert matcher.is_isomorphic(), "the figure transcription does not match the exact roots"
    # target node i -> exact printed-root index i-1
    fig_to_rootidx = {i: matcher.mapping[i] - 1 for i in target_graph.nodes}
    order = [fig_to_rootidx[i] for i in range(1, len(roots) + 1)]
    figure_gmat = matrix(K2, len(roots), len(roots), lambda i, j: gmat[order[i], order[j]])
    figure_gram = matrix(ZZ, len(roots), len(roots), lambda i, j: ip(roots[order[i]], roots[order[j]]))
    assert all(figure_gmat[i, i] == 1 and figure_gram[i, i] == squares_fig[i + 1]
               for i in range(len(roots)))
    for i, j in combinations(range(len(roots)), 2):
        assert bond(figure_gmat[i, j]) == (dict(((min(a,b),max(a,b)),t) for a,b,t in bonds_fig).get((i+1,j+1),2))
    print("=== cusp %d; eta = %s" % (cusp, list(eta)))
    print("figure order: %s" % FIGURE_ORDER[cusp])
    print("coloured-bond graph match to printed nodes: %s" %
          ", ".join("%d->r%d" % (i, order[i - 1] + 1) for i in range(1, len(roots) + 1)))
    print("bond list from exact roots: %s" % derived_bonds)
    print("wall Gram matrix in figure order:\n%s" % show_matrix(figure_gram))
    Frame = cusp_frame(eta)
    Kbasis = Frame.submatrix(1, 0, 10, N)
    assert all(ip(Kbasis.row(i), eta) == 0 for i in range(10))
    Kgram = Kbasis * G * Kbasis.transpose()
    assert Kgram.det() in (-256, -1024)
    for fig_delta in range(1, len(roots) + 1):
        delta_index = fig_delta - 1
        if squares_fig[fig_delta] != -2:
            continue
        delta = roots[order[delta_index]]
        assert ip(delta, delta) == -2 and ip(delta, eta) == 0
        assert gcd(*[abs(int(x)) for x in delta]) == 1
        div_T = gcd(*[abs(ip(delta, b)) for b in BAS])
        div_K = gcd(*[abs(ip(delta, Kbasis.row(i))) for i in range(10)])
        assert div_T == 1 and div_K == 1
        print("-- white node %d (printed root r%d), delta = %s" %
              (fig_delta, order[delta_index] + 1, list(delta)))
        print("delta^2=-2, div_T_En(delta)=%d, gcd(delta.e^perp)=%d" % (div_T, div_K))
        cosines = facet_cosines(order, figure_gmat, delta_index)
        non_coxeter = []
        for (i, j), cos in cosines.items():
            name = cosine_name(cos)
            if name == "NON-COXETER":
                non_coxeter.append((i + 1, j + 1, cos))
            print("  facet angle (%d,%d): cos=%s, %s" % (i + 1, j + 1, cos, name))
        assert not non_coxeter, non_coxeter
        angle_counts = Counter(cosine_name(cos) for cos in cosines.values())
        print("  angle multiset: pi/2=%d, pi/3=%d, pi/4=%d, parallel=%d, no-intersection=%d" %
              (angle_counts["pi/2"], angle_counts["pi/3"], angle_counts["pi/4"],
               angle_counts["parallel"], angle_counts["no-intersection"]))
        print("  all induced finite angles are pi/2, pi/3, or pi/4; the table also records every parallel/no-intersection pair")
        coeff = bezout([ip(delta, Kbasis.row(i)) for i in range(10)])
        a = sum((int(coeff[i]) * Kbasis.row(i) for i in range(10)), vector(ZZ, [0] * N))
        assert ip(a, eta) == 0 and ip(a, delta) == 1 and ip(a, a) % 2 == 0
        E = eichler_matrix(eta, a)
        # E stores basis images in rows, so E^T acts on coordinate columns.
        assert E * G * E.transpose() == G and E.transpose() * vector(ZZ, delta) == vector(ZZ, delta) - vector(ZZ, eta)
        assert E.transpose() * vector(ZZ, eta) == vector(ZZ, eta)
        quotient_trivial = True
        for row in Kbasis.rows():
            difference = E.transpose() * row - row
            coordinates = Frame.change_ring(QQ).transpose().solve_right(vector(QQ, difference))
            quotient_trivial &= all(x in ZZ for x in coordinates) and all(int(coordinates[i]) == 0 for i in range(1, 11))
        assert quotient_trivial
        for k in range(-2, 3):
            Ek = E ** (-k)
            assert Ek * G * Ek.transpose() == G
            assert Ek.transpose() * vector(ZZ, delta) == vector(ZZ, delta) + k * vector(ZZ, eta)
        print("  Eichler lift-independent perpendicular: explicit isometry for delta -> delta+k eta, k=-2,...,2; E^a fixes eta and is trivial on eta^perp/eta")
        Bdelta, Hdelta = complement(delta)
        Ddelta, Ndelta = normal_form(Hdelta)
        assert Hdelta.det() == HCO.det() and Ndelta == NCO
        discriminant_matches.append((cusp, fig_delta, order[delta_index] + 1))
        print("  perpendicular Gram matrix:\n%s" % show_matrix(Hdelta))
        print("  rank=%d det=%d; discriminant normal form equals T_Co:\n%s" %
              (Hdelta.nrows(), Hdelta.det(), Ddelta))
        if cusp == 2 and fig_delta == 10:
            facet_bonds = {}
            for (i, j), cos in cosines.items():
                b = bond(cos)
                if b != 2:
                    facet_bonds[(i + 1, j + 1)] = b
            assert facet_bonds == COBLE_BONDS
            coblet_matches.append((cusp, fig_delta, order[delta_index] + 1, facet_bonds))
        print("")
assert coblet_matches == [(2, 10, 10, COBLE_BONDS)]
assert discriminant_matches == [(2, 10, 10), (3, 5, 8), (3, 9, 12),
                                (4, 7, 10), (4, 9, 8),
                                (5, 9, 14), (5, 10, 12), (5, 11, 11), (5, 12, 13)]
print("all nine perpendicular discriminant normal forms equal T_Co: %s" % discriminant_matches)
print("unique match to the nine-node Coble chamber bond list: cusp 2, white figure node 10 (printed root r10)")
print("PYEXIT=0")