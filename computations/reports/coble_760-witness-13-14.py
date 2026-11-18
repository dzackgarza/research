"""#760, item 7: a certified witness that roots 13 and 14 are Gamma_Co,2-equivalent at cusp 5.

The three admissible roots at cusp 5 have pairwise distinct classes in K_5, so they are distinct
roots; the question is which pairs lie in one Gamma_Co,2-orbit.  This record settles one pair.

The symmetry sigma = [8,6,5,4,3,2,7,1,9,10,11,12,14,13] of Sterk's printed cusp-5 diagram fixes the
Coble root's label 11 and exchanges labels 13 and 14.  It does not automatically lift to the
lattice: the fourteen roots span a rank-10 sublattice L_0 whose orthogonal complement is a rank-2
lattice K, and T_En contains L_0 + K with index 2 (det L_0 = -1024, det K = -4, det T_En = 1024).
Sigma acts on L_0 as an integral isometry phi of determinant -1; phi extends to T_En exactly when it
preserves the gluing class of e_1 in A_{L_0} + A_K, here (0, 1/2, 0, ..., 0 | 0, 0).

It does preserve it, and the record then builds the extension g = phi + id on K as an explicit
12 x 12 matrix and checks, rather than asserts, that g is integral, preserves the form, maps all
fourteen printed roots as sigma says, fixes delta, fixes eta_5, and exchanges the lifts of labels 13
and 14.  That g lies in Gamma_Co,2 cap Stab(eta_5) and carries the class of 13 to the class of 14,
so those two marked roots are equivalent.

What this does not settle: root 12.  No symmetry of the diagram exchanges 12 with either of 13 and
14 while fixing label 11 (coble_760-cusp-symmetry-run.txt), so the pair (12,13) is the one left,
and deciding it needs the reduction item 7 has needed all along.

    usage: python3 computations/reports/coble_760-witness-13-14.py
"""
import sys
import time
sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix, identity_matrix
C = CartanMatrix(["E",8]); U = matrix(ZZ,[[0,1],[1,0]])
G = block_diagonal_matrix(U, 2*U, -2*C); N=12
BAS=[vector(ZZ,[1 if k==i else 0 for k in range(N)]) for i in range(N)]
e,f,ep,fp=BAS[0],BAS[1],BAS[2],BAS[3]; alpha=[BAS[4+i] for i in range(8)]
Cinv=C.inverse(); abar=[vector(ZZ,[int(c) for c in sum(QQ(-Cinv[k,i])*alpha[k] for k in range(8))]) for i in range(8)]
def ip(x,y): return int(vector(ZZ,x)*G*vector(ZZ,y))
et,ft=e+ep+fp-alpha[0], f+ep+fp-alpha[0]
at=[ep-fp,alpha[1],fp+alpha[2]]+list(alpha[3:8])
Gt=matrix(ZZ,8,8,lambda i,j: ip(at[i],at[j])); Gti=Gt.inverse()
abart=[vector(ZZ,[int(c) for c in sum(QQ(2*Gti[k,i])*at[k] for k in range(8))]) for i in range(8)]
R5=[at[1],at[3],at[4],at[5],at[6],at[7],at[0],abart[7],
    2*et-at[0], 2*et+(abart[1]-abart[2]), ft-et,
    et+ft+(abart[5]-abart[2]), et+ft+(abart[0]+abart[7]-abart[2]), et+ft+at[2]]
SIG=[8,6,5,4,3,2,7,1,9,10,11,12,14,13]   # fixes label 11, swaps 13 and 14
print("the lift of sigma %s: solve g r_i = r_sigma(i) for integral g" % SIG)
rows=[]; rhs=[]
# unknowns: entries of g, indexed (a,b) -> a*N+b, with (g x)_a = sum_b g[a,b] x_b
for i in range(14):
    src=R5[i]; dst=R5[SIG[i]-1]
    for a in range(N):
        r=[0]*(N*N)
        for b in range(N):
            r[a*N+b]=int(src[b])
        rows.append(r); rhs.append(int(dst[a]))
A=matrix(ZZ, len(rows), N*N, rows); b=vector(ZZ, rhs)
print("system: %d equations, %d unknowns, rank %d" % (A.nrows(), A.ncols(), A.rank()))
t=time.time()
try:
    sol=A.solve_right(b)
    consistent=True
except ValueError:
    consistent=False; sol=None
print("consistent over QQ: %s (%.1f s)" % (consistent, time.time()-t))
if consistent:
    integral = all(x in ZZ for x in sol)
    print("the particular solution is integral: %s" % integral)
    print("solution space dimension: %d" % (N*N - A.rank()))
    if integral:
        M=matrix(ZZ, N, N, [int(x) for x in sol])
        form = matrix(QQ,N,N,list(M.transpose()*G*M)) == matrix(QQ,G)
        print("form-preserving: %s" % form)
        print("maps every root correctly: %s" % all(M*vector(ZZ,R5[i])==vector(ZZ,R5[SIG[i]-1]) for i in range(14)))
        d = M*vector(ZZ,e-f)
        print("delta -> %s (== delta: %s, == -delta: %s)" % (list(d), d==vector(ZZ,e-f), d==-vector(ZZ,e-f)))

print()
print("=== the complement of the root span, and whether the lattice splits over it")
rows2 = matrix(ZZ, 14, N, [list(G*vector(ZZ,r)) for r in R5])
S2, _, V2 = rows2.smith_form()
ker = [vector(ZZ, [V2[i, j] for i in range(N)]) for j in range(N) if all(S2[k, j] == 0 for k in range(14))]
print("kernel of the roots' pairing rows has rank %d" % len(ker))
# a basis of the root span
H = matrix(ZZ, 14, N, [list(r) for r in R5])
h = H.hermite_form(include_zero_rows=False)
L0 = [vector(ZZ, list(h.row(i))) for i in range(h.nrows()) if any(x != 0 for x in h.row(i))]
print("root span rank %d" % len(L0))
G0 = matrix(ZZ, len(L0), len(L0), lambda i, j: ip(L0[i], L0[j]))
print("det of the root span's Gram: %s" % G0.det())
for basis in ([ker] if len(ker) == 2 else []):
    GK = matrix(ZZ, len(ker), len(ker), lambda i, j: ip(ker[i], ker[j]))
    print("det of the complement's Gram: %s" % GK.det())
    print("product of determinants: %s   (det T_En = %s)" % (G0.det()*GK.det(), G.det()))
    print("the lattice splits as an orthogonal direct sum over them: %s"
          % (G0.det()*GK.det() == G.det()))

print()
print("=== the gluing class, and whether sigma preserves it")
L0b = matrix(ZZ, len(L0), N, [list(v) for v in L0])
Kb = matrix(ZZ, len(ker), N, [list(v) for v in ker])
Mbas = matrix(ZZ, 12, 12, [list(L0b.row(i)) for i in range(len(L0))] + [list(Kb.row(i)) for i in range(len(ker))]).transpose()
print("det of the glued sublattice (index in T_En): %s" % abs(Mbas.det()))
Minv = Mbas.inverse()
probe = vector(QQ, [1] + [0]*11)
u = Minv * probe                      # coordinates of e_1 in the M-basis
h0 = [QQ(x) - QQ(x).floor() for x in u[:len(L0)]]
hK = [QQ(x) - QQ(x).floor() for x in u[len(L0):]]
print("the gluing class is (h0, hK) = (%s | %s)" % ([str(x) for x in h0], [str(x) for x in hK]))
# phi on the root span, in the HNF basis of that span.  Columns of F are the images of the basis
# vectors: with C the coordinates of the roots in that basis and D those of their images,
# C F = D, so F = C^+ D.
Hre = matrix(ZZ, 14, N, [list(r) for r in R5])
Him = matrix(ZZ, 14, N, [list(R5[SIG[i]-1]) for i in range(14)])
L0b_q = matrix(QQ, L0b)
L0pinv = L0b_q.transpose() * (L0b_q * L0b_q.transpose()).inverse()      # 12 x 10
Cq = matrix(QQ, Hre) * L0pinv                                            # 14 x 10
Dq = matrix(QQ, Him) * L0pinv
assert all(x in ZZ for x in list(Cq.list()) + list(Dq.list())), "coordinates are not integral"
Cq = matrix(ZZ, Cq); Dq = matrix(ZZ, Dq)
F = (matrix(QQ, Cq).pseudoinverse() * matrix(QQ, Dq)).transpose()
print("phi on the span: integral %s, determinant %s, C F^T = D: %s"
      % (all(x in ZZ for x in F.list()), F.det(),
         matrix(QQ, Cq) * F.transpose() == matrix(QQ, Dq)))
Finv_T = (F.inverse()).transpose()
phi_h0 = [QQ(sum(Finv_T[i, j]*h0[j] for j in range(len(L0)))) for i in range(len(L0))]
phi_h0 = [QQ(x) - QQ(x).floor() for x in phi_h0]
same = all(phi_h0[i] == h0[i] for i in range(len(L0)))
print("h0 = %s" % [str(x) for x in h0])
print("phi(h0) = %s" % [str(x) for x in phi_h0])
print("phi fixes the gluing class: %s" % same)

print()
print("=== the witness, built and checked as an explicit matrix (the arbiter of the above)")
imgs_L0 = [sum((int(F[j, i]) * L0[j] for j in range(len(L0))), vector(ZZ, [0]*N)) for i in range(len(L0))]
basis = matrix(ZZ, 12, 12, [list(L0[i]) for i in range(len(L0))] + [list(ker[i]) for i in range(len(ker))]).transpose()
image = matrix(ZZ, 12, 12, [list(imgs_L0[i]) for i in range(len(L0))] + [list(ker[i]) for i in range(len(ker))]).transpose()
gq = image * matrix(QQ, basis).inverse()
print("g is integral: %s" % all(x in ZZ for x in gq.list()))
if all(x in ZZ for x in gq.list()):
    g = matrix(ZZ, gq)
    delta = e - f; eta = 2*e + 2*f + abar[0]
    form = matrix(QQ, N, N, list(g.transpose()*G*g)) == matrix(QQ, G)
    roots_ok = all(g*vector(ZZ, R5[i]) == vector(ZZ, R5[SIG[i]-1]) for i in range(14))
    print("g preserves the form: %s" % form)
    print("g maps every root as sigma says: %s" % roots_ok)
    print("g(delta) = delta: %s" % (g*vector(ZZ, delta) == vector(ZZ, delta)))
    print("g(eta_5) = eta_5: %s" % (g*vector(ZZ, eta) == vector(ZZ, eta)))
    print("g(r_13) = r_14 and g(r_14) = r_13: %s"
          % (g*vector(ZZ, R5[12]) == vector(ZZ, R5[13]) and g*vector(ZZ, R5[13]) == vector(ZZ, R5[12])))
    if form and roots_ok:
        print()
        print("WITNESS: g is an integral isometry of T_En fixing delta and eta_5 and exchanging the")
        print("lifts of labels 13 and 14, so roots 13 and 14 are Gamma_Co,2-equivalent at cusp 5.")

print("PYEXIT=0")
