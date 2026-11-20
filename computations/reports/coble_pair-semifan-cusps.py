"""The generalized Coxeter semifan of the Coble stable pairs at each 0-cusp of F_Co,2.

All geometric input is read from the committed transcript
    computations/reports/coble_enriques-white-root-facets-run.txt
(the exact wall Gram matrices of AEGS Figures 7--8 and the complete induced facet
angle tables at each of their white nodes; sources Sterk (1991), Props. 4.3.5--4.3.9,
printed pp. 19--24, and AEGS, Nagoya Math. J. 259 (2025), Figures 7--8, printed
pp. 594--595), and the relevance marking from
    computations/reports/coble_irrelevant-marking-face-run.txt
(printed labels of the irrelevant roots at cusps 3, 4, 5, folded from AEGS Figure 5);
at cusp 2 the single irrelevant root, the interior spur, is thm:coble-restricted-semifan.

This script computes, with ZZ/QQ arithmetic only:
  A. delta = e - f, T_Co = delta^perp, and the discriminant class of eta_k/2 for the
     five Enriques 0-cusps; hence the matching of the four 0-cusps of F_Co,2 with
     the cusps 2,3,4,5 and the exclusion of cusp 1;
  B. at each Coble 0-cusp the restricted chamber C_delta = C cap delta^perp at the
     white node delta: the projected wall Gram matrix, the induced bond graph, the
     coincident walls, the inertia, the inherited relevance, the Gram and inertia of
     W_irr, and the maximal affine subdiagrams with the AEGS Lemma 5.7 test;
  C. hypotheses (B2), (B3), (B4), (B5) of thm:semifan-restriction Case B, and (B1);
  D. the volume of each restricted chamber, by the criterion of thm:coxeter-polytope-volume:
     the extreme rays of the cone {(nu_i,x) >= 0}, enumerated over the eight-subsets of the
     walls (complete because the walls span K, so the cone is pointed), each classified
     ordinary (v^2 > 0), ideal (v^2 = 0) or outside (v^2 < 0).

Run:  python3 computations/reports/coble_pair-semifan-cusps.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
import re
from pathlib import Path

import sympy as sp
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

REPO = Path(__file__).resolve().parents[2]
RUN = REPO / "computations/reports/coble_enriques-white-root-facets-run.txt"

# -------------------------------------------------------------- parse the record
text = RUN.read_text(encoding="utf-8").splitlines()
GRAM, DELTA, ANGLE, MULTI = {}, {}, {}, {}
cusp = node = None
i = 0
while i < len(text):
    ln = text[i]
    m = re.match(r"=== cusp (\d+); eta = \[([^\]]+)\]", ln)
    if m:
        cusp = int(m.group(1))
        GRAM[cusp] = []
        ANGLE[cusp] = {}
        i += 1
        while not text[i].startswith("wall Gram matrix"):
            i += 1
        i += 1
        while i < len(text) and text[i].strip().startswith("["):
            GRAM[cusp].append([int(x) for x in text[i].strip().strip("[]").split()])
            i += 1
        continue
    m = re.match(r"-- white node (\d+) \(printed root r(\d+)\), delta = \[([^\]]+)\]", ln)
    if m:
        node = int(m.group(1))
        DELTA[(cusp, node)] = [int(x) for x in m.group(3).split(",")]
        ANGLE[(cusp, node)] = {}
        i += 1
        continue
    m = re.match(r"\s+facet angle \((\d+),(\d+)\): cos=([^,]+), (.*)", ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        tag = m.group(4).strip()
        ANGLE[(cusp, node)][(a, b)] = ('parallel' if tag == 'parallel'
                                       else 'no-intersection' if tag == 'no-intersection'
                                       else tag)
        i += 1
        continue
    m = re.match(r"\s+angle multiset: (.*)", ln)
    if m:
        MULTI[(cusp, node)] = m.group(1)
    i += 1

# ---------------------------------------------------------------- the T_En form
# T_En = U(e,f) + U(2)(e',f') + E8(2)(a_1..a_8);  E8 in Bourbaki numbering:
# edges 1-3, 2-4, 3-4, 4-5, 5-6, 6-7, 7-8.  Cross-checked below against
# det T_En = 1024 and det(delta^perp) = -2048.
N = 12
E8_EDGES = {(1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)}
G = [[0] * N for _ in range(N)]
G[0][1] = G[1][0] = 1
G[2][3] = G[3][2] = 2
for a in range(8):
    for b in range(8):
        if a == b:
            G[4 + a][4 + b] = -4
        elif ((a + 1, b + 1) in E8_EDGES or (b + 1, a + 1) in E8_EDGES):
            G[4 + a][4 + b] = 2

def unit(t):
    return [1 if k == t else 0 for k in range(N)]

def dot(x, y):
    return sum(F(x[a]) * G[a][b] * F(y[b]) for a in range(N) for b in range(N))

def lin(*pairs):
    return [sum(F(c) * F(w[k]) for c, w in pairs) for k in range(N)]

def inertia(M):
    n = len(M)
    A = [[F(x) for x in row] for row in M]
    idx = list(range(n)); pos = neg = 0
    while idx:
        piv = next((a for a in idx if A[a][a] != 0), None)
        if piv is not None:
            p = A[piv][piv]
            pos += 1 if p > 0 else 0
            neg += 1 if p < 0 else 0
            for a in idx:
                if a == piv:
                    continue
                fac = A[a][piv] / p
                for b in idx:
                    if b != piv:
                        A[a][b] -= fac * A[piv][b]
            idx = [a for a in idx if a != piv]
        else:
            pr = next(((a, b) for a in idx for b in idx if a < b and A[a][b] != 0), None)
            if pr is None:
                break
            i0, j0 = pr
            c = A[i0][j0]
            pos += 1; neg += 1
            rest = [a for a in idx if a not in (i0, j0)]
            for a in rest:
                for b in rest:
                    A[a][b] -= A[a][i0] * A[j0][b] / c + A[a][j0] * A[i0][b] / c
            idx = rest
    return pos, neg, len(idx)

def det_int(M):
    return int(Matrix(M).det())

E8 = [unit(4 + t) for t in range(8)]
e, f, ep, fp = unit(0), unit(1), unit(2), unit(3)
delta = lin((1, e), (-1, f))
ETA = {1: e, 2: ep}
print("The generalized Coxeter semifan of the Coble stable pairs at each 0-cusp of F_Co,2")
print()
print("=== part A. the Coble root, T_Co, and the four 0-cusps")
print("delta = e - f : delta^2 = %d, div_T_En(delta) = %d"
      % (dot(delta, delta), gcd(*[abs(int(dot(delta, unit(t)))) for t in range(N)])))
bas = [lin((1, e), (1, f)), ep, fp] + E8
GC = [[dot(x, y) for y in bas] for x in bas]
print("T_En: det %d ; delta^perp = {e+f, e', f', a_1..a_8}: rank %d, det %d, signature %s"
      % (det_int([[dot(unit(a), unit(b)) for b in range(N)] for a in range(N)]),
         len(bas), det_int(GC), inertia(GC)[:2]))
print("   -> T_Co = delta^perp has the invariants of (11,11,1): rank 11, det -2048, signature (2,9)")

for k in (1, 2, 3, 4, 5):
    eta = [F(x) for x in [None]] if False else None
    # the eta coordinates are printed in the transcript; read them back
    m = re.search(r"=== cusp %d; eta = \[([^\]]+)\]" % k, "\n".join(text))
    ETA[k] = [int(x) for x in m.group(1).split(",")]
print()
print("the discriminant class [eta/2] in A_{T_En}, as its canonical {0,1/2}^12 representative,")
print("and the orbit of prop:coble-cong-point-stabilizer(2) it belongs to:")
def cls(k):
    out = []
    for t in range(N):
        h = F(ETA[k][t], 2)
        out.append(h - int(h) if h >= 0 else h - int(h) + 1)
    return out
ORB = {}
for k in (1, 2, 3, 4, 5):
    c = cls(k)
    U = (c[0] != 0, c[1] != 0)
    u = (c[2] != 0, c[3] != 0)
    Etriv = not any(c[4 + t] != 0 for t in range(8))
    if any(U):
        name = "divisibility 1 -- no class in A_{T_En} (not a Coble cusp)"
    elif not any(u) and Etriv:
        name = "the zero class"
    elif u in [(True, False), (False, True)] and Etriv:
        name = "O_2 (2 classes)"
    elif not any(u) and not Etriv:
        name = "O_135 (135 classes)"
    elif u in [(True, False), (False, True)] and not Etriv:
        name = "O_270 (270 classes)"
    elif u == (True, True) and not Etriv:
        name = "O_120 (120 classes)"
    else:
        name = "UNCLASSIFIED"
    ORB[k] = name
    print("  cusp %d: U %s, U(2) %s, E8(2) trivial %s  ->  %s" % (k, U, u, Etriv, name))
print()
print("the four Coble 0-cusps, one over each divisibility-2 Enriques cusp:")
for k in (2, 3, 4, 5):
    print("  Sterk cusp %d  <->  %s" % (k, ORB[k]))

# ------------------------------------------------------------------- part B
DELTA_NODE = {2: 10, 3: 5, 4: 9, 5: 11}
# irrelevant figure-order nodes; cusps 3,4,5 from coble_irrelevant-marking-face-run.txt
# through the printed-label matching of the transcript, cusp 2 from thm:coble-restricted-semifan
IRR = {2: {4}, 3: {4, 9, 11}, 4: {7, 8}, 5: {9, 10, 11, 12, 13, 14}}
print()
print("=== part B. the restricted chamber at each Coble 0-cusp")
summary = {}
CHAMBER = {}
VOL = {}
for k in (2, 3, 4, 5):
    Gm = GRAM[k]; MM = len(Gm)
    dn = DELTA_NODE[k]
    ang = ANGLE[(k, dn)]
    nodes = [t + 1 for t in range(MM) if t + 1 != dn]
    # projected normals nu_i = r_i + (r_i,delta)/2 * delta, so
    # (nu_i,nu_j) = (r_i,r_j) + (r_i,delta)(r_j,delta)/2   [delta^2 = -2]
    def proj(a, b):
        return F(Gm[a - 1][b - 1] + F(Gm[a - 1][dn - 1] * Gm[b - 1][dn - 1], 2))
    sq = {t: proj(t, t) for t in nodes}
    for t in nodes:
        assert sq[t].denominator == 1, (k, t, sq[t])
    def label(a, b):
        if proj(a, b) == 0:
            return 'zero'
        t = F(proj(a, b) * proj(a, b), sq[a] * sq[b])
        if t == 1:
            return 'parallel' if proj(a, b) > 0 else 'no-intersection'
        return {F(1, 4): 'pi/3', F(1, 2): 'pi/4'}.get(t, 'NO-INTERSECTION(%s)' % t)
    # cross-check against the record's own angle table
    bad = []
    for a in range(len(nodes)):
        for b in range(a + 1, len(nodes)):
            x, y = nodes[a], nodes[b]
            rec = ang.get((x, y))
            mine = label(x, y)
            if rec is None:
                if mine not in ('zero',):
                    bad.append((x, y, 'unlisted', mine))
            elif rec == 'pi/2' and mine == 'zero':
                pass
            elif rec != mine and not (rec == 'no-intersection' and mine.startswith('NO-INTERSECTION')):
                bad.append((x, y, rec, mine))
    par = [(a, b) for a in nodes for b in nodes if a < b and label(a, b) == 'parallel']
    parent = {t: t for t in nodes}
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in par:
        parent[find(a)] = find(b)
    classes = {}
    for t in nodes:
        classes.setdefault(find(t), []).append(t)
    reps = sorted(min(v) for v in classes.values())
    irr = sorted(t for t in nodes if t in IRR[k])
    mixed = [t for t in irr if any(o not in IRR[k] for o in classes[find(t)])]
    canon = sorted({min(classes[find(t)]) for t in irr})
    Pi = [[proj(a, b) for b in canon] for a in canon]
    iner_i = inertia(Pi) if canon else (0, 0, 0)
    print()
    print("-- the 0-cusp over Sterk cusp %d (%s)" % (k, ORB[k]))
    print("   eta = %s" % ETA[k])
    print("   the white node is figure node %d ; delta = %s" % (dn, DELTA[(k, dn)]))
    print("   pairings (r_i,delta) nonzero only for %s, with values %s"
          % ([t for t in nodes if Gm[t - 1][dn - 1] != 0],
             [Gm[t - 1][dn - 1] for t in nodes if Gm[t - 1][dn - 1] != 0]))
    print("   restricted roots: %d ; squares %s" % (len(nodes), {t: int(sq[t]) for t in nodes}))
    print("   coincident walls (induced parallel pairs): %s" % par)
    print("   -> %d distinct walls: %s" % (len(reps), reps))
    print("   induced bonds: %s" % {(a, b): label(a, b) for a in nodes for b in nodes
                                    if a < b and label(a, b) != 'zero'})
    print("   no-intersection pairs: %s" % [(a, b) for a in nodes for b in nodes
                                            if a < b and label(a, b).startswith('NO-INTERSECTION')])
    print("   inertia of the restricted wall Gram (pos, neg, zero): %s" % (inertia(
        [[proj(a, b) for b in reps] for a in reps]),))
    print("   cross-check against the record's angle table: %s" % ("agrees" if not bad else bad))
    print("   irrelevant roots %s -> %d distinct irrelevant walls %s ; mixed walls %s"
          % (irr, len(canon), canon, mixed))
    print("   (B1) the cut mirror delta is relevant: %s" % (dn not in IRR[k]))
    print("   (B5) no restricted wall carries two relevances: %s" % (not mixed))
    print("   W_irr: %d generators, squares %s, pairings %s, inertia %s -> finite: %s"
          % (len(canon), [int(proj(t, t)) for t in canon],
             {(a, b): int(proj(a, b)) for a in canon for b in canon if a < b and proj(a, b) != 0},
             iner_i, iner_i[0] == 0 and iner_i[2] == 0))
    # maximal affine subdiagrams of the chamber on the distinct walls
    Nb = len(reps)
    adj = {a: set() for a in range(Nb)}
    for a in range(Nb):
        for b in range(a + 1, Nb):
            if proj(reps[a], reps[b]) != 0:
                adj[a].add(b); adj[b].add(a)
    Pd = [[proj(a, b) for b in reps] for a in reps]
    aff = []
    for r in range(1, Nb + 1):
        for S in combinations(range(Nb), r):
            p_, n_, z_ = inertia([[Pd[a][b] for b in S] for a in S])
            if p_ == 0 and z_ == 1:
                aff.append(frozenset(S))
    maxaff = [S for S in aff if not any(S < T for T in aff)]
    irrset = {reps.index(t) for t in canon}
    nbad, badlist = 0, []
    for S in maxaff:
        seen, comps = set(), []
        for a in S:
            if a in seen:
                continue
            comp, st = set(), [a]
            while st:
                x = st.pop()
                if x in comp:
                    continue
                comp.add(x)
                st += [y for y in adj[x] & S if y not in comp]
            seen |= comp
            comps.append(sorted(reps[z] for z in comp))
        badc = [c for c in comps if all(reps.index(x) in irrset for x in c)]
        if badc:
            nbad += 1
            badlist.append((sorted(reps[a] for a in S), badc))
    print("   maximal affine subdiagrams: %d ; with a connected component of irrelevant" % len(maxaff))
    print("   walls only: %d" % nbad)
    for S, badc in badlist:
        print("      %s -> %s" % (S, badc))
    summary[k] = (len(nodes), len(reps), iner_i, iner_i[0] == 0 and iner_i[2] == 0,
                  dn not in IRR[k], not mixed, len(maxaff), nbad)
    CHAMBER[k] = (reps, Pd)
print()
print("=== summary")
print("cusp roots walls  W_irr inertia  W_irr finite  delta relevant  (B5)  max-affine  irr-only-comp")
for k in (2, 3, 4, 5):
    r, w, ii, fin, rel, b5, ma, nb = summary[k]
    print("  %d    %2d    %2d   %-12s %-13s %-14s %-5s %-10s  %d" % (k, r, w, ii, fin, rel, b5, ma, nb))
print()
print("=== part D. the volume of the restricted chamber")
print("thm:coxeter-polytope-volume(3): the polytope has infinite volume if and only if its")
print("closure in the projective model has a vertex outside the closed hyperbolic space, and by")
print("(1) it has finite volume if and only if the closure is the convex hull of finitely many")
print("of its ordinary and ideal vertices.  The vertices are the extreme rays of the cone")
print("C = {x : (nu_i,x) >= 0}; since the walls span K, C is pointed, and every extreme ray is")
print("cut out by an independent set of dim K - 1 = 8 walls, so the enumeration over 8-subsets")
print("is complete.  A ray is ordinary when v^2 > 0, ideal when v^2 = 0, and outside when v^2 < 0.")


def rank_of(M):
    return Matrix(M).rank()

for k in (2, 3, 4, 5):
    reps, Pd = CHAMBER[k]
    n = len(reps)
    basis = []
    for i in range(n):
        cand = basis + [i]
        if rank_of([[Pd[a][b] for b in cand] for a in cand]) == len(cand):
            basis = cand
    assert len(basis) == 9, (k, len(basis))
    GB = [[Pd[a][b] for b in basis] for a in basis]
    Grow = [[Pd[i][b] for b in basis] for i in range(n)]
    rays = {}
    for S in combinations(range(n), 8):
        A = Matrix([[sp.Rational(Grow[i][j]) for j in range(9)] for i in S])
        if A.rank() != 8:
            continue
        ns = A.nullspace()
        if len(ns) != 1:
            continue
        v = [sp.Rational(x) for x in ns[0]]
        den = 1
        for x in v:
            den = sp.ilcm(den, int(sp.denom(x)))
        v = [int(x * den) for x in v]
        if not all(sum(F(Grow[j][t]) * v[t] for t in range(9)) >= 0 for j in range(n)):
            continue
        key = tuple(v)
        dup = False
        for kk in rays:
            if all(kk[t] * key[0] == key[t] * kk[0] for t in range(9)):
                dup = True
                break
        if not dup:
            rays[key] = sum(F(v[a]) * GB[a][b] * F(v[b]) for a in range(9) for b in range(9))
    kinds = {'ordinary': 0, 'ideal': 0, 'outside': 0}
    outside = []
    for v, nrm in rays.items():
        if nrm > 0:
            kinds['ordinary'] += 1
        elif nrm == 0:
            kinds['ideal'] += 1
        else:
            kinds['outside'] += 1
            outside.append((v, nrm))
    print()
    print("-- over Sterk cusp %d: %d distinct walls, %d extreme rays" % (k, n, len(rays)))
    print("   ordinary (v^2>0): %d ; ideal (v^2=0): %d ; outside (v^2<0): %d"
          % (kinds['ordinary'], kinds['ideal'], kinds['outside']))
    print("   finite volume: %s" % (kinds['outside'] == 0))
    for v, nrm in outside:
        print("      an extreme ray outside the closed hyperbolic space: v = %s with v^2 = %s" % (v, nrm))
    VOL[k] = (n, len(rays), kinds, kinds['outside'] == 0)
print()
print("=== part D summary")
print("cusp  walls  extreme rays  ordinary  ideal  outside  finite volume")
for k in (2, 3, 4, 5):
    n, nr, kinds, fin = VOL[k]
    print("  %d     %2d       %2d          %2d       %2d     %2d       %s"
          % (k, n, nr, kinds['ordinary'], kinds['ideal'], kinds['outside'], fin))
print("PYEXIT=0")
