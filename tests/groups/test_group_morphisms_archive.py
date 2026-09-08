r"""Archive reconciliation for owned group homomorphisms and automorphisms."""

from dzack_research.preamble.all import Groups, group_homset


def test_generator_images_define_an_actual_checked_group_homomorphism() -> None:
    source = Groups.C(4)
    target = Groups.C(2)
    source_generator = source.group_generators()[0]
    target_generator = target.group_generators()[0]
    morphism = group_homset(source, target)({source_generator: target_generator})

    assert morphism.domain() is source
    assert morphism.codomain() is target
    assert morphism(source_generator) == target_generator
    assert morphism(source_generator**2) == target.one()
    assert morphism.is_surjective()
    assert not morphism.is_injective()


def test_kernel_image_and_lift_are_actual_group_constructions() -> None:
    source = Groups.C(4)
    target = Groups.C(2)
    source_generator = source.group_generators()[0]
    target_generator = target.group_generators()[0]
    morphism = group_homset(source, target)({source_generator: target_generator})

    kernel = morphism.kernel()
    image = morphism.image()
    lifted = morphism.lift(target_generator)

    assert kernel.supergroup() is source
    assert source_generator**2 in kernel
    assert source_generator not in kernel
    assert image.supergroup() is target
    assert target_generator in image
    assert morphism(lifted) == target_generator


def test_composition_is_diagrammatic_and_retains_endpoints() -> None:
    c4 = Groups.C(4)
    c2 = Groups.C(2)
    generator4 = c4.group_generators()[0]
    generator2 = c2.group_generators()[0]
    projection = group_homset(c4, c2)({generator4: generator2})
    inclusion = group_homset(c2, c4)({generator2: generator4**2})
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
