"""Independently replay the complete finite-to-integral Coble plane section."""

import json
import hashlib
import gzip
import importlib.util
import subprocess
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path

import pytest


def test_complete_integral_flag_certificate_manifest():
    """Check the permanent provenance ledger of the 32-shard full CI run."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    manifest = json.loads((folder / "coble_integral_flag_certificate_manifest.json").read_text())
    assert manifest["schema"] == "coble-integral-flag-certificate-manifest-v1"
    assert manifest["workflow_run"] == 44170494099
    assert manifest["source_commit"] == "c08aeb6baa98cfcd2a39c46141432f4ce9c92661"
    assert manifest["line_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_singular_integral_representatives.json").read_bytes()).hexdigest()
    assert manifest["plane_certificate_sha256"] == hashlib.sha256(
        (folder / "coble_plane_integral_star_section.json").read_bytes()).hexdigest()
    assert manifest["artifact_id"] == 14371631974
    assert manifest["total_edges"] == 569160
    assert manifest["shard_count"] == len(manifest["shards"]) == 32
    assert [row["index"] for row in manifest["shards"]] == list(range(32))
    assert [row["records"] for row in manifest["shards"]] == [
        24 * len(range(i, 23715, 32)) for i in range(32)]
    assert sum(row["records"] for row in manifest["shards"]) == 569160
    for key in ("file_sha256", "records_sha256"):
        digests = [row[key] for row in manifest["shards"]]
        assert len(set(digests)) == 32
        assert all(len(digest) == 64 and
                   all(c in "0123456789abcdef" for c in digest)
                   for digest in digests)


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
    # The producer's F_2 column-mask action must equal the actual integral
    # action on every one of the 527 nonzero singular discriminant classes.
    diagonal_correction = (diagonal_change * line_word.inverse() *
                           reconstructed_ambient * line_word * inverse_change)
    column_masks = [sum((int(diagonal_correction[i, j]) & 1) << i
                        for i in range(11)) for j in range(11)]
    for class_mask in singular:
        direct = diagonal_correction * vector(
            ZZ, [(class_mask >> j) & 1 for j in range(11)])
        expected = sum((int(direct[i]) & 1) << i for i in range(11))
        image = 0
        for j in range(11):
            if (class_mask >> j) & 1:
                image ^= column_masks[j]
        assert image == expected
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


def test_bounded_compressed_shard_is_explicitly_incomplete(tmp_path):
    """A diagnostic shard cannot be mistaken for full integral acceptance."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    source = folder / "coble_plane_integral_star_section.json"
    line_source = folder / "coble_singular_integral_representatives.json"
    original = hashlib.sha256(source.read_bytes()).hexdigest()
    output = tmp_path / "shard.jsonl.gz"
    subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"),
         "shard", "0", "8", str(output), "2"],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    assert hashlib.sha256(source.read_bytes()).hexdigest() == original
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        records = [json.loads(line) for line in stream]
    assert len(records) == 4
    header = records[0]
    assert header["schema"] == "coble-exact-kernel-transport-shard-v1"
    assert header["shard_index"] == 0 and header["shard_count"] == 8
    assert header["expected_edges"] == 24 * len(range(0, 23715, 8))
    assert header["complete"] is False  # Only the final trailer can certify completion.
    assert header["plane_certificate_sha256"] == original
    assert header["line_certificate_sha256"] == hashlib.sha256(
        line_source.read_bytes()
    ).hexdigest()
    assert [(r["plane_index"], r["seed_index"], r["flag_index"])
            for r in records[1:-1]] == [(0, 0, 0), (0, 0, 1)]
    trailer = records[-1]
    assert trailer["trailer"] == header["schema"]
    assert trailer["records"] == 2 and trailer["complete"] is False
    digest = hashlib.sha256()
    for record in records[1:-1]:
        digest.update(json.dumps(record, separators=(",", ":")).encode() + b"\n")
    assert trailer["records_sha256"] == digest.hexdigest()
    assert all(len(r["positive_kernel_matrix_sha256"]) == 64
               for r in records[1:-1])
    lines = json.loads(line_source.read_text())
    gram = lines["standard_gram"]
    seed_line = {r["mask_diagonal"]: r["vector_standard"]
                 for r in lines["representatives"]}
    for row in records[1:-1]:
        source_vector = seed_line[row["line_mask_diagonal"]]
        target_vector = row["flag_vector_standard"]
        for field in ("kernel_matrix_standard", "spinor_flip_matrix_standard",
                      "positive_kernel_matrix_standard"):
            g = row[field]
            assert len(g) == 11 and all(len(r) == 11 for r in g)
            assert all(g[i][j] % 2 == int(i == j)
                       for i in range(11) for j in range(11))
            assert [sum(g[i][j] * (target_vector if field == "spinor_flip_matrix_standard"
                                    else source_vector)[j] for j in range(11))
                    for i in range(11)] == target_vector
            assert all(sum(g[k][i] * gram[k][l] * g[l][j]
                           for k in range(11) for l in range(11)) == gram[i][j]
                       for i in range(11) for j in range(11))
    spec = importlib.util.spec_from_file_location(
        "coble_kernel_audit", folder / "coble_kernel_public_incidence_audit.py")
    assert spec is not None and spec.loader is not None
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    assert audit.audit_integral_shard(output, allow_incomplete=True) == 2
    with pytest.raises(AssertionError):
        audit.audit_integral_shard(output)
    corrupted = tmp_path / "corrupted.jsonl.gz"
    bad = json.loads(json.dumps(records))
    bad[1]["flag_vector_standard"][0] += 2
    digest = hashlib.sha256()
    with gzip.open(corrupted, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(bad[0], separators=(",", ":")) + "\n")
        for record in bad[1:-1]:
            encoded = json.dumps(record, separators=(",", ":")) + "\n"
            digest.update(encoded.encode())
            stream.write(encoded)
        bad[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(bad[-1], separators=(",", ":")) + "\n")
    with pytest.raises(AssertionError):
        audit.audit_integral_shard(corrupted, allow_incomplete=True)


@pytest.mark.parametrize("plane_index", [0, 12345])
def test_complete_single_plane_shard_is_independently_certified(tmp_path, plane_index):
    """A full 24-edge shard must pass the strict auditor, not the diagnostic mode."""
    folder = Path(__file__).resolve().parents[2] / "computations" / "reports"
    output = tmp_path / "complete.jsonl.gz"
    subprocess.run(
        ["sage", str(folder / "coble_plane_integral_star_section.py"),
         "shard", str(plane_index), "23715", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        header = json.loads(next(stream))
        assert header["shard_index"] == plane_index
        assert header["expected_edges"] == 24
        assert header["complete"] is False
        records = [json.loads(line) for line in stream]
    assert len(records) == 25
    assert records[-1]["complete"] is True and records[-1]["records"] == 24
    subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True, check=True,
    )
    missing = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shards", str(output)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert missing.returncode != 0 and "missing shard indices" in missing.stderr
    duplicate = tmp_path / "duplicate-class.jsonl.gz"
    records[1] = dict(records[0], flag_index=1)
    digest = hashlib.sha256()
    with gzip.open(duplicate, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(header, separators=(",", ":")) + "\n")
        for row in records[:-1]:
            encoded = json.dumps(row, separators=(",", ":")) + "\n"
            stream.write(encoded)
            digest.update(encoded.encode())
        records[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(records[-1], separators=(",", ":")) + "\n")
    invalid = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(duplicate)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert invalid.returncode != 0 and "repeated line class" in invalid.stderr
    forged = tmp_path / "forged-word.jsonl.gz"
    with gzip.open(output, "rt", encoding="utf-8") as stream:
        original = [json.loads(line) for line in stream]
    original[1]["parabolic_correction_word"] = [[0, 1]]
    digest = hashlib.sha256()
    with gzip.open(forged, "wt", encoding="utf-8") as stream:
        stream.write(json.dumps(original[0], separators=(",", ":")) + "\n")
        for row in original[1:-1]:
            encoded = json.dumps(row, separators=(",", ":")) + "\n"
            digest.update(encoded.encode())
            stream.write(encoded)
        original[-1]["records_sha256"] = digest.hexdigest()
        stream.write(json.dumps(original[-1], separators=(",", ":")) + "\n")
    invalid = subprocess.run(
        ["python3", str(folder / "coble_kernel_public_incidence_audit.py"),
         "--shard", str(forged)],
        cwd=folder.parents[1], capture_output=True, text=True,
    )
    assert invalid.returncode != 0 and "parabolic correction word" in invalid.stderr
