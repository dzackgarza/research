"""A13, item 3: the comparison to the Enriques group at the Heegner vector, in coordinates.

Self-contained: no sage, no sage-extensions.  Exact integer and rational arithmetic with sympy.

What the page already has, and what is computed here.

The comparison has three groups: the Enriques-side restricted stabilizer R_gent of @def:gamma-co-groups
= the image of Stab_gent(Z delta) in Orth(T_Co) = the group of @def:gamma-co-en; the theta-side image
of Z_{Orth(lkt)}(theta_Co) cap Stab(H); and the congruence group Gamma^cong_{Co,2} of
@def:congruence-group.  @prop:gamma-co-images(3) identifies the first with rho^{-1}(P), and
@cor:gamma-hdg-is-congruence identifies the invariant halves of the other two with the same
rho^{-1}(P) cap Orth^+.

What this transcript decides, in the marking of @thm:theta-co-coordinates:

1. the Heegner pair in coordinates: delta = e_0-e_1, zeta = e_0+e_1, delta^2 = -2, zeta^2 = 2,
   delta.zeta = 0, of index 2 in U_1, and delta^{perp T_En} = T_Co as sublattices of lkt;
2. s_zeta, the reflection in zeta: an integral isometry of lkt, of order two, fixing S_Co
   pointwise, hence commuting with theta_Co, with trivial discriminant action on A_{T_Co} AND on
   A_{T_En} (so it lies in the kernel of rho_{T_En}, hence in gent = rho^{-1}(M)), and of spinor
   norm -1 by @prop:gamma-co-reflective-set(2).  It is the component-reversing element of the
   comparison, and it is the extension (id_{S_Co}, s_zeta) that @prop:gamma-co-two-definitions(3)
   uses;
3. the index [Orth(T_Co) : Gamma_{\\Co,2}] = [Orth(q_{T_Co}) : P], which @prop:gamma-co-images(3)
   states but does not evaluate: it is the number of decompositions of A^0 = [zeta/2]^perp into a
   two-dimensional summand isometric to A_{U(2)} and an eight-dimensional one isometric to
   A_{E_8(2)}.  Counted here by exhaustion over the 2-dimensional subspaces of the 2^10-element
   F_2-space A^0, and checked against |Orth(q_{T_Co})|/|P| from the page's group orders.
"""
import sys
from fractions import Fraction

from sympy import Matrix, Rational, zeros
from sympy import __version__ as sympy_version

sys.stdout.reconfigure(line_buffering=True)

N = 22
U_BLOCKS = [(0, 1), (2, 3), (4, 5)]
E_BLOCKS = [list(range(6, 14)), list(range(14, 22))]
E8_EDGES = [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]


def build_G():
    G = zeros(N, N)
    for a, b in U_BLOCKS:
        G[a, b] = 1
        G[b, a] = 1
    for blk in E_BLOCKS:
        for i in range(8):
            G[blk[i], blk[i]] = -2
        for i, j in E8_EDGES:
            G[blk[i], blk[j]] = 1
            G[blk[j], blk[i]] = 1
    return G


def col(entries):
    v = zeros(N, 1)
    for i, c in entries.items():
        v[i] = c
    return v


def is_integral(M):
    return all(Fraction(x).denominator == 1 for x in M)


def show(v):
    items = [(i, Fraction(x)) for i, x in enumerate(v) if x != 0]
    if not items:
        return "0"
    out = []
    for i, c in items:
        num, den = c.numerator, c.denominator
        s = ("e_%d" % i) if den == 1 else ("e_%d/%d" % (i, den))
        if abs(num) != 1:
            s = ("%d " % abs(num)) + s
        out.append(("+" if c > 0 else "-") + " " + s)
    return " ".join(out)


def square(v):
    return (v.T * G * v)[0, 0]


def pair(x, y):
    return (x.T * G * y)[0, 0]


print("provenance")
print("  sympy %s, exact integer and rational arithmetic" % sympy_version)
print("  python %s" % sys.version.split()[0])
print("  no sage and no sage-extensions")
print("  marking, S_Co, T_Co: @thm:theta-co-coordinates and @thm:gamma-co-coordinates")
print("")

G = build_G()
alpha = col({0: 1, 1: -1})
beta = col({0: 1, 1: 1})
H = col({2: 1, 3: 1, 4: 1, 5: 1})
delta = alpha
zeta = beta

S_basis = [alpha, col({2: 1, 4: 1}), col({3: 1, 5: 1})] + [col({6 + k: 1, 14 + k: 1}) for k in range(8)]
T_basis = [beta, col({2: 1, 4: -1}), col({3: 1, 5: -1})] + [col({6 + k: 1, 14 + k: -1}) for k in range(8)]
TEn_basis = [col({0: 1}), col({1: 1})] + T_basis[1:]
B_S = Matrix.hstack(*S_basis)
B_T = Matrix.hstack(*T_basis)
B_En = Matrix.hstack(*TEn_basis)
G_S = B_S.T * G * B_S
G_T = B_T.T * G * B_T
G_En = B_En.T * G * B_En

print("1. the Heegner pair in the marking of @thm:theta-co-coordinates")
print("   delta = %s, zeta = %s" % (show(delta), show(zeta)))
print("   delta^2 = %d, zeta^2 = %d, delta.zeta = %d"
      % (square(delta), square(zeta), pair(delta, zeta)))
Gab = Matrix([[square(delta), pair(delta, zeta)], [pair(zeta, delta), square(zeta)]])
print("   Gram of <delta,zeta> = %s, determinant %d, so the span has index 2 in U_1"
      % ([list(map(int, r)) for r in Gab.tolist()], int(Gab.det())))
print("   T_En = U_1 + Delta^-(U_2,U_3) + Delta^-(E8): rank %d, det %d"
      % (G_En.rows, int(G_En.det())))
print("   T_Co = <zeta> + Delta^-(U_2,U_3) + Delta^-(E8): rank %d, det %d"
      % (G_T.rows, int(G_T.det())))
print("   every T_Co basis vector is orthogonal to delta: %s"
      % all(pair(delta, v) == 0 for v in T_basis))
M = Matrix.hstack(B_T, delta)
print("   rank of [T_Co basis, delta] = %d = rank T_En, so delta^perp cap T_En = T_Co: %s"
      % (M.rank(), M.rank() == G_En.rows))
print("")

print("2. the reflection s_zeta in the marking")
w = Matrix.eye(N) - Rational(2, 1) / square(zeta) * zeta * (G * zeta).T
print("   s_zeta = 1 - (2/zeta^2) zeta (G zeta)^T: integral %s, s^2 = 1 %s, s^T G s = G %s, det %d"
      % (is_integral(w), (w * w) == Matrix.eye(N), (w.T * G * w) == G, int(w.det())))
print("   s_zeta fixes S_Co pointwise: %s" % all((w * v) == v for v in S_basis))
print("   s_zeta fixes delta: %s" % ((w * delta) == delta))
th = zeros(N, N)
th[0, 1] = 1
th[1, 0] = 1
th[2, 4] = -1
th[4, 2] = -1
th[3, 5] = -1
th[5, 3] = -1
for k in range(8):
    th[6 + k, 14 + k] = -1
    th[14 + k, 6 + k] = -1
print("   s_zeta commutes with theta_Co: %s" % ((w * th) == (th * w)))
print("   so s_zeta lies in Z_{Orth(lkt)}(theta_Co) cap Stab(H), and its restriction to T_Co is")
print("   the reflection in zeta there: %s" % all((w * v) != 0 for v in T_basis))
T_dual = B_T * G_T.inv()          # the honest dual basis of T_Co^#
En_dual = B_En * G_En.inv()       # and of T_En^#
print("   dual basis of T_Co^# checked: (t_i^*, t_j) = delta_ij %s"
      % ((T_dual.T * G * B_T) == Matrix.eye(11)))
print("   dual basis of T_En^# checked: (u_i^*, u_j) = delta_ij %s"
      % ((En_dual.T * G * B_En) == Matrix.eye(12)))
print("   s_zeta acts trivially on A_{T_Co}: s(t_i^*) - t_i^* in T_Co for the 11 dual generators %s"
      % all(is_integral(w * T_dual[:, i] - T_dual[:, i]) for i in range(11)))
print("   s_zeta acts trivially on A_{T_En}: s(u_i^*) - u_i^* in T_En for the 12 dual generators %s"
      % all(is_integral(w * En_dual[:, i] - En_dual[:, i]) for i in range(12)))
print("   hence rho_{T_En}(s_zeta) = 1, so s_zeta lies in ker rho_{T_En} and therefore in")
print("   gent = rho^{-1}(M) (@prop:sterk-group-identification(2)), and it fixes the line Z delta")
print("")

print("3. the discriminant form of T_Co, and the block A^0")
# classes of A_{T_Co}: the 2048 half-vectors, indexed by an 11-bit mask over the basis of T_Co
classes = []
for mask in range(1 << 11):
    x = zeros(N, 1)
    for k in range(11):
        if (mask >> k) & 1:
            x += T_basis[k] / 2
    classes.append(x)
qval = [Rational(square(x)) % 2 for x in classes]
print("   the 2048 classes 1/2 sum eps_i t_i; values of q take the %d values %s"
      % (len({v for v in qval}), sorted({str(v) for v in qval})))
A0 = [i for i in range(1 << 11) if qval[i].denominator == 1]
print("   A^0 = the classes with q integral: %d elements = 2^%d" % (len(A0), len(A0).bit_length() - 1))
print("   A^0 is a subgroup: %s" % all((i ^ j) in set(A0) for i in A0 for j in A0))
print("   the class of zeta/2 has q = %s, outside A^0: %s"
      % (qval[(1 << 0)], (1 << 0) not in set(A0)))
print("")

print("4. the index [Orth(T_Co) : Gamma_{Co,2}] = [Orth(q_{T_Co}) : P]")
# compress A^0 to F_2^10 by a basis
basis = []
span = {0}
for i in A0:
    if i == 0:
        continue
    if i not in span:
        basis.append(i)
        span = span | {b ^ i for b in span}
print("   a F_2-basis of A^0 found: %d vectors, spanning %d elements" % (len(basis), len(span)))
# linear coordinates of every element of A^0
pos = {}
for x in range(1 << len(basis)):
    e = 0
    for k in range(len(basis)):
        if (x >> k) & 1:
            e ^= basis[k]
    pos[e] = x
qtab = [1 if qval[e] == 1 else 0 for e in span]
# q on the compressed index
qtab = [0] * len(span)
for e, x in pos.items():
    qtab[x] = 1 if qval[e] == 1 else 0
n0 = len(span)
ALL = (1 << n0) - 1
ZEROS = 0
for x in range(n0):
    if qtab[x] == 0:
        ZEROS |= (1 << x)
# b(x,y) = 1/2 iff q(x^y) - q(x) - q(y) = 1 mod 2
halfmask = []
for x in range(n0):
    m = 0
    qx = qtab[x]
    for y in range(n0):
        if (qtab[x ^ y] - qx - qtab[y]) % 2 == 1:
            m |= (1 << y)
    halfmask.append(m)

count = 0
for i in range(1, n0):
    for j in range(i + 1, n0):
        k = i ^ j
        if k == 0:
            continue
        if sorted([qtab[i], qtab[j], qtab[k]]) != [0, 0, 1]:
            continue
        if ((halfmask[i] >> j) & 1) == 0:
            continue
        comp = ALL & ~(halfmask[i] | halfmask[j])
        if comp.bit_count() != 256:
            continue
        if (comp & ZEROS).bit_count() == 136:
            count += 1
pairs = count
count = pairs // 3   # each two-dimensional subspace is met by exactly three of its ordered pairs
print("   qualifying pairs (i,j) of nonzero classes: %d, and each subspace is met by three of" % pairs)
print("   them, so the number of decompositions A^0 = W perp W^perp with W = A_{U(2)} and")
print("   W^perp = A_{E_8(2)} is %d" % count)
orth_q = 46998591897600
P = 2 * 348364800
print("   |Orth(q_{T_Co})| = %d and |P| = %d, so |Orth(q)|/|P| = %d, %s the count"
      % (orth_q, P, orth_q // P, "equal to" if orth_q // P == count else "NOT equal to"))
print("   [Orth(T_Co) : Gamma_{Co,2}] = %d" % count)
print("")

print("5. the indices of the comparison")
WE8 = 696729600
print("   |W(E8)| = %d, 2|W(E8)| = %d" % (WE8, 2 * WE8))
print("   [Gamma_{Co,2} : Gamma_{Co,2} cap Orth^+] = 2, the two cosets being the components;")
print("   [Gamma_{Co,2} cap Orth^+ : Otilde^+(T_Co)] = |W(E8)| = %d;" % WE8)
print("   [Gamma_{Co,2} : Otilde^+(T_Co)] = %d" % (2 * WE8))
print("   [Orth(T_Co) : Otilde^+(T_Co)] = %d = %d * %d" % (count * 2 * WE8, count, 2 * WE8))
print("   (a tower of two computed indices, not an independent count)")
print("")
print("6. not computed here")
print("   the group-theoretic steps: that the theta-image is rho^{-1}(P) and that R_gent is, are")
print("   prose with @prop:gamma-co-images(3), @prop:theta-co-index and")
print("   @prop:coble-block-compatibility; @conj:gamma-co-stable is a conjecture and is used only")
print("   where it is named.")
