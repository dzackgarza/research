from sage.categories.sets_cat import Sets

from dzack_research.preamble.all import (
    BasedFreeModule,
    GroupModule,
    Groups,
    QuadraticField,
    ZZ,
    abelianization_adjunction,
    base_change_adjunction,
    category_inclusion,
    coinvariants_trivial_adjunction,
    free_forgetful_adjunction,
    group_module_base_change_adjunction,
    group_module_homset,
    module_homset,
    order_number_field_adjunction,
    trivial_invariants_adjunction,
    alternating_algebra_functor,
    symmetric_algebra_functor,
    tensor_algebra_functor,
)
from dzack_research.preamble.categories.rings.embeddings import number_field_homset
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_maps_agree(left, right, elements) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for element in elements:
        assert left(element) == right(element)


def _swap_group_module():
    group = Groups.C(2)
    module = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        coefficients = module_coefficients(vector, module)
        return module.linear_combination(
            {
                "e": coefficients.get("f", ZZ.zero()),
                "f": coefficients.get("e", ZZ.zero()),
            }
        )

    return group, GroupModule(module, group, swap)


def test_free_module_underlying_set_adjunction_has_the_hom_bijection_naturality_and_triangles() -> None:
    adjunction = free_forgetful_adjunction(ZZ)
    free = adjunction.left_adjoint()
    underlying = adjunction.right_adjoint()

    labels = finite_ordered_set(("x", "y"))
    module = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    free_labels = free(labels)
    phi = module_homset(free_labels, module)(
        {
            "x": module.module_generator("a") + module.module_generator("b"),
            "y": 2 * module.module_generator("a"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(phi)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, module)

    for label in labels:
        assert transpose(label) == phi(free_labels.module_generator(label))
        assert recovered(free_labels.module_generator(label)) == phi(
            free_labels.module_generator(label)
        )

    source_set = finite_ordered_set((ZZ(1), ZZ(2)))
    target_set = finite_ordered_set((ZZ(3), ZZ(4)))
    set_map = Sets().mor( sage.cate, ries.homse)(lambda value: ZZ(3) if value == 1 else ZZ(4))
    left, right = adjunction.unit_transformation().naturality_square(set_map)
    _assert_maps_agree(left, right, source_set)

    target_module = BasedFreeModule(ZZ, finite_ordered_set(("c",)))
    module_map = module_homset(module, target_module)(
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
    structure_map = order._ring_morphism_defining_algebra_structure()
    adjunction = base_change_adjunction(structure_map)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    source = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    target = BasedFreeModule(order, finite_ordered_set(("p",)))
    extended_source = extension(source)
    restricted_target = restriction(target)

    assert restricted_target.module_generating_set().cardinality() == 2
    phi = module_homset(extended_source, target)(
        {
            "u": target.module_generator("p"),
            "v": order(2) * target.module_generator("p"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(phi)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose)
    for label in source.module_generating_set():
        assert recovered(extended_source.module_generator(label)) == phi(
            extended_source.module_generator(label)
        )

    second_source = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    source_map = module_homset(source, second_source)(
        {
            "u": second_source.module_generator("r"),
            "v": 2 * second_source.module_generator("r"),
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(source_map)
    _assert_maps_agree(left, right, source.module_generators())

    second_target = BasedFreeModule(order, finite_ordered_set(("q",)))
    target_map = module_homset(target, second_target)(
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
        group_module_homset(acted, acted)(
            {"e": e, "f": e}
        )
    except ValueError as error:
        assert "not G-equivariant" in str(error)
    else:
        raise AssertionError("an R[G]-Hom set accepted a non-equivariant module map")

    adjunction = trivial_invariants_adjunction(ZZ, group)
    invariants = adjunction.right_adjoint()(acted)
    assert invariants.rank() == 1
    assert invariants.inclusion().is_in_image(e + f)

    source = BasedFreeModule(ZZ, finite_ordered_set(("n",)))
    trivial_source = adjunction.left_adjoint()(source)
    equivariant = group_module_homset(trivial_source, acted)(
        {"n": e + f}
    )
    transpose = adjunction.hom_set_isomorphism_forward(equivariant)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, acted)
    assert recovered(trivial_source.module_generator("n")) == equivariant(
        trivial_source.module_generator("n")
    )

    source_endomorphism = module_homset(source, source)(
        {"n": 3 * source.module_generator("n")}
    )
    left, right = adjunction.unit_transformation().naturality_square(
        source_endomorphism
    )
    _assert_maps_agree(left, right, source.module_generators())

    acted_endomorphism = group_module_homset(acted, acted)(
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
    adjunction = coinvariants_trivial_adjunction(ZZ, group)
    coinvariants = adjunction.left_adjoint()(acted)

    assert coinvariants.rank() == 1
    unit = adjunction.unit(acted)
    assert unit(e) == unit(f)

    target = BasedFreeModule(ZZ, finite_ordered_set(("n",)))
    quotient_map = module_homset(coinvariants, target)(
        {
            "e": target.module_generator("n"),
            "f": target.module_generator("n"),
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(quotient_map, source=acted)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose)
    for label in coinvariants.module_generating_set():
        assert recovered(coinvariants.module_generator(label)) == quotient_map(
            coinvariants.module_generator(label)
        )

    acted_endomorphism = group_module_homset(acted, acted)(
        {"e": 2 * e, "f": 2 * f}
    )
    left, right = adjunction.unit_transformation().naturality_square(
        acted_endomorphism
    )
    _assert_maps_agree(left, right, acted.module_generators())

    target_endomorphism = module_homset(target, target)(
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
    adjunction = order_number_field_adjunction()
    fraction_field = adjunction.left_adjoint()
    ring_of_integers = adjunction.right_adjoint()

    assert fraction_field(order) is field
    assert ring_of_integers(field) is order

    identity = number_field_homset(fraction_field(order), field).identity()
    restricted = adjunction.hom_set_isomorphism_forward(identity, order)
    recovered = adjunction.hom_set_isomorphism_inverse(restricted)
    for basis_element in order.integral_basis():
        assert restricted(basis_element) == basis_element
    assert recovered(field.primitive_element()) == field.primitive_element()

    conjugation = next(
        embedding
        for embedding in number_field_homset(field, field).embeddings()
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
    adjunction = abelianization_adjunction()
    abelianization = adjunction.left_adjoint()(group)

    assert abelianization.order() == 2
    assert abelianization.is_abelian()

    unit = adjunction.unit(group)
    group_generators = group.group_generators()
    assert unit(group_generators[0]) == abelianization.one()
    assert unit(group_generators[1]) != abelianization.one()

    target_generator = target.group_generators().unrank(0)
    from dzack_research.preamble.categories.group import group_homset

    sign_to_six = group_homset(group, target)(
        {
            group_generators[0]: target.one(),
            group_generators[1]: target_generator**3,
        }
    )
    factored = adjunction.hom_set_isomorphism_inverse(sign_to_six)
    recovered = adjunction.hom_set_isomorphism_forward(factored)
    for generator in group_generators:
        assert recovered(generator) == sign_to_six(generator)

    conjugation = group.Aut().one()
    left, right = adjunction.unit_transformation().naturality_square(conjugation)
    for generator in group_generators:
        assert left(generator) == right(generator)

    target_endomorphism = group_homset(target, target)(
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


def test_declared_subcategory_edges_give_canonical_inclusion_functors() -> None:
    from dzack_research.preamble.all import FormModules, GroupModules, Modules

    group, acted = _swap_group_module()
    forget_action = category_inclusion(GroupModules(ZZ, group), Modules(ZZ))
    assert forget_action(acted) is acted

    doubled = group_module_homset(acted, acted)(
        {
            "e": 2 * acted.module_generator("e"),
            "f": 2 * acted.module_generator("f"),
        }
    )
    assert forget_action(doubled) is doubled
    assert forget_action(doubled)(acted.module_generator("e")) == 2 * acted.module_generator("e")

    lattice = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    from dzack_research.preamble.all import BilinearForm, Lattices

    formed = BilinearForm(lattice, ZZ, [[0, 1], [1, 0]])
    forget_form = category_inclusion(FormModules(ZZ), Modules(ZZ))
    assert forget_form(formed) is formed

    hyperbolic = Lattices(ZZ)("U")
    forget_lattice = category_inclusion(Lattices(ZZ), Modules(ZZ))
    assert forget_lattice(hyperbolic) is hyperbolic


def test_scalar_extension_restriction_lifts_to_group_modules_with_equivariance_and_triangles() -> None:
    group, acted = _swap_group_module()
    field = QuadraticField(2, "a")
    order = field.ring_of_integers()
    ring_map = order._ring_morphism_defining_algebra_structure()
    adjunction = group_module_base_change_adjunction(ring_map, group)
    extension = adjunction.left_adjoint()
    restriction = adjunction.right_adjoint()

    extended = extension(acted)
    restricted = restriction(extended)
    assert restricted.module_generating_set().cardinality() == 4

    extended_identity = group_module_homset(extended, extended)(
        {
            label: extended.module_generator(label)
            for label in extended.module_generating_set()
        }
    )
    transpose = adjunction.hom_set_isomorphism_forward(extended_identity)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose)
    for generator in extended.module_generators():
        assert recovered(generator) == generator

    source_endomorphism = group_module_homset(acted, acted)(
        {
            "e": 2 * acted.module_generator("e"),
            "f": 2 * acted.module_generator("f"),
        }
    )
    left, right = adjunction.unit_transformation().naturality_square(
        source_endomorphism
    )
    _assert_maps_agree(left, right, acted.module_generators())

    target_endomorphism = group_module_homset(extended, extended)(
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
    free = free_forgetful_adjunction(ZZ).left_adjoint()
    source_set = finite_ordered_set((ZZ(1), ZZ(2)))
    middle_set = finite_ordered_set((ZZ(3), ZZ(4)))
    target_set = finite_ordered_set((ZZ(5), ZZ(6)))
    identity = Sets().mor( sage.cate, ries.homse)(lambda value: value)
    first = Sets().mor( sage.cate, ries.homse)(lambda value: ZZ(3) if value == 1 else ZZ(4))
    second = Sets().mor( sage.cate, ries.homse)(lambda value: ZZ(6) if value == 3 else ZZ(5))
    composite = Sets().mor( sage.cate, ries.homse)(lambda value: second(first(value)))

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
    extension = base_change_adjunction(
        order._ring_morphism_defining_algebra_structure()
    ).left_adjoint()
    source = BasedFreeModule(ZZ, finite_ordered_set(("a", "b")))
    middle = BasedFreeModule(ZZ, finite_ordered_set(("c", "d")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    first_linear = module_homset(source, middle)(
        {
            "a": middle.module_generator("c") + middle.module_generator("d"),
            "b": 2 * middle.module_generator("d"),
        }
    )
    second_linear = module_homset(middle, target)(
        {
            "c": 3 * target.module_generator("e"),
            "d": target.module_generator("e"),
        }
    )
    source_identity = module_homset(source, source).identity()
    carried_identity = extension(source_identity)
    extended_source = extension(source)
    for generator in extended_source.module_generators():
        assert carried_identity(generator) == generator

    carried_composite = extension(second_linear * first_linear)
    composed_carried = extension(second_linear) * extension(first_linear)
    for generator in extended_source.module_generators():
        assert carried_composite(generator) == composed_carried(generator)


def test_tensor_symmetric_and_alternating_algebras_are_functorial_on_finite_free_modules() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    middle = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("z",)))
    first = module_homset(source, middle)(
        {
            "x": middle.module_generator("u") + middle.module_generator("v"),
            "y": 2 * middle.module_generator("v"),
        }
    )
    second = module_homset(middle, target)(
        {
            "u": 3 * target.module_generator("z"),
            "v": target.module_generator("z"),
        }
    )

    for functor in (
        tensor_algebra_functor(ZZ),
        symmetric_algebra_functor(ZZ),
        alternating_algebra_functor(ZZ),
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

        identity = module_homset(source, source).identity()
        carried_identity = functor(identity)
        assert carried_identity(x) == x
        assert carried_identity(y) == y

        carried_composite = functor(second * first)
        composed_carried = carried_second * carried_first
        assert carried_composite(x) == composed_carried(x)
        assert carried_composite(y) == composed_carried(y)
