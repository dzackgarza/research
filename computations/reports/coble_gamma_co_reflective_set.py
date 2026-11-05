"""A3 (#646): the reflective set of the stable Coble group, at the owning library.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src \
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/coble_gamma_co_reflective_set.py

Declared shared runtime, adopted: image ghcr.io/dzackgarza/sage at the rootfs above
(Sage 11.0.beta5), with the research provider on PYTHONPATH at the snapshot the corpus's
own records run at, sage-extensions pin 6ad7a5ea396da6e758ee28f3dea10a35baee0266
(.scratch/se-provider-6ad7a5ea/src, rebuilt from that pin; see
deployed-runtime-readiness-20261104.md, which says which checkout the computations use and
that it is not the image's own /repos/sage-extensions at 7b222e86). Nothing in the rootfs is
written.

What this file is for.  #646 asks for two things about
Gamma_Co = O^+(T_Co) cap ker(rho_{T_Co}): an explicit reflective set in T_Co, and a
theorem that it, with finitely many further isometries, generates Gamma_Co.  The first
half is decided here and in writing/coble/lattices-and-moduli/
the-heegner-line-and-the-coble-arithmetic-group.md; the second half is not, and the
run records exactly why, operation by operation, rather than a conclusion drawn from a
refusal.  The deciding matrix for the second half -- membership in ker(rho) of an
explicit isometry -- is not available at this runtime at all; see
computations/reports/coble_owner_gap-blockers-20261105.md for the pasted crash.

The reflective set, stated.  By @def:2elementary-roots the roots of an even
2-elementary lattice are the short roots (v^2 = -2) and the long roots (v^2 = -4 with
div(v) = 2).  For v in T_Co:

  * v^2 = -2, the short roots: s_v lies in O^+(T_Co) (sn_R(s_v) = [-q(v)/2] = [1]) and in
    ker(rho_{T_Co}) (s_v(x*) = x* + (x*.v) v, and x*.v is an integer because v is in the
    lattice), so s_v lies in Gamma_Co.  Every (-2)-vector, and there are infinitely many;
  * v^2 = +2, resp. +4: s_v is integral and acts trivially on the discriminant, but
    sn_R(s_v) = [-1], so it is not in O^+(T_Co) and hence not in Gamma_Co;
  * v^2 = -4, the long roots: s_v(x) = x + b(x,v) v / 2, integral because every primitive
    vector of T_Co has divisibility 2 (lem:divisibilityAlwaysTwoTco, and the div column
    below shows it on the basis), and sn_R(s_v) = [-q(v)/2] = [2] = [1], so s_v lies in
    O^+(T_Co); whether it lies in Gamma_Co is then a per-vector question about its action
    on A_{T_Co}.  For e' - f' the answer is no, decided in the writing, which is why the
    corpus's sigma is outside Gamma_Co.

So the reflective set of Gamma_Co is the short roots, together with such long roots as
act trivially on A_{T_Co}; the short roots alone are the part that is decided by the
square.  What the run checks, and what it cannot.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as SAGE_VERSION

from sage_extensions.all import EvenTwoElementaryLattices, HyperbolicLattices, Lattices

sys.stdout.reconfigure(line_buffering=True)


def refusal(label, thunk):
    """Print what the owner does with ``thunk``: its value, or the exact refusal."""
    try:
        value = thunk()
    except Exception as exc:  # noqa: BLE001 - the refusal text is the datum
        first = str(exc).split('\n')[0]
        print('  %-46s REFUSED %s: %s' % (label, type(exc).__name__, first[:300]))
        return None
    print('  %-46s %s' % (label, value))
    return value


print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-6ad7a5ea/src on PYTHONPATH, pin 6ad7a5ea')
print('  lattice: built here from its own Gram data, not read from a stored object')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])                       # negative definite E8
T_GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
T = Lattices(ZZ)([list(row) for row in T_GRAM.rows()])
basis = [T.basis_vector(i) for i in range(T.rank())]
zeta, e_prime, f_prime = basis[0], basis[1], basis[2]
a = basis[3:]                                      # the E8(-2) basis vectors

print('T_Co = <2> + U(2) + E8(-2), the twist B(2) of prop:tco-as-twist')
print('  rank %d, determinant %s, signature %s, even: %s'
      % (T.module_rank(), T.determinant(), T.signature_pair(), T.is_even()))
assert tuple(int(v) for v in T.signature_pair()) == (2, 9)
assert int(T.determinant()) == -2048 and T.is_even()
invariants = EvenTwoElementaryLattices(T.base_ring())(T).two_elementary_invariants()
print('  two_elementary_invariants: %s   (the Coble table: (11, 11, 1))'
      % (tuple(int(x) for x in invariants),))
assert tuple(int(x) for x in invariants) == (11, 11, 1)
print('  basis squares (zeta; e-prime, f-prime; the eight E8(-2) vectors): %s'
      % [int(v.q()) for v in basis])
print('')

# ---------------------------------------------------------------- the reflective squares
print('the reflective squares the owner admits')
lengths = [int(x) for x in T.possible_root_lengths()]
print('  possible_root_lengths(): %s   (divisors of 2 * exp(A_L) = 2 * 2)' % lengths)
assert lengths == [1, 2, 4]
print('  square -1 cannot occur in an even lattice, and square +-2 and -4 are the two')
print('  cases of @def:2elementary-roots on a 2-elementary lattice.')
print('')

# ---------------------------------------------------------------- the four root cases
print('one representative of each case of the introduction')
cases = (
    ('short root  zeta + a_1', zeta + a[0]),
    ('short root  zeta + a_8', zeta + a[7]),
    ('positive root  zeta', zeta),
    ('positive root  e\' + f\'', e_prime + f_prime),
    ('long root  a_1', a[0]),
    ("long root  e' - f'", e_prime - f_prime),
)
for label, v in cases:
    print('  %-36s q = %3d   div = %d' % (label, int(v.q()), T.div(v)))
print('')

# ---------------------------------------------------------------- reflections that build
print('the reflections, built by the owner')
rho_kernel = T.stable_orthogonal_group()
print('  Gamma_Co\'s discriminant half ker(rho_T) as an owned object: %s'
      % type(rho_kernel).__name__)
short = zeta + a[0]
s_short = T.reflection(short)
print('  s_(zeta + a_1): determinant %d, fixes the vectors orthogonal to the root: %s,'
      % (s_short.determinant(), s_short(f_prime) == f_prime and s_short(a[1]) == a[1]))
print('      an involution: %s, negates the root: %s'
      % (s_short(s_short(short)) == short, s_short(short) == -short))
long_root = e_prime - f_prime
s_long = T.reflection(long_root)
print('  s_(e\' - f\'): determinant %d, an involution: %s, negates the root: %s'
      % (s_long.determinant(), s_long(s_long(long_root)) == long_root,
         s_long(long_root) == -long_root))
print('  the discriminant action of s_(e\' - f\'), computed by hand and not here:')
print('      s((e\')/2) = (f\')/2, and (f\' - e\')/2 is not in T_Co, so rho(s) != 1.')
print('')

# ---------------------------------------------------------------- what the owner refuses
print('the owner operations this question needs, and what they do here')
print('  (the lattice layer builds; the decision layer needs GAP, see the blockers record)')
refusal('T.O_plus()', lambda: T.O_plus())
refusal('T.spinor_norm()', lambda: T.spinor_norm())
refusal('T.roots()', lambda: list(T.roots()))
refusal("T.roots_of_square(-2)", lambda: list(T.roots_of_square(-2)))
refusal('T.root_sublattice()', lambda: T.root_sublattice())
refusal('HyperbolicLattices(ZZ)(T)',
        lambda: HyperbolicLattices(T.base_ring())(T))
locus = T.reflective_root_locus()
print('  %-46s %s' % ('T.reflective_root_locus()', type(locus).__name__))
print('  %-46s %s' % ('  is the short root in it', (zeta + a[0]) in locus))
print('  %-46s %s' % ('  is e\' - f\' in it', (e_prime - f_prime) in locus))
print('  %-46s %s' % ('  is a_1 in it', a[0] in locus))
print('  %-46s %s' % ('  is zeta (+2) in it', zeta in locus))
print('')

print('SUMMARY')
print('  (1) T_Co is the even lattice <2> + U(2) + E8(-2), rank 11, det -2048, signature')
print('      (2, 9), two-elementary with invariants (11, 11, 1), agreeing with the')
print('      chapter table; its admissible reflective squares are {1, 2, 4} and the')
print('      square -1 is excluded by parity, so its roots are the short roots v^2 = -2')
print('      and the long roots v^2 = -4, whose divisibility is 2 here, as')
print('      @def:2elementary-roots and lem:divisibilityAlwaysTwoTco say;')
print('  (2) the (-2)-vectors of T_Co give reflections the owner builds, and the groups')
print('      O^+(T_Co), the spinor norm and ker(rho_T_Co) are all built here as objects; but')
print('      the two steps that place a named reflection in Gamma_Co are decisions, and')
print('      neither is available: the spinor one stops the interpreter in GAP, and the')
print('      discriminant one raises in the provider before GAP is reached (probe 3 of')
print('      coble_owner_gap-blockers-20261105.md).  Both therefore remain proofs in the')
print('      writing and are not claimed as owner decisions here;')
print("  (3) the long root e' - f' has an integral reflection in O^+(T_Co) that moves the")
print('      discriminant, so the reflective set of Gamma_Co is not the whole root system:')
print('      it is the short roots together with the long roots whose reflection acts')
print('      trivially on A_T_Co, and among the short roots nothing more has to be decided;')
print('  (4) T_Co is not hyperbolic, so the Vinberg-algorithm route the research report')
print('      names (@prob:coxeter-completeness item 2, B32--B34) does not apply to T_Co')
print('      itself: HyperbolicLattices refuses it by signature, and what remains is the')
print('      reflective-lattice question in signature (2,9), for which the owner has no')
print('      operation.  No generation statement is made or implied here.')
print('OK: the reflective set is decided in writing; the generation half is blocked at the')
print('    owner with the exact operations named, not with a substituted algorithm.')
