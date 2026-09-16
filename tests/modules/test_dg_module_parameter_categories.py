import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    DifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.modules import (
    DifferentialGradedModules,
    GradedAlgebraModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_graded_module_family_ranges_over_the_algebras_of_its_parameter() -> None:
    integers = _own_ring(SageZZ)
    algebra = GradedAlgebras(integers).an_object()

    assert GradedAlgebraModules(algebra).parameter_category() is GradedAlgebras(
        integers, algebra.grading_monoid()
    )
    with pytest.raises(AssertionError, match="parameterized by"):
        GradedAlgebraModules(integers)


def test_dg_module_family_ranges_over_the_dg_algebras_of_its_parameter() -> None:
    integers = _own_ring(SageZZ)
    dga = DifferentialGradedAlgebras(integers).an_object()

    assert DifferentialGradedModules(dga).parameter_category() is DifferentialGradedAlgebras(integers)
    assert dga in GradedAlgebras(integers, dga.grading_monoid())
    with pytest.raises(AssertionError, match="parameterized by"):
        DifferentialGradedModules(integers)
