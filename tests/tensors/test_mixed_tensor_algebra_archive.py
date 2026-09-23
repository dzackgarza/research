r"""Archive reconciliation for the mixed tensor algebra."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.tensors import tensor




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


