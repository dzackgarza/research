"""Exact short ordinary words for all 19 Eichler normal kernel relations."""
import hashlib
import json
from pathlib import Path

from sage.all import ZZ, identity_matrix, matrix

root = Path.cwd() / "computations" / "reports"
if not (root / "coble_kernel_fifty_six_congruence_generators.json").exists():
    root = Path(__file__).resolve().parent
ordinary_source = root / "coble_kernel_fifty_six_congruence_generators.json"
ambient_source = root / "coble_ambient_twenty_one_generators.json"
ordinary = json.loads(ordinary_source.read_text())
ambient = json.loads(ambient_source.read_text())
generators = [matrix(ZZ, row["matrix_standard"])
              for row in ordinary["generators"]]
ambient_generators = [matrix(ZZ, row["matrix_standard"])
                      for row in ambient["generators"]]
letters = generators + [g.inverse() for g in generators]
word_indices = [
    [25], [57], [11, 68], [12, 69], [13, 70], [14, 71],
    [15, 72], [16, 73], [16, 17], [2], [26, 3],
    [18, 35, 75, 90], [19, 36, 76, 91],
    [20, 37, 77, 92], [21, 38, 78, 93],
    [22, 39, 79, 94], [23, 40, 80, 95],
    [23, 95, 96, 24], [16],
]
assert len(word_indices) == 19
rows = []
identity = identity_matrix(ZZ, 11)
for target, word in zip(ambient["level_two_normal_relation_words"][:19],
                        word_indices, strict=True):
    target_matrix = identity
    for index in target:
        target_matrix *= ambient_generators[index]
    candidate = identity
    for index in word:
        candidate *= letters[index]
    assert candidate == target_matrix
    rows.append({
        "ambient_relation_indices": target,
        "ordinary_word": [
            [index if index < 56 else index - 56,
             1 if index < 56 else -1] for index in word
        ],
    })
result = {
    "schema": "coble-kernel-56-normal-relations-ordinary-words-v1",
    "ordinary_sha256": hashlib.sha256(ordinary_source.read_bytes()).hexdigest(),
    "ambient_sha256": hashlib.sha256(ambient_source.read_bytes()).hexdigest(),
    "relation_count": len(rows),
    "max_word_length": max(len(row["ordinary_word"]) for row in rows),
    "relations": rows,
}
(root / "coble_kernel_fifty_six_normal_relation_words.json").write_text(
    json.dumps(result, indent=2) + "\n")
print("Certified all 19 normal relations as ordinary words of length at most four")
