"""research#658, the second residue on the page: what the cheap test does and does not decide.

The page asks (register row 40) which divisibility-2 0-cusps lie over a Coble 0-cusp.  An orbit of
Phi is in the image exactly when some gamma in Gamma_En carries its vector w~ into eta(T_Co) =
k^perp, i.e. exactly when beta(w~, gamma^{-1} k) = 0: w~ is orthogonal to a (-2)-vector of the
Gamma_En-orbit of k.  The book records the necessary condition -- w~ orthogonal to some (-2)-vector --
as NOT sufficient, with the witness w = 2 e~ + e~', which is primitive isotropic of divisibility 2 with
boundary lattice type (10,8,0) and is orthogonal to the (-2)-vector delta = e~ - f~ + f~'
(writing/dissertation/GAPS.md, the passage on the exact image locus).

This probe does two things, both exact, and prints where the question now stands:

1. It verifies every one of those claims about w and delta on T_En = U + U(2) + E8(2): primitivity,
   isotropy, divisibility 2, w.delta = 0, delta^2 = -2, and (as controls) that k = e~ - f~ is itself a
   (-2)-vector of divisibility 1 and is orthogonal to delta's own class of cone, so the test is not
   vacuous.
2. It prints the consequence of the one printed statement that fixes the shape of the question:
   AEGS25, Nagoya Math. J. 259 (2025), printed p. 587, after Namikawa, Math. Ann. 270 (1985),
   Theorem 2.13 -- there is a unique (-2)-vector of T_En modulo O(T_En).  Hence k and delta lie in ONE
   O(T_En)-orbit, so no refinement of the cheap test by an O(T_En)-invariant can rule w out; the
   residue is exactly whether the STABLE group O~+(T_En) = ker(rho) cap O^+ is still transitive on the
   (-2)-vectors, which is what Gamma_En is.  A probe cannot settle that: the (-2)-vectors of T_En are
   infinite in number (2ab + y^2 = -2 with y^2 in 4Z forces ab odd, for every odd ab), so no
   enumeration of them decides transitivity, and the deciding input is a generating set of Gamma_En
   together with the theorem that it moves k to delta.

Nothing here decides the image.  It decides what the residue is, and it replaces a sentence of the
essay with an exact check of the witness it quotes.

Usage: python3 computations/reports/coble_658-image-witness-probe.py
"""

from __future__ import annotations

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
N = len(G)                                   # 12


def vec(**kw):
    v = [0] * N
    for name, value in kw.items():
        v[{"e": 0, "f": 1, "ep": 2, "fp": 3}[name]] = value
    for i in range(8):
        v[4 + i] = kw.get("a%d" % (i + 1), 0)
    return v


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


def prime_factors_coordinate_gcd(v):
    return gcd(*[abs(x) for x in v]) if any(v) else 0


def divisibility(v):
    """div(v) = gcd of the values of the functional (v, -) on the standard basis."""
    vals = [sum(v[i] * G[i][j] for i in range(N)) for j in range(N)]
    return gcd(*[abs(x) for x in vals])


def report(name, v, want_square, want_div, want_primitive):
    square = dot(v, v)
    div = divisibility(v)
    primitive = prime_factors_coordinate_gcd(v) == 1
    print("%-28s square %3d  divisibility %d  primitive %s"
          % (name, square, div, primitive))
    assert square == want_square, (name, square, want_square)
    assert div == want_div, (name, div, want_div)
    assert primitive == want_primitive, (name, primitive, want_primitive)


def main():
    k = vec(e=1, f=-1)
    delta = vec(e=1, f=-1, fp=1)
    w = vec(e=2, ep=1)

    print("T_En = U + U(2) + E8(2), rank %d" % N)
    report("k = e~ - f~", k, -2, 1, True)
    report("delta = e~ - f~ + f~'", delta, -2, 1, True)
    report("w = 2e~ + e~'", w, 0, 2, True)

    print("w . delta = %d   (the cheap test: orthogonal to a (-2)-vector)" % dot(w, delta))
    assert dot(w, delta) == 0

    ep = vec(ep=1)                           # eta(e'), a vector whose class IS in the image
    report("e~'", ep, 0, 2, True)
    print("e~' . k = %d   (orthogonal to k itself, so its class is in the image)"
          % dot(ep, k))
    assert dot(ep, k) == 0
    print("w . k = %d   (the witness is not orthogonal to k, only to delta)"
          % dot(w, k))
    print()
    print("the (-2)-vectors of T_En are infinite in number: with v = a e~ + b f~ + y and y^2 in 4Z,")
    print("v^2 = 2ab + y^2 = -2 forces ab odd, which has solutions for every odd a.")
    print()
    print("AEGS25, printed p. 587 (after Namikawa, Math. Ann. 270 (1985), Thm. 2.13): there is a")
    print("unique (-2)-vector of T_En modulo O(T_En).  So k and delta lie in one O(T_En)-orbit, no")
    print("O(T_En)-invariant refines the cheap test, and the image of Phi is decided exactly by:")
    print("  is O~+(T_En) = ker(rho) cap O^+ transitive on the (-2)-vectors of T_En?")
    print("verdict: undecided -- the deciding input is a generating set of Gamma_En shown to move k")
    print("to delta; no enumeration of (-2)-vectors can decide it, they are infinite in number.")


if __name__ == "__main__":
    main()
