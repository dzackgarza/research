"""A record validates exactly when its declarations agree with its Gram tensor."""

from fractions import Fraction

import pytest
from latticedb.model import Lattice, Yaml
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
        "integral": {"parity": "even", "discriminant_group": []},
        "definite": {
            "minimum": 2,
            "kissing_number": 240,
            "automorphism_group_order": 696729600,
            "theta_series": [1, 0, 240, 0, 2160],
            "root_system": ["E8"],
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
        "integral": {"parity": "even", "discriminant_group": []},
        "indefinite": {"isotropic": True},
    }


def a2_dual() -> dict[str, Yaml]:
    """The dual of the root lattice A2: the form takes the value 2/3, so it is not integral."""
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
        "definite": {"minimum": "2/3", "kissing_number": 6, "automorphism_group_order": 12},
    }


def affine_a1() -> dict[str, Yaml]:
    """The affine root lattice of type A1: positive semidefinite with a radical of rank 1."""
    return {
        "tag": "0004",
        "name": "affine A1",
        "latex": r"\widetilde{A}_1",
        "rank": 2,
        "gram_tensor": [[2, -2], [-2, 2]],
        "signature": [1, 0],
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
        "integral": {"parity": "even", "discriminant_group": [19]},
        "definite": {"minimum": 2, "kissing_number": 2},
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
        "integral": {"parity": "odd", "discriminant_group": [2]},
        "indefinite": {"isotropic": False},
    }


def with_block(record: dict[str, Yaml], block: str, **changes: Yaml) -> dict[str, Yaml]:
    current = record.get(block)
    assert isinstance(current, dict) or current is None
    return record | {block: (current or {}) | changes}


def error_types(record: dict[str, Yaml]) -> set[str]:
    with pytest.raises(ValidationError) as raised:
        Lattice.model_validate(record)
    return {error["type"] for error in raised.value.errors()}


@pytest.mark.parametrize("record", [e8, hyperbolic_plane, a2_dual, affine_a1, binary_form_of_determinant_19, anisotropic_binary])
def test_consistent_record_is_accepted(record):
    Lattice.model_validate(record())


def test_derived_properties_follow_from_the_record():
    assert Lattice.model_validate(e8()).is_unimodular
    assert Lattice.model_validate(a2_dual()).determinant == Fraction(1, 3)
    assert not Lattice.model_validate(a2_dual()).is_unimodular
    assert Lattice.model_validate(affine_a1()).nullity == 1
    assert Lattice.model_validate(hyperbolic_plane()).is_hyperbolic
    assert not Lattice.model_validate(e8()).is_hyperbolic


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        # A block on a lattice that does not satisfy the hypothesis of the block.
        (hyperbolic_plane() | {"definite": {"minimum": 2}}, "definite_requires_definite"),
        (affine_a1() | {"definite": {"minimum": 2}}, "definite_requires_definite"),
        (e8() | {"indefinite": {"isotropic": False}}, "indefinite_requires_indefinite"),
        (e8() | {"hyperbolic": {"reflective": True}}, "hyperbolic_requires_hyperbolic"),
        (a2_dual() | {"integral": {"parity": "even", "discriminant_group": [3]}}, "integral_requires_integer_values"),
        (with_block(a2_dual(), "definite", theta_series=[1, 0, 6]), "theta_requires_integral"),
        (with_block(a2_dual(), "definite", root_system=[]), "root_system_requires_integral"),
        (with_block(affine_a1(), "integral", discriminant_group=[2]), "discriminant_group_requires_nondegenerate"),
        (with_block(affine_a1(), "integral", genus_symbol="II_{1,0}"), "genus_requires_nondegenerate"),
        # A required block or field that is absent.
        ({key: value for key, value in e8().items() if key != "integral"}, "integral_block_missing"),
        (e8() | {"integral": {"parity": "even"}}, "discriminant_group_missing"),
        # A declaration that the Gram tensor contradicts.
        (e8() | {"rank": 7}, "gram_tensor_shape"),
        (hyperbolic_plane() | {"gram_tensor": [[0, 1], [2, 0]]}, "gram_tensor_not_symmetric"),
        (e8() | {"determinant": 2}, "determinant_mismatch"),
        (e8() | {"signature": [7, 1]}, "signature_mismatch"),
        (e8() | {"definiteness": "indefinite"}, "definiteness_mismatch"),
        (affine_a1() | {"definiteness": "positive_definite"}, "definiteness_mismatch"),
        (with_block(e8(), "integral", parity="odd"), "parity_mismatch"),
        (with_block(e8(), "integral", discriminant_group=[2]), "discriminant_group_mismatch"),
        (with_block(binary_form_of_determinant_19(), "integral", discriminant_group=[]), "discriminant_group_mismatch"),
        # Invariants of a definite lattice that cannot occur together.
        (with_block(e8(), "definite", minimum=0), "minimum_not_positive"),
        (with_block(e8(), "definite", minimum=4), "minimum_exceeds_diagonal"),
        (with_block(e8(), "definite", minimum=1), "minimum_not_even"),
        (with_block(e8(), "definite", minimum="3/2"), "minimum_not_integer"),
        (with_block(binary_form_of_determinant_19(), "definite", minimum=10), "minimum_violates_hermite"),
        (with_block(e8(), "definite", kissing_number=241), "kissing_number_odd"),
        (with_block(e8(), "definite", kissing_number=512), "kissing_number_exceeds_bound"),
        (with_block(a2_dual(), "definite", kissing_number=2), "kissing_number_below_basis_count"),
        (with_block(e8(), "definite", automorphism_group_order=696729601), "automorphism_order_odd"),
        (with_block(e8(), "definite", theta_series=[2, 0, 240]), "theta_constant_term"),
        (with_block(e8(), "definite", theta_series=[1, 0, 240, 0, 2161]), "theta_odd_coefficient"),
        (with_block(e8(), "definite", theta_series=[1, 0, 240, 2, 2160]), "theta_odd_norm_in_even_lattice"),
        (with_block(e8(), "definite", theta_series=[1, 0, 242, 0, 2160]), "theta_kissing_mismatch"),
        (with_block(binary_form_of_determinant_19(), "definite", theta_series=[1, 2, 2]), "theta_below_minimum"),
        (with_block(e8(), "definite", root_system=["E8", "A1"]), "root_system_rank"),
        (with_block(e8(), "definite", root_system=["D8"]), "root_system_theta_mismatch"),
        (with_block(e8(), "definite", root_system=["E7"]), "root_system_kissing_mismatch"),
        (
            binary_form_of_determinant_19() | {"gram_tensor": [[4, 1], [1, 5]], "definite": {"minimum": 4, "root_system": ["A1"]}},
            "root_system_nonempty_above_norm_two",
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
def test_inconsistent_record_is_rejected_for_its_reason(record, expected):
    assert expected in error_types(record)


def test_meyer_theorem_rejects_an_anisotropic_claim_in_rank_five():
    record = hyperbolic_plane() | {
        "rank": 5,
        "gram_tensor": [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, -7]],
        "signature": [4, 1],
        "determinant": -7,
        "integral": {"parity": "odd", "discriminant_group": [7]},
        "indefinite": {"isotropic": False},
    }
    assert error_types(record) == {"isotropy_mismatch"}


def test_every_problem_of_a_record_is_reported_at_once():
    record = e8() | {"determinant": 3, "signature": [4, 4], "definiteness": "indefinite"}
    assert error_types(record) == {"determinant_mismatch", "signature_mismatch", "definiteness_mismatch"}
