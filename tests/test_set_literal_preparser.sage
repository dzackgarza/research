r"""Isolated behavioral proofs for the notebook's mathematical preparser."""

from itertools import islice

from dzack_research.preamble.preparser import preparse
from sage.sets.condition_set import ConditionSet
from sage.sets.image_set import ImageSet


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
