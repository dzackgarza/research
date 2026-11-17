"""Audit public Coble kernel incidence rows against theorem-derived graph degrees.

Input: log of sage-extensions' coble_gamma_co_2_incidence_rows.py
--rows Otilde,Otilde+ --lattice Tco. No finite enumeration substitutes
for the integral witnesses in this check. When given a GitHub run ID,
require a successful completed run and fetch its actual log before auditing.
The optional --class-only mode verifies the newer divided-class endpoint
relation by integral cusp representatives and the proved lifting criterion;
it does NOT certify a returned integral edge flag or subgroup transporter.

Usage:
    python3 computations/reports/coble_kernel_public_incidence_audit.py --run-id RUN
    python3 computations/reports/coble_kernel_public_incidence_audit.py --log LOG
"""
import argparse
import ast
import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
import re
import subprocess
import tempfile

LABELS = ("Otilde", "Otilde+")
EXPECTED = (569160, 527, 189720)
VERTEX = re.compile(r"\[(Otilde\+?)\] (line|plane) cusp (\d+): (\(.*\))")
EDGE = re.compile(
    r"\[(Otilde\+?)\] edge (\d+): L(\d+) < P(\d+); "
    r"line=(\(\(.*?\),\)); plane=(\(\(.*?\)\))"
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


def audit(path: Path, *, class_only: bool = False) -> None:
    vertices = {label: {"line": set(), "plane": set()} for label in LABELS}
    vertex_classes = {label: {"line": {}, "plane": {}} for label in LABELS}
    plane_bases = {label: {} for label in LABELS}
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
                else:
                    p, q = coords
                    assert len(p) == len(q) == 11
                    assert pairing(p, p) == pairing(p, q) == pairing(q, q) == 0, (
                        label, index, "plane cusp isotropy"
                    )
                    primitive_plane_pivot(p, q)
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
                    line_source, plane_source = match.groups()[4:]
                    (v,) = ast.literal_eval(line_source)
                    p, q = ast.literal_eval(plane_source)
                    assert len(v) == len(p) == len(q) == 11, (label, position, "rank")
                    assert gcd(*v) == 1, (label, position, "line primitive")
                    assert pairing(v, v) == pairing(p, p) == pairing(p, q) == pairing(q, q) == 0, (
                        label, position, "isotropy"
                    )
                    pivot = primitive_plane_pivot(p, q)
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
        assert set(plane_multiplicities.values()) == {8}, (label, "eight stars per finite plane")
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
                 else "public integral edge witnesses checked"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--log", type=Path, help="saved complete public workflow log")
    source.add_argument("--run-id", type=int, help="fetch a successful public workflow run")
    parser.add_argument("--class-only", action="store_true",
                        help="verify divided-class endpoints, not integral edge transporters")
    args = parser.parse_args()
    if args.log is not None:
        audit(args.log, class_only=args.class_only)
    else:
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
        print(f"public workflow {args.run_id} at {status['headSha']} verified")
