from __future__ import annotations

import pytest
from sage.schemes.generic.scheme import Scheme
from sage.structure.element import Element

from dzack_research.preamble.all import (
    QQ,
    FiniteGluedInvariantQuotient,
    GObjects,
    Groups,
    PolynomialRing,
    Schemes,
    Spec,
    SpecFunctor,
)
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    RingMorphism,
    ring_morphism,
)
from dzack_research.preamble.categories.schemes.schemes import SchemeMorphism
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)


class _SwapChart:
    r"""One private coordinate-swap specimen reused by the Q regressions."""

    def __init__(self) -> None:
        self.group = Groups.C(2)
        self.algebra = PolynomialRing(QQ, ("x", "y"))
        self.x = self.algebra.algebra_generator("x")
        self.y = self.algebra.algebra_generator("y")
        self.chart = Spec(self.algebra)
        swap_pullback = self.algebra.Mor(self.algebra)({"x": self.y, "y": self.x})
        swap = SpecFunctor(QQ)(swap_pullback)
        identity = self.chart.categorical_identity_morphism()
        self.acted = GObjects(self.group, Schemes(QQ))(
            self.chart,
            lambda element: identity if element == self.group.one() else swap,
        )
        self.quotient = self.acted.affine_quotient()
        self.invariant_algebra = self.quotient.coordinate_algebra()
        self.inclusion = self.acted.invariant_algebra_inclusion()
        self.linear = next(
            self.invariant_algebra.algebra_generator(label)
            for label in self.invariant_algebra.algebra_generating_set()
            if self.inclusion(self.invariant_algebra.algebra_generator(label))
            == self.x + self.y
        )
        self.quadratic = next(
            self.invariant_algebra.algebra_generator(label)
            for label in self.invariant_algebra.algebra_generating_set()
            if self.inclusion(self.invariant_algebra.algebra_generator(label))
            == self.x**2 + self.y**2
        )

    def source_scale(self, scale: int) -> CategoricalIsomorphism:
        scale_value = QQ(scale)
        overlap = self.chart.distinguished_open(self.x + self.y)
        localized = overlap.coordinate_algebra()
        localization_map = localized.localization_map()
        forward_base = self.algebra.Mor(self.algebra)(
            {"x": scale_value * self.x, "y": scale_value * self.y}
        )
        inverse_base = self.algebra.Mor(self.algebra)(
            {"x": self.x / scale_value, "y": self.y / scale_value}
        )

        def forward_pullback(element: Element) -> Element:
            numerator, denominator = localized.localization_fraction_data(element)
            numerator_image = localization_map(forward_base(numerator))
            denominator_image = localization_map(forward_base(denominator))
            result: Element = numerator_image * denominator_image.inverse_of_unit()
            return result

        def inverse_pullback(element: Element) -> Element:
            numerator, denominator = localized.localization_fraction_data(element)
            numerator_image = localization_map(inverse_base(numerator))
            denominator_image = localization_map(inverse_base(denominator))
            result: Element = numerator_image * denominator_image.inverse_of_unit()
            return result

        forward_ring_map: RingMorphism = ring_morphism(
            localized,
            localized,
            forward_pullback,
        )
        inverse_ring_map: RingMorphism = ring_morphism(
            localized,
            localized,
            inverse_pullback,
        )
        forward: SchemeMorphism = overlap.Mor(overlap)(forward_ring_map)
        inverse: SchemeMorphism = overlap.Mor(overlap)(inverse_ring_map)
        transition: CategoricalIsomorphism = Isomorphism(forward, inverse)
        return transition

    def quotient_scale(
        self,
        linear_scale: int,
        quadratic_scale: int | None = None,
    ) -> CategoricalIsomorphism:
        linear_scale_value = QQ(linear_scale)
        quadratic_scale_value = QQ(
            linear_scale**2 if quadratic_scale is None else quadratic_scale
        )
        overlap = self.quotient.distinguished_open(self.linear)
        localized = overlap.coordinate_algebra()
        localization_map = localized.localization_map()
        forward_images = {}
        inverse_images = {}
        for label in self.invariant_algebra.algebra_generating_set():
            generator = self.invariant_algebra.algebra_generator(label)
            image = self.inclusion(generator)
            if image == self.x + self.y:
                forward_images[label] = linear_scale_value * generator
                inverse_images[label] = generator / linear_scale_value
            elif image == self.x**2 + self.y**2:
                forward_images[label] = quadratic_scale_value * generator
                inverse_images[label] = generator / quadratic_scale_value
            else:
                raise AssertionError(f"unexpected invariant algebra generator image {image}")
        forward_base = self.invariant_algebra.Mor(self.invariant_algebra)(forward_images)
        inverse_base = self.invariant_algebra.Mor(self.invariant_algebra)(inverse_images)

        def forward_pullback(element: Element) -> Element:
            numerator, denominator = localized.localization_fraction_data(element)
            numerator_image = localization_map(forward_base(numerator))
            denominator_image = localization_map(forward_base(denominator))
            result: Element = numerator_image * denominator_image.inverse_of_unit()
            return result

        def inverse_pullback(element: Element) -> Element:
            numerator, denominator = localized.localization_fraction_data(element)
            numerator_image = localization_map(inverse_base(numerator))
            denominator_image = localization_map(inverse_base(denominator))
            result: Element = numerator_image * denominator_image.inverse_of_unit()
            return result

        forward_ring_map: RingMorphism = ring_morphism(
            localized,
            localized,
            forward_pullback,
        )
        inverse_ring_map: RingMorphism = ring_morphism(
            localized,
            localized,
            inverse_pullback,
        )
        forward: SchemeMorphism = overlap.Mor(overlap)(forward_ring_map)
        inverse: SchemeMorphism = overlap.Mor(overlap)(inverse_ring_map)
        transition: CategoricalIsomorphism = Isomorphism(forward, inverse)
        return transition


def _constant_acted_family(acted: Scheme, size: int) -> IndexedFamily:
    index_set = finite_ordered_set(range(size))
    family: IndexedFamily = finite_indexed_family(
        index_set,
        lambda _index: acted,
        name="Acted affine charts for a glued quotient regression",
    )
    return family


def _transition_family(
    transitions: dict[tuple[int, int], CategoricalIsomorphism],
) -> IndexedFamily:
    pair_index_set = finite_ordered_set(tuple(transitions))
    family: IndexedFamily = finite_indexed_family(
        pair_index_set,
        lambda pair: transitions[pair],
        name="Pair transitions for a glued quotient regression",
    )
    return family


class _GluedSwapQuotient:
    def __init__(
        self,
        chart_data: _SwapChart,
        quotient: FiniteGluedInvariantQuotient,
    ) -> None:
        self.chart_data = chart_data
        self.quotient = quotient
        self.source = quotient.source_scheme()


@pytest.fixture(scope="module")
def glued_swap_quotient() -> _GluedSwapQuotient:
    data = _SwapChart()
    acted_charts = _constant_acted_family(data.acted, 3)
    source_transitions = _transition_family(
        {
            (0, 1): data.source_scale(2),
            (0, 2): data.source_scale(6),
            (1, 2): data.source_scale(3),
        }
    )
    quotient_transitions = _transition_family(
        {
            (0, 1): data.quotient_scale(2),
            (0, 2): data.quotient_scale(6),
            (1, 2): data.quotient_scale(3),
        }
    )
    quotient = FiniteGluedInvariantQuotient(
        QQ,
        data.group,
        acted_charts,
        source_transitions,
        quotient_transitions,
    )
    return _GluedSwapQuotient(data, quotient)


def test_finite_glued_invariant_quotient_retains_global_action_and_descent(
    glued_swap_quotient: _GluedSwapQuotient,
) -> None:
    data = glued_swap_quotient.chart_data
    source = glued_swap_quotient.source
    quotient = glued_swap_quotient.quotient
    generator = data.group.group_generators().unrank(0)

    assert tuple(quotient.chart_index_set()) == (0, 1, 2)
    assert quotient.source_scheme() is source
    assert quotient.acted_charts()[1] is data.acted
    assert quotient.source_charts()[1] is data.chart
    assert quotient.local_quotient(0) is data.acted.affine_quotient()

    action = quotient.global_action()
    source_endomorphisms = Schemes(QQ).Mor(source, source)
    assert action.domain() is data.group
    assert action.codomain() is source_endomorphisms
    generator_action = quotient.action_of(generator)
    identity_action = quotient.action_of(data.group.one())
    assert generator_action.parent() is source_endomorphisms
    assert generator_action * generator_action == identity_action

    quotient_map = quotient.quotient_morphism()
    assert quotient_map.domain() is source
    assert quotient_map.codomain() is quotient.quotient_scheme()
    assert quotient_map * generator_action == quotient_map

    source_transition = quotient.source_transition_between(0, 1).forward()
    quotient_transition = quotient.quotient_transition_between(0, 1).forward()
    assert (
        quotient_transition * quotient.quotient_overlap_factor(0, 1)
        == quotient.quotient_overlap_factor(1, 0) * source_transition
    )


def test_glued_quotient_has_the_affine_target_universal_factorization(
    glued_swap_quotient: _GluedSwapQuotient,
) -> None:
    data = glued_swap_quotient.chart_data
    source = glued_swap_quotient.source
    quotient = glued_swap_quotient.quotient
    target_algebra = PolynomialRing(QQ, "t")
    target = Spec(target_algebra)
    coefficients = {0: 6, 1: 3, 2: 1}
    local_maps: IndexedFamily = finite_indexed_family(
        quotient.chart_index_set(),
        lambda index: data.chart.Mor(target)(
            target_algebra.Mor(data.algebra)(
                {"t": QQ(coefficients[int(index)]) * (data.x + data.y)}
            )
        ),
        name="Invariant local maps from the glued quotient regression source",
    )
    morphism: SchemeMorphism = Schemes(QQ).Mor(source, target)(local_maps)

    factor = quotient.factor_invariant_affine_morphism(morphism)

    assert factor.domain() is quotient.quotient_scheme()
    assert factor.codomain() is target
    assert factor * quotient.quotient_morphism() == morphism


def test_glued_quotient_rejects_a_noninvariant_global_map(
    glued_swap_quotient: _GluedSwapQuotient,
) -> None:
    data = glued_swap_quotient.chart_data
    source = glued_swap_quotient.source
    quotient = glued_swap_quotient.quotient
    target_algebra = PolynomialRing(QQ, "t")
    target = Spec(target_algebra)
    coefficients = {0: 6, 1: 3, 2: 1}
    local_maps: IndexedFamily = finite_indexed_family(
        quotient.chart_index_set(),
        lambda index: data.chart.Mor(target)(
            target_algebra.Mor(data.algebra)(
                {"t": QQ(coefficients[int(index)]) * (data.x - data.y)}
            )
        ),
        name="Noninvariant local maps from the glued quotient regression source",
    )
    morphism: SchemeMorphism = Schemes(QQ).Mor(source, target)(local_maps)

    with pytest.raises(ValueError, match="not invariant"):
        quotient.factor_invariant_affine_morphism(morphism)


def test_glued_quotient_rejects_a_wrong_descended_overlap_map() -> None:
    data = _SwapChart()
    acted_charts = _constant_acted_family(data.acted, 2)
    source_transitions = _transition_family({(0, 1): data.source_scale(2)})
    quotient_transitions = _transition_family(
        {(0, 1): data.quotient_scale(2, quadratic_scale=5)}
    )

    with pytest.raises(ValueError, match="quotient descent square"):
        FiniteGluedInvariantQuotient(
            QQ,
            data.group,
            acted_charts,
            source_transitions,
            quotient_transitions,
        )


def test_glued_quotient_rejects_a_nonequivariant_source_transition() -> None:
    data = _SwapChart()
    overlap = data.chart.distinguished_open(data.x * data.y)
    localized = overlap.coordinate_algebra()
    localization_map = localized.localization_map()
    forward_base = data.algebra.Mor(data.algebra)(
        {"x": QQ(2) * data.x, "y": QQ(3) * data.y}
    )
    inverse_base = data.algebra.Mor(data.algebra)(
        {"x": data.x / QQ(2), "y": data.y / QQ(3)}
    )

    def forward_pullback(element: Element) -> Element:
        numerator, denominator = localized.localization_fraction_data(element)
        numerator_image = localization_map(forward_base(numerator))
        denominator_image = localization_map(forward_base(denominator))
        result: Element = numerator_image * denominator_image.inverse_of_unit()
        return result

    def inverse_pullback(element: Element) -> Element:
        numerator, denominator = localized.localization_fraction_data(element)
        numerator_image = localization_map(inverse_base(numerator))
        denominator_image = localization_map(inverse_base(denominator))
        result: Element = numerator_image * denominator_image.inverse_of_unit()
        return result

    forward_ring_map: RingMorphism = ring_morphism(
        localized,
        localized,
        forward_pullback,
    )
    inverse_ring_map: RingMorphism = ring_morphism(
        localized,
        localized,
        inverse_pullback,
    )
    forward: SchemeMorphism = overlap.Mor(overlap)(forward_ring_map)
    inverse: SchemeMorphism = overlap.Mor(overlap)(inverse_ring_map)
    source_transition: CategoricalIsomorphism = Isomorphism(forward, inverse)
    acted_charts = _constant_acted_family(data.acted, 2)
    source_transitions = _transition_family({(0, 1): source_transition})
    quotient_transitions = _transition_family({(0, 1): data.quotient_scale(2)})

    with pytest.raises(ValueError, match="not G-equivariant"):
        FiniteGluedInvariantQuotient(
            QQ,
            data.group,
            acted_charts,
            source_transitions,
            quotient_transitions,
        )
