"""#789: the discriminant class [eta_k/2] of each of Sterk's 0-cusp representatives.

For k = 2,3,4,5 Sterk's representative eta_k lies in T_Co = delta^perp (it is
orthogonal to delta), is primitive isotropic, and has divisibility 2 in T_Co, so
[eta_k/2] is a nonzero isotropic class of A_{T_Co} = T_Co^vee/T_Co.  This script
computes, in exact arithmetic, its decomposition along

    T_Co = <h> + U(2) + E8(2),   h = e+f, h^2 = 2,

and the q-values of the U(2)- and E8(2)-components, hence which of the four
P-orbits of prop:coble-cong-point-stabilizer(2) the class lies in.

Inputs: Sterk, Math. Z. 207 (1991), (4.2.3), printed p. 16, for the five
representatives and their y_3, y_4; Dolgachev-Kondo, Izv. Math. 77 (2013), (3.6),
printed p. 513, for T_Co = <2> + U(2) + E8(2); AEGS, Nagoya Math. J. 259 (2025),
Def. 2.3, printed p. 586, for T_En.

Output: for each k, the three components of eta_k/2 (h-part, U(2)-part,
E8(2)-part), the q-value of each, and the size of the P-orbit.
"""
from sage.all import matrix, vector, ZZ, QQ, block_diagonal_matrix, CartanMatrix

C = CartanMatrix(["E", 8])
G = block_diagonal_matrix(matrix(ZZ, [[2]]),
                          matrix(ZZ, [[0, 2], [2, 0]]),
                          -2 * C)                     # T_Co, basis (h,e',f',a1..a8)
N = 11
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
h, ep, fp = BAS[0], BAS[1], BAS[2]
al = [BAS[3 + i] for i in range(8)]

def ip(a, b):
    return a * G * b

Cinv = C.inverse()
abar = [vector(ZZ, sum(QQ(-Cinv[k, i]) * al[k] for k in range(8))) for i in range(8)]
y3 = abar[7]                                        # square -4
y4 = -(4 * al[0] + 5 * al[1] + 7 * al[2] + 10 * al[3]
       + 8 * al[4] + 6 * al[5] + 4 * al[6] + 2 * al[7])   # square -8
ETA = {2: ep, 3: ep + fp + y3, 4: 2 * ep + fp + y4, 5: 2 * h + y4}

# delta in the T_En coordinates, to check eta_k . delta = 0: in T_Co coordinates
# delta has no component, so the check is that each eta_k lies in the lattice at all,
# and the orthogonality is the statement that T_Co = delta^perp.  We verify the
# components and the q-values instead.
print("y3^2 =", ip(y3, y3), "  y4^2 =", ip(y4, y4))
for k in (2, 3, 4, 5):
    v = ETA[k]
    print("cusp %d: eta = %s, eta^2 = %d" % (k, list(v), ip(v, v)))
    half = vector(QQ, v) / 2
    # components along the three summands
    hpart = QQ(half[0]) * h
    upart = QQ(half[1]) * ep + QQ(half[2]) * fp
    epart = sum(QQ(half[3 + i]) * al[i] for i in range(8))
    print("   h-part %s (in the lattice? %s), U(2)-part %s, E8-part %s"
          % (list(hpart), all(x.denominator() == 1 for x in hpart), list(upart), list(epart)))
    qU = upart * G * upart if upart != 0 else QQ(0)
    qE = epart * G * epart if epart != 0 else QQ(0)
    print("   q(U(2)-part) = %s, q(E8-part) = %s, total q = %s (in 2Z? %s)"
          % (qU, qE, qU + qE, (qU + qE) % 2 == 0))
    zeroU = all(x == 0 for x in upart)
    # q of a U(2) class: 0 means u_1 or u_2 (or 0), 1 means u_3
    if zeroU:
        ukind = "0"
    elif qU % 2 == 0:
        ukind = "u_1 or u_2 (q=0)"
    else:
        ukind = "u_3 (q=1)"
    zeroE = all(x == 0 for x in epart)
    if zeroU and zeroE:
        orbit = "zero class (should not occur)"
    elif zeroU:
        orbit = "{(0,e): e in E_0}, size 135" if qE % 2 == 0 else "UNCLASSIFIED"
    elif zeroE and qU % 2 == 0:
        orbit = "{u_1,u_2}, size 2"
    elif qU % 2 == 0 and qE % 2 == 0:
        orbit = "{(u_1,e),(u_2,e): e in E_0}, size 270"
    elif qU % 2 == 1 and qE % 2 == 1:
        orbit = "{(u_3,e'): e' in E_1}, size 120"
    else:
        orbit = "UNCLASSIFIED"
    print("   U(2) class kind:", ukind, "  E8 class q:", qE % 2, "  P-orbit:", orbit)
