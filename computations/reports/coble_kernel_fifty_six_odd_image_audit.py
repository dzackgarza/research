"""Exact GAP order of the 56 ordinary kernel candidates modulo an odd prime.

This certifies a finite image, not ordinary generation of the infinite kernel.
Run: sage computations/reports/coble_kernel_fifty_six_odd_image_audit.py 3
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from sage.all import GF, is_prime, matrix
from sage.libs.gap.libgap import libgap

root = Path.cwd() / "computations" / "reports"
if not (root / "coble_kernel_fifty_six_congruence_generators.json").exists():
    root = Path(__file__).resolve().parent
source = root / "coble_kernel_fifty_six_congruence_generators.json"
prime = int(sys.argv[1]) if len(sys.argv) > 1 else 3
assert prime > 2 and is_prime(prime)
data = json.loads(source.read_text())
generators = [matrix(GF(prime), row["matrix_standard"])
              for row in data["generators"]]
group = libgap.Group([libgap(g) for g in generators])
computed = int(libgap.Size(group))
expected = 2 * prime**25
for i in range(1, 6):
    expected *= prime ** (2 * i) - 1
print(json.dumps({
    "prime": prime,
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "matrix_count": len(generators),
    "generated_order": computed,
    "full_odd_orthogonal_order": expected,
    "full_image": computed == expected,
}, indent=2))
assert computed == expected
