"""research#658: the smallest deciding search for the witness class, with its bound stated.

Item 1f asks whether the class of w = 2e~ + e~' lies in the image of Phi, i.e. whether some element of
Gamma_En = ker(rho) cap O^+(T_En) carries k = e~ - f~ to a (-2)-vector orthogonal to w.  The (-2)-vectors
are one O(T_En)-orbit (AEGS25, printed p. 587, after Namikawa, Math. Ann. 270 (1985), Thm. 2.13), and the
elementary conjugates of k -- the transvections of
coble_658-stabilizer-image-probe.py, 28 of them realising k |-> delta = k + f~' -- all lie outside the
discriminant kernel.  So a conjugate inside the kernel, if one exists, is not elementary.

This probe is the smallest search that can decide the question positively: words in the reflections
s_r, r^2 = -2, which lie in O^+(T_En) and act trivially on A_{T_En}, hence generate a subgroup of
Gamma_En.  A word of length at most D whose image of k is orthogonal to w is a certificate: it is a
product of reflections, so it lies in Gamma_En, and it decides the witness IN THE IMAGE with no
group-theoretic input.  The search is breadth first on the orbit of k, writes down the word when it
finds one, verifies the certificate independently (integral, isometry, discriminant trivial, spinor
positive as a product of reflections, image of k orthogonal to w), and otherwise reports the depth and
width it reached.  It cannot refute the witness: a (-2)-orbit is infinite, and a bound proves nothing
about what lies beyond it.

Both outcomes are recorded: "certificate found" is a decision, and "not found within the bound" is the
state of the record and nothing more.

Usage: python3 computations/reports/coble_658-two-step-transporter-probe.py
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
DEPTH = 3
WIDTH = 150


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


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


GINV = inverse(G)


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(m):
    return is_integral(m) and matmul(transpose(m), matmul(G, m)) == G


def discriminant_trivial(m):
    mit = transpose(inverse(m))
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(mit, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def reflection(v):
    gv = mv(G, v)
    out = [[0] * N for _ in range(N)]
    for j in range(N):
        c = gv[j]                                  # (e_j, v), v^2 = -2
        out[j][j] = 1
        for i in range(N):
            out[i][j] = (1 if i == j else 0) + c * v[i]
    return out


def short_roots():
    """(-2)-vectors with U and U(2) coordinates bounded by 2 and E8(2) part 2*rho, rho an E8 root."""
    cartan = e8_cartan()
    e8_roots = []
    for x in product(range(-2, 3), repeat=8):
        q = sum(x[i] * cartan[i][j] * x[j] for i in range(8) for j in range(8))
        if q == 2:
            e8_roots.append(x)
    out = set()
    for a, b, c, d in product(range(-2, 3), repeat=4):
        for rho in [None] + e8_roots:
            v = [a, b, c, d] + ([2 * t for t in rho] if rho else [0] * 8)
            if dot(v, v) == -2:
                out.add(tuple(v))
    return sorted(out)


def main():
    k = [0] * N
    k[0], k[1] = 1, -1
    w = [0] * N
    w[0], w[2] = 2, 1
    delta = [0] * N
    delta[0], delta[1], delta[3] = 1, -1, 1

    roots = short_roots()
    print("T_En = U + U(2) + E8(2), rank %d" % N)
    print("(-2)-vectors enumerated: %d (U, U(2) coordinates in [-2,2], E8(2) part 2*rho)" % len(roots))
    print("search: words in reflections of length <= %d, orbit capped at %d" % (DEPTH, WIDTH))
    print()

    ident = [[int(i == j) for j in range(N)] for i in range(N)]
    refl = {r: reflection(list(r)) for r in roots}
    cols = {r: [tuple(refl[r][i][j] for i in range(N)) for j in range(N)] for r in roots}

    frontier = {tuple(k): ident}
    certificate = None
    for depth in range(1, DEPTH + 1):
        nxt = {}
        for point, word in frontier.items():
            for r in roots:
                R, C = refl[r], cols[r]
                image = tuple(sum(point[j] * C[j][i] for j in range(N)) for i in range(N))
                if image in nxt:
                    continue
                nxt[image] = matmul(R, word)
                if dot(list(image), w) == 0:
                    certificate = (r, depth, nxt[image], image)
                    break
            if certificate:
                break
        print("depth %d: orbit size %d" % (depth, len(nxt)))
        if certificate:
            break
        frontier = dict(list(nxt.items())[:WIDTH])
        if not frontier:
            break

    if certificate:
        r, depth, word, image = certificate
        print()
        print("CERTIFICATE FOUND at depth %d, last factor s_r for r = %s" % (depth, r[:4]))
        checks = {
            "integral": is_integral(word),
            "isometry": is_isometry(word),
            "discriminant trivial": discriminant_trivial(word),
            "image of k is orthogonal to w": dot(list(image), w) == 0,
            "image of k has square -2": dot(list(image), list(image)) == -2,
        }
        for name, value in checks.items():
            print("  %-32s %s" % (name, value))
        assert all(checks.values())
        print()
        print("verdict: the class of w = 2e~ + e~' IS in the image of Phi.")
        print("  The word is a product of reflections in (-2)-vectors, each of which lies in O^+(T_En) and")
        print("  acts trivially on A_{T_En}; so the word lies in Gamma_En and carries k to a (-2)-vector")
        print("  orthogonal to w, which is the criterion of sec-enriques-coble-correspondence.")
    else:
        print()
        print("verdict: undecided -- no certificate within depth %d and width %d." % (DEPTH, WIDTH))
        print("  A (-2)-orbit is infinite, so this bound proves nothing about what lies beyond it;")
        print("  raising the bound or passing to rho(Stab_{O(T_En)}(k)) is what would decide it.")


if __name__ == "__main__":
    main()
