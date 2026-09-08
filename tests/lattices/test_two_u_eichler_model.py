r"""The represented ``2U`` determinant model carries the two exact SL2 actions."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.eichler_criterion import two_u_eichler_model
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def _model():
    integers = _own_ring(SageZZ)
    return two_u_eichler_model(Lattices(integers)("A1"))


def test_left_and_right_sl2_actions_are_actual_action_functors() -> None:
    model = _model()
    group = model.special_linear_group()
    generators = tuple(group.group_generators())
    left = model.left_action_functor()
    right = model.right_action_functor()
    point = group.classifying_category().an_object()
    arrows = group.classifying_category().Mor(point, point)

    assert left.domain() == group.classifying_category()
    assert right.domain() == group.classifying_category()
    assert left.codomain().Mor(model.lattice(), model.lattice()) is model.lattice().O()
    assert left(arrows(generators[0])) == model.left_action(generators[0])
    assert right(arrows(generators[0])) == model.right_action(generators[0])


def test_the_determinant_model_actions_preserve_the_group_law_and_commute() -> None:
    model = _model()
    group = model.special_linear_group()
    first, second = tuple(group.group_generators())[:2]

    assert model.left_action(first * second) == (
        model.left_action(first) * model.left_action(second)
    )
    assert model.right_action(first * second) == (
        model.right_action(first) * model.right_action(second)
    )
    assert model.left_action(~first) == ~model.left_action(first)
    assert model.right_action(~first) == ~model.right_action(first)
    assert model.left_action(group.one()) == model.lattice().O().one()
    assert model.right_action(group.one()) == model.lattice().O().one()

    for left_generator in (first, second):
        for right_generator in (first, second):
            assert (
                model.left_action(left_generator) * model.right_action(right_generator)
                == model.right_action(right_generator) * model.left_action(left_generator)
            )


def test_both_sl2_factors_fix_the_orthogonal_complement_pointwise() -> None:
    model = _model()
    lattice = model.lattice()
    complement = model.orthogonal_complement()
    inclusion = lattice.injection(2)

    for group_element in model.special_linear_group().group_generators():
        for generator in complement.module_generators():
            embedded = inclusion(generator)
            assert model.left_action(group_element)(embedded) == embedded
            assert model.right_action(group_element)(embedded) == embedded


def test_K_direction_eichler_transvections_are_stable_isometries() -> None:
    model = _model()
    lattice = model.lattice()
    isotropic = model.hyperbolic_basis()[0]
    identity_discriminant_action = lattice.O().one().discriminant_morphism()

    transvections = model.complement_eichler_transvections()
    assert transvections.cardinality() == model.orthogonal_complement().module_rank()
    for transvection in transvections:
        assert transvection in lattice.O()
        assert transvection(isotropic) == isotropic
        assert transvection.discriminant_morphism() == identity_discriminant_action
