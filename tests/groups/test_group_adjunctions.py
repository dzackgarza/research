
from dzack_research.preamble.all import (
    FiniteGSets,
    FiniteSets,
    BasedFreeModule,
    finite_g_set,
    FinitelyPresentedTorsionModules,
    Modules,
    Groups,
    ZZ,
    free_group_underlying_set_adjunction,
    g_set_homset,
    group_homset,
    induction_restriction_adjunction,
    restriction_coinduction_adjunction,
)
from dzack_research.preamble.categories.sets import Sets, finite_ordered_set


def _assert_maps_agree(left, right, elements) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in elements:
        assert left(element) == right(element)


def _nontrivial_c2_set():
    group = Groups.C(2)
    points = finite_ordered_set((ZZ(0), ZZ(1), ZZ(2)))
    generator = group.group_generators().unrank(0)

    def action(group_element, point):
        if group_element == group.one():
            return point
        if point == ZZ(0):
            return ZZ(1)
        if point == ZZ(1):
            return ZZ(0)
        return point

    return group, finite_g_set(points, group, action)


def _s3_c2_sign_module():
    supergroup = Groups.S(3)
    subgroup_generator = next(
        group_generator
        for group_generator in supergroup.group_generators()
        if group_generator.order() == 2
    )
    subgroup = supergroup.subgroup([subgroup_generator])
    module = BasedFreeModule(ZZ, finite_ordered_set(("m",)))

    def sign_action(group_element, vector):
        return vector if group_element == subgroup.one() else -vector

    return supergroup, subgroup, Modules(ZZ[subgroup])(module, sign_action)


def _s3_c2_torsion_sign_module():
    supergroup = Groups.S(3)
    subgroup_generator = next(
        group_generator
        for group_generator in supergroup.group_generators()
        if group_generator.order() == 2
    )
    subgroup = supergroup.subgroup([subgroup_generator])
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))

    def sign_action(group_element, vector):
        return vector if group_element == subgroup.one() else -vector

    return supergroup, subgroup, Modules(ZZ[subgroup])(module, sign_action)


def test_orbits_trivial_fixed_gset_adjoints_have_hom_bijections_naturality_and_triangles() -> None:
    group, acted = _nontrivial_c2_set()
    group_generator = group.group_generators().unrank(0)
    target = finite_ordered_set((ZZ(10), ZZ(20)))
    second_target = finite_ordered_set((ZZ(30), ZZ(40)))

    orbit_adjunction = FiniteGSets(group).orbits_trivial_adjunction()
    orbits = orbit_adjunction.left_adjoint()(acted)
    orbit_map = Sets().Mor(orbits, target)(lambda orbit: ZZ(10) if orbit.representative() in (0, 1) else ZZ(20))
    equivariant = orbit_adjunction.hom_set_isomorphism_forward(orbit_map)
    recovered_orbit_map = orbit_adjunction.hom_set_isomorphism_inverse(equivariant)
    _assert_maps_agree(orbit_map, recovered_orbit_map, orbits)

    acted_endomorphism = g_set_homset(acted, acted)(
        lambda point: acted.act(group_generator, point)
    )
    left, right = orbit_adjunction.unit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, acted)

    target_map = Sets().Mor(target, second_target)(lambda point: ZZ(30) if point == 10 else ZZ(40))
    left, right = orbit_adjunction.counit_transformation().naturality_square(
        target_map
    )
    _assert_maps_agree(left, right, tuple(left.domain()))

    trivial_target = orbit_adjunction.right_adjoint()(target)
    first_triangle = orbit_adjunction.right_adjoint()(
        orbit_adjunction.counit(target)
    ) * orbit_adjunction.unit(trivial_target)
    _assert_maps_agree(
        first_triangle,
        g_set_homset(trivial_target, trivial_target).identity(),
        trivial_target,
    )
    second_triangle = orbit_adjunction.counit(orbits) * orbit_adjunction.left_adjoint()(
        orbit_adjunction.unit(acted)
    )
    for orbit in orbits:
        assert second_triangle(orbit) == orbit

    fixed_adjunction = FiniteSets().trivial_fixed_adjunction(group)
    source = finite_ordered_set((ZZ(50), ZZ(60)))
    trivial_source = fixed_adjunction.left_adjoint()(source)
    fixed_morphism = g_set_homset(trivial_source, acted)(lambda _point: ZZ(2))
    transpose = fixed_adjunction.hom_set_isomorphism_forward(fixed_morphism)
    recovered = fixed_adjunction.hom_set_isomorphism_inverse(transpose, acted)
    _assert_maps_agree(fixed_morphism, recovered, trivial_source)
    assert tuple(fixed_adjunction.right_adjoint()(acted)) == (ZZ(2),)

    source_endomorphism = Sets().Mor(source, source)(lambda point: ZZ(60) if point == 50 else ZZ(50))
    left, right = fixed_adjunction.unit_transformation().naturality_square(
        source_endomorphism
    )
    _assert_maps_agree(left, right, source)

    left, right = fixed_adjunction.counit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, tuple(left.domain()))

    fixed_source = fixed_adjunction.right_adjoint()(trivial_source)
    first_triangle = fixed_adjunction.right_adjoint()(
        fixed_adjunction.counit(trivial_source)
    ) * fixed_adjunction.unit(fixed_source)
    for point in fixed_source:
        assert first_triangle(point) == point
    second_triangle = fixed_adjunction.counit(trivial_source) * fixed_adjunction.left_adjoint()(
        fixed_adjunction.unit(source)
    )
    for point in trivial_source:
        assert second_triangle(point) == point


def test_free_underlying_cofree_gset_adjoints_have_hom_bijections_naturality_and_triangles() -> None:
    group, acted = _nontrivial_c2_set()
    source = finite_ordered_set((ZZ(10), ZZ(20)))
    second_source = finite_ordered_set((ZZ(30), ZZ(40)))

    free_adjunction = FiniteSets().free_underlying_adjunction(group)
    free = free_adjunction.left_adjoint()(source)
    equivariant = g_set_homset(free, acted)(
        lambda point: acted.act(
            point[0], ZZ(0) if point[1] == 10 else ZZ(2)
        )
    )
    transpose = free_adjunction.hom_set_isomorphism_forward(equivariant)
    recovered = free_adjunction.hom_set_isomorphism_inverse(transpose)
    _assert_maps_agree(equivariant, recovered, free)

    set_map = Sets().Mor(source, second_source)(lambda point: ZZ(30) if point == 10 else ZZ(40))
    left, right = free_adjunction.unit_transformation().naturality_square(set_map)
    _assert_maps_agree(left, right, source)

    group_generator = group.group_generators().unrank(0)
    acted_endomorphism = g_set_homset(acted, acted)(
        lambda point: acted.act(group_generator, point)
    )
    left, right = free_adjunction.counit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, tuple(left.domain()))

    first_triangle = free_adjunction.right_adjoint()(
        free_adjunction.counit(acted)
    ) * free_adjunction.unit(free_adjunction.right_adjoint()(acted))
    for point in acted:
        assert first_triangle(point) == point
    second_triangle = free_adjunction.counit(free) * free_adjunction.left_adjoint()(
        free_adjunction.unit(source)
    )
    for point in free:
        assert second_triangle(point) == point

    cofree_adjunction = FiniteGSets(group).underlying_cofree_adjunction()
    arbitrary_set_map = Sets().Mor(acted, source)(lambda point: ZZ(10) if point in (0, 2) else ZZ(20))
    cofree_transpose = cofree_adjunction.hom_set_isomorphism_forward(
        arbitrary_set_map
    )
    recovered_set_map = cofree_adjunction.hom_set_isomorphism_inverse(
        cofree_transpose
    )
    _assert_maps_agree(arbitrary_set_map, recovered_set_map, acted)

    left, right = cofree_adjunction.unit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, acted)
    left, right = cofree_adjunction.counit_transformation().naturality_square(
        set_map
    )
    _assert_maps_agree(left, right, tuple(left.domain()))

    cofree_source = cofree_adjunction.right_adjoint()(source)
    first_triangle = cofree_adjunction.right_adjoint()(
        cofree_adjunction.counit(source)
    ) * cofree_adjunction.unit(cofree_source)
    for function_point in cofree_source:
        assert first_triangle(function_point) == function_point
    second_triangle = cofree_adjunction.counit(
        cofree_adjunction.left_adjoint()(acted)
    ) * cofree_adjunction.left_adjoint()(cofree_adjunction.unit(acted))
    for point in acted:
        assert second_triangle(point) == point


def test_free_group_underlying_set_adjunction_uses_indexed_free_group_universal_property() -> None:
    adjunction = free_group_underlying_set_adjunction()
    source = finite_ordered_set((ZZ(2), ZZ(3)))
    second_source = finite_ordered_set((ZZ(5), ZZ(7)))
    target = Groups.C(3)
    target_generator = target.group_generators().unrank(0)
    free = adjunction.left_adjoint()(source)

    assert adjunction.right_adjoint()(target) is target
    set_morphism = Sets().Mor(source, target)(lambda point: target_generator if point == 2 else target_generator**2)
    group_morphism = adjunction.hom_set_isomorphism_inverse(set_morphism)
    recovered = adjunction.hom_set_isomorphism_forward(group_morphism)
    _assert_maps_agree(set_morphism, recovered, source)
    assert group_morphism(free.free_generator(2) * free.free_generator(3) ** -1) == target_generator**-1

    source_map = Sets().Mor(source, second_source)(lambda point: ZZ(5) if point == 2 else ZZ(7))
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_maps_agree(left, right, source)

    target_endomorphism = group_homset(target, target)(
        {target_generator: target_generator**2}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        target_endomorphism
    )
    for group_element in left.domain().free_basis():
        free_generator = left.domain().free_generator(group_element)
        assert left(free_generator) == right(free_generator)

    first_triangle = adjunction.right_adjoint()(
        adjunction.counit(target)
    ) * adjunction.unit(adjunction.right_adjoint()(target))
    for group_element in target:
        assert first_triangle(group_element) == group_element

    second_triangle = adjunction.counit(free) * adjunction.left_adjoint()(
        adjunction.unit(source)
    )
    for point in source:
        assert second_triangle(free.free_generator(point)) == free.free_generator(point)

    infinite_free = adjunction.left_adjoint()(ZZ)
    infinite_set_morphism = Sets().Mor(ZZ, target)(lambda integer: target_generator ** (integer % 3))
    infinite_group_morphism = adjunction.hom_set_isomorphism_inverse(
        infinite_set_morphism
    )
    infinite_recovered = adjunction.hom_set_isomorphism_forward(
        infinite_group_morphism
    )
    for integer in (ZZ(-5), ZZ(-1), ZZ(0), ZZ(2), ZZ(7)):
        assert infinite_recovered(integer) == infinite_set_morphism(integer)
    word = infinite_free.free_generator(2) * infinite_free.free_generator(-1) ** -2 * infinite_free.free_generator(7)
    assert infinite_group_morphism(word) == (
        infinite_set_morphism(2)
        * infinite_set_morphism(-1) ** -2
        * infinite_set_morphism(7)
    )
    infinite_triangle = adjunction.counit(infinite_free) * adjunction.left_adjoint()(
        adjunction.unit(ZZ)
    )
    for integer in (ZZ(-3), ZZ(0), ZZ(4)):
        assert infinite_triangle(infinite_free.free_generator(integer)) == infinite_free.free_generator(integer)


def test_induction_restriction_adjunction_has_equivariant_hom_bijection_naturality_and_triangles() -> None:
    supergroup, subgroup, module = _s3_c2_sign_module()
    adjunction = induction_restriction_adjunction(ZZ, subgroup, supergroup)
    induced = adjunction.left_adjoint()(module)

    doubled = induced.Mor(induced)(
        {
            label: 2 * induced.module_generator(label)
            for label in induced.module_generating_set()
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(doubled)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose)
    _assert_maps_agree(recovered, doubled, induced.module_generators())

    module_endomorphism = module.Mor(module)(
        {"m": 3 * module.module_generator("m")}
    )
    left, right = adjunction.unit_transformation().naturality_square(
        module_endomorphism
    )
    _assert_maps_agree(left, right, module.module_generators())

    induced_endomorphism = induced.Mor(induced)(
        {
            label: 5 * induced.module_generator(label)
            for label in induced.module_generating_set()
        }
    )
    left, right = adjunction.counit_transformation().naturality_square(
        induced_endomorphism
    )
    _assert_maps_agree(left, right, left.domain().module_generators())

    first_triangle = adjunction.right_adjoint()(
        adjunction.counit(induced)
    ) * adjunction.unit(adjunction.right_adjoint()(induced))
    _assert_maps_agree(
        first_triangle,
        first_triangle.domain().Mor(first_triangle.domain()).identity(),
        first_triangle.domain().module_generators(),
    )

    second_triangle = adjunction.counit(induced) * adjunction.left_adjoint()(
        adjunction.unit(module)
    )
    _assert_maps_agree(
        second_triangle,
        induced.Mor(induced).identity(),
        induced.module_generators(),
    )


def test_restriction_coinduction_adjunction_has_equivariant_hom_bijection_naturality_and_triangles() -> None:
    supergroup, subgroup, module = _s3_c2_sign_module()
    adjunction = restriction_coinduction_adjunction(ZZ, subgroup, supergroup)
    coinduced = adjunction.right_adjoint()(module)

    doubled = coinduced.Mor(coinduced)(
        {
            label: 2 * coinduced.module_generator(label)
            for label in coinduced.module_generating_set()
        }
    )
    transpose = adjunction.hom_set_isomorphism_inverse(doubled)
    recovered = adjunction.hom_set_isomorphism_forward(transpose)
    _assert_maps_agree(recovered, doubled, coinduced.module_generators())

    coinduced_endomorphism = coinduced.Mor(coinduced)(
        {
            label: 3 * coinduced.module_generator(label)
            for label in coinduced.module_generating_set()
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(
        coinduced_endomorphism
    )
    _assert_maps_agree(left, right, coinduced.module_generators())

    module_endomorphism = module.Mor(module)(
        {"m": 5 * module.module_generator("m")}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        module_endomorphism
    )
    _assert_maps_agree(left, right, left.domain().module_generators())

    first_triangle = adjunction.right_adjoint()(
        adjunction.counit(module)
    ) * adjunction.unit(coinduced)
    _assert_maps_agree(
        first_triangle,
        coinduced.Mor(coinduced).identity(),
        coinduced.module_generators(),
    )

    restricted = adjunction.left_adjoint()(coinduced)
    second_triangle = adjunction.counit(restricted) * adjunction.left_adjoint()(
        adjunction.unit(coinduced)
    )
    _assert_maps_agree(
        second_triangle,
        restricted.Mor(restricted).identity(),
        restricted.module_generators(),
    )


def test_induction_and_coinduction_preserve_torsion_presentations_and_adjunction_laws() -> None:
    supergroup, subgroup, module = _s3_c2_torsion_sign_module()
    module_generator = module.module_generator(0)
    assert module_generator.additive_order() == 4

    induction = induction_restriction_adjunction(ZZ, subgroup, supergroup)
    induced = induction.left_adjoint()(module)
    induced_invariants = induced.invariant_factors()
    assert induced_invariants.cardinality() == 3
    assert all(induced_invariants.unrank(position) == ZZ(4) for position in range(3))
    assert all(generator.additive_order() == 4 for generator in induced.module_generators())

    induced_doubling = induced.Mor(induced)(
        {
            label: 2 * induced.module_generator(label)
            for label in induced.module_generating_set()
        }
    )
    induction_transpose = induction.hom_set_isomorphism_forward(induced_doubling)
    induction_recovered = induction.hom_set_isomorphism_inverse(induction_transpose)
    _assert_maps_agree(
        induction_recovered,
        induced_doubling,
        induced.module_generators(),
    )
    induction_triangle = induction.counit(induced) * induction.left_adjoint()(
        induction.unit(module)
    )
    _assert_maps_agree(
        induction_triangle,
        induced.Mor(induced).identity(),
        induced.module_generators(),
    )

    coinduction = restriction_coinduction_adjunction(ZZ, subgroup, supergroup)
    coinduced = coinduction.right_adjoint()(module)
    coinduced_invariants = coinduced.invariant_factors()
    assert coinduced_invariants.cardinality() == 3
    assert all(
        coinduced_invariants.unrank(position) == ZZ(4)
        for position in range(3)
    )
    assert all(generator.additive_order() == 4 for generator in coinduced.module_generators())

    coinduced_doubling = coinduced.Mor(coinduced)(
        {
            label: 2 * coinduced.module_generator(label)
            for label in coinduced.module_generating_set()
        }
    )
    coinduction_transpose = coinduction.hom_set_isomorphism_inverse(
        coinduced_doubling
    )
    coinduction_recovered = coinduction.hom_set_isomorphism_forward(
        coinduction_transpose
    )
    _assert_maps_agree(
        coinduction_recovered,
        coinduced_doubling,
        coinduced.module_generators(),
    )
    coinduction_triangle = coinduction.right_adjoint()(
        coinduction.counit(module)
    ) * coinduction.unit(coinduced)
    _assert_maps_agree(
        coinduction_triangle,
        coinduced.Mor(coinduced).identity(),
        coinduced.module_generators(),
    )
