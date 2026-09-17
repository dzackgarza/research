r"""Archive reconciliation for polynomial rings and the four free-algebra comparisons."""

from dzack_research.preamble.all import QQ, ZZ, finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/framed_free_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/free_algebras.py",
    "owner_overrides": {
        "OwnedRings.ParentMethods.polynomial_ring": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
        "TensorAlgebraOf": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "SymmetricAlgebraOf": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "AlternatingAlgebraOn": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "DividedPowerAlgebraOn": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "AlternatingAlgebraOf": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "DividedPowerAlgebraOf": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "tensor_to_symmetric": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "tensor_to_alternating": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "symmetric_to_divided": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "divided_to_symmetric": "src/dzack_research/preamble/categories/modules/pure/modules.py",
        "ModuleMorphism.alternating_extension": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
        "divided_power_extension": "src/dzack_research/preamble/categories/algebras/power_algebras.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_polynomial_ring_is_the_owned_free_commutative_algebra_on_its_variables() -> None:
    labels = finite_ordered_set(("x", "y"))
    polynomial = ZZ.polynomial_ring(labels)
    symmetric = ZZ.free_module(labels).symmetric_algebra()

    assert polynomial is symmetric
    assert polynomial.algebra_generating_set() is symmetric.algebra_generating_set()
    assert polynomial.algebra_generator("x") == symmetric.algebra_generator("x")
    assert polynomial.algebra_generator("y") == symmetric.algebra_generator("y")


def test_archive_free_algebra_comparison_maps_are_the_canonical_generator_maps() -> None:
    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    tensor = module.tensor_algebra()
    symmetric = module.symmetric_algebra()
    alternating = module.exterior_algebra()
    divided = module.divided_power_algebra()

    assert tensor.generating_module() is module
    assert symmetric.generating_module() is module
    assert alternating.generating_module() is module
    assert divided.generating_module() is module

    for algebra in (tensor, symmetric, alternating, divided):
        assert algebra.graded_piece(1) is module
        assert algebra.unformed_module() is not module
        full_module = algebra.unformed_module()
        unit = algebra.one()
        assert algebra(full_module(unit)) == unit

    x_t = tensor.algebra_generator("x")
    y_t = tensor.algebra_generator("y")
    x_s = symmetric.algebra_generator("x")
    y_s = symmetric.algebra_generator("y")

    to_symmetric = module.tensor_to_symmetric()
    assert to_symmetric.domain() is tensor
    assert to_symmetric.codomain() is symmetric
    assert to_symmetric(x_t) == x_s
    assert to_symmetric(y_t) == y_s
    assert to_symmetric(x_t * y_t) == x_s * y_s
    assert to_symmetric(x_t * y_t - y_t * x_t) == symmetric.zero()

    to_alternating = module.tensor_to_alternating()
    assert to_alternating.domain() is tensor
    assert to_alternating.codomain() is alternating
    assert to_alternating(x_t * x_t) == alternating.zero()
    assert to_alternating(x_t * y_t + y_t * x_t) == alternating.zero()

    to_divided = module.symmetric_to_divided()
    assert to_divided.domain() is symmetric
    assert to_divided.codomain() is divided
    assert to_divided(x_s**3) == 6 * divided.divided_power(
        divided.algebra_generator("x"), 3
    )

    gamma_two = divided.divided_power(divided.algebra_generator("x"), 2)
    assert gamma_two != divided.zero()
    assert divided.algebra_generator("x")**2 == 2 * gamma_two
    assert divided(gamma_two.parent().unformed_module()(gamma_two)) == gamma_two


def test_divided_to_symmetric_is_the_factorial_inverse_over_QQ() -> None:
    module = QQ.free_module(finite_ordered_set(("x", "y")))
    symmetric = module.symmetric_algebra()
    divided = module.divided_power_algebra()
    forward = module.symmetric_to_divided()
    backward = module.divided_to_symmetric()

    x = symmetric.algebra_generator("x")
    y = symmetric.algebra_generator("y")
    symmetric_probe = x**2 * y + 3 * y
    divided_probe = divided.divided_power(divided.algebra_generator("x"), 2)
    divided_probe *= divided.algebra_generator("y")

    assert backward(forward(symmetric_probe)) == symmetric_probe
    assert forward(backward(divided_probe)) == divided_probe
