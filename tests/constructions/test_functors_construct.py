r"""Functors and adjunctions a mathematician expects to apply.

Each functor with a resolved domain is applied to that domain's witness and
lands in its codomain; each adjunction has a unit and a counit with the right
endpoints and a hom-set bijection that round-trips.  Functors over a base ring
are taken over every commutative ring in the catalogue.
"""

import pytest

from dzack_research.preamble.all import *  # noqa: F401,F403

NULLARY_FUNCTORS = {
    "AbelianizationFunctor": (AbelianizationFunctor, lambda: Groups.S(3), AbelianGroups),
    "CardinalityFunctor": (CardinalityFunctor, lambda: Sets.Δ[2], None),
    "FinitePowerSetFunctor": (FinitePowerSetFunctor, lambda: Sets.Δ[2], Sets),
    "FreeGroupFunctor": (FreeGroupFunctor, lambda: Sets.Δ[1], Groups),
    "GroupUnderlyingSetFunctor": (GroupUnderlyingSetFunctor, lambda: Groups.S(3), Sets),
    "RingOfIntegersFunctor": (RingOfIntegersFunctor, lambda: QQ, OwnedOrders),
    "FractionFieldFunctor": (FractionFieldFunctor, lambda: ZZ, OwnedNumberFields),
}


@pytest.mark.parametrize("name", sorted(NULLARY_FUNCTORS))
def test_a_nullary_functor_sends_an_object_into_its_codomain(name) -> None:
    constructor, specimen, codomain = NULLARY_FUNCTORS[name]
    functor = constructor()
    source = specimen()
    image = functor(source)
    assert source in functor.domain()
    if codomain is not None:
        assert image in codomain()
    assert image in functor.codomain()
    identity = source.Mor(source).identity()
    image_of_identity = functor(identity)
    assert image_of_identity.domain() == image
    assert image_of_identity.codomain() == image


def test_known_values_of_the_nullary_functors() -> None:
    assert AbelianizationFunctor()(Groups.S(3)).order() == 2
    assert CardinalityFunctor()(Sets.Δ[2]) == 3
    assert FinitePowerSetFunctor()(Sets.Δ[2]).cardinality() == 8
    assert FreeGroupFunctor()(Sets.Δ[1]).is_isomorphic_to(Groups.Free(2))
    assert GroupUnderlyingSetFunctor()(Groups.S(3)).cardinality() == 6
    assert RingOfIntegersFunctor()(QQ) is ZZ
    assert FractionFieldFunctor()(ZZ) is QQ
    gaussian = RingOfIntegersFunctor()(QuadraticField(-1, "i"))
    assert gaussian in OwnedOrders()
    assert gaussian.is_maximal()
    assert gaussian.rank() == 2


def test_functors_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    polynomials = PolynomialRing(ring, "x")

    free = FreeModuleFunctor(ring)(Sets.Δ[2])
    assert free in FreeModules(ring)
    assert free.rank() == 3
    assert UnderlyingSetFunctor(ring)(module) in Sets()
    assert DualizationFunctor(ring)(module).rank() == 2
    assert SymmetricAlgebraFunctor(ring)(module) in CommutativeAlgebras(ring)
    assert TensorAlgebraFunctor(ring)(module) in Algebras(ring)
    assert AlternatingAlgebraFunctor(ring)(module).graded_piece(2).rank() == 1
    assert AffineSpecFunctor(ring)(polynomials) in AffineSchemes(ring)
    assert AffineSpecFunctor(ring)(polynomials).relative_dimension() == 1
    assert DeRhamFunctor(ring)(polynomials) in StrictlyCommutativeDifferentialGradedAlgebras(ring)


def test_free_forgetful_adjunction_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    adjunction = free_forgetful_adjunction(ring)
    labels = Sets.Δ[1]
    free = adjunction.left_adjoint()(labels)
    module = FreeModule(ring, 3)

    unit = adjunction.unit(labels)
    assert unit.domain() is labels
    assert unit.codomain() == adjunction.right_adjoint()(free)
    assert unit.is_injective()
    counit = adjunction.counit(module)
    assert counit.codomain() is module
    assert counit.is_surjective()

    phi = free.Mor(module)({0: module.module_generator(0), 1: 2 * module.module_generator(2)})
    transpose = adjunction.hom_set_isomorphism_forward(phi)
    assert transpose(labels(1)) == 2 * module.module_generator(2)
    recovered = adjunction.hom_set_isomorphism_inverse(transpose, module)
    assert recovered == phi


def test_algebra_adjunctions_over_every_commutative_ring(commutative_ring) -> None:
    ring = commutative_ring
    module = FreeModule(ring, 2)
    for adjunction in (symmetric_algebra_adjunction(ring), tensor_algebra_adjunction(ring)):
        algebra = adjunction.left_adjoint()(module)
        unit = adjunction.unit(module)
        assert unit.domain() is module
        assert unit.codomain() == adjunction.right_adjoint()(algebra)
        assert unit.is_injective()
        counit = adjunction.counit(algebra)
        assert counit.codomain() is algebra


def test_de_rham_adjunction_over_every_field(field) -> None:
    adjunction = de_rham_adjunction(field)
    polynomials = PolynomialRing(field, "x")
    de_rham = adjunction.left_adjoint()(polynomials)
    assert adjunction.right_adjoint()(de_rham) is polynomials
    assert adjunction.unit(polynomials).domain() is polynomials
    assert adjunction.counit(de_rham).codomain() is de_rham


def test_group_and_number_field_adjunctions() -> None:
    abelianization = abelianization_adjunction()
    symmetric = Groups.S(3)
    unit = abelianization.unit(symmetric)
    assert unit.domain() is symmetric
    assert unit.is_surjective()
    assert unit.codomain().order() == 2

    free = free_group_underlying_set_adjunction()
    letters = Sets.Δ[1]
    assert free.unit(letters).domain() is letters
    assert free.unit(letters).is_injective()
    assert free.counit(symmetric).is_surjective()

    orders = order_number_field_adjunction()
    assert orders.left_adjoint()(ZZ) is QQ
    assert orders.right_adjoint()(QQ) is ZZ
    assert orders.unit(ZZ).domain() is ZZ
    assert orders.counit(QQ).codomain() is QQ
    assert QQ in Fields()
