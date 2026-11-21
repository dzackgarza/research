"""Lattice checks for thm:coble-monodromy-on-m-classical and clause 5 of
lem:transport-order-on-the-classical-coble-stack.

Run:  python3 computations/reports/coble_799-element-lattice-checks.py
Exact integer arithmetic only (sympy for the determinants).

What is checked, and why each is needed:
  (1) M = <e_0,...,e_10> with the form diag(2,-2,...,-2), K = -3e_0 + sum e_i.
  (2) K^2 = -2 and K is primitive.
  (3) x.K is even for every x in M (the condition that makes K* = K/K^2
      integral, hence M = K^perp + Z K).  A control on a lattice where the
      condition fails shows that primitivity alone does not split off K^perp.
  (4) det(M) = det(K^perp) * K^2, so det(K^perp) = -2^10.
  (5) The ten classes delta_1..delta_9, delta_c have Gram matrix 2*(-C(E_10))
      and determinant -2^10 = det(K^perp), so they span K^perp; that is what
      makes "K^perp = E_10(2)" a computation and not a diagram reading.
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix

def gram(vs, diag):
    return Matrix([[sum(diag[k] * a[k] * b[k] for k in range(len(diag)))
                    for b in vs] for a in vs])

# (1) M of rank 11, signature (1,10)
diag = [2] + [-2] * 10
n = len(diag)
e = [[1 if k == j else 0 for k in range(n)] for j in range(n)]
K = [-3] + [1] * 10
dot = lambda a, b: sum(diag[k] * a[k] * b[k] for k in range(n))

# (2)
print("K^2 =", dot(K, K))
from math import gcd
print("K primitive (gcd of coordinates is 1):", gcd(*[abs(c) for c in K]) == 1)
print("K.K = ", dot(K, K), " (so K^2 divides x.K for all x iff x.K is even)")

# (3) evenness, checked on the frame, which is a Z-basis
vals = [dot(x, K) for x in e]
print("x.K on the frame:", vals, "all even:", all(v % 2 == 0 for v in vals))
# the coefficient a(x) = (x.K)/K^2 that splits x = (x - aK) + aK
print("(x.K)/K^2 on the frame:", [Fraction(dot(x, K), dot(K, K)) for x in e])

# control: primitivity does not suffice
diag2, K2 = [2, 2], [1, 1]
e2 = [[1, 0], [0, 1]]
dot2 = lambda a, b: sum(diag2[k] * a[k] * b[k] for k in range(2))
print("control: diag(2,2), K=e1+e2: K^2 =", dot2(K2, K2),
      "K primitive:", gcd(*K2) == 1,
      " (x.K)/K^2 on the frame:", [Fraction(dot2(x, K2), dot2(K2, K2)) for x in e2],
      "-> index 2, so primitive does NOT split")

# (4) determinant of K^perp, from det(M) = det(K^perp) * K^2
detM = 1
for d in diag:
    detM *= d
print("det M =", detM, "   det K^perp = det M / K^2 =", Fraction(detM, dot(K, K)))

# (5) the ten classes of lem:coble-image-on-m-is-the-weyl-group(1)
delta = []
for i in range(1, 10):
    v = [0] * n
    v[i] += 1
    v[i + 1] -= 1
    delta.append(v)
dc = [0] * n
dc[0] += 1                      # pi^*H
for i in (1, 2, 3):
    dc[i] -= 1                  # - pi^*E_i
delta.append(dc)
G = gram(delta, diag)
print("Gram of the ten classes:\n", G)
print("det Gram =", G.det())
print("Gram / 2 has -2 on the diagonal:", all(G[i, i] // 2 == -2 for i in range(10)))
print("det of the half Gram (the Cartan matrix of E_10):", (G / 2).det())
print("rank of the ten classes:", G.rank())
print("det Gram equals det K^perp:", G.det() == Fraction(detM, dot(K, K)))
