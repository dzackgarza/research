"""The three separating specimens for general divisor-class theory."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    QuadraticField,
)
from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.picard_groups import (
    PicardGroups,
)


def _zero_class_group(scheme):
    return ClassGroups()(ZZ.free_module(0), scheme=scheme)


def _cyclic_module(order):
    generators = ZZ.free_module(1)
    relations = ZZ.free_module(1)
    return relations.Mor(generators)(
            {0: ZZ(order) * generators.module_generator(0)}
        ).cokernel()


def test_projective_n_space_over_a_field_has_picard_and_class_group_Z() -> None:
    projective = ProjectiveSpaces(QQ)(3)
    base = projective.base_scheme()
    base_picard = PicardGroups().trivial(base)
    base_class = _zero_class_group(base)
    base_comparison = base_picard.module_category().Mor(base_picard, base_class)({})

    theory = projective.divisor_class_theory(
        base_picard,
        base_class,
        base_comparison,
    )

    assert theory.picard_group().module_rank() == 1
    assert theory.class_group().module_rank() == 1
    assert theory.picard_to_class_group_morphism()(theory.picard_group().hyperplane_class()) != theory.class_group().zero()


def test_projective_n_space_over_a_base_keeps_the_base_picard_contribution() -> None:
    field = QuadraticField(-5, "a")
    order = field.ring_of_integers()
    base = (order).affine_spectrum(base_ring=order)
    projective = ProjectiveSpaces(order)(2)
    base_picard = PicardGroups()(_cyclic_module(2), scheme=base)
    base_class = ClassGroups()(_cyclic_module(2), scheme=base)
    base_comparison = base_picard.module_category().Mor(base_picard, base_class)(
        {0: base_class.module_generator(0)}
    )

    theory = projective.divisor_class_theory(
        base_picard,
        base_class,
        base_comparison,
    )

    pulled = theory.picard_group().base_picard_inclusion()(base_picard.module_generator(0))
    assert pulled.additive_order() == 2
    assert theory.picard_group().module_rank() == 2
    assert theory.class_group().module_rank() == 2
    assert theory.picard_to_class_group_morphism()(pulled).additive_order() == 2


def test_normal_singular_surface_has_a_noncartier_weil_class() -> None:
    polynomial = QQ.polynomial_ring("x,y,z")
    x = polynomial.algebra_generator("x")
    y = polynomial.algebra_generator("y")
    z = polynomial.algebra_generator("z")
    ring = polynomial.quotient_ring(polynomial.ideal(x * y - z**2))
    x, y, z = ring(x), ring(y), ring(z)
    scheme = (ring).affine_spectrum(base_ring=QQ)
    prime = ring.spectrum()(ring.ideal(x, z))
    vertex = ring.spectrum()(ring.ideal(x, y, z))
    weil = scheme.full_weil_divisor_group()

    assert ring.is_normal()
    assert not weil.prime_is_cartier_at(prime, vertex)
    assert weil.principal_divisor(x) == 2 * weil.prime_divisor(prime)
