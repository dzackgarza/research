"""Independently replay the complete finite-to-integral Coble plane section."""

import json
import hashlib
import subprocess
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path

import pytest


def test_all_coble_integral_plane_star_words():
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    data = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    section = json.loads((folder / "coble_plane_integral_star_section.json").read_text())
    gram = data["standard_gram"]
    change = data["standard_to_diagonal"]
    roots = data["generator_roots_standard"]
    base = section["base_planes_standard"]
    seed_roots = section["seed_reflection_roots_standard"]
    stars = section["base_stars_quotient_classes"]
    flag_coefficients = section["flag_line_coefficients"]
    rows = section["finite_plane_transports"]
    stabilizer = section["plane_stabilizer_generators_standard"]

    def pairing(a, b):
        return sum(a[i] * gram[i][j] * b[j]
                   for i in range(11) for j in range(11))

    def mask(v):
        diagonal = [sum(change[i][j] * v[j] for j in range(11))
                    for i in range(11)]
        return sum((x % 2) << i for i, x in enumerate(diagonal))

    def key(a, b):
        x, y = mask(a), mask(b)
        return tuple(sorted((x, y, x ^ y)))

    assert len(base) == 8 and len(rows) == 23715
    assert len(stabilizer) == 21
    assert section["plane_stabilizer_finite_image_order"] == 247726080
    assert len(seed_roots) == 7
    assert len({tuple(row["finite_plane_masks"]) for row in rows}) == 23715
    assert len({tuple(star) for star in stars}) == 8
    root_masks = [mask(root) for root in roots]
    assert flag_coefficients == [[1, 0], [0, 1], [1, 1]]
    assert len(rows) * len(base) * len(flag_coefficients) == 569160
    expected_line_masks = {row["mask_diagonal"] for row in data["representatives"]}
    line_degrees = Counter()
    base_key = key(*base[0])
    def plucker(a, b):
        minors = tuple(a[i] * b[j] - a[j] * b[i]
                       for i, j in combinations(range(11), 2))
        first = next(x for x in minors if x)
        return minors if first > 0 else tuple(-x for x in minors)

    base_plucker = plucker(*base[0])
    for g in stabilizer:
        assert len(g) == 11 and all(len(row) == 11 for row in g)
        for i in range(11):
            for j in range(11):
                assert sum(g[k][i] * gram[k][l] * g[l][j]
                           for k in range(11) for l in range(11)) == gram[i][j]
        images = [[sum(g[i][j] * v[j] for j in range(11))
                   for i in range(11)] for v in base[0]]
        assert plucker(*images) == base_plucker
    # Independently recompute the faithful finite image, rather than
    # trusting the order recorded by the certificate producer.
    from sage.all import ZZ, PermutationGroup, identity_matrix, matrix, vector

    diagonal_change = matrix(ZZ, change)
    inverse_change = diagonal_change.inverse()
    singular = sorted(row["mask_diagonal"] for row in data["representatives"])
    positions = {mask: i + 1 for i, mask in enumerate(singular)}
    permutations = []
    for g in stabilizer:
        diagonal_action = diagonal_change * matrix(ZZ, g) * inverse_change
        permutation = []
        for x in singular:
            image = diagonal_action * vector(ZZ, [(x >> i) & 1 for i in range(11)])
            y = sum((int(a) & 1) << i for i, a in enumerate(image))
            permutation.append(positions[y])
        permutations.append(permutation)
    assert int(PermutationGroup(permutations).order()) == 247726080
    sample = section["ambient_transporter_sample"]
    sample_matrix = sample["matrix_standard"]
    kernel_matrix = sample["kernel_matrix_standard"]
    positive_matrix = sample["positive_kernel_matrix_standard"]
    spinor_flip_matrix = sample["spinor_flip_matrix_standard"]
    assert len(sample_matrix) == 11 and all(len(r) == 11 for r in sample_matrix)
    sample_line, = (r for r in data["representatives"]
                    if r["mask_diagonal"] == sample["line_mask_diagonal"])
    line_vector = sample_line["vector_standard"]
    flag_vector = sample["flag_vector_standard"]
    assert [sum(sample_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert [sum(kernel_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert all(kernel_matrix[i][j] % 2 == int(i == j)
               for i in range(11) for j in range(11))
    assert [sum(positive_matrix[i][j] * line_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert [sum(spinor_flip_matrix[i][j] * flag_vector[j] for j in range(11))
            for i in range(11)] == flag_vector
    assert all(positive_matrix[i][j] % 2 == int(i == j)
               and spinor_flip_matrix[i][j] % 2 == int(i == j)
               for i in range(11) for j in range(11))
    assert pairing(flag_vector, flag_vector) == 0 and gcd(*flag_vector) == 1
    assert mask(flag_vector) == sample["line_mask_diagonal"]
    assert tuple(sample["finite_plane_masks"]) in {
        tuple(r["finite_plane_masks"]) for r in rows
    }
    assert sample["line_mask_diagonal"] in sample["finite_plane_masks"]
    for i in range(11):
        for j in range(11):
            assert sum(sample_matrix[k][i] * gram[k][l] * sample_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
            assert sum(kernel_matrix[k][i] * gram[k][l] * kernel_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
            assert sum(positive_matrix[k][i] * gram[k][l] * positive_matrix[l][j]
                       for k in range(11) for l in range(11)) == gram[i][j]
    # Independently reconstruct both matrices from the finite-plane word,
    # seed reflection, GL2 flag map, line word, and parabolic correction.
    def reflection_matrix(root):
        r = vector(ZZ, root)
        n = pairing(root, root)
        assert abs(n) == 2
        return identity_matrix(ZZ, 11) - (2 // n) * (
            r.column() * (r.row() * matrix(ZZ, gram))
        )

    def word_matrix(word, generators):
        result = identity_matrix(ZZ, 11)
        for index in word:
            result = reflection_matrix(generators[index]) * result
        return result

    sample_plane, = (r for r in rows
                     if r["finite_plane_masks"] == sample["finite_plane_masks"])
    plane_word = word_matrix(sample_plane["word_from_base"], roots)
    line_word = word_matrix(sample_line["word_from_base"], roots)
    seed_reflection = reflection_matrix(
        section["seed_reflection_roots_standard"][sample["seed_index"] - 1]
    )
    flag_maps = [identity_matrix(ZZ, 11), matrix(ZZ, stabilizer[-2]),
                 matrix(ZZ, stabilizer[-1])]
    flag_map = flag_maps[sample["flag_index"]]
    reconstructed_ambient = plane_word * seed_reflection * flag_map * line_word.inverse()
    assert reconstructed_ambient == matrix(ZZ, sample_matrix)
    parabolic_word = identity_matrix(ZZ, 11)
    for index, exponent in sample["parabolic_correction_word"]:
        parabolic_word = (reflection_matrix(
            data["vector_stabilizer_ten_roots_standard"][index]
        ) ** exponent) * parabolic_word
    correction = line_word * parabolic_word * line_word.inverse()
    assert reconstructed_ambient * correction.inverse() == matrix(ZZ, kernel_matrix)
    diagonal_kernel = diagonal_change * matrix(ZZ, kernel_matrix) * inverse_change
    diagonal_flip = diagonal_change * matrix(ZZ, spinor_flip_matrix) * inverse_change
    diagonal_positive = diagonal_change * matrix(ZZ, positive_matrix) * inverse_change
    positive_minor = lambda m: m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]
    assert positive_minor(diagonal_flip) < 0
    assert positive_minor(diagonal_positive) > 0
    sign = 1 if positive_minor(diagonal_kernel) > 0 else -1
    assert sign == sample["kernel_real_spinor_sign"]
    assert matrix(ZZ, positive_matrix) == (
        matrix(ZZ, kernel_matrix) if sign == 1 else
        matrix(ZZ, spinor_flip_matrix) * matrix(ZZ, kernel_matrix)
    )
    def quotient_class(x):
        return min(x, x ^ base_key[0], x ^ base_key[1], x ^ base_key[2])

    for index, root in enumerate(seed_roots, start=1):
        assert pairing(root, root) == 2
        for source, target in zip(base[0], base[index]):
            coefficient = pairing(source, root)
            assert [x - coefficient * y for x, y in zip(source, root)] == target
        assert mask(root) not in base_key
        root_mask = mask(root)
        reflected_star = sorted({quotient_class(
            x ^ (root_mask if (x & root_mask).bit_count() % 2 else 0))
            for x in stars[0]})
        assert reflected_star == stars[index]
    for a, b in base:
        assert key(a, b) == base_key
        assert pairing(a, a) == pairing(a, b) == pairing(b, b) == 0
        assert gcd(*(a[i] * b[j] - a[j] * b[i]
                     for i, j in combinations(range(11), 2))) == 1
        for u, v in flag_coefficients:
            line = [u * x + v * y for x, y in zip(a, b)]
            assert gcd(*line) == 1 and pairing(line, line) == 0
            assert mask(line) in key(a, b)

    for row in rows:
        a, b = [list(v) for v in base[0]]
        J = tuple(row["finite_plane_masks"])
        assert len(J) == 3 and set(J) <= expected_line_masks
        for line_mask in J:
            line_degrees[line_mask] += len(base)
        transformed_stars = set()
        for star in stars:
            image = []
            for x in star:
                for i in row["word_from_base"]:
                    root_mask = root_masks[i]
                    if (x & root_mask).bit_count() % 2:
                        x ^= root_mask
                image.append(min(x, x ^ J[0], x ^ J[1], x ^ J[2]))
            assert len(set(image)) == 7
            transformed_stars.add(tuple(sorted(image)))
        assert len(transformed_stars) == 8
        for i in row["word_from_base"]:
            assert 0 <= i < 10
            root = roots[i]
            n = pairing(root, root)
            assert abs(n) == 2
            for v in (a, b):
                numerator = 2 * pairing(v, root)
                assert numerator % n == 0
                k = numerator // n
                v[:] = [x - k * y for x, y in zip(v, root)]
        assert key(a, b) == tuple(row["finite_plane_masks"])
        assert pairing(a, a) == pairing(a, b) == pairing(b, b) == 0
    assert set(line_degrees) == expected_line_masks
    assert set(line_degrees.values()) == {1080}
    assert sum(line_degrees.values()) == 569160


@pytest.mark.parametrize("mode", ["single", "batch"])
def test_requested_nondefault_kernel_transporter(mode, tmp_path):
    """Single and streaming-batch requests preserve the canonical certificate."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    certificate = folder / "coble_plane_integral_star_section.json"
    before = hashlib.sha256(certificate.read_bytes()).digest()
    requests = [[100, 3, 1]] if mode == "single" else [[100, 3, 1], [0, 0, 0]]
    if mode == "single":
        arguments = [str(x) for x in requests[0]]
    else:
        request_file = tmp_path / "requests.jsonl"
        request_file.write_text("".join(json.dumps(row) + "\n" for row in requests))
        arguments = ["batch", str(request_file)]
    result = subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"), *arguments],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    assert hashlib.sha256(certificate.read_bytes()).digest() == before
    marker = "requested integral kernel transporter: "
    records = [json.loads(line.split(marker, 1)[1])
               for line in result.stdout.splitlines() if marker in line]
    assert len(records) == len(requests)
    lines = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    for record, (_, seed_index, flag_index) in zip(records, requests):
        assert record["seed_index"] == seed_index and record["flag_index"] == flag_index
        assert record["line_mask_diagonal"] in record["finite_plane_masks"]
        kernel = record["kernel_matrix_standard"]
        positive = record["positive_kernel_matrix_standard"]
        assert all(kernel[i][j] % 2 == int(i == j)
                   and positive[i][j] % 2 == int(i == j)
                   for i in range(11) for j in range(11))
        line, = (row["vector_standard"] for row in lines["representatives"]
                 if row["mask_diagonal"] == record["line_mask_diagonal"])
        assert [sum(positive[i][j] * line[j] for j in range(11))
                for i in range(11)] == record["flag_vector_standard"]
        assert record["parabolic_correction_word"]
