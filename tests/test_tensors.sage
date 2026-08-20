r"""Type-$(p,q)$ tensors: what they are, and how they are written down.

A Gram matrix is the components of a type-$(0,2)$ tensor -- twice covariant,
because it eats two vectors.  A multiplication table $m:A\otimes_R A\to A$ is
type $(1,2)$, once up and twice down.  Neither is "a matrix with more
indices": the valence is part of what the object is, and these check that it
is carried rather than inferred at the call site.
"""

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable

    from dzack_research.preamble.categories.modules.tensors import TensorElement


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _tensor() -> "Callable[..., TensorElement]":
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.tensors import tensor

    constructor: "Callable[..., TensorElement]" = tensor
    return constructor


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


def test_a_multiplication_table_multiplies() -> None:
    r"""Fed two elements, $m$ returns the product -- a vector, not a scalar.

    Evaluation is partial: a type-$(p,q)$ tensor given $k\le q$ elements is a
    type-$(p,q-k)$ tensor.  So a table with an upper slot does not refuse; it
    hands back what the multiplication produced.
    """
    tensor = _tensor()
    multiplication = tensor(ZZ, [[[1, 0], [0, 0]], [[0, 1], [1, 0]]], valence=(1, 2))
    one, x = list(multiplication.parent().module().module_generators())

    product = multiplication(one, x)
    assert product.valence() == (1, 0), "a product is a vector"
    assert product.components() == {(1,): 1}, "1 * x = x"
    assert multiplication(x, x).components() == {}, "x * x = 0 in R[x]/(x^2)"


def test_feeding_one_element_leaves_a_tensor_with_the_rest_of_the_slots() -> None:
    r"""$g(v)$ is the functional $w\mapsto g(v,w)$, of type $(0,1)$."""
    tensor = _tensor()
    form = tensor(ZZ, [[-2, 1], [1, -2]])
    e = list(form.parent().module().module_generators())

    partial = form(e[0])
    assert partial.valence() == (0, 1)
    assert partial.components() == {(0,): -2, (1,): 1}, "the first row of the Gram matrix"


def test_contraction_pairs_an_upper_slot_with_a_lower_one() -> None:
    r"""The basic operation: sum over the shared index.

    A vector is a type-$(1,0)$ tensor and a functional a type-$(0,1)$ one, so
    there is nothing to hand in that is not already a tensor.
    """
    tensor = _tensor()
    form = tensor(ZZ, [[-2, 1], [1, -2]])
    vector = tensor(ZZ, [1, 0], valence=(1, 0))

    contracted = vector.contract(form, 0, 0)
    assert contracted.valence() == (0, 1)
    assert contracted.components() == {(0,): -2, (1,): 1}


def test_the_trace_contracts_a_tensor_against_itself() -> None:
    r"""The identity of a rank-2 module traces to 2."""
    tensor = _tensor()
    identity = tensor(ZZ, [[1, 0], [0, 1]], valence=(1, 1))

    assert identity.trace() == 2, "the trace of the identity is the rank"


def test_the_gram_matrix_is_the_forms_covariant_tensor() -> None:
    r"""A lattice's form, read as the type-$(0,2)$ tensor it is.

    Not a reformatting: the tensor is asked for the same pairings the form
    is, and they agree entry by entry, so the matrix really is the components
    of that tensor in this module's framing.
    """
    _ensure_preamble()
    lattice = Lattices.A2
    form_tensor = lattice.gram_tensor()

    assert form_tensor.valence() == (0, 2)

    lattice_generators = list(lattice.module_generators())
    for i in (0, 1):
        for j in (0, 1):
            assert form_tensor(lattice_generators[i], lattice_generators[j]) == lattice.b(
                lattice_generators[i], lattice_generators[j]
            ), "the tensor pairs what the form pairs"


def test_a_unimodular_form_raises_and_lowers_an_index() -> None:
    r"""For \(U\), raising one index of \(g\) gives \(\delta^i_j\)."""
    _ensure_preamble()
    gram = Lattices.U.gram_tensor()
    identity = Lattices.U.raise_index(gram, 0)

    assert identity.valence() == (1, 1)
    assert identity.components() == {(0, 0): 1, (1, 1): 1}
    assert Lattices.U.lower_index(identity, 0) == gram


def test_raising_an_integral_index_requires_unimodularity() -> None:
    r"""The inverse Gram matrix of \(A_2\) is not integral."""
    _ensure_preamble()

    with pytest.raises(AssertionError, match="unimodular"):
        Lattices.A2.raise_index(Lattices.A2.gram_tensor(), 0)


def test_a_nondegenerate_lattice_raises_indices_after_rationalization() -> None:
    r"""The inverse form of (A_2) exists on (A_2\otimes\mathbb Q)."""
    _ensure_preamble()
    rational_form = Lattices.A2.vector_space()
    raised = Lattices.A2.raise_index_over_fraction_field(
        Lattices.A2.gram_tensor(),
        0,
    )

    assert raised.parent().base_ring() == QQ
    assert raised.valence() == (1, 1)
    assert raised.components() == {(0, 0): QQ.one(), (1, 1): QQ.one()}
    assert rational_form.lower_index(raised, 0) == rational_form.gram_tensor()


def test_the_correlation_is_an_isomorphism_exactly_when_unimodular() -> None:
    r"""The two musical maps for \(U\) are inverse on every basis vector."""
    _ensure_preamble()
    correlation = Lattices.U.correlation_isomorphism()

    for generator in Lattices.U.module_generators():
        assert correlation.inverse()(correlation(generator)) == generator
    for functional in Lattices.U.dual_module().module_generators():
        assert correlation(correlation.inverse()(functional)) == functional

    with pytest.raises(AssertionError, match="unimodular"):
        Lattices.A2.correlation_isomorphism()


def test_tensor_values_are_sage_elements() -> None:
    r"""Tensor arithmetic belongs to the tensor parent."""
    _ensure_preamble()
    from sage.structure.element import Element

    value = _tensor()(ZZ, [[1, 0], [0, 1]])
    assert value.parent().zero() + value == value
    assert isinstance(value, Element)


def test_mixed_tensors_are_the_homogeneous_pieces_of_one_bigraded_algebra() -> None:
    r"""The product adds valences in \(T(M)\otimes_R T(M^*)\)."""
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.tensors import MixedTensorAlgebra

    module = BasedFreeModule(ZZ, Sets.Δ[1])
    algebra = MixedTensorAlgebra(module)
    vectors = algebra.homogeneous_piece((1, 0))
    covectors = algebra.homogeneous_piece((0, 1))
    x = algebra.include(vectors({(0,): 1}))
    y = algebra.include(vectors({(1,): 1}))
    phi = algebra.include(covectors({(0,): 2, (1,): 3}))

    assert algebra.vector_tensor_algebra() is TensorAlgebraOf(module)
    assert algebra.covector_tensor_algebra() is TensorAlgebraOf(DualModule(module))
    assert Tensor(module, (2, 1)) is algebra.homogeneous_piece((2, 1))
    assert (x * y * phi).valences() == ((2, 1),)
    assert (x * y) * phi == x * (y * phi)
    assert algebra.one() * x == x == x * algebra.one()
    assert x * y != y * x


def test_covariant_slots_use_the_dual_module() -> None:
    r"""For (M=\mathbb Z/2), (M^*=\operatorname{Hom}(M,\mathbb Z)=0)."""
    _ensure_preamble()
    free = BasedFreeModule(ZZ, Sets.Δ[0])
    relation = module_homset(free, free)({0: 2 * free.module_generator(0)})
    module = FinitelyPresentedModule(relation)

    dual = DualModule(module)
    vectors = Tensor(module, (1, 0))
    covectors = Tensor(module, (0, 1))
    vector = vectors({(0,): 1})

    assert dual.is_zero()
    assert covectors.intrinsic_module().is_zero()
    assert vector != vectors.zero()
    assert 2 * vector == vectors.zero()


def test_a_tensor_piece_is_the_tensor_product_of_powers_of_a_module_and_its_dual() -> None:
    r"""Type ((2,1)) has rank (2^2\cdot2=8) for a rank-two free module."""
    _ensure_preamble()
    module = BasedFreeModule(ZZ, Sets.Δ[1])
    tensors = Tensor(module, (2, 1))

    assert tensors.dual_module() is DualModule(module)
    assert tensors.dual_module().rank() == 2
    assert tensors.intrinsic_module().rank() == 8


def test_the_degree_two_piece_of_the_tensor_algebra_is_the_tensor_square() -> None:
    r"""$T(M)[2]$ has all $\mathrm{rank}^2$ words, so it is $M^{\otimes 2}$.

    Which is why no separate $M^{\otimes 2}$ is built: were this the
    symmetric quotient it would have three monomials on two generators, not
    four, and $xy$ would equal $yx$.
    """
    _ensure_preamble()
    from dzack_research.preamble.categories.algebras.framed_free_algebras import (
        TensorAlgebraOn,
    )

    algebra = TensorAlgebraOn(QQ, Sets.Δ[1])
    piece = algebra.graded_piece_monomials(2)

    assert len(piece) == 4, "two generators, so four words of length two"
    assert all(
        algebra.monomial_degree(monomial.monomials()[0]) == 2 for monomial in piece
    )

    x, y = [algebra.algebra_generator(label) for label in algebra.algebra_generating_set()]
    assert x * y != y * x, "the tensor square does not identify xy with yx"
