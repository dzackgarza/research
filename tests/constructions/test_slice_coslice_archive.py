r"""Archived slice/coslice/subobject semantics on the current owned categories."""

from dzack_research.preamble.all import (
    CosliceCategory,
    FreeModule,
    Modules,
    Sets,
    SliceCategory,
    SubobjectCategory,
    ZZ,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_slice_retains_the_fixed_codomain_and_identity_edge() -> None:
    points = finite_ordered_set(("a", "b"))
    same_points = finite_ordered_set(("a", "b"))
    one = finite_ordered_set(("*",))

    assert points == same_points
    assert points is not same_points
    assert SliceCategory(Sets(), points).base_object() is points
    assert SliceCategory(Sets(), same_points).base_object() is same_points

    structure = Sets().Mor(points, one)(lambda _point: one[0])
    obj = SliceCategory(Sets(), one)(structure)
    swap = Sets().Mor(points, points)(
        lambda point: points[1] if point == points[0] else points[0]
    )
    hom = obj.category().Mor(obj, obj)
    square = hom(swap)

    assert obj.arrow() is structure
    assert square.left() is swap
    assert square.right() == Sets().Mor(one, one).identity()
    assert square * square == hom.identity()


def test_coslice_retains_the_fixed_domain_and_identity_edge() -> None:
    one = finite_ordered_set(("*",))
    points = finite_ordered_set(("a", "b"))
    costructure = Sets().Mor(one, points)(lambda _point: points[0])
    coslice = CosliceCategory(Sets(), one)
    obj = coslice(costructure)
    collapse = Sets().Mor(points, points)(lambda _point: points[0])
    hom = coslice.Mor(obj, obj)
    square = hom(collapse)

    assert obj.arrow() is costructure
    assert square.left() == Sets().Mor(one, one).identity()
    assert square.right() is collapse
    assert square * square == square
    assert hom.identity() * square == square


def test_subobject_is_the_object_with_its_selected_monomorphism_into_the_fixed_base() -> None:
    module = FreeModule(ZZ, 2)
    generator = module.module_generator(0)
    submodule = module.subobject_on((generator,))
    inclusion = submodule.inclusion()
    category = SubobjectCategory(Modules(ZZ), module)

    assert submodule in category
    assert category.base_object() is module
    assert category.as_slice_object(submodule).arrow() is inclusion
    identity = category.Mor(submodule, submodule).identity()
    assert identity.factor_morphism() == Modules(ZZ).Mor(submodule, submodule).identity()
    assert submodule.inclusion() is inclusion
