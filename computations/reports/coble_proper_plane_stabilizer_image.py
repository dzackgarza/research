"""Independent finite group certificate of the proper integral plane image.

Construct the full orthogonal group on the 527 singular discriminant classes,
the stabilizer F of a finite plane, and the image S of the complete 28-matrix
integral plane parabolic.  Check [F:S]=8 and [Q:S]=189720 directly.
"""
import json
import argparse
import hashlib
from math import gcd
from pathlib import Path

from sage.all import QQ, ZZ, PermutationGroup, matrix, vector
from sage.combinat.permutation import Permutation


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    line_path = folder / "coble_singular_integral_representatives.json"
    plane_path = folder / "coble_plane_integral_star_section.json"
    parabolic_path = folder / "coble_complete_plane_parabolic_generators.json"
    public_path = folder / "coble_gco_public_representatives.json"
    lines = json.loads(line_path.read_text())
    planes = json.loads(plane_path.read_text())
    parabolic = json.loads(parabolic_path.read_text())
    public = json.loads(public_path.read_text())
    assert public["source_workflow"] == 43556671111
    assert len(public["lines"]) == 4 and len(public["planes"]) == 7
    assert len(public["edges"]) == 13
    change = matrix(ZZ, lines["standard_to_diagonal"])
    gram = matrix(ZZ, lines["standard_gram"])
    lattice_gram = 2 * gram
    public_lines = {row["index"]: vector(ZZ, row["vector"])
                    for row in public["lines"]}
    public_planes = {row["index"]: tuple(vector(ZZ, v) for v in row["basis"])
                     for row in public["planes"]}
    for v in public_lines.values():
        assert gcd(*map(int, v)) == 1 and v * lattice_gram * v == 0
    for p, q in public_planes.values():
        assert p * lattice_gram * p == p * lattice_gram * q == q * lattice_gram * q == 0
        minors_gcd = 0
        for i in range(11):
            for j in range(i + 1, 11):
                minors_gcd = gcd(minors_gcd, int(p[i] * q[j] - p[j] * q[i]))
        assert minors_gcd == 1
    for edge in public["edges"]:
        p, q = [vector(ZZ, v) for v in edge["plane_witness"]]
        v = vector(ZZ, edge["line_witness"])
        assert gcd(*map(int, v)) == 1 and v * lattice_gram * v == 0
        assert p * lattice_gram * p == p * lattice_gram * q == q * lattice_gram * q == 0
        minors_gcd = 0
        for i in range(11):
            for j in range(i + 1, 11):
                minors_gcd = gcd(minors_gcd, int(p[i] * q[j] - p[j] * q[i]))
        assert minors_gcd == 1
        coefficients = matrix(ZZ, [p, q]).transpose().change_ring(QQ).solve_right(v)
        assert all(c in ZZ for c in coefficients)
    singular = sorted(row["mask_diagonal"] for row in lines["representatives"])
    assert len(singular) == 527
    positions = {x: i + 1 for i, x in enumerate(singular)}

    def mask(v):
        return sum((int(x) & 1) << i for i, x in enumerate(v))

    def permutation(g):
        return Permutation([
            positions[mask(change * g * change.inverse()
                           * vector(ZZ, [(x >> i) & 1 for i in range(11)]))]
            for x in singular
        ])

    roots = [vector(ZZ, root) for root in lines["generator_roots_standard"]]
    gram = matrix(ZZ, lines["standard_gram"])
    ambient = []
    for root in roots:
        norm = root * gram * root
        assert abs(norm) == 2
        reflection = matrix(ZZ, 11, 11, lambda i, j: (
            int(i == j) - int(2 * root[i] * (root * gram)[j] // norm)))
        ambient.append(permutation(reflection))
    Q = PermutationGroup(ambient)
    assert Q.order() == 46998591897600
    base_vectors = planes["base_planes_standard"][0]
    a, b = [mask(change * vector(ZZ, x)) for x in base_vectors]
    plane = [positions[x] for x in (a, b, a ^ b)]
    F = Q.stabilizer(plane, action="OnSets")
    assert Q.order() // F.order() == 23715
    assert F.order() == 1981808640
    generators = [matrix(ZZ, g) for g in parabolic["generators_standard"]]
    assert len(generators) == 28
    S = PermutationGroup([permutation(g) for g in generators])
    assert S.order() == 247726080
    assert all(g in F for g in S.gens())
    assert F.order() // S.order() == 8
    assert Q.order() // S.order() == 189720
    assert parabolic["finite_image_order"] == S.order()
    root_masks = [mask(change * vector(ZZ, root))
                  for root in lines["generator_roots_standard"]]

    def transport(x, word):
        for i in word:
            root = root_masks[i]
            if (x & root).bit_count() % 2:
                x ^= root
        return x

    base_plane_masks = {a, b, a ^ b}
    for entry in planes["finite_plane_transports"]:
        word = entry["word_from_base"]
        assert all(0 <= i < len(root_masks) for i in word)
        assert {transport(x, word) for x in base_plane_masks} == set(
            entry["finite_plane_masks"])
    # Recover the eight characteristic stars as the actual F/S orbit,
    # not merely as eight preselected finite labels.  A star consists
    # of seven cosets of J, each containing four singular vectors.
    plane_masks = (a, b, a ^ b)
    star_sets = [
        frozenset(x ^ j for x in star for j in (0, *plane_masks))
        for star in planes["base_stars_quotient_classes"]
    ]
    assert len(set(star_sets)) == 8 and all(len(star) == 28 for star in star_sets)
    # Singular classes span the ten-dimensional characteristic perpendicular.
    # Recover the linear action there from ten independent singular classes,
    # then apply it also to the nonsingular characteristic star classes.
    basis = []
    coefficients = {0: 0}
    for x in singular:
        if x not in coefficients:
            j = len(basis)
            basis.append(x)
            coefficients.update({u ^ x: c ^ (1 << j)
                                 for u, c in tuple(coefficients.items())})
    assert len(basis) == 10 and len(coefficients) == 1024
    assert all(star <= coefficients.keys() for star in star_sets)

    def act(g, x):
        c = coefficients[x]
        images = [singular[g(positions[b]) - 1] for b in basis]
        result = 0
        for j, image in enumerate(images):
            if c & (1 << j):
                result ^= image
        return result

    initial = star_sets[0]
    assert all(frozenset(act(g, x) for x in initial) == initial for g in S.gens())
    orbit = {initial}
    orbit_words = {initial: ()}
    frontier = [initial]
    while frontier:
        star = frontier.pop()
        for i, g in enumerate(F.gens()):
            moved = frozenset(act(g, x) for x in star)
            if moved not in orbit:
                orbit.add(moved)
                orbit_words[moved] = orbit_words[star] + (i,)
                frontier.append(moved)
    assert orbit == set(star_sets)
    # Orbit-stabilizer: the star stabilizer in F has order |F|/8=|S|.
    # Since all S generators fix the star, S is EXACTLY that stabilizer.
    assert F.order() // len(orbit) == S.order()
    # Each word is a concrete coset representative in F/S.  Replaying it
    # from the base star must give exactly the corresponding integral star.
    representatives = [orbit_words[star] for star in star_sets]
    for star, word in zip(star_sets, representatives):
        current = initial
        for i in word:
            current = frozenset(act(F.gens()[i], x) for x in current)
        assert current == star
    if args.output is not None:
        certificate = {
            "schema": "coble-proper-plane-stabilizer-finite-cosets-v1",
            "source_sha256": {
                "line": hashlib.sha256(line_path.read_bytes()).hexdigest(),
                "plane": hashlib.sha256(plane_path.read_bytes()).hexdigest(),
                "integral_parabolic": hashlib.sha256(parabolic_path.read_bytes()).hexdigest(),
                "public_gamma_co_2": hashlib.sha256(public_path.read_bytes()).hexdigest(),
            },
            "singular_masks_diagonal": singular,
            "standard_gram": lines["standard_gram"],
            "integral_reflection_roots_standard": lines["generator_roots_standard"],
            "base_finite_plane_masks": sorted((a, b, a ^ b)),
            "ambient_order": int(Q.order()),
            "finite_plane_stabilizer_order": int(F.order()),
            "integral_plane_image_order": int(S.order()),
            "finite_plane_stabilizer_generators_on_singular_classes": [
                [int(g(i)) for i in range(1, 528)] for g in F.gens()
            ],
            "integral_star_masks_diagonal": [
                sorted(star) for star in star_sets
            ],
            "integral_plane_representatives_standard": planes["base_planes_standard"],
            "flag_line_coefficients": planes["flag_line_coefficients"],
            "public_gamma_co_2_representatives": public,
            "finite_plane_transports": [
                {
                    "finite_plane_masks": entry["finite_plane_masks"],
                    "word_from_base": entry["word_from_base"],
                }
                for entry in planes["finite_plane_transports"]
            ],
            "coset_words_in_finite_plane_stabilizer_generators": [
                list(word) for word in representatives
            ],
        }
        args.output.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    print("ambient finite image order:", Q.order())
    print("finite plane stabilizer order:", F.order())
    print("integral plane stabilizer image order:", S.order())
    print("proper image index in finite plane stabilizer:", F.order() // S.order())
    print("characteristic stars in the F/S orbit:", len(orbit))
    print("finite F/S coset representative words:", [list(w) for w in representatives])
    print("integral plane orbit count:", Q.order() // S.order())


if __name__ == "__main__":
    main()
