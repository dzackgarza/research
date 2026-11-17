"""Independently replay the complete finite-to-integral Coble plane section."""

import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path


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
    from sage.all import ZZ, PermutationGroup, matrix, vector

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
