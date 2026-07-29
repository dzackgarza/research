r"""``LatticeHomomorphisms`` — form-preserving maps between integral lattices.

A morphism \(L\to M\) is an element of \(\operatorname{Hom}(L,M)\): a
\(\mathbb{Z}\)-linear map with \(I\,G_M\,I^{\mathsf T}=G_L\).  Construction
rejects anything that fails that identity; a non-form-preserving Hom is
impossible.  Sage's ``Map.__call__`` on refined lattices hits Cython
coercion through facade elements and SIGSEGVs; own application here by
matrix action on coordinates (same pattern as :class:`LatticeIsometries`).
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ


def _hom_images_from_dict(domain: Any, mapping: dict) -> list:
    if domain in DirectSumObjects():
        return _expand_direct_sum_hom_dict(domain, mapping)

    images = {
        unwrap(generator): unwrap(image)
        for generator, image in mapping.items()
    }
    ordered = []
    for generator in domain.gens():
        key = unwrap(generator)
        assert key in images, f"missing image for generator {generator}"
        ordered.append(images[key])
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
        r"""Homset construction: unwrap facades; reject non-form-preserving maps."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Build a form-preserving morphism from images, a matrix, or a map.

            For a chosen direct sum, a dictionary may specify images of entire
            summand subobjects.
            """
            domain = self.domain()
            codomain = self.codomain()
            with without_element_wrap():
                if isinstance(x, dict):
                    ordered = _hom_images_from_dict(domain, x)
                    morphism = super().__call__(ordered, *args, **kwargs)  # type: ignore[misc]
                elif isinstance(x, (list, tuple)) and x and not hasattr(x, "nrows"):
                    morphism = super().__call__(  # type: ignore[misc]
                        [unwrap(img) for img in x], *args, **kwargs
                    )
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
            return morphism

    class MorphismMethods:
        r"""Apply via coordinates × matrix — never Sage Map coercion."""

        def __call__(self: Any, x: Any) -> Any:
            """Apply this homomorphism on the owned element interface."""
            domain = self.domain()
            codomain = self.codomain()
            coords = domain.coordinate_vector(x)
            # Sage FreeModuleMorphism: row vector times matrix (m×n for m→n).
            return codomain((coords * self.matrix()).list())

        def _call_(self: Any, x: Any) -> Any:
            """Sage Map dispatch entry; same as :meth:`__call__`."""
            return self.__call__(x)
