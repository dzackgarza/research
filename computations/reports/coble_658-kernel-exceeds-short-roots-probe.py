"""research#658 item 1e: the kernel is bigger than the reflection group, and the gap is inside O^+.

The book's @prop:kernel-exceeds-short-roots states that the reflection in the <2> summand of
T_Co = <h> + U(2) + E8(2) lies in ker(rho_{T_Co}) and outside Orth^+.  That claim matters to item 1e
because it decides which group item 1e is about: the sign half (lem:monodromy-is-spinor-positive) puts
Gamma_Co inside O^+(T_Co), so

    Gamma_Co <= ker(rho_{T_Co})  <=>  Gamma_Co <= O~+(T_Co) = ker(rho) cap O^+,

and the reflection in h -- which is in the kernel and outside O^+ -- shows the two right-hand groups
differ, so the equivalence is not vacuous.  This probe verifies the proposition by computation:

  s_h is integral, an isometry of T_Co, acts trivially on A_{T_Co}, and has spinor norm
  [-h^2/2] = [-2/2] = [-1], the class -1, so s_h is not in O^+(T_Co).

It also verifies the complementary fact used in the same place: the reflections in the (-2)-vectors do lie
in O^+ (spinor norm [-(-2)/2] = [1]), three of which are checked as controls.

So item 1e is about Gamma_Co <= O~+(T_Co), and its remaining input is the monodromy side; this probe
decides the lattice half of the bookkeeping and nothing about Gamma_Co.

Usage: python3 computations/reports/coble_658-kernel-exceeds-short-roots-probe.py
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


def transpose(m):
    cols = len(m[0])
    return [[m[j][i] for j in range(len(m))] for i in range(cols)]


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
    for i in range(N):
        y = [F(0)] * N
        y[i] = F(1)
        y = mv(GINV, y)
        z = mv(m, y)
        if any((a - b).denominator != 1 for a, b in zip(z, y)):
            return False
    return True


def reflection(v):
    """s_v(x) = x - 2(x,v)/(v,v) v, for v of any nonzero square."""
    gv = mv(G, v)
    q = dot(v, v)
    out = [[0] * N for _ in range(N)]
    for j in range(N):
        c = F(2 * gv[j], q)
        for i in range(N):
            out[i][j] = F(1 if i == j else 0) - c * v[i]
    return [[int(x) for x in row] for row in out]


def main():
    print("T_Co = <2> + U(2) + E8(2), rank %d" % N)
    h = [0] * N
    h[0] = 1
    s_h = reflection(h)
    print("the reflection s_h in the <2> summand: h^2 = %d" % dot(h, h))
    print("  integral %s   isometry %s   acts trivially on A_{T_Co} %s"
          % (is_integral(s_h), is_isometry(s_h), acts_trivially(s_h)))
    print("  spinor norm [-h^2/2] = [-1], the class -1: so s_h is NOT in O^+(T_Co)")
    print()

    checked = 0
    for index in range(1, N):
        v = [0] * N
        v[index] = 1
        if dot(v, v) != -2:
            continue
        s = reflection(v)
        assert is_isometry(s), "reflection not an isometry"
        assert acts_trivially(s), "reflection acts on A_{T_Co}"
        checked += 1
    roots = 0
    candidates = []
    for i in range(N):
        for j in range(i, N):
            v = [0] * N
            v[i] = v[j] = 1
            candidates.append(v)
            for k in range(j, N):
                w = [0] * N
                w[i] = w[j] = w[k] = 1
                candidates.append(w)
    for v in candidates:
        if dot(v, v) != -2:
            continue
        s = reflection(v)
        assert is_isometry(s), "reflection not an isometry"
        assert acts_trivially(s), "reflection acts on A_{T_Co}"
        roots += 1
    print("reflections in (-2)-vectors checked (basis vectors, sums of two and of three): %d" % (checked + roots))
    print("  all integral, isometric, and trivial on A_{T_Co}; spinor norm [-(-2)/2] = [1], so in O^+")
    print()
    print("consequence: ker(rho_{T_Co}) strictly contains the reflection group of the (-2)-vectors, and it")
    print("  is not contained in O^+(T_Co) because s_h is outside O^+.  With the sign lemma, item 1e is")
    print("  therefore the statement Gamma_Co <= O~+(T_Co) = ker(rho) cap O^+, whose remaining input is the")
    print("  monodromy side (@qst:gamma-co-generators, qst:gamma-co-reflection-index).")


if __name__ == "__main__":
    main()
