"""Building the Coble anti-isometry gamma_Co through the maintained constructors.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_gluing_discriminants.py

What is attempted.  The gluing of S_Co + T_Co -> L_K3 is the graph of an anti-isometry
gamma: A_{S_Co} -> A_{T_Co}, equivalently an isometry A_{S_Co} -> A_{T_Co}(-1).  The provider
exposes `normal_form_isometry()` on a torsion form, documented as the normal-form-to-original
morphism: NF(F) -> F, with domain the normal form.  So for F = A_{S_Co} and G = A_{T_Co}(-1),

    f : NF(A_{S_Co})     -> A_{S_Co}
    g : NF(A_{T_Co}(-1)) -> A_{T_Co}(-1)

and gamma is f^{-1} followed by g, provided the two normal forms are the same object.  `then`
is documented as "other ∘ self" and refuses unless other.domain() is self.codomain(), so
direction matters: f.then(g) is not the intended composite, and a refusal there says nothing
about the provider.  The attempts below run for real, and every failure is reported with the
traceback Python produces.

Reported: the domain and codomain of each arrow, the identity test between the two normal
forms, and, if a composite is produced, the anti-isometry check q_T(gamma x) = -q_S(x) on the
generators, which is where the twist sign is verified.

Scope.  Discriminant forms only: nothing about L_K3, automorphisms of a surface, Kaehler cones,
the chamber or effectivity.

Provenance: pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage 11.0.beta5, image rootfs
read-only, repository bound at /repo.
"""
import sys
import traceback

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance')
print('  provider pin: %s   Sage: %s' % (PIN, sage_version))
print('')

S = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [2] + [-2] * 10).rows()])
E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])

DS, DT = S.discriminant_group(), T.discriminant_group()
DTm = DT.twist(-1)
print('|A_{S_Co}| = %s, |A_{T_Co}| = %s' % (DS.cardinality(), DT.cardinality()))
print('A_{S_Co}.is_anti_isometric(A_{T_Co}) = %s' % (DS.is_anti_isometric(DT),))
print('')

f = DS.normal_form_isometry()
g = DTm.normal_form_isometry()
print('the two normal-form isometries')
print('  f.domain()   = %s' % (f.domain(),))
print('  f.codomain() = %s' % (f.codomain(),))
print('  g.domain()   = %s' % (g.domain(),))
print('  g.codomain() = %s' % (g.codomain(),))
print('  f.domain() is g.domain() : %s' % (f.domain() is g.domain(),))
print('  f.domain() == g.domain() : %s' % (f.domain() == g.domain(),))
print('')

gamma = None


def attempt(label, thunk):
    global gamma
    print('attempt: %s' % label)
    try:
        arrow = thunk()
    except Exception:
        print('  FAILED, traceback:')
        for line in traceback.format_exc().splitlines():
            print('    ' + line)
        return
    print('  SUCCEEDED: %s' % (type(arrow).__name__,))
    print('    domain   = %s' % (arrow.domain(),))
    print('    codomain = %s' % (arrow.codomain(),))
    if gamma is None:
        gamma = arrow


attempt('f.inverse().then(g)   [A_S -> NF -> A_T(-1)]', lambda: f.inverse().then(g))
attempt('f.inverse() * g        [multiplicative form]', lambda: f.inverse() * g)
attempt('g * f.inverse()        [reverse order]', lambda: g * f.inverse())
attempt('f.then(g)              [wrong direction; refusal is correct]', lambda: f.then(g))

print('')
if gamma is None:
    print('RESULT: none of the attempted constructions produced a composite.')
    print('  Each refusal is shown with its own traceback above.')
else:
    print('RESULT: an arrow A_{S_Co} -> A_{T_Co}(-1) was produced.')
    gens = list(DS.module_generating_set())
    qT = DT.quadratic_value_module()
    print('  anti-isometry check on the %d generators of A_{S_Co}:' % len(gens))
    ok = True
    for x in gens:
        y = gamma(x)
        qy, qx = qT(y), gamma.domain().quadratic_value_module()(x)
        same = (qy + qx == qT.zero())
        print('    q_T(gamma x) + q_S(x) == 0 : %s' % (same,))
        ok = ok and same
    print('  gamma is an anti-isometry on every generator: %s' % (ok,))
print('')
print('Not claimed: anything about L_K3, about automorphisms, or about the chamber.')
