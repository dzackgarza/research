"""The census of the unpolarized chamber's simple roots at a labelled Coble cusp.

The unpolarized chamber of thm:unpolarized-coxeter lives in I_{1,8}(2) = Z H_0 + Z E_1 + ... + Z E_8
with H_0^2 = 2 and E_i^2 = -2 pairwise orthogonal, and its simple roots are
r_0 = H_0 - E_1 - E_2 - E_3 (square -4), r_i = E_i - E_{i+1} for 1 <= i <= 7 (square -4) and
r_8 = E_8 (square -2).

A labelled cusp has cusp lattice K = I_{1,8}(2) (thm:one-cusp-lattice) and group
Gamma_e = the image of Stab_{Gamma_{Co,2}}(eta) in Orth(K).  Since Gamma_{Co,2} = rho^{-1}(P) with
P = O(q_{U(2)}) x O(q_{E_8(2)}) acting on the U(2) and E_8(2) summands of
A_{T_Co} = A_<h> perp A_{U(2)} perp A_{E_8(2)} and trivially on A_<h>, the reflection s_r lies in
Gamma_e only if its action on A_K preserves the decomposition A_K = A_<h> perp A_{E_8(2)}; and,
because every lift of s_r has the same action on A_K (the lifts differ by ker(Orth(T_Co) ->
Orth(K)), which acts trivially there), that condition is also sufficient for the roots below.

This script checks, in the orthogonal model of K, for each simple root:
  (1) the square and the integrality of the reflection s_r(x) = x - 2(x,r)/(r,r) r on a basis;
  (2) the class of r/2 in A_K and the summand it is supported in;
  (3) the number of the 512 classes of A_K that the action of s_r moves across the decomposition.
A root moves none across exactly when its class is supported in one summand, and that is the
criterion for lying in P.  No provider call: the model and its discriminant form are written here.
"""
from fractions import Fraction as F
from itertools import product

K = [[2 if i == 0 and j == 0 else (-2 if i == j else 0) for j in range(9)] for i in range(9)]


def bil(x, y):
    return sum(K[i][j] * x[i] * y[j] for i in range(9) for j in range(9))


def refl(x, r):
    c = bil(x, r)
    q = bil(r, r)
    return [x[i] - F(2 * c, q) * r[i] for i in range(9)]


def cls(x):
    return tuple(F(v) % 1 for v in x)


def roots():
    out = {"r_0": [1, -1, -1, -1, 0, 0, 0, 0, 0]}
    for i in range(1, 8):
        v = [0] * 9
        v[i] = 1
        v[i + 1] = -1
        out[f"r_{i}"] = v
    out["r_8"] = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    return out


def main():
    print("K = I_{1,8}(2) = <2>_H0 + <-2>_{E_1..E_8}, orthogonal basis; rank 9, det 512")
    basis = [[1 if i == j else 0 for j in range(9)] for i in range(9)]
    print()
    print(f"{'root':6} {'square':>6}  {'support of [r/2]':>17}  {'integral':>8}  {'moved across':>12}  verdict")
    census = {}
    for name, r in roots().items():
        q = bil(r, r)
        integral = all(all(v.denominator == 1 for v in refl(b, r)) for b in basis)
        if q == -4:
            cl = cls([F(c, 2) for c in r])
        else:
            cl = cls([F(c) for c in r])
        if cl[0] != 0 and any(cl[i] != 0 for i in range(1, 9)):
            support = "mixed"
        elif cl[0] != 0:
            support = "A_<h>"
        else:
            support = "A_{E_8(2)}"
        across = 0
        for eps in product((0, 1), repeat=9):
            z = cls([F(e, 2) for e in eps])
            w = cls(refl([F(e, 2) for e in eps], r))
            if (z[0] == 0) != (w[0] == 0):
                across += 1
        verdict = "in Gamma_e" if across == 0 else "OUT"
        census[name] = verdict
        print(f"{name:6} {q:6}  {support:>17}  {str(integral):>8}  {across:>12}  {verdict}")
    print()
    print("witness for r_0: [E_3/2] = (0,0,0,1/2,0,0,0,0,0) -> (1/2,1/2,1/2,0,0,0,0,0,0),")
    print("which has a nonzero A_<h> component; for r_1..r_7 the class of r/2 is supported in")
    print("A_{E_8(2)} alone, so their reflections preserve the decomposition, and r_8 has square -2")
    print("and acts trivially on A_K.")
    print()
    out = [n for n, v in census.items() if v != "in Gamma_e"]
    print("outside Gamma_e among the simple roots:", out)
    print("inside Gamma_e among the simple roots:", [n for n, v in census.items() if v == "in Gamma_e"])
    print()
    print("So the labelled cusp's chamber contains the union of the two unpolarized chambers that meet")
    print("along r_0^perp, and r_0^perp is not a labelled wall: the counted simple system of")
    print("thm:unpolarized-coxeter loses exactly the node r_0 at a labelled cusp.")


if __name__ == "__main__":
    main()
