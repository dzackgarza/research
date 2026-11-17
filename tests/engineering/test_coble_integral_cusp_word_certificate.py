"""Independently replay every published integral Coble cusp word."""

import json
from math import gcd
from pathlib import Path


def test_all_coble_integral_cusp_words():
    source = (Path(__file__).resolve().parents[2] / "computations" / "reports"
              / "coble_singular_integral_representatives.json")
    data = json.loads(source.read_text())
    gram = data["standard_gram"]
    change = data["standard_to_diagonal"]
    roots = data["generator_roots_standard"]
    rows = data["representatives"]

    def pairing(a, b):
        return sum(a[i] * gram[i][j] * b[j]
                   for i in range(11) for j in range(11))

    assert len(roots) == 10 and len(rows) == 527
    assert len({row["mask_diagonal"] for row in rows}) == 527
    base, = (row["vector_standard"] for row in rows
             if row["mask_diagonal"] == data["base_mask_diagonal"])
    assert gcd(*base) == 1 and pairing(base, base) == 0
    stabilizer_roots = data["vector_stabilizer_roots_standard"]
    assert data["vector_stabilizer_finite_order"] == 89181388800
    stabilizer_masks = set()
    for root in stabilizer_roots:
        assert abs(pairing(root, root)) == 2
        assert pairing(root, base) == 0  # exact vector, not just its class
        diagonal = [sum(change[i][j] * root[j] for j in range(11))
                    for i in range(11)]
        stabilizer_masks.add(sum((x % 2) << i for i, x in enumerate(diagonal)))
    assert len(stabilizer_masks) == len(stabilizer_roots)
    base_mask = data["base_mask_diagonal"]
    expected_stabilizer_masks = {
        mask for mask in range(1 << 11)
        if mask.bit_count() % 2 == 0
        and (mask & base_mask).bit_count() % 2 == 0
        and (sum((1 if i < 2 else -1) * ((mask >> i) & 1)
                 for i in range(11)) // 2) % 2 == 1
    }
    assert stabilizer_masks == expected_stabilizer_masks
    ten_masks = data["vector_stabilizer_ten_masks"]
    ten_roots = data["vector_stabilizer_ten_roots_standard"]
    assert len(ten_masks) == len(ten_roots) == len(set(ten_masks)) == 10
    assert set(ten_masks) <= stabilizer_masks
    for expected_mask, root in zip(ten_masks, ten_roots):
        assert root in stabilizer_roots and pairing(root, base) == 0
        diagonal = [sum(change[i][j] * root[j] for j in range(11))
                    for i in range(11)]
        assert sum((x % 2) << i for i, x in enumerate(diagonal)) == expected_mask
    sample_mask = data["vector_stabilizer_sample_target_mask"]
    sample_word = data["vector_stabilizer_sample_word"]
    assert sample_mask in stabilizer_masks and sample_mask not in ten_masks
    assert sample_word and all(0 <= i < 10 and exponent != 0
                               for i, exponent in sample_word)
    target_root, = (root for root in stabilizer_roots
                    if sum((sum(change[i][j] * root[j] for j in range(11)) % 2)
                           << i for i in range(11)) == sample_mask)

    def reflection(v, root):
        n = pairing(root, root)
        numerator = 2 * pairing(v, root)
        assert numerator % n == 0
        k = numerator // n
        return [a - k * b for a, b in zip(v, root)]

    # Check the full mod-two matrix on an integral basis, not only one
    # chosen singular vector. The word's exact integral action fixes u.
    for j in range(11):
        e = [int(i == j) for i in range(11)]
        v = e
        for i, exponent in reversed(sample_word):
            if exponent % 2:
                v = reflection(v, ten_roots[i])
        target = reflection(e, target_root)
        assert all((a - b) % 2 == 0 for a, b in zip(v, target))
    v = list(base)
    for i, exponent in reversed(sample_word):
        if exponent % 2:
            v = reflection(v, ten_roots[i])
    assert v == base
    for root in roots:
        assert abs(pairing(root, root)) == 2

    for row in rows:
        v = list(base)
        for i in row["word_from_base"]:
            assert 0 <= i < 10
            root = roots[i]
            norm = pairing(root, root)
            numerator = 2 * pairing(v, root)
            assert numerator % norm == 0
            k = numerator // norm
            v = [a - k * b for a, b in zip(v, root)]
        assert v == row["vector_standard"]
        assert pairing(v, v) == 0 and gcd(*v) == 1
        diagonal = [sum(change[i][j] * v[j] for j in range(11))
                    for i in range(11)]
        mask = sum((x % 2) << i for i, x in enumerate(diagonal))
        assert mask == row["mask_diagonal"]
        # Conjugate the ten exact-vector parabolic generators by this
        # integral word. Their resulting reflections fix this *actual*
        # primitive isotropic vector, not just its discriminant class.
        conjugate_masks = set()
        for parabolic_root in ten_roots:
            transported = list(parabolic_root)
            for i in row["word_from_base"]:
                root = roots[i]
                n = pairing(root, root)
                numerator = 2 * pairing(transported, root)
                assert numerator % n == 0
                k = numerator // n
                transported = [a - k * b for a, b in zip(transported, root)]
            assert abs(pairing(transported, transported)) == 2
            assert pairing(transported, v) == 0
            diagonal_root = [sum(change[i][j] * transported[j]
                                 for j in range(11)) for i in range(11)]
            conjugate_masks.add(sum((x % 2) << i
                                    for i, x in enumerate(diagonal_root)))
        assert len(conjugate_masks) == 10
