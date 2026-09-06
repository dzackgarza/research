r"""Graded commutativity is stated over any grading that has a parity.

The Koszul sign is ``(-1)^(eps(p) eps(q))``, so what the rule needs of a
grading monoid is the homomorphism ``eps`` into ``ZZ/2`` and nothing else.
The integers are the grading with a canonical ``eps``; a superalgebra is
graded by ``ZZ/2`` and states the identity.
"""

import pytest

from dzack_research.preamble.all import (
    GradedCommutativeAlgebras,
    StrictlyGradedCommutativeAlgebras,
    ZZ,
)
from dzack_research.preamble.categories.rings.ring_foundation import Zmod, ring_morphism


def test_the_integer_grading_carries_its_canonical_parity() -> None:
    parity = GradedCommutativeAlgebras(ZZ).parity_homomorphism()

    assert parity.domain() is ZZ
    assert parity.codomain() is Zmod(2)
    assert parity(ZZ(3)) == Zmod(2)(1)
    assert parity(ZZ(4)) == Zmod(2)(0)


def test_a_superalgebra_is_graded_by_the_parity_it_states() -> None:
    two = Zmod(2)
    identity = ring_morphism(two, two, lambda degree: degree)
    superalgebras = GradedCommutativeAlgebras(ZZ, two, identity)

    assert superalgebras.grading_monoid() is two
    assert superalgebras.parity_homomorphism() is identity


def test_strict_graded_commutativity_keeps_the_grading_it_was_given() -> None:
    two = Zmod(2)
    identity = ring_morphism(two, two, lambda degree: degree)
    strict = StrictlyGradedCommutativeAlgebras(ZZ, two, identity)

    assert strict.grading_monoid() is two
    assert GradedCommutativeAlgebras(ZZ, two, identity) in strict.super_categories()


def test_a_grading_with_no_canonical_parity_names_the_datum_it_wants() -> None:
    r"""The refusal is about the missing parity, not about which monoid it is."""
    with pytest.raises(AssertionError, match="parity"):
        GradedCommutativeAlgebras(ZZ, Zmod(2))
