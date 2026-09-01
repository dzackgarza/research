r"""Canonical owners for categorical constructions in the live category graph.

The archived preamble had a broad construction framework tied to a retired
category substrate.  The live code keeps the public mathematical vocabulary
here and dispatches to the exact backend supplied by the relevant category.
This prevents module, lattice, and algebra layers from creating competing
public notions of tensor product, biproduct, kernel, cokernel, or subobject.
"""


def TensorProduct(left, right):
    r"""Return the categorical tensor product of ``left`` and ``right``."""
    if left.base_ring() != right.base_ring():
        raise ValueError("a tensor product requires one common base ring")
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModules,
    )
    from dzack_research.preamble.categories.modules.tensor_products import (
        _module_tensor_product,
    )

    category = FinitelyPresentedModules(left.base_ring())
    if left in category and right in category:
        return _module_tensor_product(left, right)
    raise NotImplementedError(
        f"no live tensor-product backend is registered for {left} and {right}"
    )


def TensorSquare(obj):
    r"""Return the canonical tensor square ``obj tensor obj``."""
    return TensorProduct(obj, obj)


def Biproduct(left, right):
    r"""Return the categorical biproduct of ``left`` and ``right``."""
    if left.base_ring() != right.base_ring():
        raise ValueError("a biproduct requires one common base ring")
    from dzack_research.preamble.categories.modules.biproducts import (
        _module_biproduct,
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModules,
    )

    category = FinitelyPresentedModules(left.base_ring())
    if left in category and right in category:
        return _module_biproduct(left, right)
    raise NotImplementedError(
        f"no live biproduct backend is registered for {left} and {right}"
    )


def _common_module_ring(left, right):
    try:
        ring = left.base_ring()
    except AttributeError:
        return None
    if ring is None:
        return None
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    if left in Modules(ring) and right in Modules(ring):
        return ring
    return None


def Product(left, right):
    r"""Return the categorical binary product in the strongest represented category."""
    if _common_module_ring(left, right) is not None:
        return Biproduct(left, right)
    from dzack_research.preamble.categories.sets import CartesianProductOfSets, Sets

    if left in Sets() and right in Sets():
        return CartesianProductOfSets(left, right)
    raise NotImplementedError(f"no represented binary product backend for {left} and {right}")


def Coproduct(left, right):
    r"""Return the categorical binary coproduct in the strongest represented category."""
    if _common_module_ring(left, right) is not None:
        return Biproduct(left, right)
    from dzack_research.preamble.categories.sets import CoproductOfSets, Sets

    if left in Sets() and right in Sets():
        return CoproductOfSets(left, right)
    raise NotImplementedError(f"no represented binary coproduct backend for {left} and {right}")


def Kernel(morphism):
    r"""Return the categorical kernel represented by ``morphism``."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    domain = morphism.domain()
    codomain = morphism.codomain()
    if domain.base_ring() == codomain.base_ring() and domain in Modules(domain.base_ring()):
        return morphism.kernel()
    raise NotImplementedError(f"{morphism} has no live categorical kernel backend")


def Cokernel(morphism):
    r"""Return the categorical cokernel represented by ``morphism``."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    domain = morphism.domain()
    codomain = morphism.codomain()
    if domain.base_ring() == codomain.base_ring() and domain in Modules(domain.base_ring()):
        return morphism.cokernel()
    raise NotImplementedError(f"{morphism} has no live categorical cokernel backend")


def Subobjects(base_object, category=None):
    r"""Return ``Sub_C(base_object)`` in the stated category ``C``.

    When ``category`` is omitted, the object's current category is used.  This
    matters: subobjects of a module are module subobjects, not arbitrary
    subsets of its underlying set.
    """
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        SubobjectCategory,
    )

    base_category = base_object.category() if category is None else category
    if base_object not in base_category:
        raise TypeError("the subobject base must lie in the stated category")
    return SubobjectCategory(base_category, base_object)


__all__ = [
    "Biproduct",
    "Cokernel",
    "Coproduct",
    "Kernel",
    "Product",
    "Subobjects",
    "TensorProduct",
    "TensorSquare",
]
