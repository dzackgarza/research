"""research#663 (REL): the odd-local perfection input of the repaired Step 3.

The argument.  With K_ell the closure of W~ in G_ell = Spin(Z_ell) and P_ell the kernel of reduction
modulo ell, K_ell is open and normal and G_ell = K_ell P_ell, so G_ell/K_ell = P_ell/(P_ell cap K_ell)
is a finite ell-group.  A perfect G_ell therefore has K_ell = G_ell.  The perfection of G_ell is
proved level by level: the reduction modulo ell is the finite simply connected Chevalley group
Spin_11(F_ell), which is perfect, and each principal congruence layer is the adjoint module
so_11(F_ell), on which the finite group has no nonzero coinvariants.  For ell >= 17 that is the
irreducibility of the adjoint module (as in @thm:coble-fifty-six-all-odd-prime-powers).  For
ell = 3, 5, 7, 11, 13 it is the rank-55 commutator condition recorded here.

What this file computes.  From the certified 46 integral unipotents of
@prop:coble-ordinary-fifty-six-congruence-generators, transported to the diagonal basis of B = I_{2,9},
it forms the span over F_ell of all differences Ad(g)A - A, for A in the 55-dimensional basis
E_ij - eps_i eps_j E_ji of so_11(F_ell) and g one of the 46 unipotents, and reports the rank.  The
span over the 46 generators is the span over the group they generate: the quotient by it is fixed by
each generator, hence by the group.

This is the only odd-prime computation the repaired Step 3 uses.  The rank-55 layer computations of
W itself at ell = 3,...,13, which the kernel's round 7 used, are not needed: the repaired argument
gets the odd-local fullness from openness, normality, the bottom image and perfection.

Usage:  sage computations/reports/coble_663-rel-odd-local-perfection.py
"""

import hashlib
import json
from pathlib import Path

from sage.all import GF, ZZ, matrix
from sage_extensions.all import Lattices, NamedLattices

REPORT = Path(__file__).resolve().parent


def library_gram(lattice):
    gram = lattice.gram_matrix()
    return matrix(ZZ, 11, 11, lambda i, j: ZZ(gram.matrix_entry(i, j)))


T_COBLE = NamedLattices.Tco
GRAM_T = library_gram(T_COBLE)
HALVED = GRAM_T / 2
B_TWISTED = Lattices(ZZ)([[ZZ(HALVED[i, j]) for j in range(11)] for i in range(11)])
B = Lattices(ZZ).IPQ(2, 9)
GRAM_B = library_gram(B)
TWIST = matrix(ZZ, B_TWISTED.isometry_to(B)._engine_coordinate_matrix())
assert TWIST.transpose() * GRAM_B * TWIST == HALVED
EPSILON = [int(GRAM_B[i, i]) for i in range(11)]
assert EPSILON == [1, 1] + [-1] * 9

source = REPORT / "coble_kernel_fifty_six_congruence_generators.json"
data = json.loads(source.read_text())
matrices = [matrix(ZZ, row["matrix_standard"]) for row in data["generators"]]
unipotents = [g for g in matrices if (g - matrix(ZZ, 11, 11, 1)) ** 3 == 0]
assert len(unipotents) == 46, len(unipotents)

records = []
for prime in (3, 5, 7, 11, 13):
    field = GF(prime)
    finite = [matrix(field, TWIST * g * TWIST.inverse()) for g in unipotents]
    for g in finite:
        assert g.transpose() * matrix(field, GRAM_B) * g == matrix(field, GRAM_B)
    pivots = {}

    def add(entries):
        vector = [field(entry) for entry in entries]
        while True:
            pivot = next((i for i, value in enumerate(vector) if value), None)
            if pivot is None:
                return
            if pivot in pivots:
                coefficient = vector[pivot]
                vector = [value - coefficient * other for value, other in zip(vector, pivots[pivot])]
            else:
                coefficient = vector[pivot]
                vector = [value / coefficient for value in vector]
                pivots[pivot] = vector
                return

    for i in range(11):
        for j in range(i + 1, 11):
            elementary = matrix(field, 11, 11)
            elementary[i, j] = 1
            elementary[j, i] = -(-1 if i < 2 else 1) * (-1 if j < 2 else 1)
            for g in finite:
                add((g * elementary * g.inverse() - elementary).list())
    rank = len(pivots)
    assert rank == 55, (prime, rank)
    records.append({"prime": prime, "adjoint_commutator_rank": rank,
                    "dim_so_11": 55, "coinvariants_vanishing": rank == 55})

record = {
    "schema": "coble-663-rel-odd-local-perfection-v1",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "unipotent_count": len(unipotents),
    "records": records,
}
(REPORT / "coble_663-rel-odd-local-perfection.json").write_text(json.dumps(record, indent=2) + "\n")

lines = [
    "research#663 (REL): the odd-local perfection input of the repaired Step 3",
    "=" * 92,
    f"script sha256: {record['script_sha256']}",
    f"source sha256: {record['source_sha256']}",
    "",
    "G_ell = Spin(Z_ell) is perfect if every finite congruence quotient is: the mod-ell quotient is",
    "the finite simply connected Chevalley group Spin_11(F_ell) (perfect), and each principal",
    "congruence layer is the adjoint module so_11(F_ell), whose coinvariants vanish.",
    "",
    "adjoint coinvariants, exact rank over F_ell:",
]
for row in records:
    lines.append(f"  ell = {row['prime']:2d}: rank {row['adjoint_commutator_rank']} of {row['dim_so_11']}"
                 f"  -> no nonzero coinvariants")
lines += [
    "",
    "For ell >= 17 the same vanishing is the irreducibility of the adjoint module",
    "(@thm:coble-fifty-six-all-odd-prime-powers); no computation is used there.",
    "The rank-55 layer computations of W at odd ell are NOT used by the repaired Step 3.",
    "",
]
(REPORT / "coble_663-rel-odd-local-perfection-run.txt").write_text("\n".join(lines))
print("\n".join(lines))
