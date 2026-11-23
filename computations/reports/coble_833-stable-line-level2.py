"""research#833 (A24-O2): the level-2 membership laws of the stable-group line stabilizer.

The page (writing/coble/lattices-and-moduli/integral-line-and-plane-lifting.md, the section "The
stable-group line stabilizer") claims exactly four things, and this script checks them:

1. K = v^perp/v = U perp D with U = <e,f>, D = <-1>^7, and Otilde(T_Co) = ker rho = {g = id mod 2B}.
   For k in K_ev the transvection E(e,k) is an integral isometry of K (extended by the identity on
   P); it is congruent to the identity modulo 2K if and only if k is in 2K.  Boundary case:
   k = d_1 + d_2 is in K_ev but not in 2K, and E(e, d_1+d_2) is an integral isometry which is *not*
   congruent to the identity modulo 2K.

2. The 35 elements r_{d_j}, t_K(e,2d_j), t_K(f,2d_j), r_{e+d_j}, r_{f+d_j} are integral isometries
   of K congruent to the identity modulo 2K; of them 21 fix the line Ze (the seven r_{d_j}, the
   seven t_K(e,2d_j), the seven r_{e+d_j}), which is the set of those that act trivially on the
   plane P = <v,e> through id_P perp phi.

3. E(e,k) is additive in k: E(e,k_1)E(e,k_2) = E(e,k_1+k_2) exactly, so the nine transvections at a
   Z-basis of K_ev generate the whole acting group {E(e,k) : k in K_ev} of the parabolic.

4. The central shear sigma = E_{e_1,e_2} of the *plane* parabolic is not congruent to the identity
   modulo 2B, while sigma^2 is: this is why the level-2 unipotent radical is 2K_ev and not K_ev, and
   it is the exact point at which the plane family of thm:o2-plane-family leaves the stable group.

5. The necessary condition of lem:o2-level-four.  Gamma_K(2)/Gamma_K(4) injects into
   {A in Mat_9(F_2) : A^t Gbar + Gbar A = 0}, of dimension 45; the 35 elements above span 21 of it,
   and the further element r_{e+d_1+d_2} r_{e+d_1-d_2} of Gamma_K(2) has its class inside that span.
   So this datum neither proves nor refutes completeness modulo four, and the page says so.

Usage: python3 computations/reports/coble_833-stable-line-level2.py
"""
n = 9
G = [[0] * n for _ in range(n)]
G[0][1] = G[1][0] = 1
for i in range(2, n):
    G[i][i] = -1
Gb = [[G[i][j] % 2 for j in range(n)] for i in range(n)]
e = [1, 0] + [0] * 7
f = [0, 1] + [0] * 7
ds = [[0, 0] + [1 if k == j else 0 for k in range(7)] for j in range(7)]


def dot(x, y, Gm=None):
    Gm = Gm or G
    m = len(Gm)
    return sum(x[i] * Gm[i][j] * y[j] for i in range(m) for j in range(m))


def frommap(fn, m=None):
    m = m or n
    M = [[0] * m for _ in range(m)]
    for j in range(m):
        x = [0] * m
        x[j] = 1
        y = fn(x)
        for i in range(m):
            M[i][j] = y[i]
    return M


def isom(M, Gm=None):
    m = len(M)
    Gm = Gm or G
    return all(sum(M[i][a] * Gm[i][j] * M[j][b] for i in range(m) for j in range(m)) == Gm[a][b]
               for a in range(m) for b in range(m))


def cong2(M):
    m = len(M)
    return all((M[i][j] - (1 if i == j else 0)) % 2 == 0 for i in range(m) for j in range(m))


def fixes_e(M):
    return all(M[i][0] == (1 if i == 0 else 0) for i in range(len(M)))


def refl(w, Gm=None):
    w2 = dot(w, w, Gm)
    assert w2 in (1, -1, 2, -2), w2
    return lambda x: [x[i] - 2 * dot(x, w, Gm) * w[i] // w2 for i in range(len(x))]


def eich(u, k, Gm=None):
    kk = dot(k, k, Gm)
    assert kk % 2 == 0 and dot(u, k, Gm) == 0
    return lambda x: [x[i] - dot(x, k, Gm) * u[i] + dot(x, u, Gm) * k[i]
                      - (kk // 2) * dot(x, u, Gm) * u[i] for i in range(len(x))]


print("=== 1. the integrality and level-2 boundary for E(e,k), k in K_ev")
for name, k in (("k = d_1 + d_2 (K_ev, not 2K)", [ds[0][i] + ds[1][i] for i in range(n)]),
                ("k = 2d_1 (in 2K)", [2 * x for x in ds[0]])):
    M = frommap(eich(e, k))
    print("   %-30s integral isometry %s | = id mod 2K %s | fixes Ze %s"
          % (name, isom(M), cong2(M), fixes_e(M)))

print()
print("=== 2. the 35-element level-2 family")
fam = {}
for j, d in enumerate(ds):
    fam["r_d%d" % (j + 1)] = refl(d)
    fam["t_K(e,2d%d)" % (j + 1)] = eich(e, [2 * x for x in d])
    fam["t_K(f,2d%d)" % (j + 1)] = eich(f, [2 * x for x in d])
    fam["r_(e+d%d)" % (j + 1)] = refl([e[i] + d[i] for i in range(n)])
    fam["r_(f+d%d)" % (j + 1)] = refl([f[i] + d[i] for i in range(n)])
mats = {k: frommap(v) for k, v in fam.items()}
print("   size", len(mats), "| all integral isometries", all(isom(M) for M in mats.values()),
      "| all = id mod 2K", all(cong2(M) for M in mats.values()))
print("   those fixing the line Ze:", sum(1 for M in mats.values() if fixes_e(M)),
      "(the seven r_d, the seven t_K(e,2d), the seven r_(e+d))")

print()
print("=== 3. additivity in the second argument")
k1 = [2 * x for x in ds[0]]
k2 = [2 * x for x in ds[1]]
A1, A2 = frommap(eich(e, k1)), frommap(eich(e, k2))
A12 = frommap(eich(e, [k1[i] + k2[i] for i in range(n)]))
prod = [[sum(A1[i][t] * A2[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
print("   E(e,2d_1)E(e,2d_2) = E(e,2d_1+2d_2) exactly:", prod == A12)

print()
print("=== 4. the central shear sigma of the plane parabolic")
m = 11
Gp = [[0] * m for _ in range(m)]
Gp[0][1] = Gp[1][0] = 1
Gp[2][3] = Gp[3][2] = 1
for i in range(4, m):
    Gp[i][i] = -1
u = [0] * m
u[0] = 1
kk = [0] * m
kk[2] = 1
S = frommap(eich(u, kk, Gp), m)
S2 = [[sum(S[i][t] * S[t][j] for t in range(m)) for j in range(m)] for i in range(m)]
print("   sigma = id mod 2B:", cong2(S), "| sigma^2 = id mod 2B:", cong2(S2),
      "| both integral isometries:", isom(S, Gp) and isom(S2, Gp))

print()
print("=== 5. the level-4 datum")


def gf2_rank(rows):
    basis = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in basis:
                row ^= basis[p]
            else:
                basis[p] = row
                break
    return len(basis)


def inv(M):
    M = [[M[i][j] % 2 for j in range(n)] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c] % 2)
        M[c], M[p] = M[p], M[c]
        for i in range(n):
            if i != c and M[i][c] % 2:
                M[i] = [(x + y) % 2 for x, y in zip(M[i], M[c])]
    return [r[n:] for r in M]


Gbi = inv(Gb)
amb = []
for a in range(n):
    for b in range(a, n):
        Sm = [[0] * n for _ in range(n)]
        Sm[a][b] = Sm[b][a] = 1
        A = [[sum(Gbi[i][t] * Sm[t][j] for t in range(n)) % 2 for j in range(n)] for i in range(n)]
        amb.append(sum(A[i][j] << (i * n + j) for i in range(n) for j in range(n)))
rows = []
for M in mats.values():
    A = [[(M[i][j] - (1 if i == j else 0)) // 2 % 2 for j in range(n)] for i in range(n)]
    rows.append(sum(A[i][j] << (i * n + j) for i in range(n) for j in range(n)))
print("   dim {A : A^t Gbar + Gbar A = 0} =", gf2_rank(amb),
      "| dim spanned by the 35 elements =", gf2_rank(rows))
v = [e[i] + ds[0][i] + ds[1][i] for i in range(n)]
w = [e[i] + ds[0][i] - ds[1][i] for i in range(n)]
Mg = frommap(lambda x: refl(v)(refl(w)(x)))
A = [[(Mg[i][j] - (1 if i == j else 0)) // 2 % 2 for j in range(n)] for i in range(n)]
row = sum(A[i][j] << (i * n + j) for i in range(n) for j in range(n))
y, basis = row, {}
for x in rows:
    while x:
        p = x.bit_length() - 1
        if p in basis:
            x ^= basis[p]
        else:
            basis[p] = x
            break
while y:
    p = y.bit_length() - 1
    if p in basis:
        y ^= basis[p]
    else:
        break
print("   witness r_(e+d1+d2) r_(e+d1-d2): isometry", isom(Mg), "| = id mod 2K", cong2(Mg),
      "| class inside the span:", y == 0)
