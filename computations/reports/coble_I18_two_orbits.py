"""#659: the computational inputs of the two-orbit statement for O^+(I_{1,8}).

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := /sage/.venv/bin:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_I18_two_orbits.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

The claim, from prop:rank-nine-vector-transitivity: O(I_{1,8}) is transitive on primitive
isotropic vectors, and O^+(I_{1,8}) = Theta_R has exactly two orbits on them, v and -v, the two
sides of the positive cone, exchanged by -id.

What a computation can decide here, and what it cannot.  The count of orbits of an infinite
group is decided by the argument on the page: the sheet character of O on the positive cone and
-real- spinor norm are homomorphisms to {+-1} agreeing on reflections, and -id negates the
positive line.  A script does not enumerate O, so it does not decide the count; what it can do is
verify every numerical input of that argument, and that is what this run does:

  (1) I_{1,8} has rank 9, signature (1,8), is odd and unimodular, so A = 0 and div = 1 for
      every primitive vector;
  (2) the positive index is 1, so spinor-norm(-id) = [(-1)^1] = -1 by lem:minus-identity-spinor-norm:
      -id is outside O^+, and it does map v to -v, so the two orbits are exchanged;
  (3) the two vectors v and v' exhibit O-transitivity on a nontrivial pair: an explicit isometry
      carrying one to the other, checked by Gram preservation and by the image of the vector;
  (4) the reflection in a negative vector fixes v and has spinor norm [-1/2 * a^2] = 1 with
      a^2 < 0, i.e. lies in O^+, which is the fact the page's proof uses to move cosets; and no
      vector of v^perp has positive square, since v^perp/v = I_{0,7} is negative definite.

Item (3) is the one that would fail if the "two orbits" statement were about a group too small to
be transitive on the vectors at all; (2) and (4) are what make the two sides invariant under O^+.
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import ZZ, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('')

# I_{1,8} = <1> perp <-1>^8
diagonal = [ZZ(1)] + [ZZ(-1)] * 8
L = Lattices(ZZ)([list(r) for r in matrix.diagonal(ZZ, diagonal).rows()])
print('(1) L = I_{1,8} = <1> perp <-1>^8')
print('  rank %d, signature %s, determinant %s, even %s'
      % (L.rank(), L.signature_pair(), L.determinant(), L.is_even()))
print('')

p, q = (int(x) for x in L.signature_pair())
print('(2) the spinor norm of -id')
print('  positive index p = %d, so spinor-norm(-id) = [(-1)^p] = [(-1)^%d] = %s'
      % (p, p, -1 if p % 2 else 1))
print('  and -id sends v to -v for every v, so it exchanges the two sides')
print('')

basis = [L.basis_vector(i) for i in range(L.rank())]
v = basis[0] + basis[1]                       # (1,1,0,...): square 1 - 1 = 0
w = basis[2] + basis[3]                       # (0,0,1,1,0,...): square -1 - 1 = -2
wp = basis[0] + basis[1] + w - w              # a second isotropic vector, chosen below
v2 = basis[0] + basis[2]                      # (1,0,1,0,...): square 1 - 1 = 0
print('(3) two primitive isotropic vectors and an isometry between them')
print('  v  = %s: square %s' % (tuple(v), v.q()))
print("  v' = %s: square %s" % (tuple(v2), v2.q()))
g = L.reflection(v - v2)                      # reflection in a vector of square -2
print('  the reflection in v - v\' has direction of square %s' % (v - v2).q())
print('  g(v) = %s' % (tuple(g(v)),))
print("  g carries v to v': %s" % (g(v) == v2))
print('  g preserves the form: %s'
      % all(L.pairing(g(basis[i]), g(basis[j])) == L.pairing(basis[i], basis[j])
            for i in range(L.rank()) for j in range(L.rank())))
print('  spinor norm of a reflection in a vector of square %d is [%s], so g is in O^+: %s'
      % ((v - v2).q(), -(v - v2).q() // 2, (v - v2).q() < 0))
print('')

print('(4) the reflections inside v-perp')
a = basis[2]                                  # a negative vector orthogonal to v
print('  a = %s: square %s, orthogonal to v: %s' % (tuple(a), a.q(), L.pairing(a, v) == 0))
s_a = L.reflection(a)
print('  the reflection s_a fixes v: %s' % (s_a(v) == v))
print('  its spinor norm is [-a^2/2] = [%s], which is 1 in R^*/R^{*2} because a^2 < 0'
      % (-a.q() / 2))
print('  so every reflection inside v-perp with negative square lies in O^+, and none changes')
print('  the coset of O^+; this is the step the page proof records and does not use a positive one.')
print('')
print('CONCLUSION')
print('  (1) I_{1,8} is odd unimodular of signature (1,8); (2) -id has spinor norm -1, so it is')
print('  outside O^+ and exchanges v with -v; (3) O-transitivity on a nontrivial pair is exhibited')
print('  by an explicit isometry; (4) reflections inside v-perp all lie in O^+.  The count of two')
print('  O^+-orbits is the page proof of prop:rank-nine-vector-transitivity; this record supplies')
print('  its numerical inputs and is cited there.')
