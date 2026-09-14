r"""Archive reconciliation for polynomial rings and the four free-algebra comparisons."""

from dzack_research.preamble.all import QQ, ZZ, finite_ordered_set
from dzack_research.preamble.categories.algebras import (
    AlternatingAlgebraOf,
    DividedPowerAlgebraOf,
    SymmetricAlgebraOf,
    SymmetricAlgebraOn,
    TensorAlgebraOf,
    divided_to_symmetric,
    polynomial_ring,
    symmetric_to_divided,
    tensor_to_alternating,
    tensor_to_symmetric,
)
from dzack_research.preamble.categories.modules import BasedFreeModule

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/framed_free_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/free_algebras.py",
    "owner_overrides": {
        "polynomial_ring": "src/dzack_research/preamble/categories/algebras/framed_free_algebras.py",
        "TensorAlgebraOf": "src/dzack_research/preamble/categories/algebras/framed_free_algebras.py",
        "SymmetricAlgebraOf": "src/dzack_research/preamble/categories/algebras/framed_free_algebras.py",
        "AlternatingAlgebraOn": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
        "DividedPowerAlgebraOn": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
        "AlternatingAlgebraOf": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
        "DividedPowerAlgebraOf": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
        "tensor_to_symmetric": "src/dzack_research/preamble/categories/algebras/comparison_maps.py",
        "tensor_to_alternating": "src/dzack_research/preamble/categories/algebras/comparison_maps.py",
        "symmetric_to_divided": "src/dzack_research/preamble/categories/algebras/comparison_maps.py",
        "divided_to_symmetric": "src/dzack_research/preamble/categories/algebras/comparison_maps.py",
        "alternating_extension": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
        "divided_power_extension": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_polynomial_ring_is_the_owned_free_commutative_algebra_on_its_variables() -> None:
    labels = finite_ordered_set(("x", "y"))
    polynomial = polynomial_ring(ZZ, labels)
    symmetric = SymmetricAlgebraOn(ZZ, labels)

    assert polynomial is symmetric
    assert polynomial.algebra_generating_set() is symmetric.algebra_generating_set()
    assert polynomial.algebra_generator("x") == symmetric.algebra_generator("x")
    assert polynomial.algebra_generator("y") == symmetric.algebra_generator("y")


def test_archive_free_algebra_comparison_maps_are_the_canonical_generator_maps() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    tensor = TensorAlgebraOf(module)
    symmetric = SymmetricAlgebraOf(module)
    alternating = AlternatingAlgebraOf(module)
    divided = DividedPowerAlgebraOf(module)

    assert tensor.free_source_module() is module
    assert symmetric.free_source_module() is module
    assert alternating.free_source_module() is module
    assert divided.free_source_module() is module

    x_t = tensor.algebra_generator("x")
    y_t = tensor.algebra_generator("y")
    x_s = symmetric.algebra_generator("x")
    y_s = symmetric.algebra_generator("y")

    to_symmetric = tensor_to_symmetric(module)
    assert to_symmetric.domain() is tensor
    assert to_symmetric.codomain() is symmetric
    assert to_symmetric(x_t) == x_s
    assert to_symmetric(y_t) == y_s
    assert to_symmetric(x_t * y_t) == x_s * y_s
    assert to_symmetric(x_t * y_t - y_t * x_t) == symmetric.zero()

    to_alternating = tensor_to_alternating(module)
    assert to_alternating.domain() is tensor
    assert to_alternating.codomain() is alternating
    assert to_alternating(x_t * x_t) == alternating.zero()
    assert to_alternating(x_t * y_t + y_t * x_t) == alternating.zero()

    to_divided = symmetric_to_divided(module)
    assert to_divided.domain() is symmetric
    assert to_divided.codomain() is divided
    assert to_divided(x_s**3) == 6 * divided.divided_power(
        divided.algebra_generator("x"), 3
    )


def test_divided_to_symmetric_is_the_factorial_inverse_over_QQ() -> None:
    module = BasedFreeModule(QQ, finite_ordered_set(("x", "y")))
    symmetric = SymmetricAlgebraOf(module)
    divided = DividedPowerAlgebraOf(module)
    forward = symmetric_to_divided(module)
    backward = divided_to_symmetric(module)

    x = symmetric.algebra_generator("x")
    y = symmetric.algebra_generator("y")
    symmetric_probe = x**2 * y + 3 * y
    divided_probe = divided.divided_power(divided.algebra_generator("x"), 2)
    divided_probe *= divided.algebra_generator("y")

    assert backward(forward(symmetric_probe)) == symmetric_probe
    assert forward(backward(divided_probe)) == divided_probe
