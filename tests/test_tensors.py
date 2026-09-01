import pickle

from sage.all import FreeAlgebra, GF, MatrixSpace, QQ, ZZ, matrix, vector

from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.tensors import Tensor, tensor
from dzack_research.static_types import (
    apply as static_apply,
    bilinear_form_view,
    lower_index as static_lower_index,
    pair as static_pair,
    vector_view,
)


def test_one_index_tensor_is_owned_and_is_not_a_sage_vector() -> None:
    native = vector(ZZ, [1, 2, 3])
    value = tensor(ZZ, (3,), (), [1, 2, 3])

    assert Tensor in value.__class__.__mro__
    assert native.__class__ not in value.__class__.__mro__
    assert value.parent() is not native.parent()
    assert value.list() == native.list()
    assert value.tensor_shape() == (3,)
    assert value.upper_ranks() == (3,)
    assert value.lower_ranks() == ()


def test_covector_is_not_identified_with_a_vector() -> None:
    covector = tensor(ZZ, (), (3,), [1, 2, 3])
    vector_class = vector(ZZ, [1, 2, 3]).__class__

    assert Tensor in covector.__class__.__mro__
    assert vector_class not in covector.__class__.__mro__
    assert covector.upper_ranks() == ()
    assert covector.lower_ranks() == (3,)
    assert covector.tensor_valence() == (0, 1)


def test_static_tensor_views_are_identity_views_of_live_tensor_objects() -> None:
    value = tensor.vector(QQ, [2, 3])
    identity = tensor.matrix(QQ, [[1, 0], [0, 1]])
    gram = tensor(QQ, (), (2, 2), [[2, 1], [1, 2]])

    viewed_value = vector_view(value)
    viewed_gram = bilinear_form_view(gram)

    assert viewed_value is value
    assert viewed_gram is gram
    assert static_apply(identity, viewed_value) == value
    covector = static_lower_index(viewed_gram, viewed_value)
    assert static_pair(covector, viewed_value) == gram(value, value)


def test_two_index_tensor_is_owned_and_is_not_a_sage_matrix() -> None:
    native = matrix(ZZ, [[1, 2, 3], [4, 5, 6]])
    value = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])

    assert Tensor in value.__class__.__mro__
    assert native.__class__ not in value.__class__.__mro__
    assert value.parent() is not native.parent()
    assert value.list() == native.list()
    assert value.tensor_shape() == (2, 3)
    assert value.upper_ranks() == (2,)
    assert value.lower_ranks() == (3,)


def test_integer_rank_shorthand_builds_the_linear_map_tensor() -> None:
    native = matrix(ZZ, 2, 2, [1, 2, 3, 4])
    value = tensor(ZZ, 2, 2, [1, 2, 3, 4])

    assert value.tensor_valence() == (1, 1)
    assert value.list() == native.list()
    assert Tensor in value.__class__.__mro__


def test_two_index_variance_controls_whether_the_tensor_is_a_matrix() -> None:
    upper = tensor(ZZ, (2, 3), (), range(6))
    lower = tensor(ZZ, (), (2, 3), range(6))
    matrix_class = matrix(ZZ, 2, 3).__class__

    assert matrix_class not in upper.__class__.__mro__
    assert matrix_class not in lower.__class__.__mro__
    assert upper.tensor_valence() == (2, 0)
    assert lower.tensor_valence() == (0, 2)
    assert upper.upper_ranks() == (2, 3) and upper.lower_ranks() == ()
    assert lower.upper_ranks() == () and lower.lower_ranks() == (2, 3)


def test_tensor_matrix_accepts_the_matrix_constructor_family() -> None:
    calls = (
        ((2,), {}),
        ((2, 3), {}),
        ((QQ, 2, [1, 2, 3, 4, 5, 6]), {}),
        ((ZZ, 2, 2, [1, 2, 3, 4]), {}),
        ((ZZ, 2, 3, lambda i, j: i + j), {}),
        ((ZZ, {(0, 0): 1, (1, 1): 2}), {}),
        ((ZZ, 2, 2, {(0, 0): 1}), {"sparse": True}),
        ((), {"base_ring": ZZ, "nrows": 2, "ncols": 2, "entries": [1, 2, 3, 4]}),
        ((), {"space": MatrixSpace(ZZ, 2, 2), "entries": [1, 2, 3, 4]}),
    )

    for args, kwds in calls:
        native = matrix(*args, **kwds)
        value = tensor.matrix(*args, **kwds)
        assert Tensor in value.__class__.__mro__
        assert value.tensor_valence() == (1, 1)
        assert value.tensor_shape() == (native.nrows(), native.ncols())
        assert value.list() == native.list()


def test_matrix_constructor_homomorphism_results_become_owned_tensors_too() -> None:
    value = tensor.matrix(
        ZZ,
        row_keys=("a", "b"),
        column_keys=("x", "y"),
        entries=[1, 2, 3, 4],
    )

    assert Tensor in value.__class__.__mro__
    assert value.tensor_valence() == (1, 1)
    assert value.tensor_shape() == (2, 2)
    assert value.components() == [[1, 2], [3, 4]]


def test_tensor_vector_accepts_the_vector_constructor_family() -> None:
    calls = (
        (([1, 2, 3],), {}),
        ((ZZ, [1, 2, 3]), {}),
        (([1, 2, 3], QQ), {}),
        ((QQ, 3, [1, 2, 3]), {}),
        ((ZZ, 3), {}),
        ((ZZ, {0: 1, 2: 3}), {"sparse": True}),
    )

    for args, kwds in calls:
        native = vector(*args, **kwds)
        value = tensor.vector(*args, **kwds)
        assert Tensor in value.__class__.__mro__
        assert value.tensor_valence() == (1, 0)
        assert value.upper_ranks() == (native.degree(),)
        assert value.list() == native.list()


def test_named_matrix_constructors_are_available_under_tensor_matrix() -> None:
    identity = tensor.matrix.identity(ZZ, 3)
    diagonal = tensor.matrix.diagonal(ZZ, [1, 2, 3])
    zero = tensor.matrix.zero(QQ, 2, 3)

    assert identity.list() == matrix.identity(ZZ, 3).list()
    assert diagonal.list() == matrix.diagonal(ZZ, [1, 2, 3]).list()
    assert zero.list() == matrix.zero(QQ, 2, 3).list()
    assert all(value.tensor_valence() == (1, 1) for value in (identity, diagonal, zero))
    assert all(Tensor in value.__class__.__mro__ for value in (identity, diagonal, zero))
    assert tensor.matrix.options is matrix.options

    constructor_names = {
        name
        for name in dir(matrix)
        if not name.startswith("_")
        and name
        not in {
            "options",
            "func_closure",
            "func_code",
            "func_defaults",
            "func_dict",
            "func_doc",
            "func_globals",
            "func_name",
        }
    }
    assert constructor_names <= set(dir(tensor.matrix))


def test_block_constructor_returns_the_assembled_linear_map_tensor() -> None:
    blocked = tensor.matrix.block(
        [
            [matrix.identity(ZZ, 1), matrix.zero(ZZ, 1)],
            [matrix.zero(ZZ, 1), matrix.identity(ZZ, 1)],
        ]
    )

    assert Tensor in blocked.__class__.__mro__
    assert blocked.tensor_valence() == (1, 1)
    assert blocked.components() == [[1, 0], [0, 1]]


def test_three_index_tensor_is_not_a_vector_or_matrix_extension() -> None:
    value = tensor(ZZ, (2, 2), (2,), [[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    vector_class = vector(ZZ, [1, 2]).__class__
    matrix_class = matrix(ZZ, [[1, 2], [3, 4]]).__class__

    assert Tensor in value.__class__.__mro__
    assert vector_class not in value.__class__.__mro__
    assert matrix_class not in value.__class__.__mro__
    assert value.tensor_shape() == (2, 2, 2)
    assert value.tensor_order() == 3
    assert value.upper_ranks() == (2, 2)
    assert value.lower_ranks() == (2,)
    assert value[1, 0, 1] == 6
    assert value.components() == [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def test_explicit_higher_tensor_dimensions_generalize_vector_and_matrix_dimensions() -> None:
    value = tensor(ZZ, (2, 2), (2,), range(8))

    assert value.tensor_shape() == (2, 2, 2)
    assert value.components() == [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]


def test_main_tensor_constructor_does_not_infer_variance_from_component_nesting() -> None:
    try:
        tensor(ZZ, [1, 2, 3])
    except TypeError:
        pass
    else:
        raise AssertionError("one index cannot determine vector versus covector")


def test_higher_tensors_are_module_elements_with_componentwise_linear_structure() -> None:
    left = tensor(ZZ, (2, 2), (2,), [[[1, 0], [0, 0]], [[0, 0], [0, 0]]])
    right = tensor(ZZ, (2, 2), (2,), [[[0, 0], [0, 0]], [[0, 0], [0, 1]]])

    total = left + right
    assert total[0, 0, 0] == 1
    assert total[1, 1, 1] == 1
    assert (3 * left)[0, 0, 0] == 3
    assert total.parent() is left.parent() is right.parent()
    assert total == tensor(
        ZZ,
        (2, 2),
        (2,),
        [[[1, 0], [0, 0]], [[0, 0], [0, 1]]],
    )
    assert left.parent().zero() + left == left


def test_addition_requires_the_same_variance_and_rank_vector() -> None:
    vector_value = tensor(ZZ, (2,), (), [1, 2])
    covector = tensor(ZZ, (), (2,), [1, 2])
    upper_two = tensor(ZZ, (2, 2), (), range(4))
    lower_two = tensor(ZZ, (), (2, 2), range(4))

    for left, right in ((vector_value, covector), (upper_two, lower_two)):
        try:
            left + right
        except (TypeError, ArithmeticError):
            pass
        else:
            raise AssertionError("tensors in different variance spaces must not add")


def test_tensor_multiplication_does_not_use_the_vectors_coordinate_dot_product() -> None:
    left = tensor(ZZ, (2,), (), [1, 2])
    right = tensor(ZZ, (2,), (), [3, 4])

    try:
        left * right
    except TypeError:
        pass
    else:
        raise AssertionError("two vectors cannot contract without a pairing")


def test_covector_vector_product_is_the_natural_pairing() -> None:
    covector = tensor(ZZ, (), (3,), [2, -1, 4])
    vector_value = tensor(ZZ, (3,), (), [5, 6, 7])

    assert covector * vector_value == 2 * 5 - 6 + 4 * 7
    assert covector(vector_value) == covector * vector_value


def test_bilinear_form_times_vector_is_a_covector_not_a_vector() -> None:
    gram = tensor(ZZ, (), (2, 2), [[2, 1], [1, 3]])
    vector_value = tensor(ZZ, (2,), (), [4, 5])
    covector = gram * vector_value

    assert covector.tensor_valence() == (0, 1)
    assert covector.components() == [13, 19]
    assert covector(vector_value) == 4 * 13 + 5 * 19

    for invalid in (
        lambda: vector_value * gram,
        lambda: gram * tensor(ZZ, (), (2,), [4, 5]),
    ):
        try:
            invalid()
        except TypeError:
            pass
        else:
            raise AssertionError("tensor variance must forbid row/column ambiguity")


def test_covector_times_matrix_is_left_composition() -> None:
    covector = tensor(ZZ, (), (2,), [2, -1])
    linear_map = tensor(ZZ, (2,), (3,), [1, 2, 3, 4, 5, 6])

    composite = covector * linear_map

    assert composite.upper_ranks() == ()
    assert composite.lower_ranks() == (3,)
    assert composite.components() == [-2, -1, 0]


def test_matrix_tensor_multiplication_is_composition_and_action() -> None:
    left = tensor(ZZ, (2,), (3,), [1, 0, 2, 0, 1, 3])
    right = tensor(ZZ, (3,), (2,), [1, 2, 3, 4, 5, 6])
    vector_value = tensor(ZZ, (3,), (), [7, 8, 9])

    composite = left * right
    image = left * vector_value

    assert Tensor in composite.__class__.__mro__
    assert composite.upper_ranks() == (2,)
    assert composite.lower_ranks() == (2,)
    assert composite.list() == (
        matrix(ZZ, 2, 3, left.list()) * matrix(ZZ, 3, 2, right.list())
    ).list()
    assert Tensor in image.__class__.__mro__
    assert image.upper_ranks() == (2,) and image.lower_ranks() == ()
    assert image.list() == (matrix(ZZ, 2, 3, left.list()) * vector(ZZ, [7, 8, 9])).list()


def test_matrix_tensor_transpose_remains_a_typed_linear_map() -> None:
    linear_map = tensor(ZZ, (2,), (3,), [1, 2, 3, 4, 5, 6])
    transposed = linear_map.transpose()

    assert Tensor in transposed.__class__.__mro__
    assert transposed.tensor_valence() == (1, 1)
    assert transposed.tensor_shape() == (3, 2)
    assert transposed.list() == matrix(ZZ, 2, 3, linear_map.list()).transpose().list()


def test_dual_tensor_is_the_variance_correct_transpose_of_a_linear_map() -> None:
    linear_map = tensor(ZZ, (2,), (3,), [[1, 2, 3], [4, 5, 6]])
    dual = linear_map.dual_tensor()

    assert dual.tensor_valence() == (1, 1)
    assert dual.tensor_shape() == (3, 2)
    assert dual.components() == [[1, 4], [2, 5], [3, 6]]

    bilinear = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    bilinear_dual = bilinear.dual_tensor()
    assert bilinear_dual.tensor_valence() == (2, 0)
    assert bilinear_dual.components() == [[1, -1], [-1, 2]]


def test_inverse_tensor_is_only_for_an_invertible_linear_map() -> None:
    pairing = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    try:
        pairing.inverse_tensor()
    except TypeError:
        pass
    else:
        raise AssertionError("a pairing has a dual tensor, not an inverse tensor")

    linear_map = tensor(QQ, (2,), (2,), [[2, 1], [1, 1]])
    inverse_map = linear_map.inverse_tensor()
    assert inverse_map.tensor_valence() == (1, 1)
    assert inverse_map * linear_map == tensor.matrix.identity(QQ, 2)


def test_dual_pairing_contracts_a_covector_to_a_vector() -> None:
    pairing = tensor(QQ, (), (2, 2), [[2, 1], [1, 1]])
    dual = pairing.dual_tensor()
    covector = tensor(QQ, (), (2,), [3, 5])
    vector_value = dual * covector

    assert dual.tensor_valence() == (2, 0)
    assert vector_value.tensor_valence() == (1, 0)
    assert list(vector_value) == [-2, 7]
    assert pairing * vector_value == covector


def test_multiplication_does_not_treat_vectors_as_row_covectors() -> None:
    vector_value = tensor(ZZ, (2,), (), [1, 2])
    covector = tensor(ZZ, (), (2,), [3, 4])
    linear_map = tensor(ZZ, (2,), (2,), [1, 2, 3, 4])

    for product in (
        lambda: vector_value * linear_map,
        lambda: linear_map * covector,
        lambda: vector_value * covector,
    ):
        try:
            product()
        except TypeError:
            pass
        else:
            raise AssertionError("multiplication must respect upper/lower variance")


def test_linear_operations_preserve_tensor_identity_in_native_specializations() -> None:
    vector_tensor = tensor(GF(5), (2,), (), [1, 2])
    matrix_tensor = tensor(ZZ, (2,), (2,), [[1, 2], [3, 4]])
    covector = tensor(ZZ, (), (2,), [1, 2])

    assert Tensor in (vector_tensor + vector_tensor).__class__.__mro__
    assert Tensor in (3 * vector_tensor).__class__.__mro__
    assert Tensor in (matrix_tensor + matrix_tensor).__class__.__mro__
    assert Tensor in (3 * matrix_tensor).__class__.__mro__
    assert Tensor in (3 * covector).__class__.__mro__


def test_left_and_right_scalar_multiplication_remain_distinct_over_a_noncommutative_ring() -> None:
    ring = FreeAlgebra(QQ, 2, names=("x", "y"))
    x, y = ring.gens()
    vector_tensor = tensor(ring, (2,), (), [x, y])
    covector = tensor(ring, (), (2,), [x, y])
    matrix_tensor = tensor(ring, (1,), (1,), [y])

    assert (x * vector_tensor)[1] == x * y
    assert (vector_tensor * x)[1] == y * x
    assert (x * covector)[1] == x * y
    assert (covector * x)[1] == y * x
    assert (x * matrix_tensor)[0, 0] == x * y
    assert (matrix_tensor * x)[0, 0] == y * x


def test_tensor_identity_survives_pickling() -> None:
    values = (
        tensor(ZZ, (2,), (), [1, 2]),
        tensor(ZZ, (), (2,), [1, 2]),
        tensor(ZZ, (2,), (2,), [[1, 2], [3, 4]]),
        tensor(ZZ, (2, 2), (2,), [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    )

    for value in values:
        restored = pickle.loads(pickle.dumps(value))
        assert Tensor in restored.__class__.__mro__
        assert restored == value


def test_tensor_vector_accepts_an_owned_number_field() -> None:
    from dzack_research.preamble.all import QuadraticField

    field = QuadraticField(2, "a")
    value = tensor.vector(field, [1, 0])

    assert Tensor in value.__class__.__mro__
    assert value.tensor_valence() == (1, 0)
    assert list(value) == [1, 0]


def test_ragged_component_arrays_are_rejected() -> None:
    try:
        tensor(ZZ, (), (2, 2), [[1, 2], [3]])
    except ValueError as error:
        assert "ragged" in str(error)
    else:
        raise AssertionError("ragged tensor components must be rejected")


def test_tensor_space_is_the_module_the_tensor_belongs_to() -> None:
    covector = tensor(ZZ, (), (3,), [1, 2, 3])
    gram = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
    mixed = tensor(ZZ, (2, 3), (), range(6))

    assert covector.tensor_type() == (0, 1)
    assert repr(covector.parent()) == "(ZZ^3)*"
    assert covector.tensor_space() is covector.parent()
    assert repr(gram.parent()) == "((ZZ^2)*)^{⊗2}"
    assert gram.tensor_type() == (0, 2)
    assert repr(mixed.parent()) == "ZZ^2 ⊗ ZZ^3"
    upper, lower = gram.index_modules()
    assert not upper
    assert len(lower) == 2
    assert lower[0].rank() == 2
    indices_upper, indices_lower = gram.tensor_indices()
    assert not indices_upper
    assert tuple(indices_lower[0]) == (0, 1)


def test_identity_pairing_names_the_hom_module_at_infinite_rank() -> None:
    from sage.rings.infinity import Infinity
    from sage.rings.semirings.non_negative_integer_semiring import NN
    from dzack_research.preamble.categories.lattices import Lattices

    finite = Lattices(ZZ)(ZZ**2).gram_tensor()
    infinite = Lattices(ZZ)(ZZ**NN).gram_tensor()

    assert finite.tensor_type() == (0, 2)
    assert repr(finite) == "I_2 ∈ ((ZZ^2)*)^{⊗2}"
    assert repr(infinite) == "I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*"
    assert infinite.tensor_shape() == (Infinity, Infinity)
    upper, lower = infinite.tensor_indices()
    assert not upper
    assert lower[0].cardinality() == Infinity


def test_tensor_covector_accepts_the_vector_constructor_family() -> None:
    calls = (
        (([1, 2, 3],), {}),
        ((ZZ, [1, 2, 3]), {}),
        (([1, 2, 3], QQ), {}),
        ((QQ, 3, [1, 2, 3]), {}),
        ((ZZ, 3), {}),
        ((ZZ, {0: 1, 2: 3}), {"sparse": True}),
    )

    for args, kwds in calls:
        native = vector(*args, **kwds)
        value = tensor.covector(*args, **kwds)
        assert value.tensor_valence() == (0, 1)
        assert value.lower_ranks() == (native.degree(),)
        assert value.list() == native.list()
        assert engine_ring(value.base_ring()) is engine_ring(tensor.vector(*args, **kwds).base_ring())


def test_a_covector_and_a_vector_of_the_same_components_are_distinct() -> None:
    covector = tensor.covector(ZZ, [1, 2, 3])
    vector_value = tensor.vector(ZZ, [1, 2, 3])

    assert covector != vector_value
    assert covector.parent() is not vector_value.parent()
    assert covector * vector_value == 14

    try:
        covector + vector_value
    except TypeError:
        pass
    else:
        raise AssertionError("a covector and a vector do not add")


def test_a_vector_reports_the_operands_own_variance_when_it_cannot_multiply() -> None:
    vector_value = tensor.vector(ZZ, [1, 2])

    try:
        vector_value * tensor.covector(ZZ, [3, 4])
    except TypeError as error:
        assert "type-(1, 0)" in str(error) and "type-(0, 1)" in str(error)
    else:
        raise AssertionError("a vector has no covariant index to contract")




def test_morphism_and_endomorphism_name_codomain_and_domain_indices() -> None:
    f = tensor.morphism(ZZ, 2, 3, [[1, 0, 2], [0, 1, 3]])
    t = tensor.endomorphism(ZZ, 2, [[0, 1], [1, 0]])

    assert f.tensor_valence() == (1, 1)
    assert f.upper_ranks() == (2,) and f.lower_ranks() == (3,)
    assert (f * tensor.vector(ZZ, [1, 1, 1])).list() == [3, 4]
    assert t.upper_ranks() == t.lower_ranks() == (2,)
    assert t.trace() == 0
    assert t * t == tensor.endomorphism(ZZ, 2, [[1, 0], [0, 1]])


def test_morphism_constructors_refuse_the_infinite_rank_reading() -> None:
    from sage.rings.infinity import Infinity

    for build in (
        lambda: tensor.morphism(ZZ, Infinity, 2),
        lambda: tensor.endomorphism(ZZ, Infinity),
    ):
        try:
            build()
        except ValueError as error:
            assert "finitely generated" in str(error)
        else:
            raise AssertionError("a type-(1,1) reading needs finite generation")


def test_a_tensor_is_component_data_only_where_a_shape_makes_sense() -> None:
    covector = tensor.covector(ZZ, [1, 2, 3])

    assert tensor.matrix(ZZ, covector).components() == [[1, 2, 3]]

    try:
        tensor.matrix(ZZ, tensor(ZZ, (2, 2), (2,), range(8)))
    except TypeError as error:
        assert "component data" in str(error)
    else:
        raise AssertionError("a three-index tensor is not a matrix's components")
