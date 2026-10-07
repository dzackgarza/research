"""A record validates exactly when its fields have the shapes of the schema and each block is present exactly when its hypothesis holds."""

import ast
from collections.abc import Callable
from fractions import Fraction
from pathlib import Path

import pytest
from latticedb import certificates
from latticedb.model import GroupData, Lattice, Morphism, Yaml
from pydantic import ValidationError


ROOT = Path(__file__).resolve().parent.parent


def test_latticedb_has_no_direct_mathematical_engine_imports() -> None:
    """Mathematical computation crosses the research-preamble boundary."""
    forbidden = ("sage", "cypari2", "flint", "fpylll")
    for path in sorted((ROOT / "src" / "latticedb").glob("*.py")):
        tree = ast.parse(path.read_text())
        modules = {
            node.module
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module is not None
        } | {
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        assert not any(
            module == prefix or module.startswith(prefix + ".")
            for module in modules
            for prefix in forbidden
        ), path.relative_to(ROOT)
    assert not (ROOT / "src" / "latticedb" / "roots.py").exists()
    assert not (ROOT / "src" / "latticedb" / "root_systems.py").exists()


def test_model_does_not_recompute_authored_mathematical_invariants() -> None:
    """Mathematical truth is checked by CI validation, not by Pydantic construction."""
    record = e8()
    integral = dict(record["integral"])
    integral["level"] = 17
    integral["bad_reduction_primes"] = [17]
    integral["quadratic_character"] = 17
    record["integral"] = integral
    lattice = Lattice.model_validate(record)
    assert lattice.integral is not None
    assert lattice.integral.level == 17


def test_group_cardinality_is_plain_serialized_schema_data() -> None:
    assert GroupData.model_validate({"cardinality": 8}).cardinality == 8
    assert GroupData.model_validate({"cardinality": "aleph0"}).cardinality == "aleph0"
    with pytest.raises(ValidationError):
        GroupData.model_validate({"cardinality": 0})


def test_definite_group_generators_name_scale_one_self_morphisms() -> None:
    record = e8()
    generator = [[-int(i == j) for j in range(8)] for i in range(8)]
    record["morphisms"] = [{"target": "0001", "name": "minus identity", "matrix": generator}]
    definite = dict(record["definite"])
    definite["automorphism_group_generator_morphisms"] = ["minus identity"]
    record["definite"] = definite
    lattice = Lattice.model_validate(record)
    assert lattice.definite is not None
    assert lattice.definite.automorphism_group_generator_morphisms == ("minus identity",)

    bad = dict(record)
    bad_definite = dict(definite)
    bad_definite["automorphism_group_generator_morphisms"] = ["missing"]
    bad["definite"] = bad_definite
    with pytest.raises(ValidationError, match="each generator name occurs once"):
        Lattice.model_validate(bad)


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
        "integral": {"parity": "even", "discriminant_group": [], "overlattice_count": 1, "delta": 0, "bad_reduction_primes": [2], "quadratic_character": 1},
        "definite": {
            "minimum": 2,
            "kissing_number": 240,
            "automorphism_group_order": 696729600,
            "theta_series": [1, 0, 240, 0, 2160, 0, 6720, 0, 17520],
            "root_system": ["E8"],
            # E8 in its basis of simple roots.
            "roots": [{"type": "E8", "scale": 1, "simple_roots": [[int(i == j) for j in range(8)] for i in range(8)]}],
        },
        "root_sublattice": {"invariant_factors": [1] * 8, "norms": [2]},
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
        "integral": {"parity": "even", "discriminant_group": [], "overlattice_count": 1, "delta": 0, "bad_reduction_primes": [2], "quadratic_character": 1},
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
        "definite": {
            "minimum": "2/3",
            "kissing_number": 6,
            "automorphism_group_order": 12,
            # A2* is A2 with the form b / 3, so its roots are those of A2: type G2, with b(e_1, e_1) = 2/3 and b(-e_1 + e_2, -e_1 + e_2) = 2.
            "roots": [{"type": "G2", "scale": "1/3", "simple_roots": [[1, 0], [-1, 1]]}],
        },
        "root_sublattice": {"invariant_factors": [1, 1], "norms": ["2/3"]},
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
        "integral": {"parity": "even", "discriminant_group": [19], "overlattice_count": 1, "bad_reduction_primes": [2, 19], "quadratic_character": -19},
        "definite": {
            "minimum": 2,
            "kissing_number": 2,
            "theta_series": [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 0],
            "root_system": ["A1"],
            # Two orthogonal components of type A1, with b(r, r) = 2 and b(r, r) = 38.
            "roots": [{"type": "A1", "scale": 1, "simple_roots": [[1, -1]]}, {"type": "A1", "scale": 19, "simple_roots": [[1, 1]]}],
        },
        # (1, -1) and (1, 1) generate the vectors with even coordinate sum.
        "root_sublattice": {"invariant_factors": [1, 2]},
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
        "integral": {"parity": "odd", "discriminant_group": [2], "overlattice_count": 1, "bad_reduction_primes": [2], "quadratic_character": 8},
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
        "integral": {"parity": "odd", "discriminant_group": [], "overlattice_count": 1, "bad_reduction_primes": [2], "quadratic_character": -4},
        "definite": {
            "minimum": 1,
            "kissing_number": 4,
            "theta_series": [1, 4, 4, 0, 4, 8, 0, 0, 4, 4, 8, 0, 0],
            "root_system": ["A1", "A1"],
            # The simple roots e_1 - e_2 (long) and e_2 (short) of type B2; a short root has b(r, r) = 1.
            "roots": [{"type": "B2", "scale": "1/2", "simple_roots": [[1, -1], [0, 1]]}],
        },
        "root_sublattice": {"invariant_factors": [1, 1], "norms": [1]},
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
        "integral": {"parity": "even", "discriminant_group": [7], "overlattice_count": 1, "bad_reduction_primes": [2, 7], "quadratic_character": -7},
        "definite": {
            "minimum": 2,
            "kissing_number": 42,
            "theta_series": [1, 0, 42, 0, 210, 0, 350, 0, 882],
            "root_system": ["A6"],
            "roots": [{"type": "A6", "scale": 1, "simple_roots": [[int(i == j) for j in range(6)] for i in range(6)]}],
        },
        "root_sublattice": {"invariant_factors": [1] * 6, "norms": [2]},
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
        "integral": {"parity": "even", "discriminant_group": [2], "overlattice_count": 1, "delta": 1, "bad_reduction_primes": [2]},
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
        "integral": {"parity": "even", "discriminant_group": [3], "overlattice_count": 1, "bad_reduction_primes": [2, 3], "quadratic_character": -3},
        "definite": {
            "minimum": 2,
            "kissing_number": 6,
            "theta_series": [1, 0, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0],
            "root_system": ["A2"],
            # The simple roots e_1 (short) and -e_1 + e_2 (long, b = 6) of type G2, with b(e_1, -e_1 + e_2) = -3.
            "roots": [{"type": "G2", "scale": 1, "simple_roots": [[1, 0], [-1, 1]]}],
        },
        "root_sublattice": {"invariant_factors": [1, 1], "norms": [2]},
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


def with_root_span(record: dict[str, Yaml], span: dict[str, Yaml], sublattice: dict[str, Yaml]) -> dict[str, Yaml]:
    return record | {"root_span": span, "root_sublattice": sublattice}


# The roots (1, 1) and (1, -1) of U, with b(r, r) = 2 and -2, generate a sublattice of index 2.
ROOT_SPAN_OF_U: dict[str, Yaml] = {"roots": [[1, 1], [1, -1]], "norms": [2, -2], "summands": ROOT_SPAN_SUMMANDS_OF_U, "embedding": [[1, 1], [1, -1]]}
ROOT_SUBLATTICE_OF_U: dict[str, Yaml] = {"invariant_factors": [1, 2]}


def test_certificate_hash_uses_the_stored_result_without_recomputing_it() -> None:
    lattice = Lattice.model_validate(e8())
    computation = "0001 definite.automorphism_group_order"
    assert lattice.definite is not None
    value = lattice.definite.automorphism_group_order
    certificate_hash = certificates.certification_hash(computation, lattice, value)
    held = {
        computation: certificates.Certificate(hash=certificate_hash, by="test")
    }
    assert certificates.is_certified(
        held, computation, certificate_hash, certificate_hash
    )
    assert not certificates.is_certified(held, computation, None, certificate_hash)
    changed = certificates.certification_hash(computation, lattice, 1)
    assert changed != certificate_hash
    assert not certificates.is_certified(held, computation, certificate_hash, changed)


def with_orbits(record: dict[str, Yaml], **series: list[int]) -> dict[str, Yaml]:
    """`record` with the series of orbits of primitive vectors whose coefficients of z are given for each group; `Otilde_plus` names `Otilde+`."""
    return with_block(record, "integral", primitive_orbits={group.replace("_plus", "+"): {"z": z} for group, z in series.items()})


def test_the_series_of_orbits_of_a2_is_accepted() -> None:
    # O~(A2) = W(A2) is simply transitive on the 6 roots, and its subgroup of rotations has 2 orbits on them.
    one, two = [0, 1, 0, 0], [0, 2, 0, 0]
    lattice = Lattice.model_validate(with_orbits(a2(), O=one, SO=one, O_plus=one, SO_plus=one, Otilde=one, SOtilde=two, Otilde_plus=two, SOtilde_plus=two))
    assert lattice.integral is not None and lattice.integral.primitive_orbits is not None
    assert lattice.integral.primitive_orbits["SOtilde"].coefficient(2) == 2
    assert lattice.integral.primitive_orbits["SOtilde"].coefficient(-2) is None


def test_orbit_series_are_stored_schema_data_not_mathematically_recomputed() -> None:
    lattice = Lattice.model_validate(
        with_orbits(a2(), O=[1, 1], SO=[0, 0], O_plus=[7, 3])
    )
    assert lattice.integral is not None
    assert lattice.integral.primitive_orbits is not None
    assert lattice.integral.primitive_orbits["O"].z == (1, 1)


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        (hyperbolic_plane() | {"root_sublattice": ROOT_SUBLATTICE_OF_U}, "root_sublattice_not_decided"),
        (hyperbolic_plane() | {"root_span": {"roots": [[1, 1], [1, -1]], "summands": [{"tag": "0001", "scale": 0}], "embedding": [[1, 1], [1, -1]]}}, "summand_scale_zero"),
        (e8() | {"rank": 7}, "gram_tensor_shape"),
        (e8() | {"signature": [8, 1]}, "signature_shape"),
        (with_block(e8(), "definite", roots=[{"type": "E8", "scale": 1, "simple_roots": [[1, 0, 0, 0, 0, 0, 0, 0]]}]), "roots_shape"),
        (with_root_span(hyperbolic_plane(), {"roots": [[1, 1, 0]], "norms": [2]}, {"invariant_factors": [1]}), "root_span_shape"),
        (with_root_span(hyperbolic_plane(), {"roots": [[1, 1], [1, -1]], "norms": [2]}, ROOT_SUBLATTICE_OF_U), "root_span_norms_shape"),
        (with_root_span(hyperbolic_plane(), ROOT_SPAN_OF_U | {"embedding": None}, ROOT_SUBLATTICE_OF_U), "root_span_representative_incomplete"),
        (e8() | {"root_span": {"roots": [], "norms": []}}, "root_span_on_definite"),
        (with_block(e8(), "root_sublattice", invariant_factors=[1] * 9), "root_sublattice_factors_shape"),
        (with_root_span(hyperbolic_plane(), ROOT_SPAN_OF_U, {"invariant_factors": [2, 3]}), "root_sublattice_factors_shape"),
        (e8() | {"colour": "blue"}, "extra_forbidden"),
        (e8() | {"tag": "e8"}, "string_pattern_mismatch"),
        (e8() | {"determinant": 1.0}, "rational_type"),
        (e8() | {"determinant": "one"}, "rational_parsing"),
        (with_block(e8(), "definite", root_system=["E9"]), "string_pattern_mismatch"),
        (with_block(e8(), "definite", root_system=["D3"]), "string_pattern_mismatch"),
    ],
)
def test_structurally_inconsistent_record_is_rejected(record: dict[str, Yaml], expected: str) -> None:
    assert expected in error_types(record)


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
        Morphism.model_validate({"target": "0001", "name": "phi", "matrix": matrix, "row_subdivisions": row_subdivisions, "column_subdivisions": column_subdivisions})


def test_the_images_of_a_morphism_are_the_columns_of_its_matrix() -> None:
    morphism = Morphism.model_validate({"target": "0001", "name": "phi", "matrix": [[1, 2], [3, 4], [5, 6]], "row_subdivisions": [1, 2], "column_subdivisions": [1]})
    assert morphism.images == ((1, 3, 5), (2, 4, 6))
