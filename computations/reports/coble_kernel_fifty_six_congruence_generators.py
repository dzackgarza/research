"""Exact 56 ordinary integral kernel elements spanning Gamma(2) modulo four.

This is a finite congruence certificate, NOT a proof that these 56 elements
ordinarily generate the infinite integral level-two kernel.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sage.all import GF, ZZ, identity_matrix, matrix

ROOT = Path(__file__).resolve().parent
if not (ROOT / 'coble_plane_parabolic_level_two_generators.json').is_file():
    ROOT = Path.cwd() / 'computations' / 'reports'
P = ROOT / 'coble_plane_parabolic_level_two_generators.json'
A = ROOT / 'coble_ambient_twenty_one_generators.json'
parabolic = json.loads(P.read_text())
ambient = json.loads(A.read_text())
K = [matrix(ZZ, row) for row in parabolic['generators_standard']]
E = [matrix(ZZ, row['matrix_standard']) for row in ambient['generators']]
I = identity_matrix(ZZ, 11)
D = matrix(ZZ, ambient['standard_gram'])
pivots = {}
rows = []

def add(g, source):
    assert g.transpose() * D * g == D
    assert matrix(GF(2), g) == identity_matrix(GF(2), 11)
    bits = sum((((int(g[i, j]) - int(i == j)) // 2) % 2) << (11 * i + j)
               for i in range(11) for j in range(11))
    while bits:
        pivot = bits.bit_length() - 1
        if pivot in pivots:
            bits ^= pivots[pivot]
        else:
            pivots[pivot] = bits
            rows.append({'source': source,
                         'matrix_standard': [list(map(int, row)) for row in g.rows()]})
            return

for j, g in enumerate(K):
    add(g, {'parabolic_generator_index': j, 'conjugating_ambient_index': None})
for i in range(10, 16):
    h = E[i]
    for j, g in enumerate(K):
        add(h * g * h.inverse(),
            {'parabolic_generator_index': j, 'conjugating_ambient_index': i})
assert len(rows) == len(pivots) == 56
payload = {
    'schema': 'coble-kernel-56-ordinary-mod-four-v1',
    'parabolic_sha256': hashlib.sha256(P.read_bytes()).hexdigest(),
    'ambient_sha256': hashlib.sha256(A.read_bytes()).hexdigest(),
    'generator_count': 56,
    'mod_four_image_rank': 56,
    'generators': rows,
}
output = ROOT / 'coble_kernel_fifty_six_congruence_generators.json'
output.write_text(json.dumps(payload, indent=2) + '\n')
print('Certified 56 ordinary integral kernel matrices, mod-four rank 56')
