r"""Finite component representatives retain their original quotient classes."""

from dzack_research.preamble.all import ZZ, Modules
from dzack_research.preamble.categories.modules import FinitelyPresentedTorsionModules


def test_word_component_reduction_preserves_quotients_and_mixed_torsion() -> None:
    two = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2,))
    three = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((3,))
    tensor = Modules(ZZ).tensor_product((two, three))
    mixed = tensor.pure_tensor(two.module_generator(0), three.module_generator(0))
    reduced = tensor._smith_representative(mixed)
    assert reduced.parent() is tensor
    assert reduced == mixed == tensor.zero()
    value = three.module_generator(0)
    reduced_value = three._smith_representative(4 * value)
    assert reduced_value.parent() is three
    assert reduced_value == value
    assert three._smith_representative(reduced_value) == reduced_value
