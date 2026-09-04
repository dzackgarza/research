import pytest

from dzack_research.preamble.all import QQ, ZZ, Lattices
from dzack_research.preamble.categories.modules import (
    AlternatingPower,
    BasedFreeModule,
    DeterminantLine,
    ExteriorForms,
    FramingVolumeTrivialization,
    HodgeDiscriminant,
    HodgeStar,
    HodgeStarOverFractionField,
    MultivectorHodgeStar,
    PoincareDuality,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_volume_is_literal_determinant_line_isomorphism_and_poincare_duality() -> None:
    module = BasedFreeModule(ZZ, finite_ordered_set(("e", "f")))
    determinant = DeterminantLine(module)
    volume = FramingVolumeTrivialization(module)
    dual = module.dual_module()
    pd = PoincareDuality(module, volume, 1)
    e = module.module_generator("e")
    f = module.module_generator("f")

    assert volume.domain() is determinant
    assert volume.codomain() is ZZ
    assert pd.domain() is module
    assert pd.codomain() is dual
    assert pd(e) == dual.module_generator("f")
    assert pd(f) == -dual.module_generator("e")
    assert pd.inverse()(pd(e)) == e


def test_hodge_star_is_the_metric_poincare_composite_and_has_expected_square() -> None:
    euclidean = Lattices(ZZ)(2)
    volume = FramingVolumeTrivialization(euclidean)
    star = HodgeStar(euclidean, volume, 1)
    forms = ExteriorForms(euclidean, 1)
    first = forms.module_generator(next(iter(forms.module_generating_set())))
    square = HodgeStar(euclidean, volume, 1).forward() * star.forward()

    assert star.domain() is forms
    assert star.codomain() is forms
    assert HodgeDiscriminant(euclidean, volume) == 1
    assert square(first) == -first

    hyperbolic = Lattices(ZZ)("U")
    hyperbolic_volume = FramingVolumeTrivialization(hyperbolic)
    hyperbolic_star = HodgeStar(hyperbolic, hyperbolic_volume, 1)
    hyperbolic_forms = ExteriorForms(hyperbolic, 1)
    generator = hyperbolic_forms.module_generator(
        next(iter(hyperbolic_forms.module_generating_set()))
    )
    assert HodgeDiscriminant(hyperbolic, hyperbolic_volume) == -1
    assert (hyperbolic_star.forward() * hyperbolic_star.forward())(generator) == generator


def test_multivector_hodge_star_is_distinct_from_form_hodge_star() -> None:
    lattice = Lattices(ZZ)("U")
    volume = FramingVolumeTrivialization(lattice)
    vector_star = MultivectorHodgeStar(lattice, volume, 1)
    form_star = HodgeStar(lattice, volume, 1)

    assert vector_star.domain() is AlternatingPower(lattice, 1)
    assert vector_star.codomain() is AlternatingPower(lattice, 1)
    assert form_star.domain() is ExteriorForms(lattice, 1)
    assert vector_star.domain() is not form_star.domain()


def test_nonunimodular_metric_does_not_invent_an_integral_form_hodge_star() -> None:
    lattice = Lattices(ZZ)("A2")
    volume = FramingVolumeTrivialization(lattice)

    assert lattice.is_nondegenerate()
    assert not lattice.is_unimodular()
    with pytest.raises(ValueError, match="unimodular"):
        HodgeStar(lattice, volume, 1)

    vector_star = MultivectorHodgeStar(lattice, volume, 1)
    generator = vector_star.domain().module_generator(
        next(iter(vector_star.domain().module_generating_set()))
    )
    assert (vector_star * vector_star)(generator) == -3 * generator

    rational_star = HodgeStarOverFractionField(lattice, volume, 1)
    assert rational_star.domain().base_ring() is QQ
    rational_generator = rational_star.domain().module_generator(
        next(iter(rational_star.domain().module_generating_set()))
    )
    assert (rational_star.forward() * rational_star.forward())(
        rational_generator
    ) == QQ(-1) / 3 * rational_generator
    assert lattice.hodge_star_over_fraction_field(volume, 1).domain().base_ring() is QQ
