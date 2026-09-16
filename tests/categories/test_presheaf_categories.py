r"""Presheaves are objects of the functor category ``[C^op, D]``; Yoneda is a functor into it."""

from dzack_research.preamble.all import ZZ, Cat, Modules, Sets
from dzack_research.preamble.categories.abstract_categories import FiniteOrdinalCategory
from dzack_research.preamble.categories.functors.core import IdentityFunctor
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_presheaves_are_the_functor_category_on_the_opposite() -> None:
    presheaves = Sets().presheaves()

    assert presheaves is Cat().Mor(Sets().opposite(), Sets())
    assert presheaves is Cat().presheaves(Sets())
    assert presheaves in Cat()


def test_presheaves_with_different_values_over_one_site_are_distinct_objects_of_cat() -> None:
    site = FiniteOrdinalCategory(2)
    set_valued = site.presheaves(Sets())
    module_valued = site.presheaves(Modules(ZZ))

    assert set_valued is not module_valued
    assert set_valued in Cat() and module_valued in Cat()

    points = finite_ordered_set(("a", "b"))
    constant_set = set_valued(set_valued.constant_functor(points))
    constant_module = module_valued(module_valued.constant_functor(ZZ.free_module(points)))
    set_hom = set_valued.Mor(constant_set, constant_set)
    module_hom = module_valued.Mor(constant_module, constant_module)

    assert set_hom is not module_hom
    assert set_hom.identity() * set_hom.identity() == set_hom.identity()


def test_yoneda_sends_an_object_to_its_representable_presheaf() -> None:
    site = Sets()
    points = finite_ordered_set(("a", "b"))
    yoneda = site.yoneda_embedding()
    representable = yoneda(points)

    assert representable in site.presheaves()
    functor = representable.arrow().functor()
    assert functor.domain() is site.opposite()
    assert functor.codomain() is Sets()
    assert functor(site.opposite()(points)) is site.Mor(points, points)


def test_yoneda_acts_on_a_nonidentity_arrow_by_postcomposition() -> None:
    site = Sets()
    points = finite_ordered_set(("a", "b"))
    swap = site.Mor(points, points)(lambda point: "b" if point == "a" else "a")
    yoneda = site.yoneda_embedding()
    image = yoneda(swap)

    assert image.domain() is yoneda(points)
    assert image.codomain() is yoneda(points)
    component = image.component(site.opposite()(points))
    identity = site.Mor(points, points).identity()
    assert component(identity) == swap
    assert component(swap) == swap * swap


def test_yoneda_on_a_poset_separates_the_order() -> None:
    site = FiniteOrdinalCategory(3)
    yoneda = site.yoneda_embedding()
    opposite = site.opposite()
    top = yoneda(site(2)).arrow().functor()
    bottom = yoneda(site(0)).arrow().functor()

    assert top(opposite(site(0))).cardinality() == 1
    assert bottom(opposite(site(2))).cardinality() == 0


def test_representable_presheaf_is_contravariant_in_the_site() -> None:
    site = FiniteOrdinalCategory(3)
    opposite = site.opposite()
    representable = site.yoneda_embedding()(site(2)).arrow().functor()
    arrow = site.Mor(site(0), site(1)).unique()
    reversed_arrow = opposite.Mor(opposite(site(1)), opposite(site(0)))(arrow)
    restriction = representable(reversed_arrow)

    assert restriction.domain() is site.Mor(site(1), site(2))
    assert restriction.codomain() is site.Mor(site(0), site(2))
    assert restriction(site.Mor(site(1), site(2)).unique()) == site.Mor(site(0), site(2)).unique()


def test_presheaf_transport_acts_on_objects_and_natural_transformations() -> None:
    site = Sets()
    points = finite_ordered_set(("a", "b"))
    yoneda = site.yoneda_embedding()
    transport = Cat().presheaf_transport(IdentityFunctor(site), Sets().power_set_functor())

    assert transport.domain() is site.presheaves()
    assert transport.codomain() is site.presheaves()
    transported = transport(yoneda(points))
    value = transported.arrow().functor()(site.opposite()(points))
    assert value is Sets().power_set_functor()(site.Mor(points, points))

    swap = site.Mor(points, points)(lambda point: "b" if point == "a" else "a")
    transported_swap = transport(yoneda(swap))
    assert transported_swap.domain() is transported
    assert transported_swap.codomain() is transported
