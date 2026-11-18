"""The (-4)-root H_0 - E_1 - E_2 - E_3 of the unpolarized Coble chamber is not a wall at a labelled cusp.

The unpolarized chamber of thm:unpolarized-coxeter lives in I_{1,8}(2) = Z H_0 + Z E_1 + ... + Z E_8
with H_0^2 = 2 and E_i^2 = -2 pairwise orthogonal, and its simple roots include
r_0 = H_0 - E_1 - E_2 - E_3, of square -4.

A labelled cusp has cusp lattice K = I_{1,8}(2) (thm:one-cusp-lattice), and the group of the
labelled cusp is Gamma_e = the image of Stab_{Gamma_{Co,2}}(eta) in Orth(K).  Since
Gamma_{Co,2} = rho_{T_Co}^{-1}(P) with P = O(q_{U(2)}) x O(q_{E_8(2)}) acting on the U(2) and
E_8(2) summands of A_{T_Co} = A_<h> perp A_{U(2)} perp A_{E_8(2)} and trivially on A_<h>, an isometry
of K lies in Gamma_e only if its action on A_K preserves the decomposition
A_K = A_<h> perp A_{E_8(2)}.

This script checks, in the orthogonal model of K:
  (1) r_0^2 = -4 and s_{r_0}(x) = x + (1/2)(x, r_0) r_0 is integral on a basis of K;
  (2) s_{r_0} preserves q on all 512 classes of A_K;
  (3) it moves classes across the decomposition: the witness [E_3/2] is carried to
      [H_0/2] + [E_1/2] + [E_2/2], which has a nonzero <h>-component.
So s_{r_0} is not in Gamma_e at any labelled cusp, and the labelled chamber is not the unpolarized
one.  No provider call: the model and its discriminant form are written out here.
"""
from fractions import Fraction as F
from itertools import product


def main():
    K = [[2 if i == 0 and j == 0 else (-2 if i == j else 0) for j in range(9)] for i in range(9)]

    def bil(x, y):
        return sum(K[i][j] * x[i] * y[j] for i in range(9) for j in range(9))

    def q(z):
        return F(sum(F(z[i]) * K[i][j] * F(z[j]) for i in range(9) for j in range(9))) % 2

    r0 = [1, -1, -1, -1, 0, 0, 0, 0, 0]
    print("K = I_{1,8}(2) = <2>_H0 + <-2>_{E1..E8}, orthogonal basis; rank 9, det",
          round(__import__("functools").reduce(lambda a, b: a * b, [2] + [-2] * 8)), )
    print("r_0 = H_0 - E_1 - E_2 - E_3, r_0^2 =", bil(r0, r0))

    def refl(x):
        c = bil(x, r0)
        return [x[i] + F(c, 2) * r0[i] for i in range(9)]

    basis = [[1 if i == j else 0 for j in range(9)] for i in range(9)]
    print("s_{r_0} integral on a basis of K:", all(all(v.denominator == 1 for v in refl(b)) for b in basis))

    def cls(x):
        return tuple(F(v) % 1 for v in x)

    changed = 0
    across = 0
    witness = None
    for eps in product((0, 1), repeat=9):
        z = cls([F(e, 2) for e in eps])
        w = cls(refl([F(e, 2) for e in eps]))
        if q(z) != q(w):
            changed += 1
        if (z[0] == 0) != (w[0] == 0):
            across += 1
            if witness is None:
                witness = (z, w)
    print("classes of A_K (512) whose q changes:", changed)
    print("classes moved across A_<h> perp A_{E_8(2)}:", across, "of 512")
    print("witness: [E_3/2] =", tuple(str(v) for v in witness[0]),
          " -> ", tuple(str(v) for v in witness[1]))
    print()
    print("so the action of s_{r_0} on A_K does not preserve the decomposition that P is defined by,")
    print("and every lift of s_{r_0} has the same action on A_K because the lifts differ by")
    print("ker(Orth(T_Co) -> Orth(K)), which acts trivially there.  Hence s_{r_0} is outside")
    print("Gamma_e at every labelled cusp: the folded diagram is not the unpolarized chamber.")


if __name__ == "__main__":
    main()
