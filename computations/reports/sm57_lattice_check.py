# Check the class identities for the extra (-2)-curves C_1,C_2 of a bitangent ruling fibre.
# Lattice N = <L1,L2,D>, Gram: L1^2=L2^2=0, L1.L2=2, D^2=-2, D.L_i=0 ; H = L1+L2.
import sympy as sp
L1,L2,D = sp.symbols('L1 L2 D')
basis=[L1,L2,D]
def dot(a,b):
    # bilinear form on N
    M = sp.Matrix([[0,2,0],[2,0,0],[0,0,-2]])   # order L1,L2,D
    va=sp.Matrix([a.coeff(v) for v in basis]); vb=sp.Matrix([b.coeff(v) for v in basis])
    return sp.simplify((va.T*M*vb)[0,0])
H = L1+L2
print("H.L1,H.L2,H.D =",dot(H,L1),dot(H,L2),dot(H,D))
# C_i = (L1 +- u)/2 with u in N^perp, u^2=-8 ; relations to be checked symbolically:
# C1+C2 = L1, C1.C2 = 2, C_i^2=-2, C_i.L1=0, C_i.L2=1, C_i.D=0, C_i.H=1
# Solve for C1 = a L1 + b L2 + c D + (u/2) with u in N^perp: write C1 = (L1/2) + (u/2).
a=sp.Rational(1,2); b=0; c=0
C1 = a*L1+b*L2+c*D
C2 = L1 - C1
print("C1+C2 = L1 ?", sp.simplify(C2-(L1-C1))==0)
print("C1.L1 (N-part) =",dot(C1,L1), " so C1.L1 = 0 with u.L1=0")
print("C1.L2 (N-part) =",dot(C1,L2), " so C1.L2 = 1 with u.L2=0")
print("C1.D  (N-part) =",dot(C1,D),  " so C1.D = 0 with u.D=0")
print("C1.H (N-part) =",dot(C1,H), " so C1.H = 1")
# u := 2C1 - L1 has u.L1=u.L2=u.D=0 and u^2 = -8
print("u = 2C1 - L1 = 0 in N (i.e. u lies in N^perp):", sp.simplify(2*C1-L1)==0)
print("u.C1 = (u^2)/2 = -4 :", sp.Rational(-8,2))
print("Hence for y in N_R with y.L1 = lam, and z_t = y + t u : z_t.C1 = lam/2 - 4t, which changes sign.")
