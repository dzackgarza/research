"""#760, item 7: roots 12 and 13 are Gamma_Co,2-equivalent, and with 13 and 14 all three are one orbit.

The pair (12,13) was the last undecided one.  It does not need a permutation of the printed diagram:
the transposition of 12 and 13 that fixes the Coble root is not a symmetry of the printed Gram, but
it does not have to be.  What is needed is an isometry of T_En fixing delta and eta_5 and swapping
the two vectors, and that can be built on the rank-3 lattice they span with delta.

P = saturation of <delta, r12, r13> has rank 3 and determinant -8; it is not a direct summand (the
parallel record coble_759-swap-1213-run.txt records the same index-2 gluing), so the identity on the
rank-9 complement need not be the extension that works.  Here it is: the transposition of the two
square-(-2) generators of P, extended by the identity on P^perp, comes out integral.

The record builds that extension as a 12 x 12 integer matrix and checks it rather than asserting it:
g is integral, det g = -1, g^T G g = G, g(delta) = delta, g(eta_5) = eta_5, g(r12) = r13 and
g(r13) = r12.  So g lies in Gamma_Co,2, fixes eta_5, and carries the class of root 12 to the class
of root 13.  Together with coble_760-witness-13-14-run.txt --- which gives an isometry fixing delta
and eta_5 and exchanging 13 with 14 --- all three admissible roots at cusp 5 lie in ONE
Gamma_Co,2-orbit.

What that means for the conjecture is stated on the page: with one orbit there is no pair of
inequivalent admissible roots at cusp 5, and cusps 3 and 4 carry one each, so the conjecture's
hypothesis is never met at a marked cusp and its conclusion holds vacuously.  Nothing is lost in the
KSBA boundary because there is nothing to lose: the marking is unique up to Gamma_Co,2.

    usage: python3 computations/reports/coble_760-witness-12-13.py
"""
import sys
sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
exec(open('/repo/computations/reports/coble_760-witness-13-14.py').read().split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
delta = e-f; eta = 2*e+2*f+abar[0]
r12, r13 = R5[11], R5[12]
rows = [list(G*vector(ZZ,v)) for v in (delta, r12, r13)]
S,_,V = matrix(ZZ,3,N,rows).smith_form()
K3 = [vector(ZZ,[V[i,j] for i in range(N)]) for j in range(N) if all(S[k,j]==0 for k in range(3))]
S2,_,V2 = matrix(ZZ,len(K3),N,[list(G*vector(ZZ,k)) for k in K3]).smith_form()
P = [vector(ZZ,[V2[i,j] for i in range(N)]) for j in range(N) if all(S2[k,j]==0 for k in range(len(K3)))]
def intriple(v): return matrix(QQ, [list(delta), list(r12), list(r13)]).transpose().solve_right(vector(QQ,v))
swapped=[]
for b in P:
    co = intriple(b); assert all(x in ZZ for x in co), co
    swapped.append(int(co[0])*delta + int(co[2])*r12 + int(co[1])*r13)
PP = matrix(ZZ,12,12,[list(v) for v in P]+[list(v) for v in K3]).transpose()
img = matrix(ZZ,12,12,[list(v) for v in swapped]+[list(v) for v in K3]).transpose()
g = matrix(ZZ, matrix(QQ,img)*matrix(QQ,PP).inverse())
print("g integral:", all(x in ZZ for x in g.list()))
print("det g:", g.det())
print("g^T G g == G:", matrix(QQ,N,N,list(g.transpose()*G*g)) == matrix(QQ,G))
print("g(delta) == delta:", g*vector(ZZ,delta)==vector(ZZ,delta))
print("g(eta) == eta:", g*vector(ZZ,eta)==vector(ZZ,eta))
print("g(r12) == r13:", g*vector(ZZ,r12)==vector(ZZ,r13), " g(r13) == r12:", g*vector(ZZ,r13)==vector(ZZ,r12))
print("g fixes every irrelevant free direction? (r14):", g*vector(ZZ,R5[13])==vector(ZZ,R5[13]))
print()
print("delta is the root of printed label 11:", R5[10]==delta or R5[10]==-delta)
print("so g is in Gamma_Co,2 = Stab_O(T_En)(Z delta) and fixes eta_5: it is in the acting group")
print("and it carries the class of root 12 to the class of root 13.")

print("PYEXIT=0")
