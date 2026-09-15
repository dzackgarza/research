r"""Kähler differential notation and consumers use the category constructor."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
from dzack_research.preamble.categories.algebras.kahler_differentials import (
    KahlerDifferentialModules,
    KahlerDifferentials,
)


def test_kahler_notation_is_the_category_owned_object() -> None:
    algebra = CommutativeAlgebras(ZZ).an_object()
    category = KahlerDifferentialModules(algebra)

    declared = category(algebra)
    notation = algebra.kahler_differentials()

    assert declared is notation
    assert declared in category
    assert declared.source_algebra() is algebra
    assert declared.universal_derivation().domain() is algebra

