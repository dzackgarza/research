r"""Graded commutativity is stated over any grading that has a parity.

The Koszul sign is ``(-1)^(eps(p) eps(q))``, so what the rule needs of a
grading monoid is the homomorphism ``eps`` into ``ZZ/2`` and nothing else.
The parity is part of the grading datum: the integers and ``ZZ/2`` carry a
canonical ``eps``, any other monoid states one with the grading.
"""

import pytest

from dzack_research.preamble.all import (
    NN,
    ZZ,
    GradedAlgebras,
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.rings.ring_foundation import Zmod


def test_the_integer_grading_carries_its_canonical_parity() -> None:
    algebras = GradedAlgebras(ZZ).Supercommutative()
    degrees = algebras.grading_monoid()
    parity = algebras.parity_homomorphism()

    assert parity.domain() is degrees
    assert parity.codomain() is Zmod(2)
    assert parity(degrees(3)) == Zmod(2)(1)
    assert parity(degrees(4)) == Zmod(2)(0)


def test_a_superalgebra_is_graded_by_the_parity_it_states() -> None:
    two = Zmod(2)
    identity = two.Mor(two)(lambda degree: degree)
    superalgebras = GradedAlgebras(ZZ, two, identity).Supercommutative()

    assert superalgebras.grading_monoid() is two
    assert superalgebras.parity_homomorphism() is identity


def test_strict_graded_commutativity_keeps_the_grading_it_was_given() -> None:
    two = Zmod(2)
    identity = two.Mor(two)(lambda degree: degree)
    strict = StrictlyGradedCommutativeAlgebras(ZZ, two, identity)

    assert strict.grading_monoid() is two
    assert strict.parity_homomorphism() is identity
    assert GradedAlgebras(ZZ, two, identity).Supercommutative() in strict.super_categories()


def test_a_grading_with_no_canonical_parity_names_the_datum_it_wants() -> None:
    r"""The refusal is about the missing parity, not about which monoid it is."""
    with pytest.raises(AssertionError, match="parity"):
        GradedAlgebras(ZZ, NN).Supercommutative()
