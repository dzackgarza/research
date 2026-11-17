"""Classify all archived integral Coble flags into the thirteen G_Co orbits.

Run with Sage's Python interpreter and all 32 downloaded certificate shards.
On the research Sage container, the CLI accepts a -c expression:

    sage -c 'import glob,runpy,sys; sys.argv=["audit",*sorted(glob.glob(".tmp/coble-complete-44170494099/coble-integral-shard-*/shard-*.jsonl.gz"))]; runpy.run_path("computations/reports/coble_integral_flag_quotient_audit.py",run_name="__main__")'

The --limit N option is a bounded diagnostic, never full acceptance.
"""
import argparse
from collections import Counter
import gzip
import json
from pathlib import Path
import runpy
import sys

from sage.all import ZZ, matrix
sys.path.insert(0, str(Path(__file__).resolve().parent))
from coble_kernel_public_incidence_audit import verify_integral_shard_manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    lines = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    planes = json.loads((folder / "coble_plane_integral_star_section.json").read_text())
    indices = verify_integral_shard_manifest(
        args.shards, folder / "coble_integral_flag_certificate_manifest.json")
    if args.limit is None:
        assert indices == set(range(32))
    else:
        assert args.limit > 0

    finite = runpy.run_path(str(folder / "coble_gco_plane-orbits.py"))
    orbit_of = {flag: i for i, orbit in enumerate(finite["flag_orbits"])
                for flag in orbit}
    sizes = [len(orbit) for orbit in finite["flag_orbits"]]
    assert len(orbit_of) == 569160 and len(sizes) == 13
    endpoints = {
        i: (finite["plane_orbit_index"][next(iter(orbit))[:2]],
            finite["size_of"][next(iter(orbit))[2]])
        for i, orbit in enumerate(finite["flag_orbits"])
    }
    assert len(set(endpoints.values())) == 13
    # Convert the eleven diagonal coordinates of <1>+U+E8(-1) to
    # the ten U+E8(-1) coordinates of the independent finite orbit model.
    inverse = matrix(ZZ, lines["standard_to_diagonal"]).inverse()
    assert abs(inverse.det()) == 1
    masks = [sum((int(inverse[i + 1, j]) & 1) << i for i in range(10))
             for j in range(11)]
    first = sum((int(inverse[0, j]) & 1) << j for j in range(11))

    def project(mask):
        assert (mask & first).bit_count() % 2 == 0
        result = 0
        for j in range(11):
            if mask & (1 << j):
                result ^= masks[j]
        return result

    change = lines["standard_to_diagonal"]
    root_masks = [
        sum((sum(change[i][j] * root[j] for j in range(11)) & 1) << i
            for i in range(11))
        for root in lines["generator_roots_standard"]
    ]

    def transport(mask, word):
        for index in word:
            root = root_masks[index]
            if (mask & root).bit_count() % 2:
                mask ^= root
        return mask

    counts = Counter()
    total = 0
    cached_index = None
    for path in args.shards:
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            header = json.loads(next(stream))
            for record in stream:
                row = json.loads(record)
                if "trailer" in row:
                    break
                index = row["plane_index"]
                assert index % 32 == header["shard_index"]
                if index != cached_index:
                    entry = planes["finite_plane_transports"][index]
                    J = frozenset(project(x) for x in entry["finite_plane_masks"])
                    assert J in finite["PLANES"]
                    span = (0, *J)
                    stars = []
                    for seven in planes["base_stars_quotient_classes"]:
                        reps = [project(transport(x, entry["word_from_base"]))
                                for x in seven]
                        star = frozenset(x ^ y for x in reps for y in span)
                        assert len(star) == 28
                        stars.append(star)
                    assert len(set(stars)) == 8
                    cached_index = index
                c = project(row["line_mask_diagonal"])
                assert c in J
                key = (J, stars[row["seed_index"]], c)
                assert key in orbit_of, (index, row["seed_index"], c)
                orbit = orbit_of[key]
                assert endpoints[orbit] == (
                    finite["plane_orbit_index"][key[:2]], finite["size_of"][c])
                counts[orbit] += 1
                total += 1
                if args.limit is not None and total >= args.limit:
                    print("sampled integral flags:", total,
                          "finite orbits:", len(counts))
                    return
    assert total == 569160
    assert sorted(counts.values()) == sorted(sizes)
    assert set(counts) == set(range(13))
    print("integral flags descended to thirteen G_Co orbits:",
          sorted(counts.values()))
    print("distinct line/plane quotient endpoints:", len(set(endpoints.values())))
    print("exact integral flags classified:", total)


if __name__ == "__main__":
    main()
