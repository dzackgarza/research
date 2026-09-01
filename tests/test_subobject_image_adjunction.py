from dzack_research.preamble.all import (
    BasedFreeModule,
    Subobjects,
    ZZ,
    module_homset,
    subobject_image_adjunction,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def _assert_module_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    for label in left.domain().module_generating_set():
        generator = left.domain().module_generator(label)
        assert left(generator) == right(generator)


def _assert_order_maps_agree(left, right) -> None:
    assert left.domain() is right.domain()
    assert left.codomain() is right.codomain()
    _assert_module_maps_agree(left.factor_morphism(), right.factor_morphism())


def test_fixed_ambient_subobjects_and_direct_inverse_image_form_a_galois_connection() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("e1", "e2")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    e1, e2 = source.module_generators()
    u, v = target.module_generators()
    morphism = module_homset(source, target)(
        {"e1": 2 * u, "e2": v}
    )

    source_subobjects = Subobjects(source)
    target_subobjects = Subobjects(target)
    a = source.subobject_on((2 * e1 + e2,))
    not_a = source.subobject_on((e1,))
    b = target.subobject_on((4 * u, v))

    adjunction = subobject_image_adjunction(morphism)
    direct = adjunction.left_adjoint()
    inverse = adjunction.right_adjoint()
    image_a = direct(a)
    preimage_b = inverse(b)

    # The preimage is the mathematical pullback subobject, not a row-space
    # proxy: it sits in the original source through an inclusion of index two.
    assert preimage_b.inclusion().codomain() is source
    assert preimage_b.index() == 2
    assert preimage_b.inclusion().is_in_image(2 * e1)
    assert preimage_b.inclusion().is_in_image(e2)
    assert not preimage_b.inclusion().is_in_image(e1)

    assert target_subobjects.leq(image_a, b)
    assert source_subobjects.leq(a, preimage_b)
    assert target_subobjects.leq(direct(not_a), b) is False
    assert source_subobjects.leq(not_a, preimage_b) is False

    forward_witness = target_subobjects.hom(image_a, b).canonical_morphism()
    transpose = adjunction.hom_set_isomorphism_forward(forward_witness, a)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, b)
    assert transpose.domain() is a
    assert transpose.codomain() is preimage_b
    assert recovered.domain() is image_a
    assert recovered.codomain() is b

    # Naturality uses genuine commuting-triangle morphisms in the thin
    # fixed-ambient categories.
    a_larger = source.subobject_on((2 * e1, e2))
    source_order_map = source_subobjects.hom(a, a_larger).canonical_morphism()
    left, right = adjunction.unit_transformation().naturality_square(source_order_map)
    _assert_order_maps_agree(left, right)

    b_larger = target.subobject_on((2 * u, v))
    target_order_map = target_subobjects.hom(b, b_larger).canonical_morphism()
    left, right = adjunction.counit_transformation().naturality_square(target_order_map)
    _assert_order_maps_agree(left, right)

    left_triangle = adjunction.counit(direct(a)) * direct(adjunction.unit(a))
    _assert_order_maps_agree(
        left_triangle,
        target_subobjects.identity(direct(a)),
    )

    right_triangle = inverse(adjunction.counit(b)) * adjunction.unit(inverse(b))
    _assert_order_maps_agree(
        right_triangle,
        source_subobjects.identity(inverse(b)),
    )
