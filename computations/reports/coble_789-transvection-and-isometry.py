"""#789: the Z e'-translate lemma and the explicit isometry of U + E8(2).

Two checks, both exact integer arithmetic in SageMath:

(A) The Eichler transvection E(x) = x + (x,e')e - (x,e)e' of T_En = U + U(2) + E8(2)
    is an integral isometry fixing e' and sending delta = e-f to delta - e'; its
    k-th power sends delta to delta - k e'.  It acts trivially on A_{T_En}, hence lies
    in the discriminant kernel and therefore in Gamma_{En,2} = rho^{-1}(M).

(B) The explicit isometry N of K = U + E8(2) with N(e-f) = e+f+a_1.

Inputs: AEGS Def. 2.3 (printed p. 586) for T_En; Sterk (4.2.2)-(4.2.3) (printed p. 16)
for the basis and delta; Sterk Prop. 2.7 (printed p. 6) for Gamma_{En,2} as the group
preserving the decomposition of A_{T_En}; Gritsenko-Hulek, arXiv:0810.1614v1, section 3.1,
Lemma 3.1 and the integrality assertion after (10), printed pp. 8-9, for the integrality
of the transvection.
"""
from sage.all import matrix, vector, ZZ, QQ, block_diagonal_matrix, CartanMatrix

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)          # T_En, basis (e,f,e',f',a1..a8)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
al = [BAS[4 + i] for i in range(8)]
delta = e - f

def ip(x, y):
    return x * G * y

# ---- (A) the transvection -------------------------------------------------
cols = []
for x in BAS:
    cols.append(vector(ZZ, x + ip(x, ep) * e - ip(x, e) * ep))
E = matrix(ZZ, N, N, lambda i, j: cols[j][i])
print("(A) E(e')=e':", E * ep == ep)
print("(A) E(delta)=delta+e':", E * delta == delta + ep)
print("(A) E^T G E = G:", E.transpose() * G * E == G, " det E =", E.det())
for k in range(1, 6):
    print("    E^%d(delta) = delta + %d e':" % (k, k), E**k * delta == delta + k * ep)
Ginv = G.inverse()
trivial = True
for i in range(N):
    y = Ginv * vector(ZZ, [1 if j == i else 0 for j in range(N)])   # a basis of T_En^vee
    d = y + ip(y, ep) * e - ip(y, e) * ep - y
    if any(q.denominator() != 1 for q in d):
        trivial = False
        print("    FAILS on dual basis vector", i, list(d))
print("(A) E acts trivially on A_{T_En} (E(y)-y integral for a basis of the dual):", trivial)

# ---- (B) the explicit isometry of K = U + E8(2) ---------------------------
GK = block_diagonal_matrix(U, -2 * C)                 # K = U + E8(2), basis (e,f,a1..a8)
BASk = [vector(ZZ, [1 if k == i else 0 for k in range(10)]) for i in range(10)]
ek, fk = BASk[0], BASk[1]
ak = [BASk[2 + i] for i in range(8)]

def ipk(x, y):
    return x * GK * y

dK = ek - fk
y = ek + fk + ak[0]
vp = 3 * ek + fk + ak[0]
Mv = matrix(ZZ, 2, 10, [list(GK * y), list(GK * vp)])
B = Mv.right_kernel_matrix()
print("(B) B G_K B^T equals -2 Cartan(E8):", B * GK * B.transpose() == -2 * C)
colsK = [2 * ek + fk + ak[0], ek] + [B.row(i) for i in range(8)]
NI = matrix(ZZ, 10, 10, lambda i, j: colsK[j][i])
print("(B) N^T G_K N = G_K:", NI.transpose() * GK * NI == GK, " det N =", NI.det())
print("(B) N(e-f) = e+f+a_1:", NI * dK == y)
print("(B) the matrix N, rows:")
for i in range(10):
    print("   ", list(NI.row(i)))
