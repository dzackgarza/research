r"""Universal constructions a mathematician expects in every category the session owns.

Products, coproducts, biproducts, kernels, cokernels, pushouts, fiber
products and subobject categories in sets, modules over every ring, and
groups; slices, coslices, opposites, products of categories, functor
categories, natural transformations, cores, and the Hom, End, Aut, Mono, Epi
and Iso constructions.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Limits and colimits in Sets.
# ---------------------------------------------------------------------------


def test_products_and_coproducts_of_finite_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    product = Product(two, three)
    coproduct = Coproduct(two, three)

    assert product.cardinality() == 6
    assert product in Sets()
    assert product.projection(0).codomain() is two
    assert product.projection(1).codomain() is three
    assert coproduct.cardinality() == 5
    assert coproduct.injection(0).domain() is two
    assert coproduct.injection(1).domain() is three
    assert Product(Product(three, three), three).cardinality() == 27
    one = Sets.Δ[0]
    assert Product(one, three).cardinality() == 3
    assert Coproduct(one, three).cardinality() == 4


def test_the_universal_property_of_the_product_of_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    product = Product(two, three)
    first = Sets().Mor(three, two)(lambda point: two(int(point) % 2))
    second = Sets().Mor(three, three).identity()
    induced = product.from_maps(three, {0: first, 1: second})
    assert induced.domain() is three
    assert induced.codomain() is product
    assert product.projection(0) * induced == first
    assert product.projection(1) * induced == second


def test_pushouts_and_fiber_products_of_finite_sets() -> None:
    one = Sets.Δ[0]
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    into_two = Sets().Mor(one, two)(lambda point: two(0))
    into_three = Sets().Mor(one, three)(lambda point: three(0))
    glued = Pushout(into_two, into_three)
    assert glued.cardinality() == 4

    onto_one_from_two = Sets().Mor(two, one)(lambda point: one(0))
    onto_one_from_three = Sets().Mor(three, one)(lambda point: one(0))
    pulled_back = FiberProduct(onto_one_from_two, onto_one_from_three)
    assert pulled_back.cardinality() == 6
    assert pulled_back.left_projection().codomain() is two


def test_subobjects_of_a_finite_set_form_its_power_set() -> None:
    three = Sets.Δ[2]
    subobjects = Subobjects(three)
    assert subobjects in Cat()
    assert subobjects.cardinality() == 8
    assert SubobjectsOf(Sets(), three).cardinality() == 8


# ---------------------------------------------------------------------------
# Limits and colimits in modules over every ring.
# ---------------------------------------------------------------------------


def test_products_coproducts_and_biproducts_of_modules(commutative_ring) -> None:
    ring = commutative_ring
    left = FreeModule(ring, 2)
    right = FreeModule(ring, 3)
    for construction in (Product, Coproduct, Biproduct):
        both = construction(left, right)
        assert both in Modules(ring)
        assert both.module_rank() == 5
    assert left.tensor_product(right).module_rank() == 6
    assert Product(left, right) == Coproduct(left, right)


def test_kernels_and_cokernels_of_module_morphisms(commutative_ring) -> None:
    ring = commutative_ring
    plane = FreeModule(ring, 2)
    line = FreeModule(ring, 1)
    projection = plane.Mor(line)({0: line.module_generator(0), 1: line.zero()})
    doubling = line.Mor(line)({0: 2 * line.module_generator(0)})

    assert Kernel(projection).module_rank() == 1
    assert Kernel(projection).inclusion().codomain() is plane
    assert Cokernel(projection).cardinality() == 1
    assert Cokernel(doubling).cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality()
    assert Cokernel(doubling).projection().domain() is line
    assert Kernel(doubling).module_rank() == (1 if ring(2) == ring.zero() else 0)


def test_pushouts_and_fiber_products_of_modules(commutative_ring) -> None:
    ring = commutative_ring
    line = FreeModule(ring, 1)
    plane = FreeModule(ring, 2)
    first_axis = line.Mor(plane)({0: plane.module_generator(0)})
    second_axis = line.Mor(plane)({0: plane.module_generator(1)})
    glued = Pushout(first_axis, first_axis)
    assert glued in Modules(ring)
    assert glued.module_rank() == 3
    first_projection = plane.Mor(line)({0: line.module_generator(0), 1: line.zero()})
    pulled_back = FiberProduct(first_projection, first_projection)
    assert pulled_back in Modules(ring)
    assert pulled_back.module_rank() == 3
    assert Pushout(first_axis, second_axis).module_rank() == 3


def test_subobjects_of_a_module_form_a_category(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    subobjects = Subobjects(module)
    line = module.subobject_on([module.module_generator(0)])
    assert subobjects in Cat()
    assert line in subobjects
    assert line in SubobjectsOf(Modules(ring), module)
    assert subobjects.Mor(line, line).identity()(line.module_generator(0)) == line.module_generator(0)


# ---------------------------------------------------------------------------
# Limits and colimits in groups.
# ---------------------------------------------------------------------------


def test_products_coproducts_kernels_and_cokernels_of_groups() -> None:
    symmetric = Groups.S(3)
    two = Groups.C(2)
    three = Groups.C(3)
    product = Product(symmetric, two)
    free_product = Coproduct(two, three)
    sign = symmetric.Mor(two)(
        {g: (two.group_generators().unrank(0) if g.order() == 2 else two.one()) for g in symmetric.group_generators()}
    )

    assert product in Groups()
    assert product.order() == 12
    assert not product.is_abelian()
    assert free_product in Groups()
    assert free_product not in FiniteGroups()
    assert free_product.cardinality() == aleph0
    assert Kernel(sign).order() == 3
    assert Kernel(sign).is_abelian()
    assert Cokernel(Kernel(sign).inclusion()).order() == 2
    assert Cokernel(sign).order() == 1
    assert Product(two, three).is_isomorphic_to(Groups.C(6))


def test_subgroups_of_the_symmetric_group_form_a_category() -> None:
    symmetric = Groups.S(3)
    subgroups = Subobjects(symmetric)
    assert subgroups in Cat()
    assert subgroups.cardinality() == 6
    assert Subobjects(Groups.C(6)).cardinality() == 4
    assert Subobjects(Groups.Q()).cardinality() == 6


# ---------------------------------------------------------------------------
# Categories built from categories.
# ---------------------------------------------------------------------------


def test_slices_coslices_opposites_products_and_functor_categories() -> None:
    module = FreeModule(ZZ, 2)
    for category in (
        SliceOver(Modules(ZZ), module),
        CosliceUnder(OwnedRings(), ZZ),
        OppositeCategory(Sets()),
        ProductCategory(Sets(), Groups()),
        FunctorCategory(Sets(), Sets()),
        Core(Sets()),
        Modules(ZZ),
        Sets(),
        Groups(),
    ):
        assert category in Cat()
    assert module.subobject_on([module.module_generator(0)]) in SliceOver(Modules(ZZ), module)
    assert Sets.Δ[2] in OppositeCategory(Sets())
    assert Sets().identity_functor() in FunctorCategory(Sets(), Sets())
    assert Fields() in Cat()
    assert Cat() in Cat()


def test_identity_and_inclusion_functors() -> None:
    identity = Sets().identity_functor()
    three = Sets.Δ[2]
    assert identity(three) is three
    assert identity(Sets().Mor(three, three).identity()) == Sets().Mor(three, three).identity()
    inclusion = category_inclusion(Fields(), CommutativeRings())
    assert inclusion(QQ) is QQ
    assert inclusion.domain() is Fields()
    assert inclusion.codomain() is CommutativeRings()
    assert category_inclusion(AbelianGroups(), Groups())(Groups.C(4)) is Groups.C(4)


def test_natural_transformations_between_functors() -> None:
    identity = Sets().identity_functor()
    transformations = NaturalTransformations(identity, identity)
    assert transformations in Sets()
    three = Sets.Δ[2]
    unit = transformations.identity()
    assert unit.component(three) == Sets().Mor(three, three).identity()
    left, right = unit.naturality_square(Sets().Mor(three, three).identity())
    assert left == right


def test_isomorphisms_and_the_core() -> None:
    two = Sets.Δ[1]
    swap = Sets().Mor(two, two)(lambda point: two(1 - int(point)))
    isomorphism = Isomorphism(swap, swap)
    assert isomorphism in IsoCategoryOf(Sets()).Of(two, two)
    assert isomorphism in Core(Sets()).Mor(two, two)
    assert isomorphism.inverse() * isomorphism == IsoCategoryOf(Sets()).Of(two, two).identity()
    assert IsoCategoryOf(Sets()).Of(two, two).cardinality() == 2
    assert Core(Sets()).Mor(two, Sets.Δ[2]).cardinality() == 0


def test_hom_end_aut_mono_epi_constructions_on_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    assert HomCategoryOf(Sets()).Of(two, three) is Sets().Mor(two, three)
    assert HomCategoryOf(Sets()).Of(two, three).cardinality() == 9
    assert EndCategoryOf(Sets()).Of(three).cardinality() == 27
    assert AutCategoryOf(Sets()).Of(three).order() == 6
    assert AutCategoryOf(Sets()).Of(three) in Groups()
    assert MonoCategoryOf(Sets()).Of(two, three).cardinality() == 6
    assert EpiCategoryOf(Sets()).Of(three, two).cardinality() == 6
    assert EpiCategoryOf(Sets()).Of(two, three).cardinality() == 0
    assert IsoCategoryOf(Sets()).Of(two, three).cardinality() == 0


def test_hom_end_aut_constructions_on_modules_over_a_field(field) -> None:
    plane = FreeModule(field, 2)
    endomorphisms = EndCategoryOf(Modules(field)).Of(plane)
    automorphisms = AutCategoryOf(Modules(field)).Of(plane)
    assert endomorphisms in Cat()
    assert automorphisms in Groups()
    assert endomorphisms.identity() in automorphisms
    if field.cardinality().is_finite():
        q = field.cardinality()
        assert endomorphisms.cardinality() == q**4
        assert automorphisms.order() == (q**2 - 1) * (q**2 - q)
    else:
        assert automorphisms.cardinality() == field.cardinality()


def test_direct_sum_objects_know_their_summands() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    assert lattice in DirectSumObjects()
    assert lattice.number_of_summands() == 2
    assert lattice.summands().cardinality() == 2
    assert lattice.summand(0).module_rank() == 2
    assert lattice.summand(1).determinant() == 3
