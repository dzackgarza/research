r"""Type-$(p,q)$ tensors: what they are, and how they are written down.

A Gram matrix is the components of a type-$(0,2)$ tensor -- twice covariant,
because it eats two vectors.  A multiplication table $m:A\otimes_R A\to A$ is
type $(1,2)$, once up and twice down.  Neither is "a matrix with more
indices": the valence is part of what the object is, and these check that it
is carried rather than inferred at the call site.
"""

import pytest


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _tensor():
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.tensors import tensor

    return tensor


def test_a_gram_matrix_is_a_twice_covariant_tensor() -> None:
    r"""$A_2$'s form, written as it would be written as a matrix."""
    tensor = _tensor()
    form = tensor(ZZ, [[-2, 1], [1, -2]])

    assert form.valence() == (0, 2), "a form eats two vectors and returns a scalar"
    assert form[0, 0] == -2 and form[0, 1] == 1

    e = list(form.parent().module().module_generators())
    assert form(e[0], e[0]) == -2, "the norm of a root, in the AG convention"
    assert form(e[0], e[1]) == 1
    assert form(e[0], e[1]) == form(e[1], e[0]), "this one is symmetric"


def test_the_nesting_says_how_many_slots_and_covariance_is_the_default() -> None:
    r"""Depth is the number of slots; a form is what an unlabelled one is."""
    tensor = _tensor()

    assert tensor(ZZ, [[1, 0], [0, 1]]).valence() == (0, 2)
    assert tensor(ZZ, [[[1, 0], [0, 0]], [[0, 0], [0, 0]]]).valence() == (0, 3)


def test_a_multiplication_table_is_a_type_one_two_tensor() -> None:
    r"""$m:A\otimes_R A\to A$ is once contravariant and twice covariant.

    $R[x]/(x^2)$ on the basis $1, x$: $1\cdot 1 = 1$, $1\cdot x = x\cdot 1 =
    x$, and $x\cdot x = 0$, which is the component that is absent.
    """
    tensor = _tensor()
    multiplication = tensor(
        ZZ,
        [
            [[1, 0], [0, 0]],
            [[0, 1], [1, 0]],
        ],
        valence=(1, 2),
    )

    assert multiplication.valence() == (1, 2)
    assert multiplication[0, 0, 0] == 1, "1 * 1 = 1"
    assert multiplication[1, 0, 1] == 1, "1 * x = x"
    assert multiplication[1, 1, 0] == 1, "x * 1 = x"
    assert multiplication[0, 1, 1] == 0, "x * x = 0"


def test_a_stated_valence_must_account_for_every_slot() -> None:
    r"""A type and a nesting that disagree is a defect, not a coercion."""
    tensor = _tensor()

    with pytest.raises(AssertionError, match="slots"):
        tensor(ZZ, [[1, 2], [3, 4]], valence=(1, 2))


def test_ragged_components_are_refused() -> None:
    r"""The slots of a tensor on one module all have the module's size."""
    tensor = _tensor()

    with pytest.raises(AssertionError, match="ragged"):
        tensor(ZZ, [[1, 2], [3]])


def test_tensors_of_one_type_add_and_scale() -> None:
    r"""They are a module, and the components carry it."""
    tensor = _tensor()
    first = tensor(ZZ, [[1, 0], [0, 1]])
    second = tensor(ZZ, [[0, 1], [1, 0]])

    assert (first + second)[0, 0] == 1
    assert (first + second)[0, 1] == 1
    assert (2 * first)[1, 1] == 2

    e = list(first.parent().module().module_generators())
    assert (first + second)(e[0], e[1]) == first(e[0], e[1]) + second(e[0], e[1])


def test_evaluation_is_offered_only_where_it_means_something() -> None:
    r"""A tensor with an upper slot eats a functional, which is not supplied."""
    tensor = _tensor()
    multiplication = tensor(ZZ, [[[1, 0], [0, 0]], [[0, 1], [1, 0]]], valence=(1, 2))

    e = list(multiplication.parent().module().module_generators())
    with pytest.raises(AssertionError, match="purely covariant"):
        multiplication(e[0], e[1])
