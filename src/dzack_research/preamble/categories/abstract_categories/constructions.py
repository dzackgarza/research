r"""Canonical categorical construction vocabulary.

The abstract layer owns only the names and category dispatch. Concrete
mathematical categories own their represented constructions.
"""

from sage.categories.category import Category
from dzack_research.preamble.categories.abstract_categories.arrow_categories import SubobjectCategory


def _common_category(*objects):
    if not objects:
        raise ValueError("a categorical construction requires at least one object")
    return Category.meet([obj.category() for obj in objects])


def _category_operation(operation, *objects, arguments=None):
    common = _common_category(*objects)
    method_name = f"_categorical_{operation}"
    for category in common.all_super_categories():
        method = getattr(category, method_name, None)
        if method is not None:
            return method(*(objects if arguments is None else arguments))
    raise NotImplementedError(
        f"no represented {operation.replace('_', '-')} is owned by a common category of "
        + ", ".join(map(str, objects))
    )


def TensorProduct(left, right):
    return _category_operation("tensor_product", left, right)


def TensorSquare(obj):
    return TensorProduct(obj, obj)


def Biproduct(left, right):
    return _category_operation("biproduct", left, right)


def Product(left, right):
    return _category_operation("product", left, right)


def Coproduct(left, right):
    return _category_operation("coproduct", left, right)


def _ProductMorphism(left_morphism, right_morphism, *, source, target):
    return _category_operation(
        "product_morphism",
        left_morphism.domain(), right_morphism.domain(),
        left_morphism.codomain(), right_morphism.codomain(),
        arguments=(left_morphism, right_morphism, source, target),
    )


def _CoproductMorphism(left_morphism, right_morphism, *, source, target):
    return _category_operation(
        "coproduct_morphism",
        left_morphism.domain(), right_morphism.domain(),
        left_morphism.codomain(), right_morphism.codomain(),
        arguments=(left_morphism, right_morphism, source, target),
    )


def Pushout(left_morphism, right_morphism):
    if left_morphism.domain() is not right_morphism.domain():
        raise ValueError("pushout arrows require one common domain")
    return _category_operation(
        "pushout",
        left_morphism.domain(), left_morphism.codomain(), right_morphism.codomain(),
        arguments=(left_morphism, right_morphism),
    )


def FiberProduct(left_morphism, right_morphism):
    if left_morphism.codomain() is not right_morphism.codomain():
        raise ValueError("fiber-product arrows require one common codomain")
    return _category_operation(
        "pullback",
        left_morphism.domain(), right_morphism.domain(), left_morphism.codomain(),
        arguments=(left_morphism, right_morphism),
    )


def Kernel(morphism):
    return morphism.kernel()


def Cokernel(morphism):
    return morphism.cokernel()


def Equalizer(left_morphism, right_morphism):
    r"""Return the represented equalizer of two parallel arrows."""
    if (
        left_morphism.domain() is not right_morphism.domain()
        or left_morphism.codomain() is not right_morphism.codomain()
    ):
        raise ValueError("equalizer arrows must be parallel")
    return _category_operation(
        "equalizer",
        left_morphism.domain(),
        left_morphism.codomain(),
        arguments=(left_morphism, right_morphism),
    )


def Coequalizer(left_morphism, right_morphism):
    r"""Return the represented coequalizer of two parallel arrows."""
    if (
        left_morphism.domain() is not right_morphism.domain()
        or left_morphism.codomain() is not right_morphism.codomain()
    ):
        raise ValueError("coequalizer arrows must be parallel")
    return _category_operation(
        "coequalizer",
        left_morphism.domain(),
        left_morphism.codomain(),
        arguments=(left_morphism, right_morphism),
    )


def _nonempty_parallel_family(morphisms, construction):
    try:
        reference = morphisms[0]
    except (AttributeError, IndexError) as error:
        raise ValueError(f"a {construction} family must be nonempty") from error
    return reference


def EqualizerOfFamily(morphisms):
    r"""Return the represented wide equalizer of a nonempty arrow family."""
    reference = _nonempty_parallel_family(morphisms, "wide equalizer")
    return _category_operation(
        "equalizer_family",
        reference.domain(),
        reference.codomain(),
        arguments=(morphisms,),
    )


def CoequalizerOfFamily(morphisms):
    r"""Return the represented wide coequalizer of a nonempty arrow family."""
    reference = _nonempty_parallel_family(morphisms, "wide coequalizer")
    return _category_operation(
        "coequalizer_family",
        reference.domain(),
        reference.codomain(),
        arguments=(morphisms,),
    )


def Subobjects(base_object, category=None):
    base_category = base_object.category() if category is None else category
    if base_object not in base_category:
        raise TypeError("the subobject base must lie in the stated category")
    return SubobjectCategory(base_category, base_object)


__all__ = [
    "Biproduct", "Coequalizer", "CoequalizerOfFamily", "Cokernel", "Coproduct",
    "Equalizer", "EqualizerOfFamily", "FiberProduct", "Kernel", "Product",
    "Pushout", "Subobjects", "TensorProduct", "TensorSquare",
]
