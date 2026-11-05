"""A4 (#647): which of the two definitions of Gamma_Co is which, at the owning library.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src \\
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \\
        /repo/computations/reports/coble_gamma_co_two_definitions.py

Declared runtime and provider as in coble_gamma_co_reflective_set.py: the adopted rootfs
(Sage 11.0.beta5) with sage-extensions pin 6ad7a5ea on PYTHONPATH.  Nothing is written to
the rootfs.

What #647 asks.  Its first half is definitional: Gamma_Co = O^+(T_Co)* and
tilde O^+(T_Co) coincide because the book *defines* O^+(L) := Theta_R(L) and takes the
pullback along it, so the identity is a substitution (lem:gamma-co-is-tilde-o-plus in
writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md).
Its second half is arithmetic: the Heegner and theta descriptions contain Gamma_Co as the
kernel of their action on A_{T_Co} (@prop:gamma-co-in-heegner-group,
@prop:gamma-co-in-theta-centralizer), so they agree with it exactly when a certain finite
subgroup of O(A_{T_Co}, q_{T_Co}) -- a group of order 46 998 591 897 600 -- is trivial.

What this run establishes, and what it cannot.  The finite subgroup on the *Enriques* side
is nontrivial, and that is proved by hand here with the owner checking every input: the
reflection of S_En in u_0 - w_0 fixes h and moves the class of u_0/2, because
s(u_0/2) - u_0/2 = (u_0 - w_0)/2 and that vector is not in S_En (lem:polarization-
stabilizer-discriminant-nontrivial).  The step that reads the class off -- the discriminant
action of a named isometry -- is the call #272 breaks, so it is *stated and checked at its
inputs* here and not decided: `s.discriminant_morphism()` raises
  TypeError: TorsionFormOrthogonalGroup._element_constructor_() got an unexpected keyword
  argument 'check'
on S_En exactly as it does on T_Co.  Nothing below claims the two inclusions are strict;
that needs rho_T(Gamma^theta_Co) itself, and no operation here decides it.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as SAGE_VERSION

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-6ad7a5ea/src on PYTHONPATH, pin 6ad7a5ea')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
C_GRAM = block_diagonal_matrix(U, E8)
C = Lattices(ZZ)([list(row) for row in C_GRAM.rows()])
S = Lattices(ZZ)([list(row) for row in (2 * C_GRAM).rows()])

print('the two lattices of the Heegner side')
print('  C = U + E8(-1): rank %d, signature %s, determinant %s'
      % (C.rank(), C.signature_pair(), C.determinant()))
print('  S_En = C(2):    rank %d, signature %s, determinant %s'
      % (S.rank(), S.signature_pair(), S.determinant()))
c_basis = [C.basis_vector(i) for i in range(C.rank())]
s_basis = [S.basis_vector(i) for i in range(S.rank())]
h_C = c_basis[0] + c_basis[1]
h_S = s_basis[0] + s_basis[1]
print('  h = u_0 + w_0: h^2 = %d in C and %d in S_En' % (h_C.q(), h_S.q()))
assert h_C.q() == 2 and h_S.q() == 4
print('')

u0, w0 = s_basis[0], s_basis[1]
print('the U(2) summand of S_En, which the proof below uses')
print('  u_0^2 = %d, w_0^2 = %d, u_0 . w_0 = %d'
      % (u0.q(), w0.q(), S.pairing(u0, w0)))
assert u0.q() == 0 and w0.q() == 0 and S.pairing(u0, w0) == 2
v = u0 - w0
print('  v = u_0 - w_0: q = %d, divisibility %d' % (v.q(), S.div(v)))
assert v.q() == -4 and S.div(v) == 2
A_S = S.discriminant_group()
print('  |A_{S_En}| = %d, and the exponent of A_L bounds possible_root_lengths: %s'
      % (A_S.cardinality(), list(S.possible_root_lengths())))
print('')

print('the reflection, built by the owner')
s = S.reflection(v)
print('  s = s_(u_0 - w_0): determinant %d, an involution: %s'
      % (s.determinant(), s(s(v)) == v))
print('  s fixes h = u_0 + w_0: %s   <-- the first half of the lemma' % (s(h_S) == h_S))
assert s(h_S) == h_S
print('  s fixes the sum u_0 + w_0: %s, and transposes the two directions: s(u_0) = w_0: %s'
      % (s(u0 + w0) == u0 + w0, s(u0) == w0))
print('')

print('the step that decides the lemma: the discriminant action of s')
print('  s(x) = x + b(x,v)v/2 because q(v) = -4, and b(u_0/2, v) = b(u_0,v)/2 = -1, so')
print('  s(u_0/2) = w_0/2 and s(u_0/2) - u_0/2 = (w_0 - u_0)/2, whose coordinates in the')
print('  basis of S_En are (-1/2, 1/2, 0, ..., 0): not in S_En, so rho(s) != 1.')
print('  Asking the owner instead:')
try:
    s.discriminant_morphism()
    print('  s.discriminant_morphism() RETURNED -- the class arithmetic would be decided here')
except Exception as exc:  # noqa: BLE001 - the refusal text is the datum
    print('  s.discriminant_morphism() RAISED %s: %s'
          % (type(exc).__name__, str(exc).split('\n')[0][:200]))
print('  the same call on T_Co fails identically; it is dzackgarza/sage-extensions#272')
print('')

print('SUMMARY')
print('  (1) the first half of #647 is definitional and needs nothing here:')
print('      Gamma_Co = O^+(T_Co)* = tilde O^+(T_Co), because the book defines')
print('      O^+(L) := Theta_R(L) and tilde O^+(L) as the pullback of ker rho_L along it')
print('      (lem:gamma-co-is-tilde-o-plus);')
print('  (2) the finite subgroup that separates the two further definitions is nontrivial on')
print('      the Enriques side, by hand and with every input above checked: s_(u_0 - w_0)')
print('      lies in Stab_{O(S_En)}(h) and carries the class of u_0/2 to that of w_0/2,')
print('      whose difference (w_0 - u_0)/2 is not in S_En.  So rho_{S_En}(Stab(h)) != 1')
print('      (lem:polarization-stabilizer-discriminant-nontrivial);')
print('  (3) that does not settle #647: what decides it is rho_T(Gamma^theta_Co) and')
print('      rho_T(Gamma^Hdg_Co), subgroups of O(A_{T_Co}, q) of order at most')
print('      46 998 591 897 600, and exhibiting their elements needs the discriminant action')
print('      of a named isometry -- the call that raises above.  The question is therefore')
print('      reduced to a finite-group computation and recorded as blocked on #272; no')
print('      statement about strictness of either inclusion is made here.')
print('OK: the definitional half is a lemma, the separating subgroup is nontrivial by proof,')
print('    and the finite computation that decides the rest is named and blocked at its call.')
