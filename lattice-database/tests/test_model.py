"""A record validates exactly when its declarations agree with its Gram tensor."""

from collections.abc import Callable
from fractions import Fraction

import pytest
from latticedb.model import Lattice, Morphism, Yaml
from pydantic import ValidationError

PROVENANCE: dict[str, Yaml] = {"source": "Test record."}


def e8() -> dict[str, Yaml]:
    """The root lattice E8: even, unimodular, positive definite, 240 minimal vectors."""
    return {
        "tag": "0001",
        "name": "E8",
        "latex": "E_8",
        "rank": 8,
        "gram_tensor": [
            [2, 0, -1, 0, 0, 0, 0, 0],
            [0, 2, 0, -1, 0, 0, 0, 0],
            [-1, 0, 2, -1, 0, 0, 0, 0],
            [0, -1, -1, 2, -1, 0, 0, 0],
            [0, 0, 0, -1, 2, -1, 0, 0],
            [0, 0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, 0, -1, 2, -1],
            [0, 0, 0, 0, 0, 0, -1, 2],
        ],
        "signature": [8, 0],
        "determinant": 1,
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [], "overlattice_count": 1},
        "definite": {
            "minimum": 2,
            "kissing_number": 240,
            "automorphism_group_order": 696729600,
            "theta_series": [1, 0, 240, 0, 2160, 0, 6720, 0, 17520],
            "root_system": ["E8"],
            # E8 in its basis of simple roots.
            "roots": [{"type": "E8", "scale": 1, "simple_roots": [[int(i == j) for j in range(8)] for i in range(8)]}],
        },
    }


def hyperbolic_plane() -> dict[str, Yaml]:
    """The even unimodular lattice of signature (1, 1)."""
    return {
        "tag": "0002",
        "name": "U",
        "latex": "U",
        "rank": 2,
        "gram_tensor": [[0, 1], [1, 0]],
        "signature": [1, 1],
        "determinant": -1,
        "definiteness": "indefinite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [], "overlattice_count": 1},
        "indefinite": {"isotropic": True},
    }


# The roots (1, 1) and (1, -1) of U have b(v, v) = 2 and -2 and are orthogonal: their span is M(2) + M(-2) for the record 0001 of rank 1.
ROOT_SPAN_SUMMANDS_OF_U: list[Yaml] = [{"tag": "0001", "scale": 2}, {"tag": "0001", "scale": -2}]


def a2_dual() -> dict[str, Yaml]:
    """The dual lattice of the root lattice A2:the form takes the value 2/3, so it is not integral."""
    return {
        "tag": "0003",
        "name": "A2*",
        "latex": "A_2^*",
        "rank": 2,
        "gram_tensor": [["2/3", "-1/3"], ["-1/3", "2/3"]],
        "signature": [2, 0],
        "determinant": "1/3",
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "definite": {
            "minimum": "2/3",
            "kissing_number": 6,
            "automorphism_group_order": 12,
            # A2* is A2 with the form b / 3, so its roots are those of A2: type G2, with b(e_1, e_1) = 2/3 and b(-e_1 + e_2, -e_1 + e_2) = 2.
            "roots": [{"type": "G2", "scale": "1/3", "simple_roots": [[1, 0], [-1, 1]]}],
        },
    }


def affine_a2() -> dict[str, Yaml]:
    """The affine root lattice of type A2: positive semidefinite with a radical of rank 1."""
    return {
        "tag": "0004",
        "name": "affine A2",
        "latex": r"\widetilde{A}_2",
        "rank": 3,
        "gram_tensor": [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]],
        "signature": [2, 0],
        "determinant": 0,
        "definiteness": "positive_semidefinite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even"},
    }


def binary_form_of_determinant_19() -> dict[str, Yaml]:
    """x = (1, -1) has b(x, x) = 2, and x = (1, 0) has b(x, x) = 10."""
    return {
        "tag": "0005",
        "name": "[10, 9, 10]",
        "latex": "[10, 9, 10]",
        "rank": 2,
        "gram_tensor": [[10, 9], [9, 10]],
        "signature": [2, 0],
        "determinant": 19,
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [19], "overlattice_count": 1},
        "definite": {
            "minimum": 2,
            "kissing_number": 2,
            "theta_series": [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0],
            "root_system": ["A1"],
            # Two orthogonal components of type A1, with b(r, r) = 2 and b(r, r) = 38.
            "roots": [{"type": "A1", "scale": 1, "simple_roots": [[1, -1]]}, {"type": "A1", "scale": 19, "simple_roots": [[1, 1]]}],
        },
    }


def anisotropic_binary() -> dict[str, Yaml]:
    """x^2 - 2y^2 has no nonzero rational zero, because 2 is not a square."""
    return {
        "tag": "0006",
        "name": "<1> + <-2>",
        "latex": r"\langle 1 \rangle \oplus \langle -2 \rangle",
        "rank": 2,
        "gram_tensor": [[1, 0], [0, -2]],
        "signature": [1, 1],
        "determinant": -2,
        "definiteness": "indefinite",
        "provenance": PROVENANCE,
        "integral": {"parity": "odd", "discriminant_group": [2], "overlattice_count": 1},
        "indefinite": {"isotropic": False},
    }


def square_lattice() -> dict[str, Yaml]:
    """I_{2,0}, the module Z^2 with the Euclidean form: the four x with b(x, x) = 2 generate the sublattice of index 2 of the x with even coordinate sum."""
    return {
        "tag": "0007",
        "name": "<1> + <1>",
        "latex": r"\langle 1 \rangle \oplus \langle 1 \rangle",
        "rank": 2,
        "gram_tensor": [[1, 0], [0, 1]],
        "signature": [2, 0],
        "determinant": 1,
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "integral": {"parity": "odd", "discriminant_group": [], "overlattice_count": 1},
        "definite": {
            "minimum": 1,
            "kissing_number": 4,
            "theta_series": [1, 4, 4, 0, 4, 8, 0, 0, 4, 4, 8, 0, 0],
            "root_system": ["A1", "A1"],
            # The simple roots e_1 - e_2 (long) and e_2 (short) of type B2; a short root has b(r, r) = 1.
            "roots": [{"type": "B2", "scale": "1/2", "simple_roots": [[1, -1], [0, 1]]}],
        },
    }


def a6() -> dict[str, Yaml]:
    """The root lattice A6 in a basis of simple roots: determinant 7, 42 roots. The root system D5 + A1 also has rank 6 and 42 roots."""
    return {
        "tag": "0008",
        "name": "A6",
        "latex": "A_6",
        "rank": 6,
        "gram_tensor": [[2 if i == j else -1 if abs(i - j) == 1 else 0 for j in range(6)] for i in range(6)],
        "signature": [6, 0],
        "determinant": 7,
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [7], "overlattice_count": 1},
        "definite": {
            "minimum": 2,
            "kissing_number": 42,
            "theta_series": [1, 0, 42, 0, 210, 0, 350, 0, 882],
            "root_system": ["A6"],
            "roots": [{"type": "A6", "scale": 1, "simple_roots": [[int(i == j) for j in range(6)] for i in range(6)]}],
        },
    }


def hyperbolic_plane_plus_a1() -> dict[str, Yaml]:
    """U + <-2>, of signature (1, 2), in the basis e, f, g with b(e, f) = 1 and b(g, g) = -2."""
    return {
        "tag": "0009",
        "name": "U + <-2>",
        "latex": r"U \oplus \langle -2 \rangle",
        "rank": 3,
        "gram_tensor": [[0, 1, 0], [1, 0, 0], [0, 0, -2]],
        "signature": [1, 2],
        "determinant": 2,
        "definiteness": "indefinite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [2], "overlattice_count": 1},
        "indefinite": {"isotropic": True},
    }


def a2() -> dict[str, Yaml]:
    """The root lattice A2 in a basis of simple roots: 6 vectors of norm 2, and 6 vectors of norm 6 that are also roots."""
    return {
        "tag": "000B",
        "name": "A2",
        "latex": "A_2",
        "rank": 2,
        "gram_tensor": [[2, -1], [-1, 2]],
        "signature": [2, 0],
        "determinant": 3,
        "definiteness": "positive_definite",
        "provenance": PROVENANCE,
        "integral": {"parity": "even", "discriminant_group": [3], "overlattice_count": 1},
        "definite": {
            "minimum": 2,
            "kissing_number": 6,
            "theta_series": [1, 0, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0],
            "root_system": ["A2"],
            # The simple roots e_1 (short) and -e_1 + e_2 (long, b = 6) of type G2, with b(e_1, -e_1 + e_2) = -3.
            "roots": [{"type": "G2", "scale": 1, "simple_roots": [[1, 0], [-1, 1]]}],
        },
    }


def with_block(record: dict[str, Yaml], block: str, **changes: Yaml) -> dict[str, Yaml]:
    current = record.get(block)
    assert isinstance(current, dict) or current is None
    return record | {block: (current or {}) | changes}


def without(record: dict[str, Yaml], block: str, field: str) -> dict[str, Yaml]:
    current = record[block]
    assert isinstance(current, dict)
    return record | {block: {key: value for key, value in current.items() if key != field}}


def error_types(record: dict[str, Yaml]) -> set[str]:
    with pytest.raises(ValidationError) as raised:
        Lattice.model_validate(record)
    return {error["type"] for error in raised.value.errors()}


@pytest.mark.parametrize(
    "record",
    [e8, hyperbolic_plane, a2_dual, affine_a2, binary_form_of_determinant_19, anisotropic_binary, square_lattice, a6, hyperbolic_plane_plus_a1, a2],
)
def test_consistent_record_is_accepted(record: Callable[[], dict[str, Yaml]]) -> None:
    Lattice.model_validate(record())


def test_derived_properties_follow_from_the_record() -> None:
    assert Lattice.model_validate(e8()).is_unimodular
    assert Lattice.model_validate(a2_dual()).determinant == Fraction(1, 3)
    assert not Lattice.model_validate(a2_dual()).is_unimodular
    assert Lattice.model_validate(affine_a2()).nullity == 1
    assert Lattice.model_validate(hyperbolic_plane()).is_hyperbolic
    assert not Lattice.model_validate(e8()).is_hyperbolic


def test_the_vectors_of_norm_two_generate_e8_and_a_sublattice_of_index_two_of_the_square_lattice() -> None:
    assert Lattice.model_validate(e8()).norm_two_span_index == 1
    square = Lattice.model_validate(square_lattice())
    assert square.norm_two_span_rank == 2
    assert square.norm_two_span_index == 2


def test_the_index_of_the_span_of_the_vectors_of_norm_two_is_not_stated_when_its_rank_is_less_than_the_rank_of_the_lattice() -> None:
    lattice = Lattice.model_validate(with_block(binary_form_of_determinant_19(), "definite", root_system=["A1"]))
    assert lattice.norm_two_span_rank == 1
    assert lattice.norm_two_span_index is None


def test_the_roots_of_a_definite_lattice_are_listed_with_every_value_of_the_form() -> None:
    # E8 is even and unimodular, so b(r, L) = Z for a primitive r, and a root has b(r, r) = 2: the 240 minimal vectors.
    assert len(Lattice.model_validate(e8()).positive_roots) == 120
    # The roots of I_{2,0} are the 4 vectors +-e_i and the 4 vectors +-e_1 +-e_2: type B2.
    square = Lattice.model_validate(square_lattice())
    assert set(square.positive_roots.items()) == {((1, 0), Fraction(1)), ((0, 1), Fraction(1)), ((1, 1), Fraction(2)), ((1, -1), Fraction(2))}
    # The roots of A2 are the 6 vectors of norm 2 and the 6 vectors of norm 6: type G2.
    assert sorted(Lattice.model_validate(a2()).positive_roots.values()) == [2, 2, 2, 6, 6, 6]
    # [10, 9, 10] has the roots +-(1, -1) of norm 2 and +-(1, 1) of norm 38: b((1, 1), L) = 19 Z.
    binary = Lattice.model_validate(binary_form_of_determinant_19())
    assert binary.positive_roots == {(1, -1): Fraction(2), (1, 1): Fraction(38)}


def test_a_definite_root_lattice_is_generated_by_its_roots() -> None:
    assert Lattice.model_validate(e8()).is_root_lattice
    assert Lattice.model_validate(e8()).root_norms == (Fraction(2),)
    assert Lattice.model_validate(a6()).root_norms == (Fraction(2),)
    # I_{2,0} is generated by e_1, e_2 with b(e_i, e_i) = 1.
    assert Lattice.model_validate(square_lattice()).root_norms == (Fraction(1),)
    # A2* is A2 with the form b / 3; its basis vectors have b(e_i, e_i) = 2/3.
    assert Lattice.model_validate(a2_dual()).root_norms == (Fraction(2, 3),)


def test_the_roots_of_a_definite_lattice_can_generate_a_sublattice_of_finite_index() -> None:
    # (1, -1) and (1, 1) generate the sublattice of index 2 of [10, 9, 10] of the vectors with even coordinate sum.
    binary = Lattice.model_validate(binary_form_of_determinant_19())
    assert binary.is_root_lattice is False
    assert binary.root_span_rank == 2
    assert binary.root_span_index == 2
    assert binary.root_span_is_primitive is False
    assert binary.root_norms is None


def test_roots_that_generate_a_lattice_that_is_not_definite_prove_that_it_is_a_root_lattice() -> None:
    # U + <-2> with basis e, f, g is generated by e - f, g and e + g, each with b(r, r) = -2.
    plane_plus_a1 = Lattice.model_validate(hyperbolic_plane_plus_a1() | {"root_span": {"roots": [[1, -1, 0], [0, 0, 1], [1, 0, 1]]}})
    assert plane_plus_a1.is_root_lattice
    assert plane_plus_a1.root_norms == (Fraction(-2),)
    # <1> + <-2> is generated by e_1 and e_2; the affine lattice of type A2 by its three simple roots.
    assert Lattice.model_validate(anisotropic_binary() | {"root_span": {"roots": [[1, 0], [0, 1]]}}).is_root_lattice
    affine = Lattice.model_validate(affine_a2() | {"root_span": {"roots": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}})
    assert affine.is_root_lattice
    assert affine.root_norms == (Fraction(2),)


def test_the_roots_of_the_hyperbolic_plane_generate_a_sublattice_of_index_two() -> None:
    # The roots of U are (1, 1), (1, -1) and their negatives.
    plane = Lattice.model_validate(hyperbolic_plane() | {"root_span": {"roots": [[1, 1], [1, -1]], "summands": ROOT_SPAN_SUMMANDS_OF_U, "embedding": [[1, 1], [1, -1]]}})
    assert plane.is_root_lattice is False
    assert plane.root_span_rank == 2
    assert plane.root_span_index == 2
    assert plane.root_span_is_primitive is False
    assert plane.root_norms is None


def test_a_lattice_with_no_roots_has_the_zero_sublattice_as_a_primitive_root_span() -> None:
    # Each x = (a, b) of <1> + <0> has b(x, x) = a^2, which is never 2.
    degenerate = Lattice.model_validate(
        {
            "tag": "000A",
            "name": "<1> + <0>",
            "latex": r"\langle 1 \rangle \oplus \langle 0 \rangle",
            "rank": 2,
            "gram_tensor": [[1, 0], [0, 0]],
            "signature": [1, 0],
            "determinant": 0,
            "definiteness": "positive_semidefinite",
            "provenance": PROVENANCE,
            "integral": {"parity": "odd"},
            "root_span": {"roots": []},
        }
    )
    assert degenerate.is_root_lattice is False
    assert degenerate.root_span_rank == 0
    assert degenerate.root_span_is_primitive is True


def test_a_lattice_that_is_not_definite_is_not_decided_without_a_root_span() -> None:
    plane = Lattice.model_validate(hyperbolic_plane())
    assert plane.is_root_lattice is None
    assert plane.root_span_rank is None
    assert plane.root_span_index is None
    assert plane.root_span_is_primitive is None
    assert plane.root_norms is None


def test_a_root_system_with_the_right_rank_and_number_of_roots_is_rejected_when_it_is_not_the_root_system_of_the_lattice() -> None:
    assert error_types(with_block(a6(), "definite", root_system=["D5", "A1"])) == {"root_system_mismatch"}


def test_a_theta_series_is_stated_past_the_minimum_and_further_for_a_small_rank() -> None:
    # Rank 8: through norm 8. Rank 2: through norm 12. A record can state more entries, and each is checked: [10, 9, 10] is even, so no x has b(x, x) = 13.
    assert error_types(with_block(e8(), "definite", theta_series=[1, 0, 240, 0, 2160, 0, 6720, 0])) == {"theta_series_short"}
    assert error_types(with_block(square_lattice(), "definite", theta_series=[1, 4, 4, 0, 4, 8, 0, 0, 4, 4, 8, 0])) == {"theta_series_short"}
    Lattice.model_validate(with_block(binary_form_of_determinant_19(), "definite", theta_series=[1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0]))
    assert error_types(with_block(binary_form_of_determinant_19(), "definite", theta_series=[1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0, 2])) == {"theta_series_mismatch"}


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        # A block on a lattice that does not satisfy the hypothesis of the block.
        (hyperbolic_plane() | {"definite": binary_form_of_determinant_19()["definite"]}, "definite_requires_definite"),
        (affine_a2() | {"definite": binary_form_of_determinant_19()["definite"]}, "definite_requires_definite"),
        (e8() | {"indefinite": {"isotropic": False}}, "indefinite_requires_indefinite"),
        (e8() | {"hyperbolic": {"reflective": True}}, "hyperbolic_requires_hyperbolic"),
        (a2_dual() | {"integral": {"parity": "even", "discriminant_group": [3]}}, "integral_requires_integer_values"),
        (with_block(a2_dual(), "definite", theta_series=[1, 0, 6]), "theta_requires_integral"),
        (with_block(a2_dual(), "definite", root_system=[]), "root_system_requires_integral"),
        (with_block(affine_a2(), "integral", discriminant_group=[2]), "discriminant_group_requires_nondegenerate"),
        (with_block(affine_a2(), "integral", genus_symbol="II_{2,0}"), "genus_requires_nondegenerate"),
        (with_block(affine_a2(), "integral", overlattice_count=1), "overlattice_count_requires_nondegenerate"),
        (without(a2(), "integral", "overlattice_count"), "overlattice_count_missing"),
        # The discriminant group of A2 has order 3 and a nondegenerate form, so the form vanishes on the trivial subgroup only.
        (with_block(a2(), "integral", overlattice_count=2), "overlattice_count_mismatch"),
        # A required block or field that is absent.
        ({key: value for key, value in e8().items() if key != "integral"}, "integral_block_missing"),
        (e8() | {"integral": {"parity": "even"}}, "discriminant_group_missing"),
        ({key: value for key, value in e8().items() if key != "definite"}, "definite_block_missing"),
        ({key: value for key, value in hyperbolic_plane().items() if key != "indefinite"}, "indefinite_block_missing"),
        (without(e8(), "definite", "theta_series"), "theta_series_missing"),
        (without(e8(), "definite", "root_system"), "root_system_missing"),
        (without(e8(), "definite", "roots"), "missing"),
        # A twist M(n) of a lattice M, with n = 2, n = 0 and n = -1; U + <2> is the twist by -1 of U + <-2>, whose signature (1, 2) is the one recorded.
        (square_lattice() | {"gram_tensor": [[2, 0], [0, 2]]}, "twisted"),
        (square_lattice() | {"gram_tensor": [[0, 0], [0, 0]]}, "twisted"),
        (square_lattice() | {"gram_tensor": [[-1, 0], [0, -1]]}, "twisted"),
        (hyperbolic_plane_plus_a1() | {"gram_tensor": [[0, 1, 0], [1, 0, 0], [0, 0, 2]]}, "twisted"),
        (hyperbolic_plane() | {"root_span": {"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 0}], "embedding": [[1, 1], [1, -1]]}}, "summand_scale_zero"),
        # A declaration that the Gram tensor contradicts.
        (e8() | {"rank": 7}, "gram_tensor_shape"),
        (hyperbolic_plane() | {"gram_tensor": [[0, 1], [2, 0]]}, "gram_tensor_not_symmetric"),
        (e8() | {"determinant": 2}, "determinant_mismatch"),
        (e8() | {"signature": [7, 1]}, "signature_mismatch"),
        (e8() | {"definiteness": "indefinite"}, "definiteness_mismatch"),
        (affine_a2() | {"definiteness": "positive_definite"}, "definiteness_mismatch"),
        (with_block(e8(), "integral", parity="odd"), "parity_mismatch"),
        (with_block(e8(), "integral", discriminant_group=[2]), "discriminant_group_mismatch"),
        (with_block(binary_form_of_determinant_19(), "integral", discriminant_group=[]), "discriminant_group_mismatch"),
        # Invariants of a definite lattice that the Gram tensor contradicts.
        (with_block(e8(), "definite", minimum=4), "minimum_mismatch"),
        (with_block(binary_form_of_determinant_19(), "definite", minimum=10), "minimum_mismatch"),
        (with_block(a2_dual(), "definite", minimum=2), "minimum_mismatch"),
        (with_block(e8(), "definite", kissing_number=242), "kissing_number_mismatch"),
        (with_block(a2_dual(), "definite", kissing_number=2), "kissing_number_mismatch"),
        (with_block(e8(), "definite", automorphism_group_order=696729601), "automorphism_order_odd"),
        (with_block(e8(), "definite", theta_series=[2, 0, 240, 0, 2160, 0, 6720, 0, 17520]), "theta_series_mismatch"),
        (with_block(e8(), "definite", theta_series=[1, 0, 240, 0, 2160, 0, 6720, 0, 17522]), "theta_series_mismatch"),
        (with_block(e8(), "definite", theta_series=[1, 0, 240, 0, 2160]), "theta_series_short"),
        (with_block(binary_form_of_determinant_19(), "definite", theta_series=[1, 2, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0]), "theta_series_mismatch"),
        # D8 has rank 8 and 112 roots; E7 + A1 has 128; E8 has 240. D5 + A1 has the rank and the number of roots of A6.
        (with_block(e8(), "definite", root_system=["D8"]), "root_system_mismatch"),
        (with_block(e8(), "definite", root_system=["E7", "A1"]), "root_system_mismatch"),
        (with_block(e8(), "definite", root_system=[]), "root_system_mismatch"),
        (with_block(a6(), "definite", root_system=["D5", "A1"]), "root_system_mismatch"),
        # I_{2,0} has the 4 vectors +-e_1 +-e_2 with b(r, r) = 2, and A1 has 2 roots.
        (with_block(square_lattice(), "definite", root_system=["A1"]), "root_system_mismatch"),
        # A root system that is not the set of roots of the lattice.
        # The vectors of norm 2 of A2 are a root system of type A2 with 6 roots; A2 has 12 roots.
        (with_block(a2(), "definite", roots=[{"type": "A2", "scale": 1, "simple_roots": [[1, 0], [0, 1]]}]), "root_count_mismatch"),
        # e_1 and e_2 are orthogonal roots of I_{2,0}, and they give 4 of its 8 roots.
        (
            with_block(
                square_lattice(),
                "definite",
                roots=[{"type": "A1", "scale": "1/2", "simple_roots": [[1, 0]]}, {"type": "A1", "scale": "1/2", "simple_roots": [[0, 1]]}],
            ),
            "root_count_mismatch",
        ),
        # The simple roots of E8 do not have the Gram matrix of D8.
        (
            with_block(e8(), "definite", roots=[{"type": "D8", "scale": 1, "simple_roots": [[int(i == j) for j in range(8)] for i in range(8)]}]),
            "simple_roots_gram_mismatch",
        ),
        # (1, 0) has b = 10 and b((1, 0), (0, 1)) = 9, so its reflection is not in O(L).
        (with_block(binary_form_of_determinant_19(), "definite", roots=[{"type": "A1", "scale": 5, "simple_roots": [[1, 0]]}]), "simple_root_not_root"),
        # The simple roots e_1 and e_2 of A2 are not orthogonal.
        (
            with_block(a2(), "definite", roots=[{"type": "A1", "scale": 1, "simple_roots": [[1, 0]]}, {"type": "A1", "scale": 1, "simple_roots": [[0, 1]]}]),
            "root_components_not_orthogonal",
        ),
        (with_block(e8(), "definite", roots=[{"type": "E8", "scale": 1, "simple_roots": [[1, 0, 0, 0, 0, 0, 0, 0]]}]), "roots_shape"),
        # The `root_span` block of a lattice that is not definite.
        (e8() | {"root_span": {"roots": []}}, "root_span_on_definite"),
        # b((1, 0), (1, 0)) = 0 in U, and (2, 2) is not primitive.
        (hyperbolic_plane() | {"root_span": {"roots": [[1, 0]]}}, "root_span_not_root"),
        (hyperbolic_plane() | {"root_span": {"roots": [[2, 2]]}}, "root_span_not_root"),
        (hyperbolic_plane() | {"root_span": {"roots": [[1, 1, 0]]}}, "root_span_shape"),
        (hyperbolic_plane() | {"root_span": {"roots": [[1, 1], [1, -1]], "summands": ROOT_SPAN_SUMMANDS_OF_U}}, "root_span_representative_incomplete"),
        # e and f generate U, and the roots (1, 1) and (1, -1) generate a sublattice of index 2.
        (
            hyperbolic_plane() | {"root_span": {"roots": [[1, 1], [1, -1]], "summands": ROOT_SPAN_SUMMANDS_OF_U, "embedding": [[1, 0], [0, 1]]}},
            "root_span_embedding_mismatch",
        ),
        # Isotropy that the rank and the determinant decide.
        (with_block(hyperbolic_plane(), "indefinite", isotropic=False), "isotropy_mismatch"),
        (with_block(anisotropic_binary(), "indefinite", isotropic=True), "isotropy_mismatch"),
        # Values outside the schema.
        (e8() | {"colour": "blue"}, "extra_forbidden"),
        (e8() | {"tag": "e8"}, "string_pattern_mismatch"),
        (e8() | {"determinant": 1.0}, "rational_type"),
        (e8() | {"determinant": "one"}, "rational_parsing"),
        (with_block(e8(), "definite", root_system=["E9"]), "string_pattern_mismatch"),
        (with_block(e8(), "definite", root_system=["D3"]), "string_pattern_mismatch"),
    ],
)
def test_inconsistent_record_is_rejected_for_its_reason(record: dict[str, Yaml], expected: str) -> None:
    assert expected in error_types(record)


def test_meyer_theorem_rejects_an_anisotropic_claim_in_rank_five() -> None:
    record = hyperbolic_plane() | {
        "rank": 5,
        "gram_tensor": [[7, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, -1]],
        "signature": [1, 4],
        "determinant": 7,
        "integral": {"parity": "odd", "discriminant_group": [7], "overlattice_count": 1},
        "indefinite": {"isotropic": False},
    }
    assert error_types(record) == {"isotropy_mismatch"}


def test_every_problem_of_a_record_is_reported_at_once() -> None:
    record = e8() | {"determinant": 3, "signature": [4, 4], "definiteness": "indefinite"}
    assert error_types(record) == {"determinant_mismatch", "signature_mismatch", "definiteness_mismatch"}


@pytest.mark.parametrize(
    ("matrix", "row_subdivisions", "column_subdivisions"),
    [
        ([[1, 0], [0]], [], []),
        ([[]], [], []),
        ([[1, 0], [0, 1]], [0], []),
        ([[1, 0], [0, 1]], [], [2]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [2, 1], []),
    ],
)
def test_a_morphism_is_rejected_when_its_matrix_is_not_rectangular_or_a_line_does_not_lie_inside_it(
    matrix: list[list[int]], row_subdivisions: list[int], column_subdivisions: list[int]
) -> None:
    with pytest.raises(ValidationError):
        Morphism.model_validate({"name": "phi", "matrix": matrix, "row_subdivisions": row_subdivisions, "column_subdivisions": column_subdivisions})


def test_the_images_of_a_morphism_are_the_columns_of_its_matrix() -> None:
    morphism = Morphism.model_validate({"name": "phi", "matrix": [[1, 2], [3, 4], [5, 6]], "row_subdivisions": [1, 2], "column_subdivisions": [1]})
    assert morphism.images == ((1, 3, 5), (2, 4, 6))
