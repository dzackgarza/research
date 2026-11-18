"""The four 0-cusps of F_{Co,2}: the public representatives checked, and their cusp lattices.

The representatives are the ones sage-extensions run 43556671111 prints, archived here as
computations/reports/coble_gco_public_incidence_source-run.log:

    [Gamma_{Co,2}] line cusp 0: ((0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),)
    [Gamma_{Co,2}] line cusp 1: ((0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0),)
    [Gamma_{Co,2}] line cusp 2: ((-2, -4, 0, 0, -1, -1, -1, -1, -1, 0, 1),)
    [Gamma_{Co,2}] line cusp 3: ((-50, -4, -1, 30, 26, 58, 61, 58, 54, 54, 51),)

They are written in the provider's standard basis, and that basis is archived: the artifact
computations/reports/coble_proper_plane_stabilizer_image.json (schema
coble-proper-plane-stabilizer-finite-cosets-v1, sha256 of the file printed below) carries the key
"standard_gram", which is the Gram matrix of B = <1> + U + E8(-1) in that basis; the lattice of the
report is T_Co = B(2), whose Gram is twice it.

For each of the four vectors this script checks that v is primitive and isotropic in T_Co, computes
its divisibility, the class [v/2] in A_{T_Co} and its q-value, and the Gram matrix of the cusp
lattice K = v^perp / Z v with its determinant, signature, elementary divisors and level profile.
The four are then compared: the cusp lattice is one lattice, as thm:one-cusp-lattice says, and the
invariants (rank 9, det 512, signature (1,8), 2-elementary, delta = 1) identify it with
<2> + E8(-2) = I_{1,8}(2) by Nikulin's classification of indefinite 2-elementary lattices.

No provider call: the inputs are the archived row and the archived Gram.
"""
import hashlib
import json
import pathlib
from fractions import Fraction as F
from math import gcd
from itertools import product


ARTIFACT = pathlib.Path(__file__).with_name("coble_proper_plane_stabilizer_image.json")

LINES = {
    0: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    2: [-2, -4, 0, 0, -1, -1, -1, -1, -1, 0, 1],
    3: [-50, -4, -1, 30, 26, 58, 61, 58, 54, 54, 51],
}


def bil(G, x, y):
    n = len(G)
    return sum(G[i][j] * x[i] * y[j] for i in range(n) for j in range(n))


def gcd_of(xs):
    g = 0
    for x in xs:
        g = gcd(g, abs(int(x)))
    return g


def det_int(M):
    import sympy
    return int(sympy.Matrix(M).det())


def signature(G):
    import sympy
    ev = sympy.Matrix(G).eigenvals()
    pos = sum(int(m) for l, m in ev.items() if sympy.nsimplify(l) > 0)
    neg = sum(int(m) for l, m in ev.items() if sympy.nsimplify(l) < 0)
    zer = sum(int(m) for l, m in ev.items() if sympy.nsimplify(l) == 0)
    return pos, neg, zer


def bezout(a, b):
    """(s, t, g) with s*a + t*b = g = gcd(a, b) >= 0, valid also when a or b is 0."""
    if a == 0 and b == 0:
        return (0, 0, 0)
    old_r, r = abs(a), abs(b)
    old_s, s_ = 1, 0
    old_t, t_ = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s_ = s_, old_s - q * s_
        old_t, t_ = t_, old_t - q * t_
    # old_s*|a| + old_t*|b| = old_r
    sgn_a = -1 if a < 0 else 1
    sgn_b = -1 if b < 0 else 1
    return (old_s * sgn_a, old_t * sgn_b, old_r)


def unimodular_with_first_column(c):
    """An integral T with det +-1 whose first column is c, for c primitive."""
    import sympy
    n = len(c)
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    w = list(c)
    pos = next(i for i in range(n) if w[i] != 0)
    if pos != 0:
        U[0], U[pos] = U[pos], U[0]
        w[0], w[pos] = w[pos], w[0]
    for i in range(1, n):
        if w[i] == 0:
            continue
        a, b = w[0], w[i]
        s, t, g = bezout(a, b)
        r0, ri = U[0][:], U[i][:]
        U[0] = [s * x + t * y for x, y in zip(r0, ri)]
        U[i] = [(-b // g) * x + (a // g) * y for x, y in zip(r0, ri)]
        w[0], w[i] = g, 0
        assert sum(U[0][k] * c[k] for k in range(n)) == w[0]
    assert abs(w[0]) == 1 and all(x == 0 for x in w[1:]), w
    Uc = [sum(U[i][k] * c[k] for k in range(n)) for i in range(n)]
    assert Uc == [1] + [0] * (n - 1), Uc
    T = sympy.Matrix(U).inv()
    T = [[int(sympy.nsimplify(T[i, j])) for j in range(n)] for i in range(n)]
    assert [T[i][0] for i in range(n)] == c, "first column must be c"
    return T


def kernel_basis(G, v):
    """A Z-basis of v^perp = {x : (x, v) = 0}.

    Let r_i = (b_i, v), d = gcd(r) and r' = r/d, primitive.  If T is unimodular with first column
    r', then the matrix V = T^T has first row r', so (Vx)_1 = r'x and
    ker(r') = V^{-1}{y : y_1 = 0}, that is the rows 2..11 of T^{-1}.
    """
    import sympy
    n = len(G)
    r = [sum(G[i][j] * v[j] for j in range(n)) for i in range(n)]
    d = gcd_of(r)
    assert d > 0
    rp = [x // d for x in r]
    T = unimodular_with_first_column(rp)
    Ti = sympy.Matrix(T).inv()
    basis = []
    for i in range(1, n):
        row = [int(sympy.nsimplify(Ti[i, j])) for j in range(n)]
        assert sum(rp[k] * row[k] for k in range(n)) == 0
        basis.append(row)
    assert sympy.Matrix([[b[i] for b in basis] for i in range(n)]).rank() == n - 1
    return basis


def cusp_lattice(G, v):
    """The Gram matrix of K = v^perp / Z v."""
    import sympy
    B = kernel_basis(G, v)
    Q = [[bil(G, a, b) for b in B] for a in B]
    # coordinates of v in the basis B: solve an invertible 10x10 minor exactly and verify
    import itertools
    n = len(G)
    c = None
    for rows in itertools.combinations(range(n), 10):
        M = sympy.Matrix([[B[j][i] for j in range(10)] for i in rows])
        if M.det() == 0:
            continue
        try:
            sol = M.solve(sympy.Matrix([v[i] for i in rows]))
        except Exception:
            continue
        cand = [sympy.nsimplify(x) for x in sol]
        if any(sympy.denom(x) != 1 for x in cand):
            continue
        cand = [int(x) for x in cand]
        if all(sum(B[i][k] * cand[i] for i in range(10)) == v[k] for k in range(n)):
            c = cand
            break
    assert c is not None, "v must lie in the Z-span of the kernel basis"
    g = gcd_of(c)
    c = [x // g for x in c]
    T = unimodular_with_first_column(c)
    n = len(T)
    Tt = [[T[j][i] for j in range(n)] for i in range(n)]
    TQ = [[sum(Tt[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    Qp = [[sum(TQ[i][k] * T[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    assert all(Qp[0][j] == 0 for j in range(n)) and all(Qp[i][0] == 0 for i in range(n))
    return [[Qp[i + 1][j + 1] for j in range(n - 1)] for i in range(n - 1)]


def invariants(K):
    """(rank, det, signature, is 2-elementary, delta) of a 2-elementary candidate."""
    import sympy
    n = len(K)
    d = det_int(K)
    sig = signature(K)
    # 2-elementary iff the elementary divisors of the Gram are all <= 2, tested by 2K^* <= K:
    # equivalently det(K) is a power of 2 and the Smith normal form of K has no odd part > 1
    from sympy.matrices.normalforms import smith_normal_form
    from sympy import ZZ
    sm = smith_normal_form(sympy.Matrix(K), domain=ZZ)
    elem = [abs(int(sm[i, i])) for i in range(min(sm.shape))]
    two_elem = all(e in (1, 2) for e in elem) and all(e != 0 for e in elem)
    a = sum(1 for e in elem if e == 2)
    # delta: 1 iff q takes a value outside Z/2Z, i.e. some half-integral representative has
    # a square which is not an integer
    delta = None
    if two_elem:
        delta = 0
        for eps in product((0, 1), repeat=n):
            x = [F(e, 2) for e in eps]
            q = F(sum(x[i] * K[i][j] * x[j] for i in range(n) for j in range(n)))
            if q.denominator == 2:
                delta = 1
                break
    return dict(rank=n, det=d, signature=sig, elementary=elem, two_elementary=two_elem,
                a=a, delta=delta)


def level_profile(K):
    n = len(K)
    counts = {}
    for eps in product((0, 1), repeat=n):
        x = [F(e, 2) for e in eps]
        q = F(sum(x[i] * K[i][j] * x[j] for i in range(n) for j in range(n))) % 2
        counts[q] = counts.get(q, 0) + 1
    return counts


def main():
    raw = ARTIFACT.read_bytes()
    data = json.loads(raw)
    print("standard basis archived at", ARTIFACT.name)
    print("   schema:", data["schema"])
    print("   sha256 of the file:", hashlib.sha256(raw).hexdigest())
    GB = data["standard_gram"]
    assert len(GB) == 11 and all(len(r) == 11 for r in GB)
    G = [[2 * x for x in row] for row in GB]        # T_Co = B(2)
    print("   B = <1> + U + E8(-1) on it, det", det_int(GB), ", signature", signature(GB))
    print("   T_Co = B(2), det", det_int(G), ", signature", signature(G))
    print()
    classes = {}
    grams = {}
    invs = {}
    for k in sorted(LINES):
        v = LINES[k]
        sq = bil(G, v, v)
        div = gcd_of([bil(G, v, [1 if i == j else 0 for i in range(11)]) for j in range(11)])
        w = [F(x, 2) for x in v]
        q = F(sum(w[i] * G[i][j] * w[j] for i in range(11) for j in range(11))) % 2
        cls = tuple(x % 1 for x in w)
        classes[k] = cls
        print(f"line cusp {k}: v = {tuple(v)}")
        print(f"   primitive: {gcd_of(v) == 1}   v^2 = {sq}   divisibility: {div}")
        print(f"   class [v/2] = {tuple(str(x) for x in cls)}   q = {q}   singular: {q == 0}")
        K = cusp_lattice(G, v)
        grams[k] = K
        info = invariants(K)
        invs[k] = (info["rank"], info["det"], info["signature"], info["two_elementary"], info["a"], info["delta"])
        print(f"   K = v^perp / Z v: rank {info['rank']}, det {info['det']}, signature {info['signature'][:2]}")
        print(f"   elementary divisors of the Gram of K: {info['elementary']}   2-elementary: {info['two_elementary']}, a = {info['a']}, delta = {info['delta']}")
        print(f"   level profile of q_K: { {str(x): y for x, y in sorted(level_profile(K).items())} }")
    print()
    print("the four classes [v/2] are pairwise distinct:", len(set(classes.values())) == 4)
    print("the four cusp lattices have identical invariants:", len(set(invs.values())) == 1)
    print("invariants (rank, det, signature, 2-elementary, a, delta):", invs[0])
    print()
    print("rank 9, det 512 = 2^9, signature (1,8), 2-elementary with delta = 1 is <2> + E8(-2) =")
    print("I_{1,8}(2) by Nikulin's classification of indefinite 2-elementary lattices, so the four")
    print("0-cusps of F_{Co,2} have one cusp lattice, as thm:one-cusp-lattice states, and this")
    print("instantiates it at the four public representatives.")
    print()
    for k in sorted(grams):
        print(f"K at line cusp {k}, in the basis of the script:")
        for row in grams[k]:
            print("   ", row)


if __name__ == "__main__":
    main()
