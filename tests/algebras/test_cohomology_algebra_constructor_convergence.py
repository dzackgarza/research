r"""Cohomology algebras are constructed by their codomain category."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.algebras.cohomology_algebras import (
    CohomologyAlgebra,
    CohomologyAlgebras,
)
from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras
from dzack_research.preamble.categories.algebras.differential_graded_algebras import DifferentialGradedAlgebras


def test_notation_and_functor_land_in_the_category_owned_object() -> None:
    dga = DeRhamAlgebras(ZZ).an_object()
    category = CohomologyAlgebras(ZZ)

    assert dga.de_rham_source_algebra().module_generating_set().cardinality() == 2
    assert dga.graded_piece(0).module_generating_set().cardinality() == 2

    declared = category(dga)
    notation = CohomologyAlgebra(dga)
    functor_image = DifferentialGradedAlgebras(ZZ).cohomology_algebra()(dga)

    assert declared is notation
    assert declared is functor_image
    assert declared in category
    assert declared.source_dga() is dga
    assert declared.one().parent() is declared

