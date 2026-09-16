r"""The de Rham functor and notation use the category-owned construction."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.de_rham_algebras import (
    DeRhamAlgebras,
)


def test_de_rham_routes_share_one_category_owned_object() -> None:
    algebra = Algebras(ZZ).Associative().Unital().Commutative().an_object()
    category = DeRhamAlgebras(ZZ)

    declared = category(algebra)
    notation = algebra.de_rham_algebra()
    functor_image = Algebras(ZZ).Associative().Unital().Commutative().de_rham()(algebra)

    assert declared is notation
    assert declared is functor_image
    assert declared in category
    assert declared.de_rham_source_algebra() is algebra
    assert declared.kahler_differentials().source_algebra() is algebra
