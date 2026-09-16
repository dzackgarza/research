r"""Kähler differential notation and consumers use the category constructor."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.kahler_differentials import (
    KahlerDifferentialModules,
)


def test_kahler_notation_is_the_category_owned_object() -> None:
    algebra = Algebras(ZZ).Associative().Unital().Commutative().an_object()
    category = KahlerDifferentialModules(algebra)

    declared = category(algebra)
    notation = algebra.kahler_differentials()

    assert declared is notation
    assert declared in category
    assert declared.source_algebra() is algebra
    assert declared.universal_derivation().domain() is algebra

