r"""Canonical categorical construction vocabulary.

The abstract layer owns only the names and category dispatch. Concrete
mathematical categories own their represented constructions.
"""

from collections.abc import Sequence

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from dzack_research.preamble.categories.abstract_categories.arrow_categories import SubobjectCategory
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily


def _common_category(*objects: Parent) -> Category:
    if not objects:
        raise ValueError("a categorical construction requires at least one object")
    return Category.meet([obj.category() for obj in objects])


def TensorProduct(left: Parent, right: Parent) -> Parent:
    category = _common_category(left, right)
    construction = category._categorical_tensor_product
    assert construction is not NotImplemented, (
        f"no represented tensor product is owned by a common category of {left}, {right}"
    )
    return construction(left, right)


def TensorSquare(obj: Parent) -> Parent:
    return TensorProduct(obj, obj)


def Biproduct(left: Parent, right: Parent) -> Parent:
    category = _common_category(left, right)
    construction = category._categorical_biproduct
    assert construction is not NotImplemented, (
        f"no represented biproduct is owned by a common category of {left}, {right}"
    )
    return construction(left, right)


def Product(left: Parent, right: Parent) -> Parent:
    category = _common_category(left, right)
    construction = category._categorical_product
    assert construction is not NotImplemented, (
        f"no represented product is owned by a common category of {left}, {right}"
    )
    return construction(left, right)


def Coproduct(left: Parent, right: Parent) -> Parent:
    category = _common_category(left, right)
    construction = category._categorical_coproduct
    assert construction is not NotImplemented, (
        f"no represented coproduct is owned by a common category of {left}, {right}"
    )
    return construction(left, right)


def _ProductMorphism(
    left_morphism: Morphism,
    right_morphism: Morphism,
    *,
    source: Parent,
    target: Parent,
) -> Morphism:
    category = _common_category(
        left_morphism.domain(), right_morphism.domain(),
        left_morphism.codomain(), right_morphism.codomain(),
    )
    construction = category._categorical_product_morphism
    assert construction is not NotImplemented, (
        "no represented product-morphism construction is owned by the common category"
    )
    return construction(left_morphism, right_morphism, source, target)


def _CoproductMorphism(
    left_morphism: Morphism,
    right_morphism: Morphism,
    *,
    source: Parent,
    target: Parent,
) -> Morphism:
    category = _common_category(
        left_morphism.domain(), right_morphism.domain(),
        left_morphism.codomain(), right_morphism.codomain(),
    )
    construction = category._categorical_coproduct_morphism
    assert construction is not NotImplemented, (
        "no represented coproduct-morphism construction is owned by the common category"
    )
    return construction(left_morphism, right_morphism, source, target)


def Pushout(left_morphism: Morphism, right_morphism: Morphism) -> Parent:
    if left_morphism.domain() is not right_morphism.domain():
        raise ValueError("pushout arrows require one common domain")
    category = _common_category(
        left_morphism.domain(), left_morphism.codomain(), right_morphism.codomain(),
    )
    construction = category._categorical_pushout
    assert construction is not NotImplemented, (
        "no represented pushout is owned by a common category of the span"
    )
    return construction(left_morphism, right_morphism)


def FiberProduct(left_morphism: Morphism, right_morphism: Morphism) -> Parent:
    if left_morphism.codomain() is not right_morphism.codomain():
        raise ValueError("fiber-product arrows require one common codomain")
    category = _common_category(
        left_morphism.domain(), right_morphism.domain(), left_morphism.codomain(),
    )
    construction = category._categorical_pullback
    assert construction is not NotImplemented, (
        "no represented pullback is owned by a common category of the cospan"
    )
    return construction(left_morphism, right_morphism)


def Kernel(morphism: Morphism) -> Parent:
    return morphism.kernel()


def Cokernel(morphism: Morphism) -> Parent:
    return morphism.cokernel()


def Equalizer(left_morphism: Morphism, right_morphism: Morphism) -> Parent:
    r"""Return the represented equalizer of two parallel arrows."""
    if (
        left_morphism.domain() is not right_morphism.domain()
        or left_morphism.codomain() is not right_morphism.codomain()
    ):
        raise ValueError("equalizer arrows must be parallel")
    category = _common_category(
        left_morphism.domain(),
        left_morphism.codomain(),
    )
    construction = category._categorical_equalizer
    assert construction is not NotImplemented, (
        "no represented equalizer is owned by the arrows' common category"
    )
    return construction(left_morphism, right_morphism)


def Coequalizer(left_morphism: Morphism, right_morphism: Morphism) -> Parent:
    r"""Return the represented coequalizer of two parallel arrows."""
    if (
        left_morphism.domain() is not right_morphism.domain()
        or left_morphism.codomain() is not right_morphism.codomain()
    ):
        raise ValueError("coequalizer arrows must be parallel")
    category = _common_category(
        left_morphism.domain(),
        left_morphism.codomain(),
    )
    construction = category._categorical_coequalizer
    assert construction is not NotImplemented, (
        "no represented coequalizer is owned by the arrows' common category"
    )
    return construction(left_morphism, right_morphism)


def _parallel_family(
    morphisms: IndexedFamily | Sequence[Morphism],
    construction: str,
) -> tuple[IndexedFamily, Morphism]:
    family = morphisms if isinstance(morphisms, IndexedFamily) else finite_family(morphisms)
    indices = iter(family.index_set())
    try:
        first_index = next(indices)
    except StopIteration as error:
        raise ValueError(f"a {construction} family must be nonempty") from error
    return family, family[first_index]


def EqualizerOfFamily(
    morphisms: IndexedFamily | Sequence[Morphism],
) -> Parent:
    r"""Return the represented wide equalizer of a nonempty arrow family."""
    family, reference = _parallel_family(morphisms, "wide equalizer")
    category = _common_category(reference.domain(), reference.codomain())
    construction = category._categorical_equalizer_family
    assert construction is not NotImplemented, (
        "no represented wide equalizer is owned by the arrows' common category"
    )
    return construction(family)


def CoequalizerOfFamily(
    morphisms: IndexedFamily | Sequence[Morphism],
) -> Parent:
    r"""Return the represented wide coequalizer of a nonempty arrow family."""
    family, reference = _parallel_family(morphisms, "wide coequalizer")
    category = _common_category(reference.domain(), reference.codomain())
    construction = category._categorical_coequalizer_family
    assert construction is not NotImplemented, (
        "no represented wide coequalizer is owned by the arrows' common category"
    )
    return construction(family)


def Subobjects(
    base_object: Parent,
    category: Category | None = None,
) -> SubobjectCategory:
    base_category = base_object.category() if category is None else category
    if base_object not in base_category:
        raise TypeError("the subobject base must lie in the stated category")
    return SubobjectCategory(base_category, base_object)


__all__ = [
    "Biproduct", "Coequalizer", "CoequalizerOfFamily", "Cokernel", "Coproduct",
    "Equalizer", "EqualizerOfFamily", "FiberProduct", "Kernel", "Product",
    "Pushout", "Subobjects", "TensorProduct", "TensorSquare",
]
