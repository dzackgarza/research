"""Referee recomputation for m1/d5 of swarm smw0uqe8g (independent of m1's scripts).

Lattices: T_Co = <2> + U(2) + E8(2), S_Co = <-2> + U(2) + E8(2); classes = L/2L.
E8(2): Gram = -2*C with C the positive E8 Cartan.  q([t/2]) = t^2/4 mod 2.
Checks:
 1. q-level profiles of A_T and A_S (full 2048-class census).
 2. For r in {2,4,6,8}: which A_T classes carry a vector of norm -r
    (search: U(2) box, E8 vectors with norm down to -60), and the set
    difference (level set minus witnessed set).
 3. BAD_S size via the proved bound (A-null forces c = -2(a+b); s^2=-4
    forces 7u^2+v^2+2k=4 with u=a+b, v=a-b, k = w^T C w).
"""
import numpy as np
from itertools import product
from collections import Counter, defaultdict

C = np.array([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,-1],
              [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,-1,2,0],[0,0,-1,0,0,0,0,2]], dtype=np.int64)

def e8norm(W):  # rows of W are E8 coefficient vectors; return w^T C w
    return np.einsum('ij,jk,ik->i', W, C, W)

# --- census of profiles (pure Python, exact) ---
def profile(sign):
    prof = Counter()
    for bits in product((0,1), repeat=11):
        c, m, n = bits[0], bits[1], bits[2]
        w = np.array(bits[3:], dtype=np.int64)
        t2 = sign*2*c*c + 4*m*n + (-2)*int(w @ C @ w)
        q = (t2/4) % 2
        prof[q] += 1
    return dict(sorted(prof.items()))

print('A_T q-profile:', profile(+1))
print('A_S q-profile:', profile(-1))

# --- E8 vectors with k = w^T C w <= 30 (norm >= -60), grouped by mod-2 class ---
KMAX = 30
rng = np.arange(-4, 5)
norm_by_class = defaultdict(set)
grid5 = np.array(list(product(rng, repeat=5)), dtype=np.int64)
for first3 in product(rng, repeat=3):
    W = np.concatenate([np.tile(np.array(first3, dtype=np.int64), (len(grid5),1)), grid5], axis=1)
    ks = e8norm(W)
    keep = W[ks <= KMAX]
    kk = ks[ks <= KMAX]
    for row, k in zip(keep, kk):
        norm_by_class[tuple(int(x) % 2 for x in row)].add(int(k))
print('E8(2): mod-2 classes seen:', len(norm_by_class),
      '; kappa values per class (min..max count):',
      min(len(v) for v in norm_by_class.values()), '..', max(len(v) for v in norm_by_class.values()))

# --- witnessed norms in A_T classes ---
def witnessed(r):
    """For each class of A_T, does it carry a vector of norm -r?"""
    miss = []
    for bits in product((0,1), repeat=11):
        c0, m0, n0 = bits[0], bits[1], bits[2]
        wmod = tuple(int(x) for x in bits[3:])
        found = False
        for dc in range(-3, 4):
            c = c0 + 2*dc
            for dm in range(-3, 4):
                m = m0 + 2*dm
                rem_u = -r - 2*c*c - 4*m*n0  # minimal n variant first
                for dn in range(-3, 4):
                    n = n0 + 2*dn
                    need = -r - 2*c*c - 4*m*n
                    if need > 0 or need % 2:
                        continue
                    k = -need // 2
                    if k <= KMAX and k in norm_by_class.get(wmod, set()):
                        found = True
                        break
                if found: break
            if found: break
        if not found:
            miss.append(bits)
    return miss

for r in (2, 4, 6, 8):
    miss = witnessed(r)
    lvl = {2: '3/2', 4: '1', 6: '1/2', 8: '0'}[r]
    print(f'r={r}: classes with NO norm-{r} witness: {len(miss)} -> {miss}'
          f' (m1 claims level q={lvl} minus witnesses = ' +
          ('[]' if r != 6 else '[eta_0=(1,0,...)]') + ')')

# --- BAD_S via proved bound: 7u^2 + v^2 + 2k = 4, u=a+b, v=a-b ---
# Reconciliation (owner's correction of the earlier committed log): the first
# version enumerated w in the CLIPPED box [-3,3]^8 and printed 95; the bound is
# not met (the highest E8 root has coefficient 6).  The exact input is the same
# Gram matrix C; the evidence below is complete, not bounded:  norm-2 vectors
# of the E8 Cartan are exactly its roots, enumerated by closure of the simple
# roots under simple-root addition (positive half) plus the sign map, integer
# arithmetic, no box -- 240 = #roots(E8).
def cartan(v):
    return int(sum(v[i]*int(C[i][j])*v[j] for i in range(8) for j in range(8)))
simples = [tuple(1 if i==k else 0 for i in range(8)) for k in range(8)]
roots, frontier, seenC = set(), list(simples), set(simples)
while frontier:
    r = frontier.pop()
    if cartan(r) == 2:
        roots.add(r)
        for s in simples:
            for cand in (tuple(r[i]+s[i] for i in range(8)), tuple(r[i]-s[i] for i in range(8))):
                if cand not in seenC:
                    seenC.add(cand); frontier.append(cand)
roots |= {tuple(-x for x in r) for r in roots}
print('E8 roots (exact closure, same Gram input):', len(roots))
sols = []
for u in range(-2, 3):
    for v in range(-2, 3):
        k = (4 - 7*u*u - v*v)/2
        if k != int(k) or k < 0 or (u+v) % 2:  # a,b integral needs u,v same parity
            continue
        k = int(k)
        if k > 2: continue
        cnt = len(roots) if k == 2 else (1 if k == 0 else 0)
        sols.extend((u, v, k) for _ in range(cnt))
        print(f'u={u} v={v} k={k}: lattice solutions={cnt}')

# Explicit level-vs-witnessed comparison (the decisive set identities).
def level_set(qv):
    out = set()
    for bits in product((0, 1), repeat=11):
        c, m, n = bits[:3]
        w = np.array(bits[3:], dtype=np.int64)
        if ((2*c*c + 4*m*n + (-2)*int(w @ C @ w))/4) % 2 == qv:
            out.add(bits)
    return out
def witnessed_set(r):
    out = set()
    for bits in product((0, 1), repeat=11):
        c0, m0, n0 = bits[:3]
        wmod = tuple(int(x) for x in bits[3:])
        ok = False
        for dc in range(-3, 4):
            c = c0 + 2*dc
            for dm in range(-3, 4):
                m = m0 + 2*dm
                for dn in range(-3, 4):
                    n = n0 + 2*dn
                    need = -r - 2*c*c - 4*m*n
                    if need > 0 or need % 2:
                        continue
                    k = -need // 2
                    if 0 <= k <= KMAX and k in norm_by_class.get(wmod, set()):
                        ok = True
                        break
                if ok: break
            if ok: break
        if ok: out.add(bits)
    return out
ETA0 = (1,) + (0,)*10
for r, qv in ((2, 1.5), (4, 1.0), (6, 0.5), (8, 0.0)):
    L = level_set(qv)
    W = witnessed_set(r)
    assert W <= L, 'witnessed outside level (structural inclusion failed)'
    diff = sorted(L - W)
    expected = [] if r != 6 else [ETA0]
    print(f'r={r}: |level q={qv}| = {len(L)}, witnessed = {len(W)}, '
          f'level minus witnessed = {diff} (expected {expected})')
    assert diff == expected
print('set identities confirmed: {q_T = 1} = BAD_T(-4); {q_T = 1/2} = BAD_T(-6) + {eta_0}; '
      'levels for r=2,8 saturated by witnesses.')

print('BAD_S classes (proved bound, exact enumeration, s ~ -s):', len(sols)//2)
