r"""Isolated behavioral proofs for the notebook's mathematical preparser."""

from itertools import islice
import shutil
import subprocess
import tempfile
from pathlib import Path

from dzack_research.preamble.preparser import preparse
from sage.sets.condition_set import ConditionSet
from sage.sets.image_set import ImageSet
import pytest


def _execute(source):
    namespace = dict(globals())
    exec(preparse(source), namespace)
    return namespace


def test_mathematical_set_notation_executes_without_loading_the_preamble():
    namespace = _execute(
        "literal = {1, 2, 3}; "
        "nested = {{1, 2}, {3, 4}}; "
        'mapping = {"one": 1}; '
        'sets_in_mapping = {"odds": {1, 3}}; '
        "comprehension = {x for x in [1, 2, 2, 3]}; "
        "negatives = {-n | n in NN}; "
        "primes = {x in NN | x.is_prime()}; "
        "primes_right = {x | x in NN and x.is_prime()}; "
        "affine = {3x + 2 | x in ZZ}; "
        "even_integers = {x in ZZ | x in 2*ZZ}"
    )

    assert namespace["literal"] == Set([1, 2, 3])
    assert namespace["nested"] == Set([Set([1, 2]), Set([3, 4])])
    assert namespace["mapping"] == {"one": 1}
    assert namespace["sets_in_mapping"]["odds"] == Set([1, 3])
    assert namespace["comprehension"] == Set([1, 2, 3])
    assert tuple(islice(namespace["negatives"], 4)) == (0, -1, -2, -3)
    assert tuple(islice(namespace["primes"], 4)) == (2, 3, 5, 7)
    assert tuple(islice(namespace["primes_right"], 4)) == (2, 3, 5, 7)
    assert tuple(islice(namespace["affine"], 5)) == (2, 5, -1, 8, -4)
    assert tuple(islice(namespace["even_integers"], 8)) == (
        0,
        2,
        -2,
        4,
        -4,
        6,
        -6,
        8,
    )


def test_preparser_composes_with_sage_generator_declarations():
    namespace = _execute(
        "R.<x, y> = PolynomialRing(QQ, 2); "
        "generators = {x, y}; "
        "quadrics = {u^2 | u in generators}"
    )

    assert namespace["R"].gens() == (namespace["x"], namespace["y"])
    assert namespace["generators"] == Set([namespace["x"], namespace["y"]])
    assert Set(tuple(namespace["quadrics"])) == Set(
        [namespace["x"]^2, namespace["y"]^2]
    )


def test_direct_preparse_applies_implicit_multiplication_in_derivatives():
    namespace = _execute("x = var('x'); result = diff(x^5 + 2x, x)")

    assert namespace["result"] == 5 * namespace["x"]^4 + 2


def test_direct_preparse_applies_implicit_multiplication_in_integrals():
    namespace = _execute("x = var('x'); result = integral(3x^2, x)")

    assert namespace["result"] == namespace["x"]^3


def test_direct_preparse_applies_implicit_multiplication_in_matrices():
    namespace = _execute(
        "x = var('x'); result = matrix(SR, [[x, 2x], [3x, 4x]])"
    )
    x = namespace["x"]

    assert namespace["result"] == matrix(SR, [[x, 2*x], [3*x, 4*x]])


def test_direct_preparse_applies_implicit_multiplication_in_functions():
    namespace = _execute(
        "f(x, y) = x^2 + 2x*y + y^2; result = f(1, 2)"
    )

    assert namespace["result"] == 9


def test_identity_builder_on_a_finite_range_is_the_extensional_set():
    namespace = _execute("result = {x | x in [1..5]}")

    assert namespace["result"] == Set([1, 2, 3, 4, 5])


def test_identity_builder_on_nested_sets_is_the_extensional_set():
    namespace = _execute("result = {x | x in {{1, 2}, {3, 4}}}")

    assert namespace["result"] == Set([Set([1, 2]), Set([3, 4])])


def test_fstring_replacement_fields_preserve_sage_expressions():
    namespace = _execute("x = 7; result = f'{x}'")

    assert namespace["result"] == "7"


def test_fstring_escaped_braces_preserve_replacement_fields():
    namespace = _execute("x = 7; result = f'{{{x}}}'")

    assert namespace["result"] == "{7}"


def test_fstring_dictionary_expressions_remain_dictionaries():
    namespace = _execute("""result = f"{ {'a': 1} }" """)

    assert namespace["result"] == "{'a': 1}"


def test_sage_command_preparse_compiles_match_case_with_integer_patterns():
    """The `.sage` preparse command output must be repaired by the preparse wrapper."""
    if shutil.which("sage") is None:
        pytest.skip("Sage CLI unavailable for preparse regression check")

    source = """
def classify(x):
    match x:
        case 0:
            return 0
        case -1:
            return -1
        case 1:
            return 1
        case _:
            return x
""".strip()

    with tempfile.TemporaryDirectory() as work_dir:
        path = Path(work_dir) / "classify.sage"
        path.write_text(source)
        run = subprocess.run(
            ["sage", "--preparse", str(path)],
            cwd=work_dir,
            check=False,
            capture_output=True,
            text=True,
        )
        assert run.returncode == 0, run.stderr
        generated = Path(f"{path}.py")
        assert generated.exists(), f"expected generated file {generated}"

        repaired = preparse(generated.read_text())
        assert "case _sage_const_" not in repaired
        compile(repaired, "<sage-preparse>", "exec")


def test_native_sage_preparse_does_not_break_match_case_integers():
    source = "def classify(x):\n    match x:\n        case 0:\n            return 0\n        case -1:\n            return -1\n        case 1:\n            return 1\n        case _:\n            return x\n"
    repaired = preparse(source)
    compile(repaired, "<preparsed>", "exec")

    namespace = _execute(source)
    assert namespace["classify"](0) == 0
    assert namespace["classify"](-1) == -1
    assert namespace["classify"](1) == 1
    assert namespace["classify"](7) == 7


def test_multiline_identity_builder_preserves_its_domain():
    namespace = _execute(
        """
result = {
    x |
    x in ZZ
}
"""
    )

    assert tuple(islice(namespace["result"], 5)) == (0, 1, -1, 2, -2)


def test_bitwise_or_is_an_ordinary_set_element():
    namespace = _execute("result = {1 | 2}")

    assert namespace["result"] == Set([3])


def test_bitwise_or_is_an_ordinary_dictionary_value():
    namespace = _execute("result = {'a': 1 | 2}")

    assert namespace["result"] == {"a": 3}


def test_bitwise_or_is_preserved_in_set_comprehensions():
    namespace = _execute("result = {x | 1 for x in range(3)}")

    assert namespace["result"] == Set([1, 3])


def test_bitwise_or_is_preserved_in_dictionary_comprehensions():
    namespace = _execute("result = {x: x | 1 for x in range(3)}")

    assert namespace["result"] == {0: 1, 1: 1, 2: 3}
