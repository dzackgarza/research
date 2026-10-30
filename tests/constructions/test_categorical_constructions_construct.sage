r"""Universal constructions a mathematician expects in every category the session owns.

Products, coproducts, biproducts, kernels, cokernels, pushouts, fiber
products and subobject categories in sets, modules over every ring, and
groups; slices, coslices, opposites, products of categories, functor
categories, natural transformations, cores, and the Hom, End, Aut, Mono, Epi
and Iso constructions.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403
from sage_extensions.categories.group.groups import OwnedAbelianGroups, OwnedGroups
from sage_extensions.categories.modules.pure.modules import Modules

# ---------------------------------------------------------------------------
# Limits and colimits in Sets.
# ---------------------------------------------------------------------------


def test_products_and_coproducts_of_finite_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    sets = Sets()
    product = sets.product((two, three))
    coproduct = sets.coproduct((two, three))

    assert product.cardinality() == cardinal(6)
    assert product in Sets()
    assert product.projection(0).codomain() is two
    assert product.projection(1).codomain() is three
    assert coproduct.cardinality() == cardinal(5)
    assert coproduct.injection(0).domain() is two
    assert coproduct.injection(1).domain() is three
    assert sets.product((sets.product((three, three)), three)).cardinality() == cardinal(27)
    one = Sets.Δ[0]
    assert sets.product((one, three)).cardinality() == cardinal(3)
    assert sets.coproduct((one, three)).cardinality() == cardinal(4)


def test_the_universal_property_of_the_product_of_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    product = Sets().product((two, three))
    first = Sets().Mor(three, two)(lambda point: two(int(point) % 2))
    second = Sets().Mor(three, three).identity()
    induced = product.from_maps(
        three,
        lambda index: first if int(index) == 0 else second,
    )
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
    glued = Sets().pushout(into_two, into_three)
    assert glued.cardinality() == cardinal(4)

    onto_one_from_two = Sets().Mor(two, one)(lambda point: one(0))
    onto_one_from_three = Sets().Mor(three, one)(lambda point: one(0))
    pulled_back = Sets().fiber_product(onto_one_from_two, onto_one_from_three)
    assert pulled_back.cardinality() == cardinal(6)
    assert pulled_back.left_projection().codomain() is two


def test_subobjects_of_a_finite_set_form_its_power_set() -> None:
    three = Sets.Δ[2]
    subobjects = Sets().Subobjects(three)
    singleton = three.power_set()((three(0),))
    pair = three.power_set()((three(0), three(1)))
    assert subobjects in Cat()
    assert subobjects.cardinality() == cardinal(8)
    assert Sets().Subobjects(three).cardinality() == cardinal(8)
    assert singleton in subobjects
    assert singleton.inclusion().codomain() is three
    assert singleton.underlying_set() is singleton.inclusion().domain()
    assert singleton.category() is subobjects
    factor = subobjects.Mor(singleton, pair)
    assert factor.domain() is singleton
    assert factor.codomain() is pair
    assert factor(singleton.inclusion().factor_through(pair.inclusion())).left().domain() is singleton.underlying_set()

    four = Sets.Δ[3]
    same_points = four.power_set()((four(0),))
    assert same_points.inclusion().codomain() is four
    assert singleton != same_points
    assert singleton.inclusion() != same_points.inclusion()


# ---------------------------------------------------------------------------
# Limits and colimits in modules over every ring.
# ---------------------------------------------------------------------------


def test_products_coproducts_and_biproducts_of_modules(commutative_ring) -> None:
    ring = commutative_ring
    left = ring.free_module(2)
    right = ring.free_module(3)
    modules = Modules(ring)
    for both in (
        modules.product((left, right)),
        modules.coproduct((left, right)),
        modules.biproduct((left, right)),
    ):
        assert both in Modules(ring)
        assert both.module_rank() == cardinal(5)
    assert left.tensor_product(right).module_rank() == cardinal(6)
    assert modules.product((left, right)) == modules.coproduct((left, right))


def test_kernels_and_cokernels_of_module_morphisms(commutative_ring) -> None:
    ring = commutative_ring
    plane = ring.free_module(2)
    line = ring.free_module(1)
    projection = plane.Mor(line)({0: line.module_generator(0), 1: line.zero()})
    doubling = line.Mor(line)({0: 2 * line.module_generator(0)})

    assert projection.kernel().module_rank() == cardinal(1)
    assert projection.kernel().inclusion().codomain() is plane
    assert projection.cokernel().cardinality() == cardinal(1)
    assert doubling.cokernel().cardinality() == ring.quotient_ring(ring.ideal(ring(2))).cardinality()
    assert doubling.cokernel().projection().domain() is line
    assert doubling.kernel().module_rank() == cardinal(1 if ring(2) == ring.zero() else 0)


def test_pushouts_and_fiber_products_of_modules(commutative_ring) -> None:
    ring = commutative_ring
    line = ring.free_module(1)
    plane = ring.free_module(2)
    first_axis = line.Mor(plane)({0: plane.module_generator(0)})
    second_axis = line.Mor(plane)({0: plane.module_generator(1)})
    glued = Modules(ring).pushout(first_axis, first_axis)
    assert glued in Modules(ring)
    assert glued.module_rank() == cardinal(3)
    first_projection = plane.Mor(line)({0: line.module_generator(0), 1: line.zero()})
    pulled_back = Modules(ring).fiber_product(first_projection, first_projection)
    assert pulled_back in Modules(ring)
    assert pulled_back.module_rank() == cardinal(3)
    assert Modules(ring).pushout(first_axis, second_axis).module_rank() == cardinal(3)


def test_subobjects_of_a_module_form_a_category(commutative_ring) -> None:
    ring = commutative_ring
    module = ring.free_module(2)
    subobjects = Modules(ring).Subobjects(module)
    line = module.subobject_on([module.module_generator(0)])
    assert subobjects in Cat()
    assert line in subobjects
    assert line in Modules(ring).Subobjects(module)
    assert subobjects.Mor(line, line).identity()(line.module_generator(0)) == line.module_generator(0)


# ---------------------------------------------------------------------------
# Limits and colimits in groups.
# ---------------------------------------------------------------------------


def test_products_coproducts_kernels_and_cokernels_of_groups() -> None:
    symmetric = OwnedGroups().S(3)
    two = OwnedGroups().C(2)
    three = OwnedGroups().C(3)
    groups = OwnedGroups()
    product = groups.product((symmetric, two))
    free_product = groups.coproduct((two, three))
    sign = symmetric.Mor(two)(
        {g: (two.group_generators()[0] if g.order() == 2 else two.one()) for g in symmetric.group_generators()}
    )

    assert product in OwnedGroups()
    assert product.order() == 12
    assert not product.is_abelian()
    assert free_product in OwnedGroups()
    assert free_product not in FiniteGroups()
    assert free_product.cardinality() == aleph0
    assert sign.kernel().order() == 3
    assert sign.kernel().is_abelian()
    assert sign.kernel().inclusion().cokernel().order() == 2
    assert sign.cokernel().order() == 1
    assert groups.product((two, three)).is_isomorphic_to(OwnedGroups().C(6))


def test_subgroups_of_the_symmetric_group_form_a_category() -> None:
    symmetric = OwnedGroups().S(3)
    subgroups = OwnedGroups().Subobjects(symmetric)
    assert subgroups in Cat()
    assert subgroups.cardinality() == cardinal(6)
    assert OwnedGroups().Subobjects(OwnedGroups().C(6)).cardinality() == cardinal(4)
    assert OwnedGroups().Subobjects(OwnedGroups().Q()).cardinality() == cardinal(6)


# ---------------------------------------------------------------------------
# Categories built from categories.
# ---------------------------------------------------------------------------


def test_slices_coslices_opposites_products_and_functor_categories() -> None:
    module = ZZ.free_module(2)
    for category in (
        Modules(ZZ).SliceOver(module),
        OwnedRings().CosliceUnder(ZZ),
        Sets().opposite(),
        Cat().product((Sets(), OwnedGroups())),
        Cat().Mor(Sets(), Sets()),
        Sets().Core(),
        Modules(ZZ),
        Sets(),
        OwnedGroups(),
    ):
        assert category in Cat()
    assert module.subobject_on([module.module_generator(0)]) in Modules(ZZ).SliceOver(module)
    assert Sets.Δ[2] in Sets().opposite()
    functor_category = Cat().Mor(Sets(), Sets())
    assert functor_category(Sets().identity_functor()) in functor_category
    assert Fields() in Cat()
    assert Cat() in Cat()


def test_all_cat_construction_accessors_build_owned_categories() -> None:
    r"""Each of the 21 Cat-carried accessors builds its selected category on the supplied data."""
    groups = OwnedGroups()
    group = OwnedGroups().C(2)
    symmetric = OwnedGroups().S(3)
    labels = Sets.Δ[1]
    index = PosetCategory(labels, le=lambda left, right: int(left) <= int(right))
    diagrams = groups.Diagram(index)
    diagram = diagrams.constant_functor(group)
    sign = symmetric.Mor(group)(
        {
            generator: (
                group.group_generators()[0]
                if generator.order() == 2
                else group.one()
            )
            for generator in symmetric.group_generators()
        }
    )
    modules = Modules(ZZ)
    module = ZZ.free_module(1)

    arrow = groups.Arrow()
    iso_arrow = groups.IsoArrow()
    core = groups.core()
    directed = groups.DirectedSystem(index)
    inverse = groups.InverseSystem(index)
    cone = groups.Cone(diagram)
    cocone = groups.Cocone(diagram)
    product = groups.Product((group, group))
    coproduct = groups.Coproduct((group, group))
    biproduct = modules.Biproduct((module, module))
    direct_sum = modules.DirectSum()
    tensor_product = modules.TensorProduct((module, module))
    slice_category = groups.SliceOver(group)
    coslice_category = groups.CosliceUnder(group)
    subobjects = groups.SubObject(symmetric)
    superobjects = groups.SuperObject(group)
    covering_objects = groups.CoveringObject(group)
    covered_objects = groups.CoveredObject(symmetric)
    kernels = groups.Kernel(sign)
    cokernels = groups.Cokernel(sign)
    identity_group = groups.Mor(group, group).identity()
    identity_symmetric = groups.Mor(symmetric, symmetric).identity()
    arrow_object = arrow(sign)
    iso_arrow_object = iso_arrow(identity_group)
    core_identity = core.Mor(group, group)(identity_group, identity_group)
    directed_diagram = directed.constant_functor(group)
    inverse_diagram = inverse.constant_functor(group)
    cone_object = cone.cone(group, lambda _index: identity_group)
    cocone_object = cocone.cocone(group, lambda _index: identity_group)
    slice_object = slice_category(identity_group)
    coslice_object = coslice_category(identity_group)
    superobject = superobjects(identity_group)
    covering_object = covering_objects(identity_group)
    covered_object = covered_objects(identity_symmetric)
    kernel_object = sign.kernel()
    cokernel_object = sign.cokernel()

    construction_names = (
        "Arrow",
        "IsoArrow",
        "core",
        "Diagram",
        "DirectedSystem",
        "InverseSystem",
        "Cone",
        "Cocone",
        "Product",
        "Coproduct",
        "Biproduct",
        "DirectSum",
        "TensorProduct",
        "SliceOver",
        "CosliceUnder",
        "SubObject",
        "SuperObject",
        "CoveringObject",
        "CoveredObject",
        "Kernel",
        "Cokernel",
    )
    constructions = (
        arrow,
        iso_arrow,
        core,
        diagrams,
        directed,
        inverse,
        cone,
        cocone,
        product,
        coproduct,
        biproduct,
        direct_sum,
        tensor_product,
        slice_category,
        coslice_category,
        subobjects,
        superobjects,
        covering_objects,
        covered_objects,
        kernels,
        cokernels,
    )
    for name, construction in zip(construction_names, constructions, strict=True):
        assert construction in Cat(), f"{name} returned {construction}, not an object of Cat()"
    assert diagrams is Cat().Mor(index, groups)
    assert diagram.domain() is index
    assert diagram.codomain() is groups
    assert arrow_object in arrow
    assert iso_arrow_object in iso_arrow
    assert group in core
    assert core_identity == core.identity(group)
    assert directed_diagram in directed
    assert directed_diagram.domain() is index
    assert inverse_diagram in inverse
    assert inverse_diagram.domain() is index.opposite()
    assert directed.index_category() is index
    assert inverse.base_index_category() is index
    assert cone.diagram() is diagram
    assert cocone.diagram() is diagram
    assert cone_object in cone
    assert cone_object.diagram() is diagram
    assert cocone_object in cocone
    assert cocone_object.diagram() is diagram
    print("CAT-370: diagram and cone constructors passed", flush=True)
    product_construction = groups.product_construction((group, group))
    assert product_construction.diagram() is product.diagram()
    product_cone = product.cone(
        group, lambda _index: groups.Mor(group, group).identity()
    )
    product_factor = product_construction.factor(product_cone)
    assert product_construction.cone() in product.diagram().Cones()
    assert product_cone in product
    assert product_factor.apex_map().domain() is group
    assert product_factor.apex_map().codomain() is product_construction.object()
    for index_object in product.diagram().domain().objects():
        assert (
            product_construction.structure_morphism(index_object)
            * product_factor.apex_map()
            == product_cone.structure_morphism(index_object)
        )
    print("CAT-370: product universal property passed", flush=True)

    print("CAT-370: before selected coproduct construction", flush=True)
    coproduct_construction = groups.coproduct_construction((group, group))
    assert coproduct_construction.diagram() is coproduct.diagram()
    print("CAT-370: selected coproduct construction passed", flush=True)
    coproduct_cocone = coproduct.cocone(
        group, lambda _index: groups.Mor(group, group).identity()
    )
    coproduct_factor = coproduct_construction.factor(coproduct_cocone)
    assert coproduct_construction.cocone() in coproduct.diagram().Cocones()
    assert coproduct_cocone in coproduct
    assert coproduct_factor.apex_map().domain() is coproduct_construction.object()
    assert coproduct_factor.apex_map().codomain() is group
    for index_object in coproduct.diagram().domain().objects():
        assert (
            coproduct_factor.apex_map()
            * coproduct_construction.costructure_morphism(index_object)
            == coproduct_cocone.costructure_morphism(index_object)
        )
    print("CAT-370: coproduct universal property passed", flush=True)

    module_two = ZZ.free_module(2)
    biproduct_object = modules.biproduct((module, module_two))
    print("CAT-370: biproduct constructed", flush=True)
    assert biproduct is biproduct_object.category()
    assert biproduct_object.biproduct_factor(0) is module
    assert biproduct_object.biproduct_factor(1) is module_two
    assert (
        biproduct_object.projection(0) * biproduct_object.injection(0)
        == modules.Mor(module, module).identity()
    )
    assert (
        biproduct_object.projection(1) * biproduct_object.injection(1)
        == modules.Mor(module_two, module_two).identity()
    )
    print("CAT-370: biproduct maps passed", flush=True)

    print("CAT-370: before direct-sum verification", flush=True)
    direct_sum_object = direct_sum.verify_decomposition(
        biproduct_object, (module, module_two)
    )
    print("CAT-370: direct-sum verification passed", flush=True)
    assert direct_sum.base_category() is modules
    assert direct_sum_object in direct_sum
    assert direct_sum_object.summand(0) is module
    assert direct_sum_object.summand(1) is module_two
    assert direct_sum_object.injection(0).codomain() is direct_sum_object
    assert direct_sum_object.projection(0).domain() is direct_sum_object

    print("CAT-370: before tensor product", flush=True)
    tensor_product_object = modules.tensor_product((module, module_two))
    print("CAT-370: tensor product constructed", flush=True)
    assert tensor_product is tensor_product_object.category()
    assert tensor_product_object.tensor_factor(0) is module
    assert tensor_product_object.tensor_factor(1) is module_two
    assert (
        tensor_product_object.pure_tensor(
            module.module_generator(0), module_two.module_generator(0)
        )
        in tensor_product_object
    )
    print("CAT-370: pure tensor passed", flush=True)
    assert slice_object in slice_category
    assert slice_category.arrow(slice_object) is identity_group
    assert coslice_object in coslice_category
    assert coslice_category.arrow(coslice_object) is identity_group
    assert slice_category.base_object() is group
    assert coslice_category.base_object() is group
    assert subobjects.base_object() is symmetric
    assert kernel_object in subobjects
    assert superobjects.base_object() is group
    assert superobject in superobjects
    assert covering_objects.base_object() is group
    assert covering_object in covering_objects
    assert covered_objects.base_object() is symmetric
    assert covered_object in covered_objects
    assert kernel_object in kernels
    assert kernels.base_object() is sign.domain()
    assert cokernel_object in cokernels
    assert cokernels.base_object() is sign.codomain()


def test_identity_and_inclusion_functors() -> None:
    identity = Sets().identity_functor()
    three = Sets.Δ[2]
    assert identity(three) is three
    assert identity(Sets().Mor(three, three).identity()) == Sets().Mor(three, three).identity()
    inclusion = Fields().inclusion_into(CommutativeRings())
    assert inclusion(QQ) is QQ
    assert inclusion.domain() is Fields()
    assert inclusion.codomain() is CommutativeRings()
    assert OwnedAbelianGroups().inclusion_into(OwnedGroups())(OwnedGroups().C(4)) is OwnedGroups().C(4)


def test_natural_transformations_between_functors() -> None:
    identity = Sets().identity_functor()
    transformations = identity.natural_transformations_to(identity)
    assert transformations in Sets()
    three = Sets.Δ[2]
    unit = transformations.identity()
    assert unit.component(three) == Sets().Mor(three, three).identity()
    identity = Sets().Mor(three, three).identity()
    square = unit.naturality_square(identity)
    left = square.parent().projection(0)(square)
    right = square.parent().projection(1)(square)
    assert left == unit.naturality_target_composite(identity)
    assert right == unit.naturality_source_composite(identity)
    assert left == right


def test_isomorphisms_and_the_core() -> None:
    two = Sets.Δ[1]
    swap = Sets().Mor(two, two)(lambda point: two(1 - int(point)))
    isomorphism = Sets().Core().Mor(two, two)(swap, swap)
    assert isomorphism in Sets().Iso(two, two)
    assert isomorphism in Sets().Core().Mor(two, two)
    assert isomorphism.inverse() * isomorphism == Sets().Iso(two, two).identity()
    assert Sets().Iso(two, two).cardinality() == cardinal(2)
    assert Sets().Core().Mor(two, Sets.Δ[2]).cardinality() == cardinal(0)


def test_hom_end_aut_mono_epi_constructions_on_sets() -> None:
    two = Sets.Δ[1]
    three = Sets.Δ[2]
    assert Sets().Mor(two, three) is Sets().Mor(two, three)
    assert Sets().Mor(two, three).cardinality() == cardinal(9)
    assert Sets().End(three).cardinality() == cardinal(27)
    assert Sets().Aut(three).order() == 6
    assert Sets().Aut(three) in OwnedGroups()
    assert Sets().Mono(two, three).cardinality() == cardinal(6)
    assert Sets().Epi(three, two).cardinality() == cardinal(6)
    assert Sets().Epi(two, three).cardinality() == cardinal(0)
    assert Sets().Iso(two, three).cardinality() == cardinal(0)


def test_hom_end_aut_constructions_on_modules_over_a_field(field) -> None:
    plane = field.free_module(2)
    endomorphisms = Modules(field).End(plane)
    automorphisms = Modules(field).Aut(plane)
    assert endomorphisms in Cat()
    assert automorphisms in OwnedGroups()
    assert endomorphisms.identity() in automorphisms
    if field.cardinality().is_finite():
        q = field.cardinality()
        assert endomorphisms.cardinality() == cardinal(q**4)
        assert automorphisms.order() == (q**2 - 1) * (q**2 - q)
    else:
        assert automorphisms.cardinality() == field.cardinality()


def test_direct_sum_objects_know_their_summands() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    assert lattice in DirectSumObjects(Lattices(ZZ))
    assert lattice.number_of_summands() == cardinal(2)
    assert lattice.summands().cardinality() == cardinal(2)
    assert lattice.summand(0).module_rank() == cardinal(2)
    assert lattice.summand(1).determinant() == 3
