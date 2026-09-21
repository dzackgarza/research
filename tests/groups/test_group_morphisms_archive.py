r"""Archive reconciliation for owned group homomorphisms and automorphisms."""

from dzack_research.preamble.all import Groups

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/group_morphisms.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "disposition": "reconciled-live-owner",
}


def test_generator_images_define_an_actual_checked_group_homomorphism() -> None:
    source = Groups.C(4)
    target = Groups.C(2)
    source_generator = source.group_generators()[0]
    target_generator = target.group_generators()[0]
    mor = source.Mor(target)
    morphism = mor({source_generator: target_generator})

    assert mor is Groups().MorCategory().Of(source, target)
    assert morphism.parent() is mor
    assert morphism.domain() is source
    assert morphism.codomain() is target
    assert morphism(source_generator) == target_generator
    assert morphism(source_generator**2) == target.one()
    assert morphism.is_surjective()
    assert not morphism.is_injective()


def test_finite_group_mor_cardinality_uses_the_represented_gap_mor() -> None:
    assert Groups.C(2).Mor(Groups.C(3)).cardinality() == 1
    assert Groups.C(4).Mor(Groups.C(6)).cardinality() == 2
    assert Groups.C(12).Mor(Groups.C(18)).cardinality() == 6


def test_kernel_image_and_lift_are_actual_group_constructions() -> None:
    source = Groups.C(4)
    target = Groups.C(2)
    source_generator = source.group_generators()[0]
    target_generator = target.group_generators()[0]
    morphism = source.Mor(target)({source_generator: target_generator})

    kernel = morphism.kernel()
    image = morphism.image()
    lifted = morphism.lift(target_generator)

    assert kernel.supergroup() is source
    assert source_generator**2 in kernel
    assert source_generator not in kernel
    assert image.supergroup() is target
    assert target_generator in image
    assert morphism(lifted) == target_generator


def test_finite_kernel_uses_the_exact_gap_structure_predicates() -> None:
    symmetric = Groups.S(3)
    target = Groups.C(2)
    target_generator = target.group_generators()[0]
    sign = symmetric.Mor(target)(
        {
            generator: (
                target_generator if generator.order() == 2 else target.one()
            )
            for generator in symmetric.group_generators()
        }
    )
    kernel = sign.kernel()

    assert kernel.cardinality() == 3
    assert kernel.is_abelian()


def test_group_cokernels_quotient_by_the_normal_closure_of_the_image() -> None:
    symmetric = Groups.S(3)
    target = Groups.C(2)
    target_generator = target.group_generators()[0]
    sign = symmetric.Mor(target)(
        {
            generator: (
                target_generator if generator.order() == 2 else target.one()
            )
            for generator in symmetric.group_generators()
        }
    )
    kernel = sign.kernel()

    inclusion = kernel.inclusion()
    assert kernel.inclusion() is inclusion
    quotient = inclusion.cokernel()
    quotient_projection = inclusion.cokernel_projection()
    assert quotient.order() == 2
    assert quotient_projection.domain() is symmetric
    assert quotient_projection.codomain() is quotient
    assert quotient_projection.is_surjective()

    trivial = sign.cokernel()
    trivial_projection = sign.cokernel_projection()
    assert trivial.order() == 1
    assert trivial_projection.domain() is target
    assert trivial_projection.codomain() is trivial
    assert trivial_projection.is_surjective()


def test_composition_is_diagrammatic_and_retains_endpoints() -> None:
    c4 = Groups.C(4)
    c2 = Groups.C(2)
    generator4 = c4.group_generators()[0]
    generator2 = c2.group_generators()[0]
    projection = c4.Mor(c2)({generator4: generator2})
    inclusion = c2.Mor(c4)({generator2: generator4**2})
    composite = inclusion * projection

    assert composite.domain() is c4
    assert composite.codomain() is c4
    assert composite(generator4) == generator4**2


def test_automorphism_group_elements_have_actual_inverses() -> None:
    group = Groups.C(4)
    automorphisms = group.Aut()
    nontrivial = automorphisms.group_generators()[0]

    assert nontrivial.parent() is automorphisms
    assert nontrivial.inverse().parent() is automorphisms
    assert nontrivial * nontrivial.inverse() == automorphisms.one()
