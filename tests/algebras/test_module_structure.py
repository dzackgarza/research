
from dzack_research.preamble.all import (
    QQ,
    Modules,
)












def test_presented_pid_algebra_flatness_uses_the_exact_scalar_kernel() -> None:
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    presentation = parameter.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family = (presentation).quotient_by_relations((x * y - t,))

    assert family in Modules(parameter)
    assert family.is_integral_domain()
    assert family.is_torsion_free()
    assert family.is_flat()

    killed_presentation = parameter.polynomial_ring(("z", "w"))
    killed = (killed_presentation).quotient_by_relations((t,))
    assert killed.is_integral_domain()
    assert not killed.is_torsion_free()
    assert not killed.is_flat()














