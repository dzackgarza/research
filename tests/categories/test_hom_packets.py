
from dzack_research.preamble.all import (
    AutCategoryOf,
    Algebras,
    EndCategoryOf,
    EpiCategoryOf,
    HomCategoryOf,
    IsoCategoryOf,
    MonoCategoryOf,
    Modules,
    QQ,
    Sets,
    SymmetricAlgebraOn,
    FinitelyPresentedAlgebra,
    Groups,
    Isomorphism,
    Lattices,
    ZZ,
    algebra_homset,
    algebra_underlying_module_functor,
    category_packet,
    set_injection,
    set_surjection,
)
from dzack_research.preamble.categories.functors.hom_packets import (
    induced_aut_functor,
    induced_end_functor,
    induced_hom_functor,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups


def test_hom_and_end_families_recover_actual_external_homsets() -> None:
    source = Sets.Δ[2]
    target = Sets.Δ[1]
    hom_family = HomCategoryOf(Sets())
    hom_category = hom_family.Of(source, target)
    map_ = Sets().Mor(source, target)(lambda value: target(value % 2))
    assert map_ in hom_category
    arrow_object = hom_category.object(map_)
    assert arrow_object.arrow() is map_
    assert hom_category.identity_2(map_).domain() is arrow_object

    end = EndCategoryOf(Sets()).Of(source)
    identity = end.identity_endomorphism()
    for value in source:
        assert identity(value) == value


def test_mono_epi_iso_and_aut_hom_families_have_the_expected_arrow_classes() -> None:
    source = Sets.Δ[1]
    target = Sets.Δ[3]
    inclusion = set_injection(source, target, lambda value: target(value + 1))
    quotient = set_surjection(target, source, lambda value: source(value % 2))

    monos = MonoCategoryOf(Sets()).Of(source, target)
    epis = EpiCategoryOf(Sets()).Of(target, source)
    assert inclusion in monos
    assert quotient in epis

    swap = Sets().Mor(source, source)(lambda value: source(1 - int(value)))
    isomorphism = Isomorphism(swap, swap)
    isos = IsoCategoryOf(Sets()).Of(source, source)
    auts = AutCategoryOf(Sets()).Of(source)
    assert auts is isos
    assert isomorphism in isos
    assert isomorphism in auts
    assert auts.identity_automorphism() in auts


def test_category_packet_transports_hom_end_aut_supercategories() -> None:
    algebras = Algebras(QQ)
    modules = Modules(QQ)
    packet = category_packet(algebras)

    assert packet.C() is algebras
    module_packet = category_packet(modules)
    assert module_packet.Homs() in packet.Homs().super_categories()
    assert module_packet.Ends() in packet.Ends().super_categories()
    assert module_packet.Auts() in packet.Auts().super_categories()
    assert packet.Homs() in packet.Monos().super_categories()
    assert packet.Homs() in packet.Epis().super_categories()
    assert packet.Homs() in packet.Isos().super_categories()
    assert packet.Monos() in packet.Isos().super_categories()
    assert packet.Epis() in packet.Isos().super_categories()
    assert packet.Ends() in packet.Auts().super_categories()
    assert packet.Isos() in packet.Auts().super_categories()

    algebra = SymmetricAlgebraOn(QQ, ("x",))
    algebra_hom_category = packet.Homs().Of(algebra, algebra)
    module_hom_category = module_packet.Homs().Of(algebra, algebra)
    assert module_hom_category in algebra_hom_category.super_categories()

    algebra_iso_category = packet.Isos().Of(algebra, algebra)
    assert packet.Homs().Of(algebra, algebra) in algebra_iso_category.super_categories()
    assert packet.Monos().Of(algebra, algebra) in algebra_iso_category.super_categories()
    assert packet.Epis().Of(algebra, algebra) in algebra_iso_category.super_categories()

    algebra_aut_category = packet.Auts().Of(algebra)
    assert algebra_aut_category is packet.Isos().Of(algebra, algebra)
    assert packet.Ends().Of(algebra) in algebra_aut_category.super_categories()


def test_forgetful_functor_induces_hom_end_and_aut_functors() -> None:
    polynomial = SymmetricAlgebraOn(QQ, ("x",))
    x = polynomial.algebra_generator("x")
    algebra = FinitelyPresentedAlgebra(polynomial, [x**2])
    identity = algebra_homset(algebra, algebra).identity()
    isomorphism = Isomorphism(identity, identity)
    forget = algebra_underlying_module_functor(QQ)

    hom_source = HomCategoryOf(Algebras(QQ)).Of(algebra, algebra)(identity)
    hom_image = induced_hom_functor(forget, algebra, algebra)(hom_source)
    assert hom_image.parent() is Modules(QQ).Mor(forget(algebra), forget(algebra))
    assert hom_image(forget(algebra).one()) == forget(identity)(forget(algebra).one())

    end_source = EndCategoryOf(Algebras(QQ)).Of(algebra)(identity)
    end_image = induced_end_functor(forget, algebra)(end_source)
    assert end_image.parent() is Modules(QQ).End(forget(algebra))
    assert end_image(forget(algebra).one()) == forget(identity)(forget(algebra).one())

    aut_source = AutCategoryOf(Algebras(QQ)).Of(algebra)(isomorphism)
    aut_image = induced_aut_functor(forget, algebra)(aut_source)
    underlying_iso = aut_image.arrow()
    assert underlying_iso.forward().domain() is forget(algebra)
    assert underlying_iso.forward().codomain() is forget(algebra)


def test_lattice_embedding_isometry_and_automorphism_are_packet_objects() -> None:
    lattices = Lattices(ZZ)
    lattice = lattices(2)

    assert lattice.Emb(lattice) is lattices.Mono(lattice, lattice)
    assert lattice.Isom(lattice) is lattices.Iso(lattice, lattice)
    assert lattice.Aut() is lattices.Aut(lattice)
    assert lattice.Aut() is lattices.Iso(lattice, lattice)
    assert lattice.Aut() in OwnedGroups()

    assert lattices.Mor(lattice, lattice) in lattice.Emb(lattice).super_categories()
    assert lattices.Mono(lattice, lattice) in lattice.Isom(lattice).super_categories()
    assert lattices.Epi(lattice, lattice) in lattice.Isom(lattice).super_categories()
    assert lattices.End(lattice) in lattice.Aut().super_categories()
    assert lattice.Aut().identity().parent() is lattice.Aut()


def test_group_hom_end_and_aut_are_the_packet_objects() -> None:
    groups = OwnedGroups()
    group = Groups.C(3)

    assert group.Mor(group) is groups.Mor(group, group)
    assert group.End() is groups.End(group)
    assert groups.End(group) is groups.Mor(group, group)
    assert group.Aut() is groups.Aut(group)
    assert group.Aut() is groups.Iso(group, group)
    assert group.Aut().one().parent() is group.Aut()
    assert groups.End(group) in group.Aut().super_categories()


def test_ring_hom_packet_reuses_the_canonical_equal_endpoint_hom_object() -> None:
    from dzack_research.preamble.categories.rings.ring_foundation import (
        OwnedRings,
        ring_homset,
    )

    rings = OwnedRings()
    hom = ring_homset(ZZ, ZZ)
    assert hom is rings.Mor(ZZ, ZZ)
    assert hom is rings.End(ZZ)
    identity = hom.identity()
    assert identity.parent() is hom
    assert (identity * identity).parent() is hom
    assert (identity * identity)(ZZ(3)) == ZZ(3)
