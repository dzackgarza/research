from dzack_research.preamble.all import (
    ZZ,
    FinitelyPresentedTorsionModules,
    Groups,
    Modules,
)
from dzack_research.preamble.categories.sets import Sets, finite_ordered_set


def _assert_maps_agree(left, right, elements) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in elements:
        assert left(element) == right(element)






def _s3_c2_torsion_sign_module():
    supergroup = Groups.S(3)
    subgroup_generator = next(group_generator for group_generator in supergroup.group_generators() if group_generator.order() == 2)
    subgroup = supergroup.subgroup([subgroup_generator])
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))

    def sign_action(group_element, vector):
        return vector if group_element == subgroup.one() else -vector

    return supergroup, subgroup, Modules(ZZ[subgroup])(module, sign_action)






def test_free_group_underlying_set_adjunction_uses_indexed_free_group_universal_property() -> None:
    adjunction = Sets().free_group_adjunction()
    source = finite_ordered_set((ZZ(2), ZZ(3)))
    second_source = finite_ordered_set((ZZ(5), ZZ(7)))
    target = Groups.C(3)
    target_generator = target.group_generators()[0]
    free = adjunction.left_adjoint()(source)

    assert adjunction.right_adjoint()(target) is target
    set_morphism = Sets().Mor(source, target)(lambda point: target_generator if point == 2 else target_generator**2)
    group_morphism = adjunction.mor_set_isomorphism_inverse(set_morphism, target)
    recovered = adjunction.mor_set_isomorphism_forward(group_morphism, source)
    _assert_maps_agree(set_morphism, recovered, source)
    assert group_morphism.generator_morphism().parent() is Sets().Mor(source, target)
    assert group_morphism(free.free_generator(2) * free.free_generator(3) ** -1) == target_generator**-1

    direct = free.Mor(target)({ZZ(2): target_generator, ZZ(3): target_generator**2})
    assert direct.generator_morphism().parent() is Sets().Mor(source, target)

    source_map = Sets().Mor(source, second_source)(lambda point: ZZ(5) if point == 2 else ZZ(7))
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_maps_agree(left, right, source)

    target_endomorphism = target.Mor(target)({target_generator: target_generator**2})
    left, right = adjunction.counit_transformation().naturality_square(target_endomorphism)
    for group_element in left.domain().free_basis():
        free_generator = left.domain().free_generator(group_element)
        assert left(free_generator) == right(free_generator)

    first_triangle = adjunction.right_adjoint()(adjunction.counit(target)) * adjunction.unit(adjunction.right_adjoint()(target))
    for group_element in target:
        assert first_triangle(group_element) == group_element

    second_triangle = adjunction.counit(free) * adjunction.left_adjoint()(adjunction.unit(source))
    for point in source:
        assert second_triangle(free.free_generator(point)) == free.free_generator(point)

    infinite_free = adjunction.left_adjoint()(ZZ)
    infinite_set_morphism = Sets().Mor(ZZ, target)(lambda integer: target_generator ** (integer % 3))
    infinite_group_morphism = adjunction.mor_set_isomorphism_inverse(infinite_set_morphism, target)
    infinite_recovered = adjunction.mor_set_isomorphism_forward(infinite_group_morphism, ZZ)
    for integer in (ZZ(-5), ZZ(-1), ZZ(0), ZZ(2), ZZ(7)):
        assert infinite_recovered(integer) == infinite_set_morphism(integer)
    word = infinite_free.free_generator(2) * infinite_free.free_generator(-1) ** -2 * infinite_free.free_generator(7)
    assert infinite_group_morphism(word) == (infinite_set_morphism(2) * infinite_set_morphism(-1) ** -2 * infinite_set_morphism(7))
    infinite_triangle = adjunction.counit(infinite_free) * adjunction.left_adjoint()(adjunction.unit(ZZ))
    for integer in (ZZ(-3), ZZ(0), ZZ(4)):
        assert infinite_triangle(infinite_free.free_generator(integer)) == infinite_free.free_generator(integer)






def test_induction_and_coinduction_preserve_torsion_presentations_and_adjunction_laws() -> None:
    supergroup, subgroup, module = _s3_c2_torsion_sign_module()
    module_generator = module.module_generator(0)
    assert module_generator.additive_order() == 4

    induction = Modules(ZZ[subgroup]).induction_restriction_adjunction(supergroup)
    induced = induction.left_adjoint()(module)
    induced_invariants = induced.invariant_factors()
    assert induced_invariants.cardinality() == 3
    assert all(induced_invariants[position] == ZZ(4) for position in range(3))
    assert all(generator.additive_order() == 4 for generator in induced.module_generators())

    induced_doubling = induced.Mor(induced)({label: 2 * induced.module_generator(label) for label in induced.module_generating_set()})
    induction_transpose = induction.mor_set_isomorphism_forward(induced_doubling, module)
    induction_recovered = induction.mor_set_isomorphism_inverse(induction_transpose, induced)
    _assert_maps_agree(
        induction_recovered,
        induced_doubling,
        induced.module_generators(),
    )
    induction_triangle = induction.counit(induced) * induction.left_adjoint()(induction.unit(module))
    _assert_maps_agree(
        induction_triangle,
        induced.Mor(induced).identity(),
        induced.module_generators(),
    )

    coinduction = Modules(ZZ[supergroup]).restriction_coinduction_adjunction(subgroup)
    coinduced = coinduction.right_adjoint()(module)
    coinduced_invariants = coinduced.invariant_factors()
    assert coinduced_invariants.cardinality() == 3
    assert all(coinduced_invariants[position] == ZZ(4) for position in range(3))
    assert all(generator.additive_order() == 4 for generator in coinduced.module_generators())

    coinduced_doubling = coinduced.Mor(coinduced)({label: 2 * coinduced.module_generator(label) for label in coinduced.module_generating_set()})
    coinduction_transpose = coinduction.mor_set_isomorphism_inverse(coinduced_doubling, module)
    coinduction_recovered = coinduction.mor_set_isomorphism_forward(coinduction_transpose, coinduced)
    _assert_maps_agree(
        coinduction_recovered,
        coinduced_doubling,
        coinduced.module_generators(),
    )
    coinduction_triangle = coinduction.right_adjoint()(coinduction.counit(module)) * coinduction.unit(coinduced)
    _assert_maps_agree(
        coinduction_triangle,
        coinduced.Mor(coinduced).identity(),
        coinduced.module_generators(),
    )
