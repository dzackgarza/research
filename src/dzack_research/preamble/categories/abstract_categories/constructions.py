r"""Canonical categorical construction vocabulary.

The abstract layer owns only the names and category dispatch. Concrete
mathematical categories own their represented constructions.
"""

from sage.categories.category import Category


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
    kernel = getattr(morphism, "kernel", None)
    if kernel is None:
        raise NotImplementedError(f"{morphism} has no represented categorical kernel")
    return kernel()


def Cokernel(morphism):
    cokernel = getattr(morphism, "cokernel", None)
    if cokernel is None:
        raise NotImplementedError(f"{morphism} has no represented categorical cokernel")
    return cokernel()


def Subobjects(base_object, category=None):
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import SubobjectCategory
    base_category = base_object.category() if category is None else category
    if base_object not in base_category:
        raise TypeError("the subobject base must lie in the stated category")
    return SubobjectCategory(base_category, base_object)


__all__ = [
    "Biproduct", "Cokernel", "Coproduct", "FiberProduct", "Kernel",
    "Product", "Pushout", "Subobjects", "TensorProduct", "TensorSquare",
]
