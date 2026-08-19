r"""Full discriminant-form isotropic orbits for the standard Coble target.

This is the finite computation for

    N = <2> + E_10(2) = 2B,  B = <1> + U + E_8(-1).

The discriminant group is identified with ``B/2B``.  The quadratic form is encoded by

    Q(v) = B(v,v) mod 4,

which represents ``2 q_N(v/2 + N)``.  Thus ``q_N``-isotropic classes are exactly the
``Q=0`` residue classes.

The group computed below is the full automorphism group of this finite quadratic form:
the subgroup of ``GL(B/2B)`` preserving all four fibers of ``Q``.  The final orbit
calculation is therefore a statement about ``Iso(A_N,q_N)/O(A_N,q_N)``.
"""

from sage.all import (
    GF,
    GL,
    ZZ,
    Permutation,
    PermutationGroup,
    block_diagonal_matrix,
    matrix,
    vector,
)
from sage.libs.gap.libgap import libgap

F = GF(2)
RANK = 11

E8 = matrix(
    ZZ,
    [
        [2, -1, 0, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, 0],
        [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, -1],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0],
        [0, 0, 0, 0, -1, 0, 0, 2],
    ],
)

GRAM_B = block_diagonal_matrix(
    matrix(ZZ, [[1]]),
    matrix(ZZ, [[0, 1], [1, 0]]),
    -E8,
)


def residue_vector(bits):
    r"""Return the element of ``B/2B`` encoded by an integer bitmask."""
    return vector(ZZ, [(bits >> i) & 1 for i in range(RANK)])


def quadratic_value(bits):
    r"""Return ``B(v,v) mod 4`` for a residue vector ``v in B/2B``."""
    v = residue_vector(bits)
    return int((v * GRAM_B * v.column())[0]) % 4


def act_bits(bits, g):
    r"""Return the bitmask for the right action of ``g in GL(B/2B)``."""
    v = vector(F, [(bits >> i) & 1 for i in range(RANK)])
    w = v * g
    return sum((1 << i) for i, entry in enumerate(w) if int(entry))


def main():
    r"""Compute ``Iso(A_N,q_N)/O(A_N,q_N)``."""
    general_linear_group = GL(RANK, F)
    action_generators = [
        Permutation([act_bits(bits, g) + 1 for bits in range(1 << RANK)])
        for g in general_linear_group.gens()
    ]
    permutation_action = PermutationGroup(action_generators)

    fibers = {
        value: [bits + 1 for bits in range(1 << RANK) if quadratic_value(bits) == value]
        for value in range(4)
    }

    orthogonal_group = permutation_action.gap()
    for value in range(4):
        orthogonal_group = libgap.Stabilizer(
            orthogonal_group,
            libgap(fibers[value]),
            libgap.OnSets,
        )

    isotropic_orbits = libgap.OrbitsDomain(
        orthogonal_group,
        libgap(fibers[0]),
        libgap.OnPoints,
    )

    print("fiber_sizes", {value: len(fibers[value]) for value in range(4)})
    print("group_order", orthogonal_group.Size())
    print("orbit_lengths", [int(orbit.Length()) for orbit in isotropic_orbits])
    print("representatives_as_bits", [int(orbit[0]) - 1 for orbit in isotropic_orbits])


if __name__ == "__main__":
    main()
