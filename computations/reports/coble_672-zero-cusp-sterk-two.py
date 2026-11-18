"""Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber.

Input, read back and not copied, from two committed transcripts:

  computations/reports/coble_enriques-white-root-facets-run.txt
      the five Enriques cusp vectors eta_1,...,eta_5 in T_En = U + U(2) + E8(2) coordinates,
      their exact wall Gram matrices in figure order, and the white nodes;
  computations/reports/coble_pair-semifan-cusps-run.txt
      per cusp, the white node, the pairings (r_i, delta), and the induced facets.

Everything below is exact integer / rational arithmetic in plain python3.

  A. T_Co = delta^perp, delta = e - f; for each of the five cusp vectors: its pairings with
     delta (so whether it is a vector of T_Co at all), its square, its primitivity, its
     divisibility in T_En and in T_dp, and the boundary lattice eta^perp_{T_Co}/Z eta ---
     rank, determinant (Bareiss), signature, invariant factors, and the 2-elementary
     invariants (a, delta) through the dual basis.
  B. the restricted chamber C cap delta^perp at each of the four cusps k = 2,3,4,5 ---
     its walls, their squares, its labelled edge graph, and its number of distinct walls ---
     against the adjacency table of thm:coble-cusp-chamber (AN06 Table 1, entry N = 10,
     printed p. 52).

Run:  python3 computations/reports/coble_672-zero-cusp-sterk-two.py
"""
import math
import re
from fractions import Fraction as F
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[2]
WHITE = REPO / "computations/reports/coble_enriques-white-root-facets-run.txt"
PAIR = REPO / "computations/reports/coble_pair-semifan-cusps-run.txt"


# ---------------------------------------------------------------- exact linear algebra
def e8_gram():
    """Bourbaki E8, negated: simple roots of square -2, adjacent pairing +1."""
    nbrs = {1: [3], 2: [4], 3: [1, 4], 4: [2, 3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7]}
    C = [[0] * 8 for _ in range(8)]
    for i in range(8):
        C[i][i] = -2
    for i in range(1, 9):
        for j in nbrs[i]:
            if j > i:
                C[i - 1][j - 1] = 1
                C[j - 1][i - 1] = 1
    return C


def block_diag(*Ms):
    n = sum(len(M) for M in Ms)
    m = sum(len(M[0]) for M in Ms)
    G = [[0] * m for _ in range(n)]
    r = c = 0
    for M in Ms:
        for i in range(len(M)):
            for j in range(len(M[0])):
                G[r + i][c + j] = M[i][j]
        r += len(M)
        c += len(M[0])
    return G


U = [[0, 1], [1, 0]]
U2 = [[0, 2], [2, 0]]
TWO = [[2]]
E8 = e8_gram()
E8_2 = [[2 * x for x in row] for row in E8]
G_Co = block_diag(TWO, U2, E8_2)                 # <2> + U(2) + E8(2)
G_En = block_diag(U, U2, E8_2)                   # U + U(2) + E8(2)
G_dp = block_diag(U, U2, E8, E8)                 # U + U(2) + E8^2


def mat(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def pairing(G, v, w):
    return sum(v[i] * G[i][j] * w[j] for i in range(len(v)) for j in range(len(v)))


def square(G, v):
    return pairing(G, v, v)


def divisibility(G, v):
    """gcd of beta(v,x) over x in the lattice: the gcd of the entries of G v."""
    col = [c[0] for c in mat(G, [[x] for x in v])]
    g = 0
    for x in col:
        g = math.gcd(g, abs(x))
    return g


def xgcd(a, b):
    if b == 0:
        return (abs(a), (1 if a >= 0 else -1), 0)
    r0, r, s0, s, t0, t = a, b, 1, 0, 0, 1
    while r:
        q = r0 // r
        r0, r = r, r0 - q * r
        s0, s = s, s0 - q * s
        t0, t = t, t0 - q * t
    if r0 < 0:
        r0, s0, t0 = -r0, -s0, -t0
    return r0, s0, t0


def reduce_row(r):
    """(d, T) with T unimodular, r T = (d, 0, ..., 0); columns 1.. of T span ker(r)."""
    n = len(r)
    r = list(r)
    T = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def swapcols(j, k):
        r[j], r[k] = r[k], r[j]
        for i in range(n):
            T[i][j], T[i][k] = T[i][k], T[i][j]

    for j in range(1, n):
        if r[j] == 0:
            continue
        if r[0] == 0:
            swapcols(0, j)
            if r[j] == 0:
                continue
        a, b = r[0], r[j]
        g, s, t = xgcd(a, b)
        c0 = [T[i][0] for i in range(n)]
        cj = [T[i][j] for i in range(n)]
        p, q = -b // g, a // g
        for i in range(n):
            T[i][0] = s * c0[i] + t * cj[i]
            T[i][j] = p * c0[i] + q * cj[i]
        r[0], r[j] = g, 0
    if r[0] < 0:                      # fix the sign of the generator so that r T = (+d, 0, ...)
        r[0] = -r[0]
        for i in range(n):
            T[i][0] = -T[i][0]
    return r[0], T


def det_bareiss(G):
    n = len(G)
    M = [row[:] for row in G]
    sign = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // (M[k - 1][k - 1] if k else 1)
    return sign * M[n - 1][n - 1]


def signature(G):
    ev = np.linalg.eigvalsh(np.array(G, dtype=float))
    return (sum(1 for x in ev if x > 1e-6), sum(1 for x in ev if x < -1e-6))


def inverse_unimodular(S):
    m = len(S)
    A = [[F(S[i][j]) for j in range(m)] + [F(1 if i == j else 0) for j in range(m)] for i in range(m)]
    for c in range(m):
        p = next(i for i in range(c, m) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for i in range(m):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[c][j] for j in range(2 * m)]
    assert all(x.denominator == 1 for row in A for x in row), "inverse not integral"
    return [[int(x) for x in row[m:]] for row in A]


def solve_coords(K, v):
    """coordinates of v in the Z-basis given by the columns of K (exact, asserted integral)."""
    n, m = len(K), len(K[0])
    M = [[F(K[i][j]) for j in range(m)] + [F(v[i])] for i in range(n)]
    piv, rr = [], 0
    for c in range(m):
        p = next((i for i in range(rr, n) if M[i][c] != 0), None)
        if p is None:
            continue
        M[rr], M[p] = M[p], M[rr]
        pv = M[rr][c]
        M[rr] = [x / pv for x in M[rr]]
        for i in range(n):
            if i != rr and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[rr][j] for j in range(m + 1)]
        piv.append(c)
        rr += 1
    u = [0] * m
    for i, c in enumerate(piv):
        u[c] = M[i][m]
    assert all(x.denominator == 1 for x in u), "v is not in the span"
    return [int(x) for x in u]


def quotient_gram(G, u):
    """Gram matrix of u^perp / Z u, for a primitive isotropic u.

    u^perp has the basis K (a kernel basis); u is primitive in it; the quotient basis is the
    complement of Z u found by completing u to a basis of Z^{n-1}.  (The kernel of u^(perp) is
    not a complement: u itself lies in it, u^2 = 0.)
    """
    n = len(G)
    r = [c[0] for c in mat(G, [[x] for x in u])]
    _, T1 = reduce_row(r)
    K = [[T1[i][j] for j in range(1, n)] for i in range(n)]                 # n x (n-1)
    H = mat(mat([[K[j][i] for j in range(n)] for i in range(n - 1)], G), K)  # (n-1) x (n-1)
    uc = solve_coords(K, u)
    assert math.gcd(*uc) == 1, "u is not primitive in u^perp"
    _, T = reduce_row(uc)
    S = [[T[j][i] for j in range(len(T))] for i in range(len(T))]           # S uc = e_1
    V = inverse_unimodular(S)
    assert [V[i][0] for i in range(len(V))] == uc
    m = n - 1
    C = [[V[i][j] for j in range(1, m)] for i in range(m)]
    return mat(mat([[C[j][i] for j in range(m)] for i in range(m - 1)], H), C)


def invariant_factors(G):
    """Smith normal form diagonal of a nonsingular symmetric integer matrix."""
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(Matrix(G), domain=None)
    return [abs(int(D[i, i])) for i in range(len(G))]


def two_elementary(G):
    """(rank, a, delta) for an even 2-elementary lattice; q evaluated on the dual basis."""
    n = len(G)
    A = [[F(G[i][j]) for j in range(n)] + [F(1 if i == j else 0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[c][j] for j in range(2 * n)]
    Ginv = [[A[i][j + n] for j in range(n)] for i in range(n)]
    det = det_bareiss(G)
    a = 0
    m = abs(det)
    while m % 2 == 0:
        a += 1
        m //= 2
    delta = 0
    for i in range(n):
        q = Ginv[i][i] / 2                     # q of the i-th dual basis vector
        if q.denominator != 1:
            delta = 1
    return n, a, delta


# ---------------------------------------------------------------- read the transcripts
import platform

print("Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber")
print("python3 %s; exact integer and rational arithmetic only (numpy only for a signature check)"
      % platform.python_version())
print("input, read back and not copied:")
print("  computations/reports/coble_enriques-white-root-facets-run.txt"
      "  (the five cusp vectors and the exact wall Gram matrices)")
print("  computations/reports/coble_pair-semifan-cusps-run.txt"
      "  (white nodes and the (r_i, delta) pairings)")
print()
eta = {}
for ln in WHITE.read_text(encoding="utf-8").splitlines():
    m = re.match(r"=== cusp (\d+); eta = \[([^\]]+)\]", ln)
    if m:
        eta[int(m.group(1))] = [int(x) for x in m.group(2).split(",")]
delta = [1, -1] + [0] * 10                     # delta = e - f in T_En
print("read back from coble_enriques-white-root-facets-run.txt: cusps", sorted(eta))
print("delta = e - f: square %d, div_T_En %d, rank of delta^perp %s"
      % (square(G_En, delta), divisibility(G_En, delta),
         len(quotient_gram(G_En, delta))))
print("T_Co = delta^perp: rank 11, det %d, signature %s, even %s"
      % (det_bareiss(G_Co), signature(G_Co), all(G_Co[i][i] % 2 == 0 for i in range(11))))
print()

print("=== part A. the five cusp vectors inside and outside T_Co")
print("  cusp  (eta,delta)  square  gcd coords  div_T_En  div_T_dp  |  eta^perp_T_Co/Zeta")
for k in sorted(eta):
    v = eta[k]
    pd = pairing(G_En, v, delta)
    g = 0
    for x in v:
        g = math.gcd(g, abs(x))
    w = [v[0], v[1], v[2], v[3]] + v[4:] + v[4:]        # T_En -> T_dp, E8(2) diagonally
    line = "  %4d  %10d  %6d  %10d  %8d  %8d  |" % (k, pd, square(G_En, v), g,
                                                    divisibility(G_En, v), divisibility(G_dp, w))
    if pd == 0:
        vCo = [v[0]] + v[2:]                            # delta^perp: e and f have equal coefficients
        assert v[1] == v[0]
        Q = quotient_gram(G_Co, vCo)
        d = divisibility(G_Co, vCo)
        n, a, dl = two_elementary(Q)
        print(line + ("  div_T_Co %d, rank %d, det %d, signature %s, even %s,"
                      " invariants (r,a,delta) = (%d,%d,%d)"
                      % (d, len(Q), det_bareiss(Q), signature(Q),
                         all(Q[i][i] % 2 == 0 for i in range(len(Q))), n, a, dl)))
    else:
        print(line + "  not a vector of T_Co, so no 0-cusp of F_Co,2 over it")
print()

print("=== part A'. the invariant factors of the four boundary lattices")
for k in (2, 3, 4, 5):
    v = eta[k]
    vCo = [v[0]] + v[2:]
    Q = quotient_gram(G_Co, vCo)
    print("  cusp %d: %s" % (k, invariant_factors(Q)))
print()

# ---------------------------------------------------------------- part B
print("=== part B. the restricted chamber C cap delta^perp at each enriques 0-cusp")
text = PAIR.read_text(encoding="utf-8").splitlines()
cur = None
white_node, pairdelta = {}, {}
for ln in text:
    m = re.match(r"-- the 0-cusp over Sterk cusp (\d+)", ln)
    if m:
        cur = int(m.group(1))
        continue
    if cur is None:
        continue
    m = re.search(r"the white node is figure node (\d+)", ln)
    if m:
        white_node[cur] = int(m.group(1))
    m = re.match(r"\s+pairings \(r_i,delta\) nonzero only for \[([^\]]*)\], with values \[([^\]]*)\]", ln)
    if m and m.group(1).strip():
        idx = [int(x) for x in m.group(1).split(",")]
        val = [int(x) for x in m.group(2).split(",")]
        pairdelta[cur] = dict(zip(idx, val))


def wall_gram_from_white(cusp):
    """the exact wall Gram matrix in figure order, as printed in the white-root transcript."""
    lines = WHITE.read_text(encoding="utf-8").splitlines()
    start = None
    for i, ln in enumerate(lines):
        if re.match(r"=== cusp %d; eta" % cusp, ln):
            start = i
            break
    j = start
    while not lines[j].startswith("wall Gram matrix"):
        j += 1
    j += 1
    M = []
    while j < len(lines) and lines[j].strip().startswith("["):
        M.append([int(x) for x in lines[j].strip().strip("[]").split()])
        j += 1
    return M


def spider(G, walls):
    """canonical description of the labelled graph of a wall set: whether it is a tree, its
    degree sequence, the squares, the bond labels (cos(pi/label) = |g|), and, when the graph
    is a tree with a single branch vertex, the arms as (length, label of the last edge, square
    of the end vertex).  Written out rather than searched for, since the graphs compared here
    are small."""
    idx = sorted(walls)
    n = len(idx)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if G[idx[i]][idx[j]] != 0]
    deg = [0] * n
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    labels = {}
    for i, j in edges:
        cos = abs(float(G[idx[i]][idx[j]])) / math.sqrt(
            float(G[idx[i]][idx[i]]) * float(G[idx[j]][idx[j]]))
        if abs(cos - 0.5) < 1e-9:
            lab = "3"
        elif abs(cos - 2 ** -0.5) < 1e-9:
            lab = "4"
        elif abs(cos - 1) < 1e-9:
            lab = "thick"
        else:
            lab = "other"
        labels[(i, j)] = lab
    squares = [G[idx[i]][idx[i]] for i in range(n)]
    arms = None
    branch = [i for i in range(n) if deg[i] >= 3]
    if len(edges) == n - 1 and len(branch) == 1:
        b = branch[0]
        arms = []
        for i, j in edges:
            if b not in (i, j):
                continue
            prev, cur_ = b, (j if i == b else i)
            length, last = 1, (min(prev, cur_), max(prev, cur_))
            while deg[cur_] == 2:
                nxt = [z for (a, c) in edges for z in ([c] if a == cur_ else ([a] if c == cur_ else []))
                       if z != prev]
                prev, cur_ = cur_, nxt[0]
                length += 1
                last = (min(prev, cur_), max(prev, cur_))
            arms.append((length, labels[last], squares[cur_]))
        arms.sort()
    return dict(tree=(len(edges) == n - 1), n=n, degrees=sorted(deg),
                squares=[str(x) for x in sorted(squares)],
                edge_labels=sorted(labels.values()), arms=arms)


coble_edges = [(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
coble_square = {w: (-2 if w == 9 else -4) for w in range(1, 10)}
nC = 9
G_coble = [[0] * nC for _ in range(nC)]
for w in range(1, 10):
    G_coble[w - 1][w - 1] = coble_square[w]
for u, v in coble_edges:
    G_coble[u - 1][v - 1] = 2
    G_coble[v - 1][u - 1] = 2
print("  thm:coble-cusp-chamber (AN06 Table 1, N = 10, printed p. 52), nine walls:")
print("   ", spider(G_coble, set(range(nC))))

for k in (2, 3, 4, 5):
    G = wall_gram_from_white(k)
    white = white_node[k]                     # the white node is delta itself; delta projects to 0
    pd = {i: 0 for i in range(1, len(G) + 1)}
    pd.update(pairdelta.get(k, {}))
    keep = [i for i in range(1, len(G) + 1) if i != white]
    # the projected wall of a root alpha is alpha + ((alpha,delta)/2) delta, and since
    # delta^2 = -2 its square is alpha^2; the pairing becomes g_ij + g_id g_jd / 2.
    P = [[0] * len(G) for _ in range(len(G))]
    for a in keep:
        for b in keep:
            P[a - 1][b - 1] = G[a - 1][b - 1] + F(pd[a] * pd[b], 2)
    walls = set(i - 1 for i in keep)
    desc = spider(P, walls)
    thick = sum(1 for lab in desc["edge_labels"] if lab == "thick")
    print("  cusp %d: white node figure %d; %d projected roots, %d induced parallel pair(s),"
          " %d distinct walls" % (k, white, len(walls), thick, len(walls) - thick))
    print("   ", desc)
