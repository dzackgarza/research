r"""Unverified local Mor lifts with genuine, nonidentity natural transformations.

Mathlib's ``CategoryTheory.PrelaxFunctor.mapFunctor`` separates the action on
2-arrows from the underlying object and 1-arrow actions. These specimens use
local functors on Hom categories, without claiming horizontal coherence.
"""

import pytest

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.functors.core import Functor, IdentityFunctor
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


class _UnderlyingCatIdentity(Functor):
    """Only the ordinary functor data are specified, not a higher action."""

    def __init__(self):
        super().__init__(Cat(), Cat())

    def _apply_object(self, obj):
        return obj

    def _apply_morphism(self, arrow):
        return arrow


def test_identity_cat_lift_preserves_a_transformation_between_distinct_functors():
    shape = DiscreteCategory(finite_ordered_set(("left", "right")))
    points = Sets.Δ[1]
    target = Sets.Δ[2]
    functors = Cat().Mor(shape, Sets())
    first = functors.constant_functor(points)
    second = functors.constant_functor(target)
    shift = Sets().Mor(points, target)(lambda point: target(int(point) + 1))
    alpha = functors.Mor(first, second)(lambda _obj: shift)
    induced = IdentityFunctor(Cat()).induced_mor_functor(shape, Sets())

    assert alpha.domain() is not alpha.codomain()
    assert induced.domain() is functors
    assert induced.codomain() is functors
    assert induced.on_object(first.object()) is first.object()
    assert induced(alpha) is alpha
    assert induced(alpha).component(shape("left")) is shift
    assert induced(alpha).component(shape("right"))(points(0)) == target(1)
    assert induced(alpha).domain() is first.object()
    assert induced(alpha).codomain() is second.object()
    assert induced(alpha) is induced(alpha)
    identity = functors.Mor(first, first).identity()
    assert induced(identity) is identity
    assert induced(alpha * identity) is alpha
    # Equivalent defining data are still not a placed functor object.
    with pytest.raises(TypeError, match="not an object"):
        induced.on_object(first.arrow())


def test_identity_end_lift_does_not_erase_a_nonidentity_endotransformation():
    points = Sets.Δ[2]
    functors = Cat().End(Sets())
    constant = functors.constant_functor(points)
    cycle = Sets().Mor(points, points)(lambda point: points((int(point) + 1) % 3))
    alpha = functors.Mor(constant, constant)(lambda _obj: cycle)
    induced = IdentityFunctor(Cat()).induced_end_functor(Sets())

    assert alpha.domain() is alpha.codomain()
    assert induced(alpha) is alpha
    assert induced(alpha).component(points)(points(0)) == points(1)
    identity = functors.Mor(constant, constant).identity()
    assert induced(identity).component(points)(points(0)) == points(0)
    composite = alpha * alpha
    assert induced(composite) is composite
    assert induced(composite).component(points)(points(0)) == points(2)


def test_specified_local_action_changes_components_and_composes_vertically():
    shape = DiscreteCategory(finite_ordered_set(("left", "right")))
    points = Sets.Δ[2]
    functors = Cat().Mor(shape, Sets())
    constant = functors.constant_functor(points)
    maps = Sets().Mor(points, points)
    cycle = maps(lambda point: points((int(point) + 1) % 3))
    inverse_cycle = maps(lambda point: points((int(point) + 2) % 3))
    swap = maps(lambda point: points({0: 1, 1: 0, 2: 2}[int(point)]))
    other_swap = maps(lambda point: points({0: 0, 1: 2, 2: 1}[int(point)]))
    transformations = functors.Mor(constant, constant)
    alpha = transformations(lambda _obj: swap)
    beta = transformations(lambda _obj: other_swap)

    def permutation(value, selected):
        match value:
            case _ if value is points:
                return selected
            case _:
                return Sets().Mor(value, value).identity()

    def conjugate(transformation):
        # The domain is discrete, so these objectwise components define a
        # natural transformation for every pair of functors here. Conjugation
        # cancels adjacent inverse pairs and preserves vertical composition.
        source = transformation.domain().functor()
        target = transformation.codomain().functor()
        return functors.Mor(source, target)(
            lambda obj: permutation(target(obj), cycle)
            * transformation.component(obj)
            * permutation(source(obj), inverse_cycle)
        )

    induced = IdentityFunctor(Cat()).induced_mor_functor(
        shape, Sets(), on_two_morphism=conjugate,
    )
    image = induced(alpha)
    component = image.component(shape("left"))
    assert image.domain() is induced(alpha.domain())
    assert image.codomain() is induced(alpha.codomain())
    assert component(points(0)) == points(0)
    assert component(points(1)) == points(2)
    assert component(points(2)) == points(1)
    assert alpha.component(shape("left"))(points(0)) == points(1)
    assert induced(alpha) is image

    direct = induced(beta * alpha)
    factored = induced(beta) * induced(alpha)
    identity_image = induced(transformations.identity())
    for point in points:
        assert direct.component(shape("left"))(point) == factored.component(shape("left"))(point)
        assert identity_image.component(shape("right"))(point) == point

    # Compose the specified local lifts, not unspecified higher data on the
    # underlying ordinary composite. The second conjugation is not the first.
    twice = induced.then(induced)(alpha)
    assert twice.component(shape("left"))(points(0)) == points(2)
    assert twice.component(shape("left"))(points(1)) == points(1)
    assert twice.component(shape("left"))(points(2)) == points(0)


def test_nondiscrete_lift_requires_complete_local_arrow_data_at_construction():
    shape = DiscreteCategory(finite_ordered_set(("point",)))
    ordinary = _UnderlyingCatIdentity()
    with pytest.raises(TypeError, match="must be callable"):
        ordinary.induced_mor_functor(shape, Sets(), on_two_morphism=42)
    with pytest.raises(TypeError, match="requires on_two_morphism"):
        ordinary.induced_mor_functor(shape, Sets())
    with pytest.raises(TypeError, match="requires on_two_morphism"):
        ordinary.induced_end_functor(Sets())

    points = Sets.Δ[1]
    functors = Cat().Mor(shape, Sets())
    constant = functors.constant_functor(points)
    swap = Sets().Mor(points, points)(lambda point: points(1 - int(point)))
    alpha = functors.Mor(constant, constant)(lambda _obj: swap)
    specified = ordinary.induced_mor_functor(
        shape, Sets(), on_two_morphism=lambda arrow: arrow,
    )
    assert specified(alpha) is alpha
    specified_end = ordinary.induced_end_functor(
        Sets(), on_two_morphism=lambda arrow: arrow,
    )
    end_constant = specified_end.domain().constant_functor(points)
    end_alpha = specified_end.domain().Mor(end_constant, end_constant)(lambda _obj: swap)
    assert specified_end(end_alpha) is end_alpha


def test_local_action_admits_both_source_and_selected_target_two_mors():
    shape = DiscreteCategory(finite_ordered_set(("left", "right")))
    other_shape = DiscreteCategory(finite_ordered_set(("other",)))
    points = Sets.Δ[1]
    functors = Cat().Mor(shape, Sets())
    constant = functors.constant_functor(points)
    swap = Sets().Mor(points, points)(lambda point: points(1 - int(point)))
    alpha = functors.Mor(constant, constant)(lambda _obj: swap)
    induced = IdentityFunctor(Cat()).induced_mor_functor(shape, Sets())
    other_functors = Cat().Mor(other_shape, Sets())
    other_constant = other_functors.constant_functor(points)
    wrong_source = other_functors.Mor(other_constant, other_constant)(lambda _obj: swap)
    with pytest.raises(TypeError):
        induced.on_morphism(wrong_source)

    different = functors.constant_functor(Sets.Δ[2])
    wrong_target = functors.Mor(different, different).identity()
    bad = IdentityFunctor(Cat()).induced_mor_functor(
        shape, Sets(), on_two_morphism=lambda _arrow: wrong_target,
    )
    with pytest.raises(TypeError, match="not a morphism of the functor's codomain"):
        bad.on_morphism(alpha)


@pytest.mark.parametrize("kind", ("mor", "end", "aut"))
def test_each_discrete_packet_lift_retains_the_supplied_action(kind):
    points = Sets.Δ[1]
    maps = Sets().Mor(points, points)
    swap = maps(lambda point: points(1 - int(point)))
    calls = []

    def transport(two_arrow):
        calls.append(two_arrow)
        source = induced.on_object(two_arrow.domain())
        target = induced.on_object(two_arrow.codomain())
        return induced.codomain().two_mor(source, target).identity()

    ordinary = IdentityFunctor(Sets())
    match kind:
        case "mor":
            induced = ordinary.induced_mor_functor(points, points, on_two_morphism=transport)
            arrow = swap
        case "end":
            induced = ordinary.induced_end_functor(points, on_two_morphism=transport)
            arrow = swap
        case "aut":
            induced = ordinary.induced_aut_functor(points, on_two_morphism=transport)
            arrow = Sets().Core().Mor(points, points)(swap, swap)

    stated = induced.domain().object(arrow)
    identity = induced.domain().two_mor(stated, stated).identity()
    result = induced(identity)
    assert len(calls) == 1 and calls[0] is identity
    assert result is induced.codomain().two_mor(
        induced(stated), induced(stated),
    ).identity()
    assert induced(identity) is result
    assert len(calls) == 1
