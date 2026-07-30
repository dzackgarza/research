r"""``LatticeHomomorphisms`` — form-preserving maps between integral lattices.

A morphism \(L\to M\) is an element of \(\operatorname{Hom}(L,M)\): a
\(\mathbb{Z}\)-linear map with \(I\,G_M\,I^{\mathsf T}=G_L\).  Construction
rejects anything that fails that identity; a non-form-preserving Hom is
impossible.  Application is Sage's native morphism call — lattice elements
are genuine native vectors.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.cpython.type import can_assign_class
from sage.matrix.constructor import matrix
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.rings.integer_ring import ZZ


class LatticeMorphism(FreeModuleMorphism):
    r"""A form-preserving map $L\to M$ of lattices with generating sets.

    The category's owned morphism type, alongside its owned parents and
    elements.  Sage's ``FreeModuleHomspace`` hardcodes ``FreeModuleMorphism``
    when it builds a map, so the homset reassigns the class of what it produced
    -- the same ``__class__`` move override-refine makes, and legitimate for the
    same reason: these are heap types with no extra layout.
    """


def _hom_images_from_dict(domain: Any, mapping: dict) -> list:
    if domain in DirectSumObjects():
        return _expand_direct_sum_hom_dict(domain, mapping)

    images = dict(mapping)
    ordered = []
    for generator in domain.gens():
        assert generator in images, f"missing image for generator {generator}"
        ordered.append(images[generator])
    return ordered


class LatticeHomomorphisms(Category):
    r"""Form-preserving homomorphisms of integral lattices."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        # Modules(ZZ), not Sets(): refining FreeModuleMorphism into a Sets
        # subcategory segfaults in Sage's map dispatch on this stack.
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Homset construction: reject non-form-preserving maps."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Build a form-preserving morphism from images, a matrix, or a map.

            For a chosen direct sum, a dictionary may specify images of entire
            summand subobjects.
            """
            domain = self.domain()
            codomain = self.codomain()
            if isinstance(x, dict):
                ordered = _hom_images_from_dict(domain, x)
                morphism = super().__call__(ordered, *args, **kwargs)  # type: ignore[misc]
            elif isinstance(x, (list, tuple)) and x and not hasattr(x, "nrows"):
                morphism = super().__call__(list(x), *args, **kwargs)  # type: ignore[misc]
            elif hasattr(x, "nrows") and hasattr(x, "ncols"):
                morphism = super().__call__(matrix(ZZ, x), *args, **kwargs)  # type: ignore[misc]
            elif hasattr(x, "matrix") and callable(x.matrix):
                morphism = super().__call__(  # type: ignore[misc]
                    matrix(ZZ, x.matrix()), *args, **kwargs
                )
            else:
                morphism = super().__call__(x, *args, **kwargs)  # type: ignore[misc]

            mat = matrix(ZZ, morphism.matrix())
            assert mat.nrows() == domain.rank() and mat.ncols() == codomain.rank(), (
                f"homomorphism matrix shape {mat.nrows()}×{mat.ncols()} "
                f"does not match ranks {domain.rank()}→{codomain.rank()}"
            )
            assert mat * codomain.gram_matrix() * mat.transpose() == domain.gram_matrix(), (
                "matrix does not preserve the Gram form: I G_M I^T != G_L"
            )
            assert can_assign_class(morphism), (
                f"cannot own the type of {type(morphism).__name__}; a lattice "
                "morphism must be a heap type"
            )
            morphism.__class__ = LatticeMorphism
            return morphism
