"""#760: the pruned search for a Gamma_Co,2-transporter of the class of 12 to that of 13, to depth 16.

The pair (12,13) at cusp 5 is decided by whether some u in Gamma_Co,2 keeps the line ZZ eta_5 and
carries the class of r12 to that of r13 in K_5.  This record searches for u = g * s, where g is the raw
12<->13 witness restricted to T_Co (it keeps the line and moves the class, and is outside Gamma_Co,2)
and s ranges over words in the 52 verified generators of Stab_{O(T_Co)}(r12).

Both cheap conditions depend on s alone --- g preserves the line and g r12 = r13, so g*s keeps the line
exactly when s does, and carries the class exactly when s fixes the class of r12 --- so the search
prunes instead of enumerating: only words satisfying both are extended, and membership in Gamma_Co,2 is
tested only for those, by the exact point test on the 2048 classes of A_{T_Co}.

Result, to depth 16: 6, 23, 77, 233, 645, 1632, 3738, 7602, 13730, 22088, 31514, 40370, 46918, 50404,
51617, 51830 survivors, and NONE of them lands in Gamma_Co,2.  The survivor counts saturate --- the
last three differ by 1,213 and 213 --- but saturation is NOT exhaustion: a word can satisfy both
conditions while a prefix does not, so the search cannot be read as an enumeration of the subgroup, and
this is a bound and not a decision.  The negative needs a generating set of
Gamma_Co,2 cap Stab_O(r12) cap Stab_O(Z eta_5); the positive would need one such s, and 51,830 verified
candidates say it is not a short word in the generators the provider supplies.

An earlier run of the same search was killed at depth 10 (exit 137) because it deduplicated against a
global set of 372,899 integer matrices; deduplicating per level fixes it, since the frontier is three
orders of magnitude smaller than the union of the levels.

A second variant does not return.  Feeding ``root_class_orbits`` the generators of Gamma_Co,2 that
preserve the line -- which by sage-extensions#312's membership criterion is admissible input, since
rho(K_v) is trivial at Sterk's cusps -- was run for 17 min 33 s of elapsed time and 16 min 39 s of CPU
at a resident size of 7.5 GB without printing a result, and was stopped: this VM had 1 GB available and
carries other projects' jobs.  So a larger acting family does not make the call return at this size;
the cost is in the orbit computation over O(K_5), not in the family.

    usage: python3 computations/reports/coble_760-transporter-pruned-search.py   (~8 min, needs .scratch/w760/tco_stab.pkl)
"""

import sys, pickle, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%7.1fs]" % (time.time()-t0), *a, flush=True)
from sage.all import ZZ, QQ, matrix, vector, identity_matrix, block_diagonal_matrix, CartanMatrix

D = pickle.load(open('/repo/.scratch/w760/tco_stab.pkl', 'rb'))
labels = D["labels"]; NC = len(labels)
Gc = matrix(ZZ, D["Gc"]); Ms = [matrix(ZZ, NC, NC, g) for g in D["gens"]]
co = dict(zip(labels, range(NC)))
def vec(d): return vector(ZZ, [d.get(l, 0) for l in labels])
r12 = vec({"h": 1, "ep": 3, "fp": 3, "a1": -2, "a2": 1, "a3": 2, "a4": 2, "a5": 1})
r13 = vec({"h": 1, "ep": 3, "fp": 4, "a1": -2, "a2": 2, "a3": 3, "a4": 4, "a5": 3, "a6": 2, "a7": 1})
src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
ab0 = [int(x) for x in vector(ZZ, abar[0])][4:12]
eta = vec(dict({"h": 2}, **{"a%d" % (i+1): ab0[i] for i in range(8) if ab0[i]}))
assert eta*Gc*eta == 0
S, U, V = Gc.smith_form(); d = [int(S[i,i]) for i in range(NC)]
Uq, Uinv = matrix(QQ, U), matrix(QQ, matrix(ZZ, U).inverse())
def key(a):
    b = Uq*vector(QQ, a); return tuple(0 if d[i]==1 else int(b[i]) % d[i] for i in range(NC))
def lift(k): return vector(ZZ, Uinv*vector(QQ, k))
zero = tuple(0 for _ in range(NC))
def cls_within(m, base):           # the point test relative to a base point
    rho = matrix(QQ, matrix(ZZ, m.inverse()).transpose())
    return frozenset(key(rho*vector(ZZ, lift(k))) for k in base)
point = {zero, key(vector(ZZ, [1 if x=="ep" else 0 for x in labels])), key(vector(ZZ, [1 if x=="fp" else 0 for x in labels]))}
point = point | {key(vector(ZZ, lift(x)) + vector(ZZ, lift(y))) for x in list(point) for y in list(point)}
base = cls_within(identity_matrix(ZZ, NC), point)
def in_GammaCo2(m): return cls_within(m, point) == base
def mult_eta(w):
    for i in range(NC):
        if eta[i]:
            if w[i] % eta[i]: return False
            k = w[i]//eta[i]
            return all(w[j] == k*eta[j] for j in range(NC))
    return w.is_zero()

# the raw transporter restricted, as before
h12 = vector(ZZ, [1 if k==0 else 0 for k in range(12)]) + vector(ZZ, [1 if k==1 else 0 for k in range(12)])
E2C = matrix(ZZ, NC, 12, [list(h12)] + [list(vector(ZZ, [1 if k==i else 0 for k in range(12)])) for i in range(2,12)]).transpose()
rows = [list(G*vector(ZZ, v)) for v in (vector(ZZ, delta), R5[11], R5[12])]
Sv, _, Vv = matrix(ZZ, 3, 12, rows).smith_form()
K3 = [vector(ZZ, [Vv[i,j] for i in range(12)]) for j in range(12) if all(Sv[k,j]==0 for k in range(3))]
Sb, _, Vb = matrix(ZZ, len(K3), 12, [list(G*vector(ZZ,k)) for k in K3]).smith_form()
P = [vector(ZZ, [Vb[i,j] for i in range(12)]) for j in range(12) if all(Sb[k,j]==0 for k in range(len(K3)))]
T = matrix(QQ, [list(vector(ZZ,delta)), list(R5[11]), list(R5[12])]).transpose()
sw = []
for b in P:
    c = T.solve_right(vector(QQ, b)); sw.append(int(c[0])*vector(ZZ,delta) + int(c[2])*vector(ZZ,R5[11]) + int(c[1])*vector(ZZ,R5[12]))
PP = matrix(ZZ, 12, 12, [list(v) for v in P] + [list(v) for v in K3]).transpose()
im = matrix(ZZ, 12, 12, [list(v) for v in sw] + [list(v) for v in K3]).transpose()
g12 = matrix(ZZ, matrix(QQ, im) * matrix(QQ, PP).inverse())
cols = []
for j in range(NC):
    w = g12*vector(ZZ, E2C.column(j))
    x = matrix(QQ, Gc).solve_right(vector(QQ, matrix(ZZ,E2C).transpose()*G*w))
    cols.append(vector(ZZ, [int(y) for y in x]))
g = matrix(ZZ, NC, NC, cols).transpose()
say("generators: %d; g|T_Co keeps the line %s, moves the class %s, in Gamma_Co,2 %s"
    % (len(Ms), g*eta in (eta,-eta), mult_eta(g*r12 - r13), in_GammaCo2(g)))

frontier = {(): identity_matrix(ZZ, NC)}
found = None
for depth in range(1, 17):
    nxt = {}                      # per-level dedupe only: the global set is what ran out of memory
    for s in frontier.values():
        for m in Ms:
            t = m * s
            if t*eta not in (eta, -eta): continue
            if not mult_eta(t*r12 - r12): continue
            k = hash(tuple(t.list()))
            if k in nxt: continue
            nxt[k] = t
            if in_GammaCo2(g * t):
                found = (depth, t, g * t); break
        if found: break
    frontier = nxt
    say("depth %d: survivors %d, found %s" % (depth, len(frontier), found is not None))
    if found or not frontier or len(frontier) > 120000: break
print()
if found:
    depth, s, u = found
    say("TRANSPORTER FOUND at depth %d" % depth)
    say("   u = g*s: integral %s, isometry %s, in Gamma_Co,2 %s, keeps the eta_5 line %s, u[r12] = [r13] %s"
        % (all(x in ZZ for x in u.list()), matrix(QQ, NC,NC,list(u.transpose()*Gc*u)) == matrix(QQ, Gc),
           in_GammaCo2(u), u*eta in (eta,-eta), mult_eta(u*r12 - r13)))
    pickle.dump(list(u.list()), open('/repo/.scratch/w760/u_tco.pkl','wb'))
else:
    say("no transporter found within the pruned search to the recorded depth")
print("PYEXIT=0")
