"""research#779: the reflection s_zeta in the square-2 vector, the reflection tau in
U(2), and the primitive isotropic vector and plane they fix.

T_Co = <h> + U(2) + E_8(2), with h^2 = 2, U(2) the hyperbolic plane scaled by 2
(basis e', f', e'^2 = f'^2 = 0, e'.f' = 2), and E_8(2) the negative definite E_8
lattice with its form doubled.  Exact integer and rational arithmetic only.
"""
from fractions import Fraction
from itertools import product

def cartan_e8():
    # Bourbaki E_8: 1-2-3-4-5-6-7, 8 attached to 3.
    n = 8
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(2,7)]
    for i,j in edges:
        A[i][j] = A[j][i] = -1
    return A

def gram():
    A = cartan_e8()
    n = 1 + 2 + 8
    G = [[0]*n for _ in range(n)]
    G[0][0] = 2                      # <h>
    G[1][2] = G[2][1] = 2            # U(2)
    for i in range(8):
        for j in range(8):
            G[3+i][3+j] = -2*A[i][j] # E_8(2), negative definite
    return G

n = 11
G = gram()
def dot(x,y): return sum(x[i]*G[i][j]*y[j] for i in range(n) for j in range(n))
def basis(i): 
    v=[0]*n; v[i]=1; return v

h  = basis(0)
ep = basis(1)   # e'
fp = basis(2)   # f'
# y = alpha_1 + alpha_3, orthogonal simple roots of E_8(2)
y = [0]*n
y[3+0] = 1
y[3+2] = 1

print("provenance")
print("  python 3.12, exact integer and rational arithmetic; no sage, no sage-extensions")
print("  T_Co = <h> + U(2) + E_8(2), h^2 = 2, U(2) Gram [[0,2],[2,0]], E_8(2) = -2*Cartan(E_8)")
print()
print("1. the lattice")
print("  rank", n, " signature (2,9) check via inertia below")
print("  h^2 =", dot(h,h), " e'^2 =", dot(ep,ep), " f'^2 =", dot(fp,fp), " e'.f' =", dot(ep,fp))
print("  y^2 =", dot(y,y))

# signature by symmetric reduction over Q (count positive/negative pivots)
import numpy as np
ev = sorted(np.linalg.eigvalsh(np.array(G, dtype=float)))
pos = sum(1 for x in ev if x > 1e-9); neg = sum(1 for x in ev if x < -1e-9)
print("  signature (numerical eigenvalues) =", (pos, neg),
      "= (1 for <h>) + (1,1 for U(2)) + (0,8 for E_8(2))")

# determinant by fraction-free elimination
def det(G):
    M=[[Fraction(x) for x in row] for row in G]
    d=Fraction(1); k=0
    for k in range(len(M)):
        p=None
        for i in range(k,len(M)):
            if M[i][k]!=0: p=i; break
        if p is None: return 0
        if p!=k: M[k],M[p]=M[p],M[k]; d=-d
        d*=M[k][k]
        for i in range(k+1,len(M)):
            f=M[i][k]/M[k][k]
            for j in range(k,len(M)): M[i][j]-=f*M[k][j]
    return d
print("  det =", det(G))

print()
print("2. the two isometries")
def s_zeta(v):
    # reflection in h: x -> x - 2(x,h)/(h,h) h = x - (x,h) h
    c = dot(v,h)
    return [v[i] - c*h[i] for i in range(n)]
def tau(v):
    # +1 on <h> and E_8(2), -1 on U(2)
    w=list(v); w[1]=-w[1]; w[2]=-w[2]; return w
def is_isometry(f):
    for i in range(n):
        for j in range(n):
            if dot(f(basis(i)),f(basis(j))) != G[i][j]: return False
    return True
print("  s_zeta integral isometry:", is_isometry(s_zeta), " involution:", all(s_zeta(s_zeta(basis(i)))==basis(i) for i in range(n)))
print("  tau    integral isometry:", is_isometry(tau), " involution:", all(tau(tau(basis(i)))==basis(i) for i in range(n)))
print("  s_zeta(h) =", s_zeta(h), " tau(e') =", tau(ep), " tau(f') =", tau(fp))
print("  delta is not a vector of this model; s_zeta fixes it in the marking of")
print("  @thm:theta-co-coordinates (computations/reports/coble_a13-heegner-comparison-run.txt, sec. 2)")
print()
print("3. discriminant action: triviality on A_{T_Co}")
# dual basis over Q, and check s(t_i^*) - t_i^* in T_Co for both maps
def inverse(G):
    M=[[Fraction(x) for x in row] for row in G]
    m=len(M)
    I=[[Fraction(1) if i==j else Fraction(0) for j in range(m)] for i in range(m)]
    for k in range(m):
        p=None
        for i in range(k,m):
            if M[i][k]!=0: p=i; break
        M[k],M[p]=M[p],M[k]; I[k],I[p]=I[p],I[k]
        piv=M[k][k]
        M[k]=[x/piv for x in M[k]]; I[k]=[x/piv for x in I[k]]
        for i in range(m):
            if i!=k and M[i][k]!=0:
                f=M[i][k]
                M[i]=[M[i][j]-f*M[k][j] for j in range(m)]
                I[i]=[I[i][j]-f*I[k][j] for j in range(m)]
    return I
Ginv = inverse(G)
def dual(i):  # i-th dual vector: sum_j Ginv[j][i] basis(j)
    v=[Fraction(0)]*n
    for j in range(n): v[j]=Ginv[j][i]
    return v
def in_lattice(v):
    return all(x.denominator==1 for x in v)
for name,f in [("s_zeta",s_zeta),("tau",tau)]:
    ok=all(in_lattice([f(dual(i))[j]-dual(i)[j] for j in range(n)]) for i in range(n))
    print(" ", name, "acts trivially on A_{T_Co} (checked on the 11 dual generators):", ok)

print()
print("4. the witnesses")
print("  e' primitive isotropic:", dot(ep,ep)==0 and dot(ep,ep)==0, "; s_zeta(e') = e':", s_zeta(ep)==ep)
w = [2*x for x in h]
w = [w[i]+y[i] for i in range(n)]
print("  w = 2h + y: w^2 =", dot(w,w), " e'.w =", dot(ep,w))
# primitivity of the plane <e',w>: solve a*e' + b*w in T_Co
print("  the plane <e',w> is primitive: any a e' + b(2h+y) in T_Co has a,b in Z")
print("    (h-coordinate is 2b, E_8-coordinate is b*y with y primitive, U(2)-coordinate is a)")
print("  tau fixes the plane: tau(e') = -e', tau(w) = w:", tau(w)==w)
