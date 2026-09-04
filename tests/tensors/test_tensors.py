import pickle

import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    DualizationFunctor,
    FreeModule,
    FreeModuleOn,
    MatrixSpace,
    QuadraticField,
    Sets,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.tensors import Tensor, tensor


def test_vector_and_covector_are_distinct_owned_tensor_types() -> None:
    vector = tensor.vector(ZZ, [1, 2, 3])
    covector = tensor.covector(ZZ, [1, 2, 3])

    assert Tensor in vector.__class__.__mro__
    assert Tensor in covector.__class__.__mro__
    assert vector.base_ring() is ZZ is covector.base_ring()
    assert vector.tensor_valence() == (1, 0)
    assert covector.tensor_valence() == (0, 1)
    assert vector.parent() is not covector.parent()
    assert vector != covector


def test_tensor_constructors_require_owned_base_rings() -> None:
    with pytest.raises(TypeError, match="preamble ring"):
        tensor(SageZZ, (2,), (), [1, 2])
    with pytest.raises(TypeError, match="preamble ring"):
        tensor.vector(SageZZ, [1, 2])
    with pytest.raises(TypeError, match="preamble base ring"):
        tensor.matrix(SageZZ, [[1, 0], [0, 1]])


def test_vector_and_covector_constructors_accept_only_ring_and_components() -> None:
    assert tensor.vector(ZZ, [1, 2]).components() == [1, 2]
    assert tensor.covector(ZZ, [1, 2]).components() == [1, 2]
    with pytest.raises(TypeError, match="one component family"):
        tensor.vector(ZZ, 2, [1, 2])
    with pytest.raises(TypeError, match="one component family"):
        tensor.covector(ZZ, {0: 1}, sparse=True)


def test_matrix_tensor_is_component_data_not_a_module_morphism() -> None:
    components = tensor.matrix(ZZ, [[1, 2], [3, 4]])
    morphism = MatrixSpace(ZZ, 2, 2).from_rows([[1, 2], [3, 4]])

    assert components.tensor_valence() == (1, 1)
    assert components.tensor_shape() == (2, 2)
    assert morphism.parent() is not components.parent()
    assert tensor.from_matrix(morphism) == components


def test_a_matrix_hom_is_taken_between_framed_free_modules() -> None:
    r"""M_{m x n}(R) = Hom_R(F_R(S), F_R(T)) for chosen finite sets S and T.

    The free-module functor takes a *set*, not an integer: there is no
    canonical set of cardinality n, so "R^n" names no particular object.  What
    MatrixSpace(R, m, n) does is choose one -- the standard finite ordinal
    Delta[n-1] = {0, ..., n-1} -- and route it through the same constructor
    FreeModuleOn uses.  The integer is sugar for that choice, and the choice is
    what the matrix entries are indexed by.

    So a free module on a different set of the same cardinality is isomorphic
    to F_R(Delta[n-1]) and is not equal to it, and its Hom is a different
    object.  That is why FreshFreeModuleOn does not intern its parents.
    """
    with pytest.raises(TypeError):
        tensor.matrix(ZZ, row_keys=("a", "b"), entries=[1, 2])

    components = tensor.matrix(ZZ, [[1, 2], [3, 4]])
    maps = MatrixSpace(ZZ, 2, 2)
    f = maps.from_tensor(components)

    # The integer arity resolves to the free module on a named set.
    assert Sets.Δ[1].cardinality() == 2
    assert FreeModule(ZZ, 2) is FreeModuleOn(ZZ, Sets.Δ[1])

    assert f.parent() is maps
    assert f.domain() is FreeModuleOn(ZZ, Sets.Δ[1])
    assert f.codomain() is FreeModuleOn(ZZ, Sets.Δ[1])
    assert maps.identity() * f == f
    assert f * maps.identity() == f
    assert tensor.from_matrix(f) == components

    # Another 2-element set gives an isomorphic module that is not this one.
    other = FreeModuleOn(ZZ, finite_ordered_set(("a", "b")))
    assert other.module_generating_set().cardinality() == Sets.Δ[1].cardinality()
    assert other is not FreeModuleOn(ZZ, Sets.Δ[1])
    assert other.Hom(other) is not maps


def test_matrix_tensor_accepts_rectangular_component_data_or_explicit_shape() -> None:
    rows = tensor.matrix(ZZ, [[1, 2, 3], [4, 5, 6]])
    flat = tensor.matrix(ZZ, 2, 3, [1, 2, 3, 4, 5, 6])
    zero = tensor.matrix(QQ, 2, 3)

    assert rows == flat
    assert rows.tensor_shape() == (2, 3)
    assert zero.components() == [[0, 0, 0], [0, 0, 0]]


def test_general_tensor_constructor_encodes_variance_and_higher_rank() -> None:
    upper = tensor(ZZ, (2, 3), (), range(6))
    lower = tensor(ZZ, (), (2, 3), range(6))
    higher = tensor(
        ZZ,
        (2, 2),
        (2,),
        [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    )

    assert upper.tensor_valence() == (2, 0)
    assert lower.tensor_valence() == (0, 2)
    assert upper.parent() is not lower.parent()
    assert higher.tensor_shape() == (2, 2, 2)
    assert higher.tensor_order() == 3
    assert higher[1, 0, 1] == ZZ(6)


def test_main_tensor_constructor_does_not_infer_variance() -> None:
    with pytest.raises(TypeError):
        tensor(ZZ, [1, 2, 3])


def test_ragged_component_arrays_are_rejected() -> None:
    with pytest.raises(ValueError, match="ragged"):
        tensor(ZZ, (), (2, 2), [[1, 2], [3]])


def test_tensor_modules_have_componentwise_additive_and_scalar_structure() -> None:
    left = tensor(ZZ, (2, 2), (2,), [[[1, 0], [0, 0]], [[0, 0], [0, 0]]])
    right = tensor(ZZ, (2, 2), (2,), [[[0, 0], [0, 0]], [[0, 0], [0, 1]]])
    total = left + right

    assert total[0, 0, 0] == ZZ.one()
    assert total[1, 1, 1] == ZZ.one()
    assert (ZZ(3) * left)[0, 0, 0] == ZZ(3)
    assert total.parent() is left.parent() is right.parent()
    assert left.parent().zero() + left == left


def test_addition_requires_one_variance_space() -> None:
    vector = tensor.vector(ZZ, [1, 2])
    covector = tensor.covector(ZZ, [1, 2])
    upper_two = tensor(ZZ, (2, 2), (), range(4))
    lower_two = tensor(ZZ, (), (2, 2), range(4))

    for left, right in ((vector, covector), (upper_two, lower_two)):
        with pytest.raises((TypeError, ArithmeticError)):
            left + right


def test_two_vectors_do_not_contract_without_a_pairing() -> None:
    with pytest.raises(TypeError):
        tensor.vector(ZZ, [1, 2]) * tensor.vector(ZZ, [3, 4])


def test_covector_vector_product_is_the_natural_pairing() -> None:
    covector = tensor.covector(ZZ, [2, -1, 4])
    vector = tensor.vector(ZZ, [5, 6, 7])

    assert covector * vector == ZZ(32)
    assert covector(vector) == ZZ(32)


def test_bilinear_form_lowers_an_index() -> None:
    form = tensor(ZZ, (), (2, 2), [[2, 1], [1, 3]])
    vector = tensor.vector(ZZ, [4, 5])
    covector = form * vector

    assert covector.tensor_valence() == (0, 1)
    assert covector.components() == [13, 19]
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

    assert contracted.components() == [[11, 14], [18, 22]]
    assert image.components() == [25, 35]
    assert contracted.tensor_valence() == (1, 1)
    assert image.tensor_valence() == (1, 0)


def test_covector_type_one_one_adjacent_contraction() -> None:
    covector = tensor.covector(ZZ, [2, -1])
    linear_components = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])

    contracted = covector * linear_components
    assert contracted.tensor_valence() == (0, 1)
    assert contracted.components() == [-2, -1, 0]


def test_type_one_one_dualization_belongs_to_module_duality() -> None:
    linear_components = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])
    linear_map = MatrixSpace(ZZ, 2, 3).from_tensor(linear_components)
    dual = tensor.from_morphism(DualizationFunctor(ZZ)(linear_map))

    assert dual.tensor_valence() == (1, 1)
    assert dual.tensor_shape() == (3, 2)
    assert dual.components() == [[1, 4], [2, 5], [3, 6]]
    with pytest.raises(TypeError, match="pairings/copairings"):
        linear_components.dual_tensor()


def test_dual_tensor_preserves_pairing_variance_information() -> None:
    bilinear = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    bilinear_dual = bilinear.dual_tensor()
    assert bilinear_dual.tensor_valence() == (2, 0)
    assert bilinear_dual.components() == [[1, -1], [-1, 2]]


def test_matrix_inverse_belongs_to_the_linear_map_parent_not_tensor_data() -> None:
    linear_components = tensor(QQ, (2,), (2,), [[2, 1], [1, 1]])
    matrix = MatrixSpace(QQ, 2).from_tensor(linear_components)
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

    assert vector.tensor_valence() == (1, 0)
    assert vector.components() == [-2, 7]
    assert pairing * vector == covector


def test_tensor_pullback_requires_an_actual_linear_morphism() -> None:
    form = tensor(ZZ, (), (2, 2), [[2, 1], [1, 3]])
    change = MatrixSpace(ZZ, 2, 2).from_rows([[1, 1], [0, 1]])
    pulled = form.pullback(change)

    assert pulled.components() == [[2, 3], [3, 7]]
    with pytest.raises(TypeError, match="owned linear morphism"):
        form.pullback(tensor.from_matrix(change))


def test_matrix_space_is_the_actual_linear_map_parent() -> None:
    hom = MatrixSpace(ZZ, 2, 3)
    morphism = hom.from_rows([[1, 0, 2], [0, 1, 3]])
    vector = tensor.vector(ZZ, [1, 1, 1])

    assert morphism.parent() is hom
    assert tensor.from_matrix(morphism).tensor_shape() == (2, 3)
    assert (tensor.from_matrix(morphism) * vector).components() == [3, 4]


def test_tensor_operations_remain_owned_over_a_finite_field() -> None:
    field = GF(5)
    value = tensor.vector(field, [1, 2])

    assert value.base_ring() is field
    assert (value + value).base_ring() is field
    assert (field(3) * value).base_ring() is field


def test_tensor_vector_accepts_an_owned_number_field() -> None:
    field = QuadraticField(2, "a")
    value = tensor.vector(field, [1, 0])

    assert value.base_ring() is field
    assert value.tensor_valence() == (1, 0)
    assert value.components() == [field.one(), field.zero()]


def test_tensor_identity_survives_pickling() -> None:
    values = (
        tensor.vector(ZZ, [1, 2]),
        tensor.covector(ZZ, [1, 2]),
        tensor.matrix(ZZ, [[1, 2], [3, 4]]),
        tensor(ZZ, (2, 2), (2,), range(8)),
    )

    for value in values:
        restored = pickle.loads(pickle.dumps(value))
        assert Tensor in restored.__class__.__mro__
        assert restored == value


def test_tensor_space_records_index_modules() -> None:
    covector = tensor.covector(ZZ, [1, 2, 3])
    gram = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
    mixed = tensor(ZZ, (2, 3), (), range(6))

    assert covector.tensor_type() == (0, 1)
    assert covector.tensor_space() is covector.parent()
    assert gram.tensor_type() == (0, 2)
    assert mixed.tensor_type() == (2, 0)
    upper, lower = gram.index_modules()
    assert not upper and lower.cardinality() == 2
    assert int(lower[0].rank()) == 2


def test_tensor_matrix_can_reinterpret_two_index_tensor_components_only() -> None:
    covector = tensor.covector(ZZ, [1, 2, 3])
    two_index = tensor(ZZ, (), (2, 2), [[1, 2], [3, 4]])
    higher = tensor(ZZ, (2, 2), (2,), range(8))

    assert tensor.matrix(ZZ, two_index).components() == [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="two indices"):
        tensor.matrix(ZZ, covector)
    with pytest.raises(TypeError, match="two indices"):
        tensor.matrix(ZZ, higher)
