"""research#658: the two remaining residues reduce to one group-theoretic computation.

Item 1e (the lifting) is Gamma_Co <= ker rho_{T_Co}.  Item 1f (the image of Phi) is: is w~ orthogonal to
some element of the Gamma_En-orbit of k?  This probe shows, exactly, that both are decided by the image
of one stabilizer under one discriminant representation, and it decides the cheap attempt on 1f
negatively, so that nobody mistakes it for the answer.

1f, the elementary attempt.  k = e~ - f~ and delta = e~ - f~ + f~' are (-2)-vectors of T_En, hence in one
O(T_En)-orbit by AEGS25, printed p. 587 (after Namikawa, Math. Ann. 270 (1985), Thm. 2.13).  The move
k |-> k + f~' is realised by the elementary transvection tau(x) = x + (x.u)v - (x.v)u with {u,v} =
{f~, f~'}: it is integral, an isometry, of determinant 1, and tau(k) = delta.  It is NOT in the
discriminant kernel, and neither is any of the 28 elementary transvections realising the same move that
this probe finds.  So the cheap transporter is unavailable, and by exactly the same measure as in 1e.

What that leaves, stated once for both items.  An element g with g(k) = delta exists in O(T_En); to place
one in Gamma_En = ker(rho) cap O^+ one needs the discriminant action of g to be cancelled by an element
of Stab(k).  Both residues are therefore decided by

    rho( Stab_{O(T_En)}(k) )  inside  O(A_{T_En}),  a group of order 46 998 591 897 600,

together with the sign.  That image is a finite-index subgroup of a finite group; nothing in this
repository computes it, and neither 1e nor 1f can be settled without it.  The probe prints "undecided"
and names the input, so that no later run mistakes an absence for a computation.

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
    """Is rho(m) the identity on A = G^{-1}Z^n / Z^n?"""
    mit = transpose(inverse(m))
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(mit, y)
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

    print("T_En = U + U(2) + E8(2), rank %d" % N)
    print("k = e~ - f~      square %d   delta = k + f~'   square %d   w = 2e~ + e~'   square %d"
          % (dot(k, k), dot(delta, delta), dot(w, w)))
    print("w . delta = %d   (the witness's cheap test)" % dot(w, delta))
    print()

    tau = transvection(as_vector((1, 1)), fp)          # u = f~, v = f~'
    print("the elementary transporter tau (u = f~, v = f~'):")
    print("  integral %s   isometry %s   determinant %d   tau(k) = delta %s"
          % (is_integral(tau), is_isometry(tau), determinant(tau), mv(tau, k) == delta))
    print("  discriminant action trivial: %s" % discriminant_trivial(tau))
    print()

    moves = []
    for a, b, c, d in product(range(-3, 4), repeat=4):
        u = as_vector((0, a), (1, b), (2, c), (3, d))
        if dot(u, u) != 0 or dot(u, k) != 1 or dot(u, fp) != 0:
            continue
        g = transvection(u, fp)
        if not is_isometry(g) or mv(g, k) != delta:
            continue
        moves.append((u, g))
    for a, b, c, d in product(range(-3, 4), repeat=4):
        v = as_vector((0, a), (1, b), (2, c), (3, d))
        if dot(v, v) != 0 or dot(v, k) != -1 or dot(v, fp) != 0:
            continue
        g = transvection(fp, v)
        if not is_isometry(g) or mv(g, k) != delta:
            continue
        moves.append((v, g))
    inside = [u for u, g in moves if discriminant_trivial(g)]
    print("elementary transvections realising k |-> delta found: %d" % len(moves))
    print("  of those with trivial discriminant action: %d" % len(inside))
    print()

    print("AEGS25, printed p. 587 (after Namikawa, Math. Ann. 270 (1985), Thm. 2.13): one (-2)-vector")
    print("modulo O(T_En), so k and delta are O(T_En)-conjugate.  Every elementary conjugate is")
    print("outside the discriminant kernel, so the question for both residues is the same one:")
    print("  does rho(Stab_{O(T_En)}(k)) meet the coset of rho(tau) in O(A_{T_En})?")
    print("verdict: undecided -- the deciding input is that stabilizer image, a subgroup of a group of")
    print("order 46 998 591 897 600, which nothing in this repository computes.")


if __name__ == "__main__":
    main()
