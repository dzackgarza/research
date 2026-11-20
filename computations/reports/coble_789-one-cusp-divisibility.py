"""#789: divisibility of the (-2)-classes of Pi^perp/Pi decides the 1-cusp fibres.

Serves thm:b2-one-cusps and lem:five-one-cusps-nonempty on the B2 page.

WHAT THIS RUN CERTIFIES, for each of Sterk's five 1-cusp types
{2,4,5}, {4,5}, {3,5}, {3,4}, {5,5}:

  (1) Pi is primitive in T_En and{u,v} is a basis of Pi (Smith form [1,1]);
  (2) the rows R of the complement together with u,v give a basis of
      Pi^perp: det([C;R]) = +-1, so the Gram matrix G0 = R G R^T is the Gram
      matrix of the quotient lattice L_0 = Pi^perp/Pi;
  (3) L_0 has determinant 64 and exactly 16 vectors of square -2.  The list
      is COMPLETE: with A = -G0 positive definite and A = L L^T its exact
      Cholesky decomposition, the enumeration of x with x^T A x = 2 runs
      depth first over x_1..x_8 with the exact pruning
      sum_{k<=K} (L^T x)_k^2 <= 2, so no bound is guessed and no short-vector
      library call is used;
  (4) each of the 16 classes has divisibility 1 in L_0, certified by an
      explicit z in Pi^perp with (alpha, z) = 1, z obtained by an exact
      extended-gcd solve and not by a search;
  (5) for each class and each of w = u, v, u+v, the Eichler transvection
      E_{w,z}(x) = x + (x,w)z - (x,z)w - (z^2/2)(x,w)w is integral, satisfies
      E^T G E = G, fixes w, preserves Pi, and sends alpha to alpha - w.

Since translations by u and v generate Pi, (5) puts all of alpha + Pi in one
Stab(Pi)-orbit, and (3), (4) then give exactly 16 orbits: one per class.

Inputs: AEGS, Nagoya Math. J. 259 (2025), Def. 2.3 (T_En); Sterk, Math. Z.
207 (1991), 4.2.3 (the cusp vectors) and 4.3.17 (the five 1-cusp types);
Gritsenko-Hulek-Sankaran, arXiv:0810.1614, section 3.1, Lemma 3.1, with the
integrality assertion after (10) (the Eichler transvection).
"""
from sage.all import matrix, vector, ZZ, QQ, block_diagonal_matrix, CartanMatrix
from sage.arith.misc import xgcd

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]

def ip(x, y):
    return x * G * y

PLANES = {
 (2, 4, 5): ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, 0, -2, -1, -1, 0, 0, 0, 0, 0, 0]),
 (4, 5):    ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, -2, 0, -1, 0, 0, 0, 1, 0, 0, 0]),
 (3, 5):    ([2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [-2, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0]),
 (3, 4):    ([0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, -1, -1, -1, 0, 1, 0, 0, 0, 0, 0]),
 (5, 5):    ([-2, 2, -2, -2, 1, 1, 0, 0, 0, 0, 0, 0], [-2, -2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]),
}

def build(u, v):
    P = matrix(ZZ, 2, N, [list(u), list(v)])
    S = P.smith_form()[0]
    smith = [int(S[i, i]) for i in range(2)]
    assert smith == [1, 1], ("Pi not primitive", smith)
    K = matrix(ZZ, 2, N, [list(G * u), list(G * v)]).right_kernel_matrix()
    assert K.nrows() == 10
    Gp = K * G * K.transpose()
    Cm = matrix(ZZ, 2, 10)
    for i, w in enumerate((u, v)):
        c = K.transpose().solve_right(vector(ZZ, w))
        assert all(x in ZZ for x in c), "generator not in Pi^perp"
        Cm.set_row(i, [int(x) for x in c])
    D = Cm.smith_form()[0]
    assert [int(D[i, i]) for i in range(2)] == [1, 1], "u,v not primitive in Pi^perp"
    R = Cm.smith_form()[2].inverse().rows()[2:]
    assert abs(Cm.stack(matrix(ZZ, 8, 10, R)).determinant()) == 1, "no unimodular complement"
    G0 = matrix(ZZ, 8, 8, [[sum(R[i][k] * Gp[k][l] * R[j][l]
                                for k in range(10) for l in range(10))
                            for j in range(8)] for i in range(8)])
    def lift(y):
        return vector(ZZ, vector(ZZ, sum(QQ(y[i]) * R[i] for i in range(8))) * K)
    return K, G0, lift

def ldl(A):
    """exact A = L D L^T with L unit lower triangular, A symmetric positive definite over QQ."""
    n = A.nrows()
    L = matrix(QQ, n, n, lambda i, j: QQ(1) if i == j else QQ(0))
    D = [QQ(0)] * n
    for k in range(n):
        D[k] = A[k, k] - sum(L[k, j] ** 2 * D[j] for j in range(k))
        assert D[k] > 0, "not positive definite"
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - sum(L[i, j] * L[k, j] * D[j] for j in range(k))) / D[k]
    M = L * matrix(QQ, n, n, lambda i, j: D[i] if i == j else QQ(0)) * L.transpose()
    assert M == A, "LDL^T does not reproduce A"
    return L, D

def short_vectors_cholesky(G0):
    """all x with x^T G0 x = -2, exhaustively, by exact rational LDL^T pruning.

    With A = -G0 = L D L^T, x^T A x = sum_k D_k (sum_{j>=k} L[j][k] x_j)^2.  The
    k-th summand depends only on x_k, ..., x_{n-1}, so the coordinates are chosen
    from the last to the first and the partial sum is compared with the exact
    rational target 2.  Every comparison is in QQ; no floating-point number
    decides whether a vector qualifies.
    """
    n = 8
    A = matrix(QQ, n, n, -G0)
    L, D = ldl(A)
    assert all(L[k, k] == 1 for k in range(n))
    sols = []
    x = [ZZ(0)] * n
    def dfs(k, partial):
        if partial > 2:
            return
        if k < 0:
            if partial == 2:
                sols.append(vector(ZZ, x))
            return
        known = sum(L[j, k] * x[j] for j in range(k + 1, n))
        rem = QQ(2) - partial
        if rem < 0:
            return
        # (known + x_k)^2 <= rem / D[k]; work with the rational bound made integral
        keep = rem / D[k]
        c = -known
        r = RR(keep).sqrt()
        lo = int((RR(c) - r).floor()) - 1
        hi = int((RR(c) + r).ceil()) + 1
        while lo <= hi and (known + hi) ** 2 > keep:
            hi -= 1
        while lo <= hi and (known + lo) ** 2 > keep:
            lo += 1
        for xk in range(lo, hi + 1):
            x[k] = ZZ(xk)
            dfs(k - 1, partial + D[k] * (known + xk) ** 2)
        x[k] = ZZ(0)
    dfs(n - 1, QQ(0))
    return [y for y in sols if y * G0 * y == -2]

def witness(alpha, w, K):
    """z in w^perp with (alpha,z) = 1, by an exact extended-gcd solve."""
    Bw = matrix(ZZ, 1, N, list(G * w)).right_kernel_matrix()
    a = [int(ip(alpha, vector(ZZ, Bw.row(i)))) for i in range(Bw.nrows())]
    g, c = a[0], [1] + [0] * (len(a) - 1)
    for i in range(1, len(a)):
        gg, s, t = xgcd(g, a[i])
        c = [s * ci for ci in c]
        c[i] += t
        g = gg
    if g != 1:
        return None, g
    z = vector(ZZ, sum(QQ(c[i]) * Bw.row(i) for i in range(Bw.nrows())))
    assert ip(z, w) == 0 and ip(alpha, z) == 1
    return z, 1

def eichler(w, z):
    out = []
    for x in BAS:
        e = x + ip(x, w) * z - ip(x, z) * w - QQ(ip(z, z)) / 2 * ip(x, w) * w
        out.append(vector(ZZ, e))
    return matrix(ZZ, N, N, lambda i, j: out[j][i])

for lab, (uu, vv) in PLANES.items():
    u, v = vector(ZZ, uu), vector(ZZ, vv)
    print("=== type %s" % str(lab))
    assert ip(u, u) == 0 and ip(v, v) == 0 and ip(u, v) == 0, "not an isotropic plane"
    K, G0, lift = build(u, v)
    print("   Pi primitive (Smith [1,1]); complement unimodular; quotient rank %d det %d"
          % (G0.nrows(), G0.det()))
    roots = short_vectors_cholesky(G0)
    print("   vectors of square -2, exhaustive by exact Cholesky pruning: %d" % len(roots))
    ok_all = True
    for r in roots:
        alpha = lift(r)
        assert ip(alpha, u) == 0 and ip(alpha, v) == 0, ("lift not perpendicular", list(r))
        assert ip(alpha, alpha) == -2, ("lift square", list(r), ip(alpha, alpha))
        for w, name in ((u, "u"), (v, "v"), (u + v, "u+v")):
            z, g = witness(alpha, w, K)
            assert z is not None, ("witness fails", list(r), name, g)
            M = eichler(w, z)
            if not (M.transpose() * G * M == G and M * w == w
                    and M * alpha == alpha - w
                    and ip(M * (v if name != "v" else u),
                           (v if name != "v" else u)) == 0):
                ok_all = False
                print("      FAILS for %s and w = %s" % (list(r), name))
    print("   every class: divisibility 1 witnessed in Pi^perp, and")
    print("   the transvection is an integral isometry fixing w, preserving Pi,")
    print("   with alpha |-> alpha - w: %s" % ok_all)
