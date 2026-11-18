"""Whether the public orbit row's four line-cusp vectors are readable in the corpus's basis (research#671).

sage-extensions run 43556671111 prints the four 0-cusps of F_{Co,2} as

    [Gamma_{Co,2}] line cusp 0: ((0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),)
    [Gamma_{Co,2}] line cusp 1: ((0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0),)
    [Gamma_{Co,2}] line cusp 2: ((-2, -4, 0, 0, -1, -1, -1, -1, -1, 0, 1),)
    [Gamma_{Co,2}] line cusp 3: ((-50, -4, -1, 30, 26, 58, 61, 58, 54, 54, 51),)

(archived as computations/reports/coble_gco_public_incidence_source-run.log).  The question this
script answers is whether those 11-tuples are coordinates in the basis the corpus states for
T_Co, so that a page can use them:  T_Co = <2>_{H} + U(2)_{(e,f)} + E8(-2)  with
G = diag(2) + [[0,2],[2,0]] + (-2)*Cartan(E8), the model of computations/reports/
coble_cusp-stabilizer-orthogonal.py  Part A and of prop:tco-as-twist's B(2).

Answer: no.  In that Gram the four vectors have squares 0, 0, -4 and -3336, so two of the four are
not isotropic and none of them can be a primitive isotropic vector of T_Co in that basis.  The
discrepancy is not a permutation of the three summands either: the script tests all six orders of
<2>, U(2), E8(-2) and all six of <2>, U(2), E8(+2), and in none of the twelve is every one of the
four vectors isotropic.

So the coordinate data of the public row are expressed in the provider's own basis of its Tco
object, and that basis, equivalently the Gram matrix of that object, is not archived anywhere in
this repository.  Until it is, the four representatives cannot be checked or used on a page, and
the cusp lattices at the four labelled cusps cannot be computed from the public row.
"""
from fractions import Fraction as F
from math import gcd
from itertools import permutations

E8_EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]
LINES = {
    0: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    2: [-2, -4, 0, 0, -1, -1, -1, -1, -1, 0, 1],
    3: [-50, -4, -1, 30, 26, 58, 61, 58, 54, 54, 51],
}


def cartan():
    C = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
    for a, b in E8_EDGES:
        C[a][b] = C[b][a] = -1
    return C


def direct_sum(blocks):
    n = sum(len(b) for b in blocks)
    M = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                M[off + i][off + j] = b[i][j]
        off += len(b)
    return M


def bil(G, x, y):
    return sum(G[i][j] * x[i] * y[j] for i in range(len(G)) for j in range(len(G)))


def gcd_of(xs):
    g = 0
    for x in xs:
        g = gcd(g, abs(int(x)))
    return g


def main():
    C = cartan()
    H2 = [[2]]
    U2 = [[0, 2], [2, 0]]
    E8neg = [[-2 * x for x in r] for r in C]
    E8pos = [[2 * x for x in r] for r in C]
    G = direct_sum([H2, U2, E8neg])
    import sympy
    ev = sympy.Matrix(G).eigenvals()
    pos = sum(int(m) for l, m in ev.items() if sympy.nsimplify(l) > 0)
    neg = sum(int(m) for l, m in ev.items() if sympy.nsimplify(l) < 0)
    print("T_Co Gram: <2> + U(2) + E8(-2), rank 11, det", int(sympy.Matrix(G).det()),
          " signature", (pos, neg, 0))
    print()
    print("the four public line-cusp vectors in that basis:")
    for k in sorted(LINES):
        v = LINES[k]
        sq = bil(G, v, v)
        div = gcd_of([bil(G, v, [1 if i == j else 0 for i in range(11)]) for j in range(11)])
        print(f"  line cusp {k}: v = {tuple(v)}")
        print(f"     primitive: {gcd_of(v) == 1}   v^2 = {sq}   isotropic: {sq == 0}   divisibility: {div}")
    print()
    print("so the coordinates of the public row are NOT in this basis.")
    print()
    print("testing permutations of the summands, to see whether the difference is only an ordering:")
    for name, blockset in (("E8(-2)", ["H", "U", "E8neg"]), ("E8(+2)", ["H", "U", "E8pos"])):
        pool = {"H": H2, "U": U2, "E8neg": E8neg, "E8pos": E8pos}
        for order in permutations(blockset):
            Gm = direct_sum([pool[b] for b in order])
            vals = [bil(Gm, v, v) for v in LINES.values()]
            ok = all(x == 0 for x in vals)
            print(f"  {name}, order {order}: v^2 = {vals}   all isotropic: {ok}")
    print()
    print("no ordering in either sign convention makes all four vectors isotropic, so the public row")
    print("is in the provider's own basis of its Tco object.")
    print("The datum that is missing, and that would make the row usable, is the Gram matrix of that")
    print("object, equivalently the basis change from it to <2> + U(2) + E8(-2); it is not archived")
    print("in this repository.")


if __name__ == "__main__":
    main()
