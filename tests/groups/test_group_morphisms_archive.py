r"""Archive reconciliation for owned group homomorphisms and automorphisms."""

from dzack_research.preamble.all import Groups

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/group/group_morphisms.sage",
    "live_owner": "src/dzack_research/preamble/categories/group/groups.py",
    "disposition": "reconciled-live-owner",
}




def test_finite_group_mor_cardinality_uses_the_represented_gap_mor() -> None:
    assert Groups.C(2).Mor(Groups.C(3)).cardinality() == 1
    assert Groups.C(4).Mor(Groups.C(6)).cardinality() == 2
    assert Groups.C(12).Mor(Groups.C(18)).cardinality() == 6




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




