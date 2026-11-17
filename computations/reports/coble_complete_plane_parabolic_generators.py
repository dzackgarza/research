"""Complete the Coble plane parabolic's integral Levi generators.

The 21 matrices in the archived certificate generate its correct *finite*
discriminant image, but omit the seven sign changes of O(<-1>^7).
This certificate adds those seven integral reflections without altering
the already certified 569160 flag witnesses or their source hashes.
"""
import json
import argparse
import hashlib
from pathlib import Path

from sage.all import ZZ, identity_matrix, matrix, vector


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    line_path = folder / "coble_singular_integral_representatives.json"
    plane_path = folder / "coble_plane_integral_star_section.json"
    lines = json.loads(line_path.read_text())
    planes = json.loads(plane_path.read_text())
    gram = matrix(ZZ, lines["standard_gram"])
    change = matrix(ZZ, lines["standard_to_diagonal"])
    inverse = change.inverse()
    unit = lambda i: vector(ZZ, [int(i == j) for j in range(11)])
    e1, e2 = unit(0) + unit(2), unit(1) + unit(4)
    d = [unit(0) + unit(2) + unit(3),
         unit(1) + unit(4) + unit(5)] + [unit(i) for i in range(6, 11)]
    signs = matrix(ZZ, 11, 11, lambda i, j: (
        (1 if i < 2 else -1) if i == j else 0))
    assert inverse.transpose() * gram * inverse == signs
    assert all(x * signs * y == (-1 if i == j else 0)
               for i, x in enumerate(d) for j, y in enumerate(d))
    old = [matrix(ZZ, rows) for rows in planes["plane_stabilizer_generators_standard"]]
    assert len(old) == 21
    reflections = []
    for root in d:
        # Reflection in a norm -1 vector: x -> x + 2(x,root)root.
        R = identity_matrix(ZZ, 11) + 2 * root.column() * (root.row() * signs)
        assert R.transpose() * signs * R == signs
        assert R * root == -root
        assert R * e1 == e1 and R * e2 == e2
        reflections.append(inverse * R * change)
    complete = old + reflections
    assert len(complete) == 28
    assert all(g.transpose() * gram * g == gram and abs(g.det()) == 1
               for g in complete)
    # All seven new sign changes are trivial modulo 2, so the exact
    # finite discriminant image order is unchanged.
    assert all(all(int(x) % 2 == int(i == j)
                   for i, row in enumerate(g.rows()) for j, x in enumerate(row))
               for g in reflections)
    assert planes["plane_stabilizer_finite_image_order"] == 247726080
    # d_i+d_6 and their sign-conjugates d_i-d_6 generate D^ev:
    # the first six sums and 2d_6 form a determinant-2 basis of Z^7.
    even_basis = matrix(ZZ, [
        [int(j == i) + int(j == 6) for j in range(7)]
        for i in range(6)
    ] + [[2 * int(j == 6) for j in range(7)]])
    assert abs(even_basis.det()) == 2
    if args.output is not None:
        certificate = {
            "schema": "coble-complete-integral-plane-parabolic-v1",
            "line_certificate_sha256": hashlib.sha256(line_path.read_bytes()).hexdigest(),
            "plane_certificate_sha256": hashlib.sha256(plane_path.read_bytes()).hexdigest(),
            "generator_count": len(complete),
            "finite_image_order": planes["plane_stabilizer_finite_image_order"],
            "even_unipotent_coefficient_index": int(abs(even_basis.det())),
            "generators_standard": [
                [[int(x) for x in row] for row in g.rows()] for g in complete
            ],
        }
        args.output.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    print("complete integral parabolic generator count:", len(complete))
    print("unchanged finite image order:", planes["plane_stabilizer_finite_image_order"])
    print("even unipotent coefficient lattice index:", abs(even_basis.det()))


if __name__ == "__main__":
    main()
