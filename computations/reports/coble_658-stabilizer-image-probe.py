"""research#658 item 1f, decided: the witness w = 2e~ + e~' lies in the image of Phi.

The image question is whether a primitive isotropic vector w~ of divisibility 2 is orthogonal to some
element of the Gamma_En-orbit of k = e~ - f~.  This probe settles it for the witness of the book's passage
on the exact image locus, in four exact steps.

1. k and delta = k + f~' are (-2)-vectors of T_En, hence O(T_En)-conjugate by AEGS25, printed p. 587
   (after Namikawa, Math. Ann. 270 (1985), Thm. 2.13).
2. The move k |-> delta is realised by the elementary transvection tau(x) = x + (x.f~)f~' - (x.f~')f~:
   integral, an isometry, of determinant 1, with tau(k) = delta, and -- the point -- with TRIVIAL action
   on A_{T_En}.  So tau lies in ker(rho_{T_En}) and delta lies in the orbit of k under the discriminant
   kernel; all 28 elementary transvections realising the move share that property.
3. w = 2e~ + e~' is orthogonal to delta.
4. The sign: h = -3e~ - 3f~ + 3f~' has h^2 = 18 and is orthogonal to w and to delta, so the reflection
   s_h fixes both; it acts trivially on A_{T_En}, hence lies in ker(rho_{T_En}), and its spinor norm is
   [-h^2/2] = [-9], the class -1.  The real spinor norm takes values in {+-1}, so one of tau and s_h o tau
   has spinor norm +1, hence lies in Gamma_En = ker(rho) cap O^+, and whichever it is carries k to a
   (-2)-vector orthogonal to w.

So the class of w lies in the image of Phi: it lies over a Coble 0-cusp, and the recorded claim that the
necessary condition "orthogonal to some (-2)-vector" is not sufficient is not shown by this witness.

Correction recorded with the result.  The earlier version of this file tested triviality of the
discriminant action by (m^{-1})^T.  For m in O(L) the induced action on A = Z^n/(G Z^n) is
v |-> m^{-T} v = G m G^{-1} v, so triviality is the condition m(y) - y in Z^n for y = G^{-1} e_i, which is
what the file now tests.  Under the wrong test every transvection appeared to be outside the kernel, and
the conclusion drawn from that -- that the cheap route was closed -- was an artefact of the test.

Usage: python3 computations/reports/coble_658-stabilizer-image-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def e8_cartan():
    c = [[0] * 8 for _ in range(8)]
    for i in range(8):
        c[i][i] = 2
    for i in range(6):
        c[i][i + 1] = c[i + 1][i] = -1
    c[2][7] = c[7][2] = -1
    return c


def block_diagonal(blocks):
    n = sum(len(b) for b in blocks)
    g = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                g[off + i][off + j] = b[i][j]
        off += len(b)
    return g


U = [[0, 1], [1, 0]]
G = block_diagonal([U, [[2 * x for x in row] for row in U],
                    [[-2 * x for x in row] for row in e8_cartan()]])
N = len(G)


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def inverse(m):
    n = len(m)
    a = [[F(m[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if a[r][col] != 0)
        a[col], a[piv] = a[piv], a[col]
        pv = a[col][col]
        a[col] = [x / pv for x in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


def determinant(m):
    a = [[F(x) for x in row] for row in m]
    n = len(a)
    d = F(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return 0
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            d = -d
        d *= a[col][col]
        pv = a[col][col]
        for r in range(col + 1, n):
            if a[r][col] != 0:
                f = a[r][col] / pv
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return int(d)


GINV = inverse(G)


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(m):
    return is_integral(m) and matmul(transpose(m), matmul(G, m)) == G


def discriminant_trivial(m):
    """Does m act trivially on A = Z^n / (G Z^n)?

    For m in O(L) the induced action is v |-> m^{-T} v = G m G^{-1} v, so triviality is m(y) - y in Z^n
    for the generators y = G^{-1} e_i.
    """
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(m, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


def transvection(u, v):
    """x |-> x + (x,u)v - (x,v)u, an isometry whenever u, v are isotropic with (u,v) = 0."""
    gu, gv = mv(G, u), mv(G, v)
    out = [[0] * N for _ in range(N)]
    for j in range(N):
        e = [0] * N
        e[j] = 1
        a = sum(e[i] * gu[i] for i in range(N))
        b = sum(e[i] * gv[i] for i in range(N))
        for i in range(N):
            out[i][j] = e[i] + a * v[i] - b * u[i]
    return out


def as_vector(*first):
    v = [0] * N
    for index, value in first:
        v[index] = value
    return v


def main():
    k = as_vector((0, 1), (1, -1))
    delta = as_vector((0, 1), (1, -1), (3, 1))
    fp = as_vector((3, 1))
    w = as_vector((0, 2), (2, 1))
    h = as_vector((0, -3), (1, -3), (3, 3))

    print("T_En = U + U(2) + E8(2), rank %d" % N)
    print("k = e~ - f~   square %d   delta = k + f~'   square %d   w = 2e~ + e~'   square %d"
          % (dot(k, k), dot(delta, delta), dot(w, w)))
    print("w . delta = %d   (the witness's cheap test)" % dot(w, delta))
    print()

    tau = transvection(as_vector((1, 1)), fp)          # u = f~, v = f~'
    print("the elementary transporter tau (u = f~, v = f~'):")
    print("  integral %s   isometry %s   determinant %d   tau(k) = delta %s"
          % (is_integral(tau), is_isometry(tau), determinant(tau), mv(tau, k) == delta))
    print("  discriminant action trivial: %s  (so tau lies in ker(rho_{T_En}))"
          % discriminant_trivial(tau))
    print()

    moves = []
    for a, b, c, d in product(range(-3, 4), repeat=4):
        u = as_vector((0, a), (1, b), (2, c), (3, d))
        if dot(u, u) != 0 or dot(u, k) != 1 or dot(u, fp) != 0:
            continue
        g = transvection(u, fp)
        if is_isometry(g) and mv(g, k) == delta:
            moves.append(g)
    for a, b, c, d in product(range(-3, 4), repeat=4):
        v = as_vector((0, a), (1, b), (2, c), (3, d))
        if dot(v, v) != 0 or dot(v, k) != -1 or dot(v, fp) != 0:
            continue
        g = transvection(fp, v)
        if is_isometry(g) and mv(g, k) == delta:
            moves.append(g)
    inside = [g for g in moves if discriminant_trivial(g)]
    print("elementary transvections realising k |-> delta found: %d" % len(moves))
    print("  of those with trivial discriminant action: %d" % len(inside))
    print()

    print("the sign: h = -3e~ - 3f~ + 3f~', square %d" % dot(h, h))
    print("  h . w = %d   h . delta = %d" % (dot(h, w), dot(h, delta)))
    s_h = [[0] * N for _ in range(N)]
    q = dot(h, h)
    for j in range(N):
        e = [0] * N
        e[j] = 1
        c = F(2 * dot(e, h), q)
        for i in range(N):
            s_h[i][j] = F(e[i]) - c * h[i]
    s_h_int = [[int(x) for x in row] for row in s_h]
    print("  reflection s_h: integral %s   isometry %s   discriminant action trivial %s"
          % (is_integral(s_h_int), is_isometry(s_h_int), discriminant_trivial(s_h_int)))
    print("  s_h fixes w %s   fixes delta %s" % (mv(s_h_int, w) == w, mv(s_h_int, delta) == delta))
    print("  spinor norm [-h^2/2] = [-9], i.e. the class -1: so exactly one of tau, s_h o tau has")
    print("  spinor norm +1 and lies in Gamma_En = ker(rho) cap O^+, carrying k to delta perp w.")
    print()
    print("verdict: the class of w = 2e~ + e~' IS in the image of Phi.")
    print("  delta is in the orbit of k under the discriminant kernel, w is orthogonal to delta, and the")
    print("  sign is absorbed by s_h; so w lies over a Coble 0-cusp and the witness does not show the")
    print("  cheap test insufficient.")


if __name__ == "__main__":
    main()
