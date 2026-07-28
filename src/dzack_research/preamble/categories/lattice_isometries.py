r"""``LatticeIsometries`` — morphisms of integral lattices that preserve the form.

``L.Aut()`` is the isometry Homset.  Its element constructor takes a dict of
generator images ``{e_i: image}`` (or a list of images / a matrix); isometry
is checked on ``morphism.to_matrix()``.

Invariant / coinvariant lattices live on the lattice
(``L.invariant_lattice(action)``, ``L.coinvariant_lattice(action)``);
morphisms delegate to their domain.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.rings.integer_ring import ZZ


class LatticeIsometries(Category):
    r"""Isometries of integral lattices (as Hom morphisms / Aut elements)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice isometries"

    def super_categories(self) -> list:
        # Modules(ZZ), not Sets(): refining FreeModuleMorphism into a Sets
        # subcategory segfaults in Sage's map dispatch on this stack.
        return [Modules(ZZ)]

    class ParentMethods:
        r"""Homset methods: element construction is the isometry constructor."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            """Construct an isometry from ``{generator: image}``, images, or a matrix."""
            from dzack_research.preamble.refine import unwrap, without_element_wrap

            domain = self.domain()
            codomain = self.codomain()

            with without_element_wrap():
                if isinstance(x, dict):
                    from dzack_research.preamble.categories.integral_lattices import (
                        expand_block_hom_dict,
                    )

                    ordered = expand_block_hom_dict(domain, x)
                    morphism = super().__call__(ordered, *args, **kwargs)  # type: ignore[misc]
                elif isinstance(x, (list, tuple)) and x and not hasattr(x, "nrows"):
                    morphism = super().__call__(  # type: ignore[misc]
                        [unwrap(img) for img in x], *args, **kwargs
                    )
                elif hasattr(x, "nrows") and hasattr(x, "ncols"):
                    # Matrix input (Sage matrices also have a misleading to_matrix).
                    morphism = super().__call__(matrix(ZZ, x), *args, **kwargs)  # type: ignore[misc]
                elif hasattr(x, "domain") and hasattr(x, "to_matrix") and callable(
                    x.to_matrix
                ):
                    morphism = super().__call__(  # type: ignore[misc]
                        matrix(ZZ, x.to_matrix()), *args, **kwargs
                    )
                elif (
                    hasattr(x, "domain")
                    and hasattr(x, "matrix")
                    and callable(x.matrix)
                ):
                    morphism = super().__call__(  # type: ignore[misc]
                        matrix(ZZ, x.matrix()), *args, **kwargs
                    )
                else:
                    morphism = super().__call__(matrix(ZZ, x), *args, **kwargs)  # type: ignore[misc]

            mat = matrix(ZZ, morphism.matrix())
            assert mat.nrows() == domain.rank() and mat.ncols() == domain.rank(), (
                f"isometry matrix shape {mat.nrows()}×{mat.ncols()} "
                f"does not match domain rank {domain.rank()}"
            )
            assert mat.nrows() == codomain.rank(), (
                f"isometry matrix does not match codomain rank {codomain.rank()}"
            )
            gram_domain = domain.gram_matrix()
            gram_codomain = codomain.gram_matrix()
            assert mat.transpose() * gram_codomain * mat == gram_domain, (
                "matrix does not preserve the Gram form: I^T G_M I != G_L"
            )
            if domain is codomain:
                assert mat.det() in (ZZ(1), ZZ(-1)), (
                    f"automorphism matrix must have determinant ±1, got {mat.det()}"
                )
            return morphism

    class MorphismMethods:
        r"""Methods on isometries refined into this category.

        Sage's ``Map.is_identity`` / composition on ``FreeModuleMorphism``
        segfault once the domain lattice has been override-refined; own those
        operations here via matrices.
        """

        def to_matrix(self: Any) -> Any:
            """Return the matrix of this isometry on the domain basis."""
            return self.matrix()

        def is_identity(self: Any) -> bool:
            """Return whether this isometry is the identity (matrix test)."""
            mat = self.to_matrix()
            return bool(mat == identity_matrix(ZZ, mat.nrows()))

        def is_involution(self: Any) -> bool:
            r"""Return whether $I^{2}=\mathrm{id}$."""
            return (self * self).is_identity()

        def __mul__(self: Any, other: Any) -> Any:
            """Compose isometries by matrix product through the Homset."""
            if not hasattr(other, "to_matrix") and not hasattr(other, "matrix"):
                return NotImplemented
            other_mat = other.to_matrix() if hasattr(other, "to_matrix") else other.matrix()
            return self.parent()(self.to_matrix() * other_mat)

        def __call__(self: Any, x: Any) -> Any:
            """Apply the isometry on the owned element interface."""
            # Row-vector action (Sage FreeModuleMorphism convention): c * A.
            # Left-multiply by A would only accidentally work for square
            # symmetric Aut matrices; embeddings need c * A.
            domain = self.domain()
            codomain = self.codomain()
            coords = domain.coordinate_vector(x)
            return codomain((coords * self.to_matrix()).list())

        def _call_(self: Any, x: Any) -> Any:
            """Sage Map dispatch entry; same as :meth:`__call__`."""
            return self.__call__(x)

        def invariant_lattice(self: Any) -> Any:
            r"""Return $L^{+}=L^{\langle I\rangle}$ via the domain lattice."""
            return self.domain().invariant_lattice(self)

        def coinvariant_lattice(self: Any) -> Any:
            r"""Return the coinvariant lattice via the domain lattice."""
            return self.domain().coinvariant_lattice(self)

        def coinvariant_inclusion(self: Any) -> Any:
            r"""Return the coinvariant inclusion via the domain lattice."""
            return self.domain().coinvariant_inclusion(self)
