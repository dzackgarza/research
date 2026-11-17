"""Audit public Coble kernel incidence rows against theorem-derived graph degrees.

Input: log of sage-extensions' coble_gamma_co_2_incidence_rows.py
--rows Otilde,Otilde+ --lattice Tco. No finite enumeration substitutes
for the integral witnesses in this check. Strict edge rows additionally
require an exact 11x11 integral transporter matrix, in the public T_Co
basis, from the indexed line representative to the displayed flag line.
For Otilde+ its positive-plane orientation is checked exactly.
When given a GitHub run ID,
require a successful completed run and fetch its actual log before auditing.
The optional --class-only mode verifies the newer divided-class endpoint
relation by integral cusp representatives and the proved lifting criterion;
it does NOT certify a returned integral edge flag or subgroup transporter.

Usage:
    python3 computations/reports/coble_kernel_public_incidence_audit.py --run-id RUN
    python3 computations/reports/coble_kernel_public_incidence_audit.py --log LOG
    python3 computations/reports/coble_kernel_public_incidence_audit.py --shards shard-*.jsonl.gz
"""
import argparse
import ast
import hashlib
import gzip
import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
import re
import subprocess
import tempfile

if not __debug__:
    raise RuntimeError("Coble incidence certification requires Python assertions; do not run with -O")

LABELS = ("Otilde", "Otilde+")
EXPECTED = (569160, 527, 189720)


def _exact_matrix_product(a, b):
    """Multiply eleven-dimensional integer matrices without Sage."""
    return [[sum(a[i][k] * b[k][j] for k in range(11))
             for j in range(11)] for i in range(11)]


def _exact_reflection(root):
    """Integral root reflection in the public T_Co basis."""
    n = pairing(root, root)
    assert abs(n) == 4
    coefficients = [2 * pairing(tuple(int(i == j) for i in range(11)), root)
                    for j in range(11)]
    assert all(c % n == 0 for c in coefficients)
    return [[int(i == j) - root[i] * (coefficients[j] // n)
             for j in range(11)] for i in range(11)]


def _exact_reflection_word(word, generators):
    result = [[int(i == j) for j in range(11)] for i in range(11)]
    for index in word:
        assert type(index) is int and 0 <= index < len(generators)
        result = _exact_matrix_product(_exact_reflection(generators[index]), result)
    return result


def audit_integral_shard(path: Path, *, allow_incomplete: bool = False) -> int:
    """Independently verify a compressed exact transporter shard, without trusting its producer."""
    folder = Path(__file__).resolve().parent
    line_path = folder / "coble_singular_integral_representatives.json"
    plane_path = folder / "coble_plane_integral_star_section.json"
    lines = json.loads(line_path.read_text())
    planes = json.loads(plane_path.read_text())
    source = {r["mask_diagonal"]: tuple(r["vector_standard"])
              for r in lines["representatives"]}
    roots = [tuple(r) for r in lines["generator_roots_standard"]]
    seeds = planes["base_planes_standard"]
    seed_roots = planes["seed_reflection_roots_standard"]
    stabilizer = planes["plane_stabilizer_generators_standard"]
    parabolic_roots = lines["vector_stabilizer_ten_roots_standard"]
    line_rows = {r["mask_diagonal"]: r for r in lines["representatives"]}
    assert len(source) == len(lines["representatives"]) == 527
    assert len(planes["finite_plane_transports"]) == 23715 and len(seeds) == 8
    finite_keys = [tuple(r["finite_plane_masks"])
                   for r in planes["finite_plane_transports"]]
    assert len(set(finite_keys)) == 23715
    assert all(len(key) == 3 and tuple(sorted(key)) == key and len(set(key)) == 3
               for key in finite_keys)
    class_degrees = Counter(c for key in finite_keys for c in key)
    assert set(class_degrees) == set(source)
    assert set(class_degrees.values()) == {135}
    assert sum(class_degrees.values()) * len(seeds) == EXPECTED[0]
    change = lines["standard_to_diagonal"]
    root_masks = [sum((sum(change[i][j] * root[j] for j in range(11)) & 1) << i
                      for i in range(11)) for root in roots]
    base_stars = planes["base_stars_quotient_classes"]
    assert len(base_stars) == len(seeds) == 8
    basis = [tuple(int(i == j) for i in range(11)) for j in range(11)]
    digest = hashlib.sha256()
    plane_word_cache = {}
    line_word_cache = {}
    checked_stars = set()
    identity = [[int(i == j) for j in range(11)] for i in range(11)]
    with gzip.open(path, "rb") as stream:
        header = json.loads(next(stream))
        assert header["schema"] == "coble-exact-kernel-transport-shard-v1"
        assert header["complete"] is False
        assert header["line_certificate_sha256"] == hashlib.sha256(line_path.read_bytes()).hexdigest()
        assert header["plane_certificate_sha256"] == hashlib.sha256(plane_path.read_bytes()).hexdigest()
        index, total = header["shard_index"], header["shard_count"]
        assert type(index) is type(total) is int and 0 <= index < total
        expected = 24 * len(range(index, len(planes["finite_plane_transports"]), total))
        assert header["expected_edges"] == expected
        count = 0
        seed_classes = set()
        for raw in stream:
            row = json.loads(raw)
            if "trailer" in row:
                assert row["trailer"] == header["schema"]
                assert row["records"] == count and row["records_sha256"] == digest.hexdigest()
                assert row["complete"] is (count == expected)
                assert row["complete"] or allow_incomplete
                assert next(stream, None) is None
                return count
            digest.update(raw)
            plane_index = index + (count // 24) * total
            assert (row["plane_index"], row["seed_index"], row["flag_index"]) == (
                plane_index, (count % 24) // 3, count % 3)
            assert plane_index < len(planes["finite_plane_transports"])
            if plane_index not in checked_stars:
                finite_plane = planes["finite_plane_transports"][plane_index]
                key = finite_plane["finite_plane_masks"]
                transported_stars = set()
                for star in base_stars:
                    image = []
                    for class_mask in star:
                        for root_index in finite_plane["word_from_base"]:
                            mask = root_masks[root_index]
                            if (class_mask & mask).bit_count() % 2:
                                class_mask ^= mask
                        image.append(min(class_mask, *(class_mask ^ c for c in key)))
                    assert len(set(image)) == 7, "nonprimitive integral star quotient"
                    transported_stars.add(tuple(sorted(image)))
                assert len(transported_stars) == 8, "integral star fibre collapsed"
                checked_stars.add(plane_index)
            assert row["line_mask_diagonal"] in planes["finite_plane_transports"][plane_index]["finite_plane_masks"]
            assert row["line_mask_diagonal"] not in seed_classes, (
                plane_index, row["seed_index"], "repeated line class")
            seed_classes.add(row["line_mask_diagonal"])
            if count % 3 == 2:
                assert seed_classes == set(planes["finite_plane_transports"][plane_index]["finite_plane_masks"])
                seed_classes.clear()
            u = source[row["line_mask_diagonal"]]
            v = tuple(row["flag_vector_standard"])
            assert len(v) == 11 and gcd(*v) == 1 and pairing(v, v) == 0
            v_mask = sum((sum(change[i][j] * v[j] for j in range(11)) & 1) << i
                         for i in range(11))
            assert v_mask == row["line_mask_diagonal"], "flag divided class disagrees with line cusp"
            p, q = (tuple(w) for w in seeds[row["seed_index"]])
            for root_index in planes["finite_plane_transports"][plane_index]["word_from_base"]:
                root = roots[root_index]
                norm = pairing(root, root)
                assert abs(norm) == 4  # T_Co is twice the unimodular Coble form.
                cp, cq = 2 * pairing(p, root), 2 * pairing(q, root)
                assert cp % norm == cq % norm == 0
                p = tuple(a - (cp // norm) * b for a, b in zip(p, root))
                q = tuple(a - (cq // norm) * b for a, b in zip(q, root))
            a, b, determinant = primitive_plane_pivot(p, q)
            assert pairing(p, p) == pairing(p, q) == pairing(q, q) == 0
            masks = [sum((sum(change[i][j] * w[j] for j in range(11)) & 1) << i
                         for i in range(11)) for w in (p, q)]
            assert sorted((masks[0], masks[1], masks[0] ^ masks[1])) == (
                planes["finite_plane_transports"][plane_index]["finite_plane_masks"])
            assert all(v[c] * determinant
                       - v[a] * (p[c] * q[b] - p[b] * q[c])
                       - v[b] * (p[a] * q[c] - p[c] * q[a]) == 0
                       for c in range(11)), (plane_index, "flag not in integral plane")
            for field in ("kernel_matrix_standard", "positive_kernel_matrix_standard"):
                g = row[field]
                assert len(g) == 11 and all(len(r) == 11 for r in g)
                assert all(type(x) is int for r in g for x in r)
                assert all(g[i][j] % 2 == int(i == j) for i in range(11) for j in range(11))
                assert tuple(sum(g[i][j] * u[j] for j in range(11)) for i in range(11)) == v
                columns = [tuple(g[i][j] for i in range(11)) for j in range(11)]
                assert all(pairing(columns[i], columns[j]) == pairing(basis[i], basis[j])
                           for i in range(11) for j in range(11))
            flip = row["spinor_flip_matrix_standard"]
            assert len(flip) == 11 and all(len(r) == 11 for r in flip)
            assert all(type(z) is int for r in flip for z in r)
            assert all(flip[i][j] % 2 == int(i == j) for i in range(11) for j in range(11))
            assert tuple(sum(flip[i][j] * v[j] for j in range(11)) for i in range(11)) == v
            flip_columns = [tuple(flip[i][j] for i in range(11)) for j in range(11)]
            assert all(pairing(flip_columns[i], flip_columns[j]) == pairing(basis[i], basis[j])
                       for i in range(11) for j in range(11))
            x, y = basis[0], tuple(int(i in (1, 2)) for i in range(11))
            fx = tuple(sum(flip[i][j] * x[j] for j in range(11)) for i in range(11))
            fy = tuple(sum(flip[i][j] * y[j] for j in range(11)) for i in range(11))
            assert pairing(x, fx) * pairing(y, fy) - pairing(x, fy) * pairing(y, fx) < 0
            for field in ("kernel_matrix_standard", "positive_kernel_matrix_standard"):
                g = row[field]
                gx = tuple(sum(g[i][j] * x[j] for j in range(11)) for i in range(11))
                gy = tuple(sum(g[i][j] * y[j] for j in range(11)) for i in range(11))
                minor = pairing(x, gx) * pairing(y, gy) - pairing(x, gy) * pairing(y, gx)
                assert minor != 0
                if field == "kernel_matrix_standard":
                    assert row["kernel_real_spinor_sign"] == (1 if minor > 0 else -1)
                else:
                    assert minor > 0
            g = row["positive_kernel_matrix_standard"]
            kernel = row["kernel_matrix_standard"]
            if plane_index not in plane_word_cache:
                plane_word_cache.clear()
                plane_word_cache[plane_index] = _exact_reflection_word(
                    planes["finite_plane_transports"][plane_index]["word_from_base"], roots)
            line_mask = row["line_mask_diagonal"]
            if line_mask not in line_word_cache:
                line_word_cache[line_mask] = _exact_reflection_word(
                    line_rows[line_mask]["word_from_base"], roots)
            seed_map = (identity if row["seed_index"] == 0 else
                        _exact_reflection(seed_roots[row["seed_index"] - 1]))
            flag_map = [identity, stabilizer[-2], stabilizer[-1]][row["flag_index"]]
            ambient_times_line = _exact_matrix_product(
                _exact_matrix_product(plane_word_cache[plane_index], seed_map), flag_map)
            correction_indices = []
            for factor in row["parabolic_correction_word"]:
                assert len(factor) == 2
                root_index, exponent = factor
                assert type(root_index) is type(exponent) is int
                assert 0 <= root_index < len(parabolic_roots)
                assert exponent != 0
                if exponent % 2:
                    correction_indices.append(root_index)
            # A reflection acts on a column in O(11^2) integer operations;
            # forming a dense 11x11 product for every word letter costs O(11^3).
            # Verify the full matrix identity on the eleven standard columns.
            for j in range(11):
                column = [int(i == j) for i in range(11)]
                for root_index in correction_indices:
                    root = parabolic_roots[root_index]
                    norm = pairing(root, root)
                    coefficient = 2 * pairing(column, root)
                    assert abs(norm) == 4 and coefficient % norm == 0
                    column = [a - (coefficient // norm) * b
                              for a, b in zip(column, root)]
                carried = [sum(line_word_cache[line_mask][i][k] * column[k]
                               for k in range(11)) for i in range(11)]
                result = [sum(kernel[i][k] * carried[k] for k in range(11))
                          for i in range(11)]
                assert result == [ambient_times_line[i][j] for i in range(11)], (
                    "parabolic correction word does not reconstruct kernel", j)
            assert g == (kernel if row["kernel_real_spinor_sign"] == 1 else
                         [[sum(flip[i][k] * kernel[k][j] for k in range(11))
                           for j in range(11)] for i in range(11)])
            assert row["positive_kernel_matrix_sha256"] == hashlib.sha256(
                json.dumps(g, separators=(",", ":")).encode()).hexdigest()
            count += 1
    raise AssertionError("missing terminal shard certificate")
VERTEX = re.compile(r"\[(Otilde\+?)\] (line|plane) cusp (\d+): (\(.*\))")
EDGE = re.compile(
    r"\[(Otilde\+?)\] edge (\d+): L(\d+) < P(\d+); "
    r"line=(\(\(.*?\),\)); plane=(\(\(.*?\)\)); transporter=(\[\[.*\]\])\s*$"
)
CLASS_EDGE = re.compile(r"\[(Otilde\+?)\] edge (\d+): L(\d+) < P(\d+)\s*$")
DECIDED = re.compile(
    r"\[(Otilde\+?)\] decided: (\d+) edges over (\d+) line cusps and (\d+) plane cusps"
)
ROW_PREFIX = re.compile(r"\[(Otilde\+?)\] (line cusp|plane cusp|edge|decided):?\s")
SUMMARY = (
    "recorded counts: Otilde 569160 edges over 527 line and 189720 plane cusps; "
    "Otilde+ 569160 edges over 527 line and 189720 plane cusps"
)
E8_EDGES = ((0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7))


def pairing(x: tuple, y: tuple) -> int:
    """Integral pairing of <2> + U(2) + E8(-2) in the public basis."""
    e, f = x[3:], y[3:]
    return (2 * x[0] * y[0] + 2 * (x[1] * y[2] + x[2] * y[1])
            - 4 * sum(e[i] * f[i] for i in range(8))
            + 2 * sum(e[a] * f[b] + e[b] * f[a] for a, b in E8_EDGES))


def mod2_span(p: tuple, q: tuple) -> frozenset:
    """The order-four discriminant subgroup of a primitive isotropic plane."""
    x, y = (tuple(int(t) % 2 for t in v) for v in (p, q))
    span = frozenset((tuple(0 for _ in x), x, y,
                      tuple(a ^ b for a, b in zip(x, y))))
    assert len(span) == 4
    return span


def primitive_plane_pivot(p: tuple, q: tuple) -> tuple:
    """An exact nonzero minor of a saturated rank-two plane basis."""
    minor_gcd = 0
    pivot = None
    for a, b in combinations(range(11), 2):
        minor = p[a] * q[b] - p[b] * q[a]
        if minor and pivot is None:
            pivot = (a, b, minor)
        minor_gcd = gcd(minor_gcd, minor)
        if minor_gcd == 1:
            break
    assert minor_gcd == 1 and pivot is not None, "plane is not primitive"
    return pivot


def plane_plucker_key(p: tuple, q: tuple) -> tuple:
    """Canonical primitive Pluecker coordinates of the integral plane.

    A change of integral basis of a saturated plane has determinant +/-1,
    so it changes all minors by one common sign. Conversely proportional
    primitive decomposable bivectors determine the same rational plane,
    whose saturation is the same integral plane.
    """
    minors = tuple(p[a] * q[b] - p[b] * q[a]
                   for a, b in combinations(range(11), 2))
    first = next(x for x in minors if x)
    return minors if first > 0 else tuple(-x for x in minors)


def audit(path: Path, *, class_only: bool = False) -> None:
    vertices = {label: {"line": set(), "plane": set()} for label in LABELS}
    vertex_classes = {label: {"line": {}, "plane": {}} for label in LABELS}
    integral_planes = {label: set() for label in LABELS}
    plane_bases = {label: {} for label in LABELS}
    line_vectors = {label: {} for label in LABELS}
    plane_keys = {label: {} for label in LABELS}
    degrees = {label: (Counter(), Counter()) for label in LABELS}
    pairs = {label: set() for label in LABELS}
    positions = {label: set() for label in LABELS}
    decided = {}
    summaries = 0
    with path.open(encoding="utf-8", errors="replace") as stream:
        for line in stream:
            if SUMMARY in line:
                summaries += 1
            match = VERTEX.search(line)
            if match:
                label, kind, index, source = match.groups()
                index = int(index)
                assert index not in vertices[label][kind], (label, kind, index)
                vertices[label][kind].add(index)
                coords = ast.literal_eval(source)
                if kind == "line":
                    (v,) = coords
                    assert len(v) == 11
                    assert gcd(*v) == 1 and pairing(v, v) == 0, (label, index, "line cusp")
                    vertex_classes[label][kind][index] = tuple(int(t) % 2 for t in v)
                    line_vectors[label][index] = v
                else:
                    p, q = coords
                    assert len(p) == len(q) == 11
                    assert pairing(p, p) == pairing(p, q) == pairing(q, q) == 0, (
                        label, index, "plane cusp isotropy"
                    )
                    primitive_plane_pivot(p, q)
                    plucker = plane_plucker_key(p, q)
                    assert plucker not in integral_planes[label], (
                        label, index, "repeated integral plane span"
                    )
                    integral_planes[label].add(plucker)
                    plane_keys[label][index] = plucker
                    vertex_classes[label][kind][index] = mod2_span(p, q)
                    plane_bases[label][index] = (p, q)
                continue
            match = (CLASS_EDGE if class_only else EDGE).search(line)
            if match:
                label, position, line_id, plane_id = match.groups()[:4]
                position, line_id, plane_id = map(int, (position, line_id, plane_id))
                if class_only:
                    c = vertex_classes[label]["line"].get(line_id)
                    J = vertex_classes[label]["plane"].get(plane_id)
                    assert c is not None and J is not None and c in J, (
                        label, position, "divided-class incidence"
                    )
                    # Produce an actual primitive integral line in the
                    # displayed plane for this endpoint class. The stable
                    # fibre theorem proves its orbit matches the line cusp;
                    # it does not output the transporter matrix.
                    p, q = plane_bases[label][plane_id]
                    candidates = (p, q, tuple(a + b for a, b in zip(p, q)))
                    flags = [v for v in candidates if tuple(t % 2 for t in v) == c]
                    assert len(flags) == 1, (label, position, "integral flag lift")
                    assert gcd(*flags[0]) == 1 and pairing(flags[0], flags[0]) == 0, (
                        label, position, "primitive integral flag"
                    )
                else:
                    line_source, plane_source, transporter_source = match.groups()[4:]
                    (v,) = ast.literal_eval(line_source)
                    p, q = ast.literal_eval(plane_source)
                    assert len(v) == len(p) == len(q) == 11, (label, position, "rank")
                    assert gcd(*v) == 1, (label, position, "line primitive")
                    assert pairing(v, v) == pairing(p, p) == pairing(p, q) == pairing(q, q) == 0, (
                        label, position, "isotropy"
                    )
                    pivot = primitive_plane_pivot(p, q)
                    assert plane_plucker_key(p, q) == plane_keys[label].get(plane_id), (
                        label, position, "edge plane differs from indexed integral plane"
                    )
                    # A primitive rank-two plane contains v iff all rank-three
                    # minors of [v,p,q] vanish. One nonzero 2x2 pivot suffices.
                    a, b, determinant = pivot
                    assert all(v[c] * determinant
                               - v[a] * (p[c] * q[b] - p[b] * q[c])
                               - v[b] * (p[a] * q[c] - p[c] * q[a]) == 0
                               for c in range(11)), (label, position, "line-in-plane")
                    assert tuple(int(t) % 2 for t in v) == vertex_classes[label]["line"].get(line_id), (
                        label, position, "line orbit discriminant class"
                    )
                    assert mod2_span(p, q) == vertex_classes[label]["plane"].get(plane_id), (
                        label, position, "plane orbit discriminant subgroup"
                    )
                    rows = ast.literal_eval(transporter_source)
                    assert len(rows) == 11 and all(len(row) == 11 for row in rows), (
                        label, position, "integral transporter matrix shape"
                    )
                    assert all(type(x) is int for row in rows for x in row), (
                        label, position, "integral transporter entries"
                    )
                    assert all(rows[i][j] % 2 == int(i == j)
                               for i in range(11) for j in range(11)), (
                        label, position, "transporter discriminant kernel"
                    )
                    columns = [tuple(rows[i][j] for i in range(11)) for j in range(11)]
                    basis = [tuple(int(i == j) for i in range(11)) for j in range(11)]
                    assert all(pairing(columns[i], columns[j]) == pairing(basis[i], basis[j])
                               for i in range(11) for j in range(11)), (
                        label, position, "transporter integral Gram"
                    )
                    source_line = line_vectors[label].get(line_id)
                    assert source_line is not None and all(
                        sum(rows[i][j] * source_line[j] for j in range(11)) == v[i]
                        for i in range(11)
                    ), (label, position, "transporter exact line-to-flag action")
                    if label == "Otilde+":
                        positive_0, positive_1 = basis[0], tuple(
                            int(i in (1, 2)) for i in range(11)
                        )
                        images = [tuple(sum(rows[i][j] * w[j] for j in range(11))
                                        for i in range(11))
                                  for w in (positive_0, positive_1)]
                        a = pairing(positive_0, images[0])
                        b = pairing(positive_0, images[1])
                        c = pairing(positive_1, images[0])
                        d = pairing(positive_1, images[1])
                        assert a * d - b * c > 0, (
                            label, position, "positive real spinor orientation"
                        )
                assert position not in positions[label], (label, position)
                positions[label].add(position)
                pair = (line_id, plane_id)
                assert pair not in pairs[label], (label, pair)
                pairs[label].add(pair)
                degrees[label][0][line_id] += 1
                degrees[label][1][plane_id] += 1
                continue
            match = DECIDED.search(line)
            if match:
                label, edges, lines, planes = match.groups()
                assert label not in decided, label
                decided[label] = tuple(map(int, (edges, lines, planes)))
                continue
            # A malformed public witness line must not disappear from the
            # audit just because its syntax did not match the strict parser.
            assert ROW_PREFIX.search(line) is None, ("unparsed public row", line[:240])
    assert summaries == 1, ("final successful two-row summary", summaries)
    for label in LABELS:
        assert vertices[label]["line"] == set(range(EXPECTED[1])), (label, "line vertices")
        assert vertices[label]["plane"] == set(range(EXPECTED[2])), (label, "plane vertices")
        assert len(set(vertex_classes[label]["line"].values())) == EXPECTED[1], (
            label, "distinct discriminant line classes"
        )
        plane_multiplicities = Counter(vertex_classes[label]["plane"].values())
        assert len(plane_multiplicities) == 23715, (label, "finite isotropic planes")
        # This verifies eight *integral representatives* per finite plane.
        # Distinctness of their intrinsic quotient stars is a stronger
        # assertion, not proved by counting or by distinct Pluecker keys.
        assert set(plane_multiplicities.values()) == {8}, (
            label, "eight integral plane representatives per finite plane"
        )
        assert positions[label] == set(range(EXPECTED[0])), (label, "edge positions")
        assert len(pairs[label]) == EXPECTED[0], (label, "distinct edges")
        line_degrees, plane_degrees = degrees[label]
        assert set(line_degrees) == vertices[label]["line"]
        assert set(plane_degrees) == vertices[label]["plane"]
        assert set(line_degrees.values()) == {1080}, (label, "line degrees")
        assert set(plane_degrees.values()) == {3}, (label, "plane degrees")
        assert decided.get(label) == EXPECTED, (label, "public row status")
        print(f"{label}: {EXPECTED[1]} lines, {EXPECTED[2]} planes, "
              f"{EXPECTED[0]} distinct edges; degrees (1080,3); decided; "
              + ("class-only, no public integral edge transporters" if class_only
                 else "public integral kernel transporters checked"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--log", type=Path, help="saved complete public workflow log")
    source.add_argument("--run-id", type=int, help="fetch a successful public workflow run")
    source.add_argument("--shard", type=Path, help="independently audit a compressed integral transporter shard")
    source.add_argument("--shards", nargs="+", type=Path,
                        help="certify the full 569160-edge family of compressed shards")
    parser.add_argument("--class-only", action="store_true",
                        help="verify divided-class endpoints, not integral edge transporters")
    parser.add_argument("--allow-incomplete", action="store_true",
                        help="diagnostic shard verification only, never full acceptance")
    args = parser.parse_args()
    if args.shard is not None:
        assert not args.class_only
        count = audit_integral_shard(args.shard, allow_incomplete=args.allow_incomplete)
        print(f"independently verified integral transporter shard: {count} records")
    elif args.shards is not None:
        assert not args.class_only and not args.allow_incomplete
        indices = set()
        total = None
        hashes = None
        edges = 0
        for path in args.shards:
            with gzip.open(path, "rt", encoding="utf-8") as stream:
                header = json.loads(next(stream))
            assert header["schema"] == "coble-exact-kernel-transport-shard-v1"
            if total is None:
                total = header["shard_count"]
                hashes = (header["line_certificate_sha256"],
                          header["plane_certificate_sha256"])
            assert header["shard_count"] == total
            assert (header["line_certificate_sha256"],
                    header["plane_certificate_sha256"]) == hashes
            assert header["shard_index"] not in indices, "duplicate shard index"
            indices.add(header["shard_index"])
            edges += audit_integral_shard(path)
        assert total is not None and indices == set(range(total)), "missing shard indices"
        assert edges == EXPECTED[0], "missing integral flag transporters"
        print(f"independently certified complete integral kernel incidence: {edges} edges")
    elif args.log is not None:
        assert not args.allow_incomplete
        audit(args.log, class_only=args.class_only)
        with args.log.open("rb") as source_file:
            print(f"audited log SHA-256: {hashlib.file_digest(source_file, 'sha256').hexdigest()}")
    else:
        assert not args.allow_incomplete
        repository = "dzackgarza/sage-extensions"
        status = json.loads(subprocess.run(
            ["gh", "run", "view", str(args.run_id), "-R", repository,
             "--json", "status,conclusion,headSha"],
            check=True, text=True, capture_output=True,
        ).stdout)
        assert status["status"] == "completed" and status["conclusion"] == "success", (
            "public run did not succeed", args.run_id, status
        )
        with tempfile.TemporaryDirectory(prefix="coble-public-kernel-") as directory:
            log = Path(directory) / "workflow.log"
            with log.open("w", encoding="utf-8") as output:
                subprocess.run(
                    ["gh", "run", "view", str(args.run_id), "-R", repository, "--log"],
                    check=True, stdout=output,
                )
            audit(log, class_only=args.class_only)
            with log.open("rb") as source_file:
                print(f"audited log SHA-256: {hashlib.file_digest(source_file, 'sha256').hexdigest()}")
        print(f"public workflow {args.run_id} at {status['headSha']} verified")
