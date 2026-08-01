r"""Behavioral proofs for the notebook's mathematical set preparser."""

from itertools import islice
from pathlib import Path

import dzack_research

from dzack_research.preamble.preparse_sets import install_set_literal_preparser
from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse


_preamble = Path(dzack_research.__file__).resolve().parent / "preamble"
load(str(_preamble / "install.sage"))
sage_preparse.implicit_multiplication(True)
install_set_literal_preparser(sage_preparse, sage_interpreter)


def test_mathematical_set_builders_execute_after_sage_preparsing():
    namespace = dict(globals())
    source = (
        "literal = {1, 2, 3}; "
        'mapping = {"one": 1}; '
        "negatives = {-n | n in NN}; "
        "primes = {x in NN | x.is_prime()}; "
        "affine = {3x + 2 | x in ZZ}"
    )
    exec(sage_preparse.preparse(source), namespace)

    assert namespace["literal"].equal_as_sets(Set([1, 2, 3]))
    assert namespace["mapping"] == {"one": 1}
    assert tuple(islice(namespace["negatives"], 4)) == (0, -1, -2, -3)
    assert tuple(islice(namespace["primes"], 4)) == (2, 3, 5, 7)
    assert tuple(islice(namespace["affine"], 5)) == (2, 5, -1, 8, -4)
