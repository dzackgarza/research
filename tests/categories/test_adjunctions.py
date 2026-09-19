import pytest

from dzack_research.preamble.all import (
    ZZ,
    Groups,
    Modules,
    OwnedOrders,
    QuadraticField,
    Sets,
)
from dzack_research.preamble.categories.functors.core import Adjunction
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_maps_agree(left, right, elements) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in elements:
        assert left(element) == right(element)


def _swap_group_module():
    group = Groups.C(2)
    module = ZZ.free_module(finite_ordered_set(("e", "f")))

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        coefficients = module.framing_coefficients(vector)
        return module.linear_combination(
            {
                "e": coefficients.get("f", ZZ.zero()),
                "f": coefficients.get("e", ZZ.zero()),
            }
        )

    return group, Modules(ZZ[group])(module, swap)


def test_adjunction_rejects_parallel_public_equivalent_data() -> None:
    with pytest.raises(TypeError, match="equivalent public data"):

        class _IndependentlySpecifiedAdjunction(Adjunction):
            def unit(self, obj):
                return obj

            def hom_set_isomorphism_forward(self, morphism, source):
                return morphism


def test_module_equalizer_and_coequalizer_use_kernel_and_cokernel_semantics() -> None:
    module = ZZ.free_module(finite_ordered_set(("e",)))
    e = module.module_generator("e")
    identity = module.module_category().Mor(module, module).identity()
    negative_identity = module.module_category().Mor(module, module)({"e": -e})

    equalizer = Modules(ZZ).equalizer(identity, negative_identity)
    coequalizer = Modules(ZZ).coequalizer(identity, negative_identity)

    assert equalizer.module_rank() == 0
    assert coequalizer in Modules(ZZ)
    assert coequalizer not in module.category()
    invariant_factors = coequalizer.invariant_factors()
    assert invariant_factors.cardinality() == 1
    assert invariant_factors[0] == ZZ(2)


def test_group_invariants_and_coinvariants_impose_all_generator_relations() -> None:
    group = Groups.V4()
    first, second = tuple(group.group_generators())
    product = first * second
    module = ZZ.free_module(finite_ordered_set(("e", "f")))

    def action(group_element, vector):
        coefficients = module.framing_coefficients(vector)
        first_sign = -1 if group_element in (first, product) else 1
        second_sign = -1 if group_element in (second, product) else 1
        return module.linear_combination(
            {
                "e": first_sign * coefficients.get("e", ZZ.zero()),
                "f": second_sign * coefficients.get("f", ZZ.zero()),
            }
        )

    acted = Modules(ZZ[group])(module, action)
    invariants = acted.module_invariants()
    coinvariants = acted.module_coinvariants()

    assert invariants.module_rank() == 0
    invariant_factors = coinvariants.invariant_factors()
    assert invariant_factors.cardinality() == 2
    assert tuple(invariant_factors) == (ZZ(2), ZZ(2))


def test_free_module_underlying_set_adjunction_has_the_hom_bijection_naturality_and_triangles() -> None:
    adjunction = Sets().free_module_adjunction(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()

    labels = finite_ordered_set(("x", "y"))
    module = ZZ.free_module(finite_ordered_set(("a", "b")))
    free_labels = free(labels)
    phi = free_labels.module_category().Mor(free_labels, module)(
        {
            "x": module.module_generator("a") + module.module_generator("b"),
            "y": 2 * module.module_generator("a"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(phi, labels)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, module)

    for label in labels:
        assert transpose(label) == phi(free_labels.module_generator(label))
        assert recovered(free_labels.module_generator(label)) == phi(
            free_labels.module_generator(label)
        )

    source_set = finite_ordered_set((ZZ(1), ZZ(2)))
    target_set = finite_ordered_set((ZZ(3), ZZ(4)))
    set_map = Sets().Mor(source_set, target_set)(lambda value: ZZ(3) if value == 1 else ZZ(4))
    left, right = adjunction.unit_transformation().naturality_square(set_map)
    _assert_maps_agree(left, right, source_set)

    target_module = ZZ.free_module(finite_ordered_set(("c",)))
    module_map = module.module_category().Mor(module, target_module)(
        {
            "a": target_module.module_generator("c"),
            "b": 2 * target_module.module_generator("c"),
        }
    )
    left, right = adjunction.counit_transformation().naturality_square(module_map)
    probes = (
        module.module_generator("a"),
        module.module_generator("b"),
        module.module_generator("a") + module.module_generator("b"),
    )
    free_underlying_module = left.domain()
    _assert_maps_agree(
        left,
        right,
        tuple(free_underlying_module.module_generator(probe) for probe in probes),
    )

    first_triangle = underlying(adjunction.counit(module)) * adjunction.unit(
        underlying(module)
    )
    for probe in probes:
        assert first_triangle(probe) == probe

    free_source_set = free(source_set)
    second_triangle = adjunction.counit(free_source_set) * free(
        adjunction.unit(source_set)
    )
    for generator in free_source_set.module_generators():
        assert second_triangle(generator) == generator


def test_scalar_extension_restriction_adjunction_over_a_quadratic_order_satisfies_all_laws() -> None:
    field = QuadraticField(2, "a")
    order = field.ring_of_integers()
    structure_map = order.algebra_structure_morphism()
    adjunction = Modules(structure_map.domain()).base_change_adjunction(structure_map)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    source = ZZ.free_module(finite_ordered_set(("u", "v")))
    target = order.free_module(finite_ordered_set(("p",)))
    extended_source = extension(source)
    restricted_target = restriction(target)

    assert restricted_target.module_generating_set().cardinality() == 2
    phi = extended_source.module_category().Mor(extended_source, target)(
        {
            "u": target.module_generator("p"),
            "v": order(2) * target.module_generator("p"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(phi, source)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, target)
    for label in source.module_generating_set():
        assert recovered(extended_source.module_generator(label)) == phi(
            extended_source.module_generator(label)
        )

    second_source = ZZ.free_module(finite_ordered_set(("r",)))
    source_map = source.module_category().Mor(source, second_source)(
        {
            "u": second_source.module_generator("r"),
            "v": 2 * second_source.module_generator("r"),
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_maps_agree(left, right, source.module_generators())

    second_target = order.free_module(finite_ordered_set(("q",)))
    target_map = target.module_category().Mor(target, second_target)(
        {"p": order(3) * second_target.module_generator("q")}
    )
    left, right = adjunction.counit_transformation().naturality_square(target_map)
    _assert_maps_agree(left, right, left.domain().module_generators())

    first_triangle = restriction(adjunction.counit(target)) * adjunction.unit(
        restricted_target
    )
    for generator in restricted_target.module_generators():
        assert first_triangle(generator) == generator

    second_triangle = adjunction.counit(extended_source) * extension(
        adjunction.unit(source)
    )
    for generator in extended_source.module_generators():
        assert second_triangle(generator) == generator


def test_trivial_action_is_left_adjoint_to_invariants_using_equivariant_homsets() -> None:
    group, acted = _swap_group_module()
    e = acted.module_generator("e")
    f = acted.module_generator("f")

    try:
        acted.Mor(acted)(
            {"e": e, "f": e}
        )
    except ValueError as error:
        assert "not G-equivariant" in str(error)
    else:
        raise AssertionError("an R[G]-Hom set accepted a non-equivariant module map")

    adjunction = Modules(ZZ).trivial_invariants_adjunction(group)
    invariants = adjunction.right_adjoint()(acted)
    assert invariants.module_rank() == 1
    assert invariants.inclusion().is_in_image(e + f)

    source = ZZ.free_module(finite_ordered_set(("n",)))
    trivial_source = adjunction.left_adjoint()(source)
    equivariant = trivial_source.Mor(acted)(
        {"n": e + f}
    )
    transpose = adjunction.hom_set_isomorphism_forward(equivariant, source)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, acted)
    assert recovered(trivial_source.module_generator("n")) == equivariant(
        trivial_source.module_generator("n")
    )

    source_endomorphism = source.module_category().Mor(source, source)(
        {"n": 3 * source.module_generator("n")}
    )
    left, right = adjunction.unit_transformation().naturality_square(
        source_endomorphism
    )
    _assert_maps_agree(left, right, source.module_generators())

    acted_endomorphism = acted.Mor(acted)(
        {"e": 2 * e, "f": 2 * f}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, left.domain().module_generators())

    first_triangle = adjunction.right_adjoint()(adjunction.counit(acted)) * adjunction.unit(
        invariants
    )
    for generator in invariants.module_generators():
        assert first_triangle(generator) == generator

    second_triangle = adjunction.counit(trivial_source) * adjunction.left_adjoint()(
        adjunction.unit(source)
    )
    for generator in trivial_source.module_generators():
        assert second_triangle(generator) == generator


def test_coinvariants_are_left_adjoint_to_the_trivial_action() -> None:
    group, acted = _swap_group_module()
    e = acted.module_generator("e")
    f = acted.module_generator("f")
    adjunction = Modules(ZZ[group]).coinvariants_trivial_adjunction()
    coinvariants = adjunction.left_adjoint()(acted)

    assert coinvariants.module_rank() == 1
    unit = adjunction.unit(acted)
    assert unit(e) == unit(f)

    target = ZZ.free_module(finite_ordered_set(("n",)))
    quotient_map = coinvariants.module_category().Mor(coinvariants, target)(
        {
            "e": target.module_generator("n"),
            "f": target.module_generator("n"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(quotient_map, source=acted)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, target)
    for label in coinvariants.module_generating_set():
        assert recovered(coinvariants.module_generator(label)) == quotient_map(
            coinvariants.module_generator(label)
        )

    acted_endomorphism = acted.Mor(acted)(
        {"e": 2 * e, "f": 2 * f}
    )
    left, right = adjunction.unit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, acted.module_generators())

    target_endomorphism = target.module_category().Mor(target, target)(
        {"n": 3 * target.module_generator("n")}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        target_endomorphism
    )
    _assert_maps_agree(left, right, left.domain().module_generators())

    trivial_target = adjunction.right_adjoint()(target)
    first_triangle = adjunction.right_adjoint()(adjunction.counit(target)) * adjunction.unit(
        trivial_target
    )
    for generator in trivial_target.module_generators():
        assert first_triangle(generator) == generator

    second_triangle = adjunction.counit(coinvariants) * adjunction.left_adjoint()(
        adjunction.unit(acted)
    )
    for generator in coinvariants.module_generators():
        assert second_triangle(generator) == generator


def test_fraction_field_is_left_adjoint_to_ring_of_integers_with_embedding_naturality_and_triangles() -> None:
    field = QuadraticField(2, "a")
    order = field.ring_of_integers()
    adjunction = OwnedOrders().fraction_field_adjunction()
    fraction_field = adjunction.left_adjoint()
    ring_of_integers = adjunction.right_adjoint()

    assert fraction_field(order) is field
    assert ring_of_integers(field) is order

    identity = fraction_field(order).Mor(field).identity()
    restricted = adjunction.hom_set_isomorphism_forward(identity, order)
    recovered = adjunction.hom_set_isomorphism_inverse(restricted, field)
    for basis_element in order.integral_basis():
        assert restricted(basis_element) == basis_element
    assert recovered(field.primitive_element()) == field.primitive_element()

    conjugation = next(
        embedding
        for embedding in field.Mor(field).embeddings()
        if embedding(field.primitive_element()) != field.primitive_element()
    )
    left, right = adjunction.counit_transformation().naturality_square(conjugation)
    assert left(field.primitive_element()) == right(field.primitive_element())

    restricted_conjugation = ring_of_integers(conjugation)
    left, right = adjunction.unit_transformation().naturality_square(
        restricted_conjugation
    )
    for basis_element in order.integral_basis():
        assert left(basis_element) == right(basis_element)

    first_triangle = ring_of_integers(adjunction.counit(field)) * adjunction.unit(
        ring_of_integers(field)
    )
    for basis_element in order.integral_basis():
        assert first_triangle(basis_element) == basis_element

    second_triangle = adjunction.counit(fraction_field(order)) * fraction_field(
        adjunction.unit(order)
    )
    assert second_triangle(field.primitive_element()) == field.primitive_element()


def test_abelianization_is_left_adjoint_to_the_inclusion_of_abelian_groups() -> None:
    group = Groups.S(3)
    target = Groups.C(6)
    adjunction = Groups().abelianization_adjunction()
    abelianization = adjunction.left_adjoint()(group)

    assert abelianization.order() == 2
    assert abelianization.is_abelian()

    unit = adjunction.unit(group)
    group_generators = group.group_generators()
    assert unit(group_generators[0]) == abelianization.one()
    assert unit(group_generators[1]) != abelianization.one()

    target_generator = target.group_generators()[0]

    assert adjunction.right_adjoint()(target) is target
    sign_to_six = group.Mor(target)(
        {
            group_generators[0]: target.one(),
            group_generators[1]: target_generator**3,
        }
    )
    factored = adjunction.hom_set_isomorphism_inverse(sign_to_six, target)
    recovered = adjunction.hom_set_isomorphism_forward(factored, group)
    for generator in group_generators:
        assert recovered(generator) == sign_to_six(generator)

    conjugation = group.Aut().one()
    assert conjugation in group.Mor(group)
    left, right = adjunction.unit_transformation().naturality_square(conjugation)
    for generator in group_generators:
        assert left(generator) == right(generator)

    target_endomorphism = target.Mor(target)(
        {target_generator: target_generator**5}
    )
    left, right = adjunction.counit_transformation().naturality_square(
        target_endomorphism
    )
    for element in left.domain():
        assert left(element) == right(element)

    first_triangle = adjunction.right_adjoint()(adjunction.counit(target)) * adjunction.unit(
        adjunction.right_adjoint()(target)
    )
    for generator in target.group_generators():
        assert first_triangle(generator) == generator

    second_triangle = adjunction.counit(abelianization) * adjunction.left_adjoint()(
        adjunction.unit(group)
    )
    for element in abelianization:
        assert second_triangle(element) == element


def test_declared_inclusions_and_scalar_restriction_use_their_actual_functors() -> None:
    from dzack_research.preamble.all import FormModules

    group, acted = _swap_group_module()
    group_algebra = ZZ[group]
    group_modules = Modules(group_algebra)
    assert not group_modules.is_subcategory(Modules(ZZ))

    forget_action = group_modules.restriction_of_scalars(
        group_algebra.algebra_structure_morphism()
    )
    restricted = forget_action(acted)
    assert restricted is acted.unformed_module()

    doubled = acted.Mor(acted)(
        {
            "e": 2 * acted.module_generator("e"),
            "f": 2 * acted.module_generator("f"),
        }
    )
    restricted_doubled = forget_action(doubled)
    assert restricted_doubled.domain() is restricted
    assert restricted_doubled.codomain() is restricted
    assert restricted_doubled(restricted.module_generator("e")) == (
        2 * restricted.module_generator("e")
    )

    lattice = ZZ.free_module(finite_ordered_set(("x", "y")))
    from dzack_research.preamble.all import Lattices

    formed = lattice.equip_bilinear_form(ZZ, [[0, 1], [1, 0]])
    forget_form = FormModules(ZZ).inclusion_into(Modules(ZZ))
    assert forget_form(formed) is formed

    hyperbolic = Lattices(ZZ)("U")
    forget_lattice = Lattices(ZZ).inclusion_into(Modules(ZZ))
    assert forget_lattice(hyperbolic) is hyperbolic


def test_scalar_extension_restriction_lifts_to_group_modules_with_equivariance_and_triangles() -> None:
    group, acted = _swap_group_module()
    field = QuadraticField(2, "a")
    order = field.ring_of_integers()
    ring_map = order.algebra_structure_morphism()
    adjunction = Modules(ring_map.domain()[group]).coefficient_base_change_adjunction(ring_map)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    extended = extension(acted)
    assert acted.base_change(ring_map) is extended
    restricted = restriction(extended)
    assert restricted.module_generating_set().cardinality() == 4

    extended_identity = extended.Mor(extended)(
        {
            label: extended.module_generator(label)
            for label in extended.module_generating_set()
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(extended_identity, acted)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, extended)
    for generator in extended.module_generators():
        assert recovered(generator) == generator

    source_endomorphism = acted.Mor(acted)(
        {
            "e": 2 * acted.module_generator("e"),
            "f": 2 * acted.module_generator("f"),
        }
    )
    extended_source_endomorphism = extension(source_endomorphism)
    for generator in extended.module_generators():
        assert extended_source_endomorphism(generator) == 2 * generator

    left, right = adjunction.unit_transformation().naturality_square(
        source_endomorphism
    )
    _assert_maps_agree(left, right, acted.module_generators())

    target_endomorphism = extended.Mor(extended)(
        {
            "e": order(3) * extended.module_generator("e"),
            "f": order(3) * extended.module_generator("f"),
        }
    )
    left, right = adjunction.counit_transformation().naturality_square(
        target_endomorphism
    )
    _assert_maps_agree(left, right, left.domain().module_generators())

    first_triangle = restriction(adjunction.counit(extended)) * adjunction.unit(
        restricted
    )
    for generator in restricted.module_generators():
        assert first_triangle(generator) == generator

    second_triangle = adjunction.counit(extended) * extension(adjunction.unit(acted))
    for generator in extended.module_generators():
        assert second_triangle(generator) == generator


def test_free_and_scalar_extension_functors_preserve_identities_and_composition() -> None:
    free = Sets().free_module_adjunction(ZZ).left_adjoint()
    source_set = finite_ordered_set((ZZ(1), ZZ(2)))
    middle_set = finite_ordered_set((ZZ(3), ZZ(4)))
    target_set = finite_ordered_set((ZZ(5), ZZ(6)))
    identity = Sets().Mor(source_set, source_set)(lambda value: value)
    first = Sets().Mor(source_set, middle_set)(lambda value: ZZ(3) if value == 1 else ZZ(4))
    second = Sets().Mor(middle_set, target_set)(lambda value: ZZ(6) if value == 3 else ZZ(5))
    composite = Sets().Mor(source_set, target_set)(lambda value: second(first(value)))

    free_source = free(source_set)
    carried_identity = free(identity)
    for generator in free_source.module_generators():
        assert carried_identity(generator) == generator

    carried_composite = free(composite)
    composed_carried = free(second) * free(first)
    for generator in free_source.module_generators():
        assert carried_composite(generator) == composed_carried(generator)

    field = QuadraticField(2, "a")
    order = field.ring_of_integers()
    structure_map = order.algebra_structure_morphism()
    extension = Modules(structure_map.domain()).base_change_adjunction(
        structure_map
    ).left_adjoint()
    source = ZZ.free_module(finite_ordered_set(("a", "b")))
    middle = ZZ.free_module(finite_ordered_set(("c", "d")))
    target = ZZ.free_module(finite_ordered_set(("e",)))
    first_linear = source.module_category().Mor(source, middle)(
        {
            "a": middle.module_generator("c") + middle.module_generator("d"),
            "b": 2 * middle.module_generator("d"),
        }
    )
    second_linear = middle.module_category().Mor(middle, target)(
        {
            "c": 3 * target.module_generator("e"),
            "d": target.module_generator("e"),
        }
    )
    source_identity = source.module_category().Mor(source, source).identity()
    carried_identity = extension(source_identity)
    extended_source = extension(source)
    for generator in extended_source.module_generators():
        assert carried_identity(generator) == generator

    carried_composite = extension(second_linear * first_linear)
    composed_carried = extension(second_linear) * extension(first_linear)
    for generator in extended_source.module_generators():
        assert carried_composite(generator) == composed_carried(generator)


def test_tensor_symmetric_and_alternating_algebras_are_functorial_on_finite_free_modules() -> None:
    source = ZZ.free_module(finite_ordered_set(("x", "y")))
    middle = ZZ.free_module(finite_ordered_set(("u", "v")))
    target = ZZ.free_module(finite_ordered_set(("z",)))
    first = source.module_category().Mor(source, middle)(
        {
            "x": middle.module_generator("u") + middle.module_generator("v"),
            "y": 2 * middle.module_generator("v"),
        }
    )
    second = middle.module_category().Mor(middle, target)(
        {
            "u": 3 * target.module_generator("z"),
            "v": target.module_generator("z"),
        }
    )

    modules = Modules(ZZ)
    for functor in (
        modules.tensor_algebra(),
        modules.symmetric_algebra(),
        modules.exterior_algebra(),
    ):
        source_algebra = functor(source)
        middle_algebra = functor(middle)
        target_algebra = functor(target)
        carried_first = functor(first)
        carried_second = functor(second)

        x = source_algebra.algebra_generator("x")
        y = source_algebra.algebra_generator("y")
        u = middle_algebra.algebra_generator("u")
        v = middle_algebra.algebra_generator("v")
        z = target_algebra.algebra_generator("z")
        assert carried_first(x) == u + v
        assert carried_first(y) == 2 * v
        assert carried_second(u) == 3 * z
        assert carried_second(v) == z

        identity = source.module_category().Mor(source, source).identity()
        carried_identity = functor(identity)
        assert carried_identity(x) == x
        assert carried_identity(y) == y

        carried_composite = functor(second * first)
        composed_carried = carried_second * carried_first
        assert carried_composite(x) == composed_carried(x)
        assert carried_composite(y) == composed_carried(y)
