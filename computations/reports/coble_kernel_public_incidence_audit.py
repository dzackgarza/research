"""Audit public Coble kernel incidence rows against theorem-derived graph degrees.

Input: log of sage-extensions' coble_gamma_co_2_incidence_rows.py
--rows Otilde,Otilde+ --lattice Tco. No finite enumeration substitutes
for the integral witnesses in this check.
"""
import argparse
from collections import Counter
from pathlib import Path
import re

LABELS = ("Otilde", "Otilde+")
EXPECTED = (569160, 527, 189720)
VERTEX = re.compile(r"\[(Otilde\+?)\] (line|plane) cusp (\d+):")
EDGE = re.compile(r"\[(Otilde\+?)\] edge (\d+): L(\d+) < P(\d+);")
DECIDED = re.compile(
    r"\[(Otilde\+?)\] decided: (\d+) edges over (\d+) line cusps and (\d+) plane cusps"
)
SUMMARY = (
    "recorded counts: Otilde 569160 edges over 527 line and 189720 plane cusps; "
    "Otilde+ 569160 edges over 527 line and 189720 plane cusps"
)


def audit(path: Path) -> None:
    vertices = {label: {"line": set(), "plane": set()} for label in LABELS}
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
                label, kind, index = match.groups()
                index = int(index)
                assert index not in vertices[label][kind], (label, kind, index)
                vertices[label][kind].add(index)
                continue
            match = EDGE.search(line)
            if match:
                label, position, line_id, plane_id = match.groups()
                position, line_id, plane_id = map(int, (position, line_id, plane_id))
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
    assert summaries == 1, ("final successful two-row summary", summaries)
    for label in LABELS:
        assert vertices[label]["line"] == set(range(EXPECTED[1])), (label, "line vertices")
        assert vertices[label]["plane"] == set(range(EXPECTED[2])), (label, "plane vertices")
        assert positions[label] == set(range(EXPECTED[0])), (label, "edge positions")
        assert len(pairs[label]) == EXPECTED[0], (label, "distinct edges")
        line_degrees, plane_degrees = degrees[label]
        assert set(line_degrees) == vertices[label]["line"]
        assert set(plane_degrees) == vertices[label]["plane"]
        assert set(line_degrees.values()) == {1080}, (label, "line degrees")
        assert set(plane_degrees.values()) == {3}, (label, "plane degrees")
        assert decided.get(label) == EXPECTED, (label, "public row status")
        print(f"{label}: {EXPECTED[1]} lines, {EXPECTED[2]} planes, "
              f"{EXPECTED[0]} distinct edges; degrees (1080,3); decided")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path)
    audit(parser.parse_args().log)
