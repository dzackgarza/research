r"""The represented ``2U`` determinant model carries the two exact SL2 actions."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def _model():
    integers = _own_ring(SageZZ)
    return Lattices(integers)("A1").two_u_eichler_model()


def test_left_and_right_sl2_actions_are_actual_action_functors() -> None:
    model = _model()
    group = model.special_linear_group()
    generators = group.group_generators()
    left = model.left_action_functor()
    right = model.right_action_functor()
    point = group.classifying_category().an_object()
    arrows = group.classifying_category().Mor(point, point)

    assert left.domain() == group.classifying_category()
    assert right.domain() == group.classifying_category()
    lattice = model.lattice()
    lattice_mor = left.codomain().Mor(lattice, lattice)
    assert lattice_mor is lattice.Mor(lattice)
    left_arrow = left(arrows(generators[0]))
    right_arrow = right(arrows(generators[0]))
    left_isometry = model.left_action(generators[0])
    right_isometry = model.right_action(generators[0])
    assert left_arrow.parent() is lattice.O()
    assert right_arrow.parent() is lattice.O()
    assert lattice_mor(left_arrow) is left_arrow
    assert lattice_mor(right_arrow) is right_arrow
    assert left_arrow == left_isometry
    assert right_arrow == right_isometry


def test_the_determinant_model_actions_preserve_the_group_law_and_commute() -> None:
    model = _model()
    group = model.special_linear_group()
    generators = group.group_generators()
    first, second = generators[0], generators[1]

    assert model.left_action(first * second) == (model.left_action(first) * model.left_action(second))
    assert model.right_action(first * second) == (model.right_action(first) * model.right_action(second))
    assert model.left_action(~first) == ~model.left_action(first)
    assert model.right_action(~first) == ~model.right_action(first)
    assert model.left_action(group.one()) == model.lattice().O().one()
    assert model.right_action(group.one()) == model.lattice().O().one()

    for left_generator in (first, second):
        for right_generator in (first, second):
            assert model.left_action(left_generator) * model.right_action(right_generator) == model.right_action(right_generator) * model.left_action(left_generator)


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


def test_actual_K_isometries_extend_canonically_and_need_no_discriminant_guess() -> None:
    integers = _own_ring(SageZZ)
    complement = Lattices(integers)("A2")
    model = complement.two_u_eichler_model()
    lattice = model.lattice()
    minus_one = complement.O()(tuple(-generator for generator in complement.module_generators()))
    lifted = model.complement_action(minus_one)

    for hyperbolic_generator in model.hyperbolic_basis():
        assert lifted(hyperbolic_generator) == hyperbolic_generator
    inclusion = lattice.injection(2)
    for generator in complement.module_generators():
        assert lifted(inclusion(generator)) == inclusion(minus_one(generator))

    assert model.complement_action(complement.O().one()) == lattice.O().one()
    assert model.complement_action(minus_one * minus_one) == (model.complement_action(minus_one) * model.complement_action(minus_one))
    assert lifted.discriminant_morphism() != lattice.O().one().discriminant_morphism()

    action = model.complement_action_functor()
    point = complement.O().classifying_category().an_object()
    arrow = complement.O().classifying_category().Mor(point, point)(minus_one)
    assert action(arrow) == lifted


def test_covering_discriminant_classes_have_explicit_primitive_vectors() -> None:
    integers = _own_ring(SageZZ)
    complement = Lattices(integers)("A2")
    model = complement.two_u_eichler_model()
    square = integers(-2)
    representatives = model.covering_vector_representatives(square)

    assert representatives.cardinality() > 0
    for discriminant_class in representatives.index_set():
        vector = representatives[discriminant_class]
        assert vector.q() == square
        assert vector.is_primitive()
        assert vector.div() == discriminant_class.additive_order()
        assert discriminant_class in complement.covering_discriminant_classes(square)


def test_unimodular_complement_covering_representative_is_the_hyperbolic_one() -> None:
    integers = _own_ring(SageZZ)
    complement = Lattices(integers)("E8")
    model = complement.two_u_eichler_model()
    representatives = model.covering_vector_representatives(integers(2))

    assert representatives.cardinality() == 1
    vector = next(iter(representatives))
    assert vector.q() == 2
    assert vector.div() == 1
    assert vector.is_primitive()


def test_two_u_model_lifts_generators_of_its_full_discriminant_group() -> None:
    integers = _own_ring(SageZZ)
    complement = Lattices(integers)("A2")
    model = complement.two_u_eichler_model()
    lattice = model.lattice()
    target = lattice.discriminant_group().O()
    lifts = model.discriminant_generator_lifts()

    target_generators = target.group_generators()
    assert lifts.index_set() == target_generators
    for generator in lifts.index_set():
        witness = lifts[generator]
        assert witness in lattice.O()
        assert witness.discriminant_morphism() == generator


def test_source_generating_family_retains_each_mathematical_source() -> None:
    integers = _own_ring(SageZZ)
    complement = Lattices(integers)("A2")
    model = complement.two_u_eichler_model()
    family = model.source_generating_family()
    kinds = {kind for kind, _datum in family.index_set()}

    assert kinds == {
        "left-SL2",
        "right-SL2",
        "O(K)",
        "Eichler",
        "discriminant-lift",
    }
    assert all(isometry in model.lattice().O() for isometry in family)
    for kind, datum in family.index_set():
        match kind:
            case "left-SL2":
                assert family[kind, datum] == model.left_action(datum)
            case "right-SL2":
                assert family[kind, datum] == model.right_action(datum)
            case "O(K)":
                assert family[kind, datum] == model.complement_action(datum)
            case "Eichler" | "discriminant-lift":
                assert family[kind, datum] in model.lattice().O()
            case _:
                raise AssertionError(f"unexpected generator source {kind}")
