"""The premises of the joint-flag uniqueness theorem, at the maintained pin.

Published transplanted form of the m3/smw0gfl0i check
(.ultramath/smw0gfl0i/m3/a21_m3_flag_theorem_check.py); self-contained, except for the
sage_extensions provider package.  Two print lines are corrected against the original:
the definite piece's note now makes no discriminant-image claim (the original said "its image
is trivial", which is false: the actual image of O(E8(-2)) on A_{E8(-2)} is the full mod-2
Weyl reduction O^+_8(F_2) with kernel {+-1}; see computations/reports/smwg_operator-extension.md
SS3).  Every computed value is unchanged.  One duplicated assignment block was removed from
section 5.  Run:

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b $PWD:/repo -w /repo /sage/.venv/bin/sage \
        computations/reports/coble_joint_flag_premises.py

What this certifies (nothing about the construction side is computed here; it is cited):

 1. The reflected pair J_Co = w.alpha o I_enr, J_dP = w.alpha o I_dP of the maintained
    computations/reports/coble_reflected_pair.py, rebuilt by the same construction, has the four
    joint eigenspace lattices with the maintained types, ranks (3,8,0,11), signatures
    (1,2), (0,8), (0,0), (2,9), determinant absolute values 8, 256, 1, 2048.
 2. Each nonzero piece is even and 2-elementary (|A| = 2^rank); V++ and V-- are INDEFINITE
    (so Nikulin 1980 Thm 3.6.3, O(S) -> O(q_S) surjective for even indefinite 2-elementary S,
    applies to them) and V+- = E8(-2) is definite (so 3.6.3 is NOT claimed for it).
 3. The gluing is a full graph: [L : V++ perp V+- perp V--] = 2048 = |A_{V--}| = |A_{V++ perp V+-}|.
 4. The labelled classes: H = Delta(e)+Delta(f) and alpha = e-f lie in V++, are fixed by both
    involutions, have H^2 = 4, alpha^2 = -2, H.alpha = 0, both primitive, H +- alpha not divisible.
 5. The corner structure of (H, alpha) inside V++ = U(2) perp <-2>: the primitive generator delta
    of (H,alpha)^perp inside V++ has delta^2 = -4, (H+delta)/2 is an element of V++, and
    e = (H+delta)/2, f = (H-delta)/2, alpha is an index-one U(2) perp <-2> basis of V++.
    (e,f are the hyperbolic U(2) basis, alpha is the <-2> generator: the same corner the
    construction supplies, H = pi^*O(1,1), alpha = [D_b].)

Reported per item: the provider call used and its value. Raw Sage matrix arithmetic is used only
to produce kernel bases and to solve integral linear systems, as in the maintained scripts.
"""
import sys
from sage.all import QQ

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix, block_matrix, identity_matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance')
print('  provider pin: %s   Sage: %s' % (PIN, sage_version))
print('  provider package: %s' % (__import__('sage_extensions').__file__,))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])          # E8(-1)
GRAM = block_diagonal_matrix(U, U, U, E8, E8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
n = int(L.rank())
print('model: L = U^3 + E8(-1)^2, rank %d, determinant %s, even %s'
      % (n, L.determinant(), L.is_even()))
G = matrix(ZZ, [[int(L.basis_vector(i) * L.basis_vector(j)) for j in range(n)] for i in range(n)])
assert G == GRAM

# ---------------------------------------------------------------- 1. the reflected pair
def blocks(coords):
    return (coords[0:2], coords[2:4], coords[4:6], coords[6:14], coords[14:22])

def image_under(kind, coords):
    v, u, u1, e, e1 = (list(part) for part in coords)
    if kind == 'dP':
        return [-x for x in v] + u1 + u + [-x for x in e] + [-x for x in e1]
    if kind == 'enr':
        return [-x for x in v] + u1 + u + e1 + e
    raise ValueError(kind)

def op_matrix(kind):
    cols = []
    for j in range(n):
        coords = [0] * n
        coords[j] = 1
        cols.append(image_under(kind, blocks(coords)))
    return matrix(ZZ, n, n, lambda i, j: cols[j][i])

M_dP = op_matrix('dP')
M_enr = op_matrix('enr')
Id = identity_matrix(ZZ, n)
for name, M in (('I_dP', M_dP), ('I_enr', M_enr)):
    print('%s: isometry of L: %s, involution: %s'
          % (name, M.transpose() * G * M == G, M * M == Id))

alpha_vec = [0] * n
alpha_vec[0], alpha_vec[1] = 1, -1
# w = reflection in alpha:  w(x) = x + (x.alpha) alpha
Wm = Id + matrix(ZZ, n, n, lambda i, j: (G[i, j] * 0))
am = matrix(ZZ, n, 1, alpha_vec)
Wm = Id + am * am.transpose() * G            # (x.alpha) alpha, since alpha^2 = -2
print('w = L.reflection(alpha): isometry: %s, involution: %s'
      % (Wm.transpose() * G * Wm == G, Wm * Wm == Id))
M_Co = Wm * M_enr
M_dPp = Wm * M_dP
for name, M in (('J_Co = w o I_enr', M_Co), ('J_dP = w o I_dP', M_dPp)):
    print('%s: isometry: %s, involution: %s' % (name, M.transpose() * G * M == G, M * M == Id))
print('J_Co and J_dP commute: %s' % ((M_Co * M_dPp == M_dPp * M_Co),))
print('product J_Co J_dP is an involution: %s, symplectic (no +1 on the whole): %s'
      % ((M_Co * M_dPp) * (M_Co * M_dPp) == Id, M_Co * M_dPp != Id))
print('')

# ---------------------------------------------------------------- 2. joint eigenspace lattices
piece_vecs = {}
piece_lat = {}
for tag, sJ, sK in [('++', 1, 1), ('+-', 1, -1), ('-+', -1, 1), ('--', -1, -1)]:
    Mstack = block_matrix([[M_Co - sJ * Id], [M_dPp - sK * Id]])
    rows = [[int(v) for v in r] for r in Mstack.transpose().kernel().basis_matrix().rows()]
    vecs = [L.linear_combination({j: L.base_ring()(c) for j, c in enumerate(r) if c}) for r in rows]
    piece_vecs[tag] = rows
    piece_lat[tag] = L.sublattice_from(vecs) if vecs else None
    if not vecs:
        print('%s: rank 0 (empty piece)' % tag)
        continue
    sub = piece_lat[tag]
    N_abs = abs(int(sub.determinant()))
    ordA = int(sub.discriminant_group().cardinality())
    print('%s: rank %d, |det| %d, signature %s, even %s, definite %s, |A| %d = 2^rank %s'
          % (tag, sub.rank(), N_abs, sub.signature_pair(), sub.is_even(), sub.is_definite(),
             ordA, ordA == 2 ** sub.rank()))

Lambda_target = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(2 * U, matrix(ZZ, [[-2]])).rows()])
E8m2_target = Lattices(ZZ)([list(r) for r in (2 * E8).rows()])
TCO_target = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
print('')
print('maintained type comparisons (provider is_isometric_to):')
print('  ++ is U(2) perp <-2>            : %s' % (piece_lat['++'].is_isometric_to(Lambda_target),))
print('  +- is E8(-2)                    : %s' % (piece_lat['+-'].is_isometric_to(E8m2_target),))
print('  -- is <2> perp U(2) perp E8(-2) : %s' % (piece_lat['--'].is_isometric_to(TCO_target),))
print('  controls: E8m2_target definite %s, TCO_target even %s indefinite %s, Lambda_target even %s indefinite %s'
      % (E8m2_target.is_definite(), TCO_target.is_even(), not TCO_target.is_definite(),
         Lambda_target.is_even(), not Lambda_target.is_definite()))
print('')
print('Nikulin 1980 Thm 3.6.3 hypotheses (even, indefinite, 2-elementary):')
for tag in ('++', '--'):
    sub = piece_lat[tag]
    ordA = int(sub.discriminant_group().cardinality())
    print('  %s: even %s, indefinite %s, |A| = 2^rank %s  -> surjectivity applies'
          % (tag, sub.is_even(), not sub.is_definite(), ordA == 2 ** sub.rank()))
print('  +- (E8(-2)): definite %s -> 3.6.3 NOT applied to it (no image claim is used: the proof'
      % (piece_lat['+-'].is_definite(),))
print('       lifts on the rank-11 block only; cf. smwg_operator-extension.md SS3)')

# ---------------------------------------------------------------- 3. index of the joint sum
allrows = []
for tag in ('++', '+-', '-+', '--'):
    allrows.extend(piece_vecs[tag])
idx = abs(matrix(ZZ, len(allrows), n, allrows).determinant())
print('')
print('[L : V++ perp V+- perp V-+ perp V--] = %d ; |A_{V--}| = %d ; |A_{V++ perp V+-}| = %d'
      % (idx, int(piece_lat['--'].discriminant_group().cardinality()),
         int(piece_lat['++'].discriminant_group().cardinality())
         * int(piece_lat['+-'].discriminant_group().cardinality())))
print('  full graph gluing (index = |A| on both sides): %s'
      % (idx == int(piece_lat['--'].discriminant_group().cardinality()),))

# ---------------------------------------------------------------- 4. labelled classes
H_vec = [0] * n
for j in (2, 3, 4, 5):
    H_vec[j] = 1
a_vec = alpha_vec  # e - f of the first U
def sq(v):
    return int((matrix(ZZ, 1, n, v) * G * matrix(ZZ, n, 1, v))[0, 0])
print('')
print('labelled classes')
print('  H   = Delta(e)+Delta(f), coords %s : H^2 = %d' % (H_vec, sq(H_vec)))
print('  alpha = e-f,             coords %s : alpha^2 = %d' % (a_vec, sq(a_vec)))
print('  H.alpha = %d' % (int((matrix(ZZ, 1, n, H_vec) * G * matrix(ZZ, n, 1, a_vec))[0, 0]),))
for name, M in (('J_Co', M_Co), ('J_dP', M_dPp)):
    print('  %s fixes H: %s, fixes alpha: %s'
          % (name, [int(r) for r in (M * matrix(ZZ, n, 1, H_vec)).list()] == H_vec,
             [int(r) for r in (M * matrix(ZZ, n, 1, a_vec)).list()] == a_vec))
print('  H/2 in L: %s ; alpha/2 in L: %s ; (H+alpha)/2 in L: %s ; (H-alpha)/2 in L: %s'
      % (all(c % 2 == 0 for c in H_vec), all(c % 2 == 0 for c in a_vec),
         all((H_vec[i] + a_vec[i]) % 2 == 0 for i in range(n)),
         all((H_vec[i] - a_vec[i]) % 2 == 0 for i in range(n))))

# ---------------------------------------------------------------- 5. the corner inside V++
Vrows = piece_vecs['++']
V = matrix(ZZ, 3, n, Vrows)
GV = V * G * V.transpose()
print('')
print('the (++) piece V++ = U(2) perp <-2> in its maintained basis')
print('  Gram of the maintained basis: %s' % (GV.rows(),))
def coords_in_V(vec):
    sol = V.transpose().solve_right(matrix(QQ, n, 1, vec))
    return [QQ(c) for c in sol.list()]
h = coords_in_V(H_vec)
a = coords_in_V(a_vec)
print('  H in V++ with coordinates %s (integral: %s)' % ([str(x) for x in h], all(x.denominator() == 1 for x in h)))
print('  alpha in V++ with coordinates %s (integral: %s)' % ([str(x) for x in a], all(x.denominator() == 1 for x in a)))
def Vdot(x, y):
    return sum(GV[i, j] * x[i] * y[j] for i in range(3) for j in range(3))
print('  cross-checks in V-coordinates: H^2 = %s, alpha^2 = %s, H.alpha = %s'
      % (Vdot(h, h), Vdot(a, a), Vdot(h, a)))
Sys = matrix(QQ, 2, 3, [[Vdot(h, [QQ(1) if k == j else QQ(0) for k in range(3)]) for j in range(3)],
                        [Vdot(a, [QQ(1) if k == j else QQ(0) for k in range(3)]) for j in range(3)]])
Kb = Sys.right_kernel().basis_matrix()
delta = [QQ(x) for x in Kb.row(0)]
from math import gcd as _gcd
dens = 1
for x in delta:
    d = x.denominator()
    dens = dens * d // _gcd(dens, d)
delta = [int(x * dens) for x in delta]
g0 = 0
for x in delta:
    g0 = _gcd(g0, abs(x))
delta = [x // g0 for x in delta]
print('  primitive generator delta of (H,alpha)^perp inside V++: %s' % (delta,))
print('    delta^2 = %s (structure says -4)' % (Vdot(delta, delta),))
print('    delta.H = %s, delta.alpha = %s' % (Vdot(delta, h), Vdot(delta, a)))
half = [(QQ(h[i]) + QQ(delta[i])) / 2 for i in range(3)]
halfm = [(QQ(h[i]) - QQ(delta[i])) / 2 for i in range(3)]
print('    (H+delta)/2 in V++: %s   coords %s'
      % (all(x.denominator() == 1 for x in half), [str(x) for x in half]))
print('    (H-delta)/2 in V++: %s   coords %s'
      % (all(x.denominator() == 1 for x in halfm), [str(x) for x in halfm]))
assert all(x.denominator() == 1 for x in half) and all(x.denominator() == 1 for x in halfm)
e = [int(x) for x in half]
f = [int(x) for x in halfm]
tri = [e, f, [int(x) for x in a]]
Gram_tri = matrix(ZZ, 3, 3, [[Vdot(tri[i], tri[j]) for j in range(3)] for i in range(3)])
print('    e = (H+delta)/2, f = H-e, alpha: Gram %s' % (Gram_tri.rows(),))
print('    det of that Gram = %s, |det V++| = %s -> index one: %s'
      % (Gram_tri.determinant(), abs(int(piece_lat['++'].determinant())),
         abs(int(Gram_tri.determinant())) == abs(int(piece_lat['++'].determinant()))))
print('    e^2 = %s, f^2 = %s, e.f = %s, e.alpha = %s, f.alpha = %s, alpha^2 = %s'
      % (Vdot(e, e), Vdot(f, f), Vdot(e, f), Vdot(e, a), Vdot(f, a), Vdot(a, a)))
print('    H = e+f: %s' % ([e[i] + f[i] for i in range(3)] == [int(x) for x in h],))

print('')
print('summary: the four joint pieces, their maintained types, the full-graph index 2048, the')
print('  placement of H and alpha in V++, and the index-one corner (e,f,alpha) of V++ are all')
print('  reproduced at the pin.  Nothing here concerns the construction side; its data are cited.')
