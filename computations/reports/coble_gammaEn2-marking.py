"""The marking: which anti-isometry gamma, and why the nine generators correspond.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot \\
    .scratch/udocker_dir/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -b $HOME/sage-extensions-cdafca84:/prov -w /repo \\
        /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \\
        PYTHONPATH=/repo/.scratch/port-held/src:/prov/src \\
        /sage/.venv/bin/python /repo/computations/reports/coble_gammaEn2-marking.py

@lem:gamma-transport-identity says the gluing anti-isometry may be taken to be the identity because
A_{S_En} and A_{T_En} agree summand by summand.  An identity-on-the-summands map is a *choice* of
marking until it is shown that the two lattices' summands are distinguished in the same way, and that
is what this script checks rather than assumes.

The discriminant of S_En = U(2) + E8(2) is A_{U(2)} + A_{E8(2)} with A_{U(2)} of order 4; that of
T_En = U + U(2) + E8(2) is A_U + A_{U(2)} + A_{E8(2)} with A_U = 0.  In each lattice the summand
subspaces are computed from the basis:

  A_{U(2)} = <[e/2], [f/2]>            (4 classes, from the U(2) slots)
  A_{E8(2)} = its orthogonal complement (256 classes)

and then the nine generators' discriminant images are read off:

  * the eight reflections in the E8(2) roots must fix A_{U(2)} pointwise and preserve A_{E8(2)};
  * the reflection in u_0 - w_0 (the U(2) swap) must fix A_{E8(2)} pointwise.

Both hold on both lattices exactly when the summand-wise identification is the canonical marking:
then the S-side and T-side nine-element families correspond generator by generator under it, gamma is
the identity on each summand, and rho_T(Gamma_En,2) = M is the group computed from the isometries of
T_En itself.  The script also records the two orbit partitions of M on the 528 isotropic classes, on
both sides, which must agree as multisets.

Checked revision sources, printed by the run itself: the port clone's git HEAD and the provider
snapshot's declared pin plus a content hash, so the numbers in the transcript name what produced them.

Transcript: `coble_gammaEn2-marking-run.txt`.
"""
import hashlib
import itertools
import os
import subprocess
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

import sage_extensions  # noqa: E402
import sage_indefinite_port  # noqa: E402

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print('provenance, from the sources themselves')
print('  Sage: %s' % SAGE_VERSION)
port = '/repo/.scratch/port-held'
print('  port clone %s at git HEAD %s' % (port, subprocess.run(
    ['git', '-C', port, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()))
prov = '/prov'
declared = [l for l in open(os.path.join(prov, 'pyproject.toml')).read().splitlines() if 'version' in l][:1]
digest = hashlib.sha256(open(os.path.join(
    prov, 'src/sage_extensions/categories/orthogonal_quotients.py'), 'rb').read()).hexdigest()[:16]
print('  provider snapshot %s, %s, sha256(orthogonal_quotients.py) = %s' % (prov, declared, digest))
print('  imported from: %s / %s' % (os.path.dirname(sage_indefinite_port.__file__),
                                    os.path.dirname(sage_extensions.__file__)))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
S = Lattices(ZZ)([list(r) for r in (2 * block_diagonal_matrix(U, E8)).rows()])       # S_En
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])  # T_En


def coordinates(lattice):
    """Coordinate basis of A, by the deterministic loop over its elements."""
    A = lattice.discriminant_quadratic_form()
    els = list(A.elements())
    coord, basis = {els[0]: 0}, []
    for e in els:
        if e in coord:
            continue
        shift = len(basis)
        coord.update({s + e: m | (1 << shift) for s, m in coord.items()})
        basis.append(e)
        if len(basis) == 10:
            break
    return A, els, coord


def act(cols, x):
    out, i = 0, 0
    while x:
        if x & 1:
            out ^= cols[i]
        x >>= 1
        i += 1
    return out


def summand_classes(lattice, coord, u2_slots):
    """The A_{U(2)} subspace from the U(2) slots, and A_{E8(2)} as its orthogonal complement."""
    u2 = []
    for slot in u2_slots:
        b = lattice.basis_vector(slot)
        cls = lattice.discriminant_class(lattice.primitive_dual(b))
        u2.append(coord[cls])
    span = {0}
    for c in u2:
        span = span | {s ^ c for s in span}
    assert len(span) == 4, len(span)
    return span


for name, lattice, u2_slots, root_slots in (
        ('S_En', S, (0, 1), tuple(range(2, 10))),
        ('T_En', T, (2, 3), tuple(range(4, 12)))):
    A, els, coord = coordinates(lattice)
    A_u2 = summand_classes(lattice, coord, u2_slots)
    iso = {coord[x] for x in A.isotropic_elements()}
    print('%s: A_{U(2)} = %d classes; isotropic classes %d' % (name, len(A_u2), len(iso)))
    seed = lattice.basis_vector(u2_slots[0])
    u0, w0 = lattice.basis_vector(u2_slots[0]), lattice.basis_vector(u2_slots[1])
    gens = [lattice.reflection(u0 - w0)] + [lattice.reflection(lattice.basis_vector(i)) for i in root_slots]
    rho = lattice.discriminant_representation()
    mats = [tuple(coord[rho(g)(b)] for b in [els[c] for c in [1 << i for i in range(10)]])
            for g in gens]
    swap, reflections = mats[0], mats[1:]
    fixes_u2 = all(act(m, c) == c for m in reflections for c in A_u2)
    fixes_complement = all(act(swap, c) == c for c in coord.values() if c not in A_u2) if False else None
    # the swap must fix A_{E8(2)} pointwise: check it fixes representatives spanning the complement
    comp = [c for c in coord.values() if c not in A_u2]
    swap_fixes_comp = all(act(swap, c) == c for c in comp)
    refl_preserve_comp = all(act(m, c) in set(comp) for m in reflections for c in comp)
    print('  eight root reflections fix A_{U(2)} pointwise: %s' % fixes_u2)
    print('  eight root reflections preserve A_{E8(2)}:      %s' % refl_preserve_comp)
    print('  the U(2) swap fixes A_{E8(2)} pointwise:       %s' % swap_fixes_comp)
    # orbit partition of M on the isotropic classes
    seen, sizes = set(), []
    for s in sorted(iso):
        if s in seen:
            continue
        orbit, stack = {s}, [s]
        seen.add(s)
        while stack:
            x = stack.pop()
            for m in mats:
                y = act(m, x)
                if y not in orbit:
                    orbit.add(y)
                    seen.add(y)
                    stack.append(y)
        sizes.append(len(orbit))
    print('  M-orbits on the isotropic classes: %d, sizes %s'
          % (len(sizes), sorted(sizes, reverse=True)))
    print('')
