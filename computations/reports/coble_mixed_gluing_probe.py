"""The mixed (-2)-classes of the S_Co + T_Co gluing, probed on a brick model of L_K3.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_mixed_gluing_probe.py

What is computed, and why.  The A20 dossier names the residual "(T-mixed)": do mixed (-2)-classes
delta = (s+t)/2 (s in S_Co, t in T_Co) with H.delta = 0 and A.delta = 0 exist in the labelled
overlattice L_K3?  The swarm's census (d4/m7 Lemma 3) reduced the candidates to the q = (-1) half
classes (s^2 = -4, t^2 = -4), and showed the rest collapse (s = 0 reduces to a pure root) or are
killed by ampleness/intersection arguments.  What remains is a question about WHICH full-graph glue
the construction carries -- and that glue is itself recorded as open in the corpus (report :661,
item 7, "the labelled embedding/gluing").

So this probe does NOT decide B24.  It does the decidable part, on one explicit brick model:
construct L = U^3 + E8(-1)^2 blockwise (even unimodular of signature (3,19), hence the K3
lattice), embed S_Co = U(2) + <-2> + E8(-2) as the U(2)-diagonal, a <-2> inside the third U, and
the E8(2)-diagonal, with T_Co = <2> + U(2) + E8(-2) as the complementary anti-diagonals and a <2>;
verify both embeddings by the maintained isometry predicate against the corpus's own models;
compute the full-graph glue with the maintained L.glue_map; and exhibit mixed (-2)-vectors with
H.delta = A.delta = 0 explicitly.  The point of printing witnesses: mixed wall classes exist for
SOME full-graph glue, so the wall list NL_2 union (F2),(F3) is non-vacuous and the pinned Coble
glue is the real question.

Everything printed as a witness is exact arithmetic and checkable by hand; the lattice
constructions, isometry decisions and the glue arrow are the maintained APIs.

Provenance: pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage 11.0.beta5.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance')
print('  provider pin: %s   Sage: %s' % (PIN, sage_version))
print('')

U2 = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])

# --- the ambient: U_a + U_b + U_c + E8_1 + E8_2 ---------------------------
# block layout in the Gram matrix: columns (0..1) U_a, (2..3) U_b, (4..5) U_c, (6..13) E8_1, (14..21) E8_2
GRAM = block_diagonal_matrix(block_diagonal_matrix(U2, U2),
                             block_diagonal_matrix(U2, block_diagonal_matrix(E8, E8)))
L = Lattices(ZZ)([list(r) for r in GRAM.rows()])
_sig = L.signature_pair()
print('ambient L: rank %d, det %s, signature %s (type %s), even %s'
      % (L.rank(), L.determinant(), _sig, type(_sig).__name__, L.is_even()))
assert L.rank() == 22 and abs(int(L.determinant())) == 1 and L.is_even()
print('  even unimodular (rank 22, signature printed above): the K3 lattice.')

RZZ = L.base_ring()

def vec(d):
    return L.linear_combination({i: RZZ(c) for i, c in d.items() if c != 0})

# --- S_Co inside: the U(2) diagonal, E8(2) diagonal, and <-2> in U_c --------
e_diag = vec({0: 1, 2: 1})            # e = (e_a, e_b), square 0
f_diag = vec({1: 1, 3: 1})            # f, square 0, e.f = 2 (so the pair is U(2))
uc_minus = vec({4: 1, 5: -1})         # the <-2> inside U_c (this is alpha in this model)
uc_plus = vec({4: 1, 5: 1})           # the <2> of U_c, lies on the T side

diag_e8 = [vec({6 + i: 1, 14 + i: 1}) for i in range(8)]     # the E8(2) diagonal (S side)
anti_e8 = [vec({6 + i: 1, 14 + i: -1}) for i in range(8)]    # the E8(2) anti-diagonal (T side)
anti_ue = vec({0: 1, 2: -1})          # the U(2) anti-diagonal (T side)
anti_uf = vec({1: 1, 3: -1})

S = L.primitive_sublattice_from([e_diag, f_diag, uc_minus] + diag_e8)
print('')
print('S sublattice: rank %d, det %s, signature %s' % (S.rank(), S.determinant(), S.signature_pair()))
T = L.orthogonal_complement(S)
print('T = S^perp:  rank %d, det %s, signature %s' % (T.rank(), T.determinant(), T.signature_pair()))

# the corpus's own models of S_Co and T_Co
S_model = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(2 * U2, block_diagonal_matrix(matrix(ZZ, [[-2]]), 2 * E8)).rows()])
T_model = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), block_diagonal_matrix(2 * U2, 2 * E8)).rows()])
print('')
print('S  is_isometric_to( U(2) + <-2> + E8(-2) ): %s' % (S.is_isometric_to(S_model),))
print('T  is_isometric_to( <2> + U(2) + E8(-2) ): %s' % (T.is_isometric_to(T_model),))

# sanity of the pieces inside L
print('')
print('piece checks inside L (all must hold):')
print('  e^2=%d f^2=%d e.f=%d (want 0,0,2)' % (e_diag.q(), f_diag.q(), e_diag.b(f_diag)))
print('  alpha = uc_minus: square %d (want -2); uc_plus: square %d (want 2)' % (uc_minus.q(), uc_plus.q()))
ws = [v.q() for v in diag_e8]
was = [v.q() for v in anti_e8]
print('  diag/anti E8 basis squares:', set(ws), set(was), '(want {-4} on the even 2*E8 scale when the')
print('    two copies are glued: each diag vector has square 2*(-2) = -4)')

# the glue
g = L.glue_map(S, T)
try:
    d_ord, c_ord = g.domain().cardinality(), g.codomain().cardinality()
except Exception as exc:
    d_ord = c_ord = 'unavailable (%s)' % type(exc).__name__
print('')
print('glue_map(S, T): glue order (domain x codomain): %s x %s' % (d_ord, c_ord))
As, At = S.discriminant_group(), T.discriminant_group()
print('|A_S| = %s, |A_T| = %s, det S = %s, det T = %s'
      % (As.cardinality(), At.cardinality(), S.determinant(), T.determinant()))
print('  full graph iff glue order = sqrt(|A_S|.|A_T|) = 2^11 = 2048.')

# --- the mixed witnesses ---------------------------------------------------
print('')
print('mixed (-2)-vectors of L with H.delta = A.delta = 0 and both projections nonzero:')
H = e_diag + f_diag            # H = e + f in the U(2) part of S (square 4)
alpha_r = uc_minus             # the <-2> in U_c: stands in for the retained exceptional root
A = 2 * H - alpha_r
print('  H^2 = %d (want 4), alpha^2 = %d (want -2), A^2 = %d (want 14)' % (H.q(), alpha_r.q(), A.q()))

t_span_gens = [uc_plus, anti_ue, anti_uf] + anti_e8
s_span_gens = [e_diag, f_diag, uc_minus] + diag_e8
witnesses = {
    'x1 = (e_a - f_a, mirror of the U(2) diag/anti pair)': vec({0: 1, 1: -1}),
    'x2 = (e_b - f_b, inside U_b)': vec({2: 1, 3: -1}),
    'control x3 = uc_minus (pure S root alpha, T-pairings must all vanish)': uc_minus,
}
hits = []
for name, x in witnesses.items():
    xs = [x.b(v) for v in s_span_gens]
    xt = [x.b(v) for v in t_span_gens]
    proj_S = any(v != 0 for v in xs)
    proj_T = any(v != 0 for v in xt)
    print('  %s' % name)
    print('    x^2 = %d, x.H = %d, x.A = %d' % (x.q(), x.b(H), x.b(A)))
    print('    nonzero S-side pairing: %s ; nonzero T-side pairing: %s' % (proj_S, proj_T))
    if x.q() == -2 and x.b(H) == 0 and x.b(A) == 0 and proj_S and proj_T:
        hits.append(name)
print('')
if hits:
    print('MIXED WALL CLASSES PRESENT in this glue (x^2=-2, x.H=0, x.A=0, both parts nonzero):')
    for h in hits:
        print('   ' + h)
else:
    print('no mixed wall class among the named candidates.')
print('')
print('interpretation, carefully scoped:')
print('  - the wall of such a class inside D(T_Co) is the hyperplane of its T-projection (t^2 = -4 for')
print('    the (F2) shape), an honest Heegner divisor of T_Co; at a period on it the class is algebraic,')
print('    Riemann-Roch makes one sign effective, and A.delta = 0 then excludes ampleness of A, so the')
print('    period is outside O and outside the one-node image.  So whenever the pinned Coble glue carries')
print('    a (F2)/(F3)-shaped pair, B24-as-verbatim (the pure (-2) arrangement complement) is false and')
print('    the arrangement needs those Heegner pieces too.')
print('  - this probe exhibits such classes in ONE glue (the diagonal/anti-diagonal brick glue), so the')
print('    "no mixed class anywhere" branch is not automatic; it can only hold, if at all, as a property')
print('    of the actual Coble glue -- which the corpus records as an open datum (report :661, item 7).')
print('')
print('Not claimed: that the brick glue IS the Coble glue; no conclusion about B24 itself.')
