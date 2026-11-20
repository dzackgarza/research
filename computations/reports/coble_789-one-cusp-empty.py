"""#789: the 1-cusp quotient Pi^perp/Pi at the four 1-cusps over cusp 1.

Sterk (Math. Z. 207 (1991), 4.3.5) states that the four
one-dimensional boundary components whose closure contains the 0-cusp e all
have the same quotient type, namely E8(-2) = E8(2).  This script checks the
case Pi = <e, e'> of the type {1,2} explicitly: Pi^perp = <e,e'> + E8(2), so
Pi^perp/Pi is E8(2), whose Gram matrix has diagonal -4 and off-diagonal 0 or 2,
so every square is divisible by 4 and there is no (-2)-vector.

Inputs: AEGS, Nagoya Math. J. 259 (2025), Def. 2.3 (T_En);
Sterk, (4.2.3) (the cusp vectors e, e'), and 4.3.5, printed
p. 20 (the common quotient type).
"""
import itertools
from sage.all import matrix, vector, ZZ, block_diagonal_matrix, CartanMatrix

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
al = [BAS[4 + i] for i in range(8)]

def ip(x, y):
    return x * G * y

print("e^2 =", ip(e, e), " e'^2 =", ip(ep, ep), " e.e' =", ip(e, ep), " e.a_i =", [ip(e, a) for a in al], " e'.a_i =", [ip(ep, a) for a in al])
# Pi^perp = <e, e'> + E8(2): check that every basis vector with the e,e' coefficients killed is in E8(2),
# and that e, e' are orthogonal to E8(2).
print("<e,e'> is orthogonal to E8(2):", all(ip(v, a) == 0 for v in (e, ep) for a in al))
# a vector x = a e + b f + c e' + d f' + y is in Pi^perp iff b = 0 and d = 0
for a, b, c, d in itertools.product(range(-2, 3), repeat=4):
    x = a * e + b * f + c * ep + d * fp
    orth = (ip(x, e) == 0 and ip(x, ep) == 0)
    if orth != (b == 0 and d == 0):
        print("MISMATCH at", a, b, c, d)
print("Pi^perp = {a e + c e' + y}: verified on the box")
E8 = -2 * C
print("E8(2) Gram diagonal:", [E8[i, i] for i in range(8)])
print("E8(2) off-diagonal entries:", sorted({E8[i, j] for i in range(8) for j in range(8) if i != j}))
def square(cc):
    return sum(cc[i] * cc[j] * E8[i, j] for i in range(8) for j in range(8))
print("every square divisible by 4 on [-2,2]^8:",
      all(square(cc) % 4 == 0 for cc in itertools.product(range(-2, 3), repeat=8)))
print("no (-2)-vector in E8(2): a square is -4*sum x_i^2 + 4*sum_{i<j, E8_ij=2} x_i x_j, a multiple of 4")
