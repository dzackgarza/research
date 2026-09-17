
from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineSpaces,
    Algebras,
    Groups,
    Lattices,
    Modules,
    OpenImmersions,
    Sets,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/abstract_categories/hom_categories.sage",
    "live_owner": "src/dzack_research/preamble/categories/abstract_categories/hom_categories.py",
    "disposition": "reconciled-live-owner",
}


def test_hom_and_end_families_recover_actual_external_homsets() -> None:
    source = Sets.Δ[2]
    target = Sets.Δ[1]
    hom_family = Sets().HomCategory()
    hom_category = hom_family.Of(source, target)
    map_ = Sets().Mor(source, target)(lambda value: target(value % 2))
    assert map_ in hom_category
    arrow_object = hom_category.object(map_)
    assert arrow_object.arrow() is map_
    assert hom_category.identity_2(map_).domain() is arrow_object

    end = Sets().End(source)
    identity = end.identity_endomorphism()
    for value in source:
        assert identity(value) == value


def test_mono_epi_iso_and_aut_hom_families_have_the_expected_arrow_classes() -> None:
    source = Sets.Δ[1]
    target = Sets.Δ[3]
    monos = Sets().Mono(source, target)
    epis = Sets().Epi(target, source)
    inclusion = monos(lambda value: target(value + 1))
    quotient = epis(lambda value: source(value % 2))
    assert inclusion.parent() is monos
    assert quotient.parent() is epis
    assert inclusion in monos
    assert quotient in epis

    source_endomorphisms = Sets().Mor(source, source)
    source_monos = Sets().Mono(source, source)
    source_epis = Sets().Epi(source, source)
    constant = source_endomorphisms(lambda _value: source(0))
    swap = source_endomorphisms(lambda value: source(1 - int(value)))
    assert constant not in source_monos
    assert constant not in source_epis
    assert swap in source_monos
    assert swap in source_epis
    isomorphism = Sets().Core().Mor(source, source)(swap, swap)
    isos = Sets().Iso(source, source)
    auts = Sets().Aut(source)
    assert auts is isos
    assert isomorphism in isos
    assert isomorphism in auts
    assert auts.identity_automorphism() in auts


def test_category_packet_transports_hom_end_aut_supercategories() -> None:
    algebras = Algebras(QQ)
    modules = Modules(QQ)
    packet = algebras.category_packet()

    assert packet.C() is algebras
    module_packet = modules.category_packet()
    forget = Algebras(QQ).underlying_module()
    assert forget.domain() is algebras
    assert forget.codomain() is modules
    assert module_packet.Homs() not in packet.Homs().super_categories()
    assert module_packet.Ends() not in packet.Ends().super_categories()
    assert module_packet.Auts() not in packet.Auts().super_categories()
    assert packet.Homs() in packet.Monos().super_categories()
    assert packet.Homs() in packet.Epis().super_categories()
    assert packet.Homs() in packet.Isos().super_categories()
    assert packet.Monos() in packet.Isos().super_categories()
    assert packet.Epis() in packet.Isos().super_categories()
    assert packet.Ends() in packet.Auts().super_categories()
    assert packet.Isos() in packet.Auts().super_categories()

    algebra = QQ.free_module(("x",)).symmetric_algebra()
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


def test_join_hom_keeps_the_most_specific_inherited_arrow_theory() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
    x = line.coordinate_algebra().algebra_generator("x")
    open_x = line.distinguished_open(x)

    subobject_hom = OpenImmersions(line).Mor(open_x, open_x)
    joined_hom = open_x.category().Mor(open_x, open_x)

    assert joined_hom is subobject_hom
    scheme_identity = open_x.categorical_identity_morphism()
    represented_identity = joined_hom(scheme_identity)
    assert represented_identity.factor_morphism() is scheme_identity


def test_supercategory_hom_accepts_the_same_arrow_from_a_stronger_hom_parent() -> None:
    algebra = QQ.free_module(("x", "y")).symmetric_algebra()
    structured_identity = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra).identity()
    ordinary_hom = Algebras(QQ).Mor(algebra, algebra)

    assert structured_identity.parent() is not ordinary_hom
    assert structured_identity in ordinary_hom

    group = Groups.C(3)
    automorphism = group.Aut().one()
    assert automorphism.parent() is group.Aut()
    assert automorphism in OwnedGroups().Mor(group, group)


def test_forgetful_functor_induces_hom_end_and_aut_functors() -> None:
    polynomial = QQ.free_module(("x",)).symmetric_algebra()
    x = polynomial.algebra_generator("x")
    algebra = (polynomial).quotient_by_relations([x**2])
    identity = Algebras(algebra.base_ring()).Associative().Unital().Mor(algebra, algebra).identity()
    isomorphism = Algebras(QQ).Core().Mor(algebra, algebra)(identity, identity)
    forget = Algebras(QQ).underlying_module()

    hom_source = Algebras(QQ).Mor(algebra, algebra)(identity)
    hom_image = forget.induced_hom_functor(algebra, algebra)(hom_source)
    assert hom_image.parent() is Modules(QQ).Mor(forget(algebra), forget(algebra))
    assert hom_image(forget(algebra).one()) == forget(identity)(forget(algebra).one())

    end_source = Algebras(QQ).End(algebra)(identity)
    end_image = forget.induced_end_functor(algebra)(end_source)
    assert end_image.parent() is Modules(QQ).End(forget(algebra))
    assert end_image(forget(algebra).one()) == forget(identity)(forget(algebra).one())

    aut_source = Algebras(QQ).Aut(algebra)(isomorphism)
    aut_image = forget.induced_aut_functor(algebra)(aut_source)
    assert aut_image.parent() is Modules(QQ).Aut(forget(algebra))
    assert aut_image.forward().domain() is forget(algebra)
    assert aut_image.forward().codomain() is forget(algebra)
    assert aut_image.inverse().domain() is forget(algebra)
    assert aut_image.inverse().codomain() is forget(algebra)


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
)

    rings = OwnedRings()
    hom = ZZ.Mor(ZZ)
    assert hom is rings.Mor(ZZ, ZZ)
    assert hom is rings.End(ZZ)
    identity = hom.identity()
    assert identity.parent() is hom
    assert (identity * identity).parent() is hom
    assert (identity * identity)(ZZ(3)) == ZZ(3)


def test_set_mono_family_constructs_and_composes_nonidentity_injections() -> None:
    source = Sets.Δ[1]
    middle = Sets.Δ[2]
    target = Sets.Δ[3]
    mono_source = Sets().Mono(source, middle)
    mono_target = Sets().Mono(middle, target)
    mono_composite = Sets().Mono(source, target)
    first = mono_source(lambda value: middle(int(value)))
    second = mono_target(lambda value: target(int(value) + 1))

    assert first in mono_source
    assert second in mono_target
    composite = second * first
    assert composite.parent() is mono_composite
    assert composite in mono_composite
    assert composite(source(0)) == target(1)
    assert composite(source(1)) == target(2)
    assert mono_composite.underlying_homset() is Sets().Mor(source, target)


def test_set_epi_family_constructs_and_composes_nonidentity_surjections() -> None:
    source = Sets.Δ[3]
    middle = Sets.Δ[2]
    target = Sets.Δ[1]
    epi_source = Sets().Epi(source, middle)
    epi_target = Sets().Epi(middle, target)
    epi_composite = Sets().Epi(source, target)
    first = epi_source(lambda value: middle(int(value) % 3))
    second = epi_target(lambda value: target(int(value) % 2))

    composite = second * first
    assert composite.parent() is epi_composite
    assert composite in epi_composite
    assert composite(source(0)) == target(0)
    assert composite(source(1)) == target(1)
    assert epi_composite.underlying_homset() is Sets().Mor(source, target)


def test_induced_map_reads_arrows_as_objects_and_preserves_their_identity_two_arrows() -> None:
    from dzack_research.preamble.categories.functors.core import IdentityFunctor

    points = Sets.Δ[1]
    arrows = Sets().Mor(points, points)
    swap = arrows(lambda point: points(1 - int(point)))
    induced = IdentityFunctor(Sets()).induced_hom_functor(points, points)
    stated = induced.domain().object(swap)

    assert induced(swap) is swap
    assert induced(stated) is swap
    assert induced(swap)(points(0)) == points(1)
    identity = induced.domain().identity_2(swap)
    assert induced(identity) is induced.codomain().identity_2(swap)


def test_identity_functor_composition_requires_matching_categories() -> None:
    import pytest
    from dzack_research.preamble.categories.functors.core import IdentityFunctor

    sets_identity = IdentityFunctor(Sets())
    module_identity = IdentityFunctor(Modules(QQ))
    assert sets_identity.then(sets_identity) is sets_identity
    with pytest.raises(ValueError, match="matching middle categories"):
        sets_identity.then(module_identity)
    with pytest.raises(ValueError, match="matching middle categories"):
        module_identity.then(sets_identity)
