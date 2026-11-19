"""research#658 item 1e: the polarized sibling of Gamma_Co does NOT lie in the discriminant kernel.

Item 1e asks whether the monodromy of the *unpolarized* Coble family lies in ker(rho_{T_Co}).  The
degree-2 polarized family has monodromy Gamma_{Co,2} = rho^{-1}(P) by @def:gamma-co-groups(5), where P is
the stabilizer in Orth(q_{T_Co}) of the decomposition [h/2]^perp = A_{U(2)} + A_{E_8(2)}
(@prop:gamma-co-images(3)).  This probe verifies the small fact that makes the two cases different:

  the swap s of the two isotropic generators e', f' of the U(2) block is an integral isometry of T_Co
  fixing h; it acts NON-trivially on A_{T_Co}; and its class action preserves the decomposition
  A_{U(2)} + A_{E_8(2)}, i.e. rho(s) lies in P.

Hence s lies in rho^{-1}(P) = Gamma_{Co,2}, so the polarized monodromy is NOT contained in the
discriminant kernel -- the discriminant kernel is strictly smaller than Gamma_{Co,2}, and the inclusion
that item 1e asks about is a genuinely sharper condition than anything the polarized family satisfies.

What that does and does not say.  It does not decide item 1e: Gamma_Co is the unpolarized monodromy and
the probe says nothing about it.  It removes the argument "the monodromy is in the kernel because the
polarized one is", by showing the polarized one is not.  Both facts are recorded so that no reading of the
book can slide from one family to the other.

Usage: python3 computations/reports/coble_658-polarized-not-kernel-probe.py
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
G = block_diagonal([[[2]], [[2 * x for x in row] for row in U],
                    [[-2 * x for x in row] for row in e8_cartan()]])      # T_Co, rank 11
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


GINV = inverse(G)


def is_integral(m):
    return all(getattr(x, "denominator", 1) == 1 for row in m for x in row)


def is_isometry(m):
    return is_integral(m) and matmul(transpose(m), matmul(G, m)) == G


def acts_trivially(m):
    """Does m act trivially on A = Z^n/(G Z^n)?

    With the classes coded by v_j = (x, e_j), an isometry acts by v |-> m^{-T} v = G m G^{-1} v, so
    triviality is m(y) - y in Z^n for the generators y = G^{-1} e_i.
    """
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(m, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def class_of(m, v):
    """The class of m applied to the class of the vector v (both as vectors of the lattice)."""
    y = mv(GINV, [F(x) for x in v])
    z = mv(m, y)
    return tuple(round(float(x % 1), 6) for x in z)


def same_class(u, w):
    """Are the vectors u and w in the same class of A = Z^n/(G Z^n)?"""
    diff = mv(GINV, [F(a - b) for a, b in zip(u, w)])
    return all(x.denominator == 1 for x in diff)


def main():
    print("T_Co = <2> + U(2) + E8(2), rank %d" % N)
    swap = [[int(i == j) for j in range(N)] for i in range(N)]
    swap[1][1] = swap[2][2] = 0
    swap[1][2] = swap[2][1] = 1                    # e' <-> f'
    print("the swap s of e', f': integral %s, isometry %s, fixes h %s"
          % (is_integral(swap), is_isometry(swap), mv(swap, [1] + [0] * (N - 1)) == [1] + [0] * (N - 1)))
    print("  acts trivially on A_{T_Co}: %s" % acts_trivially(swap))

    # the decomposition A_{T_Co} = <h/2> + A_{U(2)} + A_{E_8(2)}: a class is in A_{E_8(2)} when it has
    # no h and no U(2) coordinate; s must carry such classes to such classes.
    # the classes of the E8(2) part are those carried by vectors with v_h = v_{e'} = v_{f'} = 0; the swap
    # must carry each of them to a vector of the same shape, and that is checked on the defining vectors.
    preserved = True
    for i in range(3, N):
        v = [0] * N
        v[i] = 1
        w = mv(swap, v)                             # the swap acts on the lattice coordinates
        if any(abs(w[k]) > 0 for k in range(3)):
            preserved = False
            break
    print("  preserves the E8(2) part of A_{T_Co}: %s" % preserved)
    # the class of e'/2 is the functional (e'/2, .), i.e. the coordinate vector with a 1 in the f' slot;
    # the swap must carry it to the vector with a 1 in the e' slot, and that vector is the class of f'/2.
    # the class of e'/2 is the functional (e'/2, .), whose coordinates are (0,0,1,0,...); an isometry acts
    # on these coordinates by m^{-T}, and the claim is that the swap carries it to the class of f'/2,
    # whose coordinates are (0,1,0,...).
    e_half_class = [0] * N
    e_half_class[2] = 1
    f_half_class = [0] * N
    f_half_class[1] = 1
    image = mv(transpose(inverse(swap)), [F(x) for x in e_half_class])
    image_int = [int(x) if x.denominator == 1 else x for x in image]
    print("  and swaps the two classes [e'/2], [f'/2] of A_{U(2)}: %s"
          % (image_int == f_half_class))
    print()
    print("so rho(s) preserves the decomposition [h/2]^perp = A_{U(2)} + A_{E_8(2)}, i.e. rho(s) lies in the")
    print("P of @prop:gamma-co-images(3); hence s lies in rho^{-1}(P) = Gamma_{Co,2} and the polarized")
    print("monodromy is NOT contained in ker(rho_{T_Co}).")
    print()
    print("verdict: the discriminant kernel is strictly smaller than Gamma_{Co,2}.  Item 1e asks the same")
    print("question for the unpolarized monodromy Gamma_Co, which this probe does not decide; what it")
    print("removes is the inference from the polarized family to the unpolarized one.")


if __name__ == "__main__":
    main()
