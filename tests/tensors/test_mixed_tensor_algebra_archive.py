r"""Archive reconciliation for the mixed tensor algebra."""

from dzack_research.preamble.all import QQ, Algebras, GradedModules
from dzack_research.preamble.tensors import tensor


def test_mixed_tensor_algebra_retains_distinct_vector_and_covector_bidegrees() -> None:
    module = QQ.free_module(2)
    algebra = module.mixed_tensor_algebra()
    vector = tensor.vector(QQ, [1, 2])
    covector = tensor.covector(QQ, [3, 4])

    assert algebra in Algebras(QQ).Associative().Unital()
    assert algebra.unformed_module() in GradedModules(QQ, algebra.grading_monoid())
    assert algebra.unformed_module().graded_piece((1, 0)) is algebra.graded_piece((1, 0))
    vector_term = algebra.include(vector)
    covector_term = algebra.include(covector)
    mixed = vector_term + covector_term

    assert algebra.module() is module
    assert mixed.valences().cardinality() == 2
    assert mixed.homogeneous_component((1, 0)) == vector
    assert mixed.homogeneous_component((0, 1)) == covector


def test_mixed_tensor_product_adds_bidegrees_and_uses_live_outer_tensor_product() -> None:
    module = QQ.free_module(2)
    algebra = module.mixed_tensor_algebra()
    vector = tensor.vector(QQ, [1, 2])
    covector = tensor.covector(QQ, [3, 4])

    product = algebra.include(vector) * algebra.include(covector)
    expected = vector.tensor_product(covector)

    assert product.valences().cardinality() == 1
    assert product.homogeneous_component((1, 1)) == expected
    assert algebra.one() * product == product
    assert product * algebra.one() == product


def test_nonhomogeneous_products_collect_equal_bidegrees() -> None:
    module = QQ.free_module(2)
    algebra = module.mixed_tensor_algebra()
    first = algebra.include(tensor.vector(QQ, [1, 0]))
    second = algebra.include(tensor.vector(QQ, [0, 1]))
    covector = algebra.include(tensor.covector(QQ, [1, 1]))

    product = (first + second) * covector
    expected = (
        tensor.vector(QQ, [1, 0]).tensor_product(tensor.covector(QQ, [1, 1]))
        + tensor.vector(QQ, [0, 1]).tensor_product(tensor.covector(QQ, [1, 1]))
    )

    assert product.homogeneous_component((1, 1)) == expected


def test_mixed_tensor_algebra_exposes_the_two_tensor_algebra_factors() -> None:
    module = QQ.free_module(2)
    algebra = module.mixed_tensor_algebra()
    dual = algebra.dual_module()

    assert dual is module.dual_module()
    assert algebra.vector_tensor_algebra().generating_module() is module
    assert algebra.covector_tensor_algebra().generating_module() is dual
    assert algebra.vector_tensor_algebra().graded_piece(2).module_rank() == 4
    assert algebra.covector_tensor_algebra().graded_piece(2).module_rank() == 4
