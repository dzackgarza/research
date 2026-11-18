"""Exact integral Lie closure of the unipotent 56-kernel candidates."""
import hashlib
import json
from pathlib import Path

from sage.all import ZZ, identity_matrix, matrix

root = Path.cwd() / "computations" / "reports"
if not (root / "coble_kernel_fifty_six_congruence_generators.json").exists():
    root = Path(__file__).resolve().parent
source = root / "coble_kernel_fifty_six_congruence_generators.json"
diagonal_source = root / "coble_singular_integral_representatives.json"
data = json.loads(source.read_text())
change = matrix(ZZ, json.loads(diagonal_source.read_text())["standard_to_diagonal"])
inverse = change.inverse()
identity = identity_matrix(ZZ, 11)
initial = []
indices = []
for i, row in enumerate(data["generators"]):
    nilpotent = matrix(ZZ, row["matrix_standard"]) - identity
    if nilpotent != 0 and nilpotent**3 == 0:
        log = change * (nilpotent - nilpotent**2 / 2) * inverse
        assert all(entry in ZZ for entry in log.list())
        initial.append(matrix(ZZ, log))
        indices.append(i)
pairs = [(i, j) for i in range(11) for j in range(i + 1, 11)]
basis = matrix(ZZ, [[a[i, j] for i, j in pairs] for a in initial]).hermite_form()
basis = matrix(ZZ, [row for row in basis.rows() if row != 0])
initial_rank = basis.rank()
iterations = 0
while True:
    matrices = []
    for row in basis.rows():
        a = matrix(ZZ, 11, 11)
        for entry, (i, j) in zip(row, pairs, strict=True):
            a[i, j] = entry
            a[j, i] = -(-1 if i < 2 else 1) * (-1 if j < 2 else 1) * entry
        matrices.append(a)
    entries = [[a[i, j] for i, j in pairs] for a in matrices]
    entries.extend([(a * b - b * a)[i, j] for i, j in pairs]
                   for a in matrices for b in initial)
    updated = matrix(ZZ, entries).hermite_form()
    updated = matrix(ZZ, [row for row in updated.rows() if row != 0])
    iterations += 1
    if updated == basis:
        break
    basis = updated
assert len(indices) == 46 and initial_rank == 46
assert basis.rank() == 55 and abs(basis.det()) == 2**64
result = {
    "schema": "coble-kernel-56-unipotent-lie-span-v1",
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "diagonal_source_sha256": hashlib.sha256(diagonal_source.read_bytes()).hexdigest(),
    "unipotent_indices": indices,
    "initial_rank": int(initial_rank),
    "lie_rank": int(basis.rank()),
    "integral_index": int(abs(basis.det())),
    "iterations": iterations,
}
(root / "coble_kernel_fifty_six_lie_span.json").write_text(
    json.dumps(result, indent=2) + "\n")
print("Certified full rank 55 over Z[1/2], index", result["integral_index"])
