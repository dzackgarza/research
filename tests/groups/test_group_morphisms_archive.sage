r"""Group homomorphisms: kernels, images, cokernels, composites and automorphism groups."""

from dzack_research.preamble.all import *


def test_reduction_c4_to_c2_has_kernel_of_order_two_and_c4_mod_kernel_is_the_image() -> None:
    r"""First isomorphism theorem for $C_4 \to C_2$, $g \mapsto h$: $\ker = \langle g^2 \rangle$ and $C_4/\ker \cong C_2$."""
    source = Groups.C(4)
    target = Groups.C(2)
    (g,) = source.group_generators()
    (h,) = target.group_generators()
    reduction = source.Mor(target)({g: h})

    kernel = reduction.kernel()
    assert kernel.order() == 2
    assert g**2 in kernel
    assert g not in kernel
    assert reduction.image().order() == 2
    assert kernel.inclusion().cokernel().is_isomorphic_to(reduction.image())
    assert reduction(reduction.lift(h)) == h


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


def test_reduction_then_inclusion_c4_to_c2_to_c4_is_the_squaring_endomorphism() -> None:
    r"""$C_4 \to C_2 \to C_4$, $g \mapsto h \mapsto g^2$, is $x \mapsto x^2$; its square is trivial since $x^4 = 1$."""
    c4 = Groups.C(4)
    c2 = Groups.C(2)
    (g,) = c4.group_generators()
    (h,) = c2.group_generators()
    reduction = c4.Mor(c2)({g: h})
    inclusion = c2.Mor(c4)({h: g**2})
    squaring = inclusion * reduction

    assert squaring(g) == g**2
    assert squaring(g**3) == g**2
    assert squaring.kernel().order() == 2
    assert squaring.image().order() == 2
    assert (squaring * squaring)(g) == c4.one()


def test_automorphism_groups_of_c4_c5_v4_and_s3() -> None:
    r"""$\operatorname{Aut}(C_n) \cong (\mathbb{Z}/n)^\times$; $\operatorname{Aut}(V_4) \cong \operatorname{GL}_2(\mathbb{F}_2) \cong S_3$; $\operatorname{Aut}(S_3) = \operatorname{Inn}(S_3) \cong S_3$ (Dummit--Foote 4.4)."""
    assert Groups.C(4).Aut().order() == 2
    assert Groups.C(5).Aut().is_isomorphic_to(Groups.C(4))
    assert Groups.V4().Aut().is_isomorphic_to(Groups.S(3))
    assert Groups.S(3).Aut().is_isomorphic_to(Groups.S(3))
