# Maintained-tier computation for the Coble discriminant forms, via the VALIDATED
# provider pin 6ad7a5ea396da6e758ee28f3dea10a35baee0266 (dzackgarza/sage-extensions,
# ancestor of main 9b35a12).
#
# PROVENANCE (this run):
#   runtime : this VM, /opt/math/bin/sage 10.8, CPython 3.12.14
#   import route: module-level imports (sage_extensions.categories.*);
#     sage_extensions.all root-import is not used (it imports sageparse, absent here);
#     sage_extensions.categories.lattices (the Lattices category) does NOT import under
#     Sage 10.8 (rings/real.py ExactRealField -> native_modules free_module
#     "base must be a subring of this ring" — a Sage-version incompatibility), so the
#     discriminant forms are built DIRECTLY at the maintained category
#     TorsionQuadraticFormModules(ZZ).from_relations_and_gram, from the lattice Gram
#     matrices below.  Every value printed is produced by the maintained library code.
#
# Lattices (the corpus's two coordinate models):
#   T_Co = <2> + U(2) + E8(2)      (E8 Cartan C, Gram -2C), basis (g; e',f'; w_1..w_8)
#   S_Co = <-2> + U(2) + E8(2)     basis (alpha; e,f; w_1..w_8)
#   S_diag = diag(2, -2^10)        (the corpus report's other S model, II_{1,10}(2))
# Discriminant data: A_L = L/2L (even 2-elementary, |det| = 2^11); generators [t/2];
#   q([t_i/2]) = t_i^2/4 mod 2;   b([t_i/2],[t_j/2]) = (t_i.t_j)/2 mod 2  (inside Q/2Z).

import os, sys
_PROVIDER_SRC = os.environ.get(
    'PROVIDER_SRC',
    '/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo/.scratch/se-provider-6ad7a5ea/src')
sys.path.insert(0, _PROVIDER_SRC)   # container runner sets PROVIDER_SRC=/repo/.scratch/se-provider-6ad7a5ea/src

import os as _os, sys as _sys, types as _types
# Sage-10.8/11 compatibility shim, scoped to THIS batch run (recorded in the run's
# provenance): the provider's lazy `from sage_extensions.rings.real import RR`
# (tensors/tensor.py:1016) constructs ExactRealField() at module scope, which needs
# Sage 11's Rings().free_module(rank) convention; Sage 10.8 wants free_module(base).
# RR is used there only as an identity sentinel (`ring is not RR`) and nothing in
# the torsion-form computation touches exact reals, so the sentinel preserves every
# value exactly.  Stubbed: sage_extensions.rings, .rings.real, .rings.nonnegative_reals.
# In the DECLARED shared runtime (the container) the shim is OFF (RR_SHIM=0) and the
# real ring machinery runs; both runs are logged separately.
if _os.environ.get('RR_SHIM', '1') != '0':
    for name in ('sage_extensions.rings', 'sage_extensions.rings.real',
                 'sage_extensions.rings.nonnegative_reals'):
        if name not in _sys.modules:
            _sys.modules[name] = _types.ModuleType(name)
    _sys.modules['sage_extensions.rings'].RR = object()
    _sys.modules['sage_extensions.rings.real'].RR = _sys.modules['sage_extensions.rings'].RR
    _sys.modules['sage_extensions.rings'].NonNegativeReals = object()
    _sys.modules['sage_extensions.rings.nonnegative_reals'].NonNegativeReals = _sys.modules['sage_extensions.rings'].NonNegativeReals
    print('RR shim: ON (interim Sage-10.8 route)')
else:
    print('RR shim: OFF (declared shared runtime)')

from sage.all import CartanMatrix
from sage.version import version as sage_version
from sage_extensions.categories.rings.ring_foundation import _owned_integers, _owned_rationals
ZZ = _owned_integers()
QQ = _owned_rationals()
ONE, TWO = ZZ.one(), ZZ.one() + ZZ.one()
ZERO = ZZ.zero()
HALF = QQ(ONE) / QQ(TWO)
from sage_extensions.categories.modules.framed.formed import (
    TorsionQuadraticFormModules,
)
from sage_extensions.categories.modules.framed.fraction_field_quotients import (
    FractionFieldQuotients,
)

PIN = '6ad7a5ea396da6e758ee28f3dea10a35baee0266'
print('provenance')
_RRMODE = 'OFF (declared shared runtime)' if _os.environ.get('RR_SHIM', '1') == '0' else 'ON (interim Sage-10.8 route)'
print('  provider pin: %s   Sage: %s   route: direct from_relations_and_gram, owned rings via _owned_integers/_owned_rationals; RR shim %s' % (PIN, sage_version, _RRMODE))

TQ = TorsionQuadraticFormModules(ZZ)
VALUES = FractionFieldQuotients(ZZ)(TWO)

C8 = CartanMatrix(['E', int(8)])

def t_gram_s():
    rows = []
    # q diag, b off-diag, entries in Q/2Z (written as rationals reduced mod 2)
    # basis: alpha(-2), e, f (U(2) -> e.f = 2), w_1..w_8 (E8(2) -> -2C)
    q = [-HALF, QQ(ZERO), QQ(ZERO)] + [QQ(ONE)] * 8
    b = [[QQ(ZERO)] * 11 for _ in range(11)]
    b[1][2] = b[2][1] = HALF
    for i in range(8):
        for j in range(8):
            if i != j:
                b[3 + i][3 + j] = HALF if int(-C8[i][j]) % 2 == 1 else QQ(ZERO)
    return [[q[i] if i == j else b[i][j] for j in range(11)] for i in range(11)]

def t_gram_t():
    q = [HALF, QQ(ZERO), QQ(ZERO)] + [QQ(ONE)] * 8
    b = [[QQ(ZERO)] * 11 for _ in range(11)]
    b[1][2] = b[2][1] = HALF
    for i in range(8):
        for j in range(8):
            if i != j:
                b[3 + i][3 + j] = HALF if int(-C8[i][j]) % 2 == 1 else QQ(ZERO)
    return [[q[i] if i == j else b[i][j] for j in range(11)] for i in range(11)]

def diag_gram_s():
    # S_diag = diag(2, -2^10): q_0 = 1/2, q_i = -1/2, all b = 0
    q = [HALF] + [-HALF] * 10
    return [[q[i] if i == j else QQ(ZERO) for j in range(11)] for i in range(11)]

REL = [[TWO if i == j else ZERO for j in range(11)] for i in range(11)]

def make(gram):
    return TQ.from_relations_and_gram(REL, gram, VALUES)

DS = make(t_gram_s())
DT = make(t_gram_t())
DTm = DT.twist(ZERO - ONE)
DSdg = make(diag_gram_s())

print('  |A_S| = %s |A_T| = %s' % (DS.cardinality(), DT.cardinality()))
print('  DS.is_anti_isometric(DT) = %s ; DS.is_isomorphic(DTm) = %s ; DSdg.is_isomorphic(DS) = %s'
      % (DS.is_anti_isometric(DT), DS.is_isomorphic(DTm), DSdg.is_isomorphic(DS)))

# --- the maintained witness: normal-form transport, corpus's gamma_Co route ---
gamma_u2 = DS.isometry_to(DTm)      # geometric U(2)-model coordinates
gamma_dg = DSdg.isometry_to(DTm)    # corpus-validated-test's S construction
print('  DS.isometry_to(DTm)  = %s' % (gamma_u2,))
print('  DSdiag.isometry_to(DTm) = %s' % (gamma_dg,))

gens_S = tuple(DS.module_generators())
gens_T = tuple(DT.module_generators())
gens_Tm = tuple(DTm.module_generators())
alpha_half = gens_S[0]              # [alpha/2] in the U(2) model
eta0 = gens_T[0]                    # [g/2] in the T model (= the exceptional class)

def coord_of(gens, element):
    import itertools
    for bits in itertools.product((0, 1), repeat=11):
        if sum(int(b) * gens[i] for i, b in enumerate(bits)) == element:
            return bits
    return None

def untwisted_q(bits):
    # q of the class with the same coordinates, evaluated in DT (the untwisted form)
    return DT.q(sum(int(b) * gens_T[i] for i, b in enumerate(bits)))

img_alpha_u2 = gamma_u2.forward()(alpha_half)
alpha_bits = coord_of(gens_Tm, img_alpha_u2)
print('  gamma_u2([alpha/2]) : T coordinates (g,e,f,w1..w8) = %s' % (alpha_bits,))
print('    equals eta_0 = [g/2]? %s' % (alpha_bits == (1,) + (0,) * 10,))
print('    q_T(image) + q_S([alpha/2]) = %s (must be 0 mod 2)' % (untwisted_q(alpha_bits) + DS.q(alpha_half),))

# verification: the twisted witness is an isometry (q in DTm vs q in DS), printed
# per generator; against the untwisted DT it is then an anti-isometry by twist's definition.
ok = all(DTm.q(gamma_u2.forward()(x)) == DS.q(x) for x in gens_S)
ok_un = all(untwisted_q(coord_of(gens_Tm, gamma_u2.forward()(x))) == -DS.q(x) for x in gens_S)
print('  isometry vs twisted codomain on generators (q): %s ; anti- vs untwisted: %s' % (ok, ok_un))

# --- the eleven image classes of gamma_u2 on the S generators, as T-coordinate vectors ---
print('  gamma_u2 on S generators (T coordinates (g,e,f,w1..w8)):')
for i, x in enumerate(gens_S):
    im = gamma_u2.forward()(x)
    bits = coord_of(gens_Tm, im)
    print('    e%d -> %s   q_T = %s (q_S = %s)' % (i, bits, untwisted_q(bits), DS.q(x)))

# --- q-level profiles by the maintained q(), over all 2^11 elements ---
import itertools
def profile(form):
    G = form.module_generators()
    prof = {}
    for bits in itertools.product((0, 1), repeat=11):
        v = sum(int(b) * G[i] for i, b in enumerate(bits))
        prof[form.q(v)] = prof.get(form.q(v), 0) + 1
    return prof

print('  q-profile A_T (maintained q): %s' % (profile(DT),))
print('  q-profile A_S (maintained q): %s' % (profile(DS),))

# --- the (F2),(F3) forcing at the maintained witness ---
# BAD_S = classes [s/2] with s^2 = -4 and A.s = 0; in (a,b;w) with alpha-coeff 0:
#   all 121 classes map under gamma_u2 to T classes of q = 1, and we print their norms check:
#   we verify maintained-level that each image has q_T = 1 (the level that equals BAD_T(-4)).
bad_s_coords = []
# (F2): [(e-f)/2]
bad_s_coords.append(tuple([0, 1, 1] + [0] * 8))
# (F3): 120 root classes [w/2]: enumerate w with w^2 = -4 i.e. w^T C w = 2, classes w ~ -w, w mod 2
def cartan_norm(wv):
    return sum(wv[i] * C8[i][j] * wv[j] for i in range(8) for j in range(8))
seen = set()
import itertools as it
# exact E8 root enumeration: closure of the simple roots under additions of
# simple roots (positive half), plus the sign map for the negatives, all in  Completeness is the standard
# root-system fact that every positive root is a chain of simple-root partial
# sums, each a root; integer arithmetic, no box.
simples = [tuple(1 if i == k else 0 for i in range(8)) for k in range(8)]
roots = set()
frontier = list(simples)
seen = set(simples)
while frontier:
    r = frontier.pop()
    if cartan_norm(r) == 2:
        roots.add(r)
        for s in simples:
            for cand in (tuple(r[i] + s[i] for i in range(8)),
                         tuple(r[i] - s[i] for i in range(8))):
                if cand not in seen:
                    seen.add(cand)
                    frontier.append(cand)
roots.update(tuple(-x for x in r) for r in sorted(roots))   # the negative half (set.update: preparser-safe)
roots = sorted(roots)
assert len(roots) == 240, 'E8 root count must be 240; got %d' % len(roots)
print('  E8 roots enumerated by height induction: %d (expect 240)' % len(roots))
classes_mod2 = set()
for r in roots:
    key = tuple(x % 2 for x in r)
    neg = tuple((-x) % 2 for x in r)
    if key not in classes_mod2 and neg not in classes_mod2:
        classes_mod2.add(key)
        bad_s_coords.append(tuple([0, 0, 0] + list(key)))
print('  BAD_S classes assembled: %d (expect 121)' % len(bad_s_coords))
_probe = untwisted_q(coord_of(gens_Tm, gamma_u2.forward()(
    sum(int(b) * gens_S[i] for i, b in enumerate(bad_s_coords[0])))))
print('  probe: q of (F2)-image = %r' % (_probe,))
_qone = VALUES(QQ(ONE))
forced = 0
for bits in bad_s_coords:
    x = sum(int(b) * gens_S[i] for i, b in enumerate(bits))
    im = gamma_u2.forward()(x)
    if untwisted_q(coord_of(gens_Tm, im)) == _qone:
        forced += 1
print('  of the %d BAD_S classes, images under gamma_u2 at q_T = 1: %d (all, if forced)' % (len(bad_s_coords), forced))
print('')
print('SUMMARY: maintained witness gamma_u2 exists and is exact; the open (F4) bit evaluates as printed above.')

# ====================================================================================
# CERT-EXT section (owner's gap 4): the witness's inverse/composition identities on ALL
# 2048 elements, the q/b preservation elementwise, the orthogonal-complement (perp)
# computations and the Inv multisets, each produced by MAINTAINED calls or from the
# maintained-verified tables with the property used named per step.
# ====================================================================================
print('')
print('CERT-EXT')
gens_S = tuple(DS.module_generators())
gens_T = tuple(DT.module_generators())
gens_Tm = tuple(DTm.module_generators())

# (1) inverse/composition identities on ALL 2048 elements (maintained morphism calls).
import itertools
all_xS = [sum(int(v) * gens_S[i] for i, v in enumerate(bits)) for bits in itertools.product((0, 1), repeat=11)]
n_inv = sum(1 for x in all_xS if gamma_u2.inverse()(gamma_u2.forward()(x)) == x)
_comp = gamma_u2.then(gamma_u2.inverse())
n_comp = sum(1 for x in all_xS if _comp(x) == x)
print('  (1) inverse(w.fwd(x)/w.inv) on all 2048:', n_inv, '; then(fwd,inv)(x)==x on all 2048:', n_comp)

# (2) q preserved on ALL 2048 elements (maintained .q on both sides; this is the
#     validated-test check extended from generators to the whole module).
n_q = sum(1 for x in all_xS if DTm.q(gamma_u2.forward()(x)) == DS.q(x))
print('  (2) DTm.q(f(x)) == DS.q(x) on all 2048:', n_q)

# (3) b on all 11*11 generator pairs (maintained .b on both sides), printed for the record.
GS = gamma_u2.forward()
okB = True
matS = [[None] * 11 for _ in range(11)]
for i in range(11):
    for j in range(11):
        lft = DTm.b(GS(gens_S[i]), GS(gens_S[j]))
        rgt = DS.b(gens_S[i], gens_S[j])
        matS[i][j] = rgt
        okB = okB and (lft == rgt)
print('  (3) DTm.b(f(gi),f(gj)) == DS.b(gi,gj) on all 121 generator pairs:', okB)
def val_str(v):
    return repr(v).split(' in ')[0]
print('    source b-matrix (row i, over generators (alpha,e,f,w1..w8)), maintained .b:')
for i in range(11):
    print('     ', [val_str(matS[i][j]) for j in range(11)])

# (4) linearity spot-verification of .b against the printed table on 1500 random pairs:
import random
random.seed(int(17))
TWO_TORS = {(0, 1)}
def hh(frac):
    s = val_str(frac)
    if s in ('[0]', '0'): return 0
    if s in ('[(1)/(2)]', '[1/2]', '1/2'): return 1
    raise ValueError(s)
tab = [[hh(matS[i][j]) for j in range(11)] for i in range(11)]
def b_tab(bits_x, bits_y):
    acc = 0
    for i in range(11):
        if bits_x[i]:
            for j in range(11):
                if bits_y[j]: acc += tab[i][j]
    return acc % 2
def elem_of(gens, bits):
    return sum(int(v) * gens[i] for i, v in enumerate(bits))
oklin = True
for _ in range(1500):
    bx = tuple(random.randint(0, 1) for _ in range(11))
    by = tuple(random.randint(0, 1) for _ in range(11))
    oklin = oklin and (hh(DS.b(elem_of(gens_S, bx), elem_of(gens_S, by))) == b_tab(bx, by))
print('  (4) .b == integer table on 1500 random pairs (bilinearity property of the maintained form):', oklin)

# (5) the perp computations and the Inv multisets.
#     Value parser: maintained value-module elements print like '[0]', '[(1)/(2)]', '[1]',
#     '[(3)/(2)]' in Q/2Z (or the same in Q/Z for .b); code them as halves: 0->0, 1/2->1,
#     1->2, 3/2->3 (lev*2 units, m6's lev convention doubled).
import re as _re
def quarters(v):
    r = repr(v)
    m = _re.search(r"\[\(?(-?\d+)\)?(?:/\(?(-?\d+)\)?)?\]", r)
    if m is None:
        raise ValueError('quarters: unparseable %r (type %r)' % (r, type(v).__name__))
    num = int(m.group(1))
    den = int(m.group(2)) if m.group(2) else 1
    return int((num * (2 // den)) % 4)
def hh(frac):
    return quarters(frac)
tab = [[hh(matS[i][j]) for j in range(11)] for i in range(11)]
def b_tab(bits_x, bits_y):
    acc = 0
    for i in range(11):
        if bits_x[i]:
            for j in range(11):
                if bits_y[j]: acc += tab[i][j]
    return acc % 2        # b in Q/Z: halves {0,1/2} -> F2 functional (2b parity)
def elem_of(gens, bits):
    return sum(int(v) * gens[i] for i, v in enumerate(bits))

# (4b) linearity spot-verification of .b against the printed table on 1500 random pairs.
import random
random.seed(int(17))
oklin = True
for _ in range(1500):
    bx = tuple(random.randint(0, 1) for _ in range(11))
    by = tuple(random.randint(0, 1) for _ in range(11))
    oklin = oklin and ((hh(DS.b(elem_of(gens_S, bx), elem_of(gens_S, by))) % 2) == b_tab(bx, by))
print('  (4) .b (mod 1, parity) == integer table on 1500 random pairs:', oklin)

# maintained .q value tables (2048 maintained .q evaluations each side)
import itertools
from collections import Counter, defaultdict
qS = {bits: quarters(DS.q(elem_of(gens_S, bits))) for bits in itertools.product((0, 1), repeat=11)}
qT = {bits: quarters(DT.q(elem_of(gens_T, bits))) for bits in itertools.product((0, 1), repeat=11)}
print('  (5a) maintained .q value levels: A_S %s ; A_T %s'
      % (sorted(Counter(qS.values()).items()), sorted(Counter(qT.values()).items())))

def perp_of(bits_x):
    # perp = kernel of x^T B over F2 (b parity functional); enumerate and return the
    # orthogonal elements' coordinate tuples.
    out = []
    for bits in itertools.product((0, 1), repeat=11):
        if b_tab(bits_x, bits) == 0:
            out.append(bits)
    return out

def ms_of(bits_x, qtab, neg=False):
    ms = Counter()
    for bits in perp_of(bits_x):
        v = qtab[bits]
        if neg: v = (-v) % 4
        ms[v] += 1
    return ms

alpha0 = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ms_src = ms_of(alpha0, qS, neg=True)      # source side: (-q_S) on [alpha/2]^perp
ms_eta = ms_of(alpha0, qT, neg=False)     # Inv(eta_0): q_T on eta_0^perp
print('  (5b) source-side multiset (-q_S on [alpha/2]^perp):', sorted((k, v) for k, v in ms_src.items()))
print('  (5c) Inv(eta_0) (q_T on eta_0^perp):               ', sorted((k, v) for k, v in ms_eta.items()))

# (6) the Inv-block structure over the 528 level-1 classes of A_T (maintained .q for the
#     level partition; verified F2 pairing table for the perps; maintained .q for values).
level1 = [bits for bits, v in qT.items() if v == 1]
print('  (6a) level-1 classes of A_T:', len(level1))
blocks = defaultdict(list)
for bits in level1:
    blocks[tuple(sorted((k, v) for k, v in ms_of(bits, qT).items()))].append(bits)
print('  (6b) Inv-block sizes over level 1:', sorted(len(v) for v in blocks.values()))
for k, v in blocks.items():
    if len(v) == 1:
        print('  (6c) singleton block: invariant', k, '; the class', v[0], '; equals eta_0?', v[0] == alpha0)
