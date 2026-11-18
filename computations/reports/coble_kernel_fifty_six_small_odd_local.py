"""Finite classical recognition and first p-adic layer for small odd primes."""
import hashlib
import json
from pathlib import Path

from sage.all import GF, ZZ, Integers, identity_matrix, matrix, vector
from sage.libs.gap.libgap import libgap

libgap.LoadPackage("recog")
libgap.LoadPackage("classical")
root = Path.cwd() / "computations" / "reports"
if not (root / "coble_kernel_fifty_six_congruence_generators.json").exists():
    root = Path(__file__).resolve().parent
source = root / "coble_kernel_fifty_six_congruence_generators.json"
data = json.loads(source.read_text())
matrices = [matrix(ZZ, row["matrix_standard"]) for row in data["generators"]]
unipotents = [g for g in matrices if (g - identity_matrix(ZZ, 11))**3 == 0]
assert len(unipotents) == 46
records = []
for prime in (3, 5, 7, 11, 13):
    field = GF(prime)
    finite = [matrix(field, g) for g in matrices]
    group = libgap.Group([libgap(g) for g in finite])
    recognition = libgap.RecogniseClassical(group)
    assert str(recognition["isOmegaContained"]) == "true"
    assert str(recognition["QuadraticFormType"]) == "orthogonalcircle"
    inverse = [g.inverse() for g in finite]
    ring = Integers(prime * prime)
    pivots = {}
    queue = []

    def admit(element):
        values = vector(field, element.list())
        while values:
            pivot = next(i for i, value in enumerate(values) if value)
            if pivot in pivots:
                values -= values[pivot] * pivots[pivot]
            else:
                values /= values[pivot]
                pivots[pivot] = values
                queue.append(matrix(field, 11, 11, values))
                return

    for generator in unipotents:
        power = matrix(ring, generator) ** prime
        assert all(int(power[i, j]) % prime == int(i == j)
                   for i in range(11) for j in range(11))
        admit(matrix(field, 11, 11, [
            ((int(power[i, j]) - int(i == j)) // prime) % prime
            for i in range(11) for j in range(11)
        ]))
    position = 0
    while position < len(queue):
        element = queue[position]
        position += 1
        for generator, inv in zip(finite, inverse, strict=True):
            admit(generator * element * inv)
    assert len(pivots) == 55
    records.append({
        "prime": prime,
        "contains_omega": True,
        "orthogonal_type": "odd_dimension_11",
        "principal_p_layer_rank": len(pivots),
    })
    print("Certified local prime", prime, "rank", len(pivots), flush=True)
result = {
    "schema": "coble-kernel-56-small-odd-local-v1",
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "records": records,
}
(root / "coble_kernel_fifty_six_small_odd_local.json").write_text(
    json.dumps(result, indent=2) + "\n")
