"""Minimal reproduction: reflection() refuses a non-primitive reflection vector.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/se_reflection_nonprimitive_repro.py

Library: sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee, Lattices.reflection().

The contract as documented.  reflection(root) requires root.is_integral_reflection_vector(),
whose meaning is: for every selected module generator e_i, 2 * b(e_i, root) / b(root, root) lies
in the base ring.  The docstring says the reflection "exists exactly when root is an integral
reflection vector".  That biconditional fails for non-primitive root: with a primitive of square
-2 and root = 2a, the scalar 2 b(x, 2a) / b(2a, 2a) = b(x, a) / (-2) * 2 ... is half-integral for
x with b(x, a) odd, while the reflection it is supposed to build,
x |-> x - (2 b(x, root) / b(root, root)) root = x + b(x, a) a, is integral and is exactly the
reflection in a, which the library builds without complaint.

What the library owner could do, in the API as published: either state the contract for primitive
root, or test the image rather than the scalar -- i.e. check that
(2 b(e_i, root) / b(root, root)) * root lies in the lattice for every generator e_i, which is the
condition for the map to preserve the lattice.  No workaround is implemented here or anywhere in
this repository: the primitive cases are the ones the certificates use.
"""
from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

U = matrix(ZZ, [[0, 1], [1, 0]])
D17 = -CartanMatrix(['D', 17])
L = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(U, U, D17).rows()])
basis = [L.basis_vector(i) for i in range(21)]

a = L.basis_vector(4)                    # a primitive (-2)-root of the D_17 summand
root = 2 * a
print('a is primitive, q(a) = %s; root = 2a, q(root) = %s' % (a.q(), root.q()))
print('is_integral_reflection_vector, a:     %s' % a.is_integral_reflection_vector())
print('is_integral_reflection_vector, 2a:   %s' % root.is_integral_reflection_vector())

reflection_a = L.reflection(a)
print('reflection(a) built; it is an involution: %s'
      % all(reflection_a(reflection_a(v)) == v for v in basis))

try:
    L.reflection(root)
    print('reflection(2a) built, which would be the defect the other way round')
except ValueError as error:
    print('reflection(2a) raised ValueError:')
    print('   %s' % str(error).split(':', 1)[-1].strip()[:160])

# The two are one map.  With r = 2a the formula is
#   x -> x - (2 b(x, r)/b(r, r)) r = x - (2 * 2 b(x,a) / (4 b(a,a))) * 2a = x + b(x,a) a,
# which is exactly reflection(a): x -> x - (2 b(x,a)/b(a,a)) a with b(a,a) = -2.  The scalar for
# r is -b(x,a)/2, half-integral when b(x,a) is odd, while the image is integral.
agree = all(reflection_a(x) == x + int(x.b(a)) * a for x in basis)
print('reflection(a) satisfies x -> x + b(x,a) a on every basis vector: %s' % agree)
odd = [i for i, x in enumerate(basis) if int(x.b(a)) % 2 != 0]
print('generators x with b(x,a) odd, i.e. with a half-integral scalar for r = 2a: %s' % odd)
print()
print('So the refused map is an integral, well-defined isometry, rejected on the strength of a')
print('scalar that is not itself integral.  The defect is conservative -- a false negative -- and')
print('belongs to sage-extensions; nothing in this repository depends on the refused case.')
