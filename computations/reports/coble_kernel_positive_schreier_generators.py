"""Reidemeister--Schreier ordinary generators of the positive Coble kernel."""
import hashlib
import json
from pathlib import Path
from sage.all import ZZ, identity_matrix, matrix

ROOT = Path(__file__).resolve().parent
if not (ROOT / "coble_kernel_fifty_six_congruence_generators.json").exists():
    ROOT = Path.cwd() / "computations/reports"
SOURCE = ROOT / "coble_kernel_fifty_six_congruence_generators.json"
BASIS = ROOT / "coble_singular_integral_representatives.json"
data = json.loads(SOURCE.read_text())
C = matrix(ZZ, json.loads(BASIS.read_text())["standard_to_diagonal"])
G = [matrix(ZZ, item["matrix_standard"]) for item in data["generators"]]
gram = matrix(ZZ, json.loads((ROOT / "coble_ambient_twenty_one_generators.json").read_text())["standard_gram"])

def positive_orientation_sign(g):
    """GHS real spinor sign (multiplier -1/2), via positive 2-plane orientation."""
    d = C * g * C.inverse()
    determinant = d[:2, :2].det()
    assert determinant
    return 1 if determinant > 0 else -1

signs = [positive_orientation_sign(g) for g in G]
assert -1 in signs
negative_index = signs.index(-1)
reps = [identity_matrix(ZZ, 11), G[negative_index]]
records = []
seen = set()
for coset, rep in enumerate(reps):
    for j, g in enumerate(G):
        target = coset ^ int(signs[j] == -1)
        h = rep * g * reps[target].inverse()
        assert h.transpose() * gram * h == gram
        assert positive_orientation_sign(h) == 1
        assert all((h[i, k] - int(i == k)) % 2 == 0 for i in range(11) for k in range(11))
        if h == reps[0]:
            continue
        key = tuple(map(int, h.list()))
        if key in seen:
            continue
        seen.add(key)
        records.append({"coset": coset, "source_generator": j,
                        "matrix_standard": [list(map(int, row)) for row in h.rows()]})
payload = {"schema": "coble-positive-kernel-ordinary-schreier-v1",
           "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           "basis_source_sha256": hashlib.sha256(BASIS.read_bytes()).hexdigest(),
           "negative_coset_generator_index": negative_index,
           "generator_count": len(records), "generators": records}
(ROOT / "coble_kernel_positive_schreier_generators.json").write_text(json.dumps(payload, indent=2) + "\n")
print("Certified", len(records), "positive real-spinor ordinary generators")
