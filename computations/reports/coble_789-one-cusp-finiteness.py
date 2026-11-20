"""#789: the transvections that make a 1-cusp fibre finite.

For a primitive isotropic plane Pi = <u,v> of T_En and alpha in Pi^perp with
alpha^2 = -2, the Eichler transvections

    E_{u,z}(x) = x + (x,u)z - (x,z)u - (z^2/2)(x,u)u,    z.u = 0,

lie in Gamma_{En,2}, preserve Pi setwise, and act on Pi^perp by
x -> x - (x,z)u.  The values (alpha,z) for z in u^perp form an ideal d_u Z
with d_u | 2 (because (alpha,alpha) = -2), so the orbit of alpha contains
alpha + 2u; likewise alpha + 2v.  Hence at most four Stab(Pi)-orbits per
(-2)-class of Pi^perp/Pi, and the fibre is finite.

This script checks the identities on one concrete plane with a nonzero fibre,
Pi = <u,v> inside T_Co = delta^perp with

    u = 2h + e' - 2f',  v = e' + 2f' + y_4,  h = e+f,  y_4^2 = -8,

and alpha = delta = e - f.  Here z = delta lies in u^perp and v^perp, so
E_{u,delta}(delta) = delta + 2u and E_{v,delta}(delta) = delta + 2v.

Inputs: AEGS, Nagoya Math. J. 259 (2025), Def. 2.3 (T_En);
Sterk, Math. Z. 207 (1991), (4.2.3) (the cusp vector e');
Gritsenko-Hulek-Sankaran, arXiv:0810.1614, section 3.1, Lemma 3.1 (the Eichler transvection).
"""
from sage.all import matrix, vector, ZZ, QQ, block_diagonal_matrix, CartanMatrix

C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
al = [BAS[4 + i] for i in range(8)]
delta = e - f
h = e + f
y4 = -(4 * al[0] + 5 * al[1] + 7 * al[2] + 10 * al[3]
       + 8 * al[4] + 6 * al[5] + 4 * al[6] + 2 * al[7])

def ip(x, y):
    return x * G * y

u = 2 * h + ep - 2 * fp
v = ep + 2 * fp + y4
print("u^2 =", ip(u, u), " v^2 =", ip(v, v), " u.v =", ip(u, v))
print("delta^2 =", ip(delta, delta), " delta.u =", ip(delta, u), " delta.v =", ip(delta, v))

def E(a, z):
    cols = []
    for x in BAS:
        cols.append(vector(ZZ, x + ip(x, a) * z - ip(x, z) * a
                           - QQ(ip(z, z)) / 2 * ip(x, a) * a))
    return matrix(ZZ, N, N, lambda i, j: cols[j][i])

for name, a, other in (("E_{u,delta}", u, v), ("E_{v,delta}", v, u)):
    M = E(a, delta)
    print("%s: M^T G M = G: %s, det = %s" % (name, M.transpose() * G * M == G, M.det()))
    print("   fixes the basis vector:", M * a == a,
          "  image of the other basis vector:", list(M * other))
    print("   image of delta:", list(M * delta), " expected delta + 2*(its basis vector)")
    Ginv = G.inverse()
    triv = True
    for i in range(N):
        y = Ginv * vector(ZZ, [1 if j == i else 0 for j in range(N)])
        d = (y + ip(y, a) * delta - ip(y, delta) * a
             - QQ(ip(delta, delta)) / 2 * ip(y, a) * a) - y
        if any(q.denominator() != 1 for q in d):
            triv = False
    print("   acts trivially on A_{T_En}:", triv)
print("expected delta + 2u:", list(delta + 2 * u), " expected delta + 2v:", list(delta + 2 * v))
