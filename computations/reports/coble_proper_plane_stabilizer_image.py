"""Independent finite group certificate of the proper integral plane image.

Construct the full orthogonal group on the 527 singular discriminant classes,
the stabilizer F of a finite plane, and the image S of the complete 28-matrix
integral plane parabolic.  Check [F:S]=8 and [Q:S]=189720 directly.
"""
import json
from pathlib import Path

from sage.all import ZZ, PermutationGroup, matrix, vector
from sage.combinat.permutation import Permutation


def main():
    folder = Path(__file__).resolve().parent
    lines = json.loads((folder / "coble_singular_integral_representatives.json").read_text())
    planes = json.loads((folder / "coble_plane_integral_star_section.json").read_text())
    parabolic = json.loads((folder / "coble_complete_plane_parabolic_generators.json").read_text())
    change = matrix(ZZ, lines["standard_to_diagonal"])
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
    frontier = [initial]
    while frontier:
        star = frontier.pop()
        for g in F.gens():
            moved = frozenset(act(g, x) for x in star)
            if moved not in orbit:
                orbit.add(moved)
                frontier.append(moved)
    assert orbit == set(star_sets)
    print("ambient finite image order:", Q.order())
    print("finite plane stabilizer order:", F.order())
    print("integral plane stabilizer image order:", S.order())
    print("proper image index in finite plane stabilizer:", F.order() // S.order())
    print("characteristic stars in the F/S orbit:", len(orbit))
    print("integral plane orbit count:", Q.order() // S.order())


if __name__ == "__main__":
    main()
