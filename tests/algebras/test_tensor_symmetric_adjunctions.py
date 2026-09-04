import pytest
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings

from dzack_research.preamble.all import (
    Algebras,
    AlternatingAlgebraOf,
    BasedFreeModule,
    BilinearMap,
    CommutativeAlgebras,
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModule,
    FinitelyPresentedModules,
    FinitelyPresentedTorsionModules,
    SymmetricAlgebras,
    TensorAlgebras,
    TensorProduct,
    ZZ,
    algebra_homset,
    module_homset,
    symmetric_algebra_adjunction,
    symmetric_algebra_functor,
    tensor_algebra_adjunction,
    tensor_algebra_functor,
)
from dzack_research.preamble.categories.algebras.power_algebras import (
    power_algebra_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic(order):
    return FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((order,))


def _dual_numbers_mod_four():
    r"""Return the algebra ``(ZZ/4)[epsilon]/(epsilon^2)`` on its module."""
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4, 4))
    one = module.module_generator(0)
    epsilon = module.module_generator(1)
    multiplication = TensorProduct(module, module).from_bilinear(
        BilinearMap(
            module,
            module,
            module,
            {
                (0, 0): one,
                (0, 1): epsilon,
                (1, 0): epsilon,
                (1, 1): module.zero(),
            },
        )
    )
    algebra = Algebras(ZZ)(multiplication)
    one = algebra.module_generator(0)
    epsilon = algebra.module_generator(1)
    sign_module_map = module_homset(algebra, algebra)({0: one, 1: -epsilon})
    sign_algebra_map = algebra_homset(algebra, algebra)(sign_module_map)
    return algebra, sign_algebra_map


def test_module_map_is_adopted_as_an_algebra_map_only_when_it_preserves_the_laws() -> (
    None
):
    algebra, _involution = _dual_numbers_mod_four()
    one = algebra.module_generator(0)
    epsilon = algebra.module_generator(1)

    nonunital = module_homset(algebra, algebra)({0: algebra.zero(), 1: epsilon})
    with pytest.raises(ValueError, match="preserve the unit"):
        algebra_homset(algebra, algebra)(nonunital)

    nonmultiplicative = module_homset(algebra, algebra)({0: one, 1: one})
    with pytest.raises(ValueError, match="not multiplicative"):
        algebra_homset(algebra, algebra)(nonmultiplicative)


def _assert_module_maps_agree(left, right, probes) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in probes:
        assert left(element) == right(element)


def _assert_algebra_maps_agree(left, right, probes) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in probes:
        assert left(element) == right(element)


def test_tensor_and_symmetric_algebras_impose_presented_module_relations_in_every_degree() -> (
    None
):
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4, 4))

    tensor = tensor_algebra_functor(ZZ)(module)
    symmetric = symmetric_algebra_functor(ZZ)(module)
    tx = tensor.algebra_generator(0)
    ty = tensor.algebra_generator(1)
    sx = symmetric.algebra_generator(0)
    sy = symmetric.algebra_generator(1)

    assert tensor in Algebras(ZZ)
    assert tensor in TensorAlgebras(ZZ)
    assert symmetric in CommutativeAlgebras(ZZ)
    assert symmetric in SymmetricAlgebras(ZZ)

    # The degree-one relations generate a two-sided ideal in T(M), hence hold
    # after multiplying on either side; Sym(M) has the analogous homogeneous
    # consequences in its commutative quotient.
    assert 4 * tx == tensor.zero()
    assert 4 * ty == tensor.zero()
    assert 4 * tx * ty == tensor.zero()
    assert 4 * ty * tx == tensor.zero()
    assert tx * ty != ty * tx

    assert 4 * sx == symmetric.zero()
    assert 4 * sy == symmetric.zero()
    assert 4 * sx * sy == symmetric.zero()
    assert sx * sy == sy * sx

    # A purported universal extension is accepted precisely when the selected
    # module relation is killed by the generator assignment.
    with pytest.raises(ValueError, match="relations"):
        tensor.Hom(tensor)({0: tensor.one(), 1: tensor.zero()})
    with pytest.raises(ValueError, match="relations"):
        symmetric.Hom(symmetric)({0: symmetric.one(), 1: symmetric.zero()})


def test_tensor_and_symmetric_algebras_use_the_actual_nondiagonal_module_presentation() -> (
    None
):
    free = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    presentation = module_homset(relations, free)(
        {"r": 2 * free.module_generator("x") + 4 * free.module_generator("y")}
    )
    module = FinitelyPresentedModule(presentation)

    for constructor in (tensor_algebra_functor(ZZ), symmetric_algebra_functor(ZZ)):
        algebra = constructor(module)
        x = algebra.algebra_generator("x")
        y = algebra.algebra_generator("y")
        assert 2 * x + 4 * y == algebra.zero()
        assert (2 * x + 4 * y) * x == algebra.zero()
        assert y * (2 * x + 4 * y) == algebra.zero()
        for relation in algebra.relations():
            assert algebra.algebra_presentation_morphism()(relation) == algebra.zero()


@pytest.mark.parametrize(
    "functor_factory",
    (tensor_algebra_functor, symmetric_algebra_functor),
)
def test_presented_algebra_functors_act_on_nonfree_module_morphisms_and_preserve_composition(
    functor_factory,
) -> None:
    source = _cyclic(8)
    middle = _cyclic(4)
    target = _cyclic(2)
    first = module_homset(source, middle)({0: middle.module_generator(0)})
    second = module_homset(middle, target)({0: target.module_generator(0)})
    functor = functor_factory(ZZ)

    source_algebra = functor(source)
    middle_algebra = functor(middle)
    target_algebra = functor(target)
    x = source_algebra.algebra_generator(0)
    y = middle_algebra.algebra_generator(0)
    z = target_algebra.algebra_generator(0)

    carried_first = functor(first)
    carried_second = functor(second)
    assert carried_first(x) == y
    assert carried_first(x * x + 3 * x) == y * y + 3 * y
    assert carried_second(y) == z

    carried_composite = functor(second * first)
    stepwise = carried_second * carried_first
    _assert_algebra_maps_agree(
        carried_composite,
        stepwise,
        (x, x * x, x * x * x + x),
    )


@pytest.mark.parametrize(
    "adjunction_factory",
    (tensor_algebra_adjunction, symmetric_algebra_adjunction),
)
def test_tensor_and_symmetric_hom_bijections_on_nonfree_modules_are_natural_and_satisfy_the_triangle_law(
    adjunction_factory,
) -> None:
    adjunction = adjunction_factory(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    source = _cyclic(8)
    target_module = _cyclic(4)
    target_algebra = free(target_module)
    target_generator = target_algebra.algebra_generator(0)
    target_underlying = underlying(target_algebra)

    # A genuinely torsion linear map M -> U(A) extends uniquely to F(M) -> A.
    linear = module_homset(source, target_underlying)(
        {0: target_underlying.from_realization(2 * target_generator)}
    )
    extension = adjunction.hom_set_isomorphism_inverse(linear)
    recovered = adjunction.hom_set_isomorphism_forward(extension)
    source_generator = source.module_generator(0)
    _assert_module_maps_agree(
        recovered,
        linear,
        (source_generator, 3 * source_generator),
    )

    free_source = free(source)
    x = free_source.algebra_generator(0)
    reextended = adjunction.hom_set_isomorphism_inverse(recovered)
    _assert_algebra_maps_agree(
        reextended,
        extension,
        (x, x * x, x * x * x + 3 * x),
    )

    # The literal first triangle epsilon_{F(M)} o F(eta_M) has matching
    # represented endpoints, including the infinite underlying module U(F(M)).
    unit = adjunction.unit(source)
    carried_unit = free(unit)
    counit = adjunction.counit(free_source)
    assert unit.codomain() is underlying(free_source)
    assert carried_unit.domain() is free_source
    assert carried_unit.codomain() is counit.domain()
    triangle = counit * carried_unit
    identity = algebra_homset(free_source, free_source).identity()
    _assert_algebra_maps_agree(
        triangle,
        identity,
        (x, x * x, x * x * x + 5 * x),
    )

    # Naturality in the module variable is the unit square on a nonfree map.
    quotient = module_homset(source, target_module)(
        {0: target_module.module_generator(0)}
    )
    left, right = adjunction.unit_transformation().naturality_square(quotient)
    _assert_module_maps_agree(
        left,
        right,
        (source_generator, 3 * source_generator),
    )

    # Naturality in the algebra variable is the Hom-bijection form of counit
    # naturality.  It can be tested without replacing U(A), which is generally
    # infinitely generated, by a false finite presentation.
    smaller_module = _cyclic(2)
    algebra_map = free(
        module_homset(target_module, smaller_module)(
            {0: smaller_module.module_generator(0)}
        )
    )
    postcomposed = adjunction.hom_set_isomorphism_forward(algebra_map * extension)
    transported = underlying(algebra_map) * recovered
    _assert_module_maps_agree(
        postcomposed,
        transported,
        (source_generator, 3 * source_generator),
    )


def test_symmetric_adjunction_targets_the_owned_commutative_algebra_category() -> None:
    adjunction = symmetric_algebra_adjunction(ZZ)
    assert adjunction.left_adjoint().codomain() == CommutativeAlgebras(ZZ)
    assert adjunction.right_adjoint().domain() == CommutativeAlgebras(ZZ)

    tensor_adjunction = tensor_algebra_adjunction(ZZ)
    assert tensor_adjunction.left_adjoint().codomain() == Algebras(ZZ)
    assert tensor_adjunction.right_adjoint().domain() == Algebras(ZZ)


@pytest.mark.parametrize(
    "adjunction_factory",
    (tensor_algebra_adjunction, symmetric_algebra_adjunction),
)
def test_counit_naturality_and_right_triangle_on_a_nonfree_presented_algebra(
    adjunction_factory,
) -> None:
    adjunction = adjunction_factory(ZZ)
    algebra, involution = _dual_numbers_mod_four()
    one = algebra.module_generator(0)
    epsilon = algebra.module_generator(1)

    assert algebra in FinitelyPresentedModules(ZZ)
    assert algebra not in FinitelyGeneratedFreeModules(ZZ)
    assert algebra in CommutativeAlgebras(ZZ)
    assert involution(one * epsilon) == involution(one) * involution(epsilon)
    assert involution(epsilon * epsilon) == involution(epsilon) * involution(epsilon)

    # The literal counit square for epsilon |-> -epsilon commutes.
    left, right = adjunction.counit_transformation().naturality_square(involution)
    probes = []
    for label in left.domain().algebra_generating_set():
        probes.append(left.domain().algebra_generator(label))
    probes.append(probes[0] * probes[1] + probes[1] * probes[1])
    _assert_algebra_maps_agree(left, right, probes)

    # The literal right triangle U(epsilon_A) o eta_{U(A)} = id_{U(A)}.
    underlying = adjunction.right_adjoint()
    underlying_algebra = underlying(algebra)
    counit = adjunction.counit(algebra)
    unit = adjunction.unit(underlying_algebra)
    underlying_counit = underlying(counit)
    assert unit.codomain() is underlying_counit.domain()
    triangle = underlying_counit * unit
    for element in (one, epsilon, one + 2 * epsilon):
        assert triangle(element) == element


@pytest.mark.parametrize(
    "adjunction_factory",
    (tensor_algebra_adjunction, symmetric_algebra_adjunction),
)
def test_iterated_free_algebra_normalizes_relations_in_actual_underlying_pieces(
    adjunction_factory,
) -> None:
    adjunction = adjunction_factory(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((2, 3))
    first_free = free(module)
    first_underlying = underlying(first_free)
    iterated_free = free(first_underlying)

    source_labels = iterated_free.algebra_generating_set()
    two_source_label = source_labels(1, 0)
    three_source_label = source_labels(1, 1)
    two_torsion = iterated_free.algebra_generator(two_source_label)
    three_torsion = iterated_free.algebra_generator(three_source_label)
    assert 2 * two_torsion == iterated_free.zero()
    assert 3 * three_torsion == iterated_free.zero()
    # Z/2 tensor Z/3 is zero.  This specifically rejects independent raw-label
    # reduction, which would leave this mixed monomial nonzero.
    assert two_torsion * three_torsion == iterated_free.zero()

    assert iterated_free.graded_piece(1) is first_underlying
    degree_two = iterated_free.graded_piece(2)
    degree_two_labels = degree_two.module_generating_set()
    degree_two_label = (
        degree_two_labels(lambda _position: two_source_label)
        if iterated_free.flavor() == "tensor"
        else degree_two_labels.from_multiplicities({two_source_label: 2})
    )
    degree_two_generator = degree_two.module_generator(degree_two_label)
    assert 2 * degree_two_generator == degree_two.zero()

    invalid = algebra_homset(iterated_free, first_free)(
        lambda _label: first_free.one()
    )
    with pytest.raises(ValueError, match="relations"):
        invalid(two_torsion)

    dual_module = BasedFreeModule(ZZ, finite_ordered_set(("one", "epsilon")))
    dual_one = dual_module.module_generator("one")
    dual_epsilon = dual_module.module_generator("epsilon")
    dual_multiplication = TensorProduct(dual_module, dual_module).from_bilinear(
        BilinearMap(
            dual_module,
            dual_module,
            dual_module,
            {
                ("one", "one"): dual_one,
                ("one", "epsilon"): dual_epsilon,
                ("epsilon", "one"): dual_epsilon,
                ("epsilon", "epsilon"): dual_module.zero(),
            },
        )
    )
    dual_numbers = Algebras(ZZ)(dual_multiplication)
    module_map_to_sparse = module_homset(dual_numbers, iterated_free)(
        {"one": iterated_free.one(), "epsilon": iterated_free.zero()}
    )
    algebra_map_to_sparse = algebra_homset(dual_numbers, iterated_free)(
        module_map_to_sparse
    )
    assert (
        algebra_map_to_sparse(dual_numbers.module_generator("one"))
        == iterated_free.one()
    )
    assert (
        algebra_map_to_sparse(dual_numbers.module_generator("epsilon"))
        == iterated_free.zero()
    )
    sparse_identity = algebra_homset(iterated_free, iterated_free).identity()
    composite_to_sparse = sparse_identity * algebra_map_to_sparse
    assert (
        composite_to_sparse(dual_numbers.module_generator("one")) == iterated_free.one()
    )
    assert (
        composite_to_sparse(dual_numbers.module_generator("epsilon"))
        == iterated_free.zero()
    )

    exterior_module = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    exterior = AlternatingAlgebraOf(exterior_module)
    exterior_unit_label = exterior.module_generating_set()(0, 0)
    augmentation = SetMorphism(
        exterior.Hom(iterated_free),
        lambda element: element.monomial_coefficients().get(
            exterior_unit_label, ZZ.zero()
        )
        * iterated_free.one(),
    )
    algebra_augmentation = algebra_homset(exterior, iterated_free)(augmentation)
    power_identity = power_algebra_homset(exterior, exterior).identity()
    composite_augmentation = algebra_augmentation * power_identity
    assert composite_augmentation(exterior.one()) == iterated_free.one()
    assert (
        composite_augmentation(exterior.algebra_generator("x")) == iterated_free.zero()
    )

    cover = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    nondiagonal = FinitelyPresentedModule(
        module_homset(relations, cover)(
            {"r": 2 * cover.module_generator("x") + 4 * cover.module_generator("y")}
        )
    )
    nondiagonal_iterated = free(underlying(free(nondiagonal)))
    nondiagonal_source_labels = nondiagonal_iterated.algebra_generating_set()
    x = nondiagonal_iterated.algebra_generator(
        nondiagonal_source_labels(1, "x")
    )
    y = nondiagonal_iterated.algebra_generator(
        nondiagonal_source_labels(1, "y")
    )
    assert 2 * x + 4 * y == nondiagonal_iterated.zero()
