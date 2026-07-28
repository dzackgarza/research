r"""``LatticeHomomorphisms`` — ZZ-module maps between integral lattices.

An embedding / projection / general morphism \(L\to M\) is an \(m\times n\)
matrix on the chosen bases.  Sage's ``Map.__call__`` on refined lattices
hits Cython coercion through facade elements and SIGSEGVs; own application
here by matrix action on coordinates (same pattern as
:class:`LatticeIsometries`).
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ


class LatticeHomomorphisms(Category):
    r"""Homomorphisms of integral lattices as free ZZ-module maps."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        # Modules(ZZ), not Sets(): refining FreeModuleMorphism into a Sets
        # subcategory segfaults in Sage's map dispatch on this stack.
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Homset construction: unwrap element facades before native Hom."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            """Build a morphism from images, a matrix, or an existing map."""
            from dzack_research.preamble.refine import unwrap, without_element_wrap

            with without_element_wrap():
                if isinstance(x, dict):
                    from dzack_research.preamble.categories.integral_lattices import (
                        expand_block_hom_dict,
                    )

                    ordered = expand_block_hom_dict(self.domain(), x)
                    return super().__call__(ordered, *args, **kwargs)  # type: ignore[misc]
                if isinstance(x, (list, tuple)) and x and not hasattr(x, "nrows"):
                    return super().__call__(  # type: ignore[misc]
                        [unwrap(img) for img in x], *args, **kwargs
                    )
                if hasattr(x, "nrows") and hasattr(x, "ncols"):
                    return super().__call__(matrix(ZZ, x), *args, **kwargs)  # type: ignore[misc]
                if hasattr(x, "matrix") and callable(x.matrix):
                    return super().__call__(  # type: ignore[misc]
                        matrix(ZZ, x.matrix()), *args, **kwargs
                    )
                return super().__call__(x, *args, **kwargs)  # type: ignore[misc]

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
