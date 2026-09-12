import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    DifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.modules import (
    DifferentialGradedAlgebraParameters,
    DifferentialGradedModules,
    GradedAlgebraModules,
    GradedAlgebraParameters,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_graded_module_family_states_its_parameter_domain() -> None:
    integers = _own_ring(SageZZ)
    algebra = GradedAlgebras(integers).an_object()

    assert algebra in GradedAlgebraParameters()
    assert GradedAlgebraModules(algebra).parameter_category() is GradedAlgebraParameters()
    with pytest.raises(AssertionError, match="parameterized by"):
        GradedAlgebraModules(integers)


def test_dg_module_family_states_its_parameter_domain() -> None:
    integers = _own_ring(SageZZ)
    dga = DifferentialGradedAlgebras(integers).an_object()

    assert dga in DifferentialGradedAlgebraParameters()
    assert dga in GradedAlgebraParameters()
    assert (
        DifferentialGradedModules(dga).parameter_category()
        is DifferentialGradedAlgebraParameters()
    )
    with pytest.raises(AssertionError, match="parameterized by"):
        DifferentialGradedModules(integers)
