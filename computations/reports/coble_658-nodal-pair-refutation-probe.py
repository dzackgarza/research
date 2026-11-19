"""research#658 item 1e refuted: the nodal-pair monodromy IS a reflection in a (-4)-class of T_Co.

Item 1e asks whether Gamma_Co <= ker(rho_{T_Co}), the discriminant kernel, for the monodromy group of
the family of unpolarized Coble surfaces (@def:gamma-co-groups(1)).  The record of the one-node
construction, computations/reports/smwo_direct-period.md (Theorem E), states:

  item 1: "the deck group equal to the monodromy image G1 on T_Co";
  item 3: "G1 contains W_node = <w_delta, (w_s, w_e)>: the Picard--Lefschetz reflections w_delta,
           delta in T_Co, delta^2 = -2, ... and the nodal-pair transformations with s = delta + delta',
           e = delta - delta', s^2 = e^2 = -4";
  and, at the same section: "the nodal-pair products, which act on T_Co as the reflection in a class e
           of square -4".

The parenthesised (w_s, w_e) is not a pair of monodromy elements.  It is the block decomposition of the
single element w_delta w_delta': w_delta alone does not preserve the summands S_Co, T_Co (for t in T_Co,
w_delta(t) = t + (t.e)/2 (delta_+ + delta_-) has a component in S_Co, where delta = delta_+ + delta_-
with delta_+- in S_Co and delta_- in T_Co), while the product of the two commuting reflections does, and
acts on T_Co as the reflection in e.  This probe verifies that identity from scratch:

  (i)   in Lambda = <s> + T_Co with s^2 = -4, s orthogonal to T_Co, put delta = (s+e)/2 and
        delta' = (s-e)/2; then delta^2 = delta'^2 = -2 and delta.delta' = 0, and w_delta w_delta'
        acts on T_Co exactly as the reflection w_e in the (-4)-class e;
  (ii)  w_e is an integral isometry of T_Co (T_Co is 2Z-valued and e^2 = -4);
  (iii) w_e lies in O^+(T_Co) -- spinor norm [-e^2/2] = [2] = [1] in R^*/(R^*)^2 -- and NOT in
        ker rho_{T_Co}: w_e(y) - y = -(y.e) e/2, the class [e/2] is nonzero in A_{T_Co} (it has
        q = -1, so it is not in 2T_Co), and some y in T_Co^* has (y.e) odd.

The general lemma behind (iii), for every e in T_Co with e^2 = -4: T_Co is 2Z-valued, so w_e is
integral; if in addition rho(w_e) = id then (y.e) is even for every y in T_Co^*, that is e/2 lies in
(T_Co^*)^* = T_Co, that is e = 2f with f^2 = -1 -- impossible because T_Co is even.  So every (-4)
class of T_Co gives a reflection in O^+(T_Co) outside the discriminant kernel.  This is
@prop:gamma-co-reflective-set(3) at the level of the lattice.

The geometric input is the record's: the local monodromy of the nodal-pair degeneration is the product
of the two commuting Picard--Lefschetz reflections w_delta w_delta', and it is an element of the
monodromy of a family of Coble surfaces, hence of Gamma_Co.  Therefore Gamma_Co is not contained in
ker rho_{T_Co}: item 1e is FALSE, and by @prop:gamma-co-strong-lifting -- (1) <=> (2) -- the
Gamma_Co form of @thm:coble-strong-lifting fails with it, and the forward half
Gamma_Co <= O~^+(T_Co) of @conj:gamma-co-stable is false.

Usage: python3 computations/reports/coble_658-nodal-pair-refutation-probe.py
"""

from __future__ import annotations

from fractions import Fraction as F


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


def transpose(m):
    cols = len(m[0])
    return [[m[j][i] for j in range(len(m))] for i in range(cols)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def acts_trivially(m):
    mit = transpose(inverse(m))
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(mit, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def reflection_integral(v):
    """s_v is integral iff 2(v,e_j)/(v,v) is an integer for all j; returns the matrix when it is."""
    q = dot(v, v)
    gv = mv(G, v)
    coeffs = [F(2 * gv[j], q) for j in range(N)]
    if any(c.denominator != 1 for c in coeffs):
        return False, None
    out = [[F(1 if i == j else 0) - coeffs[j] * v[i] for j in range(N)] for i in range(N)]
    assert all(x.denominator == 1 for row in out for x in row)
    return True, [[int(x) for x in row] for row in out]


# --- Lambda = <s> + T_Co, rank 12: the model in which delta and delta' live ------------------

GL = block_diagonal([[[-4]], G])
NL = len(GL)


def reflection_map_lambda(v):
    """The rational reflection R_v(x) = x - 2(x.v)/(v.v) v on Lambda (x) Q, as an NL x NL matrix."""
    q = sum(F(v[i]) * GL[i][j] * F(v[j]) for i in range(NL) for j in range(NL))
    assert q != 0
    gv = [sum(GL[i][j] * F(v[j]) for j in range(NL)) for i in range(NL)]
    return [[F(int(i == j)) - 2 * F(v[i]) * gv[j] / q for j in range(NL)] for i in range(NL)]


def main():
    e = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]        # a root of the E8(2) summand: e^2 = -4, primitive
    print("T_Co = <2> + U(2) + E8(2), rank %d" % N)
    print("e = a_1 is the first E8(2) coordinate: e^2 = %d, primitive %s"
          % (dot(e, e), e[3] % 2 != 0))

    # (i) the block identity of the record
    s_lam = [F(1)] + [F(0)] * N
    e_lam = [F(0)] + [F(x) for x in e]
    delta = [(a + b) / 2 for a, b in zip(s_lam, e_lam)]
    delta_p = [(a - b) / 2 for a, b in zip(s_lam, e_lam)]

    def sq(v):
        return sum(v[i] * GL[i][j] * v[j] for i in range(NL) for j in range(NL))

    def pair(v, w):
        return sum(v[i] * GL[i][j] * w[j] for i in range(NL) for j in range(NL))

    print()
    print("Lambda = <s> + T_Co, s^2 = -4; delta = (s+e)/2, delta' = (s-e)/2:")
    print("  delta^2 = %s   delta'^2 = %s   delta.delta' = %s"
          % (sq(delta), sq(delta_p), pair(delta, delta_p)))
    assert sq(delta) == -2 and sq(delta_p) == -2 and pair(delta, delta_p) == 0

    W_d = reflection_map_lambda(delta)
    W_dp = reflection_map_lambda(delta_p)
    prod = matmul(W_d, W_dp)
    W_e = reflection_map_lambda(e_lam)
    print("  the product w_delta w_delta' preserves <s> and T_Co: %s"
          % all(prod[0][j] == 0 for j in range(1, NL)))
    assert all(prod[0][j] == 0 for j in range(1, NL))
    same = all(prod[i][j] == W_e[i][j] for i in range(1, NL) for j in range(1, NL))
    print("  w_delta w_delta' acts on T_Co exactly as the reflection w_e in the (-4)-class e: %s" % same)
    assert same

    ok_e, We = reflection_integral(e)
    print()
    print("(ii) the reflection w_e is integral on T_Co: %s" % ok_e)
    assert ok_e

    # (iii) w_e is in O^+ and not in the discriminant kernel
    print("(iii) spinor norm of w_e is [-e^2/2] = [%d], and [%d] = [1] in R^*/(R^*)^2: True"
          % (-dot(e, e) // 2, -dot(e, e) // 2))
    print("  w_e acts trivially on A_{T_Co}: %s" % acts_trivially(We))
    assert not acts_trivially(We)

    # T_Co^* is {G^{-1}v : v in Z^11}, and then (y, e) = v . e
    ge = mv(G, e)
    print("  e/2 lies in T_Co^* (G e is even): %s" % all(x % 2 == 0 for x in ge))
    print("  e/2 lies in T_Co: %s   (so the class [e/2] of A_{T_Co} is nonzero)"
          % all(F(x, 2).denominator == 1 for x in e))
    assert all(x % 2 == 0 for x in ge)
    assert not all(F(x, 2).denominator == 1 for x in e)
    witness = None
    for i in range(N):
        v = [0] * N
        v[i] = 1
        val = sum(v[j] * e[j] for j in range(N))
        if val % 2 == 1:
            witness = (i, val)
            break
    assert witness is not None
    print("  a class y = G^{-1}v of T_Co^* with y.e odd: v the basis vector %d, y.e = %d" % witness)
    print("  hence w_e(y) - y = -(y.e) e/2 is not in T_Co, and rho_{T_Co}(w_e) is not the identity.")

    print()
    print("verdict: item 1e is FALSE.  The nodal-pair monodromy w_delta w_delta' acts on T_Co as the")
    print("  reflection in the (-4)-class e; w_e is integral, lies in O^+(T_Co), and does not lie in")
    print("  ker rho_{T_Co}.  Gamma_Co therefore contains an element outside the discriminant kernel,")
    print("  the inclusion Gamma_Co <= O~^+(T_Co) is false, and with it the Gamma_Co form of the")
    print("  strong lifting (@prop:gamma-co-strong-lifting) and the forward half of")
    print("  @conj:gamma-co-stable.  The page's @prop:gamma-co-reflective-set(3) already proves the")
    print("  lattice half; what the record supplies is that the monodromy realises such a reflection.")


if __name__ == "__main__":
    main()
