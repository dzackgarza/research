r"""Archive reconciliation for centers of free tensor algebras."""

from dzack_research.preamble.all import QQ, TensorAlgebraOn
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_tensor_algebra_on_two_generators_has_only_scalar_center() -> None:
    tensor = TensorAlgebraOn(QQ, finite_ordered_set(("x", "y")))
    x = tensor.algebra_generator("x")
    y = tensor.algebra_generator("y")

    assert x * y != y * x
    assert tensor.ring_center() is QQ
    inclusion = tensor.center_inclusion()
    assert inclusion.domain() is QQ
    assert inclusion.codomain() is tensor
    assert inclusion(QQ(3)) == 3 * tensor.one()
    assert tensor.is_central(inclusion(QQ(3)))
    assert not tensor.is_central(x)


def test_tensor_algebra_on_one_generator_is_its_own_center() -> None:
    tensor = TensorAlgebraOn(QQ, finite_ordered_set(("x",)))

    assert tensor.ring_center() is tensor
    inclusion = tensor.center_inclusion()
    assert inclusion.domain() is tensor
    assert inclusion.codomain() is tensor
    assert inclusion(tensor.algebra_generator("x")) == tensor.algebra_generator("x")
