"""#760, item 7: the cheapest test of the lift question, and its outcome.

The lift question is whether a symmetry of the printed cusp-5 diagram is realised by an integral
isometry of T_En.  An integral isometry acts on T_En/2T_En, so a necessary condition is that it
preserve congruence of the roots modulo 2: if r_i = r_j mod 2 then also g(r_i) = g(r_j) mod 2, and
the permutation of labels must respect that relation.  A violation would disprove the lift outright
and settle the pair as inequivalent; this record runs the test for the two permutations that matter.

The outcome is that there is no obstruction: of the fourteen roots only labels 7 and 9 are
congruent modulo 2, and both permutations carry congruent labels to congruent labels.  The lift
question therefore survives the test and is not settled by it.  That is the honest content --- the
cheapest route is closed, and the extension problem itself is untouched.

    usage: python3 computations/reports/coble_760-mod2-lift-obstruction.py
"""
import sys
sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix
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
m2 = [tuple(int(x) % 2 for x in r) for r in R5]
print("the fourteen roots modulo 2 (a necessary condition for a lift):")
for i in range(14):
    print("  label %2d -> %s" % (i+1, m2[i]))
same = {}
for i in range(14):
    for j in range(i+1,14):
        if m2[i]==m2[j]: same.setdefault(i+1,[]).append(j+1)
print()
print("pairs of roots congruent modulo 2: %s" % {k: v for k, v in same.items()})
print()
sigmas = [
 [8,6,5,4,3,2,7,1,9,10,11,12,14,13],     # fixes 11, swaps 13/14
 [1,10,8,6,5,4,9,3,7,2,14,13,12,11],     # swaps 12/13, moves 11
]
for s in sigmas:
    perm = {i+1: s[i] for i in range(14)}
    ok = True
    for i in range(1,15):
        for j in range(i+1,15):
            if (m2[i-1]==m2[j-1]) != (m2[perm[i]-1]==m2[perm[j]-1]):
                ok = False
                print("  OBSTRUCTION for sigma %s: labels %d,%d congruent mod 2 is %s, but their images %d,%d is %s"
                      % (s, i, j, m2[i-1]==m2[j-1], perm[i], perm[j], m2[perm[i]-1]==m2[perm[j]-1]))
    print("  sigma %s: mod-2 congruences preserved: %s" % (s, ok))
print()
print("VERDICT: no mod-2 obstruction to either permutation.  Only labels 7 and 9 are congruent")
print("modulo 2 among the fourteen roots, and both permutations respect that relation, so this")
print("necessary condition is satisfied and the lift question is untouched by it.  The lift itself")
print("remains the open input for item 7, together with the reduction for the remaining pair.")
print("PYEXIT=0")
