
import pytest

from dzack_research.preamble.all import (
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.sets import NN
from dzack_research.preamble.tensors import tensor


























def test_covector_vector_product_is_the_natural_pairing() -> None:
    covector = tensor.covector(ZZ, [2, -1, 4])
    vector = tensor.vector(ZZ, [5, 6, 7])

    assert covector * vector == ZZ(32)
    assert covector(vector) == ZZ(32)


def test_bilinear_form_lowers_an_index() -> None:
    form = tensor(ZZ, (), (2, 2), [[2, 1], [1, 3]])
    vector = tensor.vector(ZZ, [4, 5])
    covector = form * vector

    assert covector.tensor_valence() == (NN**2)((0, 1))
    assert covector == tensor.covector(ZZ, [13, 19])
    assert covector(vector) == ZZ(147)
    with pytest.raises(TypeError):
        vector * form
    with pytest.raises(TypeError):
        form * tensor.covector(ZZ, [4, 5])


def test_type_one_one_tensor_adjacent_contraction_and_vector_contraction() -> None:
    left = tensor(ZZ, (2,), (3,), [[1, 0, 2], [0, 1, 3]])
    right = tensor(ZZ, (3,), (2,), [[1, 2], [3, 4], [5, 6]])
    vector = tensor.vector(ZZ, [7, 8, 9])

    contracted = left * right
    image = left * vector

    assert contracted == tensor(ZZ, (2,), (2,), [[11, 14], [18, 22]])
    assert image == tensor.vector(ZZ, [25, 35])
    assert contracted.tensor_valence() == (NN**2)((1, 1))
    assert image.tensor_valence() == (NN**2)((1, 0))


def test_covector_type_one_one_adjacent_contraction() -> None:
    covector = tensor.covector(ZZ, [2, -1])
    linear_components = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])

    contracted = covector * linear_components
    assert contracted.tensor_valence() == (NN**2)((0, 1))
    assert contracted == tensor.covector(ZZ, [-2, -1, 0])


def test_type_one_one_dualization_belongs_to_module_duality() -> None:
    linear_components = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])
    linear_map = ZZ.matrix_space(2, 3).from_tensor(linear_components)
    dualization = linear_map.domain().module_category().dualization()
    opposite = dualization.domain()
    opposite_map = opposite.Mor(
        opposite(linear_map.codomain()),
        opposite(linear_map.domain()),
    )(linear_map)
    dual = tensor.from_morphism(dualization(opposite_map))

    assert dual.tensor_valence() == (NN**2)((1, 1))
    _shape = dual.tensor_shape()
    assert _shape.cardinality() == 2
    assert _shape[0] == 3
    assert _shape[1] == 2
    assert dual == tensor(ZZ, (3,), (2,), [[1, 4], [2, 5], [3, 6]])
    with pytest.raises(TypeError, match="pairings/copairings"):
        linear_components.dual_tensor()


def test_dual_tensor_preserves_pairing_variance_information() -> None:
    bilinear = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    bilinear_dual = bilinear.dual_tensor()
    assert bilinear_dual.tensor_valence() == (NN**2)((2, 0))
    assert bilinear_dual == tensor(QQ, (2, 2), (), [[1, -1], [-1, 2]])


def test_matrix_inverse_belongs_to_the_linear_map_parent_not_tensor_data() -> None:
    linear_components = tensor(QQ, (2,), (2,), [[2, 1], [1, 1]])
    matrix = QQ.matrix_space(2).from_tensor(linear_components)
    inverse = matrix.inverse()

    assert inverse * matrix == matrix.parent().identity()
    assert matrix * inverse == matrix.parent().identity()
    assert matrix.determinant() == QQ(1)
    assert tensor.from_matrix(inverse) == tensor(QQ, (2,), (2,), [[1, -1], [-1, 2]])


def test_dual_pairing_raises_an_index() -> None:
    pairing = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    dual = pairing.dual_tensor()
    covector = tensor.covector(QQ, [3, 5])
    vector = dual * covector

    assert vector.tensor_valence() == (NN**2)((1, 0))
    assert vector == tensor.vector(QQ, [-2, 7])
    assert pairing * vector == covector


def test_tensor_pullback_requires_an_actual_linear_morphism() -> None:
    form = tensor(ZZ, (), (2, 2), [[2, 1], [1, 3]])
    change = ZZ.matrix_space(2, 2).from_rows([[1, 1], [0, 1]])
    pulled = form.pullback(change)

    assert pulled == tensor(ZZ, (), (2, 2), [[2, 3], [3, 7]])
    with pytest.raises(TypeError, match="owned linear morphism"):
        form.pullback(tensor.from_matrix(change))












