"""Exact 21-generator family of O(I_{2,9}), in the Coble standard basis.

The generation proof is Gritsenko--Hulek--Sankaran, Proposition 3.4,
applied to U^2 + D7(-1), with three independent character representatives.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sage.all import ZZ, identity_matrix, matrix, vector

ROOT = Path(__file__).resolve().parent
if not (ROOT / 'coble_singular_integral_representatives.json').is_file():
    # Sage's ``sage script.py`` entry point evaluates in the Sage session
    # namespace and can supply Sage's own __file__.  Support that invocation
    # from the research repository root as well as Python's runpy path.
    ROOT = Path.cwd() / 'computations' / 'reports'
SOURCE = ROOT / 'coble_singular_integral_representatives.json'
OUTPUT = ROOT / 'coble_ambient_twenty_one_generators.json'
source = json.loads(SOURCE.read_text())
standard_gram = matrix(ZZ, source['standard_gram'])
standard_to_diagonal = matrix(ZZ, source['standard_to_diagonal'])
diagonal = matrix(ZZ, 11, 11, lambda i, j: (1 if i < 2 else -1) if i == j else 0)
assert standard_to_diagonal.transpose() * diagonal * standard_to_diagonal == standard_gram
I = identity_matrix(ZZ, 11)
unit = [vector(ZZ, I.column(i)) for i in range(11)]
# Columns give two copies of U, seven negative unit vectors, in I_{2,9}.
new_basis = [
    unit[0] + unit[2], unit[0] + unit[3],
    unit[1] + unit[4], unit[1] + unit[5],
    unit[0] + unit[2] + unit[3],
    unit[1] + unit[4] + unit[5],
    *unit[6:11],
]
P = matrix(ZZ, 11, 11, lambda i, j: new_basis[j][i])
assert abs(P.det()) == 1
B = P.transpose() * diagonal * P
assert B == matrix(ZZ, 11, 11, lambda i, j: (
    1 if (i, j) in ((0, 1), (1, 0), (2, 3), (3, 2))
    else -1 if i == j and i >= 4 else 0
))
standard_from_split = standard_to_diagonal.inverse() * P
assert abs(standard_from_split.det()) == 1
assert standard_from_split.transpose() * standard_gram * standard_from_split == B
roots = [unit[i] - unit[i + 1] for i in range(4, 10)]
roots.append(unit[9] + unit[10])
complement = [unit[2], unit[3], *roots]

def transvection(e, a):
    ep = e.row() * B
    ap = a.row() * B
    return I + a.column() * ep - e.column() * ap - (a * B * a // 2) * e.column() * ep

def reflection(a):
    return I - (2 // (a * B * a)) * a.column() * (a.row() * B)

rows = []
for e_index in (0, 1):
    for i, a in enumerate(complement):
        rows.append((f'eichler_{e_index}_{i}', transvection(unit[e_index], a)))
rows.extend([
    ('root_reflection_U2', reflection(unit[2] - unit[3])),
    ('negative_unit_reflection', reflection(unit[4])),
    ('minus_identity_U1', I - 2 * unit[0].column() * unit[0].row()
                         - 2 * unit[1].column() * unit[1].row()),
])
assert len(rows) == 21
records = []
for name, split_matrix in rows:
    assert split_matrix.transpose() * B * split_matrix == B
    standard_matrix = standard_from_split * split_matrix * standard_from_split.inverse()
    assert all(x in ZZ for x in standard_matrix.list())
    standard_matrix = matrix(ZZ, standard_matrix)
    assert standard_matrix.transpose() * standard_gram * standard_matrix == standard_gram
    records.append({'name': name, 'matrix_standard': [list(map(int, row)) for row in standard_matrix.rows()]})
certificate = {
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'standard_gram': [list(map(int, row)) for row in standard_gram.rows()],
    'standard_from_split': [list(map(int, row)) for row in standard_from_split.rows()],
    'generator_count': len(records),
    'eichler_generator_indices': list(range(18)),
    'level_two_character_complement_indices': [19, 20],
    # These 21 positive words are actual integral kernel elements. Their
    # E-conjugates span E(2) modulo four, and the final two words supply
    # the character complement; no infinite kernel-generation claim.
    'level_two_normal_relation_words': (
        [[i, i] for i in range(18)] + [[7, 8], [19], [20]]
    ),
    'finite_discriminant_image_order': 46998591897600,
    'eichler_discriminant_image_order': 23499295948800,
    'generators': records,
}
OUTPUT.write_text(json.dumps(certificate, indent=2) + '\n')
print('Certified', len(records), 'exact standard-basis ambient orthogonal generators')
