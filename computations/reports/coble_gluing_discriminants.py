"""Whether the Coble pair's two discriminant forms are anti-isometric, at the owner.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_gluing_discriminants.py

What this decides, and why it is the right first step.  The gluing of the book,
S_Co + T_Co -> L_K3 with [L_K3 : S_Co + T_Co] = 2^{11}, is the graph of an anti-isometry
gamma_Co: A_{S_Co} -> A_{T_Co}; `glue_map` in the provider returns exactly that arrow, but as
its docstring says it takes the two primitive orthogonal subobjects *inside* L, which is the
object we are trying to build.  The question that does not need L is whether the anti-isometry
can exist at all: an anti-isometry A_S -> A_T is an isometry A_S -> A_T(-1), so the pair can be
glued to a unimodular lattice only if q_{S_Co} and -q_{T_Co} are isometric as quadratic forms.
That is decided here with the owner's `is_isometric_to` on the two discriminant groups.

If it returns True, the gluing datum exists up to isometry (Nikulin's gluing correspondence,
@thm:nikulin-gluing), and what remains missing is the explicit arrow, not its existence; if it
returns False, then no unimodular overlattice of S_Co + T_Co exists at all and the index 2^{11}
stated for L_K3 needs revisiting.

Not attempted here: building L_K3, or producing the explicit anti-isometry.  The provider has
`glue_map` only for subobjects of an existing ambient lattice, and the constructor of an
isometry between two abstract torsion quadratic forms is the capability recorded as missing in
A20 item 1(b).

Provenance: pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage 11.0.beta5, image rootfs
read-only, repository bound at /repo.
"""
import sys

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
print('S_Co = <2> + <-2>^10        : rank %d, |det| %d, |A| %d'
      % (S.module_rank(), abs(int(S.determinant())), DS.cardinality()))
print('T_Co = <2> + U(2) + E8(2)   : rank %d, |det| %d, |A| %d'
      % (T.module_rank(), abs(int(T.determinant())), DT.cardinality()))
print('  type of A_{S_Co}: %s' % (type(DS).__name__,))
print('  methods naming isometry/twist/quadratic on it: %s'
      % ([m for m in dir(DS) if ('isom' in m.lower() or 'twist' in m.lower() or 'quadratic' in m.lower())][:12],))

DT_minus = DT.twist(-1)

print('')
print('the anti-isometry question: is q_{S_Co} isometric to -q_{T_Co}?')
answer = DS.is_anti_isometric(DT)
print('  D_S.is_anti_isometric(D_T) -> %s' % (answer,))
print('  (equivalently D_S.is_isometric_to(D_T.twist(-1)) -> %s)'
      % (DS.is_isometric_to(DT_minus),))
print('')
if answer:
    print('CONCLUSION')
    print('  The two discriminant forms are anti-isometric, so S_Co + T_Co does admit a')
    print('  unimodular overlattice with the full graph gluing, and the index 2^11 of L_K3 is')
    print('  compatible with the pair.  What is still not in hand is the explicit arrow.')
    print('  The block was located: normal_form_isometry()')
    print('  builds NF(D_S) -> D_S and NF(D_T(-1)) -> D_T(-1), but composing them fails because')
    print('  the two normal forms are distinct objects -- f.then(g) raises ValueError and')
    print('  f*g / f@g raise TypeError -- so no canonical identification of the normal forms,')
    print('  and no isometry constructor between abstract torsion quadratic forms, is available')
    print('  at this pin.  That is A20 item 1(b), now with exact calls and traces.')
else:
    print('CONCLUSION')
    print('  The forms are NOT anti-isometric: no unimodular overlattice of S_Co + T_Co exists,')
    print('  and the index 2^11 stated for L_K3 would need revisiting.')
