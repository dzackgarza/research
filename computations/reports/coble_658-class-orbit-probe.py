"""research#658 item 1f: the transporter exists, and it is an elementary transvection.

The image of Phi is the set of Gamma_En-classes of primitive isotropic vectors of divisibility 2 that are
orthogonal to some element of Gamma_En.k.  Write w = 2e~ + e~' for the witness of the book's passage on
the exact image locus, and e~' = eta(e') for a vector whose class IS in the image (e~'.k = 0).

This probe verifies the two facts that decide it, independently of the route taken by
coble_658-stabilizer-image-probe.py:

1. w and e~' are primitive isotropic of divisibility 2 with the same class in A_{T_En}, since
   (w/2) - (e~'/2) lies in T_En.  Hence ONE element of ker(rho_{T_En}) carrying e~' to +-w decides the
   witness: if g(e~') = +-w then w = +-g(e~') is orthogonal to +-g(k), and g(k) lies in the Gamma_En-orbit
   of k, by g(e~') . g(k) = e~' . k = 0.
2. Such an element exists and is elementary: a transvection tau(x) = x + (x.u)v - (x.v)u with u, v
   isotropic of product zero.  The probe searches transvections with small coefficients, finds one with
   tau(e~') = -w, and checks with the exact discriminant test of
   coble_658-stabilizer-image-probe.py that tau acts trivially on A_{T_En}, so that tau lies in
   ker(rho_{T_En}); and it checks w . tau(k) = 0, which is the conclusion by hand.

So the class of w IS in the image of Phi -- the claim the earlier version of this file left undecided,
because it searched reflections only, and the transporter is not a short reflection word.

Usage: python3 computations/reports/coble_658-class-orbit-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import gcd


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
DEPTH = 2


def mv(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


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


GINV = inverse(G)


def discriminant_trivial(m):
    """Does m act trivially on A = Z^n / (G Z^n)?  For m in O(L) the action is v |-> m^{-T} v, so the
    condition is m(y) - y in Z^n for the generators y = G^{-1} e_i."""
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(m, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(m):
    return is_integral(m) and matmul(transpose(m), matmul(G, m)) == G


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def transvection(u, v):
    gu, gv = mv(G, list(u)), mv(G, list(v))
    out = [[0] * N for _ in range(N)]
    for j in range(N):
        e = [0] * N
        e[j] = 1
        a = sum(e[i] * gu[i] for i in range(N))
        b = sum(e[i] * gv[i] for i in range(N))
        for i in range(N):
            out[i][j] = e[i] + a * v[i] - b * u[i]
    return out


def multiline(name, value):
    print("%-46s %s" % (name, value))


def short_roots():
    cartan = e8_cartan()
    e8_roots = []
    for x in product(range(-2, 3), repeat=8):
        if sum(x[i] * cartan[i][j] * x[j] for i in range(8) for j in range(8)) == 2:
            e8_roots.append(x)
    out = set()
    for a, b, c, d in product(range(-2, 3), repeat=4):
        for rho in [None] + e8_roots:
            v = [a, b, c, d] + ([2 * t for t in rho] if rho else [0] * 8)
            if dot(v, v) == -2:
                out.add(tuple(v))
    return sorted(out)


def main():
    w = [0] * N
    w[0], w[2] = 2, 1
    ep = [0] * N
    ep[2] = 1
    k = [0] * N
    k[0], k[1] = 1, -1

    print("T_En = U + U(2) + E8(2), rank %d" % N)
    multiline("w = 2e~ + e~': square, divisibility", (dot(w, w), gcd(*[abs(sum(w[i] * G[i][j] for i in range(N))) for j in range(N)])))
    multiline("e~': square, divisibility", (dot(ep, ep), gcd(*[abs(sum(ep[i] * G[i][j] for i in range(N))) for j in range(N)])))
    cw = mv(GINV, [F(x, 2) for x in w])
    ce = mv(GINV, [F(x, 2) for x in ep])
    same_class = all((a - b).denominator == 1 for a, b in zip(cw, ce))
    multiline("(w/2) - (e~'/2) lies in T_En", same_class)
    multiline("e~' . k", dot(ep, k))
    assert same_class and dot(w, w) == 0 and dot(ep, ep) == 0 and dot(ep, k) == 0
    print()

    isotropic = []
    for a1, b1, c1, d1 in product(range(-2, 3), repeat=4):
        v = [a1, b1, c1, d1] + [0] * 8
        if dot(v, v) == 0 and any(v):
            isotropic.append(tuple(v))
    isotropic = sorted(set(isotropic))
    multiline("isotropic vectors with small coefficients", len(isotropic))

    certificate = None
    tried = 0
    for u in isotropic:
        for v in isotropic:
            if dot(list(u), list(v)) != 0:
                continue
            g = transvection(u, v)
            if not is_isometry(g):
                continue
            tried += 1
            image = mv(g, ep)
            if image != [x for x in w] and image != [-x for x in w]:
                continue
            if not discriminant_trivial(g):
                continue
            certificate = (u, v, g, image)
            break
        if certificate:
            break
    multiline("transvections examined", tried)
    print()

    if certificate:
        u, v, g, image = certificate
        print("CERTIFICATE: the transvection with u = %s" % (u[:4],))
        print("                               v = %s" % (v[:4],))
        print("  carries e~' to %s-w, is integral %s, an isometry %s, acts trivially on A_{T_En} %s"
              % ("+" if image == w else "-", is_integral(g), is_isometry(g), discriminant_trivial(g)))
        gk = mv(g, k)
        print("  and w . g(k) = %d with g(k) of square %d" % (dot(list(gk), w), dot(list(gk), list(gk))))
        assert dot(list(gk), w) == 0
        print()
        print("verdict: the class of w = 2e~ + e~' IS in the image of Phi.")
        print("  g lies in ker(rho_{T_En}) and g(k) lies in the orbit of k under the discriminant kernel, so w")
        print("  is orthogonal to an element of that orbit -- the criterion of sec-enriques-coble-correspondence.")
    else:
        print("verdict: undecided -- no transvection of small coefficients was found.")
        print("  The class reduction of the docstring does not depend on the bound.")


if __name__ == "__main__":
    main()
