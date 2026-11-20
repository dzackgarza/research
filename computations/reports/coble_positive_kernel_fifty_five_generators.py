"""Select 55 independent positive kernel matrices from the 95 Schreier generators.

This certifies finite congruence generation, not infinite ordinary generation.
"""
import hashlib
import json
from pathlib import Path

from sage.all import ZZ, matrix

ROOT = Path(__file__).resolve().parent
if not (ROOT / 'coble_kernel_positive_schreier_generators.json').exists():
    ROOT = Path.cwd() / 'computations/reports'
source = ROOT / 'coble_kernel_positive_schreier_generators.json'
rows = json.loads(source.read_text())['generators']
pivots = {}
chosen = []
for i, row in enumerate(rows):
    g = matrix(ZZ, row['matrix_standard'])
    bits = sum((((int(g[a,b]) - int(a == b)) // 2) % 2) << (11*a+b)
               for a in range(11) for b in range(11))
    while bits:
        p = bits.bit_length() - 1
        if p in pivots:
            bits ^= pivots[p]
        else:
            pivots[p] = bits
            chosen.append(i)
            break
assert len(chosen) == 55
assert chosen == list(range(55))
certificate = {
    'schema': 'coble-positive-kernel-55-ordinary-mod-sixteen-v1',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'source_generator_indices': chosen,
    'generator_count': 55,
    'mod_four_image_rank': 55,
    'generators': [rows[i] for i in chosen],
}
(ROOT / 'coble_positive_kernel_fifty_five_generators.json').write_text(
    json.dumps(certificate, indent=2) + '\n'
)
print('Certified 55 independent positive kernel generators modulo four')
