r"""Archive reconciliation for categories of chosen functor images."""

from dzack_research.preamble.categories.abstract_categories.functor_images import ImageOfFunctor
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.functors.core import Functor, IdentityFunctor
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/abstract_categories/functor_images.sage",
        "live_owner": "src/dzack_research/preamble/categories/abstract_categories/functor_images.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/abstract_categories/functors.sage",
        "live_owner": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "owner_overrides": {
            "Functor": "src/dzack_research/preamble/categories/functors/core.py",
            "Functor.Image": "src/dzack_research/preamble/categories/abstract_categories/functor_images.py",
            "ImageInclusionFunctor": "src/dzack_research/preamble/categories/abstract_categories/functor_images.py",
            "IdentityFunctor": "src/dzack_research/preamble/categories/functors/core.py",
            "IdentityFunctor.factors": "src/dzack_research/preamble/categories/functors/core.py",
            "ComposedFunctor": "src/dzack_research/preamble/categories/functors/core.py",
            "ComposedFunctor.factors": "src/dzack_research/preamble/categories/functors/core.py",
            "ComposedFunctor.is_faithful": "src/dzack_research/preamble/categories/functors/core.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


class _ConstantPresentedSetFunctor(Functor):
    def __init__(self, domain, target) -> None:
        self._target = target
        super().__init__(domain, Sets())

    def _apply_object(self, _obj):
        return self._target

    def _apply_morphism(self, _morphism):
        return Sets().Mor(self._target, self._target).identity()


class _IdentitySetsFunctor(Functor):
    def __init__(self) -> None:
        super().__init__(Sets(), Sets())

    def _apply_object(self, obj):
        return obj

    def _apply_morphism(self, morphism):
        return morphism


def test_two_preimages_of_one_codomain_object_remain_distinct_presentations() -> None:
    labels = finite_ordered_set(("left", "right"))
    source = DiscreteCategory(labels)
    target = finite_ordered_set((0, 1))
    functor = _ConstantPresentedSetFunctor(source, target)
    image = functor.Image()

    left = image(source("left"))
    right = image(source("right"))

    assert left is not right
    assert left.preimage() is source("left")
    assert right.preimage() is source("right")
    assert left.underlying_image() is target
    assert right.underlying_image() is target
    assert image is ImageOfFunctor(functor)


def test_functor_image_homs_wrap_nonidentity_codomain_arrows_and_forget_them_faithfully() -> None:
    functor = _IdentitySetsFunctor()
    image = ImageOfFunctor(functor)
    source = finite_ordered_set((0, 1))
    target = finite_ordered_set(("a", "b"))
    presented_source = image(source)
    presented_target = image(target)
    arrow = Sets().Mor(source, target)(lambda value: "a" if value == 0 else "b")

    presented_arrow = image.Mor(presented_source, presented_target)(arrow)
    inclusion = image.inclusion()

    assert presented_arrow.domain() is presented_source
    assert presented_arrow.codomain() is presented_target
    assert inclusion(presented_source) is source
    assert inclusion(presented_target) is target
    assert inclusion(presented_arrow) is arrow


def test_functor_image_mor_exposes_codomain_mor_and_composes_through_it() -> None:
    functor = _IdentitySetsFunctor()
    image = ImageOfFunctor(functor)
    source = finite_ordered_set((0, 1))
    middle = finite_ordered_set(("a", "b"))
    target = finite_ordered_set((False, True))
    presented_source = image(source)
    presented_middle = image(middle)
    presented_target = image(target)

    first_underlying = Sets().Mor(source, middle)(
        lambda value: "a" if value == 0 else "b"
    )
    second_underlying = Sets().Mor(middle, target)(lambda value: value == "b")
    first = image.Mor(presented_source, presented_middle)(first_underlying)
    second = image.Mor(presented_middle, presented_target)(second_underlying)
    outer_mor = image.Mor(presented_source, presented_target)
    composite = outer_mor.compose(second, first)
    inclusion = image.inclusion()

    assert first.parent().codomain_mor_category() is Sets().Mor(source, middle)
    assert composite.domain() is presented_source
    assert composite.codomain() is presented_target
    assert inclusion(composite) == second_underlying * first_underlying


def test_archived_composition_with_identity_keeps_the_nonidentity_set_map() -> None:
    functor = _IdentitySetsFunctor()
    identity = IdentityFunctor(Sets())
    composed_left = functor.then(identity)
    composed_right = identity.then(functor)
    source = finite_ordered_set((0, 1))
    target = finite_ordered_set(("a", "b"))
    arrow = Sets().Mor(source, target)(lambda value: target("a") if value == 0 else target("b"))

    assert composed_left is functor
    assert composed_right is functor
    assert composed_left(arrow) is arrow
    assert composed_right(arrow) is arrow
